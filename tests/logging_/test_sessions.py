"""Unit tests of logging sessions."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.logging_ import objects as ABCObjects
from dlkit.abstract_osid.logging_ import queries as ABCQueries
from dlkit.abstract_osid.logging_.objects import Log as ABCLog
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
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
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def logging_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log For Deletion'
        create_form.description = 'Test Log for LogAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_log(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_logs():
                request.cls.svc_mgr.delete_log(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def logging_session_test_fixture(request):
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("logging_session_class_fixture", "logging_session_test_fixture")
class TestLoggingSession(object):
    """Tests for LoggingSession"""
    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_log_id() == self.catalog.ident

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_log(), ABCLog)

    def test_can_log(self):
        """Tests can_log"""
        assert isinstance(self.session.can_log(), bool)

    def test_log(self):
        """Tests log"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.log(True, True)

    def test_log_at_priority(self):
        """Tests log_at_priority"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.log_at_priority(True, True, True)

    def test_get_log_entry_form(self):
        """Tests get_log_entry_form"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entry_form()

    def test_create_log_entry(self):
        """Tests create_log_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.create_log_entry(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def log_entry_lookup_session_test_fixture(request):
    request.cls.log_entry_list = list()
    request.cls.log_entry_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + str(num)
            create_form.description = 'Test LogEntry for LogEntryLookupSession tests'
            obj = request.cls.catalog.create_log_entry(create_form)
            request.cls.log_entry_list.append(obj)
            request.cls.log_entry_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_log_entry_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("log_entry_lookup_session_class_fixture", "log_entry_lookup_session_test_fixture")
class TestLogEntryLookupSession(object):
    """Tests for LogEntryLookupSession"""
    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_log_id() == self.catalog.ident

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_log(), ABCLog)

    def test_can_read_log(self):
        """Tests can_read_log"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_read_log(), bool)

    def test_use_comparative_log_entry_view(self):
        """Tests use_comparative_log_entry_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_log_entry_view()

    def test_use_plenary_log_entry_view(self):
        """Tests use_plenary_log_entry_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_log_entry_view()

    def test_use_federated_log_view(self):
        """Tests use_federated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_log_view()

    def test_use_isolated_log_view(self):
        """Tests use_isolated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_log_view()

    def test_get_log_entry(self):
        """Tests get_log_entry"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_log_view()
            obj = self.catalog.get_log_entry(self.log_entry_list[0].ident)
            assert obj.ident == self.log_entry_list[0].ident
            self.catalog.use_federated_log_view()
            obj = self.catalog.get_log_entry(self.log_entry_list[0].ident)
            assert obj.ident == self.log_entry_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_log_entry(self.fake_id)

    def test_get_log_entries_by_ids(self):
        """Tests get_log_entries_by_ids"""
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_ids(self.log_entry_ids)
        assert isinstance(objects, LogEntryList)
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_ids(self.log_entry_ids)
        assert isinstance(objects, LogEntryList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_log_entries_by_genus_type(self):
        """Tests get_log_entries_by_genus_type"""
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, LogEntryList)
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, LogEntryList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_log_entries_by_parent_genus_type(self):
        """Tests get_log_entries_by_parent_genus_type"""
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, LogEntryList)
            self.catalog.use_federated_log_view()
            objects = self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, LogEntryList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_log_entries_by_record_type(self):
        """Tests get_log_entries_by_record_type"""
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, LogEntryList)
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, LogEntryList)

    def test_get_log_entries_by_priority_type(self):
        """Tests get_log_entries_by_priority_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entries_by_priority_type(True)

    def test_get_log_entries_by_date(self):
        """Tests get_log_entries_by_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entries_by_date(True, True)

    def test_get_log_entries_by_priority_type_and_date(self):
        """Tests get_log_entries_by_priority_type_and_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entries_by_priority_type_and_date(True, True, True)

    def test_get_log_entries_for_resource(self):
        """Tests get_log_entries_for_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entries_for_resource(True)

    def test_get_log_entries_by_date_for_resource(self):
        """Tests get_log_entries_by_date_for_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entries_by_date_for_resource(True, True, True)

    def test_get_log_entries_by_priority_type_and_date_for_resource(self):
        """Tests get_log_entries_by_priority_type_and_date_for_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_entries_by_priority_type_and_date_for_resource(True, True, True, True)

    def test_get_log_entries(self):
        """Tests get_log_entries"""
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries()
        assert isinstance(objects, LogEntryList)
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries()
        assert isinstance(objects, LogEntryList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_log_entry_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_log_entry(self.log_entry_ids[0], ALIAS_ID)
            obj = self.catalog.get_log_entry(ALIAS_ID)
            assert obj.get_id() == self.log_entry_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def log_entry_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.log_entry_list = list()
    request.cls.log_entry_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + color
            create_form.description = (
                'Test LogEntry for LogEntryQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_log_entry(create_form)
            request.cls.log_entry_list.append(obj)
            request.cls.log_entry_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_log_entry_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("log_entry_query_session_class_fixture", "log_entry_query_session_test_fixture")
class TestLogEntryQuerySession(object):
    """Tests for LogEntryQuerySession"""
    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_log_id() == self.catalog.ident

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_log(), ABCLog)

    def test_can_search_log_entries(self):
        """Tests can_search_log_entries"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_log_entries(), bool)

    def test_use_federated_log_view(self):
        """Tests use_federated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_log_view()

    def test_use_isolated_log_view(self):
        """Tests use_isolated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_log_view()

    def test_get_log_entry_query(self):
        """Tests get_log_entry_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_log_entry_query()
        assert isinstance(query, ABCQueries.LogEntryQuery)

    def test_get_log_entries_by_query(self):
        """Tests get_log_entries_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_log_entry_query()
            query.match_display_name('orange')
            assert self.catalog.get_log_entries_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_log_entries_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_log_entries_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_log_entry_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_entry_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_log_entry_form_for_create([])
        request.cls.form.display_name = 'new LogEntry'
        request.cls.form.description = 'description of LogEntry'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_log_entry(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_log_entry(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("log_entry_admin_session_class_fixture", "log_entry_admin_session_test_fixture")
class TestLogEntryAdminSession(object):
    """Tests for LogEntryAdminSession"""
    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_log_id() == self.catalog.ident

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_log(), ABCLog)

    def test_can_create_log_entries(self):
        """Tests can_create_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.catalog.can_create_log_entries(), bool)

    def test_can_create_log_entry_with_record_types(self):
        """Tests can_create_log_entry_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.catalog.can_create_log_entry_with_record_types(DEFAULT_TYPE), bool)

    def test_get_log_entry_form_for_create(self):
        """Tests get_log_entry_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_log_entry_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_log_entry_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_log_entry_form_for_create([])

    def test_create_log_entry(self):
        """Tests create_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.logging_.objects import LogEntry
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, LogEntry)
            assert self.osid_object.display_name.text == 'new LogEntry'
            assert self.osid_object.description.text == 'description of LogEntry'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_log_entry(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_log_entry('I Will Break You!')
            update_form = self.catalog.get_log_entry_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_log_entry(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_log_entry('foo')

    def test_can_update_log_entries(self):
        """Tests can_update_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.catalog.can_update_log_entries(), bool)

    def test_get_log_entry_form_for_update(self):
        """Tests get_log_entry_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_log_entry_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_log_entry_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_log_entry_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='logging.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_log_entry_form_for_update(self.fake_id)

    def test_update_log_entry(self):
        """Tests update_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.logging_.objects import LogEntry
            form = self.catalog.get_log_entry_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_log_entry(form)
            assert isinstance(updated_object, LogEntry)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_log_entry(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_log_entry('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_log_entry(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_log_entry('foo')

    def test_can_delete_log_entries(self):
        """Tests can_delete_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.catalog.can_delete_log_entries(), bool)

    def test_delete_log_entry(self):
        """Tests delete_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_log_entry_form_for_create([])
            form.display_name = 'new LogEntry'
            form.description = 'description of LogEntry'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_log_entry(form)
            self.catalog.delete_log_entry(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_log_entry(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_log_entry(self.fake_id)

    def test_can_manage_log_entry_aliases(self):
        """Tests can_manage_log_entry_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_log_entry_aliases(), bool)

    def test_alias_log_entry(self):
        """Tests alias_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_log_entry(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_log_entry(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_log_entry(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_log_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.log_entry_list = list()
    request.cls.log_entry_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryLogSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log for Assignment'
        create_form.description = 'Test Log for LogEntryLogSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_log(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + str(num)
            create_form.description = 'Test LogEntry for LogEntryLogSession tests'
            obj = request.cls.catalog.create_log_entry(create_form)
            request.cls.log_entry_list.append(obj)
            request.cls.log_entry_ids.append(obj.ident)
        request.cls.svc_mgr.assign_log_entry_to_log(
            request.cls.log_entry_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_log_entry_to_log(
            request.cls.log_entry_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_log_entry_from_log(
                request.cls.log_entry_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_log_entry_from_log(
                request.cls.log_entry_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_entry_log_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("log_entry_log_session_class_fixture", "log_entry_log_session_test_fixture")
class TestLogEntryLogSession(object):
    """Tests for LogEntryLogSession"""
    def test_use_comparative_log_view(self):
        """Tests use_comparative_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_log_view()

    def test_use_plenary_log_view(self):
        """Tests use_plenary_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_log_view()

    def test_can_lookup_log_entry_log_mappings(self):
        """Tests can_lookup_log_entry_log_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_log_entry_log_mappings()
        assert isinstance(result, bool)

    def test_get_log_entry_ids_by_log(self):
        """Tests get_log_entry_ids_by_log"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_log_entry_ids_by_log(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_entry_ids_by_log(self.fake_id)

    def test_get_log_entries_by_log(self):
        """Tests get_log_entries_by_log"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_log_entries_by_log(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.LogEntryList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_log_entries_by_log(self.fake_id)

    def test_get_log_entry_ids_by_log(self):
        """Tests get_log_entry_ids_by_log"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_log_entry_ids_by_log(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_entry_ids_by_log(self.fake_id)

    def test_get_log_entrie_by_log(self):
        """Tests get_log_entrie_by_log"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_log_entrie_by_log(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.LogEntryList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_log_entrie_by_log(self.fake_id)

    def test_get_log_ids_by_log_entry(self):
        """Tests get_log_ids_by_log_entry"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_log_ids_by_log_entry(self.log_entry_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_ids_by_log_entry(self.fake_id)

    def test_get_log_by_log_entry(self):
        """Tests get_log_by_log_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_log_by_log_entry(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_log_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.log_entry_list = list()
    request.cls.log_entry_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryLogAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log for Assignment'
        create_form.description = 'Test Log for LogEntryLogAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_log(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + str(num)
            create_form.description = 'Test LogEntry for LogEntryLogAssignmentSession tests'
            obj = request.cls.catalog.create_log_entry(create_form)
            request.cls.log_entry_list.append(obj)
            request.cls.log_entry_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_entry_log_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("log_entry_log_assignment_session_class_fixture", "log_entry_log_assignment_session_test_fixture")
class TestLogEntryLogAssignmentSession(object):
    """Tests for LogEntryLogAssignmentSession"""
    def test_can_assign_log_entries(self):
        """Tests can_assign_log_entries"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_log_entries()
        assert isinstance(result, bool)

    def test_can_assign_log_entries_to_log(self):
        """Tests can_assign_log_entries_to_log"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_log_entries_to_log(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_log_ids(self):
        """Tests get_assignable_log_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_log_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_log_ids(self.fake_id)

    def test_get_assignable_log_ids_for_log_entry(self):
        """Tests get_assignable_log_ids_for_log_entry"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_log_ids_for_log_entry(self.catalog.ident, self.log_entry_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_log_ids_for_log_entry(self.fake_id, self.fake_id)

    def test_assign_log_entry_to_log(self):
        """Tests assign_log_entry_to_log"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_log_entries()
            assert results.available() == 0
            self.session.assign_log_entry_to_log(self.log_entry_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_log_entries()
            assert results.available() == 1
            self.session.unassign_log_entry_from_log(
                self.log_entry_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_log_entry_to_log(self.fake_id, self.fake_id)

    def test_unassign_log_entry_from_log(self):
        """Tests unassign_log_entry_from_log"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_log_entries()
            assert results.available() == 0
            self.session.assign_log_entry_to_log(
                self.log_entry_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_log_entries()
            assert results.available() == 1
            self.session.unassign_log_entry_from_log(
                self.log_entry_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_log_entries()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_log_entry_from_log(self.fake_id, self.fake_id)

    def test_reassign_log_entry_to_log(self):
        """Tests reassign_log_entry_to_log"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_log_entry_to_log(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'Test Log ' + str(num)
            create_form.description = 'Test Log for logging proxy manager tests'
            catalog = request.cls.svc_mgr.create_log(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_logs():
                request.cls.svc_mgr.delete_log(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("log_lookup_session_class_fixture", "log_lookup_session_test_fixture")
class TestLogLookupSession(object):
    """Tests for LogLookupSession"""
    def test_can_lookup_logs(self):
        """Tests can_lookup_logs"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_logs(), bool)

    def test_use_comparative_log_view(self):
        """Tests use_comparative_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_log_view()

    def test_use_plenary_log_view(self):
        """Tests use_plenary_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_log_view()

    def test_get_log(self):
        """Tests get_log"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_log(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log(self.fake_id)

    def test_get_logs_by_ids(self):
        """Tests get_logs_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_logs_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.LogList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_logs_by_ids([self.fake_id])

    def test_get_logs_by_genus_type(self):
        """Tests get_logs_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_logs_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.LogList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_logs_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_logs_by_parent_genus_type(self):
        """Tests get_logs_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_logs_by_parent_genus_type(True)

    def test_get_logs_by_record_type(self):
        """Tests get_logs_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_logs_by_record_type(True)

    def test_get_logs_by_provider(self):
        """Tests get_logs_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_logs_by_provider(True)

    def test_get_logs(self):
        """Tests get_logs"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_logs()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.LogList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_logs()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def log_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log For Deletion'
        create_form.description = 'Test Log for LogAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_log(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_logs():
                request.cls.svc_mgr.delete_log(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("log_admin_session_class_fixture", "log_admin_session_test_fixture")
class TestLogAdminSession(object):
    """Tests for LogAdminSession"""
    def test_can_create_logs(self):
        """Tests can_create_logs"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_logs(), bool)

    def test_can_create_log_with_record_types(self):
        """Tests can_create_log_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_log_with_record_types(DEFAULT_TYPE), bool)

    def test_get_log_form_for_create(self):
        """Tests get_log_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.logging_.objects import LogForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_log_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_log_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_form_for_create([])

    def test_create_log(self):
        """Tests create_log"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.logging_.objects import Log
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_log_form_for_create([])
            catalog_form.display_name = 'Test Log'
            catalog_form.description = 'Test Log for LogAdminSession.create_log tests'
            new_catalog = self.svc_mgr.create_log(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_log(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_log('I Will Break You!')
            update_form = self.svc_mgr.get_log_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_log(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_log('foo')

    def test_can_update_logs(self):
        """Tests can_update_logs"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_logs(), bool)

    def test_get_log_form_for_update(self):
        """Tests get_log_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.logging_.objects import LogForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_log_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_form_for_update(self.fake_id)

    def test_update_log(self):
        """Tests update_log"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_log_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_log(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_log('foo')

    def test_can_delete_logs(self):
        """Tests can_delete_logs"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_logs(), bool)

    def test_delete_log(self):
        """Tests delete_log"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_log(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_log(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_log(self.fake_id)

    def test_can_manage_log_aliases(self):
        """Tests can_manage_log_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_log_aliases(), bool)

    def test_alias_log(self):
        """Tests alias_log"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('logging_.Log%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_log(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_log(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_log(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Log ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_log(create_form)
        request.cls.svc_mgr.add_root_log(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_log(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_log(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_log(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_log(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_logs(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_log(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_log(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("log_hierarchy_session_class_fixture", "log_hierarchy_session_test_fixture")
class TestLogHierarchySession(object):
    """Tests for LogHierarchySession"""
    def test_get_log_hierarchy_id(self):
        """Tests get_log_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_log_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_log_hierarchy(self):
        """Tests get_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_log_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_hierarchy()

    def test_can_access_log_hierarchy(self):
        """Tests can_access_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_log_hierarchy(), bool)

    def test_use_comparative_log_view(self):
        """Tests use_comparative_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_log_view()

    def test_use_plenary_log_view(self):
        """Tests use_plenary_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_log_view()

    def test_get_root_log_ids(self):
        """Tests get_root_log_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_log_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_log_ids()

    def test_get_root_logs(self):
        """Tests get_root_logs"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.logging_.objects import LogList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_logs()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_logs()

    def test_has_parent_logs(self):
        """Tests has_parent_logs"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_logs(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_logs(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_logs(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_logs(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_logs(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_logs(self.fake_id)

    def test_is_parent_of_log(self):
        """Tests is_parent_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_log(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_log(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_log(self.fake_id, self.fake_id)

    def test_get_parent_log_ids(self):
        """Tests get_parent_log_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_log_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_log_ids(self.fake_id)

    def test_get_parent_logs(self):
        """Tests get_parent_logs"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_logs(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_logs(self.fake_id)

    def test_is_ancestor_of_log(self):
        """Tests is_ancestor_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_log,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_log(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_logs(self):
        """Tests has_child_logs"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_logs(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_logs(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_logs(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_logs(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_logs(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_logs(self.fake_id)

    def test_is_child_of_log(self):
        """Tests is_child_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_log(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_log(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_log(self.fake_id, self.fake_id)

    def test_get_child_log_ids(self):
        """Tests get_child_log_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_log_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_log_ids(self.fake_id)

    def test_get_child_logs(self):
        """Tests get_child_logs"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_logs(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_logs(self.fake_id)

    def test_is_descendant_of_log(self):
        """Tests is_descendant_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_log,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_log(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_log_node_ids(self):
        """Tests get_log_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_log_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_node_ids(self.fake_id, 1, 2, False)

    def test_get_log_nodes(self):
        """Tests get_log_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_log_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Log ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_log(create_form)
        request.cls.svc_mgr.add_root_log(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_log(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_log(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_log(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_log(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_logs(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_log(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("log_hierarchy_design_session_class_fixture", "log_hierarchy_design_session_test_fixture")
class TestLogHierarchyDesignSession(object):
    """Tests for LogHierarchyDesignSession"""
    def test_get_log_hierarchy_id(self):
        """Tests get_log_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_log_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_log_hierarchy(self):
        """Tests get_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_log_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_log_hierarchy()

    def test_can_modify_log_hierarchy(self):
        """Tests can_modify_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_log_hierarchy(), bool)

    def test_add_root_log(self):
        """Tests add_root_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_logs()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_log(self.fake_id)

    def test_remove_root_log(self):
        """Tests remove_root_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_logs()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Log root'
            new_log = self.svc_mgr.create_log(create_form)
            self.svc_mgr.add_root_log(new_log.ident)

            roots = self.session.get_root_logs()
            assert roots.available() == 2

            self.session.remove_root_log(new_log.ident)

            roots = self.session.get_root_logs()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_log(self.fake_id)

    def test_add_child_log(self):
        """Tests add_child_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_logs(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_log(self.fake_id, self.fake_id)

    def test_remove_child_log(self):
        """Tests remove_child_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_logs(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Log child'
            new_log = self.svc_mgr.create_log(create_form)
            self.svc_mgr.add_child_log(
                self.catalogs['Root'].ident,
                new_log.ident)

            children = self.session.get_child_logs(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_log(
                self.catalogs['Root'].ident,
                new_log.ident)

            children = self.session.get_child_logs(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_log(self.fake_id, self.fake_id)

    def test_remove_child_logs(self):
        """Tests remove_child_logs"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_logs(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Log child'
            new_log = self.svc_mgr.create_log(create_form)
            self.svc_mgr.add_child_log(
                self.catalogs['Grandchild 1'].ident,
                new_log.ident)

            children = self.session.get_child_logs(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_logs(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_logs(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_logs(self.fake_id)
