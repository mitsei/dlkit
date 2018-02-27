"""Unit tests of assessment sessions."""


import datetime
import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.assessment import objects
from dlkit.abstract_osid.assessment import objects as ABCObjects
from dlkit.abstract_osid.assessment import queries as ABCQueries
from dlkit.abstract_osid.assessment import searches as ABCSearches
from dlkit.abstract_osid.assessment.objects import AssessmentOffered
from dlkit.abstract_osid.assessment.objects import AssessmentSection, AssessmentSectionList
from dlkit.abstract_osid.assessment.objects import AssessmentTaken
from dlkit.abstract_osid.assessment.objects import Bank as ABCBank
from dlkit.abstract_osid.assessment.objects import Bank, Answer, AnswerList, AnswerForm
from dlkit.abstract_osid.assessment.objects import Question, QuestionList
from dlkit.abstract_osid.assessment.objects import ResponseList
from dlkit.abstract_osid.assessment.rules import Response
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.json_.assessment import searches
from dlkit.json_.id.objects import IdList
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.types.string import get_type_data as get_string_type_data
from dlkit.primordium.type.primitives import Type
from dlkit.records import registry
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


SEQUENCE_ASSESSMENT = Type(**registry.ASSESSMENT_RECORD_TYPES["simple-child-sequencing"])
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
DEFAULT_STRING_MATCH_TYPE = Type(**get_string_type_data("WORDIGNORECASE"))
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE 2', 'authority': 'YOURS 2'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentSession tests'
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
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
        request.cls.taken = request.cls.catalog.create_assessment_taken(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for item in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(item.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_session_class_fixture", "assessment_session_test_fixture")
class TestAssessmentSession(object):
    """Tests for AssessmentSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # this test should not be needed....
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog, Bank)

    def test_can_take_assessments(self):
        """Tests can_take_assessments"""
        assert isinstance(self.session.can_take_assessments(), bool)

    def test_has_assessment_begun(self):
        """Tests has_assessment_begun"""
        if not is_never_authz(self.service_config):
            future_start = DateTime.utcnow() + datetime.timedelta(days=1)
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
            form.set_start_time(DateTime(**{
                'year': future_start.year,
                'month': future_start.month,
                'day': future_start.day,
                'hour': future_start.hour,
                'minute': future_start.minute,
                'second': future_start.second
            }))
            future_offered = self.catalog.create_assessment_offered(form)
            form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
            future_taken = self.catalog.create_assessment_taken(form)
            assert not self.session.has_assessment_begun(future_taken.ident)

            assert self.session.has_assessment_begun(self.taken.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.has_assessment_begun(self.fake_id)

    def test_is_assessment_over(self):
        """Tests is_assessment_over"""
        # There are also other conditions that flag "over", but are not
        # tested here. Like if the offered goes past the deadline...so we
        # would have to do a time.sleep(). TODO: add those tests in.

        if not is_never_authz(self.service_config):
            assert not self.session.is_assessment_over(self.taken.ident)
            self.session.finish_assessment(self.taken.ident)
            assert self.session.is_assessment_over(self.taken.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.is_assessment_over(self.fake_id)

    def test_requires_synchronous_sections(self):
        """Tests requires_synchronous_sections"""
        if not is_never_authz(self.service_config):
            assert not self.session.requires_synchronous_sections(self.taken.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.requires_synchronous_sections(self.fake_id)

    def test_get_first_assessment_section(self):
        """Tests get_first_assessment_section"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            assert isinstance(section, AssessmentSection)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_first_assessment_section(self.fake_id)

    def test_has_next_assessment_section(self):
        """Tests has_next_assessment_section"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            assert not self.session.has_next_assessment_section(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_next_assessment_section(self.fake_id)

    def test_get_next_assessment_section(self):
        """Tests get_next_assessment_section"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            with pytest.raises(errors.IllegalState):
                self.session.get_next_assessment_section(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_next_assessment_section(self.fake_id)

    def test_has_previous_assessment_section(self):
        """Tests has_previous_assessment_section"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            assert not self.session.has_previous_assessment_section(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_previous_assessment_section(self.fake_id)

    def test_get_previous_assessment_section(self):
        """Tests get_previous_assessment_section"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            with pytest.raises(errors.IllegalState):
                self.session.get_previous_assessment_section(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_previous_assessment_section(self.fake_id)

    def test_get_assessment_section(self):
        """Tests get_assessment_section"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            test_section = self.session.get_assessment_section(section.ident)
            assert isinstance(test_section, AssessmentSection)
            assert str(test_section.ident) == str(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_section(self.fake_id)

    def test_get_assessment_sections(self):
        """Tests get_assessment_sections"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            test_sections = self.session.get_assessment_sections(self.taken.ident)
            assert isinstance(test_sections, AssessmentSectionList)
            assert test_sections.available() == 1
            first_section = test_sections.next()
            assert isinstance(first_section, AssessmentSection)
            assert str(first_section.ident) == str(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_sections(self.fake_id)

    def test_is_assessment_section_complete(self):
        """Tests is_assessment_section_complete"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            total_questions = questions.available()

            assert not self.session.is_assessment_section_complete(section.ident)

            for index, question in enumerate(questions):
                form = self.session.get_response_form(section.ident, question.ident)
                self.session.submit_response(section.ident, question.ident, form)
                if index < (total_questions - 1):
                    assert not self.session.is_assessment_section_complete(section.ident)
                else:
                    assert self.session.is_assessment_section_complete(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.is_assessment_section_complete(self.fake_id)

    def test_get_incomplete_assessment_sections(self):
        """Tests get_incomplete_assessment_sections"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()

            test_sections = self.session.get_incomplete_assessment_sections(self.taken.ident)
            assert isinstance(test_sections, AssessmentSectionList)
            assert test_sections.available() == 1
            first_section = test_sections.next()
            assert isinstance(first_section, AssessmentSection)
            assert str(first_section.ident) == str(section.ident)

            for question in questions:
                form = self.session.get_response_form(section.ident, question.ident)
                self.session.submit_response(section.ident, question.ident, form)

            self.session._provider_sessions = {}  # need to get rid of the cached taken
            test_sections = self.session.get_incomplete_assessment_sections(self.taken.ident)
            assert isinstance(test_sections, AssessmentSectionList)
            assert test_sections.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_incomplete_assessment_sections(self.fake_id)

    def test_has_assessment_section_begun(self):
        """Tests has_assessment_section_begun"""
        if not is_never_authz(self.service_config):
            future_start = DateTime.utcnow() + datetime.timedelta(days=1)
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
            form.set_start_time(DateTime(**{
                'year': future_start.year,
                'month': future_start.month,
                'day': future_start.day,
                'hour': future_start.hour,
                'minute': future_start.minute,
                'second': future_start.second
            }))
            future_offered = self.catalog.create_assessment_offered(form)
            form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
            future_taken = self.catalog.create_assessment_taken(form)

            with pytest.raises(errors.IllegalState):
                # cannot even get the sectionId to call the method
                self.catalog.get_first_assessment_section(future_taken.ident)

            section = self.catalog.get_first_assessment_section(self.taken.ident)
            assert self.session.has_assessment_section_begun(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.has_assessment_section_begun(self.fake_id)

    def test_is_assessment_section_over(self):
        """Tests is_assessment_section_over"""
        # There are also other conditions that flag "over", but are not
        # tested here. Like if the offered goes past the deadline...so we
        # would have to do a time.sleep(). TODO: add those tests in.

        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)

            assert not self.session.is_assessment_section_over(section.ident)
            self.session.finish_assessment_section(section.ident)
            assert self.session.is_assessment_section_over(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.is_assessment_section_over(self.fake_id)

    def test_requires_synchronous_responses(self):
        """Tests requires_synchronous_responses"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            assert not self.session.requires_synchronous_responses(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.requires_synchronous_responses(self.fake_id)

    def test_get_first_question(self):
        """Tests get_first_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            test_question = self.session.get_first_question(section.ident)
            assert isinstance(test_question, Question)
            assert str(first_question.ident) == str(test_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_first_question(self.fake_id)

    def test_has_next_question(self):
        """Tests has_next_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            assert self.session.has_next_question(section.ident,
                                                  first_question.ident)
            assert not self.session.has_next_question(section.ident,
                                                      fourth_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_next_question(self.fake_id, self.fake_id)

    def test_get_next_question(self):
        """Tests get_next_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            test_question = self.session.get_next_question(section.ident,
                                                           first_question.ident)
            assert isinstance(test_question, Question)
            assert str(second_question.ident) == str(test_question.ident)

            with pytest.raises(errors.IllegalState):
                self.session.get_next_question(section.ident, fourth_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_next_question(self.fake_id, self.fake_id)

    def test_has_previous_question(self):
        """Tests has_previous_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            assert self.session.has_previous_question(section.ident,
                                                      fourth_question.ident)
            assert not self.session.has_previous_question(section.ident,
                                                          first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_previous_question(self.fake_id, self.fake_id)

    def test_get_previous_question(self):
        """Tests get_previous_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            test_question = self.session.get_previous_question(section.ident,
                                                               fourth_question.ident)
            assert isinstance(test_question, Question)
            assert str(third_question.ident) == str(test_question.ident)

            with pytest.raises(errors.IllegalState):
                self.session.get_previous_question(section.ident, first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_previous_question(self.fake_id, self.fake_id)

    def test_get_question(self):
        """Tests get_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            test_question = self.session.get_question(section.ident, first_question.ident)
            assert isinstance(test_question, Question)
            assert str(test_question.ident) == str(first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_question(self.fake_id, self.fake_id)

    def test_get_questions(self):
        """Tests get_questions"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            test_questions = self.session.get_questions(section.ident)
            assert isinstance(test_questions, QuestionList)
            assert test_questions.available() == 4
            first_test_question = test_questions.next()
            assert isinstance(first_test_question, Question)
            assert str(first_test_question.ident) == str(first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_questions(self.fake_id)

    def test_get_response_form(self):
        """Tests get_response_form"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            form = self.session.get_response_form(section.ident, first_question.ident)
            assert isinstance(form, AnswerForm)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_response_form(self.fake_id, self.fake_id)

    def test_submit_response(self):
        """Tests submit_response"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            assert 'missingResponse' in section._my_map['questions'][0]['responses'][0]
            assert 0 == section._my_map['questions'][0]['responses'][0]['missingResponse']

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)
            section = self.catalog.get_assessment_section(section.ident)

            assert 'missingResponse' not in section._my_map['questions'][0]['responses'][0]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.submit_response(self.fake_id, self.fake_id, 'foo')

    def test_skip_item(self):
        """Tests skip_item"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            assert 'missingResponse' in section._my_map['questions'][0]['responses'][0]
            assert 0 == section._my_map['questions'][0]['responses'][0]['missingResponse']

            self.session.skip_item(section.ident, first_question.ident)
            section = self.catalog.get_assessment_section(section.ident)

            assert 'missingResponse' in section._my_map['questions'][0]['responses'][0]
            assert 1 == section._my_map['questions'][0]['responses'][0]['missingResponse']
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.skip_item(self.fake_id, self.fake_id)

    def test_is_question_answered(self):
        """Tests is_question_answered"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            assert not self.session.is_question_answered(section.ident,
                                                         first_question.ident)

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)

            assert self.session.is_question_answered(section.ident,
                                                     first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.is_question_answered(self.fake_id, self.fake_id)

    def test_get_unanswered_questions(self):
        """Tests get_unanswered_questions"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            question_ids = [q.ident for q in questions]

            test_questions = self.session.get_unanswered_questions(section.ident)
            assert isinstance(test_questions, QuestionList)
            assert test_questions.available() == 4
            test_question_ids = [q.ident for q in test_questions]
            assert question_ids == test_question_ids

            form = self.session.get_response_form(section.ident, question_ids[1])
            self.session.submit_response(section.ident, question_ids[1], form)

            test_questions = self.session.get_unanswered_questions(section.ident)
            assert isinstance(test_questions, QuestionList)
            assert test_questions.available() == 3
            test_question_ids = [q.ident for q in test_questions]
            assert question_ids[1] not in test_question_ids
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_unanswered_questions(self.fake_id)

    def test_has_unanswered_questions(self):
        """Tests has_unanswered_questions"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            total_questions = questions.available()

            assert self.session.has_unanswered_questions(section.ident)

            for index, question in enumerate(questions):
                form = self.session.get_response_form(section.ident, question.ident)
                self.session.submit_response(section.ident, question.ident, form)
                if index < (total_questions - 1):
                    assert self.session.has_unanswered_questions(section.ident)
                else:
                    assert not self.session.has_unanswered_questions(section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_unanswered_questions(self.fake_id)

    def test_get_first_unanswered_question(self):
        """Tests get_first_unanswered_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()

            unanswered_question = self.session.get_first_unanswered_question(section.ident)
            assert isinstance(unanswered_question, Question)
            assert str(unanswered_question.ident) == str(first_question.ident)

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)

            unanswered_question = self.session.get_first_unanswered_question(section.ident)
            assert isinstance(unanswered_question, Question)
            assert str(unanswered_question.ident) == str(second_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_first_unanswered_question(self.fake_id)

    def test_has_next_unanswered_question(self):
        """Tests has_next_unanswered_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            assert self.session.has_next_unanswered_question(section.ident,
                                                             first_question.ident)

            form = self.session.get_response_form(section.ident, second_question.ident)
            self.session.submit_response(section.ident, second_question.ident, form)

            assert self.session.has_next_unanswered_question(section.ident,
                                                             first_question.ident)
            assert not self.session.has_next_unanswered_question(section.ident,
                                                                 fourth_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_next_unanswered_question(self.fake_id, self.fake_id)

    def test_get_next_unanswered_question(self):
        """Tests get_next_unanswered_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            test_question = self.session.get_next_unanswered_question(section.ident,
                                                                      first_question.ident)
            assert isinstance(test_question, Question)
            assert str(second_question.ident) == str(test_question.ident)

            form = self.session.get_response_form(section.ident, second_question.ident)
            self.session.submit_response(section.ident, second_question.ident, form)

            test_question = self.session.get_next_unanswered_question(section.ident,
                                                                      first_question.ident)
            assert isinstance(test_question, Question)
            assert str(third_question.ident) == str(test_question.ident)

            with pytest.raises(errors.IllegalState):
                self.session.get_next_unanswered_question(section.ident,
                                                          fourth_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_next_unanswered_question(self.fake_id, self.fake_id)

    def test_has_previous_unanswered_question(self):
        """Tests has_previous_unanswered_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            assert self.session.has_previous_unanswered_question(section.ident,
                                                                 fourth_question.ident)

            form = self.session.get_response_form(section.ident, third_question.ident)
            self.session.submit_response(section.ident, third_question.ident, form)

            assert self.session.has_previous_unanswered_question(section.ident,
                                                                 fourth_question.ident)
            assert not self.session.has_previous_unanswered_question(section.ident,
                                                                     first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.has_previous_unanswered_question(self.fake_id, self.fake_id)

    def test_get_previous_unanswered_question(self):
        """Tests get_previous_unanswered_question"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()
            third_question = questions.next()
            fourth_question = questions.next()

            test_question = self.session.get_previous_unanswered_question(section.ident,
                                                                          fourth_question.ident)
            assert isinstance(test_question, Question)
            assert str(third_question.ident) == str(test_question.ident)

            form = self.session.get_response_form(section.ident, third_question.ident)
            self.session.submit_response(section.ident, third_question.ident, form)

            test_question = self.session.get_previous_unanswered_question(section.ident,
                                                                          fourth_question.ident)
            assert isinstance(test_question, Question)
            assert str(second_question.ident) == str(test_question.ident)

            with pytest.raises(errors.IllegalState):
                self.session.get_previous_unanswered_question(section.ident,
                                                              first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_previous_unanswered_question(self.fake_id, self.fake_id)

    def test_get_response(self):
        """Tests get_response"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            test_response = self.session.get_response(section.ident, first_question.ident)
            assert isinstance(test_response, Response)

            with pytest.raises(errors.IllegalState):
                test_response.object_map

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)

            test_response = self.session.get_response(section.ident, first_question.ident)
            assert isinstance(test_response, Response)

            test_response.object_map
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_response(self.fake_id, self.fake_id)

    def test_get_responses(self):
        """Tests get_responses"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()

            test_responses = self.session.get_responses(section.ident)
            assert isinstance(test_responses, ResponseList)
            assert test_responses.available() == 4
            first_response = test_responses.next()
            assert isinstance(first_response, Response)

            with pytest.raises(errors.IllegalState):
                first_response.object_map
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_responses(self.fake_id)

    def test_clear_response(self):
        """Tests clear_response"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()

            assert 'missingResponse' in section._my_map['questions'][0]['responses'][0]
            assert 0 == section._my_map['questions'][0]['responses'][0]['missingResponse']

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)
            section = self.catalog.get_assessment_section(section.ident)

            assert 'missingResponse' not in section._my_map['questions'][0]['responses'][0]

            self.session.clear_response(section.ident, first_question.ident)
            section = self.catalog.get_assessment_section(section.ident)

            assert 'missingResponse' in section._my_map['questions'][0]['responses'][0]
            assert 1 == section._my_map['questions'][0]['responses'][0]['missingResponse']
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.clear_response(self.fake_id, self.fake_id)

    def test_finish_assessment_section(self):
        """Tests finish_assessment_section"""
        if not is_never_authz(self.service_config):
            future_start = DateTime.utcnow() + datetime.timedelta(days=1)
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
            form.set_start_time(DateTime(**{
                'year': future_start.year,
                'month': future_start.month,
                'day': future_start.day,
                'hour': future_start.hour,
                'minute': future_start.minute,
                'second': future_start.second
            }))
            future_offered = self.catalog.create_assessment_offered(form)
            form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
            future_taken = self.catalog.create_assessment_taken(form)
            with pytest.raises(errors.IllegalState):
                self.catalog.get_first_assessment_section(future_taken.ident)

            first_section = self.catalog.get_first_assessment_section(self.taken.ident)
            assert 'completionTime' not in first_section._my_map
            self.session.finish_assessment_section(first_section.ident)

            with pytest.raises(errors.IllegalState):
                # it is over, so can't GET the section now
                self.catalog.get_assessment_section(first_section.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.finish_assessment_section(self.fake_id)

    def test_is_answer_available(self):
        """Tests is_answer_available"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()

            assert not self.session.is_answer_available(section.ident,
                                                        second_question.ident)

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)

            answers = self.session.get_answers(section.ident, first_question.ident)
            assert isinstance(answers, AnswerList)
            assert self.session.is_answer_available(section.ident,
                                                    first_question.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.is_answer_available(self.fake_id, self.fake_id)

    def test_get_answers(self):
        """Tests get_answers"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()
            first_question = questions.next()
            second_question = questions.next()

            with pytest.raises(errors.IllegalState):
                self.session.get_answers(section.ident, second_question.ident)

            form = self.session.get_response_form(section.ident, first_question.ident)
            self.session.submit_response(section.ident, first_question.ident, form)

            answers = self.session.get_answers(section.ident, first_question.ident)
            assert isinstance(answers, AnswerList)
            assert answers.available() == 1
            assert isinstance(answers.next(), Answer)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_answers(self.fake_id, self.fake_id)

    def test_finish_assessment(self):
        """Tests finish_assessment"""
        if not is_never_authz(self.service_config):
            future_start = DateTime.utcnow() + datetime.timedelta(days=1)
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
            form.set_start_time(DateTime(**{
                'year': future_start.year,
                'month': future_start.month,
                'day': future_start.day,
                'hour': future_start.hour,
                'minute': future_start.minute,
                'second': future_start.second
            }))
            future_offered = self.catalog.create_assessment_offered(form)
            form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
            future_taken = self.catalog.create_assessment_taken(form)
            with pytest.raises(errors.IllegalState):
                self.session.finish_assessment(future_taken.ident)

            assert self.taken._my_map['completionTime'] is None
            self.session.finish_assessment(self.taken.ident)
            taken = self.catalog.get_assessment_taken(self.taken.ident)
            assert taken._my_map['completionTime'] is not None
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.finish_assessment(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_results_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentResultsSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([SEQUENCE_ASSESSMENT])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentResultsSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)

        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = request.cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = request.cls.catalog.create_item(ifc)

            form = request.cls.catalog.get_question_form_for_create(test_item.ident, [])
            request.cls.catalog.create_question(form)

            request.cls.catalog.add_item(request.cls.assessment.ident, test_item.ident)

        form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_results_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for item in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(item.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_results_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr.get_assessment_results_session(proxy=request.cls.catalog._proxy)
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
        request.cls.taken = request.cls.catalog.create_assessment_taken(form)


@pytest.mark.usefixtures("assessment_results_session_class_fixture", "assessment_results_session_test_fixture")
class TestAssessmentResultsSession(object):
    """Tests for AssessmentResultsSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_access_assessment_results(self):
        """Tests can_access_assessment_results"""
        assert isinstance(self.session.can_access_assessment_results(), bool)

    def test_get_items(self):
        """Tests get_items"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            section.get_questions()
            assert self.session.get_items(self.taken.ident).available() == 4
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_items(self.fake_id)

    def test_get_responses(self):
        """Tests get_responses"""
        if not is_never_authz(self.service_config):
            section = self.catalog.get_first_assessment_section(self.taken.ident)
            questions = section.get_questions()

            test_responses = self.session.get_responses(self.taken.ident)
            assert isinstance(test_responses, ResponseList)
            assert test_responses.available() == 4
            first_response = test_responses.next()
            assert isinstance(first_response, Response)

            with pytest.raises(errors.IllegalState):
                first_response.object_map
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_responses(self.fake_id)

    def test_are_results_available(self):
        """Tests are_results_available"""
        if not is_never_authz(self.service_config):
            assert not self.session.are_results_available(self.assessment.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.are_results_available(self.fake_id)

    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.session.get_grade_entries(self.assessment.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_entries(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def item_lookup_session_test_fixture(request):
    request.cls.item_list = list()
    request.cls.item_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemLookupSession tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_item_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("item_lookup_session_class_fixture", "item_lookup_session_test_fixture")
class TestItemLookupSession(object):
    """Tests for ItemLookupSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_lookup_items(self):
        """Tests can_lookup_items"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_items(), bool)

    def test_use_comparative_item_view(self):
        """Tests use_comparative_item_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_item_view()

    def test_use_plenary_item_view(self):
        """Tests use_plenary_item_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_item_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_item(self):
        """Tests get_item"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_bank_view()
            obj = self.catalog.get_item(self.item_list[0].ident)
            assert obj.ident == self.item_list[0].ident
            self.catalog.use_federated_bank_view()
            obj = self.catalog.get_item(self.item_list[0].ident)
            assert obj.ident == self.item_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_item(self.fake_id)

    def test_get_items_by_ids(self):
        """Tests get_items_by_ids"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_ids(self.item_ids)
        assert isinstance(objects, ItemList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_ids(self.item_ids)
        assert isinstance(objects, ItemList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_items_by_genus_type(self):
        """Tests get_items_by_genus_type"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, ItemList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, ItemList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_items_by_parent_genus_type(self):
        """Tests get_items_by_parent_genus_type"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_items_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ItemList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_items_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, ItemList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_items_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_items_by_record_type(self):
        """Tests get_items_by_record_type"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, ItemList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, ItemList)

    def test_get_items_by_question(self):
        """Tests get_items_by_question"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_items_by_question(True)

    def test_get_items_by_answer(self):
        """Tests get_items_by_answer"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_items_by_answer(True)

    def test_get_items_by_learning_objective(self):
        """Tests get_items_by_learning_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_items_by_learning_objective(True)

    def test_get_items_by_learning_objectives(self):
        """Tests get_items_by_learning_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_items_by_learning_objectives(True)

    def test_get_items(self):
        """Tests get_items"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items()
        assert isinstance(objects, ItemList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items()
        assert isinstance(objects, ItemList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_item_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_item(self.item_ids[0], ALIAS_ID)
            obj = self.catalog.get_item(ALIAS_ID)
            assert obj.get_id() == self.item_ids[0]


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def item_query_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + color
            create_form.description = (
                'Test Item for ItemQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_item(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_item_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for item in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(item.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("item_query_session_class_fixture", "item_query_session_test_fixture")
class TestItemQuerySession(object):
    """Tests for ItemQuerySession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_search_items(self):
        """Tests can_search_items"""
        assert isinstance(self.session.can_search_items(), bool)

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_item_query(self):
        """Tests get_item_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_item_query()
        assert isinstance(query, ABCQueries.ItemQuery)

    def test_get_items_by_query(self):
        """Tests get_items_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_item_query()
            query.match_display_name('orange')
            assert self.catalog.get_items_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_items_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_items_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_search_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemSearchSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + color
            create_form.description = (
                'Test Item for ItemSearchSession tests, did I mention green')
            obj = request.cls.catalog.create_item(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_item_search_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for item in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(item.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_search_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("item_search_session_class_fixture", "item_search_session_test_fixture")
class TestItemSearchSession(object):
    """Tests for ItemSearchSession"""
    def test_get_item_search(self):
        """Tests get_item_search"""
        if not is_never_authz(self.service_config):
            search = self.session.get_item_search()
            assert isinstance(search, searches.ItemSearch)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_item_search()

    def test_get_item_search_order(self):
        """Tests get_item_search_order"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_item_search_order()

    def test_get_items_by_search(self):
        """Tests get_items_by_search"""
        if not is_never_authz(self.service_config):
            query = self.session.get_item_query()
            query.match_display_name('zxy', DEFAULT_STRING_MATCH_TYPE, True)
            search = self.session.get_item_search()
            results = self.session.get_items_by_search(query, search)
            assert isinstance(results, searches.ItemSearchResults)
            assert results.get_result_size() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_items_by_search('foo', 'foo')

    def test_get_item_query_from_inspector(self):
        """Tests get_item_query_from_inspector"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_item_query_from_inspector(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_item_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                for offered in request.cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in request.cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        request.cls.catalog.delete_assessment_taken(taken.ident)
                    request.cls.catalog.delete_assessment_offered(offered.ident)
                request.cls.catalog.delete_assessment(obj.ident)
            for item in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(item.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_admin_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_item_form_for_create([])
        request.cls.form.display_name = 'new Item'
        request.cls.form.description = 'description of Item'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_item(request.cls.form)
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("item_admin_session_class_fixture", "item_admin_session_test_fixture")
class TestItemAdminSession(object):
    """Tests for ItemAdminSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_create_items(self):
        """Tests can_create_items"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_items(), bool)

    def test_can_create_item_with_record_types(self):
        """Tests can_create_item_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_item_with_record_types(DEFAULT_TYPE), bool)

    def test_get_item_form_for_create(self):
        """Tests get_item_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_item_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_item_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_item_form_for_create([])

    def test_create_item(self):
        """Tests create_item"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import Item
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Item)
            assert self.osid_object.display_name.text == 'new Item'
            assert self.osid_object.description.text == 'description of Item'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_item(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_item('I Will Break You!')
            update_form = self.catalog.get_item_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_item(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_item('foo')

    def test_can_update_items(self):
        """Tests can_update_items"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_items(), bool)

    def test_get_item_form_for_update(self):
        """Tests get_item_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_item_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_item_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_item_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='assessment.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_item_form_for_update(self.fake_id)

    def test_update_item(self):
        """Tests update_item"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.assessment.objects import Item
            form = self.catalog.get_item_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_item(form)
            assert isinstance(updated_object, Item)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_item(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_item('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_item(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_item('foo')

    def test_can_delete_items(self):
        """Tests can_delete_items"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_items(), bool)

    def test_delete_item(self):
        """Tests delete_item"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_item_form_for_create([])
            form.display_name = 'new Item'
            form.description = 'description of Item'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_item(form)
            self.catalog.delete_item(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_item(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_item(self.fake_id)

    def test_can_manage_item_aliases(self):
        """Tests can_manage_item_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_item_aliases(), bool)

    def test_alias_item(self):
        """Tests alias_item"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_item(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_item(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_item(self.fake_id, self.fake_id)

    def test_can_create_questions(self):
        """Tests can_create_questions"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_questions(), bool)

    def test_can_create_question_with_record_types(self):
        """Tests can_create_question_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_question_with_record_types(DEFAULT_TYPE), bool)

    def test_get_question_form_for_create(self):
        """Tests get_question_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.session.get_question_form_for_create(self.osid_object.ident, [])
            assert isinstance(form, objects.QuestionForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_question_form_for_create(self.fake_id, [])

    def test_create_question(self):
        """Tests create_question"""
        if not is_never_authz(self.service_config):
            with pytest.raises(TypeError):
                # question_map = dict(self._my_map['question'])
                # TypeError: 'NoneType' object is not iterable
                self.osid_object.get_question()

            form = self.session.get_question_form_for_create(self.osid_object.ident, [])
            self.session.create_question(form)
            updated_item = self.catalog.get_item(self.osid_object.ident)
            assert isinstance(updated_item.get_question(), Question)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.create_question('foo')

    def test_can_update_questions(self):
        """Tests can_update_questions"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_questions(), bool)

    def test_get_question_form_for_update(self):
        """Tests get_question_form_for_update"""
        if not is_never_authz(self.service_config):
            form = self.session.get_question_form_for_create(self.osid_object.ident, [])
            question = self.session.create_question(form)

            form = self.session.get_question_form_for_update(question.ident)
            assert isinstance(form, objects.QuestionForm)
            assert form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_question_form_for_update(self.fake_id)

    def test_update_question(self):
        """Tests update_question"""
        if not is_never_authz(self.service_config):
            form = self.session.get_question_form_for_create(self.osid_object.ident, [])
            question = self.session.create_question(form)
            assert question.display_name.text == 'new Item'

            form = self.session.get_question_form_for_update(question.ident)
            form.display_name = 'second name'
            question = self.session.update_question(form)
            assert isinstance(question, objects.Question)
            assert question.display_name.text == 'second name'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.update_question('foo')

    def test_can_delete_questions(self):
        """Tests can_delete_questions"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_questions(), bool)

    def test_delete_question(self):
        """Tests delete_question"""
        if not is_never_authz(self.service_config):
            with pytest.raises(TypeError):
                # question_map = dict(self._my_map['question'])
                # TypeError: 'NoneType' object is not iterable
                self.osid_object.get_question()

            form = self.session.get_question_form_for_create(self.osid_object.ident, [])
            question = self.session.create_question(form)
            updated_item = self.catalog.get_item(self.osid_object.ident)
            assert isinstance(updated_item.get_question(), Question)

            with pytest.raises(errors.NotFound):
                self.session.delete_question(Id('fake.Package%3A000000000000000000000000%40ODL.MIT.EDU'))

            self.session.delete_question(question.ident)
            updated_item = self.catalog.get_item(self.osid_object.ident)

            with pytest.raises(TypeError):
                updated_item.get_question()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.delete_question(self.fake_id)

    def test_can_create_answers(self):
        """Tests can_create_answers"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_answers(), bool)

    def test_can_create_answers_with_record_types(self):
        """Tests can_create_answers_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_answers_with_record_types(DEFAULT_TYPE), bool)

    def test_get_answer_form_for_create(self):
        """Tests get_answer_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
            assert isinstance(form, objects.AnswerForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_answer_form_for_create(self.fake_id, [])

    def test_create_answer(self):
        """Tests create_answer"""
        if not is_never_authz(self.service_config):
            assert self.osid_object.get_answers().available() == 0
            form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
            self.session.create_answer(form)
            updated_item = self.catalog.get_item(self.osid_object.ident)
            assert updated_item.get_answers().available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_answer('foo')

    def test_can_update_answers(self):
        """Tests can_update_answers"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_answers(), bool)

    def test_get_answer_form_for_update(self):
        """Tests get_answer_form_for_update"""
        if not is_never_authz(self.service_config):
            form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
            answer = self.session.create_answer(form)

            form = self.session.get_answer_form_for_update(answer.ident)
            assert isinstance(form, objects.AnswerForm)
            assert form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_answer_form_for_update(self.fake_id)

    def test_update_answer(self):
        """Tests update_answer"""
        if not is_never_authz(self.service_config):
            form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
            form.display_name = 'first name'
            answer = self.session.create_answer(form)
            assert answer.display_name.text == 'first name'

            form = self.session.get_answer_form_for_update(answer.ident)
            form.display_name = 'second name'
            answer = self.session.update_answer(form)
            assert isinstance(answer, objects.Answer)
            assert answer.display_name.text == 'second name'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.update_answer('foo')

    def test_can_delete_answers(self):
        """Tests can_delete_answers"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_answers(), bool)

    def test_delete_answer(self):
        """Tests delete_answer"""
        if not is_never_authz(self.service_config):
            assert self.osid_object.get_answers().available() == 0
            form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
            answer = self.session.create_answer(form)
            updated_item = self.catalog.get_item(self.osid_object.ident)
            assert updated_item.get_answers().available() == 1

            with pytest.raises(errors.NotFound):
                self.session.delete_answer(Id('fake.Package%3A000000000000000000000000%40ODL.MIT.EDU'))

            self.session.delete_answer(answer.ident)
            updated_item = self.catalog.get_item(self.osid_object.ident)
            assert updated_item.get_answers().available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.delete_answer(self.fake_id)


class NotificationReceiver(object):
    # Implemented from resource.ResourceNotificationSession
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_notification_session_class_fixture(request):
    # Implemented from init template for ResourceNotificationSession
    request.cls.service_config = request.param
    request.cls.item_list = list()
    request.cls.item_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemNotificationSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemNotificationSession tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)

    else:
        request.cls.catalog = request.cls.svc_mgr.get_item_notification_session(NotificationReceiver(), proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_notification_session_test_fixture(request):
    # From test_templates/resource.py::ResourceNotificationSession::init_template
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("item_notification_session_class_fixture", "item_notification_session_test_fixture")
class TestItemNotificationSession(object):
    """Tests for ItemNotificationSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_register_for_item_notifications(self):
        """Tests can_register_for_item_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::can_register_for_resource_notifications_template
        if is_no_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.session.can_register_for_item_notifications()
        else:
            assert isinstance(self.session.can_register_for_item_notifications(), bool)

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_reliable_item_notifications(self):
        """Tests reliable_item_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::reliable_resource_notifications_template
        self.session.reliable_item_notifications()

    def test_unreliable_item_notifications(self):
        """Tests unreliable_item_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::unreliable_resource_notifications_template
        self.session.unreliable_item_notifications()

    def test_acknowledge_item_notification(self):
        """Tests acknowledge_item_notification"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.acknowledge_item_notification(True)

    def test_register_for_new_items(self):
        """Tests register_for_new_items"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_new_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_new_items()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_new_items()

    def test_register_for_changed_items(self):
        """Tests register_for_changed_items"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_items()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_items()

    def test_register_for_changed_item(self):
        """Tests register_for_changed_item"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_item(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_item(self.fake_id)

    def test_register_for_deleted_items(self):
        """Tests register_for_deleted_items"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_deleted_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_items()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_items()

    def test_register_for_deleted_item(self):
        """Tests register_for_deleted_item"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_deleted_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_item(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_item(self.fake_id)

    def test_reliable_item_notifications(self):
        """Tests reliable_item_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::reliable_resource_notifications_template
        self.session.reliable_item_notifications()

    def test_unreliable_item_notifications(self):
        """Tests unreliable_item_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::unreliable_resource_notifications_template
        self.session.unreliable_item_notifications()

    def test_acknowledge_item_notification(self):
        """Tests acknowledge_item_notification"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.acknowledge_item_notification(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_bank_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.item_list = list()
    request.cls.item_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for ItemBankSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemBankSession tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)
        request.cls.svc_mgr.assign_item_to_bank(
            request.cls.item_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_item_to_bank(
            request.cls.item_ids[2], request.cls.assigned_catalog.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_item_bank_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_item_from_bank(
                request.cls.item_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_item_from_bank(
                request.cls.item_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_bank_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("item_bank_session_class_fixture", "item_bank_session_test_fixture")
class TestItemBankSession(object):
    """Tests for ItemBankSession"""
    def test_can_lookup_item_bank_mappings(self):
        """Tests can_lookup_item_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_item_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_item_ids_by_bank(self):
        """Tests get_item_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_item_ids_by_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_item_ids_by_bank(self.fake_id)

    def test_get_items_by_bank(self):
        """Tests get_items_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_items_by_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.ItemList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_items_by_bank(self.fake_id)

    def test_get_item_ids_by_banks(self):
        """Tests get_item_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_item_ids_by_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_item_ids_by_banks([self.fake_id])

    def test_get_items_by_banks(self):
        """Tests get_items_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_items_by_banks(catalog_ids)
            assert isinstance(results, ABCObjects.ItemList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_items_by_banks([self.fake_id])

    def test_get_bank_ids_by_item(self):
        """Tests get_bank_ids_by_item"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bank_ids_by_item(self.item_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_ids_by_item(self.fake_id)

    def test_get_banks_by_item(self):
        """Tests get_banks_by_item"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_banks_by_item(self.item_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_item(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_bank_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.item_list = list()
    request.cls.item_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for ItemBankAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemBankAssignmentSession tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_bank_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("item_bank_assignment_session_class_fixture", "item_bank_assignment_session_test_fixture")
class TestItemBankAssignmentSession(object):
    """Tests for ItemBankAssignmentSession"""
    def test_can_assign_items(self):
        """Tests can_assign_items"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_items()
        assert isinstance(result, bool)

    def test_can_assign_items_to_bank(self):
        """Tests can_assign_items_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_items_to_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids(self.fake_id)

    def test_get_assignable_bank_ids_for_item(self):
        """Tests get_assignable_bank_ids_for_item"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids_for_item(self.catalog.ident, self.item_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids_for_item(self.fake_id, self.fake_id)

    def test_assign_item_to_bank(self):
        """Tests assign_item_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_items()
            assert results.available() == 0
            self.session.assign_item_to_bank(self.item_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_items()
            assert results.available() == 1
            self.session.unassign_item_from_bank(
                self.item_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_item_to_bank(self.fake_id, self.fake_id)

    def test_unassign_item_from_bank(self):
        """Tests unassign_item_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_items()
            assert results.available() == 0
            self.session.assign_item_to_bank(
                self.item_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_items()
            assert results.available() == 1
            self.session.unassign_item_from_bank(
                self.item_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_items()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_item_from_bank(self.fake_id, self.fake_id)

    def test_reassign_item_to_billing(self):
        """Tests reassign_item_to_billing"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_item_to_billing(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_lookup_session_test_fixture(request):
    request.cls.assessment_list = list()
    request.cls.assessment_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentLookupSession tests'
            obj = request.cls.catalog.create_assessment(create_form)
            request.cls.assessment_list.append(obj)
            request.cls.assessment_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_lookup_session_class_fixture", "assessment_lookup_session_test_fixture")
class TestAssessmentLookupSession(object):
    """Tests for AssessmentLookupSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_lookup_assessments(self):
        """Tests can_lookup_assessments"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_assessments(), bool)

    def test_use_comparative_assessment_view(self):
        """Tests use_comparative_assessment_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_view()

    def test_use_plenary_assessment_view(self):
        """Tests use_plenary_assessment_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment(self):
        """Tests get_assessment"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_bank_view()
            obj = self.catalog.get_assessment(self.assessment_list[0].ident)
            assert obj.ident == self.assessment_list[0].ident
            self.catalog.use_federated_bank_view()
            obj = self.catalog.get_assessment(self.assessment_list[0].ident)
            assert obj.ident == self.assessment_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_assessment(self.fake_id)

    def test_get_assessments_by_ids(self):
        """Tests get_assessments_by_ids"""
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_ids(self.assessment_ids)
        assert isinstance(objects, AssessmentList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_ids(self.assessment_ids)
        assert isinstance(objects, AssessmentList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assessments_by_genus_type(self):
        """Tests get_assessments_by_genus_type"""
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, AssessmentList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, AssessmentList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assessments_by_parent_genus_type(self):
        """Tests get_assessments_by_parent_genus_type"""
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_assessments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssessmentList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, AssessmentList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_assessments_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assessments_by_record_type(self):
        """Tests get_assessments_by_record_type"""
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, AssessmentList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, AssessmentList)

    def test_get_assessments(self):
        """Tests get_assessments"""
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments()
        assert isinstance(objects, AssessmentList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments()
        assert isinstance(objects, AssessmentList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assessment_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_assessment(self.assessment_ids[0], ALIAS_ID)
            obj = self.catalog.get_assessment(ALIAS_ID)
            assert obj.get_id() == self.assessment_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def assessment_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.assessment_list = list()
    request.cls.assessment_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + color
            create_form.description = (
                'Test Assessment for AssessmentQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_assessment(create_form)
            request.cls.assessment_list.append(obj)
            request.cls.assessment_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_query_session_class_fixture", "assessment_query_session_test_fixture")
class TestAssessmentQuerySession(object):
    """Tests for AssessmentQuerySession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_search_assessments(self):
        """Tests can_search_assessments"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_assessments(), bool)

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_query()
        assert isinstance(query, ABCQueries.AssessmentQuery)

    def test_get_assessments_by_query(self):
        """Tests get_assessments_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_assessment_query()
            query.match_display_name('orange')
            assert self.catalog.get_assessments_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_assessments_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_assessment_form_for_create([])
        request.cls.form.display_name = 'new Assessment'
        request.cls.form.description = 'description of Assessment'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_assessment(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_assessment(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_admin_session_class_fixture", "assessment_admin_session_test_fixture")
class TestAssessmentAdminSession(object):
    """Tests for AssessmentAdminSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_create_assessments(self):
        """Tests can_create_assessments"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_assessments(), bool)

    def test_can_create_assessment_with_record_types(self):
        """Tests can_create_assessment_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_assessment_with_record_types(DEFAULT_TYPE), bool)

    def test_get_assessment_form_for_create(self):
        """Tests get_assessment_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_form_for_create([])

    def test_create_assessment(self):
        """Tests create_assessment"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import Assessment
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Assessment)
            assert self.osid_object.display_name.text == 'new Assessment'
            assert self.osid_object.description.text == 'description of Assessment'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_assessment(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment('I Will Break You!')
            update_form = self.catalog.get_assessment_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_assessment('foo')

    def test_can_update_assessments(self):
        """Tests can_update_assessments"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_assessments(), bool)

    def test_get_assessment_form_for_update(self):
        """Tests get_assessment_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='assessment.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_form_for_update(self.fake_id)

    def test_update_assessment(self):
        """Tests update_assessment"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.assessment.objects import Assessment
            form = self.catalog.get_assessment_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_assessment(form)
            assert isinstance(updated_object, Assessment)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_assessment(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_assessment('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_assessment(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_assessment('foo')

    def test_can_delete_assessments(self):
        """Tests can_delete_assessments"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_assessments(), bool)

    def test_delete_assessment(self):
        """Tests delete_assessment"""
        # From test_templates/learning.py::ObjectiveAdminSession::delete_objective_template
        if not is_never_authz(self.service_config):
            results = self.catalog.get_assessments()
            assert results.available() == 1

            form = self.catalog.get_assessment_form_for_create([])
            form.display_name = 'new Assessment'
            form.description = 'description of Assessment'
            new_assessment = self.catalog.create_assessment(form)

            results = self.catalog.get_assessments()
            assert results.available() == 2

            self.session.delete_assessment(new_assessment.ident)

            results = self.catalog.get_assessments()
            assert results.available() == 1
            assert str(results.next().ident) != str(new_assessment.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_assessment(self.fake_id)

    def test_can_manage_assessment_aliases(self):
        """Tests can_manage_assessment_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_assessment_aliases(), bool)

    def test_alias_assessment(self):
        """Tests alias_assessment"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_assessment(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_assessment(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_assessment(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_bank_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.assessment_list = list()
    request.cls.assessment_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentBankSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentBankSession tests'
            obj = request.cls.catalog.create_assessment(create_form)
            request.cls.assessment_list.append(obj)
            request.cls.assessment_ids.append(obj.ident)
        request.cls.svc_mgr.assign_assessment_to_bank(
            request.cls.assessment_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_assessment_to_bank(
            request.cls.assessment_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_assessment_from_bank(
                request.cls.assessment_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_assessment_from_bank(
                request.cls.assessment_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_bank_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_bank_session_class_fixture", "assessment_bank_session_test_fixture")
class TestAssessmentBankSession(object):
    """Tests for AssessmentBankSession"""
    def test_can_lookup_assessment_bank_mappings(self):
        """Tests can_lookup_assessment_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_ids_by_bank(self):
        """Tests get_assessment_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_assessment_ids_by_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_assessment_ids_by_bank(self.fake_id)

    def test_get_assessments_by_bank(self):
        """Tests get_assessments_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_assessments_by_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AssessmentList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_by_bank(self.fake_id)

    def test_get_assessment_ids_by_banks(self):
        """Tests get_assessment_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_assessment_ids_by_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_ids_by_banks([self.fake_id])

    def test_get_assessments_by_banks(self):
        """Tests get_assessments_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_assessments_by_banks(catalog_ids)
            assert isinstance(results, ABCObjects.AssessmentList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_by_banks([self.fake_id])

    def test_get_bank_ids_by_assessment(self):
        """Tests get_bank_ids_by_assessment"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bank_ids_by_assessment(self.assessment_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_ids_by_assessment(self.fake_id)

    def test_get_banks_by_assessment(self):
        """Tests get_banks_by_assessment"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_banks_by_assessment(self.assessment_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_assessment(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_bank_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.assessment_list = list()
    request.cls.assessment_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentBankAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentBankAssignmentSession tests'
            obj = request.cls.catalog.create_assessment(create_form)
            request.cls.assessment_list.append(obj)
            request.cls.assessment_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_bank_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_bank_assignment_session_class_fixture", "assessment_bank_assignment_session_test_fixture")
class TestAssessmentBankAssignmentSession(object):
    """Tests for AssessmentBankAssignmentSession"""
    def test_can_assign_assessments(self):
        """Tests can_assign_assessments"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessments()
        assert isinstance(result, bool)

    def test_can_assign_assessments_to_bank(self):
        """Tests can_assign_assessments_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessments_to_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids(self.fake_id)

    def test_get_assignable_bank_ids_for_assessment(self):
        """Tests get_assignable_bank_ids_for_assessment"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids_for_assessment(self.catalog.ident, self.assessment_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids_for_assessment(self.fake_id, self.fake_id)

    def test_assign_assessment_to_bank(self):
        """Tests assign_assessment_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessments()
            assert results.available() == 0
            self.session.assign_assessment_to_bank(self.assessment_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments()
            assert results.available() == 1
            self.session.unassign_assessment_from_bank(
                self.assessment_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_assessment_to_bank(self.fake_id, self.fake_id)

    def test_unassign_assessment_from_bank(self):
        """Tests unassign_assessment_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessments()
            assert results.available() == 0
            self.session.assign_assessment_to_bank(
                self.assessment_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments()
            assert results.available() == 1
            self.session.unassign_assessment_from_bank(
                self.assessment_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_assessment_from_bank(self.fake_id, self.fake_id)

    def test_reassign_assessment_to_billing(self):
        """Tests reassign_assessment_to_billing"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_assessment_to_billing(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_basic_authoring_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()
    simple_sequence_record_type = Type(**{
        'authority': 'ODL.MIT.EDU',
        'namespace': 'osid-object',
        'identifier': 'simple-child-sequencing'})
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBasicAuthoringSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([simple_sequence_record_type])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentBasicAuthoringSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        request.cls.test_items = list()
        request.cls.test_item_ids = list()
        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = request.cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = request.cls.catalog.create_item(ifc)
            request.cls.test_items.append(test_item)
            request.cls.test_item_ids.append(test_item.ident)
            request.cls.catalog.add_item(request.cls.assessment.ident, test_item.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_basic_authoring_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_basic_authoring_session_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_basic_authoring_session_class_fixture", "assessment_basic_authoring_session_test_fixture")
class TestAssessmentBasicAuthoringSession(object):
    """Tests for AssessmentBasicAuthoringSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_author_assessments(self):
        """Tests can_author_assessments"""
        assert isinstance(self.catalog.can_author_assessments(), bool)

    def test_get_items(self):
        """Tests get_items"""
        if not is_never_authz(self.service_config):
            assert self.catalog.get_assessment_items(self.assessment.ident).available() == 4
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_items(self.fake_id)

    def test_add_item(self):
        """Tests add_item"""
        if not is_never_authz(self.service_config):
            self._reorder_items()
            ifc = self.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Additional Item')
            ifc.set_description('This is an addtional Test Item')
            additional_item = self.catalog.create_item(ifc)
            self.catalog.add_item(self.assessment.ident, additional_item.ident)
            assert self.catalog.get_assessment_items(self.assessment.ident).available() == 5
            self.catalog.remove_item(self.assessment.ident, additional_item.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.add_item(self.fake_id, self.fake_id)

    def test_remove_item(self):
        """Tests remove_item"""
        if not is_never_authz(self.service_config):
            self._reorder_items()
            self.catalog.remove_item(self.assessment.ident, self.test_item_ids[1])
            assert self.catalog.get_assessment_items(self.assessment.ident).available() == 3
            self.catalog.add_item(self.assessment.ident, self.test_item_ids[1])
            items = self.catalog.get_assessment_items(self.assessment.ident)
            assert items.next().ident == self.test_item_ids[0]
            assert items.next().ident == self.test_item_ids[2]
            assert items.next().ident == self.test_item_ids[3]
            assert items.next().ident == self.test_item_ids[1]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.remove_item(self.fake_id, self.fake_id)

    def test_move_item(self):
        """Tests move_item"""
        if not is_never_authz(self.service_config):
            self._reorder_items()
            self.catalog.move_item(self.assessment.ident, self.test_item_ids[0], self.test_item_ids[3])
            items = self.catalog.get_assessment_items(self.assessment.ident)
            assert items.next().ident == self.test_item_ids[1]
            assert items.next().ident == self.test_item_ids[2]
            assert items.next().ident == self.test_item_ids[3]
            assert items.next().ident == self.test_item_ids[0]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.move_item(self.fake_id, self.fake_id, self.fake_id)

    def test_order_items(self):
        """Tests order_items"""
        if not is_never_authz(self.service_config):
            self.catalog.order_items([
                self.test_item_ids[3],
                self.test_item_ids[2],
                self.test_item_ids[1],
                self.test_item_ids[0]],
                self.assessment.ident)
            assert self.catalog.get_assessment_items(self.assessment.ident).next().ident == self.test_item_ids[3]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.order_items([self.fake_id, self.fake_id], self.fake_id)

    def _reorder_items(self):
        self.catalog.order_items([
            self.test_item_ids[0],
            self.test_item_ids[1],
            self.test_item_ids[2],
            self.test_item_ids[3]],
            self.assessment.ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_offered_lookup_session_test_fixture(request):
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedLookupSession tests'
            obj = request.cls.catalog.create_assessment_offered(create_form)
            request.cls.assessment_offered_list.append(obj)
            request.cls.assessment_offered_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_offered_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_offered_lookup_session_class_fixture", "assessment_offered_lookup_session_test_fixture")
class TestAssessmentOfferedLookupSession(object):
    """Tests for AssessmentOfferedLookupSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_lookup_assessments_offered(self):
        """Tests can_lookup_assessments_offered"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_assessments_offered(), bool)

    def test_use_comparative_assessment_offered_view(self):
        """Tests use_comparative_assessment_offered_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_offered_view()

    def test_use_plenary_assessment_offered_view(self):
        """Tests use_plenary_assessment_offered_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_offered_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_offered(self):
        """Tests get_assessment_offered"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_assessment_offered_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_bank_view()
                obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
                assert obj.ident == self.assessment_offered_list[0].ident
                self.catalog.use_federated_bank_view()
                obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
                assert obj.ident == self.assessment_offered_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_assessment_offered(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_bank_view()
                obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
                assert obj.ident == self.assessment_offered_list[0].ident
                self.catalog.use_federated_bank_view()
                obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
                assert obj.ident == self.assessment_offered_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessment_offered(self.fake_id)

    def test_get_assessments_offered_by_ids(self):
        """Tests get_assessments_offered_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        if self.svc_mgr.supports_assessment_offered_query():
            objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
            assert isinstance(objects, AssessmentOfferedList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
            assert isinstance(objects, AssessmentOfferedList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
                assert isinstance(objects, AssessmentOfferedList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
                assert objects.available() > 0
                assert isinstance(objects, AssessmentOfferedList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)

    def test_get_assessments_offered_by_genus_type(self):
        """Tests get_assessments_offered_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        if self.svc_mgr.supports_assessment_offered_query():
            objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssessmentOfferedList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssessmentOfferedList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AssessmentOfferedList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, AssessmentOfferedList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assessments_offered_by_parent_genus_type(self):
        """Tests get_assessments_offered_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        if self.svc_mgr.supports_assessment_offered_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AssessmentOfferedList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AssessmentOfferedList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AssessmentOfferedList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AssessmentOfferedList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assessments_offered_by_record_type(self):
        """Tests get_assessments_offered_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        if self.svc_mgr.supports_assessment_offered_query():
            objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, AssessmentOfferedList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, AssessmentOfferedList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, AssessmentOfferedList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AssessmentOfferedList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)

    def test_get_assessments_offered_by_date(self):
        """Tests get_assessments_offered_by_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_offered_by_date(True, True)

    def test_get_assessments_offered_for_assessment(self):
        """Tests get_assessments_offered_for_assessment"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        if self.svc_mgr.supports_assessment_offered_query():
            results = self.session.get_assessments_offered_for_assessment(self.assessment.ident)
            assert isinstance(results, ABCObjects.AssessmentOfferedList)
            if not is_never_authz(self.service_config):
                assert results.available() == 2
            else:
                assert results.available() == 0
        else:
            if not is_never_authz(self.service_config):
                results = self.session.get_assessments_offered_for_assessment(self.assessment.ident)
                assert results.available() == 2
                assert isinstance(results, ABCObjects.AssessmentOfferedList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.session.get_assessments_offered_for_assessment(self.fake_id)

    def test_get_assessments_offered(self):
        """Tests get_assessments_offered"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        if self.svc_mgr.supports_assessment_offered_query():
            objects = self.catalog.get_assessments_offered()
            assert isinstance(objects, AssessmentOfferedList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_offered()
            assert isinstance(objects, AssessmentOfferedList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_offered()
                assert isinstance(objects, AssessmentOfferedList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_offered()
                assert objects.available() > 0
                assert isinstance(objects, AssessmentOfferedList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_offered()

    def test_get_assessment_offered_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_assessment_offered(self.assessment_offered_ids[0], ALIAS_ID)
            obj = self.catalog.get_assessment_offered(ALIAS_ID)
            assert obj.get_id() == self.assessment_offered_ids[0]


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_offered_query_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedQuerySession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + color
            create_form.description = (
                'Test AssessmentOffered for AssessmentOfferedQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_assessment_offered(create_form)
            request.cls.assessment_offered_list.append(obj)
            request.cls.assessment_offered_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_offered_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.mark.usefixtures("assessment_offered_query_session_class_fixture", "assessment_offered_query_session_test_fixture")
class TestAssessmentOfferedQuerySession(object):
    """Tests for AssessmentOfferedQuerySession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_search_assessments_offered(self):
        """Tests can_search_assessments_offered"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_assessments_offered(), bool)

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_offered_query()
        assert isinstance(query, ABCQueries.AssessmentOfferedQuery)

    def test_get_assessments_offered_by_query(self):
        """Tests get_assessments_offered_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_assessment_offered_query()
            query.match_display_name('orange')
            assert self.catalog.get_assessments_offered_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_assessments_offered_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_offered_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedAdminSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedAdminSession tests'
            obj = request.cls.catalog.create_assessment_offered(create_form)
            request.cls.assessment_offered_list.append(obj)
            request.cls.assessment_offered_ids.append(obj.ident)
        request.cls.form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        request.cls.form.display_name = 'new AssessmentOffered'
        request.cls.form.description = 'description of AssessmentOffered'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_assessment_offered(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_offered_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_taken():
                request.cls.catalog.delete_assessment_taken(obj.ident)
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_admin_session_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_offered_admin_session_class_fixture", "assessment_offered_admin_session_test_fixture")
class TestAssessmentOfferedAdminSession(object):
    """Tests for AssessmentOfferedAdminSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_create_assessments_offered(self):
        """Tests can_create_assessments_offered"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_assessments_offered(), bool)

    def test_can_create_assessment_offered_with_record_types(self):
        """Tests can_create_assessment_offered_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_assessment_offered_with_record_types(DEFAULT_TYPE), bool)

    def test_get_assessment_offered_form_for_create(self):
        """Tests get_assessment_offered_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_offered_form_for_create(self.fake_id, [])

    def test_create_assessment_offered(self):
        """Tests create_assessment_offered"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOffered
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, AssessmentOffered)
            assert self.osid_object.display_name.text == 'new AssessmentOffered'
            assert self.osid_object.description.text == 'description of AssessmentOffered'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_assessment_offered(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment_offered('I Will Break You!')
            update_form = self.catalog.get_assessment_offered_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment_offered(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_assessment_offered('foo')

    def test_can_update_assessments_offered(self):
        """Tests can_update_assessments_offered"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_assessments_offered(), bool)

    def test_get_assessment_offered_form_for_update(self):
        """Tests get_assessment_offered_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_offered_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_offered_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_offered_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='assessment.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_offered_form_for_update(self.fake_id)

    def test_update_assessment_offered(self):
        """Tests update_assessment_offered"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.assessment.objects import AssessmentOffered
            form = self.catalog.get_assessment_offered_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_assessment_offered(form)
            assert isinstance(updated_object, AssessmentOffered)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_assessment_offered(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_assessment_offered('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_assessment_offered(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_assessment_offered('foo')

    def test_can_delete_assessments_offered(self):
        """Tests can_delete_assessments_offered"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_assessments_offered(), bool)

    def test_delete_assessment_offered(self):
        """Tests delete_assessment_offered"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
            form.display_name = 'new Assessment Offered'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_assessment_offered(form)
            self.catalog.delete_assessment_offered(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_assessment_offered(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_assessment_offered(self.fake_id)

    def test_can_manage_assessment_offered_aliases(self):
        """Tests can_manage_assessment_offered_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_assessment_offered_aliases(), bool)

    def test_alias_assessment_offered(self):
        """Tests alias_assessment_offered"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_assessment_offered(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_assessment_offered(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_assessment_offered(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_bank_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentOfferedBankSession tests'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedBankSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedBankSession tests'
            obj = request.cls.catalog.create_assessment_offered(create_form)
            request.cls.assessment_offered_list.append(obj)
            request.cls.assessment_offered_ids.append(obj.ident)
        request.cls.svc_mgr.assign_assessment_offered_to_bank(
            request.cls.assessment_offered_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_assessment_offered_to_bank(
            request.cls.assessment_offered_ids[2], request.cls.assigned_catalog.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_offered_bank_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_assessment_offered_from_bank(
                request.cls.assessment_offered_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_assessment_offered_from_bank(
                request.cls.assessment_offered_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_bank_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_offered_bank_session_class_fixture", "assessment_offered_bank_session_test_fixture")
class TestAssessmentOfferedBankSession(object):
    """Tests for AssessmentOfferedBankSession"""
    def test_can_lookup_assessment_offered_bank_mappings(self):
        """Tests can_lookup_assessment_offered_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_offered_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_offered_ids_by_bank(self):
        """Tests get_assessment_offered_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_assessment_offered_ids_by_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_assessment_offered_ids_by_bank(self.fake_id)

    def test_get_assessments_offered_by_bank(self):
        """Tests get_assessments_offered_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_assessments_offered_by_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AssessmentOfferedList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_offered_by_bank(self.fake_id)

    def test_get_assessment_offered_ids_by_banks(self):
        """Tests get_assessment_offered_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_assessment_offered_ids_by_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_offered_ids_by_banks([self.fake_id])

    def test_get_assessments_offered_by_banks(self):
        """Tests get_assessments_offered_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_assessments_offered_by_banks(catalog_ids)
            assert isinstance(results, ABCObjects.AssessmentOfferedList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_offered_by_banks([self.fake_id])

    def test_get_bank_ids_by_assessment_offered(self):
        """Tests get_bank_ids_by_assessment_offered"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bank_ids_by_assessment_offered(self.assessment_offered_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_ids_by_assessment_offered(self.fake_id)

    def test_get_banks_by_assessment_offered(self):
        """Tests get_banks_by_assessment_offered"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_banks_by_assessment_offered(self.assessment_offered_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_assessment_offered(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_bank_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_offered_list = list()
    request.cls.assessment_offered_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentOfferedBankAssignmentSession tests'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedBankAssignmentSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedBankAssignmentSession tests'
            obj = request.cls.catalog.create_assessment_offered(create_form)
            request.cls.assessment_offered_list.append(obj)
            request.cls.assessment_offered_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_offered_bank_assignment_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_bank_assignment_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_offered_bank_assignment_session_class_fixture", "assessment_offered_bank_assignment_session_test_fixture")
class TestAssessmentOfferedBankAssignmentSession(object):
    """Tests for AssessmentOfferedBankAssignmentSession"""
    def test_can_assign_assessments_offered(self):
        """Tests can_assign_assessments_offered"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessments_offered()
        assert isinstance(result, bool)

    def test_can_assign_assessments_offered_to_bank(self):
        """Tests can_assign_assessments_offered_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessments_offered_to_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids(self.fake_id)

    def test_get_assignable_bank_ids_for_assessment_offered(self):
        """Tests get_assignable_bank_ids_for_assessment_offered"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids_for_assessment_offered(self.catalog.ident, self.assessment_offered_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids_for_assessment_offered(self.fake_id, self.fake_id)

    def test_assign_assessment_offered_to_bank(self):
        """Tests assign_assessment_offered_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessments_offered()
            assert results.available() == 0
            self.session.assign_assessment_offered_to_bank(self.assessment_offered_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments_offered()
            assert results.available() == 1
            self.session.unassign_assessment_offered_from_bank(
                self.assessment_offered_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_assessment_offered_to_bank(self.fake_id, self.fake_id)

    def test_unassign_assessment_offered_from_bank(self):
        """Tests unassign_assessment_offered_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessments_offered()
            assert results.available() == 0
            self.session.assign_assessment_offered_to_bank(
                self.assessment_offered_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments_offered()
            assert results.available() == 1
            self.session.unassign_assessment_offered_from_bank(
                self.assessment_offered_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments_offered()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_assessment_offered_from_bank(self.fake_id, self.fake_id)

    def test_reassign_assessment_offered_to_billing(self):
        """Tests reassign_assessment_offered_to_billing"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_assessment_offered_to_billing(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_taken_lookup_session_test_fixture(request):
    request.cls.assessment_taken_list = list()
    request.cls.assessment_taken_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenLookupSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenLookupSession tests'
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenLookupSession tests'
            obj = request.cls.catalog.create_assessment_taken(create_form)
            request.cls.assessment_taken_list.append(obj)
            request.cls.assessment_taken_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_taken_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                for obj in catalog.get_assessments():
                    for offered in catalog.get_assessments_offered_for_assessment(obj.ident):
                        for taken in catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                            catalog.delete_assessment_taken(taken.ident)
                        catalog.delete_assessment_offered(offered.ident)
                    catalog.delete_assessment(obj.ident)
                for obj in catalog.get_items():
                    catalog.delete_item(obj.ident)
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_taken_lookup_session_class_fixture", "assessment_taken_lookup_session_test_fixture")
class TestAssessmentTakenLookupSession(object):
    """Tests for AssessmentTakenLookupSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_lookup_assessments_taken(self):
        """Tests can_lookup_assessments_taken"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_assessments_taken(), bool)

    def test_use_comparative_assessment_taken_view(self):
        """Tests use_comparative_assessment_taken_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_taken_view()

    def test_use_plenary_assessment_taken_view(self):
        """Tests use_plenary_assessment_taken_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_taken_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_taken(self):
        """Tests get_assessment_taken"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_assessment_taken_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_bank_view()
                obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
                assert obj.ident == self.assessment_taken_list[0].ident
                self.catalog.use_federated_bank_view()
                obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
                assert obj.ident == self.assessment_taken_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_assessment_taken(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_bank_view()
                obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
                assert obj.ident == self.assessment_taken_list[0].ident
                self.catalog.use_federated_bank_view()
                obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
                assert obj.ident == self.assessment_taken_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessment_taken(self.fake_id)

    def test_get_assessments_taken_by_ids(self):
        """Tests get_assessments_taken_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        if self.svc_mgr.supports_assessment_taken_query():
            objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
            assert isinstance(objects, AssessmentTakenList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
            assert isinstance(objects, AssessmentTakenList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
                assert isinstance(objects, AssessmentTakenList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
                assert objects.available() > 0
                assert isinstance(objects, AssessmentTakenList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)

    def test_get_assessments_taken_by_genus_type(self):
        """Tests get_assessments_taken_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        if self.svc_mgr.supports_assessment_taken_query():
            objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssessmentTakenList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssessmentTakenList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AssessmentTakenList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, AssessmentTakenList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assessments_taken_by_parent_genus_type(self):
        """Tests get_assessments_taken_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        if self.svc_mgr.supports_assessment_taken_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AssessmentTakenList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AssessmentTakenList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AssessmentTakenList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AssessmentTakenList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assessments_taken_by_record_type(self):
        """Tests get_assessments_taken_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        if self.svc_mgr.supports_assessment_taken_query():
            objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, AssessmentTakenList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, AssessmentTakenList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, AssessmentTakenList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AssessmentTakenList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)

    def test_get_assessments_taken_by_date(self):
        """Tests get_assessments_taken_by_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_by_date(True, True)

    def test_get_assessments_taken_for_taker(self):
        """Tests get_assessments_taken_for_taker"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_for_taker(True)

    def test_get_assessments_taken_by_date_for_taker(self):
        """Tests get_assessments_taken_by_date_for_taker"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_by_date_for_taker(True, True, True)

    def test_get_assessments_taken_for_assessment(self):
        """Tests get_assessments_taken_for_assessment"""
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        if not is_never_authz(self.service_config):
            takens = self.session.get_assessments_taken_for_assessment(self.assessment.ident)
            assert isinstance(takens, AssessmentTakenList)
            assert takens.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_taken_for_assessment(self.fake_id)

    def test_get_assessments_taken_by_date_for_assessment(self):
        """Tests get_assessments_taken_by_date_for_assessment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_by_date_for_assessment(True, True, True)

    def test_get_assessments_taken_for_taker_and_assessment(self):
        """Tests get_assessments_taken_for_taker_and_assessment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_for_taker_and_assessment(True, True)

    def test_get_assessments_taken_by_date_for_taker_and_assessment(self):
        """Tests get_assessments_taken_by_date_for_taker_and_assessment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_by_date_for_taker_and_assessment(True, True, True, True)

    def test_get_assessments_taken_for_assessment_offered(self):
        """Tests get_assessments_taken_for_assessment_offered"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        if self.svc_mgr.supports_assessment_taken_query():
            results = self.session.get_assessments_taken_for_assessment_offered(self.assessment_offered.ident)
            assert isinstance(results, ABCObjects.AssessmentTakenList)
            if not is_never_authz(self.service_config):
                assert results.available() == 2
            else:
                assert results.available() == 0
        else:
            if not is_never_authz(self.service_config):
                results = self.session.get_assessments_taken_for_assessment_offered(self.assessment_offered.ident)
                assert results.available() == 2
                assert isinstance(results, ABCObjects.AssessmentTakenList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.session.get_assessments_taken_for_assessment_offered(self.fake_id)

    def test_get_assessments_taken_by_date_for_assessment_offered(self):
        """Tests get_assessments_taken_by_date_for_assessment_offered"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_by_date_for_assessment_offered(True, True, True)

    def test_get_assessments_taken_for_taker_and_assessment_offered(self):
        """Tests get_assessments_taken_for_taker_and_assessment_offered"""
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        takens = self.session.get_assessments_taken_for_taker_and_assessment_offered(
            self.catalog._proxy.get_effective_agent_id(),
            self.assessment_offered.ident)
        assert isinstance(takens, AssessmentTakenList)
        if not is_never_authz(self.service_config):
            assert takens.available() == 2
        else:
            assert takens.available() == 0

    def test_get_assessments_taken_by_date_for_taker_and_assessment_offered(self):
        """Tests get_assessments_taken_by_date_for_taker_and_assessment_offered"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assessments_taken_by_date_for_taker_and_assessment_offered(True, True, True, True)

    def test_get_assessments_taken(self):
        """Tests get_assessments_taken"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        if self.svc_mgr.supports_assessment_taken_query():
            objects = self.catalog.get_assessments_taken()
            assert isinstance(objects, AssessmentTakenList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessments_taken()
            assert isinstance(objects, AssessmentTakenList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_assessments_taken()
                assert isinstance(objects, AssessmentTakenList)
                self.catalog.use_federated_bank_view()
                objects = self.catalog.get_assessments_taken()
                assert objects.available() > 0
                assert isinstance(objects, AssessmentTakenList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_assessments_taken()

    def test_get_assessment_taken_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_assessment_taken(self.assessment_taken_ids[0], ALIAS_ID)
            obj = self.catalog.get_assessment_taken(ALIAS_ID)
            assert obj.get_id() == self.assessment_taken_ids[0]


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_taken_list = list()
    request.cls.assessment_taken_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_taken_query_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenLookupSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenLookupSession tests'
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + color
            create_form.description = (
                'Test AssessmentTaken for AssessmentTakenQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_assessment_taken(create_form)
            request.cls.assessment_taken_list.append(obj)
            request.cls.assessment_taken_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_taken_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                for obj in catalog.get_assessments_taken():
                    catalog.delete_assessment_taken(obj.ident)
                for obj in catalog.get_assessments_offered():
                    catalog.delete_assessment_offered(obj.ident)
                for obj in catalog.get_assessments():
                    catalog.delete_assessment(obj.ident)
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_taken_query_session_class_fixture", "assessment_taken_query_session_test_fixture")
class TestAssessmentTakenQuerySession(object):
    """Tests for AssessmentTakenQuerySession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_search_assessments_taken(self):
        """Tests can_search_assessments_taken"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_assessments_taken(), bool)

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_taken_query()
        assert isinstance(query, ABCQueries.AssessmentTakenQuery)

    def test_get_assessments_taken_by_query(self):
        """Tests get_assessments_taken_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_assessment_taken_query()
            query.match_display_name('orange')
            assert self.catalog.get_assessments_taken_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_assessments_taken_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_taken_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenAdminSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenAdminSession tests'
        obj = request.cls.catalog.create_assessment_offered(create_form)
        request.cls.assessment_offered = obj
        request.cls.form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
        request.cls.form.display_name = 'new AssessmentTaken'
        request.cls.form.description = 'description of AssessmentTaken'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_assessment_taken(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_taken_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessments_taken():
                request.cls.catalog.delete_assessment_taken(obj.ident)
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            for obj in request.cls.catalog.get_items():
                request.cls.catalog.delete_item(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_admin_session_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_taken_admin_session_class_fixture", "assessment_taken_admin_session_test_fixture")
class TestAssessmentTakenAdminSession(object):
    """Tests for AssessmentTakenAdminSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bank_id() == self.catalog.ident

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_create_assessments_taken(self):
        """Tests can_create_assessments_taken"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_assessments_taken(), bool)

    def test_can_create_assessment_taken_with_record_types(self):
        """Tests can_create_assessment_taken_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_assessment_taken_with_record_types(DEFAULT_TYPE), bool)

    def test_get_assessment_taken_form_for_create(self):
        """Tests get_assessment_taken_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_taken_form_for_create(self.assessment_offered.ident, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_taken_form_for_create(self.fake_id, [])

    def test_create_assessment_taken(self):
        """Tests create_assessment_taken"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTaken
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, AssessmentTaken)
            assert self.osid_object.display_name.text == 'new AssessmentTaken'
            assert self.osid_object.description.text == 'description of AssessmentTaken'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_assessment_taken(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment_taken('I Will Break You!')
            update_form = self.catalog.get_assessment_taken_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment_taken(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_assessment_taken('foo')

    def test_can_update_assessments_taken(self):
        """Tests can_update_assessments_taken"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_assessments_taken(), bool)

    def test_get_assessment_taken_form_for_update(self):
        """Tests get_assessment_taken_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_taken_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_taken_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_taken_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='assessment.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_taken_form_for_update(self.fake_id)

    def test_update_assessment_taken(self):
        """Tests update_assessment_taken"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.assessment.objects import AssessmentTaken
            form = self.catalog.get_assessment_taken_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_assessment_taken(form)
            assert isinstance(updated_object, AssessmentTaken)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_assessment_taken(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_assessment_taken('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_assessment_taken(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_assessment_taken('foo')

    def test_can_delete_assessments_taken(self):
        """Tests can_delete_assessments_taken"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_assessments_taken(), bool)

    def test_delete_assessment_taken(self):
        """Tests delete_assessment_taken"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_taken_form_for_create(self.assessment_offered.ident, [])
            form.display_name = 'new Assessment Taken'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_assessment_taken(form)
            self.catalog.delete_assessment_taken(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_assessment_taken(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_assessment_taken(self.fake_id)

    def test_can_manage_assessment_taken_aliases(self):
        """Tests can_manage_assessment_taken_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_assessment_taken_aliases(), bool)

    def test_alias_assessment_taken(self):
        """Tests alias_assessment_taken"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_assessment_taken(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_assessment_taken(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_assessment_taken(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_bank_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_taken_list = list()
    request.cls.assessment_taken_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentTakenBankSession tests'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenBankSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenLBankSession tests'
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenLookupSession tests'
            obj = request.cls.catalog.create_assessment_taken(create_form)
            request.cls.assessment_taken_list.append(obj)
            request.cls.assessment_taken_ids.append(obj.ident)
        request.cls.svc_mgr.assign_assessment_taken_to_bank(
            request.cls.assessment_taken_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_assessment_taken_to_bank(
            request.cls.assessment_taken_ids[2], request.cls.assigned_catalog.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_taken_bank_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_assessment_taken_from_bank(
                request.cls.assessment_taken_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_assessment_taken_from_bank(
                request.cls.assessment_taken_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_assessments_taken():
                request.cls.catalog.delete_assessment_taken(obj.ident)
            for obj in request.cls.catalog.get_assessments_offered():
                request.cls.catalog.delete_assessment_offered(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_bank_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_taken_bank_session_class_fixture", "assessment_taken_bank_session_test_fixture")
class TestAssessmentTakenBankSession(object):
    """Tests for AssessmentTakenBankSession"""
    def test_can_lookup_assessment_taken_bank_mappings(self):
        """Tests can_lookup_assessment_taken_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_taken_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_taken_ids_by_bank(self):
        """Tests get_assessment_taken_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_assessment_taken_ids_by_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_assessment_taken_ids_by_bank(self.fake_id)

    def test_get_assessments_taken_by_bank(self):
        """Tests get_assessments_taken_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_assessments_taken_by_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AssessmentTakenList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_taken_by_bank(self.fake_id)

    def test_get_assessment_taken_ids_by_banks(self):
        """Tests get_assessment_taken_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_assessment_taken_ids_by_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_taken_ids_by_banks([self.fake_id])

    def test_get_assessments_taken_by_banks(self):
        """Tests get_assessments_taken_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_assessments_taken_by_banks(catalog_ids)
            assert isinstance(results, ABCObjects.AssessmentTakenList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessments_taken_by_banks([self.fake_id])

    def test_get_bank_ids_by_assessment_taken(self):
        """Tests get_bank_ids_by_assessment_taken"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bank_ids_by_assessment_taken(self.assessment_taken_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_ids_by_assessment_taken(self.fake_id)

    def test_get_banks_by_assessment_taken(self):
        """Tests get_banks_by_assessment_taken"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_banks_by_assessment_taken(self.assessment_taken_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_assessment_taken(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_bank_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_taken_list = list()
    request.cls.assessment_taken_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentTakenBankAssignmentSession tests'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenBankAssignmentSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_offered_form_for_create(request.cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenBankAssignmentSession tests'
        request.cls.assessment_offered = request.cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_taken_form_for_create(request.cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenBankAssignmentSession tests'
            obj = request.cls.catalog.create_assessment_taken(create_form)
            request.cls.assessment_taken_list.append(obj)
            request.cls.assessment_taken_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_taken_bank_assignment_session(proxy=PROXY)

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
def assessment_taken_bank_assignment_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_taken_bank_assignment_session_class_fixture", "assessment_taken_bank_assignment_session_test_fixture")
class TestAssessmentTakenBankAssignmentSession(object):
    """Tests for AssessmentTakenBankAssignmentSession"""
    def test_can_assign_assessments_taken(self):
        """Tests can_assign_assessments_taken"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessments_taken()
        assert isinstance(result, bool)

    def test_can_assign_assessments_taken_to_bank(self):
        """Tests can_assign_assessments_taken_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessments_taken_to_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids(self.fake_id)

    def test_get_assignable_bank_ids_for_assessment_taken(self):
        """Tests get_assignable_bank_ids_for_assessment_taken"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids_for_assessment_taken(self.catalog.ident, self.assessment_taken_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids_for_assessment_taken(self.fake_id, self.fake_id)

    def test_assign_assessment_taken_to_bank(self):
        """Tests assign_assessment_taken_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessments_taken()
            assert results.available() == 0
            self.session.assign_assessment_taken_to_bank(self.assessment_taken_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments_taken()
            assert results.available() == 1
            self.session.unassign_assessment_taken_from_bank(
                self.assessment_taken_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_assessment_taken_to_bank(self.fake_id, self.fake_id)

    def test_unassign_assessment_taken_from_bank(self):
        """Tests unassign_assessment_taken_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessments_taken()
            assert results.available() == 0
            self.session.assign_assessment_taken_to_bank(
                self.assessment_taken_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments_taken()
            assert results.available() == 1
            self.session.unassign_assessment_taken_from_bank(
                self.assessment_taken_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessments_taken()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_assessment_taken_from_bank(self.fake_id, self.fake_id)

    def test_reassign_assessment_taken_to_billing(self):
        """Tests reassign_assessment_taken_to_billing"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_assessment_taken_to_billing(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for assessment proxy manager tests'
            catalog = request.cls.svc_mgr.create_bank(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bank_lookup_session_class_fixture", "bank_lookup_session_test_fixture")
class TestBankLookupSession(object):
    """Tests for BankLookupSession"""
    def test_can_lookup_banks(self):
        """Tests can_lookup_banks"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_banks(), bool)

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_bank(self):
        """Tests get_bank"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_bank(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank(self.fake_id)

    def test_get_banks_by_ids(self):
        """Tests get_banks_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_banks_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.BankList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_ids([self.fake_id])

    def test_get_banks_by_genus_type(self):
        """Tests get_banks_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_banks_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.BankList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_banks_by_parent_genus_type(self):
        """Tests get_banks_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_banks_by_parent_genus_type(True)

    def test_get_banks_by_record_type(self):
        """Tests get_banks_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_banks_by_record_type(True)

    def test_get_banks_by_provider(self):
        """Tests get_banks_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_banks_by_provider(True)

    def test_get_banks(self):
        """Tests get_banks"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_banks()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.BankList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_query_session_class_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
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
def bank_query_session_test_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bank_query_session_class_fixture", "bank_query_session_test_fixture")
class TestBankQuerySession(object):
    """Tests for BankQuerySession"""
    def test_can_search_banks(self):
        """Tests can_search_banks"""
        # From test_templates/resource.py::BinQuerySession::can_search_bins_template
        assert isinstance(self.session.can_search_banks(), bool)

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_bank_query()
            assert isinstance(query, ABCQueries.BankQuery)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_bank_query()

    def test_get_banks_by_query(self):
        """Tests get_banks_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_bank_query()
            query.match_display_name('Test catalog')
            assert self.session.get_banks_by_query(query).available() == 1
            query.clear_display_name_terms()
            query.match_display_name('Test catalog', match=False)
            assert self.session.get_banks_by_query(query).available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_banks_by_query('foo')


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def bank_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank For Deletion'
        create_form.description = 'Test Bank for BankAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_bank(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bank_admin_session_class_fixture", "bank_admin_session_test_fixture")
class TestBankAdminSession(object):
    """Tests for BankAdminSession"""
    def test_can_create_banks(self):
        """Tests can_create_banks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_banks(), bool)

    def test_can_create_bank_with_record_types(self):
        """Tests can_create_bank_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_bank_with_record_types(DEFAULT_TYPE), bool)

    def test_get_bank_form_for_create(self):
        """Tests get_bank_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.assessment.objects import BankForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bank_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_bank_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_form_for_create([])

    def test_create_bank(self):
        """Tests create_bank"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.assessment.objects import Bank
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bank_form_for_create([])
            catalog_form.display_name = 'Test Bank'
            catalog_form.description = 'Test Bank for BankAdminSession.create_bank tests'
            new_catalog = self.svc_mgr.create_bank(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_bank(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_bank('I Will Break You!')
            update_form = self.svc_mgr.get_bank_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_bank(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_bank('foo')

    def test_can_update_banks(self):
        """Tests can_update_banks"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_banks(), bool)

    def test_get_bank_form_for_update(self):
        """Tests get_bank_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.assessment.objects import BankForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bank_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_form_for_update(self.fake_id)

    def test_update_bank(self):
        """Tests update_bank"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bank_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_bank(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_bank('foo')

    def test_can_delete_banks(self):
        """Tests can_delete_banks"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_banks(), bool)

    def test_delete_bank(self):
        """Tests delete_bank"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_bank(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_bank(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_bank(self.fake_id)

    def test_can_manage_bank_aliases(self):
        """Tests can_manage_bank_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_bank_aliases(), bool)

    def test_alias_bank(self):
        """Tests alias_bank"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('assessment.Bank%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_bank(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_bank(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_bank(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bank ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_bank(create_form)
        request.cls.svc_mgr.add_root_bank(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_banks(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_bank(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_bank(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bank_hierarchy_session_class_fixture", "bank_hierarchy_session_test_fixture")
class TestBankHierarchySession(object):
    """Tests for BankHierarchySession"""
    def test_get_bank_hierarchy_id(self):
        """Tests get_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bank_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_bank_hierarchy(self):
        """Tests get_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_bank_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_hierarchy()

    def test_can_access_bank_hierarchy(self):
        """Tests can_access_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_bank_hierarchy(), bool)

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_root_bank_ids(self):
        """Tests get_root_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_bank_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_bank_ids()

    def test_get_root_banks(self):
        """Tests get_root_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.assessment.objects import BankList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_banks()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_banks()

    def test_has_parent_banks(self):
        """Tests has_parent_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_banks(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_banks(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_banks(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_banks(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_banks(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_banks(self.fake_id)

    def test_is_parent_of_bank(self):
        """Tests is_parent_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_bank(self.fake_id, self.fake_id)

    def test_get_parent_bank_ids(self):
        """Tests get_parent_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_bank_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_bank_ids(self.fake_id)

    def test_get_parent_banks(self):
        """Tests get_parent_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_banks(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_banks(self.fake_id)

    def test_is_ancestor_of_bank(self):
        """Tests is_ancestor_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_bank,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_bank(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_banks(self):
        """Tests has_child_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_banks(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_banks(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_banks(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_banks(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_banks(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_banks(self.fake_id)

    def test_is_child_of_bank(self):
        """Tests is_child_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_bank(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_bank(self.fake_id, self.fake_id)

    def test_get_child_bank_ids(self):
        """Tests get_child_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_bank_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_bank_ids(self.fake_id)

    def test_get_child_banks(self):
        """Tests get_child_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_banks(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_banks(self.fake_id)

    def test_is_descendant_of_bank(self):
        """Tests is_descendant_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_bank,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_bank(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_bank_node_ids(self):
        """Tests get_bank_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bank_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_node_ids(self.fake_id, 1, 2, False)

    def test_get_bank_nodes(self):
        """Tests get_bank_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bank_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bank ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_bank(create_form)
        request.cls.svc_mgr.add_root_bank(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_banks(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_bank(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bank_hierarchy_design_session_class_fixture", "bank_hierarchy_design_session_test_fixture")
class TestBankHierarchyDesignSession(object):
    """Tests for BankHierarchyDesignSession"""
    def test_get_bank_hierarchy_id(self):
        """Tests get_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bank_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_bank_hierarchy(self):
        """Tests get_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_bank_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_hierarchy()

    def test_can_modify_bank_hierarchy(self):
        """Tests can_modify_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_bank_hierarchy(), bool)

    def test_add_root_bank(self):
        """Tests add_root_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_banks()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_bank(self.fake_id)

    def test_remove_root_bank(self):
        """Tests remove_root_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_banks()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Bank root'
            new_bank = self.svc_mgr.create_bank(create_form)
            self.svc_mgr.add_root_bank(new_bank.ident)

            roots = self.session.get_root_banks()
            assert roots.available() == 2

            self.session.remove_root_bank(new_bank.ident)

            roots = self.session.get_root_banks()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_bank(self.fake_id)

    def test_add_child_bank(self):
        """Tests add_child_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_banks(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_bank(self.fake_id, self.fake_id)

    def test_remove_child_bank(self):
        """Tests remove_child_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_banks(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Bank child'
            new_bank = self.svc_mgr.create_bank(create_form)
            self.svc_mgr.add_child_bank(
                self.catalogs['Root'].ident,
                new_bank.ident)

            children = self.session.get_child_banks(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_bank(
                self.catalogs['Root'].ident,
                new_bank.ident)

            children = self.session.get_child_banks(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_bank(self.fake_id, self.fake_id)

    def test_remove_child_banks(self):
        """Tests remove_child_banks"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_banks(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Bank child'
            new_bank = self.svc_mgr.create_bank(create_form)
            self.svc_mgr.add_child_bank(
                self.catalogs['Grandchild 1'].ident,
                new_bank.ident)

            children = self.session.get_child_banks(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_banks(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_banks(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_banks(self.fake_id)
