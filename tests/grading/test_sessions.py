"""Unit tests of grading sessions."""


import datetime
import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.grading import objects as ABCObjects
from dlkit.abstract_osid.grading import queries as ABCQueries
from dlkit.abstract_osid.grading.objects import Grade
from dlkit.abstract_osid.grading.objects import Gradebook as ABCGradebook
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.json_.grading.objects import GradebookColumnSummary
from dlkit.json_.id.objects import IdList
from dlkit.primordium.calendaring.primitives import DateTime
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
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def grade_system_lookup_session_test_fixture(request):
    request.cls.grade_system_list = list()
    request.cls.grade_system_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + str(num)
            create_form.description = 'Test GradeSystem for GradeSystemLookupSession tests'
            obj = request.cls.catalog.create_grade_system(create_form)
            request.cls.grade_system_list.append(obj)
            request.cls.grade_system_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_grade_system_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_system_lookup_session_class_fixture", "grade_system_lookup_session_test_fixture")
class TestGradeSystemLookupSession(object):
    """Tests for GradeSystemLookupSession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_lookup_grade_systems(self):
        """Tests can_lookup_grade_systems"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_grade_systems(), bool)

    def test_use_comparative_grade_system_view(self):
        """Tests use_comparative_grade_system_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_grade_system_view()

    def test_use_plenary_grade_system_view(self):
        """Tests use_plenary_grade_system_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_grade_system_view()

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_gradebook_view()
            obj = self.catalog.get_grade_system(self.grade_system_list[0].ident)
            assert obj.ident == self.grade_system_list[0].ident
            self.catalog.use_federated_gradebook_view()
            obj = self.catalog.get_grade_system(self.grade_system_list[0].ident)
            assert obj.ident == self.grade_system_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_grade_system(self.fake_id)

    def test_get_grade_system_by_grade(self):
        """Tests get_grade_system_by_grade"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_system_by_grade(True)

    def test_get_grade_systems_by_ids(self):
        """Tests get_grade_systems_by_ids"""
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_ids(self.grade_system_ids)
        assert isinstance(objects, GradeSystemList)
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_ids(self.grade_system_ids)
        assert isinstance(objects, GradeSystemList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_grade_systems_by_genus_type(self):
        """Tests get_grade_systems_by_genus_type"""
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, GradeSystemList)
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, GradeSystemList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_grade_systems_by_parent_genus_type(self):
        """Tests get_grade_systems_by_parent_genus_type"""
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_grade_systems_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, GradeSystemList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_grade_systems_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, GradeSystemList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_grade_systems_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_grade_systems_by_record_type(self):
        """Tests get_grade_systems_by_record_type"""
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, GradeSystemList)
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, GradeSystemList)

    def test_get_grade_systems(self):
        """Tests get_grade_systems"""
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems()
        assert isinstance(objects, GradeSystemList)
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems()
        assert isinstance(objects, GradeSystemList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_grade_system_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_grade_system(self.grade_system_ids[0], ALIAS_ID)
            obj = self.catalog.get_grade_system(ALIAS_ID)
            assert obj.get_id() == self.grade_system_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def grade_system_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.grade_system_list = list()
    request.cls.grade_system_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + color
            create_form.description = (
                'Test GradeSystem for GradeSystemQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_grade_system(create_form)
            request.cls.grade_system_list.append(obj)
            request.cls.grade_system_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_grade_system_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_system_query_session_class_fixture", "grade_system_query_session_test_fixture")
class TestGradeSystemQuerySession(object):
    """Tests for GradeSystemQuerySession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_search_grade_systems(self):
        """Tests can_search_grade_systems"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_grade_systems(), bool)

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_grade_system_query()
        assert isinstance(query, ABCQueries.GradeSystemQuery)

    def test_get_grade_systems_by_query(self):
        """Tests get_grade_systems_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_grade_system_query()
            query.match_display_name('orange')
            assert self.catalog.get_grade_systems_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_grade_systems_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_systems_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_grade_system_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_grade_system_form_for_create([])
        request.cls.form.display_name = 'new GradeSystem'
        request.cls.form.description = 'description of GradeSystem'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_grade_system(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_grade_system(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_system_admin_session_class_fixture", "grade_system_admin_session_test_fixture")
class TestGradeSystemAdminSession(object):
    """Tests for GradeSystemAdminSession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_create_grade_systems(self):
        """Tests can_create_grade_systems"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_grade_systems(), bool)

    def test_can_create_grade_system_with_record_types(self):
        """Tests can_create_grade_system_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_grade_system_with_record_types(DEFAULT_TYPE), bool)

    def test_get_grade_system_form_for_create(self):
        """Tests get_grade_system_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_grade_system_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_grade_system_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_grade_system_form_for_create([])

    def test_create_grade_system(self):
        """Tests create_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.grading.objects import GradeSystem
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, GradeSystem)
            assert self.osid_object.display_name.text == 'new GradeSystem'
            assert self.osid_object.description.text == 'description of GradeSystem'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_grade_system(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_grade_system('I Will Break You!')
            update_form = self.catalog.get_grade_system_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_grade_system(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_grade_system('foo')

    def test_can_update_grade_systems(self):
        """Tests can_update_grade_systems"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_grade_systems(), bool)

    def test_get_grade_system_form_for_update(self):
        """Tests get_grade_system_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_grade_system_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_grade_system_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_grade_system_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='grading.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_grade_system_form_for_update(self.fake_id)

    def test_update_grade_system(self):
        """Tests update_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.grading.objects import GradeSystem
            form = self.catalog.get_grade_system_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_grade_system(form)
            assert isinstance(updated_object, GradeSystem)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_grade_system(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_grade_system('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_grade_system(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_grade_system('foo')

    def test_can_delete_grade_systems(self):
        """Tests can_delete_grade_systems"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_grade_systems(), bool)

    def test_delete_grade_system(self):
        """Tests delete_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_grade_system_form_for_create([])
            form.display_name = 'new GradeSystem'
            form.description = 'description of GradeSystem'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_grade_system(form)
            self.catalog.delete_grade_system(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_grade_system(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_grade_system(self.fake_id)

    def test_can_manage_grade_system_aliases(self):
        """Tests can_manage_grade_system_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_grade_system_aliases(), bool)

    def test_alias_grade_system(self):
        """Tests alias_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_grade_system(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_grade_system(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_grade_system(self.fake_id, self.fake_id)

    def test_can_create_grades(self):
        """Tests can_create_grades"""
        assert isinstance(self.session.can_create_grades(self.osid_object.ident),
                          bool)

    def test_can_create_grade_with_record_types(self):
        """Tests can_create_grade_with_record_types"""
        assert isinstance(self.session.can_create_grade_with_record_types(self.osid_object.ident,
                                                                          DEFAULT_TYPE),
                          bool)

    def test_get_grade_form_for_create(self):
        """Tests get_grade_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.session.get_grade_form_for_create(
                self.osid_object.ident,
                [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_form_for_create(self.fake_id, [])

    def test_create_grade(self):
        """Tests create_grade"""
        if not is_never_authz(self.service_config):
            assert self.osid_object.get_grades().available() == 0
            form = self.session.get_grade_form_for_create(
                self.osid_object.ident,
                [])
            form.display_name = 'Test object'
            grade = self.session.create_grade(form)
            assert isinstance(grade, Grade)
            assert grade.display_name.text == 'Test object'

            updated_grade_system = self.catalog.get_grade_system(self.osid_object.ident)
            assert updated_grade_system.get_grades().available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.create_grade('foo')

    def test_can_update_grades(self):
        """Tests can_update_grades"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_update_grades(True)

    def test_get_grade_form_for_update(self):
        """Tests get_grade_form_for_update"""
        if not is_never_authz(self.service_config):
            form = self.session.get_grade_form_for_create(
                self.osid_object.ident,
                [])
            grade = self.session.create_grade(form)
            form = self.session.get_grade_form_for_update(grade.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_form_for_update(self.fake_id)

    def test_update_grade(self):
        """Tests update_grade"""
        if not is_never_authz(self.service_config):
            assert self.osid_object.get_grades().available() == 0
            form = self.session.get_grade_form_for_create(
                self.osid_object.ident,
                [])
            form.display_name = 'Test object'
            grade = self.session.create_grade(form)
            assert isinstance(grade, Grade)
            assert grade.display_name.text == 'Test object'

            form = self.session.get_grade_form_for_update(grade.ident)
            form.display_name = 'new name'
            grade = self.session.update_grade(form)

            assert isinstance(grade, Grade)
            assert grade.display_name.text == 'new name'

            updated_grade_system = self.catalog.get_grade_system(self.osid_object.ident)
            assert updated_grade_system.get_grades().available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.update_grade('foo')

    def test_can_delete_grades(self):
        """Tests can_delete_grades"""
        assert isinstance(self.session.can_delete_grades(self.osid_object.ident),
                          bool)

    def test_delete_grade(self):
        """Tests delete_grade"""
        if not is_never_authz(self.service_config):
            form = self.session.get_grade_form_for_create(
                self.osid_object.ident,
                [])
            form.display_name = 'Test object'
            grade = self.session.create_grade(form)
            assert isinstance(grade, Grade)
            assert grade.display_name.text == 'Test object'

            updated_grade_system = self.catalog.get_grade_system(self.osid_object.ident)
            assert updated_grade_system.get_grades().available() == 1

            self.session.delete_grade(grade.ident)

            updated_grade_system = self.catalog.get_grade_system(self.osid_object.ident)
            assert updated_grade_system.get_grades().available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.delete_grade(self.fake_id)

    def test_can_manage_grade_aliases(self):
        """Tests can_manage_grade_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_grade_aliases(), bool)

    def test_alias_grade(self):
        """Tests alias_grade"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.alias_grade(True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_gradebook_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.grade_system_list = list()
    request.cls.grade_system_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemGradebookSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook for Assignment'
        create_form.description = 'Test Gradebook for GradeSystemGradebookSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + str(num)
            create_form.description = 'Test GradeSystem for GradeSystemGradebookSession tests'
            obj = request.cls.catalog.create_grade_system(create_form)
            request.cls.grade_system_list.append(obj)
            request.cls.grade_system_ids.append(obj.ident)
        request.cls.svc_mgr.assign_grade_system_to_gradebook(
            request.cls.grade_system_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_grade_system_to_gradebook(
            request.cls.grade_system_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_grade_system_from_gradebook(
                request.cls.grade_system_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_grade_system_from_gradebook(
                request.cls.grade_system_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_gradebook_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("grade_system_gradebook_session_class_fixture", "grade_system_gradebook_session_test_fixture")
class TestGradeSystemGradebookSession(object):
    """Tests for GradeSystemGradebookSession"""
    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_gradebook_view()

    def test_can_lookup_grade_system_gradebook_mappings(self):
        """Tests can_lookup_grade_system_gradebook_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_grade_system_gradebook_mappings()
        assert isinstance(result, bool)

    def test_get_grade_system_ids_by_gradebook(self):
        """Tests get_grade_system_ids_by_gradebook"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_grade_system_ids_by_gradebook(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_grade_system_ids_by_gradebook(self.fake_id)

    def test_get_grade_systems_by_gradebook(self):
        """Tests get_grade_systems_by_gradebook"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_grade_systems_by_gradebook(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.GradeSystemList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_systems_by_gradebook(self.fake_id)

    def test_get_grade_system_ids_by_gradebooks(self):
        """Tests get_grade_system_ids_by_gradebooks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_grade_system_ids_by_gradebooks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_system_ids_by_gradebooks([self.fake_id])

    def test_get_grade_systems_by_gradebooks(self):
        """Tests get_grade_systems_by_gradebooks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_grade_systems_by_gradebooks(catalog_ids)
            assert isinstance(results, ABCObjects.GradeSystemList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_systems_by_gradebooks([self.fake_id])

    def test_get_gradebook_ids_by_grade_system(self):
        """Tests get_gradebook_ids_by_grade_system"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_gradebook_ids_by_grade_system(self.grade_system_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_ids_by_grade_system(self.fake_id)

    def test_get_gradebooks_by_grade_system(self):
        """Tests get_gradebooks_by_grade_system"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_gradebooks_by_grade_system(self.grade_system_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebooks_by_grade_system(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_system_gradebook_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.grade_system_list = list()
    request.cls.grade_system_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemGradebookAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook for Assignment'
        create_form.description = 'Test Gradebook for GradeSystemGradebookAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + str(num)
            create_form.description = 'Test GradeSystem for GradeSystemGradebookAssignmentSession tests'
            obj = request.cls.catalog.create_grade_system(create_form)
            request.cls.grade_system_list.append(obj)
            request.cls.grade_system_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_grade_systems():
                request.cls.catalog.delete_grade_system(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_gradebook_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("grade_system_gradebook_assignment_session_class_fixture", "grade_system_gradebook_assignment_session_test_fixture")
class TestGradeSystemGradebookAssignmentSession(object):
    """Tests for GradeSystemGradebookAssignmentSession"""
    def test_can_assign_grade_system(self):
        """Tests can_assign_grade_system"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_grade_system()
        assert isinstance(result, bool)

    def test_can_assign_grade_systems_to_gradebook(self):
        """Tests can_assign_grade_systems_to_gradebook"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_grade_systems_to_gradebook(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_gradebook_ids(self):
        """Tests get_assignable_gradebook_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_gradebook_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_gradebook_ids(self.fake_id)

    def test_get_assignable_gradebook_ids_for_grade_system(self):
        """Tests get_assignable_gradebook_ids_for_grade_system"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_gradebook_ids_for_grade_system(self.catalog.ident, self.grade_system_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_gradebook_ids_for_grade_system(self.fake_id, self.fake_id)

    def test_assign_grade_system_to_gradebook(self):
        """Tests assign_grade_system_to_gradebook"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_grade_systems()
            assert results.available() == 0
            self.session.assign_grade_system_to_gradebook(self.grade_system_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_grade_systems()
            assert results.available() == 1
            self.session.unassign_grade_system_from_gradebook(
                self.grade_system_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_grade_system_to_gradebook(self.fake_id, self.fake_id)

    def test_unassign_grade_system_from_gradebook(self):
        """Tests unassign_grade_system_from_gradebook"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_grade_systems()
            assert results.available() == 0
            self.session.assign_grade_system_to_gradebook(
                self.grade_system_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_grade_systems()
            assert results.available() == 1
            self.session.unassign_grade_system_from_gradebook(
                self.grade_system_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_grade_systems()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_grade_system_from_gradebook(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def grade_entry_lookup_session_test_fixture(request):
    request.cls.grade_entry_list = list()
    request.cls.grade_entry_ids = list()
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        create_form = request.cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradeEntryLookupSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 5
        create_form.numeric_score_increment = 0.25
        request.cls.grade_system = request.cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradeEntryLookupSession tests'
            create_form.grade_system = request.cls.grade_system.ident
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_grade_entry_form_for_create(request.cls.gradebook_column_ids[num], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradeEntryLookupSession tests'
            object = request.cls.catalog.create_grade_entry(create_form)
            request.cls.grade_entry_list.append(object)
            request.cls.grade_entry_ids.append(object.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_grade_entry_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_gradebooks():
                for obj in catalog.get_grade_entries():
                    catalog.delete_grade_entry(obj.ident)
                for obj in catalog.get_gradebook_columns():
                    catalog.delete_gradebook_column(obj.ident)
                for obj in catalog.get_grade_systems():
                    catalog.delete_grade_system(obj.ident)
                request.cls.svc_mgr.delete_gradebook(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_entry_lookup_session_class_fixture", "grade_entry_lookup_session_test_fixture")
class TestGradeEntryLookupSession(object):
    """Tests for GradeEntryLookupSession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_lookup_grade_entries(self):
        """Tests can_lookup_grade_entries"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_grade_entries(), bool)

    def test_use_comparative_grade_entry_view(self):
        """Tests use_comparative_grade_entry_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_grade_entry_view()

    def test_use_plenary_grade_entry_view(self):
        """Tests use_plenary_grade_entry_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_grade_entry_view()

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_gradebook_view()

    def test_use_effective_grade_entry_view(self):
        """Tests use_effective_grade_entry_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_effective_grade_entry_view()

    def test_use_any_effective_grade_entry_view(self):
        """Tests use_any_effective_grade_entry_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_any_effective_grade_entry_view()

    def test_get_grade_entry(self):
        """Tests get_grade_entry"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_grade_entry_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_gradebook_view()
                obj = self.catalog.get_grade_entry(self.grade_entry_list[0].ident)
                assert obj.ident == self.grade_entry_list[0].ident
                self.catalog.use_federated_gradebook_view()
                obj = self.catalog.get_grade_entry(self.grade_entry_list[0].ident)
                assert obj.ident == self.grade_entry_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_grade_entry(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_gradebook_view()
                obj = self.catalog.get_grade_entry(self.grade_entry_list[0].ident)
                assert obj.ident == self.grade_entry_list[0].ident
                self.catalog.use_federated_gradebook_view()
                obj = self.catalog.get_grade_entry(self.grade_entry_list[0].ident)
                assert obj.ident == self.grade_entry_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_grade_entry(self.fake_id)

    def test_get_grade_entries_by_ids(self):
        """Tests get_grade_entries_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        if self.svc_mgr.supports_grade_entry_query():
            objects = self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)
            assert isinstance(objects, GradeEntryList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)
            assert isinstance(objects, GradeEntryList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)
                assert isinstance(objects, GradeEntryList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)
                assert objects.available() > 0
                assert isinstance(objects, GradeEntryList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)

    def test_get_grade_entries_by_genus_type(self):
        """Tests get_grade_entries_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        if self.svc_mgr.supports_grade_entry_query():
            objects = self.catalog.get_grade_entries_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, GradeEntryList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_grade_entries_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, GradeEntryList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_grade_entries_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, GradeEntryList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_grade_entries_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, GradeEntryList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_grade_entries_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_grade_entries_by_parent_genus_type(self):
        """Tests get_grade_entries_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        if self.svc_mgr.supports_grade_entry_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, GradeEntryList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, GradeEntryList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, GradeEntryList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, GradeEntryList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_grade_entries_by_record_type(self):
        """Tests get_grade_entries_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        if self.svc_mgr.supports_grade_entry_query():
            objects = self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, GradeEntryList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, GradeEntryList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, GradeEntryList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, GradeEntryList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)

    def test_get_grade_entries_on_date(self):
        """Tests get_grade_entries_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_entries_on_date(True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column(self):
        """Tests get_grade_entries_for_gradebook_column"""
        pass

    def test_get_grade_entries_for_gradebook_column_on_date(self):
        """Tests get_grade_entries_for_gradebook_column_on_date"""
        end_date = DateTime.utcnow() + datetime.timedelta(days=5)
        end_date = DateTime(**{
            'year': end_date.year,
            'month': end_date.month,
            'day': end_date.day,
            'hour': end_date.hour,
            'minute': end_date.minute,
            'second': end_date.second,
            'microsecond': end_date.microsecond
        })
        if not is_never_authz(self.service_config):
            results = self.session.get_grade_entries_for_gradebook_column_on_date(self.gradebook_column_ids[0],
                                                                                  DateTime.utcnow(),
                                                                                  end_date)
            assert isinstance(results, ABCObjects.GradeEntryList)
            assert results.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_entries_for_gradebook_column_on_date(self.fake_id,
                                                                            DateTime.utcnow(),
                                                                            end_date)

    def test_get_grade_entries_for_resource(self):
        """Tests get_grade_entries_for_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_entries_for_resource(True)

    def test_get_grade_entries_for_resource_on_date(self):
        """Tests get_grade_entries_for_resource_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_entries_for_resource_on_date(True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column_and_resource(self):
        """Tests get_grade_entries_for_gradebook_column_and_resource"""
        pass

    def test_get_grade_entries_for_gradebook_column_and_resource_on_date(self):
        """Tests get_grade_entries_for_gradebook_column_and_resource_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_entries_for_gradebook_column_and_resource_on_date(True, True, True, True)

    def test_get_grade_entries_by_grader(self):
        """Tests get_grade_entries_by_grader"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_entries_by_grader(True)

    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        if self.svc_mgr.supports_grade_entry_query():
            objects = self.catalog.get_grade_entries()
            assert isinstance(objects, GradeEntryList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_grade_entries()
            assert isinstance(objects, GradeEntryList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_grade_entries()
                assert isinstance(objects, GradeEntryList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_grade_entries()
                assert objects.available() > 0
                assert isinstance(objects, GradeEntryList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_grade_entries()

    def test_get_grade_entry_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_grade_entry(self.grade_entry_ids[0], ALIAS_ID)
            obj = self.catalog.get_grade_entry(ALIAS_ID)
            assert obj.get_id() == self.grade_entry_ids[0]


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.grade_entry_list = list()
    request.cls.grade_entry_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def grade_entry_query_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

        form = request.cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Test grade system'
        grade_system = request.cls.catalog.create_grade_system(form)

        form = request.cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Test gradebook column'
        form.set_grade_system(grade_system.ident)
        gradebook_column = request.cls.catalog.create_gradebook_column(form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_grade_entry_form_for_create(gradebook_column.ident, AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + color
            create_form.description = (
                'Test GradeEntry for GradeEntryQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_grade_entry(create_form)
            request.cls.grade_entry_list.append(obj)
            request.cls.grade_entry_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_grade_entry_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_gradebooks():
                for obj in catalog.get_grade_entries():
                    catalog.delete_grade_entry(obj.ident)
                for obj in catalog.get_gradebook_columns():
                    catalog.delete_gradebook_column(obj.ident)
                for obj in catalog.get_grade_systems():
                    catalog.delete_grade_system(obj.ident)
                request.cls.svc_mgr.delete_gradebook(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("grade_entry_query_session_class_fixture", "grade_entry_query_session_test_fixture")
class TestGradeEntryQuerySession(object):
    """Tests for GradeEntryQuerySession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_search_grade_entries(self):
        """Tests can_search_grade_entries"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_grade_entries(), bool)

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_grade_entry_query()
        assert isinstance(query, ABCQueries.GradeEntryQuery)

    def test_get_grade_entries_by_query(self):
        """Tests get_grade_entries_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_grade_entry_query()
            query.match_display_name('orange')
            assert self.catalog.get_grade_entries_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_grade_entries_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_grade_entries_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.grade_entry_list = list()
    request.cls.grade_entry_ids = list()
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        create_form = request.cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradeEntryAdminSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 5
        create_form.numeric_score_increment = 0.25
        request.cls.grade_system = request.cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradeEntryAdminSession tests'
            create_form.grade_system = request.cls.grade_system.ident
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_grade_entry_form_for_create(request.cls.gradebook_column_ids[num], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradeEntryAdminSession tests'
            object = request.cls.catalog.create_grade_entry(create_form)
            request.cls.grade_entry_list.append(object)
            request.cls.grade_entry_ids.append(object.ident)

        request.cls.form = request.cls.catalog.get_grade_entry_form_for_create(request.cls.gradebook_column_ids[0], AGENT_ID, [])
        request.cls.form.display_name = 'new GradeEntry'
        request.cls.form.description = 'description of GradeEntry'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_grade_entry(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_grade_entry_admin_session(proxy=PROXY)

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
def grade_entry_admin_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("grade_entry_admin_session_class_fixture", "grade_entry_admin_session_test_fixture")
class TestGradeEntryAdminSession(object):
    """Tests for GradeEntryAdminSession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_create_grade_entries(self):
        """Tests can_create_grade_entries"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_grade_entries(), bool)

    def test_can_create_grade_entry_with_record_types(self):
        """Tests can_create_grade_entry_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_grade_entry_with_record_types(DEFAULT_TYPE), bool)

    def test_get_grade_entry_form_for_create(self):
        """Tests get_grade_entry_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_grade_entry_form_for_create(self.gradebook_column_ids[0], AGENT_ID, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_grade_entry_form_for_create(self.fake_id, AGENT_ID, [])

    def test_create_grade_entry(self):
        """Tests create_grade_entry"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.grading.objects import GradeEntry
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, GradeEntry)
            assert self.osid_object.display_name.text == 'new GradeEntry'
            assert self.osid_object.description.text == 'description of GradeEntry'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_grade_entry(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_grade_entry('I Will Break You!')
            update_form = self.catalog.get_grade_entry_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_grade_entry(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_grade_entry('foo')

    def test_can_overridecalculated_grade_entries(self):
        """Tests can_overridecalculated_grade_entries"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_overridecalculated_grade_entries()

    def test_get_grade_entry_form_for_override(self):
        """Tests get_grade_entry_form_for_override"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_grade_entry_form_for_override(True, True)

    def test_override_calculated_grade_entry(self):
        """Tests override_calculated_grade_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.override_calculated_grade_entry(True)

    def test_can_update_grade_entries(self):
        """Tests can_update_grade_entries"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_grade_entries(), bool)

    def test_get_grade_entry_form_for_update(self):
        """Tests get_grade_entry_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_grade_entry_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_grade_entry_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_grade_entry_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='grading.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_grade_entry_form_for_update(self.fake_id)

    def test_update_grade_entry(self):
        """Tests update_grade_entry"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.grading.objects import GradeEntry
            form = self.catalog.get_grade_entry_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_grade_entry(form)
            assert isinstance(updated_object, GradeEntry)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_grade_entry(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_grade_entry('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_grade_entry(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_grade_entry('foo')

    def test_can_delete_grade_entries(self):
        """Tests can_delete_grade_entries"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_grade_entries(), bool)

    def test_delete_grade_entry(self):
        """Tests delete_grade_entry"""
        if not is_never_authz(self.service_config):
            create_form = self.catalog.get_grade_entry_form_for_create(self.gradebook_column_ids[0], AGENT_ID, [])
            create_form.display_name = 'new GradeEntry'
            create_form.description = 'description of GradeEntry'
            create_form.genus_type = NEW_TYPE
            osid_object = self.catalog.create_grade_entry(create_form)
            self.catalog.delete_grade_entry(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_grade_entry(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_grade_entry(self.fake_id)

    def test_can_manage_grade_entry_aliases(self):
        """Tests can_manage_grade_entry_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_grade_entry_aliases(), bool)

    def test_alias_grade_entry(self):
        """Tests alias_grade_entry"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_grade_entry(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_grade_entry(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_grade_entry(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def gradebook_column_lookup_session_test_fixture(request):
    request.cls.grade_entry_list = list()
    request.cls.grade_entry_ids = list()
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()

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
    else:
        request.cls.catalog = request.cls.svc_mgr.get_gradebook_column_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_gradebooks():
                for obj in catalog.get_grade_entries():
                    catalog.delete_grade_entry(obj.ident)
                for obj in catalog.get_gradebook_columns():
                    catalog.delete_gradebook_column(obj.ident)
                for obj in catalog.get_grade_systems():
                    catalog.delete_grade_system(obj.ident)
                request.cls.svc_mgr.delete_gradebook(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_column_lookup_session_class_fixture", "gradebook_column_lookup_session_test_fixture")
class TestGradebookColumnLookupSession(object):
    """Tests for GradebookColumnLookupSession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_lookup_gradebook_columns(self):
        """Tests can_lookup_gradebook_columns"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_gradebook_columns(), bool)

    def test_use_comparative_gradebook_column_view(self):
        """Tests use_comparative_gradebook_column_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_gradebook_column_view()

    def test_use_plenary_gradebook_column_view(self):
        """Tests use_plenary_gradebook_column_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_gradebook_column_view()

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_gradebook_view()

    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_gradebook_column_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_gradebook_view()
                obj = self.catalog.get_gradebook_column(self.gradebook_column_list[0].ident)
                assert obj.ident == self.gradebook_column_list[0].ident
                self.catalog.use_federated_gradebook_view()
                obj = self.catalog.get_gradebook_column(self.gradebook_column_list[0].ident)
                assert obj.ident == self.gradebook_column_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_gradebook_column(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_gradebook_view()
                obj = self.catalog.get_gradebook_column(self.gradebook_column_list[0].ident)
                assert obj.ident == self.gradebook_column_list[0].ident
                self.catalog.use_federated_gradebook_view()
                obj = self.catalog.get_gradebook_column(self.gradebook_column_list[0].ident)
                assert obj.ident == self.gradebook_column_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_gradebook_column(self.fake_id)

    def test_get_gradebook_columns_by_ids(self):
        """Tests get_gradebook_columns_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        if self.svc_mgr.supports_gradebook_column_query():
            objects = self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)
            assert isinstance(objects, GradebookColumnList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)
            assert isinstance(objects, GradebookColumnList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)
                assert isinstance(objects, GradebookColumnList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)
                assert objects.available() > 0
                assert isinstance(objects, GradebookColumnList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)

    def test_get_gradebook_columns_by_genus_type(self):
        """Tests get_gradebook_columns_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        if self.svc_mgr.supports_gradebook_column_query():
            objects = self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, GradebookColumnList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, GradebookColumnList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, GradebookColumnList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, GradebookColumnList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_gradebook_columns_by_parent_genus_type(self):
        """Tests get_gradebook_columns_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        if self.svc_mgr.supports_gradebook_column_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, GradebookColumnList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, GradebookColumnList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, GradebookColumnList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, GradebookColumnList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_gradebook_columns_by_record_type(self):
        """Tests get_gradebook_columns_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        if self.svc_mgr.supports_gradebook_column_query():
            objects = self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, GradebookColumnList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, GradebookColumnList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, GradebookColumnList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, GradebookColumnList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)

    def test_get_gradebook_columns(self):
        """Tests get_gradebook_columns"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        if self.svc_mgr.supports_gradebook_column_query():
            objects = self.catalog.get_gradebook_columns()
            assert isinstance(objects, GradebookColumnList)
            self.catalog.use_federated_gradebook_view()
            objects = self.catalog.get_gradebook_columns()
            assert isinstance(objects, GradebookColumnList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_gradebook_columns()
                assert isinstance(objects, GradebookColumnList)
                self.catalog.use_federated_gradebook_view()
                objects = self.catalog.get_gradebook_columns()
                assert objects.available() > 0
                assert isinstance(objects, GradebookColumnList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_gradebook_columns()

    def test_get_gradebook_column_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_gradebook_column(self.gradebook_column_ids[0], ALIAS_ID)
            obj = self.catalog.get_gradebook_column(ALIAS_ID)
            assert obj.get_id() == self.gradebook_column_ids[0]

    def test_supports_summary(self):
        """Tests supports_summary"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.supports_summary()

    def test_get_gradebook_column_summary(self):
        """Tests get_gradebook_column_summary"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook_column_summary(self.gradebook_column_ids[0]),
                              GradebookColumnSummary)
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_gradebook_column_summary(self.fake_id)


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def gradebook_column_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + color
            create_form.description = (
                'Test GradebookColumn for GradebookColumnQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_gradebook_column_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_column_query_session_class_fixture", "gradebook_column_query_session_test_fixture")
class TestGradebookColumnQuerySession(object):
    """Tests for GradebookColumnQuerySession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_search_gradebook_columns(self):
        """Tests can_search_gradebook_columns"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_gradebook_columns(), bool)

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_gradebook_view()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_gradebook_column_query()
        assert isinstance(query, ABCQueries.GradebookColumnQuery)

    def test_get_gradebook_columns_by_query(self):
        """Tests get_gradebook_columns_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_gradebook_column_query()
            query.match_display_name('orange')
            assert self.catalog.get_gradebook_columns_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_gradebook_columns_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_gradebook_columns_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_gradebook_column_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_gradebook_column_form_for_create([])
        request.cls.form.display_name = 'new GradebookColumn'
        request.cls.form.description = 'description of GradebookColumn'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_gradebook_column(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_gradebook_column(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_column_admin_session_class_fixture", "gradebook_column_admin_session_test_fixture")
class TestGradebookColumnAdminSession(object):
    """Tests for GradebookColumnAdminSession"""
    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_gradebook_id() == self.catalog.ident

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_gradebook(), ABCGradebook)

    def test_can_create_gradebook_columns(self):
        """Tests can_create_gradebook_columns"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.catalog.can_create_gradebook_columns(), bool)

    def test_can_create_gradebook_column_with_record_types(self):
        """Tests can_create_gradebook_column_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.catalog.can_create_gradebook_column_with_record_types(DEFAULT_TYPE), bool)

    def test_get_gradebook_column_form_for_create(self):
        """Tests get_gradebook_column_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_gradebook_column_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_gradebook_column_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_gradebook_column_form_for_create([])

    def test_create_gradebook_column(self):
        """Tests create_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookColumn
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, GradebookColumn)
            assert self.osid_object.display_name.text == 'new GradebookColumn'
            assert self.osid_object.description.text == 'description of GradebookColumn'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_gradebook_column(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_gradebook_column('I Will Break You!')
            update_form = self.catalog.get_gradebook_column_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_gradebook_column(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_gradebook_column('foo')

    def test_can_update_gradebook_columns(self):
        """Tests can_update_gradebook_columns"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.catalog.can_update_gradebook_columns(), bool)

    def test_get_gradebook_column_form_for_update(self):
        """Tests get_gradebook_column_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_gradebook_column_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_gradebook_column_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_gradebook_column_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='grading.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_gradebook_column_form_for_update(self.fake_id)

    def test_update_gradebook_column(self):
        """Tests update_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.grading.objects import GradebookColumn
            form = self.catalog.get_gradebook_column_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_gradebook_column(form)
            assert isinstance(updated_object, GradebookColumn)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_gradebook_column(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_gradebook_column('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_gradebook_column(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_gradebook_column('foo')

    def test_sequence_gradebook_columns(self):
        """Tests sequence_gradebook_columns"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.sequence_gradebook_columns(True)

    def test_move_gradebook_column(self):
        """Tests move_gradebook_column"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.move_gradebook_column(True, True)

    def test_copy_gradebook_column_entries(self):
        """Tests copy_gradebook_column_entries"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.copy_gradebook_column_entries(True, True)

    def test_can_delete_gradebook_columns(self):
        """Tests can_delete_gradebook_columns"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.catalog.can_delete_gradebook_columns(), bool)

    def test_delete_gradebook_column(self):
        """Tests delete_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_gradebook_column_form_for_create([])
            form.display_name = 'new GradebookColumn'
            form.description = 'description of GradebookColumn'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_gradebook_column(form)
            self.catalog.delete_gradebook_column(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_gradebook_column(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_gradebook_column(self.fake_id)

    def test_can_manage_gradebook_column_aliases(self):
        """Tests can_manage_gradebook_column_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_gradebook_column_aliases(), bool)

    def test_alias_gradebook_column(self):
        """Tests alias_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_gradebook_column(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_gradebook_column(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_gradebook_column(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_gradebook_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnGradebookSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook for Assignment'
        create_form.description = 'Test Gradebook for GradebookColumnGradebookSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradebookColumnGradebookSession tests'
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)
        request.cls.svc_mgr.assign_gradebook_column_to_gradebook(
            request.cls.gradebook_column_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_gradebook_column_to_gradebook(
            request.cls.gradebook_column_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_gradebook_column_from_gradebook(
                request.cls.gradebook_column_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_gradebook_column_from_gradebook(
                request.cls.gradebook_column_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_gradebook_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("gradebook_column_gradebook_session_class_fixture", "gradebook_column_gradebook_session_test_fixture")
class TestGradebookColumnGradebookSession(object):
    """Tests for GradebookColumnGradebookSession"""
    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_gradebook_view()

    def test_can_lookup_gradebook_column_gradebook_mappings(self):
        """Tests can_lookup_gradebook_column_gradebook_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_gradebook_column_gradebook_mappings()
        assert isinstance(result, bool)

    def test_get_gradebook_column_ids_by_gradebook(self):
        """Tests get_gradebook_column_ids_by_gradebook"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_gradebook_column_ids_by_gradebook(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_column_ids_by_gradebook(self.fake_id)

    def test_get_gradebook_columns_by_gradebook(self):
        """Tests get_gradebook_columns_by_gradebook"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_gradebook_columns_by_gradebook(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.GradebookColumnList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_gradebook_columns_by_gradebook(self.fake_id)

    def test_get_gradebook_column_ids_by_gradebooks(self):
        """Tests get_gradebook_column_ids_by_gradebooks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_gradebook_column_ids_by_gradebooks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_gradebook_column_ids_by_gradebooks([self.fake_id])

    def test_get_gradebook_columns_by_gradebooks(self):
        """Tests get_gradebook_columns_by_gradebooks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_gradebook_columns_by_gradebooks(catalog_ids)
            assert isinstance(results, ABCObjects.GradebookColumnList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_gradebook_columns_by_gradebooks([self.fake_id])

    def test_get_gradebook_ids_by_gradebook_column(self):
        """Tests get_gradebook_ids_by_gradebook_column"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_gradebook_ids_by_gradebook_column(self.gradebook_column_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_ids_by_gradebook_column(self.fake_id)

    def test_get_gradebooks_by_gradebook_column(self):
        """Tests get_gradebooks_by_gradebook_column"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_gradebooks_by_gradebook_column(self.gradebook_column_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebooks_by_gradebook_column(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_gradebook_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.gradebook_column_list = list()
    request.cls.gradebook_column_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnGradebookAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook for Assignment'
        create_form.description = 'Test Gradebook for GradebookColumnGradebookAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_gradebook(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradebookColumnGradebookAssignmentSession tests'
            obj = request.cls.catalog.create_gradebook_column(create_form)
            request.cls.gradebook_column_list.append(obj)
            request.cls.gradebook_column_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_gradebook_columns():
                request.cls.catalog.delete_gradebook_column(obj.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_gradebook_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("gradebook_column_gradebook_assignment_session_class_fixture", "gradebook_column_gradebook_assignment_session_test_fixture")
class TestGradebookColumnGradebookAssignmentSession(object):
    """Tests for GradebookColumnGradebookAssignmentSession"""
    def test_can_assign_gradebook_columns(self):
        """Tests can_assign_gradebook_columns"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_gradebook_columns()
        assert isinstance(result, bool)

    def test_can_assign_gradebook_columns_to_gradebook(self):
        """Tests can_assign_gradebook_columns_to_gradebook"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_gradebook_columns_to_gradebook(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_gradebook_ids(self):
        """Tests get_assignable_gradebook_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_gradebook_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_gradebook_ids(self.fake_id)

    def test_get_assignable_gradebook_ids_for_gradebook_column(self):
        """Tests get_assignable_gradebook_ids_for_gradebook_column"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_gradebook_ids_for_gradebook_column(self.catalog.ident, self.gradebook_column_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_gradebook_ids_for_gradebook_column(self.fake_id, self.fake_id)

    def test_assign_gradebook_column_to_gradebook(self):
        """Tests assign_gradebook_column_to_gradebook"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_gradebook_columns()
            assert results.available() == 0
            self.session.assign_gradebook_column_to_gradebook(self.gradebook_column_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_gradebook_columns()
            assert results.available() == 1
            self.session.unassign_gradebook_column_from_gradebook(
                self.gradebook_column_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_gradebook_column_to_gradebook(self.fake_id, self.fake_id)

    def test_unassign_gradebook_column_from_gradebook(self):
        """Tests unassign_gradebook_column_from_gradebook"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_gradebook_columns()
            assert results.available() == 0
            self.session.assign_gradebook_column_to_gradebook(
                self.gradebook_column_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_gradebook_columns()
            assert results.available() == 1
            self.session.unassign_gradebook_column_from_gradebook(
                self.gradebook_column_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_gradebook_columns()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_gradebook_column_from_gradebook(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test Gradebook ' + str(num)
            create_form.description = 'Test Gradebook for grading proxy manager tests'
            catalog = request.cls.svc_mgr.create_gradebook(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_gradebooks():
                request.cls.svc_mgr.delete_gradebook(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("gradebook_lookup_session_class_fixture", "gradebook_lookup_session_test_fixture")
class TestGradebookLookupSession(object):
    """Tests for GradebookLookupSession"""
    def test_can_lookup_gradebooks(self):
        """Tests can_lookup_gradebooks"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_gradebooks(), bool)

    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_gradebook_view()

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_gradebook(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook(self.fake_id)

    def test_get_gradebooks_by_ids(self):
        """Tests get_gradebooks_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_gradebooks_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.GradebookList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebooks_by_ids([self.fake_id])

    def test_get_gradebooks_by_genus_type(self):
        """Tests get_gradebooks_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_gradebooks_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.GradebookList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebooks_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_gradebooks_by_parent_genus_type(self):
        """Tests get_gradebooks_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_gradebooks_by_parent_genus_type(True)

    def test_get_gradebooks_by_record_type(self):
        """Tests get_gradebooks_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_gradebooks_by_record_type(True)

    def test_get_gradebooks_by_provider(self):
        """Tests get_gradebooks_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_gradebooks_by_provider(True)

    def test_get_gradebooks(self):
        """Tests get_gradebooks"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_gradebooks()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.GradebookList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebooks()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def gradebook_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook For Deletion'
        create_form.description = 'Test Gradebook for GradebookAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_gradebook(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_gradebooks():
                request.cls.svc_mgr.delete_gradebook(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("gradebook_admin_session_class_fixture", "gradebook_admin_session_test_fixture")
class TestGradebookAdminSession(object):
    """Tests for GradebookAdminSession"""
    def test_can_create_gradebooks(self):
        """Tests can_create_gradebooks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_gradebooks(), bool)

    def test_can_create_gradebook_with_record_types(self):
        """Tests can_create_gradebook_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_gradebook_with_record_types(DEFAULT_TYPE), bool)

    def test_get_gradebook_form_for_create(self):
        """Tests get_gradebook_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.grading.objects import GradebookForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_gradebook_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_gradebook_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_form_for_create([])

    def test_create_gradebook(self):
        """Tests create_gradebook"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.grading.objects import Gradebook
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_gradebook_form_for_create([])
            catalog_form.display_name = 'Test Gradebook'
            catalog_form.description = 'Test Gradebook for GradebookAdminSession.create_gradebook tests'
            new_catalog = self.svc_mgr.create_gradebook(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_gradebook(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_gradebook('I Will Break You!')
            update_form = self.svc_mgr.get_gradebook_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_gradebook(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_gradebook('foo')

    def test_can_update_gradebooks(self):
        """Tests can_update_gradebooks"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_gradebooks(), bool)

    def test_get_gradebook_form_for_update(self):
        """Tests get_gradebook_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.grading.objects import GradebookForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_gradebook_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_form_for_update(self.fake_id)

    def test_update_gradebook(self):
        """Tests update_gradebook"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_gradebook_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_gradebook(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_gradebook('foo')

    def test_can_delete_gradebooks(self):
        """Tests can_delete_gradebooks"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_gradebooks(), bool)

    def test_delete_gradebook(self):
        """Tests delete_gradebook"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_gradebook(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_gradebook(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_gradebook(self.fake_id)

    def test_can_manage_gradebook_aliases(self):
        """Tests can_manage_gradebook_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_gradebook_aliases(), bool)

    def test_alias_gradebook(self):
        """Tests alias_gradebook"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('grading.Gradebook%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_gradebook(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_gradebook(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_gradebook(self.fake_id, alias_id)


# Override this because spec doesn't have a method ``remove_child_gradebooks``
@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_hierarchy_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Gradebook ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.svc_mgr.add_root_gradebook(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_gradebook(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_gradebook(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
            request.cls.svc_mgr.remove_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
            request.cls.svc_mgr.remove_root_gradebook(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_gradebook(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_hierarchy_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("gradebook_hierarchy_session_class_fixture", "gradebook_hierarchy_session_test_fixture")
class TestGradebookHierarchySession(object):
    """Tests for GradebookHierarchySession"""
    def test_get_gradebook_hierarchy_id(self):
        """Tests get_gradebook_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_gradebook_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_gradebook_hierarchy(self):
        """Tests get_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_gradebook_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_hierarchy()

    def test_can_access_gradebook_hierarchy(self):
        """Tests can_access_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_gradebook_hierarchy(), bool)

    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_gradebook_view()

    def test_get_root_gradebook_ids(self):
        """Tests get_root_gradebook_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_gradebook_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_gradebook_ids()

    def test_get_root_gradebooks(self):
        """Tests get_root_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.grading.objects import GradebookList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_gradebooks()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_gradebooks()

    def test_has_parent_gradebooks(self):
        """Tests has_parent_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_gradebooks(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_gradebooks(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_gradebooks(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_gradebooks(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_gradebooks(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_gradebooks(self.fake_id)

    def test_is_parent_of_gradebook(self):
        """Tests is_parent_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_gradebook(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_gradebook(self.fake_id, self.fake_id)

    def test_get_parent_gradebook_ids(self):
        """Tests get_parent_gradebook_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_gradebook_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_gradebook_ids(self.fake_id)

    def test_get_parent_gradebooks(self):
        """Tests get_parent_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_gradebooks(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_gradebooks(self.fake_id)

    def test_is_ancestor_of_gradebook(self):
        """Tests is_ancestor_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_gradebook,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_gradebook(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_gradebooks(self):
        """Tests has_child_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_gradebooks(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_gradebooks(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_gradebooks(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_gradebooks(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_gradebooks(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_gradebooks(self.fake_id)

    def test_is_child_of_gradebook(self):
        """Tests is_child_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_gradebook(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_gradebook(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_gradebook(self.fake_id, self.fake_id)

    def test_get_child_gradebook_ids(self):
        """Tests get_child_gradebook_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_gradebook_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_gradebook_ids(self.fake_id)

    def test_get_child_gradebooks(self):
        """Tests get_child_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_gradebooks(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_gradebooks(self.fake_id)

    def test_is_descendant_of_gradebook(self):
        """Tests is_descendant_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_gradebook,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_gradebook(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_gradebook_node_ids(self):
        """Tests get_gradebook_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_gradebook_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_node_ids(self.fake_id, 1, 2, False)

    def test_get_gradebook_nodes(self):
        """Tests get_gradebook_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_gradebook_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_nodes(self.fake_id, 1, 2, False)


# Override this because spec doesn't have a method ``remove_child_gradebooks``
@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_hierarchy_design_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Gradebook ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.svc_mgr.add_root_gradebook(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_gradebook(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_gradebook(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
            request.cls.svc_mgr.remove_child_gradebook(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
            request.cls.svc_mgr.remove_root_gradebook(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_gradebook(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_hierarchy_design_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("gradebook_hierarchy_design_session_class_fixture", "gradebook_hierarchy_design_session_test_fixture")
class TestGradebookHierarchyDesignSession(object):
    """Tests for GradebookHierarchyDesignSession"""
    def test_get_gradebook_hierarchy_id(self):
        """Tests get_gradebook_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_gradebook_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_gradebook_hierarchy(self):
        """Tests get_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_gradebook_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_gradebook_hierarchy()

    def test_can_modify_gradebook_hierarchy(self):
        """Tests can_modify_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_gradebook_hierarchy(), bool)

    def test_add_root_gradebook(self):
        """Tests add_root_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_gradebooks()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_gradebook(self.fake_id)

    def test_remove_root_gradebook(self):
        """Tests remove_root_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_gradebooks()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Gradebook root'
            new_gradebook = self.svc_mgr.create_gradebook(create_form)
            self.svc_mgr.add_root_gradebook(new_gradebook.ident)

            roots = self.session.get_root_gradebooks()
            assert roots.available() == 2

            self.session.remove_root_gradebook(new_gradebook.ident)

            roots = self.session.get_root_gradebooks()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_gradebook(self.fake_id)

    def test_add_child_gradebook(self):
        """Tests add_child_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_gradebook(self.fake_id, self.fake_id)

    def test_remove_child_gradebook(self):
        """Tests remove_child_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Gradebook child'
            new_gradebook = self.svc_mgr.create_gradebook(create_form)
            self.svc_mgr.add_child_gradebook(
                self.catalogs['Root'].ident,
                new_gradebook.ident)

            children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_gradebook(
                self.catalogs['Root'].ident,
                new_gradebook.ident)

            children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_gradebook(self.fake_id, self.fake_id)
