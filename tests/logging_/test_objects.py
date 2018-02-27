"""Unit tests of logging objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
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
def log_entry_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)

        form = request.cls.catalog.get_log_entry_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_log_entry(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_entry_test_fixture(request):
    pass


@pytest.mark.usefixtures("log_entry_class_fixture", "log_entry_test_fixture")
class TestLogEntry(object):
    """Tests for LogEntry"""
    @pytest.mark.skip('unimplemented test')
    def test_get_priority(self):
        """Tests get_priority"""
        pass

    def test_get_timestamp(self):
        """Tests get_timestamp"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_timestamp()

    def test_get_resource_id(self):
        """Tests get_resource_id"""
        with pytest.raises(errors.Unimplemented):
            self.object.get_resource_id()

    def test_get_resource(self):
        """Tests get_resource"""
        with pytest.raises(errors.Unimplemented):
            self.object.get_resource()

    def test_get_agent_id(self):
        """Tests get_agent_id"""
        result = self.object.get_agent_id()
        assert isinstance(result, Id)
        assert str(result) == str(self.catalog._proxy.get_effective_agent_id())

    def test_get_agent(self):
        """Tests get_agent"""
        # because we don't have Agency implemented in authentication
        with pytest.raises(AttributeError):
            self.object.get_agent()

    def test_get_log_entry_record(self):
        """Tests get_log_entry_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_log_entry_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def log_entry_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_log_entry_form_for_create([])


@pytest.mark.usefixtures("log_entry_form_class_fixture", "log_entry_form_test_fixture")
class TestLogEntryForm(object):
    """Tests for LogEntryForm"""
    def test_get_priority_metadata(self):
        """Tests get_priority_metadata"""
        # From test_templates/logging.py::LogEntryForm::get_priority_metadata_template
        mdata = self.form.get_priority_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'TYPE'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_priority(self):
        """Tests set_priority"""
        # From test_templates/logging.py::LogEntryForm::set_priority_template
        self.form.set_priority(Type('type.Type%3Afake-type-id%40ODL.MIT.EDU'))
        assert self.form._my_map['priority'] == 'type.Type%3Afake-type-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_priority(True)

    def test_clear_priority(self):
        """Tests clear_priority"""
        # From test_templates/logging.py::LogEntryForm::clear_priority_template
        self.form.set_priority(Type('type.Type%3Afake-type-id%40ODL.MIT.EDU'))
        assert self.form._my_map['priority'] == 'type.Type%3Afake-type-id%40ODL.MIT.EDU'
        self.form.clear_priority()
        assert self.form._my_map['priorityId'] == self.form.get_priority_metadata().get_default_type_values()[0]

    def test_get_timestamp_metadata(self):
        """Tests get_timestamp_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_timestamp_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'DATETIME'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_timestamp(self):
        """Tests set_timestamp"""
        test_time = DateTime.utcnow()
        # By default log entries have this set, so can't use the templated test
        assert self.form._my_map['timestamp'] is not None
        self.form.set_timestamp(test_time)
        assert self.form._my_map['timestamp'] == test_time
        with pytest.raises(errors.InvalidArgument):
            self.form.set_timestamp(True)

    def test_get_agent_metadata(self):
        """Tests get_agent_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_agent_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_agent(self):
        """Tests set_agent"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['agentId'] == ''
        self.form.set_agent(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['agentId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_agent(True)

    def test_get_log_entry_form_record(self):
        """Tests get_log_entry_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_log_entry_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryList tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_log_entries():
                request.cls.catalog.delete_log_entry(obj.ident)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_entry_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.logging_.objects import LogEntryList
    request.cls.log_entry_list = list()
    request.cls.log_entry_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + str(num)
            create_form.description = 'Test LogEntry for LogEntryList tests'
            obj = request.cls.catalog.create_log_entry(create_form)
            request.cls.log_entry_list.append(obj)
            request.cls.log_entry_ids.append(obj.ident)
    request.cls.log_entry_list = LogEntryList(request.cls.log_entry_list)
    request.cls.object = request.cls.log_entry_list


@pytest.mark.usefixtures("log_entry_list_class_fixture", "log_entry_list_test_fixture")
class TestLogEntryList(object):
    """Tests for LogEntryList"""
    def test_get_next_log_entry(self):
        """Tests get_next_log_entry"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.logging_.objects import LogEntry
        if not is_never_authz(self.service_config):
            assert isinstance(self.log_entry_list.get_next_log_entry(), LogEntry)

    def test_get_next_log_entries(self):
        """Tests get_next_log_entries"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList, LogEntry
        if not is_never_authz(self.service_config):
            new_list = self.log_entry_list.get_next_log_entries(2)
            assert isinstance(new_list, LogEntryList)
            for item in new_list:
                assert isinstance(item, LogEntry)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_log_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_log(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_log(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("log_class_fixture", "log_test_fixture")
class TestLog(object):
    """Tests for Log"""
    def test_get_log_record(self):
        """Tests get_log_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_log_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_log_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("log_form_class_fixture", "log_form_test_fixture")
class TestLogForm(object):
    """Tests for LogForm"""
    def test_get_log_form_record(self):
        """Tests get_log_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_log_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogList tests'
        request.cls.catalog = request.cls.svc_mgr.create_log(create_form)
        request.cls.log_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.log_ids:
                request.cls.svc_mgr.delete_log(obj)
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.logging_.objects import LogList
    request.cls.log_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'Test Log ' + str(num)
            create_form.description = 'Test Log for LogList tests'
            obj = request.cls.svc_mgr.create_log(create_form)
            request.cls.log_list.append(obj)
            request.cls.log_ids.append(obj.ident)
    request.cls.log_list = LogList(request.cls.log_list)


@pytest.mark.usefixtures("log_list_class_fixture", "log_list_test_fixture")
class TestLogList(object):
    """Tests for LogList"""
    def test_get_next_log(self):
        """Tests get_next_log"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.logging_.objects import Log
        if not is_never_authz(self.service_config):
            assert isinstance(self.log_list.get_next_log(), Log)

    def test_get_next_logs(self):
        """Tests get_next_logs"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.logging_.objects import LogList, Log
        if not is_never_authz(self.service_config):
            new_list = self.log_list.get_next_logs(2)
            assert isinstance(new_list, LogList)
            for item in new_list:
                assert isinstance(item, Log)


@pytest.mark.usefixtures("log_node_class_fixture", "log_node_test_fixture")
class TestLogNode(object):
    """Tests for LogNode"""
    @pytest.mark.skip('unimplemented test')
    def test_get_log(self):
        """Tests get_log"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_parent_log_nodes(self):
        """Tests get_parent_log_nodes"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_child_log_nodes(self):
        """Tests get_child_log_nodes"""
        pass


@pytest.mark.usefixtures("log_node_list_class_fixture", "log_node_list_test_fixture")
class TestLogNodeList(object):
    """Tests for LogNodeList"""
    @pytest.mark.skip('unimplemented test')
    def test_get_next_log_node(self):
        """Tests get_next_log_node"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_next_log_nodes(self):
        """Tests get_next_log_nodes"""
        pass
