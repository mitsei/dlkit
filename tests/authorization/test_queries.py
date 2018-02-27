"""Unit tests of authorization queries."""


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
def authorization_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_authorization_query()


@pytest.mark.usefixtures("authorization_query_class_fixture", "authorization_query_test_fixture")
class TestAuthorizationQuery(object):
    """Tests for AuthorizationQuery"""
    def test_match_explicit_authorizations(self):
        """Tests match_explicit_authorizations"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_explicit_authorizations(True)

    def test_clear_explicit_authorizations_terms(self):
        """Tests clear_explicit_authorizations_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_explicit_authorizations_terms()

    def test_match_related_authorization_id(self):
        """Tests match_related_authorization_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'relatedAuthorizationId' not in self.query._query_terms
        self.query.match_related_authorization_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['relatedAuthorizationId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_related_authorization_id_terms(self):
        """Tests clear_related_authorization_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_related_authorization_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'relatedAuthorizationId' in self.query._query_terms
        self.query.clear_related_authorization_id_terms()
        if is_no_authz(self.service_config):
            assert 'relatedAuthorizationId' not in self.query._query_terms

    def test_supports_related_authorization_query(self):
        """Tests supports_related_authorization_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_related_authorization_query()

    def test_get_related_authorization_query(self):
        """Tests get_related_authorization_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_related_authorization_query(True)

    def test_clear_related_authorization_terms(self):
        """Tests clear_related_authorization_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_related_authorization_terms()

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
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_resource_query(True)

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
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_resource_terms()

    def test_match_trust_id(self):
        """Tests match_trust_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'trustId' not in self.query._query_terms
        self.query.match_trust_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['trustId'] == {
                '$in': [str(test_id)]
            }

    def test_match_any_trust_id(self):
        """Tests match_any_trust_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_trust_id(True)

    def test_clear_trust_id_terms(self):
        """Tests clear_trust_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_trust_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'trustId' in self.query._query_terms
        self.query.clear_trust_id_terms()
        if is_no_authz(self.service_config):
            assert 'trustId' not in self.query._query_terms

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
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_agent_query(True)

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

    def test_match_function_id(self):
        """Tests match_function_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'functionId' not in self.query._query_terms
        self.query.match_function_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['functionId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_function_id_terms(self):
        """Tests clear_function_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_function_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'functionId' in self.query._query_terms
        self.query.clear_function_id_terms()
        if is_no_authz(self.service_config):
            assert 'functionId' not in self.query._query_terms

    def test_supports_function_query(self):
        """Tests supports_function_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_function_query()

    def test_get_function_query(self):
        """Tests get_function_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_function_query(True)

    def test_clear_function_terms(self):
        """Tests clear_function_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['function'] = 'foo'
        self.query.clear_function_terms()
        if is_no_authz(self.service_config):
            assert 'function' not in self.query._query_terms

    def test_match_qualifier_id(self):
        """Tests match_qualifier_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'qualifierId' not in self.query._query_terms
        self.query.match_qualifier_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['qualifierId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_qualifier_id_terms(self):
        """Tests clear_qualifier_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_qualifier_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'qualifierId' in self.query._query_terms
        self.query.clear_qualifier_id_terms()
        if is_no_authz(self.service_config):
            assert 'qualifierId' not in self.query._query_terms

    def test_supports_qualifier_query(self):
        """Tests supports_qualifier_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_qualifier_query()

    def test_get_qualifier_query(self):
        """Tests get_qualifier_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_qualifier_query(True)

    def test_clear_qualifier_terms(self):
        """Tests clear_qualifier_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['qualifier'] = 'foo'
        self.query.clear_qualifier_terms()
        if is_no_authz(self.service_config):
            assert 'qualifier' not in self.query._query_terms

    def test_match_vault_id(self):
        """Tests match_vault_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_vault_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedVaultIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_vault_id_terms(self):
        """Tests clear_vault_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_vault_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedVaultIds' in self.query._query_terms
        self.query.clear_vault_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedVaultIds' not in self.query._query_terms

    def test_supports_vault_query(self):
        """Tests supports_vault_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_vault_query()

    def test_get_vault_query(self):
        """Tests get_vault_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_vault_query()

    def test_clear_vault_terms(self):
        """Tests clear_vault_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['vault'] = 'foo'
        self.query.clear_vault_terms()
        if is_no_authz(self.service_config):
            assert 'vault' not in self.query._query_terms

    def test_get_authorization_query_record(self):
        """Tests get_authorization_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_authorization_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_query_class_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_query_test_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.svc_mgr.get_vault_query()


@pytest.mark.usefixtures("vault_query_class_fixture", "vault_query_test_fixture")
class TestVaultQuery(object):
    """Tests for VaultQuery"""
    def test_match_function_id(self):
        """Tests match_function_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_function_id(True, True)

    def test_clear_function_id_terms(self):
        """Tests clear_function_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['functionId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_function_id_terms()

        if is_no_authz(self.service_config):
            assert 'functionId' not in self.query._query_terms

    def test_supports_function_query(self):
        """Tests supports_function_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_function_query()

    def test_get_function_query(self):
        """Tests get_function_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_function_query()

    def test_match_any_function(self):
        """Tests match_any_function"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_function(True)

    def test_clear_function_terms(self):
        """Tests clear_function_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['function'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_function_terms()

        if is_no_authz(self.service_config):
            assert 'function' not in self.query._query_terms

    def test_match_qualifier_id(self):
        """Tests match_qualifier_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_qualifier_id(True, True)

    def test_clear_qualifier_id_terms(self):
        """Tests clear_qualifier_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['qualifierId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_qualifier_id_terms()

        if is_no_authz(self.service_config):
            assert 'qualifierId' not in self.query._query_terms

    def test_supports_qualifier_query(self):
        """Tests supports_qualifier_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_qualifier_query()

    def test_get_qualifier_query(self):
        """Tests get_qualifier_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_qualifier_query()

    def test_match_any_qualifier(self):
        """Tests match_any_qualifier"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_qualifier(True)

    def test_clear_qualifier_terms(self):
        """Tests clear_qualifier_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['qualifier'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_qualifier_terms()

        if is_no_authz(self.service_config):
            assert 'qualifier' not in self.query._query_terms

    def test_match_authorization_id(self):
        """Tests match_authorization_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_authorization_id(True, True)

    def test_clear_authorization_id_terms(self):
        """Tests clear_authorization_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['authorizationId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_authorization_id_terms()

        if is_no_authz(self.service_config):
            assert 'authorizationId' not in self.query._query_terms

    def test_supports_authorization_query(self):
        """Tests supports_authorization_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_authorization_query()

    def test_get_authorization_query(self):
        """Tests get_authorization_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_authorization_query()

    def test_match_any_authorization(self):
        """Tests match_any_authorization"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_authorization(True)

    def test_clear_authorization_terms(self):
        """Tests clear_authorization_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['authorization'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_authorization_terms()

        if is_no_authz(self.service_config):
            assert 'authorization' not in self.query._query_terms

    def test_match_ancestor_vault_id(self):
        """Tests match_ancestor_vault_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_vault_id(True, True)

    def test_clear_ancestor_vault_id_terms(self):
        """Tests clear_ancestor_vault_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorVaultId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_vault_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorVaultId' not in self.query._query_terms

    def test_supports_ancestor_vault_query(self):
        """Tests supports_ancestor_vault_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_vault_query()

    def test_get_ancestor_vault_query(self):
        """Tests get_ancestor_vault_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_vault_query()

    def test_match_any_ancestor_vault(self):
        """Tests match_any_ancestor_vault"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_vault(True)

    def test_clear_ancestor_vault_terms(self):
        """Tests clear_ancestor_vault_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorVault'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_vault_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorVault' not in self.query._query_terms

    def test_match_descendant_vault_id(self):
        """Tests match_descendant_vault_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_vault_id(True, True)

    def test_clear_descendant_vault_id_terms(self):
        """Tests clear_descendant_vault_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantVaultId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_vault_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantVaultId' not in self.query._query_terms

    def test_supports_descendant_vault_query(self):
        """Tests supports_descendant_vault_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_vault_query()

    def test_get_descendant_vault_query(self):
        """Tests get_descendant_vault_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_vault_query()

    def test_match_any_descendant_vault(self):
        """Tests match_any_descendant_vault"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_vault(True)

    def test_clear_descendant_vault_terms(self):
        """Tests clear_descendant_vault_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantVault'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_vault_terms()

        if is_no_authz(self.service_config):
            assert 'descendantVault' not in self.query._query_terms

    def test_get_vault_query_record(self):
        """Tests get_vault_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_vault_query_record(True)
