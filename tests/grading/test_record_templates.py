"""Unit tests of grading records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("grade_record_class_fixture", "grade_record_test_fixture")
class TestGradeRecord(object):
    """Tests for GradeRecord"""


@pytest.mark.usefixtures("grade_query_record_class_fixture", "grade_query_record_test_fixture")
class TestGradeQueryRecord(object):
    """Tests for GradeQueryRecord"""


@pytest.mark.usefixtures("grade_form_record_class_fixture", "grade_form_record_test_fixture")
class TestGradeFormRecord(object):
    """Tests for GradeFormRecord"""


@pytest.mark.usefixtures("grade_system_record_class_fixture", "grade_system_record_test_fixture")
class TestGradeSystemRecord(object):
    """Tests for GradeSystemRecord"""


@pytest.mark.usefixtures("grade_system_query_record_class_fixture", "grade_system_query_record_test_fixture")
class TestGradeSystemQueryRecord(object):
    """Tests for GradeSystemQueryRecord"""


@pytest.mark.usefixtures("grade_system_form_record_class_fixture", "grade_system_form_record_test_fixture")
class TestGradeSystemFormRecord(object):
    """Tests for GradeSystemFormRecord"""


@pytest.mark.usefixtures("grade_system_search_record_class_fixture", "grade_system_search_record_test_fixture")
class TestGradeSystemSearchRecord(object):
    """Tests for GradeSystemSearchRecord"""


@pytest.mark.usefixtures("grade_entry_record_class_fixture", "grade_entry_record_test_fixture")
class TestGradeEntryRecord(object):
    """Tests for GradeEntryRecord"""


@pytest.mark.usefixtures("grade_entry_query_record_class_fixture", "grade_entry_query_record_test_fixture")
class TestGradeEntryQueryRecord(object):
    """Tests for GradeEntryQueryRecord"""


@pytest.mark.usefixtures("grade_entry_form_record_class_fixture", "grade_entry_form_record_test_fixture")
class TestGradeEntryFormRecord(object):
    """Tests for GradeEntryFormRecord"""


@pytest.mark.usefixtures("grade_entry_search_record_class_fixture", "grade_entry_search_record_test_fixture")
class TestGradeEntrySearchRecord(object):
    """Tests for GradeEntrySearchRecord"""


@pytest.mark.usefixtures("gradebook_column_record_class_fixture", "gradebook_column_record_test_fixture")
class TestGradebookColumnRecord(object):
    """Tests for GradebookColumnRecord"""


@pytest.mark.usefixtures("gradebook_column_query_record_class_fixture", "gradebook_column_query_record_test_fixture")
class TestGradebookColumnQueryRecord(object):
    """Tests for GradebookColumnQueryRecord"""


@pytest.mark.usefixtures("gradebook_column_form_record_class_fixture", "gradebook_column_form_record_test_fixture")
class TestGradebookColumnFormRecord(object):
    """Tests for GradebookColumnFormRecord"""


@pytest.mark.usefixtures("gradebook_column_search_record_class_fixture", "gradebook_column_search_record_test_fixture")
class TestGradebookColumnSearchRecord(object):
    """Tests for GradebookColumnSearchRecord"""


@pytest.mark.usefixtures("gradebook_column_summary_record_class_fixture", "gradebook_column_summary_record_test_fixture")
class TestGradebookColumnSummaryRecord(object):
    """Tests for GradebookColumnSummaryRecord"""


@pytest.mark.usefixtures("gradebook_column_summary_query_record_class_fixture", "gradebook_column_summary_query_record_test_fixture")
class TestGradebookColumnSummaryQueryRecord(object):
    """Tests for GradebookColumnSummaryQueryRecord"""


@pytest.mark.usefixtures("gradebook_record_class_fixture", "gradebook_record_test_fixture")
class TestGradebookRecord(object):
    """Tests for GradebookRecord"""


@pytest.mark.usefixtures("gradebook_query_record_class_fixture", "gradebook_query_record_test_fixture")
class TestGradebookQueryRecord(object):
    """Tests for GradebookQueryRecord"""


@pytest.mark.usefixtures("gradebook_form_record_class_fixture", "gradebook_form_record_test_fixture")
class TestGradebookFormRecord(object):
    """Tests for GradebookFormRecord"""


@pytest.mark.usefixtures("gradebook_search_record_class_fixture", "gradebook_search_record_test_fixture")
class TestGradebookSearchRecord(object):
    """Tests for GradebookSearchRecord"""
