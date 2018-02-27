"""Unit tests of learning sessions."""


import datetime
import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.learning import objects as ABCObjects
from dlkit.abstract_osid.learning import queries as ABCQueries
from dlkit.abstract_osid.learning.objects import ObjectiveBank as ABCObjectiveBank
from dlkit.abstract_osid.learning.objects import ObjectiveList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
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
def objective_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def objective_lookup_session_test_fixture(request):
    request.cls.objective_list = list()
    request.cls.objective_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveLookupSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_list.append(obj)
            request.cls.objective_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_lookup_session_class_fixture", "objective_lookup_session_test_fixture")
class TestObjectiveLookupSession(object):
    """Tests for ObjectiveLookupSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_lookup_objectives(self):
        """Tests can_lookup_objectives"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_objectives(), bool)

    def test_use_comparative_objective_view(self):
        """Tests use_comparative_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_objective_view()

    def test_use_plenary_objective_view(self):
        """Tests use_plenary_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_objective_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_objective(self):
        """Tests get_objective"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_objective_bank_view()
            obj = self.catalog.get_objective(self.objective_list[0].ident)
            assert obj.ident == self.objective_list[0].ident
            self.catalog.use_federated_objective_bank_view()
            obj = self.catalog.get_objective(self.objective_list[0].ident)
            assert obj.ident == self.objective_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_objective(self.fake_id)

    def test_get_objectives_by_ids(self):
        """Tests get_objectives_by_ids"""
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_ids(self.objective_ids)
        assert isinstance(objects, ObjectiveList)
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_ids(self.objective_ids)
        assert isinstance(objects, ObjectiveList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_objectives_by_genus_type(self):
        """Tests get_objectives_by_genus_type"""
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, ObjectiveList)
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, ObjectiveList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_objectives_by_parent_genus_type(self):
        """Tests get_objectives_by_parent_genus_type"""
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_objectives_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ObjectiveList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_objectives_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, ObjectiveList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_objectives_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_objectives_by_record_type(self):
        """Tests get_objectives_by_record_type"""
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, ObjectiveList)
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, ObjectiveList)

    def test_get_objectives(self):
        """Tests get_objectives"""
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives()
        assert isinstance(objects, ObjectiveList)
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives()
        assert isinstance(objects, ObjectiveList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_objective_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_objective(self.objective_ids[0], ALIAS_ID)
            obj = self.catalog.get_objective(ALIAS_ID)
            assert obj.get_id() == self.objective_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def objective_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.objective_list = list()
    request.cls.objective_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + color
            create_form.description = (
                'Test Objective for ObjectiveQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_list.append(obj)
            request.cls.objective_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_query_session_class_fixture", "objective_query_session_test_fixture")
class TestObjectiveQuerySession(object):
    """Tests for ObjectiveQuerySession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_search_objectives(self):
        """Tests can_search_objectives"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_objectives(), bool)

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_objective_query(self):
        """Tests get_objective_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_objective_query()
        assert isinstance(query, ABCQueries.ObjectiveQuery)

    def test_get_objectives_by_query(self):
        """Tests get_objectives_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_objective_query()
            query.match_display_name('orange')
            assert self.catalog.get_objectives_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_objectives_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_objectives_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_objective_form_for_create([])
        request.cls.form.display_name = 'new Objective'
        request.cls.form.description = 'description of Objective'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_objective(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_objective(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_admin_session_class_fixture", "objective_admin_session_test_fixture")
class TestObjectiveAdminSession(object):
    """Tests for ObjectiveAdminSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_create_objectives(self):
        """Tests can_create_objectives"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_objectives(), bool)

    def test_can_create_objective_with_record_types(self):
        """Tests can_create_objective_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_objective_with_record_types(DEFAULT_TYPE), bool)

    def test_get_objective_form_for_create(self):
        """Tests get_objective_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_objective_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_objective_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_objective_form_for_create([])

    def test_create_objective(self):
        """Tests create_objective"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.learning.objects import Objective
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Objective)
            assert self.osid_object.display_name.text == 'new Objective'
            assert self.osid_object.description.text == 'description of Objective'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_objective(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_objective('I Will Break You!')
            update_form = self.catalog.get_objective_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_objective(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_objective('foo')

    def test_can_update_objectives(self):
        """Tests can_update_objectives"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_objectives(), bool)

    def test_get_objective_form_for_update(self):
        """Tests get_objective_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_objective_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_objective_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_objective_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='learning.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_objective_form_for_update(self.fake_id)

    def test_update_objective(self):
        """Tests update_objective"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.learning.objects import Objective
            form = self.catalog.get_objective_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_objective(form)
            assert isinstance(updated_object, Objective)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_objective(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_objective('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_objective(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_objective('foo')

    def test_can_delete_objectives(self):
        """Tests can_delete_objectives"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_objectives(), bool)

    def test_delete_objective(self):
        """Tests delete_objective"""
        # From test_templates/learning.py::ObjectiveAdminSession::delete_objective_template
        if not is_never_authz(self.service_config):
            results = self.catalog.get_objectives()
            assert results.available() == 1

            form = self.catalog.get_objective_form_for_create([])
            form.display_name = 'new Objective'
            form.description = 'description of Objective'
            new_objective = self.catalog.create_objective(form)

            results = self.catalog.get_objectives()
            assert results.available() == 2

            self.session.delete_objective(new_objective.ident)

            results = self.catalog.get_objectives()
            assert results.available() == 1
            assert str(results.next().ident) != str(new_objective.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_objective(self.fake_id)

    def test_can_manage_objective_aliases(self):
        """Tests can_manage_objective_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_objective_aliases(), bool)

    def test_alias_objective(self):
        """Tests alias_objective"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_objective(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_objective(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_objective(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_hierarchy_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveHierarchySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_hierarchy_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_hierarchy_session_test_fixture(request):
    request.cls.child_list = list()
    request.cls.child_ids = list()
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveHierarchySession Lookup'
        create_form.description = 'Test Objective for ObjectiveHierarchySession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        request.cls.catalog.add_root_objective(request.cls.objective.ident)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveHierarchySession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.child_list.append(obj)
            request.cls.child_ids.append(obj.ident)
            request.cls.catalog.add_child_objective(request.cls.objective.ident, obj.ident)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.remove_child_objectives(request.cls.objective.ident)
            request.cls.catalog.remove_root_objective(request.cls.objective.ident)
            for obj_id in request.cls.child_ids:
                request.cls.catalog.delete_objective(obj_id)
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_hierarchy_session_class_fixture", "objective_hierarchy_session_test_fixture")
class TestObjectiveHierarchySession(object):
    """Tests for ObjectiveHierarchySession"""
    def test_get_objective_hierarchy_id(self):
        """Tests get_objective_hierarchy_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_hierarchy_id()

    def test_get_objective_hierarchy(self):
        """Tests get_objective_hierarchy"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_hierarchy()

    def test_can_access_objective_hierarchy(self):
        """Tests can_access_objective_hierarchy"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_access_objective_hierarchy()

    def test_use_comparative_objective_view(self):
        """Tests use_comparative_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_objective_view()

    def test_use_plenary_objective_view(self):
        """Tests use_plenary_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_objective_view()

    def test_get_root_objective_ids(self):
        """Tests get_root_objective_ids"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_root_objective_ids()

    def test_get_root_objectives(self):
        """Tests get_root_objectives"""
        if not is_never_authz(self.service_config):
            roots = self.catalog.get_root_objectives()
            assert roots.available() == 1
            assert isinstance(roots, ObjectiveList)
            assert str(roots.next().ident) == str(self.objective.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_root_objectives()

    def test_has_parent_objectives(self):
        """Tests has_parent_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.has_parent_objectives(True)

    def test_is_parent_of_objective(self):
        """Tests is_parent_of_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_parent_of_objective(True, True)

    def test_get_parent_objective_ids(self):
        """Tests get_parent_objective_ids"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_parent_objective_ids(True)

    def test_get_parent_objectives(self):
        """Tests get_parent_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_parent_objectives(True)

    def test_is_ancestor_of_objective(self):
        """Tests is_ancestor_of_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_ancestor_of_objective(True, True)

    def test_has_child_objectives(self):
        """Tests has_child_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.has_child_objectives(True)

    def test_is_child_of_objective(self):
        """Tests is_child_of_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_child_of_objective(True, True)

    def test_get_child_objective_ids(self):
        """Tests get_child_objective_ids"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_child_objective_ids(True)

    def test_get_child_objectives(self):
        """Tests get_child_objectives"""
        if not is_never_authz(self.service_config):
            children = self.catalog.get_child_objectives(self.objective.ident)
            assert children.available() == 2
            assert isinstance(children, ObjectiveList)
            assert str(children.next().ident) == str(self.child_ids[0])
            assert str(children.next().ident) == str(self.child_ids[1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_child_objectives(self.fake_id)

    def test_is_descendant_of_objective(self):
        """Tests is_descendant_of_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_descendant_of_objective(True, True)

    def test_get_objective_node_ids(self):
        """Tests get_objective_node_ids"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_node_ids(True, True, True, True)

    def test_get_objective_nodes(self):
        """Tests get_objective_nodes"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_nodes(True, True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_hierarchy_design_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveHierarchyDesignSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_hierarchy_design_session_test_fixture(request):
    request.cls.child_list = list()
    request.cls.child_ids = list()
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveHierarchyDesignSession Lookup'
        create_form.description = 'Test Objective for ObjectiveHierarchyDesignSession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveHierarchyDesignSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.child_list.append(obj)
            request.cls.child_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_hierarchy_design_session(proxy=PROXY)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj_id in request.cls.child_ids:
                request.cls.catalog.delete_objective(obj_id)
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_hierarchy_design_session_class_fixture", "objective_hierarchy_design_session_test_fixture")
class TestObjectiveHierarchyDesignSession(object):
    """Tests for ObjectiveHierarchyDesignSession"""
    def test_get_objective_hierarchy_id(self):
        """Tests get_objective_hierarchy_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_hierarchy_id()

    def test_get_objective_hierarchy(self):
        """Tests get_objective_hierarchy"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_hierarchy()

    def test_can_modify_objective_hierarchy(self):
        """Tests can_modify_objective_hierarchy"""
        assert isinstance(self.catalog.can_modify_objective_hierarchy(), bool)

    def test_add_root_objective(self):
        """Tests add_root_objective"""
        if not is_never_authz(self.service_config):
            roots = self.catalog.get_root_objectives()
            assert roots.available() == 0
            assert isinstance(roots, ObjectiveList)

            self.catalog.add_root_objective(self.objective.ident)
            roots = self.catalog.get_root_objectives()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_objective(self.fake_id)

    def test_remove_root_objective(self):
        """Tests remove_root_objective"""
        if not is_never_authz(self.service_config):
            self.catalog.add_root_objective(self.objective.ident)

            roots = self.catalog.get_root_objectives()
            assert roots.available() == 1

            self.catalog.remove_root_objective(self.objective.ident)

            roots = self.catalog.get_root_objectives()
            assert roots.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_objective(self.fake_id)

    def test_add_child_objective(self):
        """Tests add_child_objective"""
        if not is_never_authz(self.service_config):
            self.catalog.add_root_objective(self.objective.ident)

            with pytest.raises(errors.IllegalState):
                self.catalog.get_child_objectives(self.objective.ident)

            self.catalog.add_child_objective(self.objective.ident, self.child_ids[0])

            children = self.catalog.get_child_objectives(self.objective.ident)
            assert children.available() == 1
            assert isinstance(children, ObjectiveList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_objective(self.fake_id, self.fake_id)

    def test_remove_child_objective(self):
        """Tests remove_child_objective"""
        if not is_never_authz(self.service_config):
            self.catalog.add_root_objective(self.objective.ident)
            self.catalog.add_child_objective(self.objective.ident, self.child_ids[0])

            children = self.catalog.get_child_objectives(self.objective.ident)
            assert children.available() == 1

            self.catalog.remove_child_objective(self.objective.ident, self.child_ids[0])

            with pytest.raises(errors.IllegalState):
                self.catalog.get_child_objectives(self.objective.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_objective(self.fake_id, self.fake_id)

    def test_remove_child_objectives(self):
        """Tests remove_child_objectives"""
        if not is_never_authz(self.service_config):
            self.catalog.add_root_objective(self.objective.ident)
            self.catalog.add_child_objective(self.objective.ident, self.child_ids[0])
            self.catalog.add_child_objective(self.objective.ident, self.child_ids[1])

            children = self.catalog.get_child_objectives(self.objective.ident)
            assert children.available() == 2

            self.catalog.remove_child_objectives(self.objective.ident)

            with pytest.raises(errors.IllegalState):
                self.catalog.get_child_objectives(self.objective.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_objectives(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_sequencing_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.child_list = list()
    request.cls.child_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveSequencingSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_sequencing_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_sequencing_session_test_fixture(request):
    request.cls.objective_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveSequencingSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_list.append(obj)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj_id in request.cls.child_ids:
                request.cls.catalog.delete_objective(obj_id)
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_sequencing_session_class_fixture", "objective_sequencing_session_test_fixture")
class TestObjectiveSequencingSession(object):
    """Tests for ObjectiveSequencingSession"""
    def test_get_objective_hierarchy_id(self):
        """Tests get_objective_hierarchy_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_hierarchy_id()

    def test_get_objective_hierarchy(self):
        """Tests get_objective_hierarchy"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_hierarchy()

    def test_can_sequence_objectives(self):
        """Tests can_sequence_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_sequence_objectives()

    def test_move_objective_ahead(self):
        """Tests move_objective_ahead"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.move_objective_ahead(True, True, True)

    def test_move_objective_behind(self):
        """Tests move_objective_behind"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.move_objective_behind(True, True, True)

    def test_sequence_objectives(self):
        """Tests sequence_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.sequence_objectives(True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_objective_bank_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.objective_list = list()
    request.cls.objective_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveObjectiveBankSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_list.append(obj)
            request.cls.objective_ids.append(obj.ident)
        request.cls.svc_mgr.assign_objective_to_objective_bank(
            request.cls.objective_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_objective_to_objective_bank(
            request.cls.objective_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_objective_from_objective_bank(
                request.cls.objective_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_objective_from_objective_bank(
                request.cls.objective_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_objective_bank_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("objective_objective_bank_session_class_fixture", "objective_objective_bank_session_test_fixture")
class TestObjectiveObjectiveBankSession(object):
    """Tests for ObjectiveObjectiveBankSession"""
    def test_can_lookup_objective_objective_bank_mappings(self):
        """Tests can_lookup_objective_objective_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_objective_objective_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_objective_ids_by_objective_bank(self):
        """Tests get_objective_ids_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_objective_ids_by_objective_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_ids_by_objective_bank(self.fake_id)

    def test_get_objectives_by_objective_bank(self):
        """Tests get_objectives_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_objectives_by_objective_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.ObjectiveList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_objectives_by_objective_bank(self.fake_id)

    def test_get_objective_ids_by_objective_banks(self):
        """Tests get_objective_ids_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_objective_ids_by_objective_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_objective_ids_by_objective_banks([self.fake_id])

    def test_get_objectives_by_objective_banks(self):
        """Tests get_objectives_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_objectives_by_objective_banks(catalog_ids)
            assert isinstance(results, ABCObjects.ObjectiveList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_objectives_by_objective_banks([self.fake_id])

    def test_get_objective_bank_ids_by_objective(self):
        """Tests get_objective_bank_ids_by_objective"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_objective_bank_ids_by_objective(self.objective_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_ids_by_objective(self.fake_id)

    def test_get_objective_banks_by_objective(self):
        """Tests get_objective_banks_by_objective"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_objective_banks_by_objective(self.objective_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_banks_by_objective(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_objective_bank_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.objective_list = list()
    request.cls.objective_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveObjectiveBankAssignmentSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.objective_list.append(obj)
            request.cls.objective_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_objective_bank_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("objective_objective_bank_assignment_session_class_fixture", "objective_objective_bank_assignment_session_test_fixture")
class TestObjectiveObjectiveBankAssignmentSession(object):
    """Tests for ObjectiveObjectiveBankAssignmentSession"""
    def test_can_assign_objectives(self):
        """Tests can_assign_objectives"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_objectives()
        assert isinstance(result, bool)

    def test_can_assign_objectives_to_objective_bank(self):
        """Tests can_assign_objectives_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_objectives_to_objective_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_objective_bank_ids(self):
        """Tests get_assignable_objective_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_objective_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_objective_bank_ids(self.fake_id)

    def test_get_assignable_objective_bank_ids_for_objective(self):
        """Tests get_assignable_objective_bank_ids_for_objective"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_objective_bank_ids_for_objective(self.catalog.ident, self.objective_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_objective_bank_ids_for_objective(self.fake_id, self.fake_id)

    def test_assign_objective_to_objective_bank(self):
        """Tests assign_objective_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_objectives()
            assert results.available() == 0
            self.session.assign_objective_to_objective_bank(self.objective_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_objectives()
            assert results.available() == 1
            self.session.unassign_objective_from_objective_bank(
                self.objective_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_objective_to_objective_bank(self.fake_id, self.fake_id)

    def test_unassign_objective_from_objective_bank(self):
        """Tests unassign_objective_from_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_objectives()
            assert results.available() == 0
            self.session.assign_objective_to_objective_bank(
                self.objective_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_objectives()
            assert results.available() == 1
            self.session.unassign_objective_from_objective_bank(
                self.objective_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_objectives()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_objective_from_objective_bank(self.fake_id, self.fake_id)

    def test_reassign_proficiency_to_objective_bank(self):
        """Tests reassign_proficiency_to_objective_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_proficiency_to_objective_bank(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_requisite_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.requisite_list = list()
    request.cls.requisite_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveRequisiteSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveRequisiteSession Lookup'
        create_form.description = 'Test Objective for ObjectiveRequisiteSession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveRequisiteSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.requisite_list.append(obj)
            request.cls.requisite_ids.append(obj.ident)
            request.cls.catalog.assign_objective_requisite(request.cls.objective.ident, obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_requisite_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj_id in request.cls.requisite_ids:
                    catalog.delete_objective(obj_id)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_requisite_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("objective_requisite_session_class_fixture", "objective_requisite_session_test_fixture")
class TestObjectiveRequisiteSession(object):
    """Tests for ObjectiveRequisiteSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_lookup_objective_prerequisites(self):
        """Tests can_lookup_objective_prerequisites"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_lookup_objective_prerequisites()

    def test_use_comparative_objective_view(self):
        """Tests use_comparative_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_objective_view()

    def test_use_plenary_objective_view(self):
        """Tests use_plenary_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_objective_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_requisite_objectives(self):
        """Tests get_requisite_objectives"""
        # From test_templates/learning.py::ObjectiveRequsiteSession::get_requisite_objectives_template
        if not is_never_authz(self.service_config):
            requisites = self.catalog.get_requisite_objectives(self.objective.ident)
            assert requisites.available() == len(self.requisite_ids)
            for req in requisites:
                assert req.ident in self.requisite_ids
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_requisite_objectives(self.fake_id)

    def test_get_all_requisite_objectives(self):
        """Tests get_all_requisite_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_all_requisite_objectives(True)

    def test_get_dependent_objectives(self):
        """Tests get_dependent_objectives"""
        # From test_templates/learning.py::ObjectiveRequsiteSession::get_dependent_objectives_template
        if not is_never_authz(self.service_config):
            dependents = self.catalog.get_dependent_objectives(self.objective.ident)
            assert dependents.available() == 0
            dependents = self.catalog.get_dependent_objectives(self.requisite_ids[0])
            assert dependents.available() == 1
            assert dependents.next().ident == self.objective.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_dependent_objectives(self.fake_id)

    def test_is_objective_required(self):
        """Tests is_objective_required"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_objective_required(True, True)

    def test_get_equivalent_objectives(self):
        """Tests get_equivalent_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_equivalent_objectives(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_requisite_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def objective_requisite_assignment_session_test_fixture(request):
    request.cls.requisite_list = list()
    request.cls.requisite_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveRequisiteAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveRequisiteAssignmentSession Lookup'
        create_form.description = 'Test Objective for ObjectiveRequisiteAssignmentSession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveRequisiteAssignmentSession tests'
            obj = request.cls.catalog.create_objective(create_form)
            request.cls.requisite_list.append(obj)
            request.cls.requisite_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_objective_requisite_assignment_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj_id in request.cls.requisite_ids:
                    catalog.delete_objective(obj_id)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_requisite_assignment_session_class_fixture", "objective_requisite_assignment_session_test_fixture")
class TestObjectiveRequisiteAssignmentSession(object):
    """Tests for ObjectiveRequisiteAssignmentSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_assign_requisites(self):
        """Tests can_assign_requisites"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_assign_requisites()

    def test_assign_objective_requisite(self):
        """Tests assign_objective_requisite"""
        # From test_templates/learning.py::ObjectiveRequsiteAssignmentSession::assign_objective_requisite_template
        if not is_never_authz(self.service_config):
            results = self.catalog.get_requisite_objectives(self.objective.ident)
            assert isinstance(results, ABCObjects.ObjectiveList)
            assert results.available() == 0

            self.catalog.assign_objective_requisite(self.objective.ident, self.requisite_ids[0])

            results = self.catalog.get_requisite_objectives(self.objective.ident)
            assert results.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.assign_objective_requisite(self.fake_id, self.fake_id)

    def test_unassign_objective_requisite(self):
        """Tests unassign_objective_requisite"""
        # From test_templates/learning.py::ObjectiveRequsiteAssignmentSession::unassign_objective_requisite_template
        if not is_never_authz(self.service_config):
            self.catalog.assign_objective_requisite(self.objective.ident, self.requisite_ids[0])

            results = self.catalog.get_requisite_objectives(self.objective.ident)
            assert results.available() == 1

            self.catalog.unassign_objective_requisite(self.objective.ident, self.requisite_ids[0])

            results = self.catalog.get_requisite_objectives(self.objective.ident)
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.unassign_objective_requisite(self.fake_id, self.fake_id)

    def test_assign_equivalent_objective(self):
        """Tests assign_equivalent_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.assign_equivalent_objective(True, True)

    def test_unassign_equivalent_objective(self):
        """Tests unassign_equivalent_objective"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.unassign_equivalent_objective(True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def activity_lookup_session_test_fixture(request):
    request.cls.activity_list = list()
    request.cls.activity_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityLookupSession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityLookupSession tests'
            obj = request.cls.catalog.create_activity(create_form)
            request.cls.activity_list.append(obj)
            request.cls.activity_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_activity_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_activities():
                    catalog.delete_activity(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("activity_lookup_session_class_fixture", "activity_lookup_session_test_fixture")
class TestActivityLookupSession(object):
    """Tests for ActivityLookupSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_lookup_activities(self):
        """Tests can_lookup_activities"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_activities(), bool)

    def test_use_comparative_activity_view(self):
        """Tests use_comparative_activity_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_activity_view()

    def test_use_plenary_activity_view(self):
        """Tests use_plenary_activity_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_activity_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_activity(self):
        """Tests get_activity"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_activity_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_objective_bank_view()
                obj = self.catalog.get_activity(self.activity_list[0].ident)
                assert obj.ident == self.activity_list[0].ident
                self.catalog.use_federated_objective_bank_view()
                obj = self.catalog.get_activity(self.activity_list[0].ident)
                assert obj.ident == self.activity_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_activity(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_objective_bank_view()
                obj = self.catalog.get_activity(self.activity_list[0].ident)
                assert obj.ident == self.activity_list[0].ident
                self.catalog.use_federated_objective_bank_view()
                obj = self.catalog.get_activity(self.activity_list[0].ident)
                assert obj.ident == self.activity_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_activity(self.fake_id)

    def test_get_activities_by_ids(self):
        """Tests get_activities_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        if self.svc_mgr.supports_activity_query():
            objects = self.catalog.get_activities_by_ids(self.activity_ids)
            assert isinstance(objects, ActivityList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_activities_by_ids(self.activity_ids)
            assert isinstance(objects, ActivityList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_activities_by_ids(self.activity_ids)
                assert isinstance(objects, ActivityList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_activities_by_ids(self.activity_ids)
                assert objects.available() > 0
                assert isinstance(objects, ActivityList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_activities_by_ids(self.activity_ids)

    def test_get_activities_by_genus_type(self):
        """Tests get_activities_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        if self.svc_mgr.supports_activity_query():
            objects = self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ActivityList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ActivityList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ActivityList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, ActivityList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_activities_by_parent_genus_type(self):
        """Tests get_activities_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        if self.svc_mgr.supports_activity_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ActivityList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ActivityList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ActivityList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ActivityList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_activities_by_record_type(self):
        """Tests get_activities_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        if self.svc_mgr.supports_activity_query():
            objects = self.catalog.get_activities_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, ActivityList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_activities_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, ActivityList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_activities_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, ActivityList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_activities_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ActivityList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_activities_by_record_type(DEFAULT_TYPE)

    def test_get_activities_for_objective(self):
        """Tests get_activities_for_objective"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        if self.svc_mgr.supports_activity_query():
            results = self.session.get_activities_for_objective(self.objective.ident)
            assert isinstance(results, ABCObjects.ActivityList)
            if not is_never_authz(self.service_config):
                assert results.available() == 2
            else:
                assert results.available() == 0
        else:
            if not is_never_authz(self.service_config):
                results = self.session.get_activities_for_objective(self.objective.ident)
                assert results.available() == 2
                assert isinstance(results, ABCObjects.ActivityList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.session.get_activities_for_objective(self.fake_id)

    def test_get_activities_for_objectives(self):
        """Tests get_activities_for_objectives"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_activities_for_objectives(True)

    def test_get_activities_by_asset(self):
        """Tests get_activities_by_asset"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_activities_by_asset(True)

    def test_get_activities_by_assets(self):
        """Tests get_activities_by_assets"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_activities_by_assets(True)

    def test_get_activities(self):
        """Tests get_activities"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        if self.svc_mgr.supports_activity_query():
            objects = self.catalog.get_activities()
            assert isinstance(objects, ActivityList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_activities()
            assert isinstance(objects, ActivityList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_activities()
                assert isinstance(objects, ActivityList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_activities()
                assert objects.available() > 0
                assert isinstance(objects, ActivityList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_activities()

    def test_get_activity_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_activity(self.activity_ids[0], ALIAS_ID)
            obj = self.catalog.get_activity(ALIAS_ID)
            assert obj.get_id() == self.activity_ids[0]


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def activity_query_session_test_fixture(request):
    request.cls.activity_list = list()
    request.cls.activity_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Assignment'
        create_form.description = 'Test Objective for ProficiencyObjectiveBankAssignmentSession tests assignment'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + color
            create_form.description = (
                'Test Activity for ActivityQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_activity(create_form)
            request.cls.activity_list.append(obj)
            request.cls.activity_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_activity_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_activities():
                request.cls.catalog.delete_activity(obj.ident)
            request.cls.catalog.delete_objective(request.cls.objective.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("activity_query_session_class_fixture", "activity_query_session_test_fixture")
class TestActivityQuerySession(object):
    """Tests for ActivityQuerySession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_search_activities(self):
        """Tests can_search_activities"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_activities(), bool)

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_activity_query(self):
        """Tests get_activity_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_activity_query()
        assert isinstance(query, ABCQueries.ActivityQuery)

    def test_get_activities_by_query(self):
        """Tests get_activities_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_activity_query()
            query.match_display_name('orange')
            assert self.catalog.get_activities_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_activities_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_activities_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.activity_list = list()
    request.cls.activity_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Admin'
        create_form.description = 'Test Objective for ActivityAdminSession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        request.cls.parent_object = request.cls.objective
        for num in [0, 1]:
            create_form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityAdminSession tests'
            obj = request.cls.catalog.create_activity(create_form)
            request.cls.activity_list.append(obj)
            request.cls.activity_ids.append(obj.ident)

        request.cls.form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
        request.cls.form.display_name = 'new Activity'
        request.cls.form.description = 'description of Activity'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_activity(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_activity_admin_session(proxy=PROXY)

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
def activity_admin_session_test_fixture(request):
    pass


@pytest.mark.usefixtures("activity_admin_session_class_fixture", "activity_admin_session_test_fixture")
class TestActivityAdminSession(object):
    """Tests for ActivityAdminSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_create_activities(self):
        """Tests can_create_activities"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_activities(), bool)

    def test_can_create_activity_with_record_types(self):
        """Tests can_create_activity_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_activity_with_record_types(DEFAULT_TYPE), bool)

    def test_get_activity_form_for_create(self):
        """Tests get_activity_form_for_create"""
        # From test_templates/learning.py::ActivityAdminSession::get_activity_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_activity_form_for_create(self.parent_object.ident, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_activity_form_for_create(self.fake_id, [])

    def test_create_activity(self):
        """Tests create_activity"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.learning.objects import Activity
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Activity)
            assert self.osid_object.display_name.text == 'new Activity'
            assert self.osid_object.description.text == 'description of Activity'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_activity(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_activity('I Will Break You!')
            update_form = self.catalog.get_activity_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_activity(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_activity('foo')

    def test_can_update_activities(self):
        """Tests can_update_activities"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_activities(), bool)

    def test_get_activity_form_for_update(self):
        """Tests get_activity_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_activity_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_activity_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_activity_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='learning.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_activity_form_for_update(self.fake_id)

    def test_update_activity(self):
        """Tests update_activity"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.learning.objects import Activity
            form = self.catalog.get_activity_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_activity(form)
            assert isinstance(updated_object, Activity)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_activity(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_activity('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_activity(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_activity('foo')

    def test_can_delete_activities(self):
        """Tests can_delete_activities"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_activities(), bool)

    def test_delete_activity(self):
        """Tests delete_activity"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_activity_form_for_create(self.parent_object.ident, [])
            form.display_name = 'new Activity'
            form.description = 'description of Activity'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_activity(form)
            self.catalog.delete_activity(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_activity(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_activity(self.fake_id)

    def test_can_manage_activity_aliases(self):
        """Tests can_manage_activity_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_activity_aliases(), bool)

    def test_alias_activity(self):
        """Tests alias_activity"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_activity(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_activity(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_activity(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_objective_bank_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.activity_list = list()
    request.cls.activity_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ActivIty Lookup'
        create_form.description = 'Test Objective for ActivityLookupSession tests'
        request.cls.objective = request.cls.catalog.create_objective(create_form)

        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityObjectiveBankSession tests'
            obj = request.cls.catalog.create_activity(create_form)
            request.cls.activity_list.append(obj)
            request.cls.activity_ids.append(obj.ident)
        request.cls.svc_mgr.assign_activity_to_objective_bank(
            request.cls.activity_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_activity_to_objective_bank(
            request.cls.activity_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_activity_from_objective_bank(
                request.cls.activity_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_activity_from_objective_bank(
                request.cls.activity_ids[2], request.cls.assigned_catalog.ident)
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_activities():
                    catalog.delete_activity(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_objective_bank_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("activity_objective_bank_session_class_fixture", "activity_objective_bank_session_test_fixture")
class TestActivityObjectiveBankSession(object):
    """Tests for ActivityObjectiveBankSession"""
    def test_can_lookup_activity_objective_bank_mappings(self):
        """Tests can_lookup_activity_objective_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_activity_objective_bank_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_activity_ids_by_objective_bank(self):
        """Tests get_activity_ids_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_activity_ids_by_objective_bank(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_activity_ids_by_objective_bank(self.fake_id)

    def test_get_activities_by_objective_bank(self):
        """Tests get_activities_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_activities_by_objective_bank(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.ActivityList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_activities_by_objective_bank(self.fake_id)

    def test_get_activity_ids_by_objective_banks(self):
        """Tests get_activity_ids_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_activity_ids_by_objective_banks(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_activity_ids_by_objective_banks([self.fake_id])

    def test_get_activities_by_objective_banks(self):
        """Tests get_activities_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_activities_by_objective_banks(catalog_ids)
            assert isinstance(results, ABCObjects.ActivityList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_activities_by_objective_banks([self.fake_id])

    def test_get_objective_bank_ids_by_activity(self):
        """Tests get_objective_bank_ids_by_activity"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_objective_bank_ids_by_activity(self.activity_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_ids_by_activity(self.fake_id)

    def test_get_objective_banks_by_activity(self):
        """Tests get_objective_banks_by_activity"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_objective_banks_by_activity(self.activity_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_banks_by_activity(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_objective_bank_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.activity_list = list()
    request.cls.activity_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Assignment'
        create_form.description = 'Test Objective for ActivityObjectiveBankAssignmentSession tests assignment'
        request.cls.objective = request.cls.catalog.create_objective(create_form)

        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_activity_form_for_create(request.cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityObjectiveBankAssignmentSession tests'
            obj = request.cls.catalog.create_activity(create_form)
            request.cls.activity_list.append(obj)
            request.cls.activity_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_activities():
                request.cls.catalog.delete_activity(obj.ident)
            for obj in request.cls.catalog.get_objectives():
                request.cls.catalog.delete_objective(obj.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_objective_bank_assignment_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("activity_objective_bank_assignment_session_class_fixture", "activity_objective_bank_assignment_session_test_fixture")
class TestActivityObjectiveBankAssignmentSession(object):
    """Tests for ActivityObjectiveBankAssignmentSession"""
    def test_can_assign_activities(self):
        """Tests can_assign_activities"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_activities()
        assert isinstance(result, bool)

    def test_can_assign_activities_to_objective_bank(self):
        """Tests can_assign_activities_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_activities_to_objective_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_objective_bank_ids(self):
        """Tests get_assignable_objective_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_objective_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_objective_bank_ids(self.fake_id)

    def test_get_assignable_objective_bank_ids_for_activity(self):
        """Tests get_assignable_objective_bank_ids_for_activity"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_objective_bank_ids_for_activity(self.catalog.ident, self.activity_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_objective_bank_ids_for_activity(self.fake_id, self.fake_id)

    def test_assign_activity_to_objective_bank(self):
        """Tests assign_activity_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_activities()
            assert results.available() == 0
            self.session.assign_activity_to_objective_bank(self.activity_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_activities()
            assert results.available() == 1
            self.session.unassign_activity_from_objective_bank(
                self.activity_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_activity_to_objective_bank(self.fake_id, self.fake_id)

    def test_unassign_activity_from_objective_bank(self):
        """Tests unassign_activity_from_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_activities()
            assert results.available() == 0
            self.session.assign_activity_to_objective_bank(
                self.activity_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_activities()
            assert results.available() == 1
            self.session.unassign_activity_from_objective_bank(
                self.activity_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_activities()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_activity_from_objective_bank(self.fake_id, self.fake_id)

    def test_reassign_activity_to_objective_bank(self):
        """Tests reassign_activity_to_objective_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_activity_to_objective_bank(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def proficiency_lookup_session_test_fixture(request):
    request.cls.proficiency_list = list()
    request.cls.proficiency_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        objective = request.cls.catalog.create_objective(form)

        for color in ['Orange', 'Blue']:
            create_form = request.cls.catalog.get_proficiency_form_for_create(objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + color
            create_form.description = (
                'Test Proficiency for ProficiencyLookupSession tests, did I mention green')
            obj = request.cls.catalog.create_proficiency(create_form)
            request.cls.proficiency_list.append(obj)
            request.cls.proficiency_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_proficiency_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_proficiencies():
                    catalog.delete_proficiency(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("proficiency_lookup_session_class_fixture", "proficiency_lookup_session_test_fixture")
class TestProficiencyLookupSession(object):
    """Tests for ProficiencyLookupSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_lookup_proficiencies(self):
        """Tests can_lookup_proficiencies"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_proficiencies(), bool)

    def test_use_comparative_proficiency_view(self):
        """Tests use_comparative_proficiency_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_proficiency_view()

    def test_use_plenary_proficiency_view(self):
        """Tests use_plenary_proficiency_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_proficiency_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_use_effective_proficiency_view(self):
        """Tests use_effective_proficiency_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_effective_proficiency_view()

    def test_use_any_effective_proficiency_view(self):
        """Tests use_any_effective_proficiency_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_any_effective_proficiency_view()

    def test_get_proficiency(self):
        """Tests get_proficiency"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_proficiency_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_objective_bank_view()
                obj = self.catalog.get_proficiency(self.proficiency_list[0].ident)
                assert obj.ident == self.proficiency_list[0].ident
                self.catalog.use_federated_objective_bank_view()
                obj = self.catalog.get_proficiency(self.proficiency_list[0].ident)
                assert obj.ident == self.proficiency_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_proficiency(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_objective_bank_view()
                obj = self.catalog.get_proficiency(self.proficiency_list[0].ident)
                assert obj.ident == self.proficiency_list[0].ident
                self.catalog.use_federated_objective_bank_view()
                obj = self.catalog.get_proficiency(self.proficiency_list[0].ident)
                assert obj.ident == self.proficiency_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_proficiency(self.fake_id)

    def test_get_proficiencies_by_ids(self):
        """Tests get_proficiencies_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        if self.svc_mgr.supports_proficiency_query():
            objects = self.catalog.get_proficiencies_by_ids(self.proficiency_ids)
            assert isinstance(objects, ProficiencyList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_proficiencies_by_ids(self.proficiency_ids)
            assert isinstance(objects, ProficiencyList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_proficiencies_by_ids(self.proficiency_ids)
                assert isinstance(objects, ProficiencyList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_proficiencies_by_ids(self.proficiency_ids)
                assert objects.available() > 0
                assert isinstance(objects, ProficiencyList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_proficiencies_by_ids(self.proficiency_ids)

    def test_get_proficiencies_by_genus_type(self):
        """Tests get_proficiencies_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        if self.svc_mgr.supports_proficiency_query():
            objects = self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ProficiencyList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ProficiencyList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ProficiencyList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, ProficiencyList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_proficiencies_by_parent_genus_type(self):
        """Tests get_proficiencies_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        if self.svc_mgr.supports_proficiency_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ProficiencyList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ProficiencyList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ProficiencyList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ProficiencyList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_proficiencies_by_record_type(self):
        """Tests get_proficiencies_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        if self.svc_mgr.supports_proficiency_query():
            objects = self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, ProficiencyList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, ProficiencyList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, ProficiencyList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ProficiencyList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)

    def test_get_proficiencies_on_date(self):
        """Tests get_proficiencies_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_on_date(True, True)

    def test_get_proficiencies_by_genus_type_on_date(self):
        """Tests get_proficiencies_by_genus_type_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_by_genus_type_on_date(True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_for_objective(self):
        """Tests get_proficiencies_for_objective"""
        pass

    def test_get_proficiencies_for_objective_on_date(self):
        """Tests get_proficiencies_for_objective_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_for_objective_on_date(True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_by_genus_type_for_objective(self):
        """Tests get_proficiencies_by_genus_type_for_objective"""
        pass

    def test_get_proficiencies_by_genus_type_for_objective_on_date(self):
        """Tests get_proficiencies_by_genus_type_for_objective_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_by_genus_type_for_objective_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_for_objectives(self):
        """Tests get_proficiencies_for_objectives"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_for_resource(self):
        """Tests get_proficiencies_for_resource"""
        pass

    def test_get_proficiencies_for_resource_on_date(self):
        """Tests get_proficiencies_for_resource_on_date"""
        # From test_templates/relationship.py::RelationshipLookupSession::get_relationships_for_source_on_date_template
        if not is_never_authz(self.service_config):
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

            # NOTE: this first argument will probably break in many of the other methods,
            #   since it's not clear they always use something like AGENT_ID
            # i.e. in get_grade_entries_for_gradebook_column_on_date it needs to be
            #   a gradebookColumnId.
            results = self.session.get_proficiencies_for_resource_on_date(AGENT_ID, DateTime.utcnow(), end_date)
            assert isinstance(results, ABCObjects.ProficiencyList)
            assert results.available() == 2

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_by_genus_type_for_resource(self):
        """Tests get_proficiencies_by_genus_type_for_resource"""
        pass

    def test_get_proficiencies_by_genus_type_for_resource_on_date(self):
        """Tests get_proficiencies_by_genus_type_for_resource_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_by_genus_type_for_resource_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_for_resources(self):
        """Tests get_proficiencies_for_resources"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_for_objective_and_resource(self):
        """Tests get_proficiencies_for_objective_and_resource"""
        pass

    def test_get_proficiencies_for_objective_and_resource_on_date(self):
        """Tests get_proficiencies_for_objective_and_resource_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_for_objective_and_resource_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies_by_genus_type_for_objective_and_resource(self):
        """Tests get_proficiencies_by_genus_type_for_objective_and_resource"""
        pass

    def test_get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self):
        """Tests get_proficiencies_by_genus_type_for_objective_and_resource_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_proficiencies_by_genus_type_for_objective_and_resource_on_date(True, True, True, True, True)

    def test_get_proficiencies(self):
        """Tests get_proficiencies"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        if self.svc_mgr.supports_proficiency_query():
            objects = self.catalog.get_proficiencies()
            assert isinstance(objects, ProficiencyList)
            self.catalog.use_federated_objective_bank_view()
            objects = self.catalog.get_proficiencies()
            assert isinstance(objects, ProficiencyList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_proficiencies()
                assert isinstance(objects, ProficiencyList)
                self.catalog.use_federated_objective_bank_view()
                objects = self.catalog.get_proficiencies()
                assert objects.available() > 0
                assert isinstance(objects, ProficiencyList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_proficiencies()

    def test_get_proficiency_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_proficiency(self.proficiency_ids[0], ALIAS_ID)
            obj = self.catalog.get_proficiency(ALIAS_ID)
            assert obj.get_id() == self.proficiency_ids[0]


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def proficiency_query_session_test_fixture(request):
    request.cls.proficiency_list = list()
    request.cls.proficiency_ids = list()
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        objective = request.cls.catalog.create_objective(form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_proficiency_form_for_create(objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + color
            create_form.description = (
                'Test Proficiency for ProficiencyQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_proficiency(create_form)
            request.cls.proficiency_list.append(obj)
            request.cls.proficiency_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_proficiency_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_proficiencies():
                    catalog.delete_proficiency(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("proficiency_query_session_class_fixture", "proficiency_query_session_test_fixture")
class TestProficiencyQuerySession(object):
    """Tests for ProficiencyQuerySession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_search_proficiencies(self):
        """Tests can_search_proficiencies"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_proficiencies(), bool)

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_proficiency_query(self):
        """Tests get_proficiency_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_proficiency_query()
        assert isinstance(query, ABCQueries.ProficiencyQuery)

    def test_get_proficiencies_by_query(self):
        """Tests get_proficiencies_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_proficiency_query()
            query.match_display_name('orange')
            assert self.catalog.get_proficiencies_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_proficiencies_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_proficiencies_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.proficiency_list = list()
    request.cls.proficiency_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('objective.objective%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

        form = request.cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        request.cls.objective = request.cls.catalog.create_objective(form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + color
            create_form.description = (
                'Test Proficiency for ProficiencyLookupSession tests, did I mention green')
            obj = request.cls.catalog.create_proficiency(create_form)
            request.cls.proficiency_list.append(obj)
            request.cls.proficiency_ids.append(obj.ident)

        request.cls.form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident, AGENT_ID, [])
        request.cls.form.display_name = 'new Proficiency'
        request.cls.form.description = 'description of Proficiency'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_proficiency(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_proficiency_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                for obj in catalog.get_proficiencies():
                    catalog.delete_proficiency(obj.ident)
                for obj in catalog.get_objectives():
                    catalog.delete_objective(obj.ident)
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_admin_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("proficiency_admin_session_class_fixture", "proficiency_admin_session_test_fixture")
class TestProficiencyAdminSession(object):
    """Tests for ProficiencyAdminSession"""
    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_objective_bank_id() == self.catalog.ident

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_objective_bank(), ABCObjectiveBank)

    def test_can_create_proficiencies(self):
        """Tests can_create_proficiencies"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_proficiencies(), bool)

    def test_can_create_proficiency_with_record_types(self):
        """Tests can_create_proficiency_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_proficiency_with_record_types(DEFAULT_TYPE), bool)

    def test_get_proficiency_form_for_create(self):
        """Tests get_proficiency_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_proficiency_form_for_create(self.objective.ident, AGENT_ID, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_proficiency_form_for_create(self.fake_id, AGENT_ID, [])

    def test_create_proficiency(self):
        """Tests create_proficiency"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.learning.objects import Proficiency
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Proficiency)
            assert self.osid_object.display_name.text == 'new Proficiency'
            assert self.osid_object.description.text == 'description of Proficiency'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_proficiency(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_proficiency('I Will Break You!')
            update_form = self.catalog.get_proficiency_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_proficiency(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_proficiency('foo')

    def test_can_update_proficiencies(self):
        """Tests can_update_proficiencies"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_proficiencies(), bool)

    def test_get_proficiency_form_for_update(self):
        """Tests get_proficiency_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_proficiency_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_proficiency_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_proficiency_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='learning.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_proficiency_form_for_update(self.fake_id)

    def test_update_proficiency(self):
        """Tests update_proficiency"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.learning.objects import Proficiency
            form = self.catalog.get_proficiency_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_proficiency(form)
            assert isinstance(updated_object, Proficiency)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_proficiency(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_proficiency('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_proficiency(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_proficiency('foo')

    def test_can_delete_proficiencies(self):
        """Tests can_delete_proficiencies"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_proficiencies(), bool)

    def test_delete_proficiency(self):
        """Tests delete_proficiency"""
        if not is_never_authz(self.service_config):
            create_form = self.catalog.get_proficiency_form_for_create(self.objective.ident, AGENT_ID, [])
            create_form.display_name = 'new Proficiency'
            create_form.description = 'description of Proficiency'
            create_form.genus_type = NEW_TYPE
            osid_object = self.catalog.create_proficiency(create_form)
            self.catalog.delete_proficiency(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_proficiency(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_proficiency(self.fake_id)

    def test_delete_proficiencies(self):
        """Tests delete_proficiencies"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.delete_proficiencies()

    def test_can_manage_proficiency_aliases(self):
        """Tests can_manage_proficiency_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_proficiency_aliases(), bool)

    def test_alias_proficiency(self):
        """Tests alias_proficiency"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_proficiency(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_proficiency(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_proficiency(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_objective_bank_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.proficiency_list = list()
    request.cls.proficiency_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyObjectiveBankAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ProficiencyObjectiveBankAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        create_form = request.cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Assignment'
        create_form.description = 'Test Objective for ProficiencyObjectiveBankAssignmentSession tests assignment'
        request.cls.objective = request.cls.catalog.create_objective(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_proficiency_form_for_create(request.cls.objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + str(num)
            create_form.description = 'Test Proficiency for ProficiencyObjectiveBankAssignmentSession tests'
            obj = request.cls.catalog.create_proficiency(create_form)
            request.cls.proficiency_list.append(obj)
            request.cls.proficiency_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_proficiencies():
                request.cls.catalog.delete_proficiency(obj.ident)
            request.cls.catalog.delete_objective(request.cls.objective.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_objective_bank_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("proficiency_objective_bank_assignment_session_class_fixture", "proficiency_objective_bank_assignment_session_test_fixture")
class TestProficiencyObjectiveBankAssignmentSession(object):
    """Tests for ProficiencyObjectiveBankAssignmentSession"""
    def test_can_assign_proficiencies(self):
        """Tests can_assign_proficiencies"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_proficiencies()
        assert isinstance(result, bool)

    def test_can_assign_proficiencies_to_objective_bank(self):
        """Tests can_assign_proficiencies_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_proficiencies_to_objective_bank(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_objective_bank_ids(self):
        """Tests get_assignable_objective_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_objective_bank_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_objective_bank_ids(self.fake_id)

    def test_get_assignable_objective_bank_ids_for_proficiency(self):
        """Tests get_assignable_objective_bank_ids_for_proficiency"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_objective_bank_ids_for_proficiency(self.catalog.ident, self.proficiency_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_objective_bank_ids_for_proficiency(self.fake_id, self.fake_id)

    def test_assign_proficiency_to_objective_bank(self):
        """Tests assign_proficiency_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_proficiencies()
            assert results.available() == 0
            self.session.assign_proficiency_to_objective_bank(self.proficiency_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_proficiencies()
            assert results.available() == 1
            self.session.unassign_proficiency_from_objective_bank(
                self.proficiency_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_proficiency_to_objective_bank(self.fake_id, self.fake_id)

    def test_unassign_proficiency_from_objective_bank(self):
        """Tests unassign_proficiency_from_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_proficiencies()
            assert results.available() == 0
            self.session.assign_proficiency_to_objective_bank(
                self.proficiency_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_proficiencies()
            assert results.available() == 1
            self.session.unassign_proficiency_from_objective_bank(
                self.proficiency_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_proficiencies()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_proficiency_from_objective_bank(self.fake_id, self.fake_id)

    def test_reassign_proficiency_to_objective_bank(self):
        """Tests reassign_proficiency_to_objective_bank"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_proficiency_to_objective_bank(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for learning proxy manager tests'
            catalog = request.cls.svc_mgr.create_objective_bank(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("objective_bank_lookup_session_class_fixture", "objective_bank_lookup_session_test_fixture")
class TestObjectiveBankLookupSession(object):
    """Tests for ObjectiveBankLookupSession"""
    def test_can_lookup_objective_banks(self):
        """Tests can_lookup_objective_banks"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_objective_banks(), bool)

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_objective_bank(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank(self.fake_id)

    def test_get_objective_banks_by_ids(self):
        """Tests get_objective_banks_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_objective_banks_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.ObjectiveBankList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_banks_by_ids([self.fake_id])

    def test_get_objective_banks_by_genus_type(self):
        """Tests get_objective_banks_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_objective_banks_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.ObjectiveBankList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_banks_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_objective_banks_by_parent_genus_type(self):
        """Tests get_objective_banks_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_banks_by_parent_genus_type(True)

    def test_get_objective_banks_by_record_type(self):
        """Tests get_objective_banks_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_banks_by_record_type(True)

    def test_get_objective_banks_by_provider(self):
        """Tests get_objective_banks_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_objective_banks_by_provider(True)

    def test_get_objective_banks(self):
        """Tests get_objective_banks"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_objective_banks()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.ObjectiveBankList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_banks()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def objective_bank_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank For Deletion'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_objective_bank(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_objective_banks():
                request.cls.svc_mgr.delete_objective_bank(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("objective_bank_admin_session_class_fixture", "objective_bank_admin_session_test_fixture")
class TestObjectiveBankAdminSession(object):
    """Tests for ObjectiveBankAdminSession"""
    def test_can_create_objective_banks(self):
        """Tests can_create_objective_banks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_objective_banks(), bool)

    def test_can_create_objective_bank_with_record_types(self):
        """Tests can_create_objective_bank_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_objective_bank_with_record_types(DEFAULT_TYPE), bool)

    def test_get_objective_bank_form_for_create(self):
        """Tests get_objective_bank_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_objective_bank_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_objective_bank_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_form_for_create([])

    def test_create_objective_bank(self):
        """Tests create_objective_bank"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBank
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_objective_bank_form_for_create([])
            catalog_form.display_name = 'Test ObjectiveBank'
            catalog_form.description = 'Test ObjectiveBank for ObjectiveBankAdminSession.create_objective_bank tests'
            new_catalog = self.svc_mgr.create_objective_bank(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_objective_bank(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_objective_bank('I Will Break You!')
            update_form = self.svc_mgr.get_objective_bank_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_objective_bank(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_objective_bank('foo')

    def test_can_update_objective_banks(self):
        """Tests can_update_objective_banks"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_objective_banks(), bool)

    def test_get_objective_bank_form_for_update(self):
        """Tests get_objective_bank_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_objective_bank_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_form_for_update(self.fake_id)

    def test_update_objective_bank(self):
        """Tests update_objective_bank"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_objective_bank_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_objective_bank(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_objective_bank('foo')

    def test_can_delete_objective_banks(self):
        """Tests can_delete_objective_banks"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_objective_banks(), bool)

    def test_delete_objective_bank(self):
        """Tests delete_objective_bank"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_objective_bank(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_objective_bank(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_objective_bank(self.fake_id)

    def test_can_manage_objective_bank_aliases(self):
        """Tests can_manage_objective_bank_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_objective_bank_aliases(), bool)

    def test_alias_objective_bank(self):
        """Tests alias_objective_bank"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('learning.ObjectiveBank%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_objective_bank(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_objective_bank(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_objective_bank(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test ObjectiveBank ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_objective_bank(create_form)
        request.cls.svc_mgr.add_root_objective_bank(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_objective_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_objective_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_objective_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_objective_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_objective_banks(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_objective_bank(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_objective_bank(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("objective_bank_hierarchy_session_class_fixture", "objective_bank_hierarchy_session_test_fixture")
class TestObjectiveBankHierarchySession(object):
    """Tests for ObjectiveBankHierarchySession"""
    def test_get_objective_bank_hierarchy_id(self):
        """Tests get_objective_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_objective_bank_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_objective_bank_hierarchy(self):
        """Tests get_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_objective_bank_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_hierarchy()

    def test_can_access_objective_bank_hierarchy(self):
        """Tests can_access_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_objective_bank_hierarchy(), bool)

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_root_objective_bank_ids(self):
        """Tests get_root_objective_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_objective_bank_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_objective_bank_ids()

    def test_get_root_objective_banks(self):
        """Tests get_root_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_objective_banks()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_objective_banks()

    def test_has_parent_objective_banks(self):
        """Tests has_parent_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_objective_banks(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_objective_banks(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_objective_banks(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_objective_banks(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_objective_banks(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_objective_banks(self.fake_id)

    def test_is_parent_of_objective_bank(self):
        """Tests is_parent_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_objective_bank(self.fake_id, self.fake_id)

    def test_get_parent_objective_bank_ids(self):
        """Tests get_parent_objective_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_objective_bank_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_objective_bank_ids(self.fake_id)

    def test_get_parent_objective_banks(self):
        """Tests get_parent_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_objective_banks(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_objective_banks(self.fake_id)

    def test_is_ancestor_of_objective_bank(self):
        """Tests is_ancestor_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_objective_bank,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_objective_bank(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_objective_banks(self):
        """Tests has_child_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_objective_banks(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_objective_banks(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_objective_banks(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_objective_banks(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_objective_banks(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_objective_banks(self.fake_id)

    def test_is_child_of_objective_bank(self):
        """Tests is_child_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_objective_bank(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_objective_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_objective_bank(self.fake_id, self.fake_id)

    def test_get_child_objective_bank_ids(self):
        """Tests get_child_objective_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_objective_bank_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_objective_bank_ids(self.fake_id)

    def test_get_child_objective_banks(self):
        """Tests get_child_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_objective_banks(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_objective_banks(self.fake_id)

    def test_is_descendant_of_objective_bank(self):
        """Tests is_descendant_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_objective_bank,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_objective_bank(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_objective_bank_node_ids(self):
        """Tests get_objective_bank_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_objective_bank_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_node_ids(self.fake_id, 1, 2, False)

    def test_get_objective_bank_nodes(self):
        """Tests get_objective_bank_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_objective_bank_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test ObjectiveBank ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_objective_bank(create_form)
        request.cls.svc_mgr.add_root_objective_bank(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_objective_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_objective_bank(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_objective_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_objective_bank(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_objective_banks(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_objective_bank(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("objective_bank_hierarchy_design_session_class_fixture", "objective_bank_hierarchy_design_session_test_fixture")
class TestObjectiveBankHierarchyDesignSession(object):
    """Tests for ObjectiveBankHierarchyDesignSession"""
    def test_get_objective_bank_hierarchy_id(self):
        """Tests get_objective_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_objective_bank_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_objective_bank_hierarchy(self):
        """Tests get_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_objective_bank_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_objective_bank_hierarchy()

    def test_can_modify_objective_bank_hierarchy(self):
        """Tests can_modify_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_objective_bank_hierarchy(), bool)

    def test_add_root_objective_bank(self):
        """Tests add_root_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_objective_banks()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_objective_bank(self.fake_id)

    def test_remove_root_objective_bank(self):
        """Tests remove_root_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_objective_banks()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test ObjectiveBank root'
            new_objective_bank = self.svc_mgr.create_objective_bank(create_form)
            self.svc_mgr.add_root_objective_bank(new_objective_bank.ident)

            roots = self.session.get_root_objective_banks()
            assert roots.available() == 2

            self.session.remove_root_objective_bank(new_objective_bank.ident)

            roots = self.session.get_root_objective_banks()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_objective_bank(self.fake_id)

    def test_add_child_objective_bank(self):
        """Tests add_child_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_objective_bank(self.fake_id, self.fake_id)

    def test_remove_child_objective_bank(self):
        """Tests remove_child_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test ObjectiveBank child'
            new_objective_bank = self.svc_mgr.create_objective_bank(create_form)
            self.svc_mgr.add_child_objective_bank(
                self.catalogs['Root'].ident,
                new_objective_bank.ident)

            children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_objective_bank(
                self.catalogs['Root'].ident,
                new_objective_bank.ident)

            children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_objective_bank(self.fake_id, self.fake_id)

    def test_remove_child_objective_banks(self):
        """Tests remove_child_objective_banks"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_objective_banks(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test ObjectiveBank child'
            new_objective_bank = self.svc_mgr.create_objective_bank(create_form)
            self.svc_mgr.add_child_objective_bank(
                self.catalogs['Grandchild 1'].ident,
                new_objective_bank.ident)

            children = self.session.get_child_objective_banks(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_objective_banks(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_objective_banks(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_objective_banks(self.fake_id)
