"""Unit tests of learning records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("objective_record_class_fixture", "objective_record_test_fixture")
class TestObjectiveRecord(object):
    """Tests for ObjectiveRecord"""


@pytest.mark.usefixtures("objective_query_record_class_fixture", "objective_query_record_test_fixture")
class TestObjectiveQueryRecord(object):
    """Tests for ObjectiveQueryRecord"""


@pytest.mark.usefixtures("objective_form_record_class_fixture", "objective_form_record_test_fixture")
class TestObjectiveFormRecord(object):
    """Tests for ObjectiveFormRecord"""


@pytest.mark.usefixtures("objective_search_record_class_fixture", "objective_search_record_test_fixture")
class TestObjectiveSearchRecord(object):
    """Tests for ObjectiveSearchRecord"""


@pytest.mark.usefixtures("activity_record_class_fixture", "activity_record_test_fixture")
class TestActivityRecord(object):
    """Tests for ActivityRecord"""


@pytest.mark.usefixtures("activity_query_record_class_fixture", "activity_query_record_test_fixture")
class TestActivityQueryRecord(object):
    """Tests for ActivityQueryRecord"""


@pytest.mark.usefixtures("activity_form_record_class_fixture", "activity_form_record_test_fixture")
class TestActivityFormRecord(object):
    """Tests for ActivityFormRecord"""


@pytest.mark.usefixtures("activity_search_record_class_fixture", "activity_search_record_test_fixture")
class TestActivitySearchRecord(object):
    """Tests for ActivitySearchRecord"""


@pytest.mark.usefixtures("proficiency_record_class_fixture", "proficiency_record_test_fixture")
class TestProficiencyRecord(object):
    """Tests for ProficiencyRecord"""


@pytest.mark.usefixtures("proficiency_query_record_class_fixture", "proficiency_query_record_test_fixture")
class TestProficiencyQueryRecord(object):
    """Tests for ProficiencyQueryRecord"""


@pytest.mark.usefixtures("proficiency_form_record_class_fixture", "proficiency_form_record_test_fixture")
class TestProficiencyFormRecord(object):
    """Tests for ProficiencyFormRecord"""


@pytest.mark.usefixtures("proficiency_search_record_class_fixture", "proficiency_search_record_test_fixture")
class TestProficiencySearchRecord(object):
    """Tests for ProficiencySearchRecord"""


@pytest.mark.usefixtures("objective_bank_record_class_fixture", "objective_bank_record_test_fixture")
class TestObjectiveBankRecord(object):
    """Tests for ObjectiveBankRecord"""


@pytest.mark.usefixtures("objective_bank_query_record_class_fixture", "objective_bank_query_record_test_fixture")
class TestObjectiveBankQueryRecord(object):
    """Tests for ObjectiveBankQueryRecord"""


@pytest.mark.usefixtures("objective_bank_form_record_class_fixture", "objective_bank_form_record_test_fixture")
class TestObjectiveBankFormRecord(object):
    """Tests for ObjectiveBankFormRecord"""


@pytest.mark.usefixtures("objective_bank_search_record_class_fixture", "objective_bank_search_record_test_fixture")
class TestObjectiveBankSearchRecord(object):
    """Tests for ObjectiveBankSearchRecord"""
