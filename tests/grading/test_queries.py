"""Unit tests of grading queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.json_.grading.queries import GradeQuery
from dlkit.json_.grading.queries import GradebookColumnSummaryQuery
from dlkit.json_.grading.queries import GradebookQuery
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
def grade_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_query_test_fixture(request):
    # Since the session isn't implemented, we just construct an ActivityQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = GradeQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("grade_query_class_fixture", "grade_query_test_fixture")
class TestGradeQuery(object):
    """Tests for GradeQuery"""
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

    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradeSystem'] = 'foo'
        self.query.clear_grade_system_terms()
        if is_no_authz(self.service_config):
            assert 'gradeSystem' not in self.query._query_terms

    def test_match_input_score_start_range(self):
        """Tests match_input_score_start_range"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_input_score_start_range(True, True, True)

    def test_clear_input_score_start_range_terms(self):
        """Tests clear_input_score_start_range_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['inputScoreStartRange'] = 'foo'
        self.query.clear_input_score_start_range_terms()
        if is_no_authz(self.service_config):
            assert 'inputScoreStartRange' not in self.query._query_terms

    def test_match_input_score_end_range(self):
        """Tests match_input_score_end_range"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_input_score_end_range(True, True, True)

    def test_clear_input_score_end_range_terms(self):
        """Tests clear_input_score_end_range_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['inputScoreEndRange'] = 'foo'
        self.query.clear_input_score_end_range_terms()
        if is_no_authz(self.service_config):
            assert 'inputScoreEndRange' not in self.query._query_terms

    def test_match_input_score(self):
        """Tests match_input_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_input_score(True, True, True)

    def test_clear_input_score_terms(self):
        """Tests clear_input_score_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_input_score_terms()

    def test_match_output_score(self):
        """Tests match_output_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_output_score(True, True, True)

    def test_clear_output_score_terms(self):
        """Tests clear_output_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['outputScore'] = 'foo'
        self.query.clear_output_score_terms()
        if is_no_authz(self.service_config):
            assert 'outputScore' not in self.query._query_terms

    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradeEntryId' not in self.query._query_terms
        self.query.match_grade_entry_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradeEntryId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_entry_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradeEntryId' in self.query._query_terms
        self.query.clear_grade_entry_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradeEntryId' not in self.query._query_terms

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grade_entry_query()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_entry_query()

    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grade_entry(True)

    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_grade_entry_terms()

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedGradebookIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' in self.query._query_terms
        self.query.clear_gradebook_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' not in self.query._query_terms

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        if is_no_authz(self.service_config):
            assert 'gradebook' not in self.query._query_terms

    def test_get_grade_query_record(self):
        """Tests get_grade_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_grade_system_query()


@pytest.mark.usefixtures("grade_system_query_class_fixture", "grade_system_query_test_fixture")
class TestGradeSystemQuery(object):
    """Tests for GradeSystemQuery"""
    def test_match_based_on_grades(self):
        """Tests match_based_on_grades"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_based_on_grades(True)

    def test_clear_based_on_grades_terms(self):
        """Tests clear_based_on_grades_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['basedOnGrades'] = 'foo'
        self.query.clear_based_on_grades_terms()
        if is_no_authz(self.service_config):
            assert 'basedOnGrades' not in self.query._query_terms

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

    def test_match_lowest_numeric_score(self):
        """Tests match_lowest_numeric_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_lowest_numeric_score(True, True, True)

    def test_clear_lowest_numeric_score_terms(self):
        """Tests clear_lowest_numeric_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['lowestNumericScore'] = 'foo'
        self.query.clear_lowest_numeric_score_terms()
        if is_no_authz(self.service_config):
            assert 'lowestNumericScore' not in self.query._query_terms

    def test_match_numeric_score_increment(self):
        """Tests match_numeric_score_increment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_numeric_score_increment(True, True, True)

    def test_clear_numeric_score_increment_terms(self):
        """Tests clear_numeric_score_increment_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['numericScoreIncrement'] = 'foo'
        self.query.clear_numeric_score_increment_terms()
        if is_no_authz(self.service_config):
            assert 'numericScoreIncrement' not in self.query._query_terms

    def test_match_highest_numeric_score(self):
        """Tests match_highest_numeric_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_highest_numeric_score(True, True, True)

    def test_clear_highest_numeric_score_terms(self):
        """Tests clear_highest_numeric_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['highestNumericScore'] = 'foo'
        self.query.clear_highest_numeric_score_terms()
        if is_no_authz(self.service_config):
            assert 'highestNumericScore' not in self.query._query_terms

    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' not in self.query._query_terms
        self.query.match_gradebook_column_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradebookColumnId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_column_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' in self.query._query_terms
        self.query.clear_gradebook_column_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' not in self.query._query_terms

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_query()

    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_gradebook_column(True)

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_gradebook_column_terms()

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedGradebookIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' in self.query._query_terms
        self.query.clear_gradebook_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' not in self.query._query_terms

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        if is_no_authz(self.service_config):
            assert 'gradebook' not in self.query._query_terms

    def test_get_grade_system_query_record(self):
        """Tests get_grade_system_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_system_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_entry_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_grade_entry_query()


@pytest.mark.usefixtures("grade_entry_query_class_fixture", "grade_entry_query_test_fixture")
class TestGradeEntryQuery(object):
    """Tests for GradeEntryQuery"""
    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' not in self.query._query_terms
        self.query.match_gradebook_column_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradebookColumnId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_column_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' in self.query._query_terms
        self.query.clear_gradebook_column_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' not in self.query._query_terms

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_query()

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebookColumn'] = 'foo'
        self.query.clear_gradebook_column_terms()
        if is_no_authz(self.service_config):
            assert 'gradebookColumn' not in self.query._query_terms

    def test_match_key_resource_id(self):
        """Tests match_key_resource_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'keyResourceId' not in self.query._query_terms
        self.query.match_key_resource_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['keyResourceId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_key_resource_id_terms(self):
        """Tests clear_key_resource_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_key_resource_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'keyResourceId' in self.query._query_terms
        self.query.clear_key_resource_id_terms()
        if is_no_authz(self.service_config):
            assert 'keyResourceId' not in self.query._query_terms

    def test_supports_key_resource_query(self):
        """Tests supports_key_resource_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_key_resource_query()

    def test_get_key_resource_query(self):
        """Tests get_key_resource_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_key_resource_query()

    def test_match_any_key_resource(self):
        """Tests match_any_key_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_key_resource(True)

    def test_clear_key_resource_terms(self):
        """Tests clear_key_resource_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_key_resource_terms()

    def test_match_derived(self):
        """Tests match_derived"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_derived(True)

    def test_clear_derived_terms(self):
        """Tests clear_derived_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_derived_terms()

    def test_match_overridden_grade_entry_id(self):
        """Tests match_overridden_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'overriddenGradeEntryId' not in self.query._query_terms
        self.query.match_overridden_grade_entry_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['overriddenGradeEntryId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_overridden_grade_entry_id_terms(self):
        """Tests clear_overridden_grade_entry_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_overridden_grade_entry_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'overriddenGradeEntryId' in self.query._query_terms
        self.query.clear_overridden_grade_entry_id_terms()
        if is_no_authz(self.service_config):
            assert 'overriddenGradeEntryId' not in self.query._query_terms

    def test_supports_overridden_grade_entry_query(self):
        """Tests supports_overridden_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_overridden_grade_entry_query()

    def test_get_overridden_grade_entry_query(self):
        """Tests get_overridden_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_overridden_grade_entry_query()

    def test_match_any_overridden_grade_entry(self):
        """Tests match_any_overridden_grade_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_overridden_grade_entry(True)

    def test_clear_overridden_grade_entry_terms(self):
        """Tests clear_overridden_grade_entry_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_overridden_grade_entry_terms()

    def test_match_ignored_for_calculations(self):
        """Tests match_ignored_for_calculations"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ignored_for_calculations(True)

    def test_clear_ignored_for_calculations_terms(self):
        """Tests clear_ignored_for_calculations_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ignoredForCalculations'] = 'foo'
        self.query.clear_ignored_for_calculations_terms()
        if is_no_authz(self.service_config):
            assert 'ignoredForCalculations' not in self.query._query_terms

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
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['grade'] = 'foo'
        self.query.clear_grade_terms()
        if is_no_authz(self.service_config):
            assert 'grade' not in self.query._query_terms

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
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['score'] = 'foo'
        self.query.clear_score_terms()
        if is_no_authz(self.service_config):
            assert 'score' not in self.query._query_terms

    def test_match_time_graded(self):
        """Tests match_time_graded"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_time_graded(True, True, True)

    def test_clear_time_graded_terms(self):
        """Tests clear_time_graded_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_time_graded_terms()

    def test_match_grader_id(self):
        """Tests match_grader_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'graderId' not in self.query._query_terms
        self.query.match_grader_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['graderId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_grader_id_terms(self):
        """Tests clear_grader_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grader_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'graderId' in self.query._query_terms
        self.query.clear_grader_id_terms()
        if is_no_authz(self.service_config):
            assert 'graderId' not in self.query._query_terms

    def test_supports_grader_query(self):
        """Tests supports_grader_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grader_query()

    def test_get_grader_query(self):
        """Tests get_grader_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grader_query()

    def test_match_any_grader(self):
        """Tests match_any_grader"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grader(True)

    def test_clear_grader_terms(self):
        """Tests clear_grader_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_grader_terms()

    def test_match_grading_agent_id(self):
        """Tests match_grading_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradingAgentId' not in self.query._query_terms
        self.query.match_grading_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradingAgentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_grading_agent_id_terms(self):
        """Tests clear_grading_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grading_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradingAgentId' in self.query._query_terms
        self.query.clear_grading_agent_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradingAgentId' not in self.query._query_terms

    def test_supports_grading_agent_query(self):
        """Tests supports_grading_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grading_agent_query()

    def test_get_grading_agent_query(self):
        """Tests get_grading_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grading_agent_query()

    def test_match_any_grading_agent(self):
        """Tests match_any_grading_agent"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grading_agent(True)

    def test_clear_grading_agent_terms(self):
        """Tests clear_grading_agent_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_grading_agent_terms()

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedGradebookIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' in self.query._query_terms
        self.query.clear_gradebook_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' not in self.query._query_terms

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        if is_no_authz(self.service_config):
            assert 'gradebook' not in self.query._query_terms

    def test_get_grade_entry_query_record(self):
        """Tests get_grade_entry_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_entry_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_gradebook_column_query()


@pytest.mark.usefixtures("gradebook_column_query_class_fixture", "gradebook_column_query_test_fixture")
class TestGradebookColumnQuery(object):
    """Tests for GradebookColumnQuery"""
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

    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'gradeEntryId' not in self.query._query_terms
        self.query.match_grade_entry_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['gradeEntryId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_entry_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'gradeEntryId' in self.query._query_terms
        self.query.clear_grade_entry_id_terms()
        if is_no_authz(self.service_config):
            assert 'gradeEntryId' not in self.query._query_terms

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grade_entry_query()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_entry_query()

    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grade_entry(True)

    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_grade_entry_terms()

    def test_supports_gradebook_column_summary_query(self):
        """Tests supports_gradebook_column_summary_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_column_summary_query()

    def test_get_gradebook_column_summary_query(self):
        """Tests get_gradebook_column_summary_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_summary_query()

    def test_clear_gradebook_column_summary_terms(self):
        """Tests clear_gradebook_column_summary_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_gradebook_column_summary_terms()

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedGradebookIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' in self.query._query_terms
        self.query.clear_gradebook_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedGradebookIds' not in self.query._query_terms

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        if is_no_authz(self.service_config):
            assert 'gradebook' not in self.query._query_terms

    def test_get_gradebook_column_query_record(self):
        """Tests get_gradebook_column_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_summary_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.grade_entry_list = list()
    request.cls.grade_entry_ids = list()
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_summary_query_test_fixture(request):
    # Since the session isn't implemented, we just construct a GradebookColumnSummaryQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = GradebookColumnSummaryQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("gradebook_column_summary_query_class_fixture", "gradebook_column_summary_query_test_fixture")
class TestGradebookColumnSummaryQuery(object):
    """Tests for GradebookColumnSummaryQuery"""
    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_gradebook_column_id(True, True)

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_gradebook_column_id_terms()

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_query()

    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_gradebook_column(True)

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_gradebook_column_terms()

    def test_match_mean(self):
        """Tests match_mean"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_mean(True, True, True)

    def test_clear_mean_terms(self):
        """Tests clear_mean_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_mean_terms()

    def test_match_minimum_mean(self):
        """Tests match_minimum_mean"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_mean(True, True)

    def test_clear_minimum_mean_terms(self):
        """Tests clear_minimum_mean_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_mean_terms()

    def test_match_median(self):
        """Tests match_median"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_median(True, True, True)

    def test_clear_median_terms(self):
        """Tests clear_median_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_median_terms()

    def test_match_minimum_median(self):
        """Tests match_minimum_median"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_median(True, True)

    def test_clear_minimum_median_terms(self):
        """Tests clear_minimum_median_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_median_terms()

    def test_match_mode(self):
        """Tests match_mode"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_mode(True, True, True)

    def test_clear_mode_terms(self):
        """Tests clear_mode_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_mode_terms()

    def test_match_minimum_mode(self):
        """Tests match_minimum_mode"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_mode(True, True)

    def test_clear_minimum_mode_terms(self):
        """Tests clear_minimum_mode_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_mode_terms()

    def test_match_rms(self):
        """Tests match_rms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_rms(True, True, True)

    def test_clear_rms_terms(self):
        """Tests clear_rms_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_rms_terms()

    def test_match_minimum_rms(self):
        """Tests match_minimum_rms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_rms(True, True)

    def test_clear_minimum_rms_terms(self):
        """Tests clear_minimum_rms_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_rms_terms()

    def test_match_standard_deviation(self):
        """Tests match_standard_deviation"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_standard_deviation(True, True, True)

    def test_clear_standard_deviation_terms(self):
        """Tests clear_standard_deviation_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_standard_deviation_terms()

    def test_match_minimum_standard_deviation(self):
        """Tests match_minimum_standard_deviation"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_standard_deviation(True, True)

    def test_clear_minimum_standard_deviation_terms(self):
        """Tests clear_minimum_standard_deviation_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_standard_deviation_terms()

    def test_match_sum(self):
        """Tests match_sum"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_sum(True, True, True)

    def test_clear_sum_terms(self):
        """Tests clear_sum_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_sum_terms()

    def test_match_minimum_sum(self):
        """Tests match_minimum_sum"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_sum(True, True)

    def test_clear_minimum_sum_terms(self):
        """Tests clear_minimum_sum_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_sum_terms()

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_gradebook_id(True, True)

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_gradebook_id_terms()

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_gradebook_terms()

    def test_get_gradebook_column_summary_query_record(self):
        """Tests get_gradebook_column_summary_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_summary_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_query_test_fixture(request):
    # Since the session isn't implemented, we just construct a GradebookQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = GradebookQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("gradebook_query_class_fixture", "gradebook_query_test_fixture")
class TestGradebookQuery(object):
    """Tests for GradebookQuery"""
    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_grade_system_id(True, True)

    def test_clear_grade_system_id_terms(self):
        """Tests clear_grade_system_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradeSystemId'] = 'foo'

        if not is_never_authz(self.service_config):
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
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradeSystem'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_grade_system_terms()

        if is_no_authz(self.service_config):
            assert 'gradeSystem' not in self.query._query_terms

    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_grade_entry_id(True, True)

    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradeEntryId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_grade_entry_id_terms()

        if is_no_authz(self.service_config):
            assert 'gradeEntryId' not in self.query._query_terms

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_grade_entry_query()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_grade_entry_query()

    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_grade_entry(True)

    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradeEntry'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_grade_entry_terms()

        if is_no_authz(self.service_config):
            assert 'gradeEntry' not in self.query._query_terms

    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_gradebook_column_id(True, True)

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebookColumnId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_gradebook_column_id_terms()

        if is_no_authz(self.service_config):
            assert 'gradebookColumnId' not in self.query._query_terms

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_column_query()

    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_gradebook_column(True)

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['gradebookColumn'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_gradebook_column_terms()

        if is_no_authz(self.service_config):
            assert 'gradebookColumn' not in self.query._query_terms

    def test_match_ancestor_gradebook_id(self):
        """Tests match_ancestor_gradebook_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_gradebook_id(True, True)

    def test_clear_ancestor_gradebook_id_terms(self):
        """Tests clear_ancestor_gradebook_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorGradebookId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_gradebook_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorGradebookId' not in self.query._query_terms

    def test_supports_ancestor_gradebook_query(self):
        """Tests supports_ancestor_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_gradebook_query()

    def test_get_ancestor_gradebook_query(self):
        """Tests get_ancestor_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_gradebook_query()

    def test_match_any_ancestor_gradebook(self):
        """Tests match_any_ancestor_gradebook"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_gradebook(True)

    def test_clear_ancestor_gradebook_terms(self):
        """Tests clear_ancestor_gradebook_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorGradebook'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_gradebook_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorGradebook' not in self.query._query_terms

    def test_match_descendant_gradebook_id(self):
        """Tests match_descendant_gradebook_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_gradebook_id(True, True)

    def test_clear_descendant_gradebook_id_terms(self):
        """Tests clear_descendant_gradebook_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantGradebookId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_gradebook_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantGradebookId' not in self.query._query_terms

    def test_supports_descendant_gradebook_query(self):
        """Tests supports_descendant_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_gradebook_query()

    def test_get_descendant_gradebook_query(self):
        """Tests get_descendant_gradebook_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_gradebook_query()

    def test_match_any_descendant_gradebook(self):
        """Tests match_any_descendant_gradebook"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_gradebook(True)

    def test_clear_descendant_gradebook_terms(self):
        """Tests clear_descendant_gradebook_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantGradebook'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_gradebook_terms()

        if is_no_authz(self.service_config):
            assert 'descendantGradebook' not in self.query._query_terms

    def test_get_gradebook_query_record(self):
        """Tests get_gradebook_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_gradebook_query_record(True)
