"""Unit tests of assessment records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("question_record_class_fixture", "question_record_test_fixture")
class TestQuestionRecord(object):
    """Tests for QuestionRecord"""


@pytest.mark.usefixtures("question_query_record_class_fixture", "question_query_record_test_fixture")
class TestQuestionQueryRecord(object):
    """Tests for QuestionQueryRecord"""


@pytest.mark.usefixtures("question_form_record_class_fixture", "question_form_record_test_fixture")
class TestQuestionFormRecord(object):
    """Tests for QuestionFormRecord"""


@pytest.mark.usefixtures("answer_record_class_fixture", "answer_record_test_fixture")
class TestAnswerRecord(object):
    """Tests for AnswerRecord"""


@pytest.mark.usefixtures("answer_query_record_class_fixture", "answer_query_record_test_fixture")
class TestAnswerQueryRecord(object):
    """Tests for AnswerQueryRecord"""


@pytest.mark.usefixtures("answer_form_record_class_fixture", "answer_form_record_test_fixture")
class TestAnswerFormRecord(object):
    """Tests for AnswerFormRecord"""


@pytest.mark.usefixtures("item_record_class_fixture", "item_record_test_fixture")
class TestItemRecord(object):
    """Tests for ItemRecord"""


@pytest.mark.usefixtures("item_query_record_class_fixture", "item_query_record_test_fixture")
class TestItemQueryRecord(object):
    """Tests for ItemQueryRecord"""


@pytest.mark.usefixtures("item_form_record_class_fixture", "item_form_record_test_fixture")
class TestItemFormRecord(object):
    """Tests for ItemFormRecord"""


@pytest.mark.usefixtures("item_search_record_class_fixture", "item_search_record_test_fixture")
class TestItemSearchRecord(object):
    """Tests for ItemSearchRecord"""


@pytest.mark.usefixtures("assessment_record_class_fixture", "assessment_record_test_fixture")
class TestAssessmentRecord(object):
    """Tests for AssessmentRecord"""


@pytest.mark.usefixtures("assessment_query_record_class_fixture", "assessment_query_record_test_fixture")
class TestAssessmentQueryRecord(object):
    """Tests for AssessmentQueryRecord"""


@pytest.mark.usefixtures("assessment_form_record_class_fixture", "assessment_form_record_test_fixture")
class TestAssessmentFormRecord(object):
    """Tests for AssessmentFormRecord"""


@pytest.mark.usefixtures("assessment_search_record_class_fixture", "assessment_search_record_test_fixture")
class TestAssessmentSearchRecord(object):
    """Tests for AssessmentSearchRecord"""


@pytest.mark.usefixtures("assessment_offered_record_class_fixture", "assessment_offered_record_test_fixture")
class TestAssessmentOfferedRecord(object):
    """Tests for AssessmentOfferedRecord"""


@pytest.mark.usefixtures("assessment_offered_query_record_class_fixture", "assessment_offered_query_record_test_fixture")
class TestAssessmentOfferedQueryRecord(object):
    """Tests for AssessmentOfferedQueryRecord"""


@pytest.mark.usefixtures("assessment_offered_form_record_class_fixture", "assessment_offered_form_record_test_fixture")
class TestAssessmentOfferedFormRecord(object):
    """Tests for AssessmentOfferedFormRecord"""


@pytest.mark.usefixtures("assessment_offered_search_record_class_fixture", "assessment_offered_search_record_test_fixture")
class TestAssessmentOfferedSearchRecord(object):
    """Tests for AssessmentOfferedSearchRecord"""


@pytest.mark.usefixtures("assessment_taken_record_class_fixture", "assessment_taken_record_test_fixture")
class TestAssessmentTakenRecord(object):
    """Tests for AssessmentTakenRecord"""


@pytest.mark.usefixtures("assessment_taken_query_record_class_fixture", "assessment_taken_query_record_test_fixture")
class TestAssessmentTakenQueryRecord(object):
    """Tests for AssessmentTakenQueryRecord"""


@pytest.mark.usefixtures("assessment_taken_form_record_class_fixture", "assessment_taken_form_record_test_fixture")
class TestAssessmentTakenFormRecord(object):
    """Tests for AssessmentTakenFormRecord"""


@pytest.mark.usefixtures("assessment_taken_search_record_class_fixture", "assessment_taken_search_record_test_fixture")
class TestAssessmentTakenSearchRecord(object):
    """Tests for AssessmentTakenSearchRecord"""


@pytest.mark.usefixtures("assessment_section_record_class_fixture", "assessment_section_record_test_fixture")
class TestAssessmentSectionRecord(object):
    """Tests for AssessmentSectionRecord"""


@pytest.mark.usefixtures("bank_record_class_fixture", "bank_record_test_fixture")
class TestBankRecord(object):
    """Tests for BankRecord"""


@pytest.mark.usefixtures("bank_query_record_class_fixture", "bank_query_record_test_fixture")
class TestBankQueryRecord(object):
    """Tests for BankQueryRecord"""


@pytest.mark.usefixtures("bank_form_record_class_fixture", "bank_form_record_test_fixture")
class TestBankFormRecord(object):
    """Tests for BankFormRecord"""


@pytest.mark.usefixtures("bank_search_record_class_fixture", "bank_search_record_test_fixture")
class TestBankSearchRecord(object):
    """Tests for BankSearchRecord"""


@pytest.mark.usefixtures("response_record_class_fixture", "response_record_test_fixture")
class TestResponseRecord(object):
    """Tests for ResponseRecord"""
