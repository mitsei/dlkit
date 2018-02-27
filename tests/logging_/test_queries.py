"""Unit tests of logging queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.json_.logging_.queries import LogQuery
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


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_entry_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_entry_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_log_entry_query()


@pytest.mark.usefixtures("log_entry_query_class_fixture", "log_entry_query_test_fixture")
class TestLogEntryQuery(object):
    """Tests for LogEntryQuery"""
    def test_match_priority(self):
        """Tests match_priority"""
        with pytest.raises(errors.Unimplemented):
            self.query.match_priority('foo', match=True)

    def test_match_any_priority(self):
        """Tests match_any_priority"""
        with pytest.raises(errors.Unimplemented):
            self.query.match_any_priority(match=True)

    def test_clear_priority_terms(self):
        """Tests clear_priority_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['priority'] = 'foo'
        self.query.clear_priority_terms()
        if is_no_authz(self.service_config):
            assert 'priority' not in self.query._query_terms

    def test_match_minimum_priority(self):
        """Tests match_minimum_priority"""
        with pytest.raises(errors.Unimplemented):
            self.query.match_minimum_priority('foo', match=True)

    def test_clear_minimum_priority_terms(self):
        """Tests clear_minimum_priority_terms"""
        with pytest.raises(errors.Unimplemented):
            self.query.clear_minimum_priority_terms()

    def test_match_timestamp(self):
        """Tests match_timestamp"""
        start_date = DateTime.utcnow()
        end_date = DateTime.utcnow()
        assert 'timestamp' not in self.query._query_terms
        self.query.match_timestamp(start_date, end_date, True)
        assert self.query._query_terms['timestamp'] == {
            '$gte': start_date,
            '$lte': end_date
        }

    def test_clear_timestamp_terms(self):
        """Tests clear_timestamp_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['timestamp'] = 'foo'
        self.query.clear_timestamp_terms()
        if is_no_authz(self.service_config):
            assert 'timestamp' not in self.query._query_terms

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
        with pytest.raises(errors.Unimplemented):
            self.query.supports_resource_query()

    def test_get_resource_query(self):
        """Tests get_resource_query"""
        with pytest.raises(errors.Unimplemented):
            self.query.get_resource_query()

    def test_clear_resource_terms(self):
        """Tests clear_resource_terms"""
        with pytest.raises(errors.Unimplemented):
            self.query.clear_resource_terms()

    def test_match_agent_id(self):
        """Tests match_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'agentId' not in self.query._query_terms
        self.query.match_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['agentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_agent_id_terms(self):
        """Tests clear_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'agentId' in self.query._query_terms
        self.query.clear_agent_id_terms()
        if is_no_authz(self.service_config):
            assert 'agentId' not in self.query._query_terms

    def test_supports_agent_query(self):
        """Tests supports_agent_query"""
        with pytest.raises(errors.Unimplemented):
            self.query.supports_agent_query()

    def test_get_agent_query(self):
        """Tests get_agent_query"""
        with pytest.raises(errors.Unimplemented):
            self.query.get_agent_query()

    def test_clear_agent_terms(self):
        """Tests clear_agent_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['agent'] = 'foo'
        self.query.clear_agent_terms()
        if is_no_authz(self.service_config):
            assert 'agent' not in self.query._query_terms

    def test_match_log_id(self):
        """Tests match_log_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_log_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedLogIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_log_id_terms(self):
        """Tests clear_log_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_log_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedLogIds' in self.query._query_terms
        self.query.clear_log_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedLogIds' not in self.query._query_terms

    def test_supports_log_query(self):
        """Tests supports_log_query"""
        with pytest.raises(errors.Unimplemented):
            self.query.supports_log_query()

    def test_get_log_query(self):
        """Tests get_log_query"""
        with pytest.raises(errors.Unimplemented):
            self.query.get_log_query()

    def test_clear_log_terms(self):
        """Tests clear_log_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['log'] = 'foo'
        self.query.clear_log_terms()
        if is_no_authz(self.service_config):
            assert 'log' not in self.query._query_terms

    def test_get_log_entry_query_record(self):
        """Tests get_log_entry_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_log_entry_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def log_query_class_fixture(request):
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
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_log(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def log_query_test_fixture(request):
    # Since the session isn't implemented, we just construct a LogQuery directly
    request.cls.query = LogQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("log_query_class_fixture", "log_query_test_fixture")
class TestLogQuery(object):
    """Tests for LogQuery"""
    def test_match_log_entry_id(self):
        """Tests match_log_entry_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_log_entry_id(True, True)

    def test_clear_log_entry_id_terms(self):
        """Tests clear_log_entry_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['logEntryId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_log_entry_id_terms()

        if is_no_authz(self.service_config):
            assert 'logEntryId' not in self.query._query_terms

    def test_supports_log_entry_query(self):
        """Tests supports_log_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_log_entry_query()

    def test_get_log_entry_query(self):
        """Tests get_log_entry_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_log_entry_query()

    def test_match_any_log_entry(self):
        """Tests match_any_log_entry"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_log_entry(True)

    def test_clear_log_entry_terms(self):
        """Tests clear_log_entry_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['logEntry'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_log_entry_terms()

        if is_no_authz(self.service_config):
            assert 'logEntry' not in self.query._query_terms

    def test_match_ancestor_log_id(self):
        """Tests match_ancestor_log_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_log_id(True, True)

    def test_clear_ancestor_log_id_terms(self):
        """Tests clear_ancestor_log_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorLogId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_log_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorLogId' not in self.query._query_terms

    def test_supports_ancestor_log_query(self):
        """Tests supports_ancestor_log_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_log_query()

    def test_get_ancestor_log_query(self):
        """Tests get_ancestor_log_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_log_query()

    def test_match_any_ancestor_log(self):
        """Tests match_any_ancestor_log"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_log(True)

    def test_clear_ancestor_log_terms(self):
        """Tests clear_ancestor_log_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorLog'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_log_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorLog' not in self.query._query_terms

    def test_match_descendant_log_id(self):
        """Tests match_descendant_log_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_log_id(True, True)

    def test_clear_descendant_log_id_terms(self):
        """Tests clear_descendant_log_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantLogId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_log_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantLogId' not in self.query._query_terms

    def test_supports_descendant_log_query(self):
        """Tests supports_descendant_log_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_log_query()

    def test_get_descendant_log_query(self):
        """Tests get_descendant_log_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_log_query()

    def test_match_any_descendant_log(self):
        """Tests match_any_descendant_log"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_log(True)

    def test_clear_descendant_log_terms(self):
        """Tests clear_descendant_log_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantLog'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_log_terms()

        if is_no_authz(self.service_config):
            assert 'descendantLog' not in self.query._query_terms

    def test_get_log_query_record(self):
        """Tests get_log_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_log_query_record(True)
