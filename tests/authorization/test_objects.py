"""Unit tests of authorization objects."""


import unittest


from dlkit.abstract_osid.assessment.objects import AssessmentList
from dlkit.abstract_osid.authorization import objects as ABCObjects
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)
LOOKUP_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAuthorization(unittest.TestCase):
    """Tests for Authorization"""

    @classmethod
    def setUpClass(cls):
        cls.authorization_list = list()
        cls.authorization_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationQuerySession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        create_form = cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': str('foo'), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])
        create_form.display_name = 'Test Authorization'
        create_form.description = (
            'Test Authorization for Authorization tests')
        obj = cls.catalog.create_authorization(create_form)
        cls.object = obj

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            for obj in catalog.get_authorizations():
                catalog.delete_authorization(obj.ident)
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_is_implicit(self):
        """Tests is_implicit"""
        self.assertTrue(isinstance(self.object.is_implicit(), bool))

    def test_has_resource(self):
        """Tests has_resource"""
        self.assertTrue(isinstance(self.object.has_resource(), bool))

    def test_get_resource_id(self):
        """Tests get_resource_id"""
        # no resource, so throws IllegalState
        with self.assertRaises(errors.IllegalState):
            self.object.get_resource_id()

    def test_get_resource(self):
        """Tests get_resource"""
        # no resource, so throws IllegalState
        with self.assertRaises(errors.IllegalState):
            self.object.get_resource()

    def test_has_trust(self):
        """Tests has_trust"""
        self.assertTrue(isinstance(self.object.has_trust(), bool))

    def test_get_trust_id(self):
        """Tests get_trust_id"""
        # no trust, so throws IllegalState
        with self.assertRaises(errors.IllegalState):
            self.object.get_trust_id()

    def test_get_trust(self):
        """Tests get_trust"""
        # no trust, so throws IllegalState
        with self.assertRaises(errors.IllegalState):
            self.object.get_trust()

    def test_has_agent(self):
        """Tests has_agent"""
        self.assertTrue(isinstance(self.object.has_agent(), bool))

    def test_get_agent_id(self):
        """Tests get_agent_id"""
        result = self.object.get_agent_id()
        self.assertTrue(isinstance(result, Id))
        self.assertEqual(str(result),
                         str(AGENT_ID))

    def test_get_agent(self):
        """Tests get_agent"""
        # because we don't have Agency implemented in authentication
        with self.assertRaises(AttributeError):
            self.object.get_agent()

    def test_get_function_id(self):
        """Tests get_function_id"""
        result = self.object.get_function_id()
        self.assertTrue(isinstance(result, Id))
        self.assertEqual(str(result),
                         str(LOOKUP_RESOURCE_FUNCTION_ID))

    def test_get_function(self):
        """Tests get_function"""
        # not supported
        with self.assertRaises(errors.OperationFailed):
            self.object.get_function()

    def test_get_qualifier_id(self):
        """Tests get_qualifier_id"""
        result = self.object.get_qualifier_id()
        self.assertTrue(isinstance(result, Id))
        self.assertEqual(str(result),
                         'resource.Resource%3Afoo%40ODL.MIT.EDU')

    def test_get_qualifier(self):
        """Tests get_qualifier"""
        # not supported
        with self.assertRaises(errors.OperationFailed):
            self.object.get_qualifier()

    def test_get_authorization_record(self):
        """Tests get_authorization_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_authorization_record(True)


class TestAuthorizationForm(unittest.TestCase):
    """Tests for AuthorizationForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        cls.form = cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': '1', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_get_authorization_form_record(self):
        """Tests get_authorization_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_authorization_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAuthorizationList(unittest.TestCase):
    """Tests for AuthorizationList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        cls.form = cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': '1', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])

    def setUp(self):
        from dlkit.json_.authorization.objects import AuthorizationList
        self.authorization_list = list()
        self.authorization_ids = list()

        for num in [0, 1]:
            form = self.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(num), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            obj = self.catalog.create_authorization(form)

            self.authorization_list.append(obj)
            self.authorization_ids.append(obj.ident)
        self.authorization_list = AuthorizationList(self.authorization_list)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            for authz in catalog.get_authorizations():
                catalog.delete_authorization(authz.ident)
            cls.svc_mgr.delete_vault(catalog.ident)

    def test_get_next_authorization(self):
        """Tests get_next_authorization"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.authorization.objects import Authorization
        self.assertTrue(isinstance(self.authorization_list.get_next_authorization(), Authorization))

    def test_get_next_authorizations(self):
        """Tests get_next_authorizations"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList, Authorization
        new_list = self.authorization_list.get_next_authorizations(2)
        self.assertTrue(isinstance(new_list, AuthorizationList))
        for item in new_list:
            self.assertTrue(isinstance(item, Authorization))


class TestVault(unittest.TestCase):
    """Tests for Vault"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::Bin::init_template
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')

    def setUp(self):
        # From test_templates/resource.py::Bin::init_template
        form = self.svc_mgr.get_vault_form_for_create([])
        form.display_name = 'for testing'
        self.object = self.svc_mgr.create_vault(form)

    def tearDown(self):
        # From test_templates/resource.py::Bin::init_template
        self.svc_mgr.delete_vault(self.object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::Bin::init_template
        pass

    def test_get_vault_record(self):
        """Tests get_vault_record"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_vault_record(True)


class TestVaultForm(unittest.TestCase):
    """Tests for VaultForm"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')

    def setUp(self):
        # From test_templates/resource.py::BinForm::init_template
        self.object = self.svc_mgr.get_vault_form_for_create([])

    def tearDown(self):
        # From test_templates/resource.py::BinForm::init_template
        pass

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinForm::init_template
        pass

    def test_get_vault_form_record(self):
        """Tests get_vault_form_record"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_vault_form_record(True)


class TestVaultList(unittest.TestCase):
    """Tests for VaultList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for VaultList tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        cls.vault_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.authorization.objects import VaultList
        self.vault_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'Test Vault ' + str(num)
            create_form.description = 'Test Vault for VaultList tests'
            obj = self.svc_mgr.create_vault(create_form)
            self.vault_list.append(obj)
            self.vault_ids.append(obj.ident)
        self.vault_list = VaultList(self.vault_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.vault_ids:
            cls.svc_mgr.delete_vault(obj)
        cls.svc_mgr.delete_vault(cls.catalog.ident)

    def test_get_next_vault(self):
        """Tests get_next_vault"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.authorization.objects import Vault
        self.assertTrue(isinstance(self.vault_list.get_next_vault(), Vault))

    def test_get_next_vaults(self):
        """Tests get_next_vaults"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.authorization.objects import VaultList, Vault
        new_list = self.vault_list.get_next_vaults(2)
        self.assertTrue(isinstance(new_list, VaultList))
        for item in new_list:
            self.assertTrue(isinstance(item, Vault))


class TestVaultNode(unittest.TestCase):
    """Tests for VaultNode"""

    @unittest.skip('unimplemented test')
    def test_get_vault(self):
        """Tests get_vault"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_vault_nodes(self):
        """Tests get_parent_vault_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_vault_nodes(self):
        """Tests get_child_vault_nodes"""
        pass


class TestVaultNodeList(unittest.TestCase):
    """Tests for VaultNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_vault_node(self):
        """Tests get_next_vault_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_vault_nodes(self):
        """Tests get_next_vault_nodes"""
        pass
