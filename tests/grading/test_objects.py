"""Unit tests of grading objects."""


import pytest


from decimal import Decimal


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.authentication.objects import Agent
from dlkit.abstract_osid.grading import objects as ABCObjects
from dlkit.abstract_osid.grading.objects import GradeList
from dlkit.abstract_osid.grading.objects import GradeSystem
from dlkit.abstract_osid.grading.objects import GradebookColumn
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.assessment.objects import AssessmentOffered
from dlkit.json_.grading.objects import GradeList
from dlkit.json_.grading.objects import GradebookColumn
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime
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
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
SEQUENCE_ASSESSMENT = Type(**registry.ASSESSMENT_RECORD_TYPES["simple-child-sequencing"])


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_grade_form_for_create(
            request.cls.grade_system.ident,
            [])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_grade(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for grade in request.cls.grade_system.get_grades():
                request.cls.catalog.delete_grade(grade.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_class_fixture", "grade_test_fixture")
class TestGrade(object):
    """Tests for Grade"""
    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        if not is_never_authz(self.service_config):
            grade_system_id = self.object.get_grade_system_id()
            assert isinstance(grade_system_id, Id)
            assert str(grade_system_id) == str(self.grade_system.ident)

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        if not is_never_authz(self.service_config):
            grade_system = self.object.get_grade_system()
            assert isinstance(grade_system, ABCObjects.GradeSystem)
            assert str(grade_system.ident) == str(self.grade_system.ident)

    def test_get_input_score_start_range(self):
        """Tests get_input_score_start_range"""
        if not is_never_authz(self.service_config):
            start_range = self.object.get_input_score_end_range()
            assert start_range is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_form_for_create(
                self.grade_system.ident,
                [])
            form.set_input_score_start_range(50.0)
            new_grade = self.catalog.create_grade(form)

            assert new_grade.get_input_score_start_range() == 50.0

    def test_get_input_score_end_range(self):
        """Tests get_input_score_end_range"""
        if not is_never_authz(self.service_config):
            end_range = self.object.get_input_score_end_range()
            assert end_range is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_form_for_create(
                self.grade_system.ident,
                [])
            form.set_input_score_end_range(50.0)
            new_grade = self.catalog.create_grade(form)

            assert new_grade.get_input_score_end_range() == 50.0

    def test_get_output_score(self):
        """Tests get_output_score"""
        if not is_never_authz(self.service_config):
            score = self.object.get_output_score()
            assert score is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_form_for_create(
                self.grade_system.ident,
                [])
            form.set_output_score(50.0)
            new_grade = self.catalog.create_grade(form)

            assert new_grade.get_output_score() == 50.0

    def test_get_grade_record(self):
        """Tests get_grade_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_grade_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_form_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_grade_form_for_create(
            request.cls.grade_system.ident,
            [])

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for grade in request.cls.grade_system.get_grades():
                request.cls.catalog.delete_grade(grade.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_form_class_fixture", "grade_form_test_fixture")
class TestGradeForm(object):
    """Tests for GradeForm"""
    def test_get_input_score_start_range_metadata(self):
        """Tests get_input_score_start_range_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_input_score_start_range_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_input_score_start_range(self):
        """Tests set_input_score_start_range"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['inputScoreStartRange'] is None
            self.form.set_input_score_start_range(50.0)
            assert self.form._my_map['inputScoreStartRange'] == 50.0

    def test_clear_input_score_start_range(self):
        """Tests clear_input_score_start_range"""
        if not is_never_authz(self.service_config):
            self.form.set_input_score_start_range(50.0)
            assert self.form._my_map['inputScoreStartRange'] is not None
            self.form.clear_input_score_start_range()
            assert self.form._my_map['inputScoreStartRange'] is None

    def test_get_input_score_end_range_metadata(self):
        """Tests get_input_score_end_range_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_input_score_end_range_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_input_score_end_range(self):
        """Tests set_input_score_end_range"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['inputScoreEndRange'] is None
            self.form.set_input_score_end_range(50.0)
            assert self.form._my_map['inputScoreEndRange'] == 50.0

    def test_clear_input_score_end_range(self):
        """Tests clear_input_score_end_range"""
        if not is_never_authz(self.service_config):
            self.form.set_input_score_end_range(50.0)
            assert self.form._my_map['inputScoreEndRange'] is not None
            self.form.clear_input_score_end_range()
            assert self.form._my_map['inputScoreEndRange'] is None

    def test_get_output_score_metadata(self):
        """Tests get_output_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_output_score_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_output_score(self):
        """Tests set_output_score"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['outputScore'] is None
            self.form.set_output_score(50.0)
            assert self.form._my_map['outputScore'] == 50.0

    def test_clear_output_score(self):
        """Tests clear_output_score"""
        if not is_never_authz(self.service_config):
            self.form.set_output_score(50.0)
            assert self.form._my_map['outputScore'] is not None
            self.form.clear_output_score()
            assert self.form._my_map['outputScore'] is None

    def test_get_grade_form_record(self):
        """Tests get_grade_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_grade_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_list_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_list_test_fixture(request):
    request.cls.grade_list = []
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_grade_form_for_create(
                request.cls.grade_system.ident,
                [])
            new_grade = request.cls.catalog.create_grade(form)
            request.cls.grade_list.append(new_grade)
        request.cls.grade_list = GradeList(request.cls.grade_list,
                                           runtime=request.cls.catalog._runtime,
                                           proxy=request.cls.catalog._proxy)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for grade in request.cls.grade_system.get_grades():
                request.cls.catalog.delete_grade(grade.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_list_class_fixture", "grade_list_test_fixture")
class TestGradeList(object):
    """Tests for GradeList"""
    def test_get_next_grade(self):
        """Tests get_next_grade"""
        from dlkit.abstract_osid.grading.objects import Grade
        if not is_never_authz(self.service_config):
            assert isinstance(self.grade_list.get_next_grade(), Grade)

    def test_get_next_grades(self):
        """Tests get_next_grades"""
        from dlkit.abstract_osid.grading.objects import Grade, GradeList
        if not is_never_authz(self.service_config):
            new_list = self.grade_list.get_next_grades(2)
            assert isinstance(new_list, GradeList)
            for item in new_list:
                assert isinstance(item, Grade)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_grade_system(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_test_fixture(request):
    pass


@pytest.mark.usefixtures("grade_system_class_fixture", "grade_system_test_fixture")
class TestGradeSystem(object):
    """Tests for GradeSystem"""
    def test_is_based_on_grades(self):
        """Tests is_based_on_grades"""
        if not is_never_authz(self.service_config):
            # when not set on create, returns None
            assert self.object.is_based_on_grades() is None

            form = self.catalog.get_grade_system_form_for_create([])
            form.set_based_on_grades(True)
            new_grade_system = self.catalog.create_grade_system(form)

            assert new_grade_system.is_based_on_grades()

    def test_get_grade_ids(self):
        """Tests get_grade_ids"""
        if not is_never_authz(self.service_config):
            grade_ids = self.object.get_grade_ids()
            assert isinstance(grade_ids, IdList)
            assert grade_ids.available() == 0

    def test_get_grades(self):
        """Tests get_grades"""
        if not is_never_authz(self.service_config):
            grades = self.object.get_grades()
            assert isinstance(grades, GradeList)
            assert grades.available() == 0

    def test_get_lowest_numeric_score(self):
        """Tests get_lowest_numeric_score"""
        if not is_never_authz(self.service_config):
            score = self.object.get_lowest_numeric_score()
            assert score is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_system_form_for_create([])
            form.set_lowest_numeric_score(0.0)
            new_grade_system = self.catalog.create_grade_system(form)

            assert new_grade_system.get_lowest_numeric_score() == 0.0

    def test_get_numeric_score_increment(self):
        """Tests get_numeric_score_increment"""
        if not is_never_authz(self.service_config):
            score = self.object.get_numeric_score_increment()
            assert score is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_system_form_for_create([])
            form.set_numeric_score_increment(1.0)
            new_grade_system = self.catalog.create_grade_system(form)

            assert new_grade_system.get_numeric_score_increment() == 1.0

    def test_get_highest_numeric_score(self):
        """Tests get_highest_numeric_score"""
        if not is_never_authz(self.service_config):
            score = self.object.get_highest_numeric_score()
            assert score is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_system_form_for_create([])
            form.set_highest_numeric_score(100.0)
            new_grade_system = self.catalog.create_grade_system(form)

            assert new_grade_system.get_highest_numeric_score() == 100.0

    def test_get_grade_system_record(self):
        """Tests get_grade_system_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_grade_system_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
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


@pytest.fixture(scope="function")
def grade_system_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_grade_system_form_for_create([])


@pytest.mark.usefixtures("grade_system_form_class_fixture", "grade_system_form_test_fixture")
class TestGradeSystemForm(object):
    """Tests for GradeSystemForm"""
    def test_get_based_on_grades_metadata(self):
        """Tests get_based_on_grades_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_based_on_grades_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_based_on_grades(self):
        """Tests set_based_on_grades"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['basedOnGrades'] is None
            self.form.set_based_on_grades(True)
            assert self.form._my_map['basedOnGrades'] is not None

    def test_clear_based_on_grades(self):
        """Tests clear_based_on_grades"""
        if not is_never_authz(self.service_config):
            self.form.set_based_on_grades(True)
            assert self.form._my_map['basedOnGrades'] is not None
            self.form.clear_based_on_grades()
            assert self.form._my_map['basedOnGrades'] is None

    def test_get_lowest_numeric_score_metadata(self):
        """Tests get_lowest_numeric_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_lowest_numeric_score_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_lowest_numeric_score(self):
        """Tests set_lowest_numeric_score"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['lowestNumericScore'] is None
            self.form.set_lowest_numeric_score(100.0)
            assert self.form._my_map['lowestNumericScore'] is not None

    def test_clear_lowest_numeric_score(self):
        """Tests clear_lowest_numeric_score"""
        if not is_never_authz(self.service_config):
            self.form.set_lowest_numeric_score(100.0)
            assert self.form._my_map['lowestNumericScore'] is not None
            self.form.clear_lowest_numeric_score()
            assert self.form._my_map['lowestNumericScore'] is None

    def test_get_numeric_score_increment_metadata(self):
        """Tests get_numeric_score_increment_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_numeric_score_increment_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_numeric_score_increment(self):
        """Tests set_numeric_score_increment"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['numericScoreIncrement'] is None
            self.form.set_numeric_score_increment(100.0)
            assert self.form._my_map['numericScoreIncrement'] is not None

    def test_clear_numeric_score_increment(self):
        """Tests clear_numeric_score_increment"""
        if not is_never_authz(self.service_config):
            self.form.set_numeric_score_increment(100.0)
            assert self.form._my_map['numericScoreIncrement'] is not None
            self.form.clear_numeric_score_increment()
            assert self.form._my_map['numericScoreIncrement'] is None

    def test_get_highest_numeric_score_metadata(self):
        """Tests get_highest_numeric_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_highest_numeric_score_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_highest_numeric_score(self):
        """Tests set_highest_numeric_score"""
        if not is_never_authz(self.service_config):
            assert self.form._my_map['highestNumericScore'] is None
            self.form.set_highest_numeric_score(100.0)
            assert self.form._my_map['highestNumericScore'] is not None

    def test_clear_highest_numeric_score(self):
        """Tests clear_highest_numeric_score"""
        if not is_never_authz(self.service_config):
            self.form.set_highest_numeric_score(100.0)
            assert self.form._my_map['highestNumericScore'] is not None
            self.form.clear_highest_numeric_score()
            assert self.form._my_map['highestNumericScore'] is None

    def test_get_grade_system_form_record(self):
        """Tests get_grade_system_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_grade_system_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemList tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.grading.objects import GradeSystemList
    request.cls.grade_system_list = list()
    request.cls.grade_system_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + str(num)
            create_form.description = 'Test GradeSystem for GradeSystemList tests'
            obj = request.cls.catalog.create_grade_system(create_form)
            request.cls.grade_system_list.append(obj)
            request.cls.grade_system_ids.append(obj.ident)
    request.cls.grade_system_list = GradeSystemList(request.cls.grade_system_list)
    request.cls.object = request.cls.grade_system_list


@pytest.mark.usefixtures("grade_system_list_class_fixture", "grade_system_list_test_fixture")
class TestGradeSystemList(object):
    """Tests for GradeSystemList"""
    def test_get_next_grade_system(self):
        """Tests get_next_grade_system"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradeSystem
        if not is_never_authz(self.service_config):
            assert isinstance(self.grade_system_list.get_next_grade_system(), GradeSystem)

    def test_get_next_grade_systems(self):
        """Tests get_next_grade_systems"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList, GradeSystem
        if not is_never_authz(self.service_config):
            new_list = self.grade_system_list.get_next_grade_systems(2)
            assert isinstance(new_list, GradeSystemList)
            for item in new_list:
                assert isinstance(item, GradeSystem)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

        form = request.cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(request.cls.grade_system.ident)
        request.cls.column = request.cls.catalog.create_gradebook_column(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_entry_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_grade_entry_form_for_create(
            request.cls.column.ident,
            AGENT_ID,
            [])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_grade_entry(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for grade_entry in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(grade_entry.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_entry_class_fixture", "grade_entry_test_fixture")
class TestGradeEntry(object):
    """Tests for GradeEntry"""
    def test_get_gradebook_column_id(self):
        """Tests get_gradebook_column_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_gradebook_column_id(), Id)
            assert str(self.object.get_gradebook_column_id()) == str(self.column.ident)

    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_gradebook_column(), GradebookColumn)
            assert str(self.object.get_gradebook_column().ident) == str(self.column.ident)

    def test_get_key_resource_id(self):
        """Tests get_key_resource_id"""
        if not is_never_authz(self.service_config):
            agent_id = self.object.get_key_resource_id()
            assert isinstance(agent_id, Id)

    def test_get_key_resource(self):
        """Tests get_key_resource"""
        if not is_never_authz(self.service_config):
            agent = self.object.get_key_resource()
            assert isinstance(agent, Agent)

    def test_is_derived(self):
        """Tests is_derived"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_derived(), bool)

    def test_overrides_calculated_entry(self):
        """Tests overrides_calculated_entry"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.overrides_calculated_entry(), bool)

    def test_get_overridden_calculated_entry_id(self):
        """Tests get_overridden_calculated_entry_id"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_overridden_calculated_entry_id)

    def test_get_overridden_calculated_entry(self):
        """Tests get_overridden_calculated_entry"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_overridden_calculated_entry)

    def test_is_ignored_for_calculations(self):
        """Tests is_ignored_for_calculations"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_ignored_for_calculations(), bool)

    def test_is_graded(self):
        """Tests is_graded"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_graded(), bool)

    def test_get_grade_id(self):
        """Tests get_grade_id"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_grade()

    def test_get_grade(self):
        """Tests get_grade"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_grade()

    def test_get_score(self):
        """Tests get_score"""
        if not is_never_authz(self.service_config):
            score = self.object.get_score()
            assert score is None

            # if this is set, should be a Decimal
            form = self.catalog.get_grade_entry_form_for_create(
                self.column.ident,
                AGENT_ID,
                [])
            form.set_score(50.0)
            new_grade_entry = self.catalog.create_grade_entry(form)

            assert new_grade_entry.get_score() == 50.0

    def test_get_time_graded(self):
        """Tests get_time_graded"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_time_graded()

    def test_get_grader_id(self):
        """Tests get_grader_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_grader_id()

    def test_get_grader(self):
        """Tests get_grader"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_grader()

    def test_get_grading_agent_id(self):
        """Tests get_grading_agent_id"""
        if not is_never_authz(self.service_config):
            agent_id = self.object.get_grading_agent_id()
            assert isinstance(agent_id, Id)

    def test_get_grading_agent(self):
        """Tests get_grading_agent"""
        if not is_never_authz(self.service_config):
            agent = self.object.get_grading_agent()
            assert isinstance(agent, Agent)

    def test_get_grade_entry_record(self):
        """Tests get_grade_entry_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_grade_entry_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_form_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        form.set_based_on_grades(True)
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

        form = request.cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(request.cls.grade_system.ident)
        request.cls.column = request.cls.catalog.create_gradebook_column(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_entry_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_grade_entry_form_for_create(
            request.cls.column.ident,
            AGENT_ID,
            [])


@pytest.mark.usefixtures("grade_entry_form_class_fixture", "grade_entry_form_test_fixture")
class TestGradeEntryForm(object):
    """Tests for GradeEntryForm"""
    def test_get_ignored_for_calculations_metadata(self):
        """Tests get_ignored_for_calculations_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_ignored_for_calculations_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_ignored_for_calculations(self):
        """Tests set_ignored_for_calculations"""
        self.form.set_ignored_for_calculations(True)
        assert self.form._my_map['ignoredForCalculations']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_ignored_for_calculations('false')

    def test_clear_ignored_for_calculations(self):
        """Tests clear_ignored_for_calculations"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_ignored_for_calculations(True)
        assert self.form._my_map['ignoredForCalculations']
        self.form.clear_ignored_for_calculations()
        assert self.form._my_map['ignoredForCalculations'] is None

    def test_get_grade_metadata(self):
        """Tests get_grade_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_grade_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_grade(self):
        """Tests set_grade"""
        # This should come from ResourceForm.set_avatar_template,
        #   but we override because in this case, there is no acceptable
        #   gradeId set, so we get an exception.
        with pytest.raises(errors.InvalidArgument):
            self.form.set_grade(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))

    def test_clear_grade(self):
        """Tests clear_grade"""
        # Normally this would follow ResourceForm.clear_avatar_template
        # Except we need a valid ``grade`` for the initial ``set_grade`` to
        #   work, so we provide a hand-written impl here.
        self.form._my_map['gradeId'] = 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        assert self.form._my_map['gradeId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_grade()
        assert self.form._my_map['gradeId'] == ''

    def test_get_score_metadata(self):
        """Tests get_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_score_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DECIMAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_score(self):
        """Tests set_score"""
        # because this GradeSystem is basedOnGrades, set_score() throws
        #   an exception
        with pytest.raises(errors.InvalidArgument):
            self.form.set_score(50.0)

    def test_clear_score(self):
        """Tests clear_score"""
        # because this GradeSystem is basedOnGrades, cannot use form.set_score()
        #   to set the initial data
        self.form._my_map['score'] = 50.0
        assert self.form._my_map['score'] is not None
        self.form.clear_score()

        # Also, because this is basedOnGrades, no exception thrown
        #  AND this method also does nothing...how confusing
        assert self.form._my_map['score'] is not None

    def test_get_grade_entry_form_record(self):
        """Tests get_grade_entry_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_grade_entry_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_list_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        form.set_based_on_grades(True)
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

        form = request.cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(request.cls.grade_system.ident)
        request.cls.column = request.cls.catalog.create_gradebook_column(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_entry_list_test_fixture(request):
    from dlkit.json_.grading.objects import GradeEntryList
    request.cls.grade_entry_list = list()
    request.cls.grade_entry_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_grade_entry_form_for_create(
                request.cls.column.ident,
                AGENT_ID,
                [])

            obj = request.cls.catalog.create_grade_entry(form)

            request.cls.grade_entry_list.append(obj)
            request.cls.grade_entry_ids.append(obj.ident)
        request.cls.grade_entry_list = GradeEntryList(request.cls.grade_entry_list)


@pytest.mark.usefixtures("grade_entry_list_class_fixture", "grade_entry_list_test_fixture")
class TestGradeEntryList(object):
    """Tests for GradeEntryList"""
    def test_get_next_grade_entry(self):
        """Tests get_next_grade_entry"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradeEntry
        if not is_never_authz(self.service_config):
            assert isinstance(self.grade_entry_list.get_next_grade_entry(), GradeEntry)

    def test_get_next_grade_entries(self):
        """Tests get_next_grade_entries"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList, GradeEntry
        if not is_never_authz(self.service_config):
            new_list = self.grade_entry_list.get_next_grade_entries(2)
            assert isinstance(new_list, GradeEntryList)
            for item in new_list:
                assert isinstance(item, GradeEntry)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_class_fixture(request):
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

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        request.cls.grade_system = request.cls.catalog.create_grade_system(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_entries():
                request.cls.catalog.delete_grade_entry(obj.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.catalog.delete_grade_system(request.cls.grade_system.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(request.cls.grade_system.ident)
        request.cls.object = request.cls.catalog.create_gradebook_column(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for gradebook_column in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(gradebook_column.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_column_class_fixture", "gradebook_column_test_fixture")
class TestGradebookColumn(object):
    """Tests for GradebookColumn"""
    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        if not is_never_authz(self.service_config):
            grade_system_id = self.object.get_grade_system_id()
            assert isinstance(grade_system_id, Id)
            assert str(grade_system_id) == str(self.grade_system.ident)

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        if not is_never_authz(self.service_config):
            grade_system = self.object.get_grade_system()
            assert isinstance(grade_system, GradeSystem)
            assert str(grade_system.ident) == str(self.grade_system.ident)

    def test_get_gradebook_column_record(self):
        """Tests get_gradebook_column_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_gradebook_column_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
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


@pytest.fixture(scope="function")
def gradebook_column_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_gradebook_column_form_for_create([])


@pytest.mark.usefixtures("gradebook_column_form_class_fixture", "gradebook_column_form_test_fixture")
class TestGradebookColumnForm(object):
    """Tests for GradebookColumnForm"""
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

    def test_get_gradebook_column_form_record(self):
        """Tests get_gradebook_column_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_gradebook_column_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnList tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.grading.objects import GradebookColumnList
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradebookColumnList tests'
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)
    request.cls.gradebook_column_list = GradebookColumnList(request.cls.gradebook_column_list)
    request.cls.object = request.cls.gradebook_column_list


@pytest.mark.usefixtures("gradebook_column_list_class_fixture", "gradebook_column_list_test_fixture")
class TestGradebookColumnList(object):
    """Tests for GradebookColumnList"""
    def test_get_next_gradebook_column(self):
        """Tests get_next_gradebook_column"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookColumn
        if not is_never_authz(self.service_config):
            assert isinstance(self.gradebook_column_list.get_next_gradebook_column(), GradebookColumn)

    def test_get_next_gradebook_columns(self):
        """Tests get_next_gradebook_columns"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList, GradebookColumn
        if not is_never_authz(self.service_config):
            new_list = self.gradebook_column_list.get_next_gradebook_columns(2)
            assert isinstance(new_list, GradebookColumnList)
            for item in new_list:
                assert isinstance(item, GradebookColumn)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_summary_class_fixture(request):
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
        create_form = request.cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradebookColumnLookupSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 100
        create_form.numeric_score_increment = 1
        request.cls.grade_system = request.cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradebookColumnLookupSession tests'
            create_form.grade_system = request.cls.grade_system.ident
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)
        for num in range(0, 100):
            create_form = request.cls.catalog.get_grade_entry_form_for_create(request.cls.gradebook_column_ids[0], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradebookColumnLookupSession tests'
            create_form.set_score(float(num))
            object = request.cls.catalog.create_grade_entry(create_form)
            request.cls.grade_entry_list.append(object)
            request.cls.grade_entry_ids.append(object.ident)
        request.cls.object = request.cls.catalog.get_gradebook_column_summary(request.cls.gradebook_column_ids[0])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_gradebooks():
                for obj in catalog.get_grade_entries():
                    catalog.delete_grade_entry(obj.ident)
                for obj in catalog.get_gradebook_columns():
                    catalog.delete_gradebook_column(obj.ident)
                for obj in catalog.get_grade_systems():
                    catalog.delete_grade_system(obj.ident)
                request.cls.svc_mgr.delete_gradebook(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_summary_test_fixture(request):
    pass


@pytest.mark.usefixtures("gradebook_column_summary_class_fixture", "gradebook_column_summary_test_fixture")
class TestGradebookColumnSummary(object):
    """Tests for GradebookColumnSummary"""
    def test_get_gradebook_column_id(self):
        """Tests get_gradebook_column_id"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_gradebook_column_id(), Id)
            assert str(self.object.get_gradebook_column_id()) == str(self.gradebook_column_ids[0])

    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_gradebook_column(), GradebookColumn)
            assert str(self.object.get_gradebook_column().ident) == str(self.gradebook_column_ids[0])

    def test_get_mean(self):
        """Tests get_mean"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_mean(), Decimal)
            assert self.object.get_mean() == Decimal(49.5)

    def test_get_median(self):
        """Tests get_median"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_median(), Decimal)
            assert self.object.get_median() == Decimal(49.5)

    def test_get_mode(self):
        """Tests get_mode"""
        # From test_templates/assessment.py::AssessmentTaken::get_score_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_mode(), Decimal)
            assert self.object.get_mode() == Decimal(0.0)

    def test_get_rms(self):
        """Tests get_rms"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_rms(), Decimal)
            assert self.object.get_rms() == Decimal('57.30183243143276652887614453')

    def test_get_standard_deviation(self):
        """Tests get_standard_deviation"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_standard_deviation(), Decimal)
            assert self.object.get_standard_deviation() == Decimal('28.86607004772211800433171979')

    def test_get_sum(self):
        """Tests get_sum"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.get_sum(), Decimal)
            assert self.object.get_sum() == Decimal('4950')

    def test_get_gradebook_column_summary_record(self):
        """Tests get_gradebook_column_summary_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_gradebook_column_summary_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_gradebook(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_class_fixture", "gradebook_test_fixture")
class TestGradebook(object):
    """Tests for Gradebook"""
    def test_get_gradebook_record(self):
        """Tests get_gradebook_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_gradebook_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_gradebook_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_form_class_fixture", "gradebook_form_test_fixture")
class TestGradebookForm(object):
    """Tests for GradebookForm"""
    def test_get_gradebook_form_record(self):
        """Tests get_gradebook_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_gradebook_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookList tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.gradebook_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.gradebook_ids:
                request.cls.svc_mgr.delete_gradebook(obj)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.grading.objects import GradebookList
    request.cls.gradebook_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test Gradebook ' + str(num)
            create_form.description = 'Test Gradebook for GradebookList tests'
            obj = request.cls.svc_mgr.create_gradebook(create_form)
            request.cls.gradebook_list.append(obj)
            request.cls.gradebook_ids.append(obj.ident)
    request.cls.gradebook_list = GradebookList(request.cls.gradebook_list)


@pytest.mark.usefixtures("gradebook_list_class_fixture", "gradebook_list_test_fixture")
class TestGradebookList(object):
    """Tests for GradebookList"""
    def test_get_next_gradebook(self):
        """Tests get_next_gradebook"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import Gradebook
        if not is_never_authz(self.service_config):
            assert isinstance(self.gradebook_list.get_next_gradebook(), Gradebook)

    def test_get_next_gradebooks(self):
        """Tests get_next_gradebooks"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookList, Gradebook
        if not is_never_authz(self.service_config):
            new_list = self.gradebook_list.get_next_gradebooks(2)
            assert isinstance(new_list, GradebookList)
            for item in new_list:
                assert isinstance(item, Gradebook)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.gradebook_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.grading.objects import GradebookNode
    request.cls.gradebook_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test Gradebook ' + str(num)
            create_form.description = 'Test Gradebook for GradebookNode tests'
            obj = request.cls.svc_mgr.create_gradebook(create_form)
            request.cls.gradebook_list.append(GradebookNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.gradebook_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_gradebook(request.cls.gradebook_list[0].ident)
        request.cls.svc_mgr.add_child_gradebook(
            request.cls.gradebook_list[0].ident,
            request.cls.gradebook_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_gradebook_nodes(
            request.cls.gradebook_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_gradebook(
                request.cls.gradebook_list[0].ident,
                request.cls.gradebook_list[1].ident)
            request.cls.svc_mgr.remove_root_gradebook(request.cls.gradebook_list[0].ident)
            for node in request.cls.gradebook_list:
                request.cls.svc_mgr.delete_gradebook(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_node_class_fixture", "gradebook_node_test_fixture")
class TestGradebookNode(object):
    """Tests for GradebookNode"""
    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.grading.objects import Gradebook
        if not is_never_authz(self.service_config):
            assert isinstance(self.gradebook_list[0].get_gradebook(), OsidCatalog)
            assert str(self.gradebook_list[0].get_gradebook().ident) == str(self.gradebook_list[0].ident)

    def test_get_parent_gradebook_nodes(self):
        """Tests get_parent_gradebook_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.grading.objects import GradebookNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_gradebook_nodes(
                self.gradebook_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_gradebook_nodes(), GradebookNodeList)
            assert node.get_parent_gradebook_nodes().available() == 1
            assert str(node.get_parent_gradebook_nodes().next().ident) == str(self.gradebook_list[0].ident)

    def test_get_child_gradebook_nodes(self):
        """Tests get_child_gradebook_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.grading.objects import GradebookNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_gradebook_nodes(
                self.gradebook_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_gradebook_nodes(), GradebookNodeList)
            assert node.get_child_gradebook_nodes().available() == 1
            assert str(node.get_child_gradebook_nodes().next().ident) == str(self.gradebook_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.gradebook_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.gradebook_node_ids:
                request.cls.svc_mgr.delete_gradebook(obj)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def gradebook_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.grading.objects import GradebookNodeList, GradebookNode
    request.cls.gradebook_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test GradebookNode ' + str(num)
            create_form.description = 'Test GradebookNode for GradebookNodeList tests'
            obj = request.cls.svc_mgr.create_gradebook(create_form)
            request.cls.gradebook_node_list.append(GradebookNode(obj.object_map))
            request.cls.gradebook_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_gradebook(request.cls.gradebook_node_list[0].ident)
        request.cls.svc_mgr.add_child_gradebook(
            request.cls.gradebook_node_list[0].ident,
            request.cls.gradebook_node_list[1].ident)
    request.cls.gradebook_node_list = GradebookNodeList(request.cls.gradebook_node_list)


@pytest.mark.usefixtures("gradebook_node_list_class_fixture", "gradebook_node_list_test_fixture")
class TestGradebookNodeList(object):
    """Tests for GradebookNodeList"""
    def test_get_next_gradebook_node(self):
        """Tests get_next_gradebook_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.gradebook_node_list.get_next_gradebook_node(), GradebookNode)

    def test_get_next_gradebook_nodes(self):
        """Tests get_next_gradebook_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookNodeList, GradebookNode
        if not is_never_authz(self.service_config):
            new_list = self.gradebook_node_list.get_next_gradebook_nodes(2)
            assert isinstance(new_list, GradebookNodeList)
            for item in new_list:
                assert isinstance(item, GradebookNode)
