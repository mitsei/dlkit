"""Unit tests of assessment queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.json_.assessment.queries import AnswerQuery
from dlkit.json_.assessment.queries import QuestionQuery
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def question_query_class_fixture(request):
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
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def question_query_test_fixture(request):
    # Since the session isn't implemented, we just construct a QuestionQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = QuestionQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("question_query_class_fixture", "question_query_test_fixture")
class TestQuestionQuery(object):
    """Tests for QuestionQuery"""
    def test_get_question_query_record(self):
        """Tests get_question_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_question_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def answer_query_class_fixture(request):
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
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def answer_query_test_fixture(request):
    # Since the session isn't implemented, we just construct a AnswerQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = AnswerQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("answer_query_class_fixture", "answer_query_test_fixture")
class TestAnswerQuery(object):
    """Tests for AnswerQuery"""
    def test_get_answer_query_record(self):
        """Tests get_answer_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_answer_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_item_query()


@pytest.mark.usefixtures("item_query_class_fixture", "item_query_test_fixture")
class TestItemQuery(object):
    """Tests for ItemQuery"""
    def test_match_learning_objective_id(self):
        """Tests match_learning_objective_id"""
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
            if is_no_authz(self.service_config):
                assert 'learningObjectiveIds' not in self.query._query_terms

            self.query.match_learning_objective_id(test_id, match=True)

            if is_no_authz(self.service_config):
                assert self.query._query_terms['learningObjectiveIds'] == {
                    '$in': [str(test_id)]
                }

    def test_clear_learning_objective_id_terms(self):
        """Tests clear_learning_objective_id_terms"""
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
            self.query.match_learning_objective_id(test_id, match=True)

            if is_no_authz(self.service_config):
                assert 'learningObjectiveIds' in self.query._query_terms

            self.query.clear_learning_objective_id_terms()

            if is_no_authz(self.service_config):
                assert 'learningObjectiveIds' not in self.query._query_terms

    def test_supports_learning_objective_query(self):
        """Tests supports_learning_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_learning_objective_query()

    def test_get_learning_objective_query(self):
        """Tests get_learning_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_learning_objective_query()

    def test_match_any_learning_objective(self):
        """Tests match_any_learning_objective"""
        if not is_never_authz(self.service_config):
            if is_no_authz(self.service_config):
                assert 'learningObjectiveIds' not in self.query._query_terms

            self.query.match_any_learning_objective(match=True)

            if is_no_authz(self.service_config):
                assert self.query._query_terms['learningObjectiveIds'] == {
                    '$exists': 'true',
                    '$nin': [[], ['']]
                }

    def test_clear_learning_objective_terms(self):
        """Tests clear_learning_objective_terms"""
        if not is_never_authz(self.service_config):
            self.query.match_any_learning_objective(match=True)

            if is_no_authz(self.service_config):
                assert 'learningObjectiveIds' in self.query._query_terms

            self.query.clear_learning_objective_terms()

            if is_no_authz(self.service_config):
                assert 'learningObjectiveIds' not in self.query._query_terms

    def test_match_question_id(self):
        """Tests match_question_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'questionId' not in self.query._query_terms
        self.query.match_question_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['questionId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_question_id_terms(self):
        """Tests clear_question_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_question_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'questionId' in self.query._query_terms
        self.query.clear_question_id_terms()
        if is_no_authz(self.service_config):
            assert 'questionId' not in self.query._query_terms

    def test_supports_question_query(self):
        """Tests supports_question_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_question_query()

    def test_get_question_query(self):
        """Tests get_question_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_question_query()

    def test_match_any_question(self):
        """Tests match_any_question"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_question(True)

    def test_clear_question_terms(self):
        """Tests clear_question_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_question_terms()

    def test_match_answer_id(self):
        """Tests match_answer_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'answerId' not in self.query._query_terms
        self.query.match_answer_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['answerId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_answer_id_terms(self):
        """Tests clear_answer_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_answer_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'answerId' in self.query._query_terms
        self.query.clear_answer_id_terms()
        if is_no_authz(self.service_config):
            assert 'answerId' not in self.query._query_terms

    def test_supports_answer_query(self):
        """Tests supports_answer_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_answer_query()

    def test_get_answer_query(self):
        """Tests get_answer_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_answer_query()

    def test_match_any_answer(self):
        """Tests match_any_answer"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_answer(True)

    def test_clear_answer_terms(self):
        """Tests clear_answer_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_answer_terms()

    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assessmentId' not in self.query._query_terms
        self.query.match_assessment_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assessmentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assessmentId' in self.query._query_terms
        self.query.clear_assessment_id_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentId' not in self.query._query_terms

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_query()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_query()

    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_assessment(True)

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_assessment_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' in self.query._query_terms
        self.query.clear_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' not in self.query._query_terms

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        if is_no_authz(self.service_config):
            assert 'bank' not in self.query._query_terms

    def test_get_item_query_record(self):
        """Tests get_item_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_item_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_assessment_query()


@pytest.mark.usefixtures("assessment_query_class_fixture", "assessment_query_test_fixture")
class TestAssessmentQuery(object):
    """Tests for AssessmentQuery"""
    def test_match_level_id(self):
        """Tests match_level_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'levelId' not in self.query._query_terms
        self.query.match_level_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['levelId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_level_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'levelId' in self.query._query_terms
        self.query.clear_level_id_terms()
        if is_no_authz(self.service_config):
            assert 'levelId' not in self.query._query_terms

    def test_supports_level_query(self):
        """Tests supports_level_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_level_query()

    def test_get_level_query(self):
        """Tests get_level_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_level_query()

    def test_match_any_level(self):
        """Tests match_any_level"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_level(True)

    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['level'] = 'foo'
        self.query.clear_level_terms()
        if is_no_authz(self.service_config):
            assert 'level' not in self.query._query_terms

    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'rubricId' not in self.query._query_terms
        self.query.match_rubric_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['rubricId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rubric_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'rubricId' in self.query._query_terms
        self.query.clear_rubric_id_terms()
        if is_no_authz(self.service_config):
            assert 'rubricId' not in self.query._query_terms

    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_rubric_query()

    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_rubric_query()

    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_rubric(True)

    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['rubric'] = 'foo'
        self.query.clear_rubric_terms()
        if is_no_authz(self.service_config):
            assert 'rubric' not in self.query._query_terms

    def test_match_item_id(self):
        """Tests match_item_id"""
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
            self.query.match_item_id(test_id, match=True)
            assert self.query._query_terms['itemIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_item_id_terms(self):
        """Tests clear_item_id_terms"""
        if not is_never_authz(self.service_config):
            test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
            self.query.match_item_id(test_id, match=True)
            assert 'itemIds' in self.query._query_terms
            self.query.clear_item_id_terms()
            assert 'itemIds' not in self.query._query_terms

    def test_supports_item_query(self):
        """Tests supports_item_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_item_query()

    def test_get_item_query(self):
        """Tests get_item_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_item_query()

    def test_match_any_item(self):
        """Tests match_any_item"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_item(True)

    def test_clear_item_terms(self):
        """Tests clear_item_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_item_terms()

    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' not in self.query._query_terms
        self.query.match_assessment_offered_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assessmentOfferedId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_offered_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' in self.query._query_terms
        self.query.clear_assessment_offered_id_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' not in self.query._query_terms

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_offered_query()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_offered_query()

    def test_match_any_assessment_offered(self):
        """Tests match_any_assessment_offered"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_assessment_offered(True)

    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_assessment_offered_terms()

    def test_match_assessment_taken_id(self):
        """Tests match_assessment_taken_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assessmentTakenId' not in self.query._query_terms
        self.query.match_assessment_taken_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assessmentTakenId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_assessment_taken_id_terms(self):
        """Tests clear_assessment_taken_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_taken_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assessmentTakenId' in self.query._query_terms
        self.query.clear_assessment_taken_id_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentTakenId' not in self.query._query_terms

    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_taken_query()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_taken_query()

    def test_match_any_assessment_taken(self):
        """Tests match_any_assessment_taken"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_assessment_taken(True)

    def test_clear_assessment_taken_terms(self):
        """Tests clear_assessment_taken_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_assessment_taken_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' in self.query._query_terms
        self.query.clear_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' not in self.query._query_terms

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        if is_no_authz(self.service_config):
            assert 'bank' not in self.query._query_terms

    def test_get_assessment_query_record(self):
        """Tests get_assessment_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_assessment_offered_query()


@pytest.mark.usefixtures("assessment_offered_query_class_fixture", "assessment_offered_query_test_fixture")
class TestAssessmentOfferedQuery(object):
    """Tests for AssessmentOfferedQuery"""
    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assessmentId' not in self.query._query_terms
        self.query.match_assessment_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assessmentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assessmentId' in self.query._query_terms
        self.query.clear_assessment_id_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentId' not in self.query._query_terms

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_query()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_query()

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessment'] = 'foo'
        self.query.clear_assessment_terms()
        if is_no_authz(self.service_config):
            assert 'assessment' not in self.query._query_terms

    def test_match_level_id(self):
        """Tests match_level_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'levelId' not in self.query._query_terms
        self.query.match_level_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['levelId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_level_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'levelId' in self.query._query_terms
        self.query.clear_level_id_terms()
        if is_no_authz(self.service_config):
            assert 'levelId' not in self.query._query_terms

    def test_supports_level_query(self):
        """Tests supports_level_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_level_query()

    def test_get_level_query(self):
        """Tests get_level_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_level_query()

    def test_match_any_level(self):
        """Tests match_any_level"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_level(True)

    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['level'] = 'foo'
        self.query.clear_level_terms()
        if is_no_authz(self.service_config):
            assert 'level' not in self.query._query_terms

    def test_match_items_sequential(self):
        """Tests match_items_sequential"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_items_sequential(True)

    def test_clear_items_sequential_terms(self):
        """Tests clear_items_sequential_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['itemsSequential'] = 'foo'
        self.query.clear_items_sequential_terms()
        if is_no_authz(self.service_config):
            assert 'itemsSequential' not in self.query._query_terms

    def test_match_items_shuffled(self):
        """Tests match_items_shuffled"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_items_shuffled(True)

    def test_clear_items_shuffled_terms(self):
        """Tests clear_items_shuffled_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['itemsShuffled'] = 'foo'
        self.query.clear_items_shuffled_terms()
        if is_no_authz(self.service_config):
            assert 'itemsShuffled' not in self.query._query_terms

    def test_match_start_time(self):
        """Tests match_start_time"""
        if not is_never_authz(self.service_config):
            start_time = DateTime.utcnow()
            end_time = DateTime.utcnow()
            self.query.match_start_time(start_time, end_time, match=True)
            assert self.query._query_terms['startTime'] == {
                '$gte': start_time,
                '$lte': end_time
            }

    def test_match_any_start_time(self):
        """Tests match_any_start_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_start_time(True)

    def test_clear_start_time_terms(self):
        """Tests clear_start_time_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['startTime'] = 'foo'
        self.query.clear_start_time_terms()
        if is_no_authz(self.service_config):
            assert 'startTime' not in self.query._query_terms

    def test_match_deadline(self):
        """Tests match_deadline"""
        if not is_never_authz(self.service_config):
            start_time = DateTime.utcnow()
            end_time = DateTime.utcnow()
            self.query.match_deadline(start_time, end_time, match=True)
            assert self.query._query_terms['deadline'] == {
                '$gte': start_time,
                '$lte': end_time
            }

    def test_match_any_deadline(self):
        """Tests match_any_deadline"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_deadline(True)

    def test_clear_deadline_terms(self):
        """Tests clear_deadline_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['deadline'] = 'foo'
        self.query.clear_deadline_terms()
        if is_no_authz(self.service_config):
            assert 'deadline' not in self.query._query_terms

    def test_match_duration(self):
        """Tests match_duration"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_duration(True, True, True)

    def test_match_any_duration(self):
        """Tests match_any_duration"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_duration(True)

    def test_clear_duration_terms(self):
        """Tests clear_duration_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['duration'] = 'foo'
        self.query.clear_duration_terms()
        if is_no_authz(self.service_config):
            assert 'duration' not in self.query._query_terms

    def test_match_score_system_id(self):
        """Tests match_score_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'scoreSystemId' not in self.query._query_terms
        self.query.match_score_system_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['scoreSystemId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_score_system_id_terms(self):
        """Tests clear_score_system_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_score_system_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'scoreSystemId' in self.query._query_terms
        self.query.clear_score_system_id_terms()
        if is_no_authz(self.service_config):
            assert 'scoreSystemId' not in self.query._query_terms

    def test_supports_score_system_query(self):
        """Tests supports_score_system_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_score_system_query()

    def test_get_score_system_query(self):
        """Tests get_score_system_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_score_system_query()

    def test_match_any_score_system(self):
        """Tests match_any_score_system"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_score_system(True)

    def test_clear_score_system_terms(self):
        """Tests clear_score_system_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['scoreSystem'] = 'foo'
        self.query.clear_score_system_terms()
        if is_no_authz(self.service_config):
            assert 'scoreSystem' not in self.query._query_terms

    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradeSystemId' not in self.query._query_terms
        self.query.match_grade_system_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradeSystemId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_grade_system_id_terms(self):
        """Tests clear_grade_system_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_system_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradeSystemId' in self.query._query_terms
        self.query.clear_grade_system_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradeSystemId' not in self.query._query_terms

    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grade_system_query()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_system_query()

    def test_match_any_grade_system(self):
        """Tests match_any_grade_system"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grade_system(True)

    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradeSystem'] = 'foo'
        self.query.clear_grade_system_terms()
        if is_no_authz(self.service_config):
            assert 'gradeSystem' not in self.query._query_terms

    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'rubricId' not in self.query._query_terms
        self.query.match_rubric_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['rubricId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rubric_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'rubricId' in self.query._query_terms
        self.query.clear_rubric_id_terms()
        if is_no_authz(self.service_config):
            assert 'rubricId' not in self.query._query_terms

    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_rubric_query()

    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_rubric_query()

    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_rubric(True)

    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_rubric_terms()

    def test_match_assessment_taken_id(self):
        """Tests match_assessment_taken_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assessmentTakenId' not in self.query._query_terms
        self.query.match_assessment_taken_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assessmentTakenId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_assessment_taken_id_terms(self):
        """Tests clear_assessment_taken_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_taken_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assessmentTakenId' in self.query._query_terms
        self.query.clear_assessment_taken_id_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentTakenId' not in self.query._query_terms

    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_taken_query()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_taken_query()

    def test_match_any_assessment_taken(self):
        """Tests match_any_assessment_taken"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_assessment_taken(True)

    def test_clear_assessment_taken_terms(self):
        """Tests clear_assessment_taken_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_assessment_taken_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' in self.query._query_terms
        self.query.clear_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' not in self.query._query_terms

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        if is_no_authz(self.service_config):
            assert 'bank' not in self.query._query_terms

    def test_get_assessment_offered_query_record(self):
        """Tests get_assessment_offered_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_offered_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_assessment_taken_query()


@pytest.mark.usefixtures("assessment_taken_query_class_fixture", "assessment_taken_query_test_fixture")
class TestAssessmentTakenQuery(object):
    """Tests for AssessmentTakenQuery"""
    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' not in self.query._query_terms
        self.query.match_assessment_offered_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assessmentOfferedId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_offered_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' in self.query._query_terms
        self.query.clear_assessment_offered_id_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' not in self.query._query_terms

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_offered_query()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_offered_query()

    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessmentOffered'] = 'foo'
        self.query.clear_assessment_offered_terms()
        if is_no_authz(self.service_config):
            assert 'assessmentOffered' not in self.query._query_terms

    def test_match_taker_id(self):
        """Tests match_taker_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'takerId' not in self.query._query_terms
        self.query.match_taker_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['takerId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_taker_id_terms(self):
        """Tests clear_taker_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_taker_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'takerId' in self.query._query_terms
        self.query.clear_taker_id_terms()
        if is_no_authz(self.service_config):
            assert 'takerId' not in self.query._query_terms

    def test_supports_taker_query(self):
        """Tests supports_taker_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_taker_query()

    def test_get_taker_query(self):
        """Tests get_taker_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_taker_query()

    def test_clear_taker_terms(self):
        """Tests clear_taker_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['taker'] = 'foo'
        self.query.clear_taker_terms()
        if is_no_authz(self.service_config):
            assert 'taker' not in self.query._query_terms

    def test_match_taking_agent_id(self):
        """Tests match_taking_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'takingAgentId' not in self.query._query_terms
        self.query.match_taking_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['takingAgentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_taking_agent_id_terms(self):
        """Tests clear_taking_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_taking_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'takingAgentId' in self.query._query_terms
        self.query.clear_taking_agent_id_terms()
        if is_no_authz(self.service_config):
            assert 'takingAgentId' not in self.query._query_terms

    def test_supports_taking_agent_query(self):
        """Tests supports_taking_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_taking_agent_query()

    def test_get_taking_agent_query(self):
        """Tests get_taking_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_taking_agent_query()

    def test_clear_taking_agent_terms(self):
        """Tests clear_taking_agent_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_taking_agent_terms()

    def test_match_actual_start_time(self):
        """Tests match_actual_start_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_actual_start_time(True, True, True)

    def test_match_any_actual_start_time(self):
        """Tests match_any_actual_start_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_actual_start_time(True)

    def test_clear_actual_start_time_terms(self):
        """Tests clear_actual_start_time_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_actual_start_time_terms()

    def test_match_completion_time(self):
        """Tests match_completion_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_completion_time(True, True, True)

    def test_match_any_completion_time(self):
        """Tests match_any_completion_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_completion_time(True)

    def test_clear_completion_time_terms(self):
        """Tests clear_completion_time_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_completion_time_terms()

    def test_match_time_spent(self):
        """Tests match_time_spent"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_time_spent(True, True, True)

    def test_clear_time_spent_terms(self):
        """Tests clear_time_spent_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_time_spent_terms()

    def test_match_score_system_id(self):
        """Tests match_score_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'scoreSystemId' not in self.query._query_terms
        self.query.match_score_system_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['scoreSystemId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_score_system_id_terms(self):
        """Tests clear_score_system_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_score_system_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'scoreSystemId' in self.query._query_terms
        self.query.clear_score_system_id_terms()
        if is_no_authz(self.service_config):
            assert 'scoreSystemId' not in self.query._query_terms

    def test_supports_score_system_query(self):
        """Tests supports_score_system_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_score_system_query()

    def test_get_score_system_query(self):
        """Tests get_score_system_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_score_system_query()

    def test_match_any_score_system(self):
        """Tests match_any_score_system"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_score_system(True)

    def test_clear_score_system_terms(self):
        """Tests clear_score_system_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_score_system_terms()

    def test_match_score(self):
        """Tests match_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_score(True, True, True)

    def test_match_any_score(self):
        """Tests match_any_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_score(True)

    def test_clear_score_terms(self):
        """Tests clear_score_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_score_terms()

    def test_match_grade_id(self):
        """Tests match_grade_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradeId' not in self.query._query_terms
        self.query.match_grade_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradeId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_grade_id_terms(self):
        """Tests clear_grade_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradeId' in self.query._query_terms
        self.query.clear_grade_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradeId' not in self.query._query_terms

    def test_supports_grade_query(self):
        """Tests supports_grade_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grade_query()

    def test_get_grade_query(self):
        """Tests get_grade_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_query()

    def test_match_any_grade(self):
        """Tests match_any_grade"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grade(True)

    def test_clear_grade_terms(self):
        """Tests clear_grade_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_grade_terms()

    def test_match_feedback(self):
        """Tests match_feedback"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_feedback(True, True, True)

    def test_match_any_feedback(self):
        """Tests match_any_feedback"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_feedback(True)

    def test_clear_feedback_terms(self):
        """Tests clear_feedback_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_feedback_terms()

    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'rubricId' not in self.query._query_terms
        self.query.match_rubric_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['rubricId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rubric_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'rubricId' in self.query._query_terms
        self.query.clear_rubric_id_terms()
        if is_no_authz(self.service_config):
            assert 'rubricId' not in self.query._query_terms

    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_rubric_query()

    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_rubric_query()

    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_rubric(True)

    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_rubric_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' in self.query._query_terms
        self.query.clear_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedBankIds' not in self.query._query_terms

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        if is_no_authz(self.service_config):
            assert 'bank' not in self.query._query_terms

    def test_get_assessment_taken_query_record(self):
        """Tests get_assessment_taken_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_taken_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_query_class_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
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
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_query_test_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.svc_mgr.get_bank_query()


@pytest.mark.usefixtures("bank_query_class_fixture", "bank_query_test_fixture")
class TestBankQuery(object):
    """Tests for BankQuery"""
    def test_match_item_id(self):
        """Tests match_item_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_item_id(True, True)

    def test_clear_item_id_terms(self):
        """Tests clear_item_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['itemId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_item_id_terms()

        if is_no_authz(self.service_config):
            assert 'itemId' not in self.query._query_terms

    def test_supports_item_query(self):
        """Tests supports_item_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_item_query()

    def test_get_item_query(self):
        """Tests get_item_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_item_query()

    def test_match_any_item(self):
        """Tests match_any_item"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_item(True)

    def test_clear_item_terms(self):
        """Tests clear_item_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['item'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_item_terms()

        if is_no_authz(self.service_config):
            assert 'item' not in self.query._query_terms

    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_assessment_id(True, True)

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessmentId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_assessment_id_terms()

        if is_no_authz(self.service_config):
            assert 'assessmentId' not in self.query._query_terms

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_query()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_query()

    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_assessment(True)

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessment'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_assessment_terms()

        if is_no_authz(self.service_config):
            assert 'assessment' not in self.query._query_terms

    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_assessment_offered_id(True, True)

    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessmentOfferedId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_assessment_offered_id_terms()

        if is_no_authz(self.service_config):
            assert 'assessmentOfferedId' not in self.query._query_terms

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_offered_query()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_offered_query()

    def test_match_any_assessment_offered(self):
        """Tests match_any_assessment_offered"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_assessment_offered(True)

    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessmentOffered'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_assessment_offered_terms()

        if is_no_authz(self.service_config):
            assert 'assessmentOffered' not in self.query._query_terms

    def test_match_ancestor_bank_id(self):
        """Tests match_ancestor_bank_id"""
        if not is_never_authz(self.service_config):
            assert '_id' not in self.query._query_terms
            self.query.match_ancestor_bank_id(self.fake_id, True)
            assert self.query._query_terms['_id'] == {
                '$in': []
            }

    def test_clear_ancestor_bank_id_terms(self):
        """Tests clear_ancestor_bank_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorBankId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_bank_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorBankId' not in self.query._query_terms

    def test_supports_ancestor_bank_query(self):
        """Tests supports_ancestor_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_bank_query()

    def test_get_ancestor_bank_query(self):
        """Tests get_ancestor_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_bank_query()

    def test_match_any_ancestor_bank(self):
        """Tests match_any_ancestor_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_bank(True)

    def test_clear_ancestor_bank_terms(self):
        """Tests clear_ancestor_bank_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorBank'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_bank_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorBank' not in self.query._query_terms

    def test_match_descendant_bank_id(self):
        """Tests match_descendant_bank_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_bank_id(True, True)

    def test_clear_descendant_bank_id_terms(self):
        """Tests clear_descendant_bank_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantBankId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_bank_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantBankId' not in self.query._query_terms

    def test_supports_descendant_bank_query(self):
        """Tests supports_descendant_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_bank_query()

    def test_get_descendant_bank_query(self):
        """Tests get_descendant_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_bank_query()

    def test_match_any_descendant_bank(self):
        """Tests match_any_descendant_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_bank(True)

    def test_clear_descendant_bank_terms(self):
        """Tests clear_descendant_bank_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantBank'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_bank_terms()

        if is_no_authz(self.service_config):
            assert 'descendantBank' not in self.query._query_terms

    def test_get_bank_query_record(self):
        """Tests get_bank_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bank_query_record(True)
