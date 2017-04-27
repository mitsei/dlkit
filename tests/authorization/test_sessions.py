"""Unit tests of authorization sessions."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

LOOKUP_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
SEARCH_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
CREATE_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
DELETE_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
ASSIGN_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'resource.ResourceBin', 'authority': 'ODL.MIT.EDU'})
CREATE_BIN_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
DELETE_BIN_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
LOOKUP_BIN_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
ACCESS_BIN_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
MODIFY_BIN_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
BOOTSTRAP_VAULT_TYPE = Type(authority='ODL.MIT.EDU', namespace='authorization.Vault', identifier='bootstrap_vault')
OVERRIDE_VAULT_TYPE = Type(authority='ODL.MIT.EDU', namespace='authorization.Vault', identifier='override_vault')
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


class TestAuthorizationSession(unittest.TestCase):
    """Tests for AuthorizationSession"""

    @classmethod
    def setUpClass(cls):
        cls.authz_mgr = Runtime().get_manager('AUTHORIZATION', implementation='JSON_1')
        cls.vault_admin_session = cls.authz_mgr.get_vault_admin_session()
        cls.vault_lookup_session = cls.authz_mgr.get_vault_lookup_session()

        create_form = cls.vault_admin_session.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        create_form.genus_type = BOOTSTRAP_VAULT_TYPE
        cls.vault = cls.vault_admin_session.create_vault(create_form)

        create_form = cls.vault_admin_session.get_vault_form_for_create([])
        create_form.display_name = 'Test Override Vault'
        create_form.description = 'Test Override Vault for AuthorizationLookupSession tests'
        create_form.genus_type = OVERRIDE_VAULT_TYPE
        cls.override_vault = cls.vault_admin_session.create_vault(create_form)

        cls.authz_admin_session = cls.authz_mgr.get_authorization_admin_session_for_vault(cls.vault.ident)
        cls.override_authz_admin_session = cls.authz_mgr.get_authorization_admin_session_for_vault(cls.override_vault.ident)
        cls.authz_lookup_session = cls.authz_mgr.get_authorization_lookup_session_for_vault(cls.vault.ident)

        # Set up Bin create authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            CREATE_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Create for Test Authorizations'
        create_form.description = 'Bin Create Authorization for AuthorizationLookupSession tests'
        bin_create_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin delete authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            DELETE_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Delete for Test Authorizations'
        create_form.description = 'Bin Delete Authorization for AuthorizationLookupSession tests'
        bin_delete_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin lookup authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            LOOKUP_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Lookup for Test Authorizations'
        create_form.description = 'Bin Lookup Authorization for AuthorizationLookupSession tests'
        bin_lookup_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin hierarchy access authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            ACCESS_BIN_HIERARCHY_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Hierarchy Access for Test Authorizations'
        create_form.description = 'Bin Hierarchy Access Authorization for AuthorizationLookupSession tests'
        bin_hierarchy_modify_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin hierarchy modify authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            MODIFY_BIN_HIERARCHY_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Hierarchy Modify for Test Authorizations'
        create_form.description = 'Bin Hierarchy Modify Authorization for AuthorizationLookupSession tests'
        bin_hierarchy_modify_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource create authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            CREATE_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource create for Test Authorizations'
        create_form.description = 'Resource create Authorization for AuthorizationLookupSession tests'
        resource_create_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource delete authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            DELETE_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource Delete for Test Authorizations'
        create_form.description = 'Resource Delete Authorization for AuthorizationLookupSession tests'
        resource_delete_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource - Bin assignment authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            ASSIGN_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource Delete for Test Authorizations'
        create_form.description = 'Resource Delete Authorization for AuthorizationLookupSession tests'
        resource_delete_authz = cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource lookup authorization for current user
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            LOOKUP_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource Lookup for Test Authorizations'
        create_form.description = 'Resource Lookup Authorization for AuthorizationLookupSession tests'
        resource_lookup_authz = cls.authz_admin_session.create_authorization(create_form)

        cls.bin_list = list()
        cls.bin_id_list = list()
        cls.authz_list = list()
        cls.authz_id_list = list()
        cls.resource_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = cls.resource_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for Testing Authorization Number: ' + str(num)
            bin = cls.resource_mgr.create_bin(create_form)
            cls.bin_list.append(bin)
            cls.bin_id_list.append(bin.ident)

        cls.resource_mgr.add_root_bin(cls.bin_id_list[0])
        cls.resource_mgr.add_child_bin(cls.bin_id_list[0], cls.bin_id_list[1])
        cls.resource_mgr.add_child_bin(cls.bin_id_list[0], cls.bin_id_list[2])
        cls.resource_mgr.add_child_bin(cls.bin_id_list[1], cls.bin_id_list[3])
        cls.resource_mgr.add_child_bin(cls.bin_id_list[1], cls.bin_id_list[4])
        cls.resource_mgr.add_child_bin(cls.bin_id_list[2], cls.bin_id_list[5])

        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalog = cls.svc_mgr.get_vault(cls.vault.ident)

        # Set up Bin lookup authorization for Jane
        create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
        jane_lookup_authz = cls.authz_admin_session.create_authorization(create_form)
        cls.authz_list.append(jane_lookup_authz)
        cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up Resource lookup authorizations for Jane
        for num in [1, 5]:
            create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            authz = cls.authz_admin_session.create_authorization(create_form)
            cls.authz_list.append(authz)
            cls.authz_id_list.append(authz.ident)

        # Set up Resource lookup override authorizations for Jane
        for num in [7]:
            create_form = cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            authz = cls.override_authz_admin_session.create_authorization(create_form)
            cls.authz_list.append(authz)
            cls.authz_id_list.append(authz.ident)

        # Set up Resource search override authorizations for Jane
        for num in [7]:
            create_form = cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_RESOURCE_FUNCTION_ID,
                cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            authz = cls.override_authz_admin_session.create_authorization(create_form)
            cls.authz_list.append(authz)
            cls.authz_id_list.append(authz.ident)

        # Set up Resource search authorizations for Jane
        for num in [1, 5]:
            create_form = cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_RESOURCE_FUNCTION_ID,
                cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            authz = cls.authz_admin_session.create_authorization(create_form)
            cls.authz_list.append(authz)
            cls.authz_id_list.append(authz.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.resource_mgr.get_bins():
            for obj in catalog.get_resources():
                catalog.delete_resource(obj.ident)
            cls.resource_mgr.delete_bin(catalog.ident)
        for vault in cls.vault_lookup_session.get_vaults():
            lookup_session = cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
            admin_session = cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
            for authz in lookup_session.get_authorizations():
                admin_session.delete_authorization(authz.ident)
            cls.vault_admin_session.delete_vault(vault.ident)

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' resource in bin 2 is also assigned to bin 7)

    def test_get_vault_id(self):
        """Tests get_vault_id"""
        self.assertEqual(self.catalog.get_vault_id(), self.catalog.ident)

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_access_authorizations(self):
        """Tests can_access_authorizations"""
        pass

    def test_is_authorized(self):
        """Tests is_authorized"""
        self.assertFalse(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[0]))

    def test_is_authorized_1(self):
        """Tests is_authorized 1"""
        self.assertTrue(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[1]))

    def test_is_authorized_3(self):
        """Tests is_authorized 3"""
        self.assertTrue(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[3]))

    def test_is_authorized_4(self):
        """Tests is_authorized 4"""
        self.assertTrue(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[4]))

    def test_is_authorized_2(self):
        """Tests is_authorized 2"""
        self.assertFalse(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[2]))

    def test_is_authorized_5(self):
        """Tests is_authorized 5"""
        self.assertTrue(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[5]))

    def test_is_authorized_6(self):
        """Tests is_authorized 5"""
        self.assertFalse(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[6]))

    def test_is_authorized_7(self):
        """Tests is_authorized 5"""
        self.assertTrue(self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[7]))

    @unittest.skip('unimplemented test')
    def test_get_authorization_condition(self):
        """Tests get_authorization_condition"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_authorized_on_condition(self):
        """Tests is_authorized_on_condition"""
        pass


class TestAuthorizationLookupSession(unittest.TestCase):
    """Tests for AuthorizationLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.authorization_list = list()
        cls.authorization_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(num), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            object = cls.catalog.create_authorization(create_form)
            cls.authorization_list.append(object)
            cls.authorization_ids.append(object.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            for obj in catalog.get_authorizations():
                catalog.delete_authorization(obj.ident)
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_get_vault_id(self):
        """Tests get_vault_id"""
        self.assertEqual(self.catalog.get_vault_id(), self.catalog.ident)

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_authorizations(self):
        """Tests can_lookup_authorizations"""
        self.assertTrue(isinstance(self.catalog.can_lookup_authorizations(), bool))

    def test_use_comparative_authorization_view(self):
        """Tests use_comparative_authorization_view"""
        self.catalog.use_comparative_authorization_view()

    def test_use_plenary_authorization_view(self):
        """Tests use_plenary_authorization_view"""
        self.catalog.use_plenary_authorization_view()

    def test_use_federated_vault_view(self):
        """Tests use_federated_vault_view"""
        self.catalog.use_federated_vault_view()

    def test_use_isolated_vault_view(self):
        """Tests use_isolated_vault_view"""
        self.catalog.use_isolated_vault_view()

    @unittest.skip('unimplemented test')
    def test_use_effective_authorization_view(self):
        """Tests use_effective_authorization_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_any_effective_authorization_view(self):
        """Tests use_any_effective_authorization_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_implicit_authorization_view(self):
        """Tests use_implicit_authorization_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_explicit_authorization_view(self):
        """Tests use_explicit_authorization_view"""
        pass

    def test_get_authorization(self):
        """Tests get_authorization"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_vault_view()
        obj = self.catalog.get_authorization(self.authorization_list[0].ident)
        self.assertEqual(obj.ident, self.authorization_list[0].ident)
        self.catalog.use_federated_vault_view()
        obj = self.catalog.get_authorization(self.authorization_list[0].ident)
        self.assertEqual(obj.ident, self.authorization_list[0].ident)

    def test_get_authorizations_by_ids(self):
        """Tests get_authorizations_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        objects = self.catalog.get_authorizations_by_ids(self.authorization_ids)
        self.assertTrue(isinstance(objects, AuthorizationList))
        self.catalog.use_federated_vault_view()
        objects = self.catalog.get_authorizations_by_ids(self.authorization_ids)

    def test_get_authorizations_by_genus_type(self):
        """Tests get_authorizations_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        objects = self.catalog.get_authorizations_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AuthorizationList))
        self.catalog.use_federated_vault_view()
        objects = self.catalog.get_authorizations_by_genus_type(DEFAULT_TYPE)

    def test_get_authorizations_by_parent_genus_type(self):
        """Tests get_authorizations_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        objects = self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AuthorizationList))
        self.catalog.use_federated_vault_view()
        objects = self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_authorizations_by_record_type(self):
        """Tests get_authorizations_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        objects = self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AuthorizationList))
        self.catalog.use_federated_vault_view()
        objects = self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_authorizations_on_date(self):
        """Tests get_authorizations_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_resource(self):
        """Tests get_authorizations_for_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_resource_on_date(self):
        """Tests get_authorizations_for_resource_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_agent(self):
        """Tests get_authorizations_for_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_agent_on_date(self):
        """Tests get_authorizations_for_agent_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_function(self):
        """Tests get_authorizations_for_function"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_function_on_date(self):
        """Tests get_authorizations_for_function_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_resource_and_function(self):
        """Tests get_authorizations_for_resource_and_function"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_resource_and_function_on_date(self):
        """Tests get_authorizations_for_resource_and_function_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_agent_and_function(self):
        """Tests get_authorizations_for_agent_and_function"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_for_agent_and_function_on_date(self):
        """Tests get_authorizations_for_agent_and_function_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorizations_by_qualifier(self):
        """Tests get_authorizations_by_qualifier"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_explicit_authorization(self):
        """Tests get_explicit_authorization"""
        pass

    def test_get_authorizations(self):
        """Tests get_authorizations"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        objects = self.catalog.get_authorizations()
        self.assertTrue(isinstance(objects, AuthorizationList))
        self.catalog.use_federated_vault_view()
        objects = self.catalog.get_authorizations()

    def test_get_authorization_with_alias(self):
        self.catalog.alias_authorization(self.authorization_ids[0], ALIAS_ID)
        obj = self.catalog.get_authorization(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.authorization_ids[0])


class TestAuthorizationQuerySession(unittest.TestCase):
    """Tests for AuthorizationQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.authorization_list = list()
        cls.authorization_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationQuerySession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(color), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            create_form.display_name = 'Test Authorization ' + color
            create_form.description = (
                'Test Authorization for AuthorizationQuerySession tests, did I mention green')
            obj = cls.catalog.create_authorization(create_form)
            cls.authorization_list.append(obj)
            cls.authorization_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            for obj in catalog.get_authorizations():
                catalog.delete_authorization(obj.ident)
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_get_vault_id(self):
        """Tests get_vault_id"""
        self.assertEqual(self.catalog.get_vault_id(), self.catalog.ident)

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_search_authorizations(self):
        """Tests can_search_authorizations"""
        pass

    def test_use_federated_vault_view(self):
        """Tests use_federated_vault_view"""
        self.catalog.use_federated_vault_view()

    def test_use_isolated_vault_view(self):
        """Tests use_isolated_vault_view"""
        self.catalog.use_isolated_vault_view()

    @unittest.skip('unimplemented test')
    def test_use_implicit_authorization_view(self):
        """Tests use_implicit_authorization_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_explicit_authorization_view(self):
        """Tests use_explicit_authorization_view"""
        pass

    def test_get_authorization_query(self):
        """Tests get_authorization_query"""
        query = self.catalog.get_authorization_query()

    def test_get_authorizations_by_query(self):
        """Tests get_authorizations_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_authorization_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_authorizations_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_authorizations_by_query(query).available(), 3)


class TestAuthorizationAdminSession(unittest.TestCase):
    """Tests for AuthorizationAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.authorization_list = list()
        cls.authorization_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationAdminSession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(num), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            object = cls.catalog.create_authorization(create_form)
            cls.authorization_list.append(object)
            cls.authorization_ids.append(object.ident)

        form = cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': 'foo', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])
        form.display_name = 'new Authorization'
        form.description = 'description of Authorization'
        form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_authorization(form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            for obj in catalog.get_authorizations():
                catalog.delete_authorization(obj.ident)
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_get_vault_id(self):
        """Tests get_vault_id"""
        self.assertEqual(self.catalog.get_vault_id(), self.catalog.ident)

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_authorizations(self):
        """Tests can_create_authorizations"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_authorizations(), bool))

    def test_can_create_authorization_with_record_types(self):
        """Tests can_create_authorization_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_authorization_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_authorization_form_for_create_for_agent(self):
        """Tests get_authorization_form_for_create_for_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorization_form_for_create_for_resource(self):
        """Tests get_authorization_form_for_create_for_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorization_form_for_create_for_resource_and_trust(self):
        """Tests get_authorization_form_for_create_for_resource_and_trust"""
        pass

    def test_create_authorization(self):
        """Tests create_authorization"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.authorization.objects import Authorization
        self.assertTrue(isinstance(self.osid_object, Authorization))
        self.assertEqual(self.osid_object.display_name.text, 'new Authorization')
        self.assertEqual(self.osid_object.description.text, 'description of Authorization')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_authorizations(self):
        """Tests can_update_authorizations"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_authorizations(), bool))

    def test_get_authorization_form_for_update(self):
        """Tests get_authorization_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_authorization_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_authorization(self):
        """Tests update_authorization"""
        from dlkit.abstract_osid.authorization.objects import Authorization
        form = self.catalog.get_authorization_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_authorization(form)
        self.assertTrue(isinstance(updated_object, Authorization))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_authorizations(self):
        """Tests can_delete_authorizations"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_authorizations(), bool))

    def test_delete_authorization(self):
        """Tests delete_authorization"""
        form = self.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': 'foo2', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])
        form.display_name = 'new Authorization'
        form.description = 'description of Authorization'
        form.genus_type = NEW_TYPE
        osid_object = self.catalog.create_authorization(form)
        self.catalog.delete_authorization(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_authorization(osid_object.ident)

    def test_can_manage_authorization_aliases(self):
        """Tests can_manage_authorization_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_authorization_aliases(), bool))

    def test_alias_authorization(self):
        """Tests alias_authorization"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_authorization(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_authorization(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestVaultLookupSession(unittest.TestCase):
    """Tests for VaultLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'Test Vault ' + str(num)
            create_form.description = 'Test Vault for authorization proxy manager tests'
            catalog = cls.svc_mgr.create_vault(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            cls.svc_mgr.delete_vault(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_vaults(self):
        """Tests can_lookup_vaults"""
        pass

    def test_use_comparative_vault_view(self):
        """Tests use_comparative_vault_view"""
        self.svc_mgr.use_comparative_vault_view()

    def test_use_plenary_vault_view(self):
        """Tests use_plenary_vault_view"""
        self.svc_mgr.use_plenary_vault_view()

    def test_get_vault(self):
        """Tests get_vault"""
        catalog = self.svc_mgr.get_vault(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_vaults_by_ids(self):
        """Tests get_vaults_by_ids"""
        catalogs = self.svc_mgr.get_vaults_by_ids(self.catalog_ids)

    @unittest.skip('unimplemented test')
    def test_get_vaults_by_genus_type(self):
        """Tests get_vaults_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vaults_by_parent_genus_type(self):
        """Tests get_vaults_by_parent_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vaults_by_record_type(self):
        """Tests get_vaults_by_record_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vaults_by_provider(self):
        """Tests get_vaults_by_provider"""
        pass

    def test_get_vaults(self):
        """Tests get_vaults"""
        catalogs = self.svc_mgr.get_vaults()


class TestVaultQuerySession(unittest.TestCase):
    """Tests for VaultQuerySession"""

    @unittest.skip('unimplemented test')
    def test_can_search_vaults(self):
        """Tests can_search_vaults"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vault_query(self):
        """Tests get_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vaults_by_query(self):
        """Tests get_vaults_by_query"""
        pass


class TestVaultAdminSession(unittest.TestCase):
    """Tests for VaultAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for VaultAdminSession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault For Deletion'
        create_form.description = 'Test Vault for VaultAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_vault(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_can_create_vaults(self):
        """Tests can_create_vaults"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_vaults(), bool))

    def test_can_create_vault_with_record_types(self):
        """Tests can_create_vault_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_vault_with_record_types(DEFAULT_TYPE), bool))

    def test_get_vault_form_for_create(self):
        """Tests get_vault_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.authorization.objects import VaultForm
        catalog_form = self.svc_mgr.get_vault_form_for_create([])
        self.assertTrue(isinstance(catalog_form, VaultForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_vault(self):
        """Tests create_vault"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.authorization.objects import Vault
        catalog_form = self.svc_mgr.get_vault_form_for_create([])
        catalog_form.display_name = 'Test Vault'
        catalog_form.description = 'Test Vault for VaultAdminSession.create_vault tests'
        new_catalog = self.svc_mgr.create_vault(catalog_form)
        self.assertTrue(isinstance(new_catalog, Vault))

    @unittest.skip('unimplemented test')
    def test_can_update_vaults(self):
        """Tests can_update_vaults"""
        pass

    def test_get_vault_form_for_update(self):
        """Tests get_vault_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.authorization.objects import VaultForm
        catalog_form = self.svc_mgr.get_vault_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, VaultForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_vault(self):
        """Tests update_vault"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_vault_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_vault(catalog_form)

    @unittest.skip('unimplemented test')
    def test_can_delete_vaults(self):
        """Tests can_delete_vaults"""
        pass

    def test_delete_vault(self):
        """Tests delete_vault"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_vault(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_vault(cat_id)

    def test_can_manage_vault_aliases(self):
        """Tests can_manage_vault_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_vault_aliases(), bool))

    def test_alias_vault(self):
        """Tests alias_vault"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('authorization.Vault%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_vault(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_vault(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)
