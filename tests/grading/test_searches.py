"""Unit tests of grading searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("grade_system_search_class_fixture", "grade_system_search_test_fixture")
class TestGradeSystemSearch(object):
    """Tests for GradeSystemSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_grade_systems(self):
        """Tests search_among_grade_systems"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_grade_system_results(self):
        """Tests order_grade_system_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_system_search_record(self):
        """Tests get_grade_system_search_record"""
        pass


@pytest.mark.usefixtures("grade_system_search_results_class_fixture", "grade_system_search_results_test_fixture")
class TestGradeSystemSearchResults(object):
    """Tests for GradeSystemSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_grade_systems(self):
        """Tests get_grade_systems"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_system_query_inspector(self):
        """Tests get_grade_system_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_system_search_results_record(self):
        """Tests get_grade_system_search_results_record"""
        pass


@pytest.mark.usefixtures("grade_entry_search_class_fixture", "grade_entry_search_test_fixture")
class TestGradeEntrySearch(object):
    """Tests for GradeEntrySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_grade_entries(self):
        """Tests search_among_grade_entries"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_grade_entry_results(self):
        """Tests order_grade_entry_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entry_search_record(self):
        """Tests get_grade_entry_search_record"""
        pass


@pytest.mark.usefixtures("grade_entry_search_results_class_fixture", "grade_entry_search_results_test_fixture")
class TestGradeEntrySearchResults(object):
    """Tests for GradeEntrySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entry_query_inspector(self):
        """Tests get_grade_entry_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entry_search_results_record(self):
        """Tests get_grade_entry_search_results_record"""
        pass


@pytest.mark.usefixtures("gradebook_column_search_class_fixture", "gradebook_column_search_test_fixture")
class TestGradebookColumnSearch(object):
    """Tests for GradebookColumnSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_gradebook_columns(self):
        """Tests search_among_gradebook_columns"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_gradebook_column_results(self):
        """Tests order_gradebook_column_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_column_search_record(self):
        """Tests get_gradebook_column_search_record"""
        pass


@pytest.mark.usefixtures("gradebook_column_search_results_class_fixture", "gradebook_column_search_results_test_fixture")
class TestGradebookColumnSearchResults(object):
    """Tests for GradebookColumnSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_columns(self):
        """Tests get_gradebook_columns"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_column_query_inspector(self):
        """Tests get_gradebook_column_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_column_search_results_record(self):
        """Tests get_gradebook_column_search_results_record"""
        pass


@pytest.mark.usefixtures("gradebook_search_class_fixture", "gradebook_search_test_fixture")
class TestGradebookSearch(object):
    """Tests for GradebookSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_gradebooks(self):
        """Tests search_among_gradebooks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_gradebook_results(self):
        """Tests order_gradebook_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_search_record(self):
        """Tests get_gradebook_search_record"""
        pass


@pytest.mark.usefixtures("gradebook_search_results_class_fixture", "gradebook_search_results_test_fixture")
class TestGradebookSearchResults(object):
    """Tests for GradebookSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_gradebooks(self):
        """Tests get_gradebooks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_query_inspector(self):
        """Tests get_gradebook_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_search_results_record(self):
        """Tests get_gradebook_search_results_record"""
        pass
