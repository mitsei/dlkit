"""Unit tests of learning queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.json_.learning.queries import ActivityQuery
from dlkit.json_.learning.queries import ObjectiveBankQuery
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
def objective_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_objective_query()


@pytest.mark.usefixtures("objective_query_class_fixture", "objective_query_test_fixture")
class TestObjectiveQuery(object):
    """Tests for ObjectiveQuery"""
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
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assessment'] = 'foo'
        self.query.clear_assessment_terms()
        if is_no_authz(self.service_config):
            assert 'assessment' not in self.query._query_terms

    def test_match_knowledge_category_id(self):
        """Tests match_knowledge_category_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'knowledgeCategoryId' not in self.query._query_terms
        self.query.match_knowledge_category_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['knowledgeCategoryId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_knowledge_category_id_terms(self):
        """Tests clear_knowledge_category_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_knowledge_category_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'knowledgeCategoryId' in self.query._query_terms
        self.query.clear_knowledge_category_id_terms()
        if is_no_authz(self.service_config):
            assert 'knowledgeCategoryId' not in self.query._query_terms

    def test_supports_knowledge_category_query(self):
        """Tests supports_knowledge_category_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_knowledge_category_query()

    def test_get_knowledge_category_query(self):
        """Tests get_knowledge_category_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_knowledge_category_query()

    def test_match_any_knowledge_category(self):
        """Tests match_any_knowledge_category"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_knowledge_category(True)

    def test_clear_knowledge_category_terms(self):
        """Tests clear_knowledge_category_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['knowledgeCategory'] = 'foo'
        self.query.clear_knowledge_category_terms()
        if is_no_authz(self.service_config):
            assert 'knowledgeCategory' not in self.query._query_terms

    def test_match_cognitive_process_id(self):
        """Tests match_cognitive_process_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'cognitiveProcessId' not in self.query._query_terms
        self.query.match_cognitive_process_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['cognitiveProcessId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_cognitive_process_id_terms(self):
        """Tests clear_cognitive_process_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_cognitive_process_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'cognitiveProcessId' in self.query._query_terms
        self.query.clear_cognitive_process_id_terms()
        if is_no_authz(self.service_config):
            assert 'cognitiveProcessId' not in self.query._query_terms

    def test_supports_cognitive_process_query(self):
        """Tests supports_cognitive_process_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_cognitive_process_query()

    def test_get_cognitive_process_query(self):
        """Tests get_cognitive_process_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_cognitive_process_query()

    def test_match_any_cognitive_process(self):
        """Tests match_any_cognitive_process"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_cognitive_process(True)

    def test_clear_cognitive_process_terms(self):
        """Tests clear_cognitive_process_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['cognitiveProcess'] = 'foo'
        self.query.clear_cognitive_process_terms()
        if is_no_authz(self.service_config):
            assert 'cognitiveProcess' not in self.query._query_terms

    def test_match_activity_id(self):
        """Tests match_activity_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'activityId' not in self.query._query_terms
        self.query.match_activity_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['activityId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_activity_id_terms(self):
        """Tests clear_activity_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_activity_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'activityId' in self.query._query_terms
        self.query.clear_activity_id_terms()
        if is_no_authz(self.service_config):
            assert 'activityId' not in self.query._query_terms

    def test_supports_activity_query(self):
        """Tests supports_activity_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_activity_query()

    def test_get_activity_query(self):
        """Tests get_activity_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_activity_query()

    def test_match_any_activity(self):
        """Tests match_any_activity"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_activity(True)

    def test_clear_activity_terms(self):
        """Tests clear_activity_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_activity_terms()

    def test_match_requisite_objective_id(self):
        """Tests match_requisite_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'requisiteObjectiveId' not in self.query._query_terms
        self.query.match_requisite_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['requisiteObjectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_requisite_objective_id_terms(self):
        """Tests clear_requisite_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_requisite_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'requisiteObjectiveId' in self.query._query_terms
        self.query.clear_requisite_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'requisiteObjectiveId' not in self.query._query_terms

    def test_supports_requisite_objective_query(self):
        """Tests supports_requisite_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_requisite_objective_query()

    def test_get_requisite_objective_query(self):
        """Tests get_requisite_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_requisite_objective_query()

    def test_match_any_requisite_objective(self):
        """Tests match_any_requisite_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_requisite_objective(True)

    def test_clear_requisite_objective_terms(self):
        """Tests clear_requisite_objective_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_requisite_objective_terms()

    def test_match_dependent_objective_id(self):
        """Tests match_dependent_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'dependentObjectiveId' not in self.query._query_terms
        self.query.match_dependent_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['dependentObjectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_dependent_objective_id_terms(self):
        """Tests clear_dependent_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_dependent_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'dependentObjectiveId' in self.query._query_terms
        self.query.clear_dependent_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'dependentObjectiveId' not in self.query._query_terms

    def test_supports_depndent_objective_query(self):
        """Tests supports_depndent_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_depndent_objective_query()

    def test_get_dependent_objective_query(self):
        """Tests get_dependent_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_dependent_objective_query()

    def test_match_any_dependent_objective(self):
        """Tests match_any_dependent_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_dependent_objective(True)

    def test_clear_dependent_objective_terms(self):
        """Tests clear_dependent_objective_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_dependent_objective_terms()

    def test_match_equivalent_objective_id(self):
        """Tests match_equivalent_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'equivalentObjectiveId' not in self.query._query_terms
        self.query.match_equivalent_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['equivalentObjectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_equivalent_objective_id_terms(self):
        """Tests clear_equivalent_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_equivalent_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'equivalentObjectiveId' in self.query._query_terms
        self.query.clear_equivalent_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'equivalentObjectiveId' not in self.query._query_terms

    def test_supports_equivalent_objective_query(self):
        """Tests supports_equivalent_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_equivalent_objective_query()

    def test_get_equivalent_objective_query(self):
        """Tests get_equivalent_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_equivalent_objective_query()

    def test_match_any_equivalent_objective(self):
        """Tests match_any_equivalent_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_equivalent_objective(True)

    def test_clear_equivalent_objective_terms(self):
        """Tests clear_equivalent_objective_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_equivalent_objective_terms()

    def test_match_ancestor_objective_id(self):
        """Tests match_ancestor_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'ancestorObjectiveId' not in self.query._query_terms
        self.query.match_ancestor_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['ancestorObjectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_ancestor_objective_id_terms(self):
        """Tests clear_ancestor_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_ancestor_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'ancestorObjectiveId' in self.query._query_terms
        self.query.clear_ancestor_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'ancestorObjectiveId' not in self.query._query_terms

    def test_supports_ancestor_objective_query(self):
        """Tests supports_ancestor_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_objective_query()

    def test_get_ancestor_objective_query(self):
        """Tests get_ancestor_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_objective_query()

    def test_match_any_ancestor_objective(self):
        """Tests match_any_ancestor_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_objective(True)

    def test_clear_ancestor_objective_terms(self):
        """Tests clear_ancestor_objective_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_ancestor_objective_terms()

    def test_match_descendant_objective_id(self):
        """Tests match_descendant_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'descendantObjectiveId' not in self.query._query_terms
        self.query.match_descendant_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['descendantObjectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_descendant_objective_id_terms(self):
        """Tests clear_descendant_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_descendant_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'descendantObjectiveId' in self.query._query_terms
        self.query.clear_descendant_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'descendantObjectiveId' not in self.query._query_terms

    def test_supports_descendant_objective_query(self):
        """Tests supports_descendant_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_objective_query()

    def test_get_descendant_objective_query(self):
        """Tests get_descendant_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_objective_query()

    def test_match_any_descendant_objective(self):
        """Tests match_any_descendant_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_objective(True)

    def test_clear_descendant_objective_terms(self):
        """Tests clear_descendant_objective_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_descendant_objective_terms()

    def test_match_objective_bank_id(self):
        """Tests match_objective_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedObjectiveBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_objective_bank_id_terms(self):
        """Tests clear_objective_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedObjectiveBankIds' in self.query._query_terms
        self.query.clear_objective_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedObjectiveBankIds' not in self.query._query_terms

    def test_supports_objective_bank_query(self):
        """Tests supports_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_objective_bank_query()

    def test_get_objective_bank_query(self):
        """Tests get_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_bank_query()

    def test_clear_objective_bank_terms(self):
        """Tests clear_objective_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objectiveBank'] = 'foo'
        self.query.clear_objective_bank_terms()
        if is_no_authz(self.service_config):
            assert 'objectiveBank' not in self.query._query_terms

    def test_get_objective_query_record(self):
        """Tests get_objective_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityQuery tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ActivityQuery'
        create_form.description = 'Test Objective for ActivityQuery tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_activities():
                    catalog.delete_activity(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_query_test_fixture(request):
    # Since the session isn't implemented, we just construct an ActivityQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = ActivityQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("activity_query_class_fixture", "activity_query_test_fixture")
class TestActivityQuery(object):
    """Tests for ActivityQuery"""
    def test_match_objective_id(self):
        """Tests match_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'objectiveId' not in self.query._query_terms
        self.query.match_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['objectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_objective_id_terms(self):
        """Tests clear_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'objectiveId' in self.query._query_terms
        self.query.clear_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'objectiveId' not in self.query._query_terms

    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_objective_query()

    def test_get_objective_query(self):
        """Tests get_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_query()

    def test_clear_objective_terms(self):
        """Tests clear_objective_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objective'] = 'foo'
        self.query.clear_objective_terms()
        if is_no_authz(self.service_config):
            assert 'objective' not in self.query._query_terms

    def test_match_asset_id(self):
        """Tests match_asset_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assetId' not in self.query._query_terms
        self.query.match_asset_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assetId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_asset_id_terms(self):
        """Tests clear_asset_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assetId' in self.query._query_terms
        self.query.clear_asset_id_terms()
        if is_no_authz(self.service_config):
            assert 'assetId' not in self.query._query_terms

    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_asset_query()

    def test_get_asset_query(self):
        """Tests get_asset_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_asset_query()

    def test_match_any_asset(self):
        """Tests match_any_asset"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_asset(True)

    def test_clear_asset_terms(self):
        """Tests clear_asset_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_asset_terms()

    def test_match_course_id(self):
        """Tests match_course_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'courseId' not in self.query._query_terms
        self.query.match_course_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['courseId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_course_id_terms(self):
        """Tests clear_course_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_course_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'courseId' in self.query._query_terms
        self.query.clear_course_id_terms()
        if is_no_authz(self.service_config):
            assert 'courseId' not in self.query._query_terms

    def test_supports_course_query(self):
        """Tests supports_course_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_course_query()

    def test_get_course_query(self):
        """Tests get_course_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_course_query()

    def test_match_any_course(self):
        """Tests match_any_course"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_course(True)

    def test_clear_course_terms(self):
        """Tests clear_course_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_course_terms()

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

    def test_match_objective_bank_id(self):
        """Tests match_objective_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedObjectiveBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_objective_bank_id_terms(self):
        """Tests clear_objective_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedObjectiveBankIds' in self.query._query_terms
        self.query.clear_objective_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedObjectiveBankIds' not in self.query._query_terms

    def test_supports_objective_bank_query(self):
        """Tests supports_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_objective_bank_query()

    def test_get_objective_bank_query(self):
        """Tests get_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_bank_query()

    def test_clear_objective_bank_terms(self):
        """Tests clear_objective_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objectiveBank'] = 'foo'
        self.query.clear_objective_bank_terms()
        if is_no_authz(self.service_config):
            assert 'objectiveBank' not in self.query._query_terms

    def test_get_activity_query_record(self):
        """Tests get_activity_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_activity_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_proficiency_query()


@pytest.mark.usefixtures("proficiency_query_class_fixture", "proficiency_query_test_fixture")
class TestProficiencyQuery(object):
    """Tests for ProficiencyQuery"""
    def test_match_resource_id(self):
        """Tests match_resource_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'resourceId' not in self.query._query_terms
        self.query.match_resource_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['resourceId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_resource_id_terms(self):
        """Tests clear_resource_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_resource_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'resourceId' in self.query._query_terms
        self.query.clear_resource_id_terms()
        if is_no_authz(self.service_config):
            assert 'resourceId' not in self.query._query_terms

    def test_supports_resource_query(self):
        """Tests supports_resource_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_resource_query()

    def test_get_resource_query(self):
        """Tests get_resource_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_resource_query()

    def test_clear_resource_terms(self):
        """Tests clear_resource_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['resource'] = 'foo'
        self.query.clear_resource_terms()
        if is_no_authz(self.service_config):
            assert 'resource' not in self.query._query_terms

    def test_match_objective_id(self):
        """Tests match_objective_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'objectiveId' not in self.query._query_terms
        self.query.match_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['objectiveId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_objective_id_terms(self):
        """Tests clear_objective_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'objectiveId' in self.query._query_terms
        self.query.clear_objective_id_terms()
        if is_no_authz(self.service_config):
            assert 'objectiveId' not in self.query._query_terms

    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_objective_query()

    def test_get_objective_query(self):
        """Tests get_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_query()

    def test_match_any_objective(self):
        """Tests match_any_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_objective(True)

    def test_clear_objective_terms(self):
        """Tests clear_objective_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objective'] = 'foo'
        self.query.clear_objective_terms()
        if is_no_authz(self.service_config):
            assert 'objective' not in self.query._query_terms

    def test_match_completion(self):
        """Tests match_completion"""
        if not is_never_authz(self.service_config):
            start = float(0.0)
            end = float(100.0)
            if is_no_authz(self.service_config):
                assert 'completion' not in self.query._query_terms
            self.query.match_completion(start, end, True)
            if is_no_authz(self.service_config):
                assert self.query._query_terms['completion'] == {
                    '$gte': start,
                    '$lte': end
                }

    def test_clear_completion_terms(self):
        """Tests clear_completion_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['completion'] = 'foo'
        self.query.clear_completion_terms()
        if is_no_authz(self.service_config):
            assert 'completion' not in self.query._query_terms

    def test_match_minimum_completion(self):
        """Tests match_minimum_completion"""
        if not is_never_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.query.match_minimum_completion(float(50.0), True)

    def test_clear_minimum_completion_terms(self):
        """Tests clear_minimum_completion_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_minimum_completion_terms()

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

    def test_match_objective_bank_id(self):
        """Tests match_objective_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_bank_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedObjectiveBankIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_objective_bank_id_terms(self):
        """Tests clear_objective_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_objective_bank_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedObjectiveBankIds' in self.query._query_terms
        self.query.clear_objective_bank_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedObjectiveBankIds' not in self.query._query_terms

    def test_supports_objective_bank_query(self):
        """Tests supports_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_objective_bank_query()

    def test_get_objective_bank_query(self):
        """Tests get_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_bank_query()

    def test_clear_objective_bank_terms(self):
        """Tests clear_objective_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objectiveBank'] = 'foo'
        self.query.clear_objective_bank_terms()
        if is_no_authz(self.service_config):
            assert 'objectiveBank' not in self.query._query_terms

    def test_get_proficiency_query_record(self):
        """Tests get_proficiency_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_proficiency_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        request.cls.fake_id = Id('objective.objective%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_query_test_fixture(request):
    # Since the session isn't implemented, we just construct an ObjectiveBankQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = ObjectiveBankQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("objective_bank_query_class_fixture", "objective_bank_query_test_fixture")
class TestObjectiveBankQuery(object):
    """Tests for ObjectiveBankQuery"""
    def test_match_objective_id(self):
        """Tests match_objective_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_objective_id(True, True)

    def test_clear_objective_id_terms(self):
        """Tests clear_objective_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objectiveId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_objective_id_terms()

        if is_no_authz(self.service_config):
            assert 'objectiveId' not in self.query._query_terms

    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_objective_query()

    def test_get_objective_query(self):
        """Tests get_objective_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_query()

    def test_match_any_objective(self):
        """Tests match_any_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_objective(True)

    def test_clear_objective_terms(self):
        """Tests clear_objective_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['objective'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_objective_terms()

        if is_no_authz(self.service_config):
            assert 'objective' not in self.query._query_terms

    def test_match_activity_id(self):
        """Tests match_activity_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_activity_id(True, True)

    def test_clear_activity_id_terms(self):
        """Tests clear_activity_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['activityId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_activity_id_terms()

        if is_no_authz(self.service_config):
            assert 'activityId' not in self.query._query_terms

    def test_supports_activity_query(self):
        """Tests supports_activity_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_activity_query()

    def test_get_activity_query(self):
        """Tests get_activity_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_activity_query()

    def test_match_any_activity(self):
        """Tests match_any_activity"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_activity(True)

    def test_clear_activity_terms(self):
        """Tests clear_activity_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['activity'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_activity_terms()

        if is_no_authz(self.service_config):
            assert 'activity' not in self.query._query_terms

    def test_match_ancestor_objective_bank_id(self):
        """Tests match_ancestor_objective_bank_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_objective_bank_id(True, True)

    def test_clear_ancestor_objective_bank_id_terms(self):
        """Tests clear_ancestor_objective_bank_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorObjectiveBankId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_objective_bank_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorObjectiveBankId' not in self.query._query_terms

    def test_supports_ancestor_objective_bank_query(self):
        """Tests supports_ancestor_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_objective_bank_query()

    def test_get_ancestor_objective_bank_query(self):
        """Tests get_ancestor_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_objective_bank_query()

    def test_match_any_ancestor_objective_bank(self):
        """Tests match_any_ancestor_objective_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_objective_bank(True)

    def test_clear_ancestor_objective_bank_terms(self):
        """Tests clear_ancestor_objective_bank_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorObjectiveBank'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_objective_bank_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorObjectiveBank' not in self.query._query_terms

    def test_match_descendant_objective_bank_id(self):
        """Tests match_descendant_objective_bank_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_objective_bank_id(True, True)

    def test_clear_descendant_objective_bank_id_terms(self):
        """Tests clear_descendant_objective_bank_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantObjectiveBankId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_objective_bank_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantObjectiveBankId' not in self.query._query_terms

    def test_supports_descendant_objective_bank_query(self):
        """Tests supports_descendant_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_objective_bank_query()

    def test_get_descendant_objective_bank_query(self):
        """Tests get_descendant_objective_bank_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_objective_bank_query()

    def test_match_any_descendant_objective_bank(self):
        """Tests match_any_descendant_objective_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_objective_bank(True)

    def test_clear_descendant_objective_bank_terms(self):
        """Tests clear_descendant_objective_bank_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantObjectiveBank'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_objective_bank_terms()

        if is_no_authz(self.service_config):
            assert 'descendantObjectiveBank' not in self.query._query_terms

    def test_get_objective_bank_query_record(self):
        """Tests get_objective_bank_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_objective_bank_query_record(True)
