"""Unit tests of assessment.authoring sessions."""


import pytest


from random import shuffle


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.assessment.objects import Bank as ABCBank
from dlkit.abstract_osid.assessment_authoring import objects as ABCObjects
from dlkit.abstract_osid.assessment_authoring import queries as ABCQueries
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.json_.id.objects import IdList
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
SIMPLE_SEQUENCE_RECORD_TYPE = Type(**{"authority": "ODL.MIT.EDU", "namespace": "osid-object", "identifier": "simple-child-sequencing"})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_part_lookup_session_test_fixture(request):
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartLookupSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                                 [])
            create_form.display_name = 'Test AssessmentPart ' + str(num)
            create_form.description = 'Test AssessmentPart for AssessmentPartLookupSession tests'
            if num > 1:
                create_form.sequestered = True
            obj = request.cls.catalog.create_assessment_part_for_assessment(create_form)
            request.cls.assessment_part_list.append(obj)
            request.cls.assessment_part_ids.append(obj.ident)

        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_part_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.use_unsequestered_assessment_part_view()
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_part_lookup_session_class_fixture", "assessment_part_lookup_session_test_fixture")
class TestAssessmentPartLookupSession(object):
    """Tests for AssessmentPartLookupSession"""
    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # this should not be here...
        pass

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bank(), ABCBank)

    def test_can_lookup_assessment_parts(self):
        """Tests can_lookup_assessment_parts"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_assessment_parts(), bool)

    def test_use_comparative_assessment_part_view(self):
        """Tests use_comparative_assessment_part_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_part_view()

    def test_use_plenary_assessment_part_view(self):
        """Tests use_plenary_assessment_part_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_part_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_use_active_assessment_part_view(self):
        """Tests use_active_assessment_part_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_active_composition_view_template
        # Ideally also verify the value is set...
        self.catalog.use_active_assessment_part_view()

    def test_use_any_status_assessment_part_view(self):
        """Tests use_any_status_assessment_part_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_any_status_composition_view_template
        # Ideally also verify the value is set...
        self.catalog.use_any_status_assessment_part_view()

    def test_use_sequestered_assessment_part_view(self):
        """Tests use_sequestered_assessment_part_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_sequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_sequestered_assessment_part_view()

    def test_use_unsequestered_assessment_part_view(self):
        """Tests use_unsequestered_assessment_part_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_unsequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_unsequestered_assessment_part_view()

    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_bank_view()
            obj = self.catalog.get_assessment_part(self.assessment_part_list[0].ident)
            assert obj.ident == self.assessment_part_list[0].ident
            self.catalog.use_federated_bank_view()
            obj = self.catalog.get_assessment_part(self.assessment_part_list[0].ident)
            assert obj.ident == self.assessment_part_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_assessment_part(self.fake_id)

    def test_get_assessment_parts_by_ids(self):
        """Tests get_assessment_parts_by_ids"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_ids(self.assessment_part_ids)
        assert isinstance(objects, AssessmentPartList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_ids(self.assessment_part_ids)
        assert isinstance(objects, AssessmentPartList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assessment_parts_by_genus_type(self):
        """Tests get_assessment_parts_by_genus_type"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, AssessmentPartList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, AssessmentPartList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assessment_parts_by_parent_genus_type(self):
        """Tests get_assessment_parts_by_parent_genus_type"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_assessment_parts_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssessmentPartList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_assessment_parts_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, AssessmentPartList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_assessment_parts_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assessment_parts_by_record_type(self):
        """Tests get_assessment_parts_by_record_type"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, AssessmentPartList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, AssessmentPartList)

    def test_get_assessment_parts_for_assessment(self):
        """Tests get_assessment_parts_for_assessment"""
        # Override this because we do have AssessmentPartQuerySession implemented,
        #   so with NEVER_AUTHZ it returns an empty result set
        results = self.session.get_assessment_parts_for_assessment(self.assessment.ident)
        assert isinstance(results, ABCObjects.AssessmentPartList)
        if not is_never_authz(self.service_config):
            assert results.available() == 2
        else:
            assert results.available() == 0

    def test_get_assessment_parts(self):
        """Tests get_assessment_parts"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts()
        assert isinstance(objects, AssessmentPartList)
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts()
        assert isinstance(objects, AssessmentPartList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assessment_part_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_assessment_part(self.assessment_part_ids[0], ALIAS_ID)
            obj = self.catalog.get_assessment_part(ALIAS_ID)
            assert obj.get_id() == self.assessment_part_ids[0]

    def test_get_assessment_id(self):
        """tests get_assessment_id"""
        if not is_never_authz(self.service_config):
            assert str(self.assessment_part_list[0].get_assessment_id()) == str(self.assessment.ident)

    def test_get_assessment(self):
        """tests get_assessment"""
        def check_equal(val1, val2):
            assert val1 == val2

        def check_dict_equal(dict1, dict2):
            for item in dict1.items():
                key = item[0]
                value = item[1]
                if isinstance(value, dict):
                    check_dict_equal(value, dict2[key])
                else:
                    check_equal(value, dict2[key])

        if not is_never_authz(self.service_config):
            check_dict_equal(self.assessment_part_list[0].get_assessment().object_map,
                             self.assessment.object_map)


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def assessment_part_query_session_test_fixture(request):
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartQuerySession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

        colors = ['Orange', 'Blue', 'Green', 'orange']

        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                                 [])
            create_form.display_name = 'Test AssessmentPart ' + str(num) + colors[num]
            create_form.description = 'Test AssessmentPart for AssessmentPartQuerySession tests'
            obj = request.cls.catalog.create_assessment_part_for_assessment(create_form)
            request.cls.assessment_part_list.append(obj)
            request.cls.assessment_part_ids.append(obj.ident)

        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_part_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.use_unsequestered_assessment_part_view()
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_part_query_session_class_fixture", "assessment_part_query_session_test_fixture")
class TestAssessmentPartQuerySession(object):
    """Tests for AssessmentPartQuerySession"""
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

    def test_can_search_assessment_parts(self):
        """Tests can_search_assessment_parts"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_assessment_parts(), bool)

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_use_sequestered_assessment_part_view(self):
        """Tests use_sequestered_assessment_part_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_sequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_sequestered_assessment_part_view()

    def test_use_unsequestered_assessment_part_view(self):
        """Tests use_unsequestered_assessment_part_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_unsequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_unsequestered_assessment_part_view()

    def test_get_assessment_part_query(self):
        """Tests get_assessment_part_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_part_query()
        assert isinstance(query, ABCQueries.AssessmentPartQuery)

    def test_get_assessment_parts_by_query(self):
        """Tests get_assessment_parts_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_assessment_part_query()
            query.match_display_name('orange')
            assert self.catalog.get_assessment_parts_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_assessment_parts_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_parts_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartAdminSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_part_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_admin_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident,
                                                                                                  [SIMPLE_SEQUENCE_RECORD_TYPE])
        request.cls.form.display_name = 'new AssessmentPart'
        request.cls.form.description = 'description of AssessmentPart'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_assessment_part_for_assessment(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.osid_object = request.cls.catalog.get_assessment_part(request.cls.osid_object.ident)
            if request.cls.osid_object.has_children():
                for child_id in request.cls.osid_object.get_child_assessment_part_ids():
                    request.cls.catalog.delete_assessment_part(child_id)
            request.cls.catalog.delete_assessment_part(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_part_admin_session_class_fixture", "assessment_part_admin_session_test_fixture")
class TestAssessmentPartAdminSession(object):
    """Tests for AssessmentPartAdminSession"""
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

    def test_can_create_assessment_parts(self):
        """Tests can_create_assessment_parts"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_assessment_parts(), bool)

    def test_can_create_assessment_part_with_record_types(self):
        """Tests can_create_assessment_part_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_assessment_part_with_record_types(DEFAULT_TYPE), bool)

    def test_get_assessment_part_form_for_create_for_assessment(self):
        """Tests get_assessment_part_form_for_create_for_assessment"""
        if not is_never_authz(self.service_config):
            form = self.session.get_assessment_part_form_for_create_for_assessment(self.assessment.ident, [])
            assert isinstance(form, ABCObjects.AssessmentPartForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_part_form_for_create_for_assessment(self.fake_id, [])

    def test_create_assessment_part_for_assessment(self):
        """Tests create_assessment_part_for_assessment"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, AssessmentPart)
            assert self.osid_object.display_name.text == 'new AssessmentPart'
            assert self.osid_object.description.text == 'description of AssessmentPart'
            assert self.osid_object.genus_type == NEW_TYPE

            form = self.catalog.get_assessment_part_form_for_create_for_assessment_part(self.osid_object.ident, [])
            form.display_name = 'new AssessmentPart child'
            form.description = 'description of AssessmentPart child'
            child_part = self.catalog.create_assessment_part_for_assessment_part(form)

            parent_part = self.catalog.get_assessment_part(self.osid_object.ident)
            assert parent_part.has_children()
            assert parent_part.get_child_assessment_part_ids().available() == 1
            assert str(parent_part.get_child_assessment_part_ids().next()) == str(child_part.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_assessment_part_for_assessment_part('foo')

    def test_get_assessment_part_form_for_create_for_assessment_part(self):
        """Tests get_assessment_part_form_for_create_for_assessment_part"""
        if not is_never_authz(self.service_config):
            form = self.session.get_assessment_part_form_for_create_for_assessment_part(self.osid_object.ident, [])
            assert isinstance(form, ABCObjects.AssessmentPartForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_part_form_for_create_for_assessment_part(self.fake_id, [])

    def test_create_assessment_part_for_assessment_part(self):
        """Tests create_assessment_part_for_assessment_part"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, AssessmentPart)
            assert self.osid_object.display_name.text == 'new AssessmentPart'
            assert self.osid_object.description.text == 'description of AssessmentPart'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_assessment_part_for_assessment_part(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment_part_for_assessment_part('I Will Break You!')
            update_form = self.catalog.get_assessment_part_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_assessment_part_for_assessment_part(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_assessment_part_for_assessment_part('foo')

    def test_can_update_assessment_parts(self):
        """Tests can_update_assessment_parts"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_assessment_parts(), bool)

    def test_get_assessment_part_form_for_update(self):
        """Tests get_assessment_part_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_part_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_part_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_assessment_part_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='assessment.authoring.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_part_form_for_update(self.fake_id)

    def test_update_assessment_part(self):
        """Tests update_assessment_part"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_assessment_part_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_assessment_part(self.osid_object.ident, form)
            assert isinstance(updated_object, ABCObjects.AssessmentPart)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.update_assessment_part(self.fake_id, 'foo')

    def test_can_delete_assessment_parts(self):
        """Tests can_delete_assessment_parts"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_assessment_parts(), bool)

    def test_delete_assessment_part(self):
        """Tests delete_assessment_part"""
        if not is_never_authz(self.service_config):
            results = self.catalog.get_assessment_parts()
            assert results.available() == 1

            form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                                   [])
            form.display_name = 'new AssessmentPart'
            form.description = 'description of AssessmentPart'
            new_assessment_part = self.catalog.create_assessment_part_for_assessment(form)

            results = self.catalog.get_assessment_parts()
            assert results.available() == 2

            self.session.delete_assessment_part(new_assessment_part.ident)

            results = self.catalog.get_assessment_parts()
            assert results.available() == 1
            assert str(results.next().ident) != str(new_assessment_part.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_assessment_part(self.fake_id)

    def test_can_manage_assessment_part_aliases(self):
        """Tests can_manage_assessment_part_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_assessment_part_aliases(), bool)

    def test_alias_assessment_part(self):
        """Tests alias_assessment_part"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_assessment_part(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_assessment_part(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_assessment_part(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_bank_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentPartBankSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartBankSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentPart ' + str(num)
            create_form.description = 'Test AssessmentPart for AssessmentPartBankSession tests'
            obj = request.cls.catalog.create_assessment_part_for_assessment(create_form)
            request.cls.assessment_part_list.append(obj)
            request.cls.assessment_part_ids.append(obj.ident)
        request.cls.svc_mgr.assign_assessment_part_to_bank(
            request.cls.assessment_part_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_assessment_part_to_bank(
            request.cls.assessment_part_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_assessment_part_from_bank(
                request.cls.assessment_part_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_assessment_part_from_bank(
                request.cls.assessment_part_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_bank_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_part_bank_session_class_fixture", "assessment_part_bank_session_test_fixture")
class TestAssessmentPartBankSession(object):
    """Tests for AssessmentPartBankSession"""
    def test_can_lookup_assessment_part_bank_mappings(self):
        """Tests can_lookup_assessment_part_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_part_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_assessment_part_bank_view(self):
        """Tests use_comparative_assessment_part_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_assessment_part_bank_view()

    def test_use_plenary_assessment_part_bank_view(self):
        """Tests use_plenary_assessment_part_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_assessment_part_bank_view()

    def test_get_assessment_part_ids_by_bank(self):
        """Tests get_assessment_part_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_assessment_part_ids_by_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_assessment_part_ids_by_bank(self.fake_id)

    def test_get_assessment_parts_by_bank(self):
        """Tests get_assessment_parts_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_assessment_parts_by_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AssessmentPartList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_parts_by_bank(self.fake_id)

    def test_get_assessment_part_ids_by_banks(self):
        """Tests get_assessment_part_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_assessment_part_ids_by_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_part_ids_by_banks([self.fake_id])

    def test_get_assessment_parts_by_banks(self):
        """Tests get_assessment_parts_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_assessment_parts_by_banks(catalog_ids)
            assert isinstance(results, ABCObjects.AssessmentPartList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assessment_parts_by_banks([self.fake_id])

    def test_get_bank_ids_by_assessment_part(self):
        """Tests get_bank_ids_by_assessment_part"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bank_ids_by_assessment_part(self.assessment_part_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bank_ids_by_assessment_part(self.fake_id)

    def test_get_banks_by_assessment_part(self):
        """Tests get_banks_by_assessment_part"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_banks_by_assessment_part(self.assessment_part_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_banks_by_assessment_part(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_bank_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.assessment_part_list = list()
    request.cls.assessment_part_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentPartBankAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bank(create_form)

        assessment_form = request.cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartBankAssignmentSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(assessment_form)

        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentPart ' + str(num)
            create_form.description = 'Test AssessmentPart for AssessmentPartBankAssignmentSession tests'
            obj = request.cls.catalog.create_assessment_part_for_assessment(create_form)
            request.cls.assessment_part_list.append(obj)
            request.cls.assessment_part_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            request.cls.catalog.delete_assessment(request.cls.assessment.ident)
            request.cls.svc_mgr.delete_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_bank_assignment_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("assessment_part_bank_assignment_session_class_fixture", "assessment_part_bank_assignment_session_test_fixture")
class TestAssessmentPartBankAssignmentSession(object):
    """Tests for AssessmentPartBankAssignmentSession"""
    def test_can_assign_assessment_parts(self):
        """Tests can_assign_assessment_parts"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessment_parts()
        assert isinstance(result, bool)

    def test_can_assign_assessment_parts_to_bank(self):
        """Tests can_assign_assessment_parts_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessment_parts_to_bank(self.assigned_catalog.ident)
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

    def test_get_assignable_bank_ids_for_assessment_part(self):
        """Tests get_assignable_bank_ids_for_assessment_part"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bank_ids_for_assessment_part(self.catalog.ident, self.assessment_part_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bank_ids_for_assessment_part(self.fake_id, self.fake_id)

    def test_assign_assessment_part_to_bank(self):
        """Tests assign_assessment_part_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessment_parts()
            assert results.available() == 0
            self.session.assign_assessment_part_to_bank(self.assessment_part_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessment_parts()
            assert results.available() == 1
            self.session.unassign_assessment_part_from_bank(
                self.assessment_part_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_assessment_part_to_bank(self.fake_id, self.fake_id)

    def test_unassign_assessment_part_from_bank(self):
        """Tests unassign_assessment_part_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assessment_parts()
            assert results.available() == 0
            self.session.assign_assessment_part_to_bank(
                self.assessment_part_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessment_parts()
            assert results.available() == 1
            self.session.unassign_assessment_part_from_bank(
                self.assessment_part_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assessment_parts()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_assessment_part_from_bank(self.fake_id, self.fake_id)

    def test_reassign_assessment_part_to_bank(self):
        """Tests reassign_assessment_part_to_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_assessment_part_to_bank(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_item_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT_AUTHORING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def assessment_part_item_session_test_fixture(request):
    request.cls.item_list = list()
    request.cls.item_ids = list()
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartItemSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentPartItemSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part'
        create_form.description = 'Test Assessment Part for AssessmentPartItemSession tests'
        request.cls.assessment_part = request.cls.catalog.create_assessment_part_for_assessment(create_form)
        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for AssessmentPartItemSession tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)
            request.cls.catalog.add_item(obj.ident, request.cls.assessment_part.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_part_item_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                for obj in catalog.get_assessment_parts():
                    if obj.has_children():
                        for child_id in obj.get_child_assessment_part_ids():
                            catalog.delete_assessment_part(child_id)
                    catalog.delete_assessment_part(obj.ident)
                for obj in catalog.get_assessments():
                    catalog.delete_assessment(obj.ident)
                for obj in catalog.get_items():
                    catalog.delete_item(obj.ident)
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("assessment_part_item_session_class_fixture", "assessment_part_item_session_test_fixture")
class TestAssessmentPartItemSession(object):
    """Tests for AssessmentPartItemSession"""
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

    def test_can_access_assessment_part_items(self):
        """Tests can_access_assessment_part_items"""
        assert isinstance(self.session.can_access_assessment_part_items(), bool)

    def test_use_comparative_asseessment_part_item_view(self):
        """Tests use_comparative_asseessment_part_item_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_asseessment_part_item_view()

    def test_use_plenary_assessment_part_item_view(self):
        """Tests use_plenary_assessment_part_item_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_part_item_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_part_items(self):
        """Tests get_assessment_part_items"""
        # From test_templates/repository.py::AssetCompositionSession::get_composition_assets_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_assessment_part_items(self.assessment_part.ident).available() == 4
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_part_items(self.fake_id)

    def test_get_assessment_parts_by_item(self):
        """Tests get_assessment_parts_by_item"""
        # From test_templates/repository.py::AssetCompositionSession::get_compositions_by_asset_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_assessment_parts_by_item(self.item_ids[0]).available() == 1
            assert self.catalog.get_assessment_parts_by_item(self.item_ids[0]).next().ident == self.assessment_part.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_assessment_parts_by_item(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_part_item_design_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.item_list = list()
    request.cls.item_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT_AUTHORING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartItemDesignSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)
        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentPartItemDesignSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part'
        create_form.description = 'Test Assessment Part for AssessmentPartItemDesignSession tests'
        request.cls.assessment_part = request.cls.catalog.create_assessment_part_for_assessment(create_form)
        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for AssessmentPartItemDesignSession tests'
            obj = request.cls.catalog.create_item(create_form)
            request.cls.item_list.append(obj)
            request.cls.item_ids.append(obj.ident)
            request.cls.catalog.add_item(obj.ident, request.cls.assessment_part.ident)

        request.cls.assessment = request.cls.catalog.get_assessment(request.cls.assessment.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_assessment_part_item_design_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                for obj in catalog.get_assessment_parts():
                    catalog.delete_assessment_part(obj.ident)
                for obj in catalog.get_assessments():
                    catalog.delete_assessment(obj.ident)
                for obj in catalog.get_items():
                    catalog.delete_item(obj.ident)
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_part_item_design_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("assessment_part_item_design_session_class_fixture", "assessment_part_item_design_session_test_fixture")
class TestAssessmentPartItemDesignSession(object):
    """Tests for AssessmentPartItemDesignSession"""
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

    def test_can_design_assessment_parts(self):
        """Tests can_design_assessment_parts"""
        assert isinstance(self.session.can_design_assessment_parts(), bool)

    def test_add_item(self):
        """Tests add_item"""
        if not is_never_authz(self.service_config):
            assert self.catalog.get_assessment_part_items(self.assessment_part.ident).available() == 4

            create_form = self.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item 5'
            create_form.description = 'Test Item for AssessmentPartItemDesignSession tests'
            obj = self.catalog.create_item(create_form)
            self.session.add_item(obj.ident, self.assessment_part.ident)

            assert self.catalog.get_assessment_part_items(self.assessment_part.ident).available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.add_item(self.fake_id, self.fake_id)

    def test_move_item_ahead(self):
        """Tests move_item_ahead"""
        if not is_never_authz(self.service_config):
            original_item_order = list(self.catalog.get_assessment_part_items(self.assessment_part.ident))
            original_ids = [item.ident for item in original_item_order]
            self.session.move_item_ahead(original_ids[-1],
                                         self.assessment_part.ident,
                                         original_ids[0])
            expected_order = [original_ids[-1]] + original_ids[0:-1]
            new_order = [item.ident for item in self.catalog.get_assessment_part_items(self.assessment_part.ident)]
            assert new_order == expected_order
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.move_item_ahead(self.fake_id, self.fake_id, self.fake_id)

    def test_move_item_behind(self):
        """Tests move_item_behind"""
        if not is_never_authz(self.service_config):
            original_item_order = list(self.catalog.get_assessment_part_items(self.assessment_part.ident))
            original_ids = [item.ident for item in original_item_order]
            self.session.move_item_behind(original_ids[0],
                                          self.assessment_part.ident,
                                          original_ids[-1])
            expected_order = original_ids[1::] + [original_ids[0]]
            new_order = [item.ident for item in self.catalog.get_assessment_part_items(self.assessment_part.ident)]
            assert new_order == expected_order
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.move_item_behind(self.fake_id, self.fake_id, self.fake_id)

    def test_order_items(self):
        """Tests order_items"""
        if not is_never_authz(self.service_config):
            original_item_order = list(self.catalog.get_assessment_part_items(self.assessment_part.ident))
            original_ids = [item.ident for item in original_item_order]
            shuffle(original_ids)
            self.session.order_items(original_ids,
                                     self.assessment_part.ident)
            new_order = [item.ident for item in self.catalog.get_assessment_part_items(self.assessment_part.ident)]
            assert new_order == original_ids
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.order_items(self.fake_id, self.fake_id)

    def test_remove_item(self):
        """Tests remove_item"""
        if not is_never_authz(self.service_config):
            original_item_order = list(self.catalog.get_assessment_part_items(self.assessment_part.ident))
            original_ids = [item.ident for item in original_item_order]
            self.session.remove_item(original_ids[0],
                                     self.assessment_part.ident)
            new_order = [item.ident for item in self.catalog.get_assessment_part_items(self.assessment_part.ident)]
            assert new_order == original_ids[1::]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_item(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.sequence_rule_list = list()
    request.cls.sequence_rule_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.catalog.get_assessment_form_for_create([SIMPLE_SEQUENCE_RECORD_TYPE])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleLookupSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleLookupSession tests'
        request.cls.assessment_part_1 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleLookupSession tests'
        assessment_part_2 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        for num in [0, 1]:
            create_form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                                assessment_part_2.ident,
                                                                                [])
            create_form.display_name = 'Test Sequence Rule ' + str(num)
            create_form.description = 'Test Sequence Rule for SequenceRuleLookupSession tests'
            obj = request.cls.catalog.create_sequence_rule(create_form)
            request.cls.sequence_rule_list.append(obj)
            request.cls.sequence_rule_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_sequence_rule_lookup_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_banks():
                for obj in catalog.get_sequence_rules():
                    catalog.delete_sequence_rule(obj.ident)
                for obj in catalog.get_assessment_parts():
                    catalog.delete_assessment_part(obj.ident)
                for obj in catalog.get_assessments():
                    catalog.delete_assessment(obj.ident)
                request.cls.svc_mgr.delete_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def sequence_rule_lookup_session_test_fixture(request):
    request.cls.session = request.cls.catalog
    request.cls.assessment_part = request.cls.assessment_part_1


@pytest.mark.usefixtures("sequence_rule_lookup_session_class_fixture", "sequence_rule_lookup_session_test_fixture")
class TestSequenceRuleLookupSession(object):
    """Tests for SequenceRuleLookupSession"""
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

    def test_can_lookup_sequence_rules(self):
        """Tests can_lookup_sequence_rules"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_sequence_rules(), bool)

    def test_use_comparative_sequence_rule_view(self):
        """Tests use_comparative_sequence_rule_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_sequence_rule_view()

    def test_use_plenary_sequence_rule_view(self):
        """Tests use_plenary_sequence_rule_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_sequence_rule_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_use_active_sequence_rule_view(self):
        """Tests use_active_sequence_rule_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_active_composition_view_template
        # Ideally also verify the value is set...
        self.catalog.use_active_sequence_rule_view()

    def test_use_any_status_sequence_rule_view(self):
        """Tests use_any_status_sequence_rule_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_any_status_composition_view_template
        # Ideally also verify the value is set...
        self.catalog.use_any_status_sequence_rule_view()

    def test_get_sequence_rule(self):
        """Tests get_sequence_rule"""
        # Override this because we haven't implemented SequenceRuleQuerySession, so will
        #   throw PermissionDenied with NEVER_AUTHZ
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_bank_view()
            obj = self.catalog.get_sequence_rule(self.sequence_rule_list[0].ident)
            assert obj.ident == self.sequence_rule_list[0].ident
            self.catalog.use_federated_bank_view()
            obj = self.catalog.get_sequence_rule(self.sequence_rule_list[0].ident)
            assert obj.ident == self.sequence_rule_list[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rule(self.fake_id)

    def test_get_sequence_rules_by_ids(self):
        """Tests get_sequence_rules_by_ids"""
        # Override this because we haven't implemented SequenceRuleQuerySession, so will
        #   throw PermissionDenied with NEVER_AUTHZ
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_sequence_rules_by_ids(self.sequence_rule_ids)
            assert isinstance(objects, SequenceRuleList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_sequence_rules_by_ids(self.sequence_rule_ids)
            assert isinstance(objects, SequenceRuleList)
            assert objects.available() > 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rules_by_ids(self.sequence_rule_ids)

    def test_get_sequence_rules_by_genus_type(self):
        """Tests get_sequence_rules_by_genus_type"""
        # Override this because we haven't implemented SequenceRuleQuerySession, so will
        #   throw PermissionDenied with NEVER_AUTHZ
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_sequence_rules_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, SequenceRuleList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_sequence_rules_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, SequenceRuleList)
            assert objects.available() > 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rules_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_sequence_rules_by_parent_genus_type(self):
        """Tests get_sequence_rules_by_parent_genus_type"""
        # Override this because we haven't implemented SequenceRuleQuerySession, so will
        #   throw PermissionDenied with NEVER_AUTHZ
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_sequence_rules_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, SequenceRuleList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_sequence_rules_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, SequenceRuleList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rules_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_sequence_rules_by_record_type(self):
        """Tests get_sequence_rules_by_record_type"""
        # Override this because we haven't implemented SequenceRuleQuerySession, so will
        #   throw PermissionDenied with NEVER_AUTHZ
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_sequence_rules_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, SequenceRuleList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_sequence_rules_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, SequenceRuleList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rules_by_record_type(DEFAULT_TYPE)

    def test_get_sequence_rules_for_assessment_part(self):
        """Tests get_sequence_rules_for_assessment_part"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        if self.svc_mgr.supports_sequence_rule_query():
            results = self.session.get_sequence_rules_for_assessment_part(self.assessment_part.ident)
            assert isinstance(results, ABCObjects.SequenceRuleList)
            if not is_never_authz(self.service_config):
                assert results.available() == 2
            else:
                assert results.available() == 0
        else:
            if not is_never_authz(self.service_config):
                results = self.session.get_sequence_rules_for_assessment_part(self.assessment_part.ident)
                assert results.available() == 2
                assert isinstance(results, ABCObjects.SequenceRuleList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.session.get_sequence_rules_for_assessment_part(self.fake_id)

    def test_get_sequence_rules_for_next_assessment_part(self):
        """Tests get_sequence_rules_for_next_assessment_part"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_sequence_rules_for_next_assessment_part(True)

    def test_get_sequence_rules_for_assessment_parts(self):
        """Tests get_sequence_rules_for_assessment_parts"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_sequence_rules_for_assessment_parts(True, True)

    def test_get_sequence_rules_for_assessment(self):
        """Tests get_sequence_rules_for_assessment"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        if self.svc_mgr.supports_sequence_rule_query():
            results = self.session.get_sequence_rules_for_assessment(self.assessment.ident)
            assert isinstance(results, ABCObjects.SequenceRuleList)
            if not is_never_authz(self.service_config):
                assert results.available() == 2
            else:
                assert results.available() == 0
        else:
            if not is_never_authz(self.service_config):
                results = self.session.get_sequence_rules_for_assessment(self.assessment.ident)
                assert results.available() == 2
                assert isinstance(results, ABCObjects.SequenceRuleList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.session.get_sequence_rules_for_assessment(self.fake_id)

    def test_get_sequence_rules(self):
        """Tests get_sequence_rules"""
        # Override this because we haven't implemented SequenceRuleQuerySession, so will
        #   throw PermissionDenied with NEVER_AUTHZ
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_sequence_rules()
            assert isinstance(objects, SequenceRuleList)
            self.catalog.use_federated_bank_view()
            objects = self.catalog.get_sequence_rules()
            assert isinstance(objects, SequenceRuleList)
            assert objects.available() > 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rules()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.sequence_rule_list = list()
    request.cls.sequence_rule_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

        create_form = request.cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleAdminSession tests'
        request.cls.assessment = request.cls.catalog.create_assessment(create_form)
        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleAdminSession tests'
        request.cls.assessment_part_1 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = request.cls.catalog.get_assessment_part_form_for_create_for_assessment(request.cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleAdminSession tests'
        request.cls.assessment_part_2 = request.cls.catalog.create_assessment_part_for_assessment(create_form)

        for num in [0, 1]:
            create_form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                                request.cls.assessment_part_2.ident,
                                                                                [])
            create_form.display_name = 'Test Sequence Rule ' + str(num)
            create_form.description = 'Test Sequence Rule for SequenceRuleAdminSession tests'
            obj = request.cls.catalog.create_sequence_rule(create_form)
            request.cls.sequence_rule_list.append(obj)
            request.cls.sequence_rule_ids.append(obj.ident)

        request.cls.form = request.cls.catalog.get_sequence_rule_form_for_create(request.cls.assessment_part_1.ident,
                                                                                 request.cls.assessment_part_2.ident,
                                                                                 [])
        request.cls.form.display_name = 'new SequenceRule'
        request.cls.form.description = 'description of SequenceRule'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_sequence_rule(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_sequence_rule_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_sequence_rules():
                request.cls.catalog.delete_sequence_rule(obj.ident)
            for obj in request.cls.catalog.get_assessment_parts():
                request.cls.catalog.delete_assessment_part(obj.ident)
            for obj in request.cls.catalog.get_assessments():
                request.cls.catalog.delete_assessment(obj.ident)
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def sequence_rule_admin_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("sequence_rule_admin_session_class_fixture", "sequence_rule_admin_session_test_fixture")
class TestSequenceRuleAdminSession(object):
    """Tests for SequenceRuleAdminSession"""
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

    def test_can_create_sequence_rule(self):
        """Tests can_create_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_sequence_rule(), bool)

    def test_can_create_sequence_rule_with_record_types(self):
        """Tests can_create_sequence_rule_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_sequence_rule_with_record_types(DEFAULT_TYPE), bool)

    def test_get_sequence_rule_form_for_create(self):
        """Tests get_sequence_rule_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                  self.assessment_part_2.ident,
                                                                  [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rule_form_for_create(self.fake_id, self.fake_id, [])

    def test_create_sequence_rule(self):
        """Tests create_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRule
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, SequenceRule)
            assert self.osid_object.display_name.text == 'new SequenceRule'
            assert self.osid_object.description.text == 'description of SequenceRule'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_sequence_rule(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_sequence_rule('I Will Break You!')
            update_form = self.catalog.get_sequence_rule_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_sequence_rule(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_sequence_rule('foo')

    def test_can_update_sequence_rules(self):
        """Tests can_update_sequence_rules"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_sequence_rules(), bool)

    def test_get_sequence_rule_form_for_update(self):
        """Tests get_sequence_rule_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_sequence_rule_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_sequence_rule_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_sequence_rule_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='assessment.authoring.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_sequence_rule_form_for_update(self.fake_id)

    def test_update_sequence_rule(self):
        """Tests update_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.assessment_authoring.objects import SequenceRule
            form = self.catalog.get_sequence_rule_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_sequence_rule(form)
            assert isinstance(updated_object, SequenceRule)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_sequence_rule(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_sequence_rule('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_sequence_rule(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_sequence_rule('foo')

    def test_can_delete_sequence_rules(self):
        """Tests can_delete_sequence_rules"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_sequence_rules(), bool)

    def test_delete_sequence_rule(self):
        """Tests delete_sequence_rule"""
        if not is_never_authz(self.service_config):
            create_form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                         self.assessment_part_2.ident,
                                                                         [])
            create_form.display_name = 'new SequenceRule'
            create_form.description = 'description of SequenceRule'
            create_form.genus_type = NEW_TYPE
            osid_object = self.catalog.create_sequence_rule(create_form)
            self.catalog.delete_sequence_rule(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_sequence_rule(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_sequence_rule(self.fake_id)

    def test_can_manage_sequence_rule_aliases(self):
        """Tests can_manage_sequence_rule_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_sequence_rule_aliases(), bool)

    def test_alias_sequence_rule(self):
        """Tests alias_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_sequence_rule(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_sequence_rule(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_sequence_rule(self.fake_id, self.fake_id)

    def test_can_sequence_sequence_rules(self):
        """Tests can_sequence_sequence_rules"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_sequence_sequence_rules()

    def test_move_sequence_rule_ahead(self):
        """Tests move_sequence_rule_ahead"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.move_sequence_rule_ahead(True, True, True)

    def test_move_sequence_rule_behind(self):
        """Tests move_sequence_rule_behind"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.move_sequence_rule_behind(True, True, True)

    def test_order_sequence_rules(self):
        """Tests order_sequence_rules"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.order_sequence_rules(True, True)
