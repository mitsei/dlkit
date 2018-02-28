"""Unit tests of resource queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
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
def resource_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_resource_query()


@pytest.mark.usefixtures("resource_query_class_fixture", "resource_query_test_fixture")
class TestResourceQuery(object):
    """Tests for ResourceQuery"""
    def test_match_group(self):
        """Tests match_group"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_group(True)

    def test_clear_group_terms(self):
        """Tests clear_group_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['group'] = 'foo'
        self.query.clear_group_terms()
        if is_no_authz(self.service_config):
            assert 'group' not in self.query._query_terms

    def test_match_demographic(self):
        """Tests match_demographic"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_demographic(True)

    def test_clear_demographic_terms(self):
        """Tests clear_demographic_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_demographic_terms()

    def test_match_containing_group_id(self):
        """Tests match_containing_group_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'containingGroupId' not in self.query._query_terms
        self.query.match_containing_group_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['containingGroupId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_containing_group_id_terms(self):
        """Tests clear_containing_group_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_containing_group_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'containingGroupId' in self.query._query_terms
        self.query.clear_containing_group_id_terms()
        if is_no_authz(self.service_config):
            assert 'containingGroupId' not in self.query._query_terms

    def test_supports_containing_group_query(self):
        """Tests supports_containing_group_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_containing_group_query()

    def test_get_containing_group_query(self):
        """Tests get_containing_group_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_containing_group_query()

    def test_match_any_containing_group(self):
        """Tests match_any_containing_group"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_containing_group(True)

    def test_clear_containing_group_terms(self):
        """Tests clear_containing_group_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_containing_group_terms()

    def test_match_avatar_id(self):
        """Tests match_avatar_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'avatarId' not in self.query._query_terms
        self.query.match_avatar_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['avatarId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_avatar_id_terms(self):
        """Tests clear_avatar_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_avatar_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'avatarId' in self.query._query_terms
        self.query.clear_avatar_id_terms()
        if is_no_authz(self.service_config):
            assert 'avatarId' not in self.query._query_terms

    def test_supports_avatar_query(self):
        """Tests supports_avatar_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_avatar_query()

    def test_get_avatar_query(self):
        """Tests get_avatar_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_avatar_query()

    def test_match_any_avatar(self):
        """Tests match_any_avatar"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_avatar(True)

    def test_clear_avatar_terms(self):
        """Tests clear_avatar_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['avatar'] = 'foo'
        self.query.clear_avatar_terms()
        if is_no_authz(self.service_config):
            assert 'avatar' not in self.query._query_terms

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
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_agent_query()

    def test_get_agent_query(self):
        """Tests get_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_agent_query()

    def test_match_any_agent(self):
        """Tests match_any_agent"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_agent(True)

    def test_clear_agent_terms(self):
        """Tests clear_agent_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_agent_terms()

    def test_match_resource_relationship_id(self):
        """Tests match_resource_relationship_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'resourceRelationshipId' not in self.query._query_terms
        self.query.match_resource_relationship_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['resourceRelationshipId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_resource_relationship_id_terms(self):
        """Tests clear_resource_relationship_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_resource_relationship_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'resourceRelationshipId' in self.query._query_terms
        self.query.clear_resource_relationship_id_terms()
        if is_no_authz(self.service_config):
            assert 'resourceRelationshipId' not in self.query._query_terms

    def test_supports_resource_relationship_query(self):
        """Tests supports_resource_relationship_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_resource_relationship_query()

    def test_get_resource_relationship_query(self):
        """Tests get_resource_relationship_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_resource_relationship_query()

    def test_match_any_resource_relationship(self):
        """Tests match_any_resource_relationship"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_resource_relationship(True)

    def test_clear_resource_relationship_terms(self):
        """Tests clear_resource_relationship_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_resource_relationship_terms()

    def test_match_bin_id(self):
        """Tests match_bin_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bin_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedBinIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_bin_id_terms(self):
        """Tests clear_bin_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bin_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedBinIds' in self.query._query_terms
        self.query.clear_bin_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedBinIds' not in self.query._query_terms

    def test_supports_bin_query(self):
        """Tests supports_bin_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_bin_query()

    def test_get_bin_query(self):
        """Tests get_bin_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bin_query()

    def test_clear_bin_terms(self):
        """Tests clear_bin_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['bin'] = 'foo'
        self.query.clear_bin_terms()
        if is_no_authz(self.service_config):
            assert 'bin' not in self.query._query_terms

    def test_get_resource_query_record(self):
        """Tests get_resource_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_resource_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_query_class_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_query_test_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.svc_mgr.get_bin_query()


@pytest.mark.usefixtures("bin_query_class_fixture", "bin_query_test_fixture")
class TestBinQuery(object):
    """Tests for BinQuery"""
    def test_match_resource_id(self):
        """Tests match_resource_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_resource_id(True, True)

    def test_clear_resource_id_terms(self):
        """Tests clear_resource_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['resourceId'] = 'foo'

        if not is_never_authz(self.service_config):
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

    def test_match_any_resource(self):
        """Tests match_any_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_resource(True)

    def test_clear_resource_terms(self):
        """Tests clear_resource_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['resource'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_resource_terms()

        if is_no_authz(self.service_config):
            assert 'resource' not in self.query._query_terms

    def test_match_ancestor_bin_id(self):
        """Tests match_ancestor_bin_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_bin_id(True, True)

    def test_clear_ancestor_bin_id_terms(self):
        """Tests clear_ancestor_bin_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorBinId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_bin_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorBinId' not in self.query._query_terms

    def test_supports_ancestor_bin_query(self):
        """Tests supports_ancestor_bin_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_bin_query()

    def test_get_ancestor_bin_query(self):
        """Tests get_ancestor_bin_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_bin_query()

    def test_match_any_ancestor_bin(self):
        """Tests match_any_ancestor_bin"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_bin(True)

    def test_clear_ancestor_bin_terms(self):
        """Tests clear_ancestor_bin_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorBin'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_bin_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorBin' not in self.query._query_terms

    def test_match_descendant_bin_id(self):
        """Tests match_descendant_bin_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_bin_id(True, True)

    def test_clear_descendant_bin_id_terms(self):
        """Tests clear_descendant_bin_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantBinId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_bin_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantBinId' not in self.query._query_terms

    def test_supports_descendant_bin_query(self):
        """Tests supports_descendant_bin_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_bin_query()

    def test_get_descendant_bin_query(self):
        """Tests get_descendant_bin_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_bin_query()

    def test_match_any_descendant_bin(self):
        """Tests match_any_descendant_bin"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_bin(True)

    def test_clear_descendant_bin_terms(self):
        """Tests clear_descendant_bin_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantBin'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_bin_terms()

        if is_no_authz(self.service_config):
            assert 'descendantBin' not in self.query._query_terms

    def test_get_bin_query_record(self):
        """Tests get_bin_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_bin_query_record(True)
