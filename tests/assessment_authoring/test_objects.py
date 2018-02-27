"""Unit tests of assessment.authoring objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.assessment.objects import Assessment
from dlkit.abstract_osid.assessment_authoring import objects as ABCObjects
from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


SIMPLE_SEQUENCE_RECORD_TYPE = Type(**{"authority": "ODL.MIT.EDU", "namespace": "osid-object", "identifier": "simple-child-sequencing"})
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPart tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPart tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.use_unsequestered_assessment_part_view()
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                      [])
        request.cls.object = request.cls.catalog.create_assessment_part_for_assessment(form)
        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for assessment_part in request.cls.catalog.get_assessment_parts_for_assessment(request.cls.assessment.ident):
                if assessment_part.has_children():
                    for child_id in assessment_part.get_child_ids():
                        try:
                            request.cls.catalog.delete_assessment_part(child_id)
                        except errors.NotFound:
                            pass
                request.cls.catalog.delete_assessment_part(assessment_part.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_part_class_fixture", "assessment_part_test_fixture")
class TestAssessmentPart(object):
    """Tests for AssessmentPart"""
    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        if not is_never_authz(self.service_config):
            result_id = self.object.get_assessment_id()
            assert isinstance(result_id, Id)
            assert str(result_id) == str(self.assessment.ident)

    def test_get_assessment(self):
        """Tests get_assessment"""
        if not is_never_authz(self.service_config):
            result = self.object.get_assessment()
            assert isinstance(result, Assessment)
            assert str(result.ident) == str(self.assessment.ident)

    def test_has_parent_part(self):
        """Tests has_parent_part"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_parent_part(), bool)

    def test_get_assessment_part_id(self):
        """Tests get_assessment_part_id"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_assessment_part_id()

    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_assessment_part()

    def test_is_section(self):
        """Tests is_section"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_section(), bool)

    def test_get_weight(self):
        """Tests get_weight"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_weight()

    def test_get_allocated_time(self):
        """Tests get_allocated_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_allocated_time()

    def test_get_child_assessment_part_ids(self):
        """Tests get_child_assessment_part_ids"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_child_assessment_part_ids()

            # to get these back, need to have a simple sequencing part as the parent
            form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                                   [SIMPLE_SEQUENCE_RECORD_TYPE])
            form.set_children([Id('assessment.Part%3A000000000000000000000000%40ODL.MIT.EDU')])
            parent_part = self.catalog.create_assessment_part_for_assessment(form)

            results = parent_part.get_child_assessment_part_ids()
            assert isinstance(results, IdList)
            assert results.available() == 1
            assert str(results.next()) == 'assessment.Part%3A000000000000000000000000%40ODL.MIT.EDU'

    def test_get_child_assessment_parts(self):
        """Tests get_child_assessment_parts"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.IllegalState):
                self.object.get_child_assessment_parts()

            # to get these back, need to have a simple sequencing part as the parent

            form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                                   [SIMPLE_SEQUENCE_RECORD_TYPE])
            parent_part = self.catalog.create_assessment_part_for_assessment(form)

            form = self.catalog.get_assessment_part_form_for_create_for_assessment_part(parent_part.ident,
                                                                                        [])
            child_part = self.catalog.create_assessment_part_for_assessment(form)

            parent_part = self.catalog.get_assessment_part(parent_part.ident)

            results = parent_part.get_child_assessment_part_ids()
            assert isinstance(results, IdList)
            assert results.available() == 1
            assert str(results.next()) == str(child_part.ident)

    def test_get_assessment_part_record(self):
        """Tests get_assessment_part_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_assessment_part_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartForm tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.use_unsequestered_assessment_part_view()
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                                  [])
        request.cls.object = request.cls.form
        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)


@pytest.mark.usefixtures("assessment_part_form_class_fixture", "assessment_part_form_test_fixture")
class TestAssessmentPartForm(object):
    """Tests for AssessmentPartForm"""
    def test_get_weight_metadata(self):
        """Tests get_weight_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_weight_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'CARDINAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_weight(self):
        """Tests set_weight"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.set_weight(True)

    def test_clear_weight(self):
        """Tests clear_weight"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.clear_weight()

    def test_get_allocated_time_metadata(self):
        """Tests get_allocated_time_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_allocated_time_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DURATION'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_allocated_time(self):
        """Tests set_allocated_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_duration_template
        if not is_never_authz(self.service_config):
            test_duration = Duration(hours=1)
            assert self.form._my_map['allocatedTime'] is None
            self.form.set_allocated_time(test_duration)
            assert self.form._my_map['allocatedTime']['seconds'] == 3600
            assert self.form._my_map['allocatedTime']['days'] == 0
            assert self.form._my_map['allocatedTime']['microseconds'] == 0
            with pytest.raises(errors.InvalidArgument):
                self.form.set_allocated_time(1.05)
            # reset this for other tests
            self.form._my_map['allocatedTime'] = None

    def test_clear_allocated_time(self):
        """Tests clear_allocated_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_duration_template
        if not is_never_authz(self.service_config):
            test_duration = Duration(hours=1)
            assert self.form._my_map['allocatedTime'] is None
            self.form.set_allocated_time(test_duration)
            assert self.form._my_map['allocatedTime']['seconds'] == 3600
            assert self.form._my_map['allocatedTime']['days'] == 0
            assert self.form._my_map['allocatedTime']['microseconds'] == 0
            self.form.clear_allocated_time()
            assert self.form._my_map['allocatedTime'] == self.form.get_allocated_time_metadata().get_default_duration_values()[0]

    def test_get_assessment_part_form_record(self):
        """Tests get_assessment_part_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_assessment_part_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartList tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

        request.cls.form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                                  [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.use_unsequestered_assessment_part_view()
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_list_test_fixture(request):
    from dlkit.json_.assessment_authoring.objects import AssessmentPartList
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()

    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])

            obj = request.cls.catalog.create_assessment_part_for_assessment(form)

            request.cls.assessment_part_list.append(obj)
            request.cls.assessment_part_ids.append(obj.ident)
        request.cls.assessment_part_list = AssessmentPartList(request.cls.assessment_part_list)


@pytest.mark.usefixtures("assessment_part_list_class_fixture", "assessment_part_list_test_fixture")
class TestAssessmentPartList(object):
    """Tests for AssessmentPartList"""
    def test_get_next_assessment_part(self):
        """Tests get_next_assessment_part"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        if not is_never_authz(self.service_config):
            assert isinstance(self.assessment_part_list.get_next_assessment_part(), AssessmentPart)

    def test_get_next_assessment_parts(self):
        """Tests get_next_assessment_parts"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList, AssessmentPart
        if not is_never_authz(self.service_config):
            new_list = self.assessment_part_list.get_next_assessment_parts(2)
            assert isinstance(new_list, AssessmentPartList)
            for item in new_list:
                assert isinstance(item, AssessmentPart)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.sequence_rule_list = list()
    request.cls.sequence_rule_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRule tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRule tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRule tests'
        request.cls.assessment_part_1 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRule tests'
        request.cls.assessment_part_2 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def sequence_rule_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                     request.cls.assessment_part_2.ident,
                                                                     [])
        request.cls.object = request.cls.catalog.create_sequence_rule(form)


@pytest.mark.usefixtures("sequence_rule_class_fixture", "sequence_rule_test_fixture")
class TestSequenceRule(object):
    """Tests for SequenceRule"""
    def test_get_assessment_part_id(self):
        """Tests get_assessment_part_id"""
        if not is_never_authz(self.service_config):
            part_id = self.object.get_assessment_part_id()
            assert isinstance(part_id, Id)
            assert str(part_id) == str(self.assessment_part_1.ident)

    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        if not is_never_authz(self.service_config):
            part = self.object.get_assessment_part()
            assert isinstance(part, AssessmentPart)
            assert str(part.ident) == str(self.assessment_part_1.ident)

    @pytest.mark.skip('unimplemented test')
    def test_get_next_assessment_part_id(self):
        """Tests get_next_assessment_part_id"""
        pass

    def test_get_next_assessment_part(self):
        """Tests get_next_assessment_part"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_next_assessment_part()

    def test_get_minimum_score(self):
        """Tests get_minimum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_minimum_score()

    def test_get_maximum_score(self):
        """Tests get_maximum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_maximum_score()

    def test_is_cumulative(self):
        """Tests is_cumulative"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_cumulative(), bool)

    def test_get_applied_assessment_part_ids(self):
        """Tests get_applied_assessment_part_ids"""
        if not is_never_authz(self.service_config):
            result = self.object.get_applied_assessment_part_ids()
            assert isinstance(result, IdList)
            assert result.available() == 0

    def test_get_applied_assessment_parts(self):
        """Tests get_applied_assessment_parts"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_applied_assessment_parts()

    def test_get_sequence_rule_record(self):
        """Tests get_sequence_rule_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_sequence_rule_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.sequence_rule_list = list()
    request.cls.sequence_rule_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleForm tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleForm tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleForm tests'
        request.cls.assessment_part_1 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleForm tests'
        request.cls.assessment_part_2 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def sequence_rule_form_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                                 request.cls.assessment_part_2.ident,
                                                                                 [])
        request.cls.object = request.cls.form


@pytest.mark.usefixtures("sequence_rule_form_class_fixture", "sequence_rule_form_test_fixture")
class TestSequenceRuleForm(object):
    """Tests for SequenceRuleForm"""
    def test_get_minimum_score_metadata(self):
        """Tests get_minimum_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_minimum_score_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'CARDINAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_minimum_score(self):
        """Tests set_minimum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.set_minimum_score(True)

    def test_get_maximum_score_metadata(self):
        """Tests get_maximum_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_maximum_score_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'CARDINAL'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_maximum_score(self):
        """Tests set_maximum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.set_maximum_score(True)

    def test_get_cumulative_metadata(self):
        """Tests get_cumulative_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_cumulative_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_cumulative(self):
        """Tests set_cumulative"""
        if not is_never_authz(self.service_config):
            create_form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                         self.assessment_part_2.ident,
                                                                         [])
            create_form.set_cumulative(True)
            assert create_form._my_map['cumulative']

    def test_get_applied_assessment_parts_metadata(self):
        """Tests get_applied_assessment_parts_metadata"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_applied_assessment_parts_metadata()

    def test_apply_assessment_parts(self):
        """Tests apply_assessment_parts"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.apply_assessment_parts(True)

    def test_get_sequence_rule_form_record(self):
        """Tests get_sequence_rule_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_sequence_rule_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.sequence_rule_list = list()
    request.cls.sequence_rule_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleList tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleList tests'
        request.cls.assessment_part_1 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleList tests'
        request.cls.assessment_part_2 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        request.cls.form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                                 request.cls.assessment_part_2.ident,
                                                                                 [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_sequence_rules():
                request.cls.catalog.delete_sequence_rule(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def sequence_rule_list_test_fixture(request):
    from dlkit.json_.assessment_authoring.objects import SequenceRuleList
    request.cls.sequence_rule_list = list()
    request.cls.sequence_rule_ids = list()

    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                         request.cls.assessment_part_2.ident,
                                                                         [])
            obj = request.cls.catalog.create_sequence_rule(form)

            request.cls.sequence_rule_list.append(obj)
            request.cls.sequence_rule_ids.append(obj.ident)
        request.cls.sequence_rule_list = SequenceRuleList(request.cls.sequence_rule_list)


@pytest.mark.usefixtures("sequence_rule_list_class_fixture", "sequence_rule_list_test_fixture")
class TestSequenceRuleList(object):
    """Tests for SequenceRuleList"""
    def test_get_next_sequence_rule(self):
        """Tests get_next_sequence_rule"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRule
        if not is_never_authz(self.service_config):
            assert isinstance(self.sequence_rule_list.get_next_sequence_rule(), SequenceRule)

    def test_get_next_sequence_rules(self):
        """Tests get_next_sequence_rules"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList, SequenceRule
        if not is_never_authz(self.service_config):
            new_list = self.sequence_rule_list.get_next_sequence_rules(2)
            assert isinstance(new_list, SequenceRuleList)
            for item in new_list:
                assert isinstance(item, SequenceRule)
