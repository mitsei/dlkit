"""Unit tests of assessment objects."""


import datetime
import pytest


from decimal import Decimal


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.assessment import objects as ABCObjects
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.assessment.objects import Assessment
from dlkit.json_.assessment.objects import AssessmentOffered
from dlkit.json_.assessment.objects import AssessmentTaken
from dlkit.json_.assessment.objects import Question, AnswerList
from dlkit.json_.id.objects import IdList
from dlkit.json_.learning.objects import ObjectiveList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type
from dlkit.records import registry
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
SEQUENCE_ASSESSMENT = Type(**registry.ASSESSMENT_RECORD_TYPES["simple-child-sequencing"])


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def question_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        item_form = request.cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        request.cls.item = request.cls.catalog.create_item(item_form)

        form = request.cls.catalog.get_question_form_for_create(request.cls.item.ident, [])
        form.display_name = 'Test question'
        request.cls.question = request.cls.catalog.create_question(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def question_test_fixture(request):
    request.cls.object = request.cls.question


@pytest.mark.usefixtures("question_class_fixture", "question_test_fixture")
class TestQuestion(object):
    """Tests for Question"""
    def test_get_question_record(self):
        """Tests get_question_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_question_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def question_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        item_form = request.cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        request.cls.item = request.cls.catalog.create_item(item_form)

        request.cls.form = request.cls.catalog.get_question_form_for_create(request.cls.item.ident, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def question_form_test_fixture(request):
    pass


@pytest.mark.usefixtures("question_form_class_fixture", "question_form_test_fixture")
class TestQuestionForm(object):
    """Tests for QuestionForm"""
    def test_get_question_form_record(self):
        """Tests get_question_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_question_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def question_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for QuestionList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def question_list_test_fixture(request):
    from dlkit.json_.assessment.objects import QuestionList
    request.cls.question_list = list()
    request.cls.question_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            item_form = request.cls.catalog.get_item_form_for_create([])
            item_form.display_name = 'Item'
            item = request.cls.catalog.create_item(item_form)

            create_form = request.cls.catalog.get_question_form_for_create(item.ident, [])
            create_form.display_name = 'Test Question ' + str(num)
            create_form.description = 'Test Question for QuestionList tests'
            obj = request.cls.catalog.create_question(create_form)
            request.cls.question_list.append(obj)
            request.cls.question_ids.append(obj.ident)
    request.cls.question_list = QuestionList(request.cls.question_list)


@pytest.mark.usefixtures("question_list_class_fixture", "question_list_test_fixture")
class TestQuestionList(object):
    """Tests for QuestionList"""
    def test_get_next_question(self):
        """Tests get_next_question"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Question
        if not is_never_authz(self.service_config):
            assert isinstance(self.question_list.get_next_question(), Question)

    def test_get_next_questions(self):
        """Tests get_next_questions"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import QuestionList, Question
        if not is_never_authz(self.service_config):
            new_list = self.question_list.get_next_questions(2)
            assert isinstance(new_list, QuestionList)
            for item in new_list:
                assert isinstance(item, Question)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def answer_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        item_form = request.cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        request.cls.item = request.cls.catalog.create_item(item_form)

        form = request.cls.catalog.get_answer_form_for_create(request.cls.item.ident, [])
        form.display_name = 'Test answer'
        request.cls.answer = request.cls.catalog.create_answer(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def answer_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.answer


@pytest.mark.usefixtures("answer_class_fixture", "answer_test_fixture")
class TestAnswer(object):
    """Tests for Answer"""
    def test_get_answer_record(self):
        """Tests get_answer_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_answer_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def answer_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        item_form = request.cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        request.cls.item = request.cls.catalog.create_item(item_form)

        request.cls.form = request.cls.catalog.get_answer_form_for_create(request.cls.item.ident, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def answer_form_test_fixture(request):
    pass


@pytest.mark.usefixtures("answer_form_class_fixture", "answer_form_test_fixture")
class TestAnswerForm(object):
    """Tests for AnswerForm"""
    def test_get_answer_form_record(self):
        """Tests get_answer_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_answer_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def answer_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AnswerList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def answer_list_test_fixture(request):
    from dlkit.json_.assessment.objects import AnswerList
    request.cls.answer_list = list()
    request.cls.answer_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            item_form = request.cls.catalog.get_item_form_for_create([])
            item_form.display_name = 'Item'
            item = request.cls.catalog.create_item(item_form)

            create_form = request.cls.catalog.get_answer_form_for_create(item.ident, [])
            create_form.display_name = 'Test Answer ' + str(num)
            create_form.description = 'Test Answer for AnswerList tests'
            obj = request.cls.catalog.create_answer(create_form)
            request.cls.answer_list.append(obj)
            request.cls.answer_ids.append(obj.ident)
    request.cls.answer_list = AnswerList(request.cls.answer_list)


@pytest.mark.usefixtures("answer_list_class_fixture", "answer_list_test_fixture")
class TestAnswerList(object):
    """Tests for AnswerList"""
    def test_get_next_answer(self):
        """Tests get_next_answer"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Answer
        if not is_never_authz(self.service_config):
            assert isinstance(self.answer_list.get_next_answer(), Answer)

    def test_get_next_answers(self):
        """Tests get_next_answers"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AnswerList, Answer
        if not is_never_authz(self.service_config):
            new_list = self.answer_list.get_next_answers(2)
            assert isinstance(new_list, AnswerList)
            for item in new_list:
                assert isinstance(item, Answer)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.lsvc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.lsvc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test objective bank'
        create_form.description = 'Test objective bank description'
        request.cls.bank = request.cls.lsvc_mgr.create_objective_bank(create_form)
        request.cls.objectives = list()
        for _ in range(2):
            form = request.cls.bank.get_objective_form_for_create([])
            objective = request.cls.bank.create_objective(form)
            request.cls.objectives.append(objective)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

            for obj in request.cls.bank.get_objectives():
                request.cls.bank.delete_objective(obj.ident)
            request.cls.lsvc_mgr.delete_objective_bank(request.cls.bank.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_item_form_for_create([])
        form.display_name = 'Test object'
        form.set_learning_objectives([request.cls.objectives[0].ident,
                                      request.cls.objectives[1].ident])
        request.cls.item = request.cls.catalog.create_item(form)

        form = request.cls.catalog.get_question_form_for_create(request.cls.item.ident, [])
        request.cls.catalog.create_question(form)

        form = request.cls.catalog.get_answer_form_for_create(request.cls.item.ident, [])
        form.set_genus_type(Type('answer-genus%3Aright-answer%40ODL.MIT.EDU'))
        request.cls.catalog.create_answer(form)

        request.cls.item = request.cls.catalog.get_item(request.cls.item.ident)
        request.cls.object = request.cls.item


@pytest.mark.usefixtures("item_class_fixture", "item_test_fixture")
class TestItem(object):
    """Tests for Item"""
    def test_get_learning_objective_ids(self):
        """Tests get_learning_objective_ids"""
        if not is_never_authz(self.service_config):
            lo_ids = self.item.get_learning_objective_ids()
            assert isinstance(lo_ids, IdList)
            assert lo_ids.available() == 2
            assert str(next(lo_ids)) == str(self.objectives[0].ident)
            assert str(next(lo_ids)) == str(self.objectives[1].ident)

    def test_get_learning_objectives(self):
        """Tests get_learning_objectives"""
        if not is_never_authz(self.service_config):
            los = self.item.get_learning_objectives()
            assert isinstance(los, ObjectiveList)
            assert los.available() == 2
            assert str(next(los).ident) == str(self.objectives[0].ident)
            assert str(next(los).ident) == str(self.objectives[1].ident)

    def test_get_question_id(self):
        """Tests get_question_id"""
        if not is_never_authz(self.service_config):
            question_id = self.item.get_question_id()
            assert isinstance(question_id, Id)
            assert str(question_id) == str(self.item.ident)

    def test_get_question(self):
        """Tests get_question"""
        if not is_never_authz(self.service_config):
            question = self.item.get_question()
            assert isinstance(question, Question)
            assert str(question.ident) == str(self.item.ident)

    def test_get_answer_ids(self):
        """Tests get_answer_ids"""
        if not is_never_authz(self.service_config):
            answer_ids = self.item.get_answer_ids()
            assert isinstance(answer_ids, IdList)
            assert answer_ids.available() == 1

    def test_get_answers(self):
        """Tests get_answers"""
        if not is_never_authz(self.service_config):
            answers = self.item.get_answers()
            assert isinstance(answers, AnswerList)
            assert answers.available() == 1
            assert str(next(answers).genus_type) == 'answer-genus%3Aright-answer%40ODL.MIT.EDU'

    def test_get_item_record(self):
        """Tests get_item_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_item_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def item_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_item_form_for_create([])


@pytest.mark.usefixtures("item_form_class_fixture", "item_form_test_fixture")
class TestItemForm(object):
    """Tests for ItemForm"""
    def test_get_learning_objectives_metadata(self):
        """Tests get_learning_objectives_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.form.get_learning_objectives_metadata(), Metadata)

    def test_set_learning_objectives(self):
        """Tests set_learning_objectives"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_learning_objectives([test_id])
            assert len(self.form._my_map['learningObjectiveIds']) == 1
            assert self.form._my_map['learningObjectiveIds'][0] == str(test_id)
            with pytest.raises(errors.InvalidArgument):
                self.form.set_learning_objectives('this is not a list')
            # reset this for other tests
            self.form._my_map['learningObjectiveIds'] = list()

    def test_clear_learning_objectives(self):
        """Tests clear_learning_objectives"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
            self.form.set_learning_objectives([test_id])
            assert len(self.form._my_map['learningObjectiveIds']) == 1
            assert self.form._my_map['learningObjectiveIds'][0] == str(test_id)
            self.form.clear_learning_objectives()
            assert self.form._my_map['learningObjectiveIds'] == []

    def test_get_item_form_record(self):
        """Tests get_item_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_item_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.assessment.objects import ItemList
    request.cls.item_list = list()
    request.cls.item_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemList tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)
    request.cls.item_list = ItemList(request.cls.item_list)
    request.cls.object = request.cls.item_list


@pytest.mark.usefixtures("item_list_class_fixture", "item_list_test_fixture")
class TestItemList(object):
    """Tests for ItemList"""
    def test_get_next_item(self):
        """Tests get_next_item"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Item
        if not is_never_authz(self.service_config):
            assert isinstance(self.item_list.get_next_item(), Item)

    def test_get_next_items(self):
        """Tests get_next_items"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import ItemList, Item
        if not is_never_authz(self.service_config):
            new_list = self.item_list.get_next_items(2)
            assert isinstance(new_list, ItemList)
            for item in new_list:
                assert isinstance(item, Item)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        form = request.cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_assessment(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_class_fixture", "assessment_test_fixture")
class TestAssessment(object):
    """Tests for Assessment"""
    def test_get_level_id(self):
        """Tests get_level_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_level_id)

    def test_get_level(self):
        """Tests get_level"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_level)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # From test_templates/resources.py::Resource::has_avatar_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_rubric(), bool)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_rubric)

    def test_get_assessment_record(self):
        """Tests get_assessment_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_assessment_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def assessment_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_assessment_form_for_create([])


@pytest.mark.usefixtures("assessment_form_class_fixture", "assessment_form_test_fixture")
class TestAssessmentForm(object):
    """Tests for AssessmentForm"""
    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_level_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_level(self):
        """Tests set_level"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['levelId'] == ''
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['levelId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_level(True)

    def test_clear_level(self):
        """Tests clear_level"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['levelId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_level()
        assert self.form._my_map['levelId'] == self.form.get_level_metadata().get_default_id_values()[0]

    def test_get_rubric_metadata(self):
        """Tests get_rubric_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_rubric_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_rubric(self):
        """Tests set_rubric"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['rubricId'] == ''
        self.form.set_rubric(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['rubricId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_rubric(True)

    def test_clear_rubric(self):
        """Tests clear_rubric"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_rubric(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['rubricId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_rubric()
        assert self.form._my_map['rubricId'] == self.form.get_rubric_metadata().get_default_id_values()[0]

    def test_get_assessment_form_record(self):
        """Tests get_assessment_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_assessment_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.assessment.objects import AssessmentList
    request.cls.assessment_list = list()
    request.cls.assessment_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentList tests'
            obj = request.cls.catalog.create_assessment(create_form)
            request.cls.assessment_list.append(obj)
            request.cls.assessment_ids.append(obj.ident)
    request.cls.assessment_list = AssessmentList(request.cls.assessment_list)
    request.cls.object = request.cls.assessment_list


@pytest.mark.usefixtures("assessment_list_class_fixture", "assessment_list_test_fixture")
class TestAssessmentList(object):
    """Tests for AssessmentList"""
    def test_get_next_assessment(self):
        """Tests get_next_assessment"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Assessment
        if not is_never_authz(self.service_config):
            assert isinstance(self.assessment_list.get_next_assessment(), Assessment)

    def test_get_next_assessments(self):
        """Tests get_next_assessments"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList, Assessment
        if not is_never_authz(self.service_config):
            new_list = self.assessment_list.get_next_assessments(2)
            assert isinstance(new_list, AssessmentList)
            for item in new_list:
                assert isinstance(item, Assessment)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        form = request.cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Assessment'
        request.cls.assessment = request.cls.catalog.create_assessment(form)

        form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        form.set_start_time(DateTime.utcnow())
        form.set_duration(Duration(hours=1))
        deadline = DateTime.utcnow() + datetime.timedelta(days=4)
        form.set_deadline(DateTime(year=deadline.year,
                                   month=deadline.month,
                                   day=deadline.day,
                                   hour=deadline.hour,
                                   minute=deadline.minute,
                                   second=deadline.second,
                                   microsecond=deadline.microsecond))
        request.cls.object = request.cls.catalog.create_assessment_offered(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_offered_class_fixture", "assessment_offered_test_fixture")
class TestAssessmentOffered(object):
    """Tests for AssessmentOffered"""
    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_assessment_id(), Id)
            assert str(self.object.get_assessment_id()) == str(self.assessment.ident)

    def test_get_assessment(self):
        """Tests get_assessment"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_assessment(), Assessment)
            assert str(self.object.get_assessment().ident) == str(self.assessment.ident)

    def test_get_level_id(self):
        """Tests get_level_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_level_id)

    def test_get_level(self):
        """Tests get_level"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_level)

    def test_are_items_sequential(self):
        """Tests are_items_sequential"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.are_items_sequential(), bool)

    def test_are_items_shuffled(self):
        """Tests are_items_shuffled"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.are_items_shuffled(), bool)

    def test_has_start_time(self):
        """Tests has_start_time"""
        # From test_templates/repository.py::AssetContent::has_url_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_start_time(), bool)

    def test_get_start_time(self):
        """Tests get_start_time"""
        # From test_templates/assessment.py::AssessmentOffered::get_start_time_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_start_time(), DateTime)

    def test_has_deadline(self):
        """Tests has_deadline"""
        # From test_templates/repository.py::AssetContent::has_url_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_deadline(), bool)

    def test_get_deadline(self):
        """Tests get_deadline"""
        # From test_templates/assessment.py::AssessmentOffered::get_start_time_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_start_time(), DateTime)

    def test_has_duration(self):
        """Tests has_duration"""
        # From test_templates/repository.py::AssetContent::has_url_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_duration(), bool)

    def test_get_duration(self):
        """Tests get_duration"""
        # From test_templates/assessment.py::AssessmentOffered::get_duration_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_duration(), Duration)

    def test_is_scored(self):
        """Tests is_scored"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scored?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.is_scored)

    def test_get_score_system_id(self):
        """Tests get_score_system_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_score_system_id)

    def test_get_score_system(self):
        """Tests get_score_system"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_score_system)

    def test_is_graded(self):
        """Tests is_graded"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set graded?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.is_graded)

    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_grade_system_id)

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_grade_system)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.has_rubric)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_rubric)

    def test_get_assessment_offered_record(self):
        """Tests get_assessment_offered_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_assessment_offered_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)

        request.cls.form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident,
                                                                                      [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident,
                                                                                      [])


@pytest.mark.usefixtures("assessment_offered_form_class_fixture", "assessment_offered_form_test_fixture")
class TestAssessmentOfferedForm(object):
    """Tests for AssessmentOfferedForm"""
    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_level_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_level(self):
        """Tests set_level"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['levelId'] == ''
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['levelId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_level(True)

    def test_clear_level(self):
        """Tests clear_level"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['levelId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_level()
        assert self.form._my_map['levelId'] == self.form.get_level_metadata().get_default_id_values()[0]

    def test_get_items_sequential_metadata(self):
        """Tests get_items_sequential_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_items_sequential_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_items_sequential(self):
        """Tests set_items_sequential"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_items_sequential(True)
        assert self.form._my_map['itemsSequential']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_items_sequential('false')

    def test_clear_items_sequential(self):
        """Tests clear_items_sequential"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_items_sequential(True)
        assert self.form._my_map['itemsSequential']
        self.form.clear_items_sequential()
        assert self.form._my_map['itemsSequential'] is None

    def test_get_items_shuffled_metadata(self):
        """Tests get_items_shuffled_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_items_shuffled_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_items_shuffled(self):
        """Tests set_items_shuffled"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_items_shuffled(True)
        assert self.form._my_map['itemsShuffled']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_items_shuffled('false')

    def test_clear_items_shuffled(self):
        """Tests clear_items_shuffled"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_items_shuffled(True)
        assert self.form._my_map['itemsShuffled']
        self.form.clear_items_shuffled()
        assert self.form._my_map['itemsShuffled'] is None

    def test_get_start_time_metadata(self):
        """Tests get_start_time_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_start_time_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DATETIME'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_start_time(self):
        """Tests set_start_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['startTime'] is None
            self.form.set_start_time(test_time)
            assert self.form._my_map['startTime'] == test_time
            with pytest.raises(errors.InvalidArgument):
                self.form.set_start_time(True)
            # reset this for other tests
            self.form._my_map['startTime'] = None

    def test_clear_start_time(self):
        """Tests clear_start_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['startTime'] is None
            self.form.set_start_time(test_time)
            assert self.form._my_map['startTime'] == test_time
            self.form.clear_start_time()
            assert self.form._my_map['startTime'] == self.form.get_start_time_metadata().get_default_date_time_values()[0]

    def test_get_deadline_metadata(self):
        """Tests get_deadline_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_deadline_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DATETIME'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_deadline(self):
        """Tests set_deadline"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['deadline'] is None
            self.form.set_deadline(test_time)
            assert self.form._my_map['deadline'] == test_time
            with pytest.raises(errors.InvalidArgument):
                self.form.set_deadline(True)
            # reset this for other tests
            self.form._my_map['deadline'] = None

    def test_clear_deadline(self):
        """Tests clear_deadline"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_start_time_template
        if not is_never_authz(self.service_config):
            test_time = DateTime.utcnow()
            assert self.form._my_map['deadline'] is None
            self.form.set_deadline(test_time)
            assert self.form._my_map['deadline'] == test_time
            self.form.clear_deadline()
            assert self.form._my_map['deadline'] == self.form.get_deadline_metadata().get_default_date_time_values()[0]

    def test_get_duration_metadata(self):
        """Tests get_duration_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_duration_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DURATION'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_duration(self):
        """Tests set_duration"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_duration_template
        if not is_never_authz(self.service_config):
            test_duration = Duration(hours=1)
            assert self.form._my_map['duration'] is None
            self.form.set_duration(test_duration)
            assert self.form._my_map['duration']['seconds'] == 3600
            assert self.form._my_map['duration']['days'] == 0
            assert self.form._my_map['duration']['microseconds'] == 0
            with pytest.raises(errors.InvalidArgument):
                self.form.set_duration(1.05)
            # reset this for other tests
            self.form._my_map['duration'] = None

    def test_clear_duration(self):
        """Tests clear_duration"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_duration_template
        if not is_never_authz(self.service_config):
            test_duration = Duration(hours=1)
            assert self.form._my_map['duration'] is None
            self.form.set_duration(test_duration)
            assert self.form._my_map['duration']['seconds'] == 3600
            assert self.form._my_map['duration']['days'] == 0
            assert self.form._my_map['duration']['microseconds'] == 0
            self.form.clear_duration()
            assert self.form._my_map['duration'] == self.form.get_duration_metadata().get_default_duration_values()[0]

    def test_get_score_system_metadata(self):
        """Tests get_score_system_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_score_system_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_score_system(self):
        """Tests set_score_system"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['scoreSystemId'] == ''
        self.form.set_score_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['scoreSystemId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_score_system(True)

    def test_clear_score_system(self):
        """Tests clear_score_system"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_score_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['scoreSystemId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_score_system()
        assert self.form._my_map['scoreSystemId'] == self.form.get_score_system_metadata().get_default_id_values()[0]

    def test_get_grade_system_metadata(self):
        """Tests get_grade_system_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_grade_system_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_grade_system(self):
        """Tests set_grade_system"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['gradeSystemId'] == ''
        self.form.set_grade_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['gradeSystemId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_grade_system(True)

    def test_clear_grade_system(self):
        """Tests clear_grade_system"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_grade_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['gradeSystemId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_grade_system()
        assert self.form._my_map['gradeSystemId'] == self.form.get_grade_system_metadata().get_default_id_values()[0]

    def test_get_assessment_offered_form_record(self):
        """Tests get_assessment_offered_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_assessment_offered_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedList tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)

        request.cls.form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident,
                                                                                      [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_list_test_fixture(request):
    from dlkit.json_.assessment.objects import AssessmentOfferedList
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident,
                                                                              [])
            form.display_name = 'Test AssessmentOffered ' + str(num)
            form.description = 'Test AssessmentOffered for AssessmentOfferedList tests'
            obj = request.cls.catalog.create_assessment_offered(form)
            request.cls.assessment_offered_list.append(obj)
            request.cls.assessment_offered_ids.append(obj.ident)
    request.cls.assessment_offered_list = AssessmentOfferedList(request.cls.assessment_offered_list)


@pytest.mark.usefixtures("assessment_offered_list_class_fixture", "assessment_offered_list_test_fixture")
class TestAssessmentOfferedList(object):
    """Tests for AssessmentOfferedList"""
    def test_get_next_assessment_offered(self):
        """Tests get_next_assessment_offered"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOffered
        if not is_never_authz(self.service_config):
            assert isinstance(self.assessment_offered_list.get_next_assessment_offered(), AssessmentOffered)

    def test_get_next_assessments_offered(self):
        """Tests get_next_assessments_offered"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList, AssessmentOffered
        if not is_never_authz(self.service_config):
            new_list = self.assessment_offered_list.get_next_assessments_offered(2)
            assert isinstance(new_list, AssessmentOfferedList)
            for item in new_list:
                assert isinstance(item, AssessmentOffered)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        form = request.cls.catalog.get_assessment_form_for_create([SEQUENCE_ASSESSMENT])
        form.display_name = 'Assessment'
        request.cls.assessment = request.cls.catalog.create_assessment(form)

        form = request.cls.catalog.get_item_form_for_create([])
        form.display_name = 'Test item'
        request.cls.item = request.cls.catalog.create_item(form)

        form = request.cls.catalog.get_question_form_for_create(request.cls.item.ident, [])
        request.cls.catalog.create_question(form)
        request.cls.item = request.cls.catalog.get_item(request.cls.item.ident)

        request.cls.catalog.add_item(request.cls.assessment.ident, request.cls.item.ident)
        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)

        form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        request.cls.offered = request.cls.catalog.create_assessment_offered(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.offered.ident,
                                                                        [])
        request.cls.object = request.cls.catalog.create_assessment_taken(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_assessment_taken(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_taken_class_fixture", "assessment_taken_test_fixture")
class TestAssessmentTaken(object):
    """Tests for AssessmentTaken"""
    def test_get_assessment_offered_id(self):
        """Tests get_assessment_offered_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_assessment_offered_id(), Id)
            assert str(self.object.get_assessment_offered_id()) == str(self.offered.ident)

    def test_get_assessment_offered(self):
        """Tests get_assessment_offered"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_assessment_offered(), AssessmentOffered)
            assert str(self.object.get_assessment_offered().ident) == str(self.offered.ident)

    def test_get_taker_id(self):
        """Tests get_taker_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_taker_id(), Id)
            assert str(self.object.get_taker_id()) == str(self.catalog._proxy.get_effective_agent_id())

    def test_get_taker(self):
        """Tests get_taker"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.object.get_taker()

    def test_get_taking_agent_id(self):
        """Tests get_taking_agent_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_taking_agent_id(), Id)
            assert str(self.object.get_taking_agent_id()) == str(self.catalog._proxy.get_effective_agent_id())

    def test_get_taking_agent(self):
        """Tests get_taking_agent"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.object.get_taking_agent()

    def test_has_started(self):
        """Tests has_started"""
        # tests if the assessment has begun
        if not is_never_authz(self.service_config):
            assert self.object.has_started()

    def test_get_actual_start_time(self):
        """Tests get_actual_start_time"""
        # tests if the taker has started the assessment
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.actual_start_time
            # Also test the other branches of this method
            form = self.catalog.get_assessment_taken_form_for_create(self.offered.ident,
                                                                     [])
            taken = self.catalog.create_assessment_taken(form)
            section = self.catalog.get_first_assessment_section(taken.ident)
            section.get_questions()
            taken = self.catalog.get_assessment_taken(taken.ident)
            assert isinstance(taken.actual_start_time, DateTime)
            self.catalog.delete_assessment_taken(taken.ident)

    def test_has_ended(self):
        """Tests has_ended"""
        # tests if the assessment is over
        if not is_never_authz(self.service_config):
            assert not self.object.has_ended()

    def test_get_completion_time(self):
        """Tests get_completion_time"""
        # tests if the taker has "finished" the assessment
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.completion_time
            # Also test the other branches of this method
            form = self.catalog.get_assessment_taken_form_for_create(self.offered.ident,
                                                                     [])
            taken = self.catalog.create_assessment_taken(form)
            section = self.catalog.get_first_assessment_section(taken.ident)
            section.get_questions()

            self.catalog.finish_assessment(taken.ident)

            taken = self.catalog.get_assessment_taken(taken.ident)
            assert isinstance(taken.completion_time, DateTime)
            self.catalog.delete_assessment_taken(taken.ident)

    def test_get_time_spent(self):
        """Tests get_time_spent"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.time_spent
            # Also test the other branches of this method
            form = self.catalog.get_assessment_taken_form_for_create(self.offered.ident,
                                                                     [])
            taken = self.catalog.create_assessment_taken(form)
            section = self.catalog.get_first_assessment_section(taken.ident)
            section.get_questions()

            self.catalog.finish_assessment(taken.ident)
            taken = self.catalog.get_assessment_taken(taken.ident)
            assert isinstance(taken.time_spent, datetime.timedelta)
            self.catalog.delete_assessment_taken(taken.ident)

    def test_get_completion(self):
        """Tests get_completion"""
        # From test_templates/assessment.py::AssessmentTaken::get_completion_template
        # Our implementation is probably wrong -- there is no "completion" setter
        # in the form / spec...so unclear how the value gets here.
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_completion)

    def test_is_scored(self):
        """Tests is_scored"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scored?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.is_scored)

    def test_get_score_system_id(self):
        """Tests get_score_system_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scoreSystemId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_score_system_id)

    def test_get_score_system(self):
        """Tests get_score_system"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scoreSystemId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_score_system)

    def test_get_score(self):
        """Tests get_score"""
        # From test_templates/assessment.py::AssessmentTaken::get_score_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_score(), Decimal)
            assert self.object.get_score() == Decimal(0.0)

    def test_is_graded(self):
        """Tests is_graded"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set graded?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.is_graded)

    def test_get_grade_id(self):
        """Tests get_grade_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_grade_id)

    def test_get_grade(self):
        """Tests get_grade"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_grade)

    def test_get_feedback(self):
        """Tests get_feedback"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set feedback?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_feedback)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.has_rubric)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        if not is_never_authz(self.service_config):
            pytest.raises(KeyError,
                          self.object.get_rubric)

    def test_get_assessment_taken_record(self):
        """Tests get_assessment_taken_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_assessment_taken_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenForm tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenForm tests'
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(create_form)

        request.cls.form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_form_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_taken_form_class_fixture", "assessment_taken_form_test_fixture")
class TestAssessmentTakenForm(object):
    """Tests for AssessmentTakenForm"""
    def test_get_taker_metadata(self):
        """Tests get_taker_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_taker_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_taker(self):
        """Tests set_taker"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['takerId'] == ''
        self.form.set_taker(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['takerId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_taker(True)

    def test_clear_taker(self):
        """Tests clear_taker"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_taker(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['takerId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_taker()
        assert self.form._my_map['takerId'] == self.form.get_taker_metadata().get_default_id_values()[0]

    def test_get_assessment_taken_form_record(self):
        """Tests get_assessment_taken_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_assessment_taken_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenList tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)

        form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident,
                                                                          [])
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(form)

        request.cls.form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident,
                                                                                    [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_taken():
                request.cls.catalog.delete_assessment_taken(obj.ident)
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_list_test_fixture(request):
    from dlkit.json_.assessment.objects import AssessmentTakenList
    request.cls.assessment_taken_list = list()
    request.cls.assessment_taken_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident,
                                                                              [])
            form.display_name = 'Test AssessmentOffered ' + str(num)
            form.description = 'Test AssessmentOffered for AssessmentTakenList tests'
            obj = request.cls.catalog.create_assessment_offered(form)

            form = request.cls.catalog.get_assessment_taken_form_for_create(obj.ident, [])
            obj = request.cls.catalog.create_assessment_taken(form)
            request.cls.assessment_taken_list.append(obj)
            request.cls.assessment_taken_ids.append(obj.ident)
    request.cls.assessment_taken_list = AssessmentTakenList(request.cls.assessment_taken_list)


@pytest.mark.usefixtures("assessment_taken_list_class_fixture", "assessment_taken_list_test_fixture")
class TestAssessmentTakenList(object):
    """Tests for AssessmentTakenList"""
    def test_get_next_assessment_taken(self):
        """Tests get_next_assessment_taken"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTaken
        if not is_never_authz(self.service_config):
            assert isinstance(self.assessment_taken_list.get_next_assessment_taken(), AssessmentTaken)

    def test_get_next_assessments_taken(self):
        """Tests get_next_assessments_taken"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList, AssessmentTaken
        if not is_never_authz(self.service_config):
            new_list = self.assessment_taken_list.get_next_assessments_taken(2)
            assert isinstance(new_list, AssessmentTakenList)
            for item in new_list:
                assert isinstance(item, AssessmentTaken)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_section_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        form = request.cls.catalog.get_assessment_form_for_create([SEQUENCE_ASSESSMENT])
        form.display_name = 'Assessment'
        request.cls.assessment = request.cls.catalog.create_assessment(form)

        form = request.cls.catalog.get_item_form_for_create([])
        form.display_name = 'Test item'
        request.cls.item = request.cls.catalog.create_item(form)

        form = request.cls.catalog.get_question_form_for_create(request.cls.item.ident, [])
        request.cls.catalog.create_question(form)
        request.cls.item = request.cls.catalog.get_item(request.cls.item.ident)

        request.cls.catalog.add_item(request.cls.assessment.ident, request.cls.item.ident)
        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)

        form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        request.cls.offered = request.cls.catalog.create_assessment_offered(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_section_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.offered.ident,
                                                                        [])
        request.cls.taken = request.cls.catalog.create_assessment_taken(form)
        request.cls.section = request.cls.catalog.get_first_assessment_section(request.cls.taken.ident)
        request.cls.object = request.cls.section

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_assessment_taken(request.cls.taken.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_section_class_fixture", "assessment_section_test_fixture")
class TestAssessmentSection(object):
    """Tests for AssessmentSection"""
    def test_get_assessment_taken_id(self):
        """Tests get_assessment_taken_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.section.get_assessment_taken_id(), Id)
            assert str(self.section.get_assessment_taken_id()) == str(self.taken.ident)

    def test_get_assessment_taken(self):
        """Tests get_assessment_taken"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.section.get_assessment_taken(), AssessmentTaken)
            assert str(self.section.get_assessment_taken().ident) == str(self.taken.ident)

    def test_has_allocated_time(self):
        """Tests has_allocated_time"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.section.has_allocated_time()

    def test_get_allocated_time(self):
        """Tests get_allocated_time"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.section.get_allocated_time()

    def test_are_items_sequential(self):
        """Tests are_items_sequential"""
        # This does not throw an exception because of the SIMPLE_SEQUENCE record
        if not is_never_authz(self.service_config):
            assert not self.section.are_items_sequential()

    def test_are_items_shuffled(self):
        """Tests are_items_shuffled"""
        # This does not throw an exception because of the SIMPLE_SEQUENCE record
        if not is_never_authz(self.service_config):
            assert not self.section.are_items_shuffled()

    def test_get_assessment_section_record(self):
        """Tests get_assessment_section_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_assessment_section_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_section_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentSectionList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentSectionList tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)

        request.cls.form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                                  [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_section_list_test_fixture(request):
    from dlkit.json_.assessment.objects import AssessmentSectionList
    request.cls.assessment_section_list = list()
    request.cls.assessment_section_ids = list()

    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])

            obj = request.cls.catalog.create_assessment_part_for_assessment(form)

            request.cls.assessment_section_list.append(obj)
            request.cls.assessment_section_ids.append(obj.ident)
    request.cls.assessment_section_list = AssessmentSectionList(request.cls.assessment_section_list)


@pytest.mark.usefixtures("assessment_section_list_class_fixture", "assessment_section_list_test_fixture")
class TestAssessmentSectionList(object):
    """Tests for AssessmentSectionList"""
    def test_get_next_assessment_section(self):
        """Tests get_next_assessment_section"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        if not is_never_authz(self.service_config):
            assert isinstance(self.assessment_section_list.get_next_assessment_section(), AssessmentPart)

    def test_get_next_assessment_sections(self):
        """Tests get_next_assessment_sections"""
        from dlkit.abstract_osid.assessment.objects import AssessmentSectionList
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        if not is_never_authz(self.service_config):
            new_list = self.assessment_section_list.get_next_assessment_sections(2)
            assert isinstance(new_list, AssessmentSectionList)
            for item in new_list:
                assert isinstance(item, AssessmentPart)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_bank_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_bank(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bank_class_fixture", "bank_test_fixture")
class TestBank(object):
    """Tests for Bank"""
    def test_get_bank_record(self):
        """Tests get_bank_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_bank_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_bank_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bank_form_class_fixture", "bank_form_test_fixture")
class TestBankForm(object):
    """Tests for BankForm"""
    def test_get_bank_form_record(self):
        """Tests get_bank_form_record"""
        if uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        elif not is_never_authz(self.service_config):
            with pytest.raises(errors.Unsupported):
                self.object.get_bank_form_record(DEFAULT_TYPE)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        request.cls.bank_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.bank_ids:
                request.cls.svc_mgr.delete_bank(obj)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.assessment.objects import BankList
    request.cls.bank_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for BankList tests'
            obj = request.cls.svc_mgr.create_bank(create_form)
            request.cls.bank_list.append(obj)
            request.cls.bank_ids.append(obj.ident)
    request.cls.bank_list = BankList(request.cls.bank_list)


@pytest.mark.usefixtures("bank_list_class_fixture", "bank_list_test_fixture")
class TestBankList(object):
    """Tests for BankList"""
    def test_get_next_bank(self):
        """Tests get_next_bank"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Bank
        if not is_never_authz(self.service_config):
            assert isinstance(self.bank_list.get_next_bank(), Bank)

    def test_get_next_banks(self):
        """Tests get_next_banks"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import BankList, Bank
        if not is_never_authz(self.service_config):
            new_list = self.bank_list.get_next_banks(2)
            assert isinstance(new_list, BankList)
            for item in new_list:
                assert isinstance(item, Bank)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        request.cls.bank_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.assessment.objects import BankNode
    request.cls.bank_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for BankNode tests'
            obj = request.cls.svc_mgr.create_bank(create_form)
            request.cls.bank_list.append(BankNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.bank_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_bank(request.cls.bank_list[0].ident)
        request.cls.svc_mgr.add_child_bank(
            request.cls.bank_list[0].ident,
            request.cls.bank_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_bank_nodes(
            request.cls.bank_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_bank(
                request.cls.bank_list[0].ident,
                request.cls.bank_list[1].ident)
            request.cls.svc_mgr.remove_root_bank(request.cls.bank_list[0].ident)
            for node in request.cls.bank_list:
                request.cls.svc_mgr.delete_bank(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bank_node_class_fixture", "bank_node_test_fixture")
class TestBankNode(object):
    """Tests for BankNode"""
    def test_get_bank(self):
        """Tests get_bank"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.assessment.objects import Bank
        if not is_never_authz(self.service_config):
            assert isinstance(self.bank_list[0].get_bank(), OsidCatalog)
            assert str(self.bank_list[0].get_bank().ident) == str(self.bank_list[0].ident)

    def test_get_parent_bank_nodes(self):
        """Tests get_parent_bank_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.assessment.objects import BankNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bank_nodes(
                self.bank_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_bank_nodes(), BankNodeList)
            assert node.get_parent_bank_nodes().available() == 1
            assert str(node.get_parent_bank_nodes().next().ident) == str(self.bank_list[0].ident)

    def test_get_child_bank_nodes(self):
        """Tests get_child_bank_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.assessment.objects import BankNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bank_nodes(
                self.bank_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_bank_nodes(), BankNodeList)
            assert node.get_child_bank_nodes().available() == 1
            assert str(node.get_child_bank_nodes().next().ident) == str(self.bank_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        request.cls.bank_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.bank_node_ids:
                request.cls.svc_mgr.delete_bank(obj)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def bank_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.assessment.objects import BankNodeList, BankNode
    request.cls.bank_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test BankNode ' + str(num)
            create_form.description = 'Test BankNode for BankNodeList tests'
            obj = request.cls.svc_mgr.create_bank(create_form)
            request.cls.bank_node_list.append(BankNode(obj.object_map))
            request.cls.bank_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_bank(request.cls.bank_node_list[0].ident)
        request.cls.svc_mgr.add_child_bank(
            request.cls.bank_node_list[0].ident,
            request.cls.bank_node_list[1].ident)
    request.cls.bank_node_list = BankNodeList(request.cls.bank_node_list)


@pytest.mark.usefixtures("bank_node_list_class_fixture", "bank_node_list_test_fixture")
class TestBankNodeList(object):
    """Tests for BankNodeList"""
    def test_get_next_bank_node(self):
        """Tests get_next_bank_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import BankNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.bank_node_list.get_next_bank_node(), BankNode)

    def test_get_next_bank_nodes(self):
        """Tests get_next_bank_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import BankNodeList, BankNode
        if not is_never_authz(self.service_config):
            new_list = self.bank_node_list.get_next_bank_nodes(2)
            assert isinstance(new_list, BankNodeList)
            for item in new_list:
                assert isinstance(item, BankNode)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def response_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ResponseList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.catalog.get_assessment_form_for_create([SEQUENCE_ASSESSMENT])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)

        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = request.cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = request.cls.catalog.create_item(ifc)
            form = request.cls.catalog.get_question_form_for_create(test_item.ident, [])
            request.cls.catalog.create_question(form)

            if number == 'One':
                form = request.cls.catalog.get_answer_form_for_create(test_item.ident, [])
                request.cls.catalog.create_answer(form)

            request.cls.catalog.add_item(request.cls.assessment.ident, test_item.ident)

        form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def response_list_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
        request.cls.taken = request.cls.catalog.create_assessment_taken(form)

        section = request.cls.catalog.get_first_assessment_section(request.cls.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        for num in [0, 1]:
            create_form = request.cls.catalog.get_response_form(section.ident, first_question.ident)
            request.cls.catalog.submit_response(section.ident, first_question.ident, create_form)

        request.cls.response_list = request.cls.catalog.get_responses(section.ident)
        request.cls.object = request.cls.response_list


@pytest.mark.usefixtures("response_list_class_fixture", "response_list_test_fixture")
class TestResponseList(object):
    """Tests for ResponseList"""
    def test_get_next_response(self):
        """Tests get_next_response"""
        from dlkit.abstract_osid.assessment.rules import Response
        if not is_never_authz(self.service_config):
            assert isinstance(self.response_list.get_next_response(), Response)

    def test_get_next_responses(self):
        """Tests get_next_responses"""
        from dlkit.abstract_osid.assessment.objects import ResponseList
        from dlkit.abstract_osid.assessment.rules import Response
        if not is_never_authz(self.service_config):
            new_list = self.response_list.get_next_responses(2)
            assert isinstance(new_list, ResponseList)
            for item in new_list:
                assert isinstance(item, Response)
