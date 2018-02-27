"""Unit tests of assessment.authoring queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.json_.assessment_authoring.queries import SequenceRuleQuery
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
def assessment_part_query_class_fixture(request):
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
        create_form.description = 'Test Bank for AssessmentPartQuery tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartQuery tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.use_unsequestered_assessment_part_view()
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_query_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.catalog.get_assessment_part_query()


@pytest.mark.usefixtures("assessment_part_query_class_fixture", "assessment_part_query_test_fixture")
class TestAssessmentPartQuery(object):
    """Tests for AssessmentPartQuery"""
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

    def test_match_parent_assessment_part_id(self):
        """Tests match_parent_assessment_part_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'parentAssessmentPartId' not in self.query._query_terms
        self.query.match_parent_assessment_part_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['parentAssessmentPartId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_parent_assessment_part_id_terms(self):
        """Tests clear_parent_assessment_part_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_parent_assessment_part_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'parentAssessmentPartId' in self.query._query_terms
        self.query.clear_parent_assessment_part_id_terms()
        if is_no_authz(self.service_config):
            assert 'parentAssessmentPartId' not in self.query._query_terms

    def test_supports_parent_assessment_part_query(self):
        """Tests supports_parent_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_parent_assessment_part_query()

    def test_get_parent_assessment_part_query(self):
        """Tests get_parent_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_parent_assessment_part_query()

    def test_match_any_parent_assessment_part(self):
        """Tests match_any_parent_assessment_part"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_parent_assessment_part(True)

    def test_clear_parent_assessment_part_terms(self):
        """Tests clear_parent_assessment_part_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_parent_assessment_part_terms()

    def test_match_section(self):
        """Tests match_section"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_section(True)

    def test_clear_section_terms(self):
        """Tests clear_section_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_section_terms()

    def test_match_weight(self):
        """Tests match_weight"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_weight(True, True, True)

    def test_match_any_weight(self):
        """Tests match_any_weight"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_weight(True)

    def test_clear_weight_terms(self):
        """Tests clear_weight_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['weight'] = 'foo'
        self.query.clear_weight_terms()
        if is_no_authz(self.service_config):
            assert 'weight' not in self.query._query_terms

    def test_match_allocated_time(self):
        """Tests match_allocated_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_allocated_time(True, True, True)

    def test_match_any_allocated_time(self):
        """Tests match_any_allocated_time"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_allocated_time(True)

    def test_clear_allocated_time_terms(self):
        """Tests clear_allocated_time_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['allocatedTime'] = 'foo'
        self.query.clear_allocated_time_terms()
        if is_no_authz(self.service_config):
            assert 'allocatedTime' not in self.query._query_terms

    def test_match_child_assessment_part_id(self):
        """Tests match_child_assessment_part_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'childAssessmentPartId' not in self.query._query_terms
        self.query.match_child_assessment_part_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['childAssessmentPartId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_child_assessment_part_id_terms(self):
        """Tests clear_child_assessment_part_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_child_assessment_part_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'childAssessmentPartId' in self.query._query_terms
        self.query.clear_child_assessment_part_id_terms()
        if is_no_authz(self.service_config):
            assert 'childAssessmentPartId' not in self.query._query_terms

    def test_supports_child_assessment_part_query(self):
        """Tests supports_child_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_child_assessment_part_query()

    def test_get_child_assessment_part_query(self):
        """Tests get_child_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_child_assessment_part_query()

    def test_match_any_child_assessment_part(self):
        """Tests match_any_child_assessment_part"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_child_assessment_part(True)

    def test_clear_child_assessment_part_terms(self):
        """Tests clear_child_assessment_part_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_child_assessment_part_terms()

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

    def test_get_assessment_part_query_record(self):
        """Tests get_assessment_part_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_part_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleQuery tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_sequence_rules():
                request.cls.catalog.delete_sequence_rule(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def sequence_rule_query_test_fixture(request):
    # Since the session isn't implemented, we just construct an SequenceRuleQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = SequenceRuleQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("sequence_rule_query_class_fixture", "sequence_rule_query_test_fixture")
class TestSequenceRuleQuery(object):
    """Tests for SequenceRuleQuery"""
    def test_match_assessment_part_id(self):
        """Tests match_assessment_part_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_assessment_part_id(True, True)

    def test_clear_assessment_part_id_terms(self):
        """Tests clear_assessment_part_id_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_assessment_part_id_terms()

    def test_supports_assessment_part_query(self):
        """Tests supports_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_assessment_part_query()

    def test_get_assessment_part_query(self):
        """Tests get_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_assessment_part_query()

    def test_clear_assessment_part_terms(self):
        """Tests clear_assessment_part_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_assessment_part_terms()

    def test_match_next_assessment_part_id(self):
        """Tests match_next_assessment_part_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_next_assessment_part_id(True, True)

    def test_clear_next_assessment_part_id_terms(self):
        """Tests clear_next_assessment_part_id_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_next_assessment_part_id_terms()

    def test_supports_next_assessment_part_query(self):
        """Tests supports_next_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_next_assessment_part_query()

    def test_get_next_assessment_part_query(self):
        """Tests get_next_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_next_assessment_part_query()

    def test_clear_next_assessment_part_terms(self):
        """Tests clear_next_assessment_part_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_next_assessment_part_terms()

    def test_match_minimum_score(self):
        """Tests match_minimum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_score(True, True, True)

    def test_match_any_minimum_score(self):
        """Tests match_any_minimum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_minimum_score(True)

    def test_clear_minimum_score_terms(self):
        """Tests clear_minimum_score_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_score_terms()

    def test_match_maximum_score(self):
        """Tests match_maximum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_maximum_score(True, True, True)

    def test_match_any_maximum_score(self):
        """Tests match_any_maximum_score"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_maximum_score(True)

    def test_clear_maximum_score_terms(self):
        """Tests clear_maximum_score_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_maximum_score_terms()

    def test_match_cumulative(self):
        """Tests match_cumulative"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_cumulative(True)

    def test_clear_cumulative_terms(self):
        """Tests clear_cumulative_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_cumulative_terms()

    def test_match_applied_assessment_part_id(self):
        """Tests match_applied_assessment_part_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_applied_assessment_part_id(True, True)

    def test_clear_applied_assessment_part_id_terms(self):
        """Tests clear_applied_assessment_part_id_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_applied_assessment_part_id_terms()

    def test_supports_applied_assessment_part_query(self):
        """Tests supports_applied_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_applied_assessment_part_query()

    def test_get_applied_assessment_part_query(self):
        """Tests get_applied_assessment_part_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_applied_assessment_part_query()

    def test_match_any_applied_assessment_part(self):
        """Tests match_any_applied_assessment_part"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_applied_assessment_part(True)

    def test_clear_applied_assessment_part_terms(self):
        """Tests clear_applied_assessment_part_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_applied_assessment_part_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_bank_id(True, True)

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_bank_id_terms()

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
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_bank_terms()

    def test_get_sequence_rule_query_record(self):
        """Tests get_sequence_rule_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_sequence_rule_query_record(True)
