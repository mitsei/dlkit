"""DLKit Services implementations of authorization service."""
# pylint: disable=no-init
#     osid specification includes some 'marker' interfaces.
# pylint: disable=too-many-ancestors
#     number of ancestors defined in spec.
# pylint: disable=too-few-public-methods,too-many-public-methods
#     number of methods defined in spec. Worse yet, these are aggregates.
# pylint: disable=invalid-name
#     method and class names defined in spec.
# pylint: disable=no-self-use,unused-argument
#     to catch unimplemented methods.
# pylint: disable=super-init-not-called
#     it just isn't.



from . import osid
from .osid_errors import Unimplemented, IllegalState, InvalidArgument
from dlkit.abstract_osid.authorization import objects as abc_authorization_objects
from dlkit.manager_impls.authorization import managers as authorization_managers



DEFAULT = 0
COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
ANY_STATUS = 0
ACTIVE = 1
UNSEQUESTERED = 0
SEQUESTERED = 1
AUTOMATIC = 0
MANDATORY = 1
DISABLED = -1


class AuthorizationProfile(osid.OsidProfile, authorization_managers.AuthorizationProfile):
    """AuthorizationProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None
    def supports_authorization(self):
        """Pass through to provider supports_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization()

    def supports_authorization_lookup(self):
        """Pass through to provider supports_authorization_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization_lookup()

    def supports_authorization_query(self):
        """Pass through to provider supports_authorization_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization_query()

    def supports_authorization_admin(self):
        """Pass through to provider supports_authorization_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization_admin()

    def supports_vault_lookup(self):
        """Pass through to provider supports_vault_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_vault_lookup()

    def supports_vault_query(self):
        """Pass through to provider supports_vault_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_vault_query()

    def supports_vault_admin(self):
        """Pass through to provider supports_vault_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_vault_admin()

    def get_authorization_record_types(self):
        """Pass through to provider get_authorization_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authorization_record_types()

    authorization_record_types = property(fget=get_authorization_record_types)

    def get_authorization_search_record_types(self):
        """Pass through to provider get_authorization_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authorization_search_record_types()

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def get_function_record_types(self):
        """Pass through to provider get_function_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_function_record_types()

    function_record_types = property(fget=get_function_record_types)

    def get_function_search_record_types(self):
        """Pass through to provider get_function_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_function_search_record_types()

    function_search_record_types = property(fget=get_function_search_record_types)

    def get_qualifier_record_types(self):
        """Pass through to provider get_qualifier_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_qualifier_record_types()

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def get_qualifier_search_record_types(self):
        """Pass through to provider get_qualifier_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_qualifier_search_record_types()

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def get_vault_record_types(self):
        """Pass through to provider get_vault_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_vault_record_types()

    vault_record_types = property(fget=get_vault_record_types)

    def get_vault_search_record_types(self):
        """Pass through to provider get_vault_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_vault_search_record_types()

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def get_authorization_condition_record_types(self):
        """Pass through to provider get_authorization_condition_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authorization_condition_record_types()

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)

    ##Implemented from authorization.batch - AuthorizationBatchProfile



class AuthorizationManager(osid.OsidManager, osid.OsidSession, AuthorizationProfile, authorization_managers.AuthorizationManager):
    """AuthorizationManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._vault_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT

    def _set_vault_view(self, session):
        """Sets the underlying vault view to match current view"""
        if self._vault_view == COMPARATIVE:
            try:
                session.use_comparative_vault_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_vault_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_vault_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:authorizationProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('AUTHORIZATION', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('AUTHORIZATION', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()
    def get_authorization_session(self, *args, **kwargs):
        """Pass through to provider get_authorization_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_authorization_session(*args, **kwargs)

    authorization_session = property(fget=get_authorization_session)

    def get_authorization_session_for_vault(self, *args, **kwargs):
        """Pass through to provider get_authorization_session_for_vault"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_authorization_session_for_vault(*args, **kwargs)

    def get_authorization_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_authorization_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_authorization_lookup_session(*args, **kwargs)

    authorization_lookup_session = property(fget=get_authorization_lookup_session)

    def get_authorization_lookup_session_for_vault(self, *args, **kwargs):
        """Pass through to provider get_authorization_lookup_session_for_vault"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_authorization_lookup_session_for_vault(*args, **kwargs)

    def get_authorization_query_session(self, *args, **kwargs):
        """Pass through to provider get_authorization_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_authorization_query_session(*args, **kwargs)

    authorization_query_session = property(fget=get_authorization_query_session)

    def get_authorization_query_session_for_vault(self, *args, **kwargs):
        """Pass through to provider get_authorization_query_session_for_vault"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_authorization_query_session_for_vault(*args, **kwargs)

    def get_authorization_admin_session(self, *args, **kwargs):
        """Pass through to provider get_authorization_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_authorization_admin_session(*args, **kwargs)

    authorization_admin_session = property(fget=get_authorization_admin_session)

    def get_authorization_admin_session_for_vault(self, *args, **kwargs):
        """Pass through to provider get_authorization_admin_session_for_vault"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_authorization_admin_session_for_vault(*args, **kwargs)

    def get_vault_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_vault_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_vault_lookup_session(*args, **kwargs)

    vault_lookup_session = property(fget=get_vault_lookup_session)

    def get_vault_query_session(self, *args, **kwargs):
        """Pass through to provider get_vault_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_vault_query_session(*args, **kwargs)

    vault_query_session = property(fget=get_vault_query_session)

    def get_vault_admin_session(self, *args, **kwargs):
        """Pass through to provider get_vault_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_vault_admin_session(*args, **kwargs)

    vault_admin_session = property(fget=get_vault_admin_session)

    def get_authorization_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    def get_authorization_rules_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    authorization_rules_manager = property(fget=get_authorization_rules_manager)
##
# The following methods are from osid.authorization.VaultLookupSession

    def can_lookup_vaults(self):
        """Pass through to provider VaultLookupSession.can_lookup_vaults"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('vault_lookup_session').can_lookup_vaults()

    def use_comparative_vault_view(self):
        """Pass through to provider VaultLookupSession.use_comparative_vault_view"""
        self._vault_view = COMPARATIVE
        # self._get_provider_session('vault_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_vault_view()
            except AttributeError:
                pass

    def use_plenary_vault_view(self):
        """Pass through to provider VaultLookupSession.use_plenary_vault_view"""
        self._vault_view = PLENARY
        # self._get_provider_session('vault_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_vault_view()
            except AttributeError:
                pass

    def get_vault(self, *args, **kwargs):
        """Pass through to provider VaultLookupSession.get_vault"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return Vault(self._provider_manager,
                           self._get_provider_session('vault_lookup_session').get_vault(*args, **kwargs),
                           self._runtime,
                           self._proxy)

    def get_vaults_by_ids(self, *args, **kwargs):
        """Pass through to provider VaultLookupSession.get_vaults_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('vault_lookup_session').get_vaults_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Vault(self._provider_manager, cat, self._runtime, self._proxy))
        return VaultList(cat_list)

    def get_vaults_by_genus_type(self, *args, **kwargs):
        """Pass through to provider VaultLookupSession.get_vaults_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('vault_lookup_session').get_vaults_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Vault(self._provider_manager, cat, self._runtime, self._proxy))
        return VaultList(cat_list)

    def get_vaults_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider VaultLookupSession.get_vaults_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('vault_lookup_session').get_vaults_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Vault(self._provider_manager, cat, self._runtime, self._proxy))
        return VaultList(cat_list)

    def get_vaults_by_record_type(self, *args, **kwargs):
        """Pass through to provider VaultLookupSession.get_vaults_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('vault_lookup_session').get_vaults_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Vault(self._provider_manager, cat, self._runtime, self._proxy))
        return VaultList(cat_list)

    def get_vaults_by_provider(self, *args, **kwargs):
        """Pass through to provider VaultLookupSession.get_vaults_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('vault_lookup_session').get_vaults_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Vault(self._provider_manager, cat, self._runtime, self._proxy))
        return VaultList(cat_list)

    def get_vaults(self):
        """Pass through to provider VaultLookupSession.get_vaults"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('vault_lookup_session').get_vaults()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Vault(self._provider_manager, cat, self._runtime, self._proxy))
        return VaultList(cat_list)

    vaults = property(fget=get_vaults)


##
# The following methods are from osid.authorization.VaultQuerySession

    def can_search_vaults(self):
        """Pass through to provider VaultQuerySession.can_search_vaults"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('vault_query_session').can_search_vaults()

    def get_vault_query(self):
        """Pass through to provider VaultQuerySession.get_vault_query"""
        # Implemented from kitosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        return self._get_provider_session('vault_query_session').get_vault_query()

    vault_query = property(fget=get_vault_query)

    def get_vaults_by_query(self, *args, **kwargs):
        """Pass through to provider VaultQuerySession.get_vaults_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        return self._get_provider_session('vault_query_session').get_vaults_by_query(*args, **kwargs)


##
# The following methods are from osid.authorization.VaultAdminSession

    def can_create_vaults(self):
        """Pass through to provider VaultAdminSession.can_create_vaults"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('vault_admin_session').can_create_vaults()

    def can_create_vault_with_record_types(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.can_create_vault_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('vault_admin_session').can_create_vault_with_record_types(*args, **kwargs)

    def get_vault_form_for_create(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.get_vault_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('vault_admin_session').get_vault_form_for_create(*args, **kwargs)

    def create_vault(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.create_vault"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return Vault(self._provider_manager,
                           self._get_provider_session('vault_admin_session').create_vault(*args, **kwargs),
                           self._runtime,
                           self._proxy)

    def can_update_vaults(self):
        """Pass through to provider VaultAdminSession.can_update_vaults"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('vault_admin_session').can_update_vaults()

    def get_vault_form_for_update(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.get_vault_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('vault_admin_session').get_vault_form_for_update(*args, **kwargs)

    def get_vault_form(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.get_vault_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'vault_record_types' in kwargs:
            return self.get_vault_form_for_create(*args, **kwargs)
        else:
            return self.get_vault_form_for_update(*args, **kwargs)

    def update_vault(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.update_vault"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return Vault(self._provider_manager,
                           self._get_provider_session('vault_admin_session').update_vault(*args, **kwargs),
                           self._runtime,
                           self._proxy)

    def save_vault(self, vault_form, *args, **kwargs):
        """Pass through to provider VaultAdminSession.update_vault"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if vault_form.is_for_update():
            return self.update_vault(vault_form, *args, **kwargs)
        else:
            return self.create_vault(vault_form, *args, **kwargs)

    def can_delete_vaults(self):
        """Pass through to provider VaultAdminSession.can_delete_vaults"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('vault_admin_session').can_delete_vaults()

    def delete_vault(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.delete_vault"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('vault_admin_session').delete_vault(*args, **kwargs)

    def can_manage_vault_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_vault(self, *args, **kwargs):
        """Pass through to provider VaultAdminSession.alias_vault"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.alias_bin
        self._get_provider_session('vault_admin_session').alias_vault(*args, **kwargs)



    ##Implemented from authorization.batch - AuthorizationBatchManager


    ##Implemented from authorization.batch - AuthorizationBatchProxyManager



class AuthorizationProxyManager(osid.OsidProxyManager, AuthorizationProfile, authorization_managers.AuthorizationProxyManager):
    """AuthorizationProxyManager convenience adapter including related Session methods."""

    def get_authorization_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorization_session_for_vault(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorization_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AuthorizationManager.get_authorization_lookup_session(*args, **kwargs)

    def get_authorization_lookup_session_for_vault(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AuthorizationManager.get_authorization_lookup_session_for_vault(*args, **kwargs)

    def get_authorization_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AuthorizationManager.get_authorization_query_session(*args, **kwargs)

    def get_authorization_query_session_for_vault(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AuthorizationManager.get_authorization_query_session_for_vault(*args, **kwargs)

    def get_authorization_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorization_admin_session_for_vault(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_vault_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_vault_query_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_vault_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorization_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    def get_authorization_rules_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)

    ##Implemented from authorization.batch - AuthorizationBatchProxyManager



class Vault(abc_authorization_objects.Vault, osid.OsidSession, osid.OsidCatalog):
    """Vault convenience adapter including related Session methods."""
    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, runtime, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        self._runtime = runtime
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._vault_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_vault_view(self, session):
        """Sets the underlying vault view to match current view"""
        if self._vault_view == FEDERATED:
            try:
                session.use_federated_vault_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_vault_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_operable_view(self, session):
        """Sets the underlying operable views to match current view"""
        for obj_name in self._operable_views:
            if self._operable_views[obj_name] == ACTIVE:
                try:
                    getattr(session, 'use_active_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_any_status_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_containable_view(self, session):
        """Sets the underlying containable views to match current view"""
        for obj_name in self._containable_views:
            if self._containable_views[obj_name] == SEQUESTERED:
                try:
                    getattr(session, 'use_sequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_unsequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session.

        Instantiates a new one if the named session is not already known.

        """
        agent_key = self._get_agent_key()
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_vault')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_vault_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_vault_id(self):
        """Gets the Id of this vault."""
        return self._catalog_id

    def get_vault(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        else:
            raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()
    def get_vault_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.authorization.AuthorizationSession

    def can_access_authorizations(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def is_authorized(self, *args, **kwargs):
        """Pass through to provider AuthorizationSession.is_authorized"""
        return self._get_provider_session('authorization_session').is_authorized(*args, **kwargs)

    def get_authorization_condition(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def is_authorized_on_condition(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.authorization.AuthorizationLookupSession

    def can_lookup_authorizations(self):
        """Pass through to provider AuthorizationLookupSession.can_lookup_authorizations"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('authorization_lookup_session').can_lookup_authorizations()

    def use_comparative_authorization_view(self):
        """Pass through to provider AuthorizationLookupSession.use_comparative_authorization_view"""
        self._object_views['authorization'] = COMPARATIVE
        # self._get_provider_session('authorization_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_authorization_view()
            except AttributeError:
                pass

    def use_plenary_authorization_view(self):
        """Pass through to provider AuthorizationLookupSession.use_plenary_authorization_view"""
        self._object_views['authorization'] = PLENARY
        # self._get_provider_session('authorization_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_authorization_view()
            except AttributeError:
                pass

    def use_federated_vault_view(self):
        """Pass through to provider AuthorizationLookupSession.use_federated_vault_view"""
        self._vault_view = FEDERATED
        # self._get_provider_session('authorization_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_vault_view()
            except AttributeError:
                pass

    def use_isolated_vault_view(self):
        """Pass through to provider AuthorizationLookupSession.use_isolated_vault_view"""
        self._vault_view = ISOLATED
        # self._get_provider_session('authorization_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_vault_view()
            except AttributeError:
                pass

    def use_effective_authorization_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_any_effective_authorization_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_implicit_authorization_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_explicit_authorization_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_authorization(self, *args, **kwargs):
        """Pass through to provider AuthorizationLookupSession.get_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('authorization_lookup_session').get_authorization(*args, **kwargs)

    def get_authorizations_by_ids(self, *args, **kwargs):
        """Pass through to provider AuthorizationLookupSession.get_authorizations_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('authorization_lookup_session').get_authorizations_by_ids(*args, **kwargs)

    def get_authorizations_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AuthorizationLookupSession.get_authorizations_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('authorization_lookup_session').get_authorizations_by_genus_type(*args, **kwargs)

    def get_authorizations_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider AuthorizationLookupSession.get_authorizations_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('authorization_lookup_session').get_authorizations_by_parent_genus_type(*args, **kwargs)

    def get_authorizations_by_record_type(self, *args, **kwargs):
        """Pass through to provider AuthorizationLookupSession.get_authorizations_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('authorization_lookup_session').get_authorizations_by_record_type(*args, **kwargs)

    def get_authorizations_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_agent(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_agent_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_function(self, *args, **kwargs):
        """Pass through to provider AuthorizationLookupSession.get_authorizations_for_function"""
        # Implemented from kitosid template for -
        # osid.resource.ActivityLookupSession.get_activities_for_objective
        return self._get_provider_session('authorization_lookup_session').get_authorizations_for_function(*args, **kwargs)

    def get_authorizations_for_function_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_resource_and_function(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_resource_and_function_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_agent_and_function(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_for_agent_and_function_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations_by_qualifier(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_explicit_authorization(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_authorizations(self):
        """Pass through to provider AuthorizationLookupSession.get_authorizations"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('authorization_lookup_session').get_authorizations()

    authorizations = property(fget=get_authorizations)


##
# The following methods are from osid.authorization.AuthorizationQuerySession

    def can_search_authorizations(self):
        """Pass through to provider AuthorizationQuerySession.can_search_authorizations"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('authorization_query_session').can_search_authorizations()

    def get_authorization_query(self):
        """Pass through to provider AuthorizationQuerySession.get_authorization_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('authorization_query_session').get_authorization_query()

    authorization_query = property(fget=get_authorization_query)

    def get_authorizations_by_query(self, *args, **kwargs):
        """Pass through to provider AuthorizationQuerySession.get_authorizations_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('authorization_query_session').get_authorizations_by_query(*args, **kwargs)


##
# The following methods are from osid.authorization.AuthorizationAdminSession

    def can_create_authorizations(self):
        """Pass through to provider AuthorizationAdminSession.can_create_authorizations"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('authorization_admin_session').can_create_authorizations()

    def can_create_authorization_with_record_types(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.can_create_authorization_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('authorization_admin_session').can_create_authorization_with_record_types(*args, **kwargs)

    def get_authorization_form_for_create_for_agent(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.get_authorization_form_for_create_for_agent"""
        return self._get_provider_session('authorization_admin_session').get_authorization_form_for_create_for_agent(*args, **kwargs)

    def get_authorization_form_for_create_for_resource(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.get_authorization_form_for_create_for_resource"""
        return self._get_provider_session('authorization_admin_session').get_authorization_form_for_create_for_resource(*args, **kwargs)

    def get_authorization_form_for_create_for_resource_and_trust(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def create_authorization(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.create_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('authorization_admin_session').create_authorization(*args, **kwargs)

    def can_update_authorizations(self):
        """Pass through to provider AuthorizationAdminSession.can_update_authorizations"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('authorization_admin_session').can_update_authorizations()

    def get_authorization_form_for_update(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.get_authorization_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('authorization_admin_session').get_authorization_form_for_update(*args, **kwargs)

    def get_authorization_form(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.get_authorization_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'authorization_record_types' in kwargs:
            return self.get_authorization_form_for_create(*args, **kwargs)
        else:
            return self.get_authorization_form_for_update(*args, **kwargs)

    def duplicate_authorization(self, authorization_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('authorization_admin_session').duplicate_authorization(authorization_id)

    def update_authorization(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.update_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('authorization_admin_session').update_authorization(*args, **kwargs)

    def save_authorization(self, authorization_form, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.update_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if authorization_form.is_for_update():
            return self.update_authorization(authorization_form, *args, **kwargs)
        else:
            return self.create_authorization(authorization_form, *args, **kwargs)

    def can_delete_authorizations(self):
        """Pass through to provider AuthorizationAdminSession.can_delete_authorizations"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('authorization_admin_session').can_delete_authorizations()

    def delete_authorization(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.delete_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('authorization_admin_session').delete_authorization(*args, **kwargs)

    def can_manage_authorization_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_authorization(self, *args, **kwargs):
        """Pass through to provider AuthorizationAdminSession.alias_authorization"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('authorization_admin_session').alias_authorization(*args, **kwargs)




class VaultList(abc_authorization_objects.VaultList, osid.OsidList):
    """VaultList convenience adapter including related Session methods."""

    def get_next_vault(self):
        """Gets next object"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        try:
            next_item = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        else:
            return next_item

    def next(self):
        """next method for enumerator"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        next_item = osid.OsidList.next(self)
        return next_item

    next_vault = property(fget=get_next_vault)

    def get_next_vaults(self, n):
        """gets next n objects from list"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            i = 0
            while i < n:
                try:
                    next_list.append(self.next())
                except StopIteration:
                    break
                i += 1
            return next_list

