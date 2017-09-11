"""JSON implementations of authorization managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import profile
from . import sessions
from .. import utilities
from ..osid import managers as osid_managers
from ..primitives import Type
from ..type.objects import TypeList
from ..utilities import get_registry
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.authorization import managers as authorization_managers


class AuthorizationProfile(osid_managers.OsidProfile, authorization_managers.AuthorizationProfile):
    """The ``AuthorizationProfile`` describes the interoperability among authorization services."""

    def supports_authorization(self):
        """Tests for the availability of an authorization service which is the basic service for checking authorizations.

        return: (boolean) - ``true`` if authorization is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_authorization' in profile.SUPPORTS

    def supports_authorization_lookup(self):
        """Tests if an authorization lookup service is supported.

        An authorization lookup service defines methods to access
        authorizations.

        return: (boolean) - true if authorization lookup is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_authorization_lookup' in profile.SUPPORTS

    def supports_authorization_query(self):
        """Tests if an authorization query service is supported.

        return: (boolean) - ``true`` if authorization query is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_authorization_query' in profile.SUPPORTS

    def supports_authorization_admin(self):
        """Tests if an authorization administrative service is supported.

        return: (boolean) - ``true`` if authorization admin is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_authorization_admin' in profile.SUPPORTS

    def supports_authorization_vault(self):
        """Tests if an authorization to vault lookup session is available.

        return: (boolean) - ``true`` if authorization vault lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_authorization_vault' in profile.SUPPORTS

    def supports_authorization_vault_assignment(self):
        """Tests if an authorization to vault assignment session is available.

        return: (boolean) - ``true`` if authorization vault assignment
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_authorization_vault_assignment' in profile.SUPPORTS

    def supports_vault_lookup(self):
        """Tests if a vault lookup service is supported.

        A vault lookup service defines methods to access authorization
        vaults.

        return: (boolean) - ``true`` if function lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_vault_lookup' in profile.SUPPORTS

    def supports_vault_query(self):
        """Tests if a vault query service is supported.

        return: (boolean) - ``true`` if vault query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_vault_query' in profile.SUPPORTS

    def supports_vault_admin(self):
        """Tests if a vault administrative service is supported.

        return: (boolean) - ``true`` if vault admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_vault_admin' in profile.SUPPORTS

    def supports_vault_hierarchy(self):
        """Tests if a vault hierarchy traversal is supported.

        return: (boolean) - ``true`` if a vault hierarchy traversal is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_vault_hierarchy' in profile.SUPPORTS

    def supports_vault_hierarchy_design(self):
        """Tests if vault hierarchy design is supported.

        return: (boolean) - ``true`` if a function hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_vault_hierarchy_design' in profile.SUPPORTS

    def get_authorization_record_types(self):
        """Gets the supported ``Authorization`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                authorization record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AUTHORIZATION_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    authorization_record_types = property(fget=get_authorization_record_types)

    def get_authorization_search_record_types(self):
        """Gets the supported ``Authorization`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                authorization search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AUTHORIZATION_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def get_function_record_types(self):
        """Gets the supported ``Function`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Function`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('FUNCTION_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    function_record_types = property(fget=get_function_record_types)

    def get_function_search_record_types(self):
        """Gets the supported ``Function`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Function`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('FUNCTION_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    function_search_record_types = property(fget=get_function_search_record_types)

    def get_qualifier_record_types(self):
        """Gets the supported ``Qualifier`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Qualifier`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('QUALIFIER_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def get_qualifier_search_record_types(self):
        """Gets the supported ``Qualifier`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Qualifier`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('QUALIFIER_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def get_vault_record_types(self):
        """Gets the supported ``Vault`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Vault`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('VAULT_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    vault_record_types = property(fget=get_vault_record_types)

    def get_vault_search_record_types(self):
        """Gets the supported vault search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Vault`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('VAULT_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def get_authorization_condition_record_types(self):
        """Gets the supported ``AuthorizationCondition`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``AuthorizationCondition`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AUTHORIZATION_CONDITION_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)


class AuthorizationManager(osid_managers.OsidManager, AuthorizationProfile, authorization_managers.AuthorizationManager):
    """The authorization manager provides access to authorization sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AuthorizationSession:`` a session to performs authorization
        checks
      * ``AuthorizationLookupSession:`` a session to look up
        ``Authorizations``
      * ``AuthorizationQuerySession:`` a session to query
        ``Authorizations``
      * ``AuthorizationSearchSession:`` a session to search
        ``Authorizations``
      * ``AuthorizationAdminSession:`` a session to create, modify and
        delete ``Authorizations``
      * ``AuthorizationNotificationSession: a`` session to receive
        messages pertaining to ``Authorization`` changes
      * ``AuthorizationVaultSession:`` a session to look up
        authorization to vault mappings
      * ``AuthorizationVaultAssignmentSession:`` a session to manage
        authorization to vault mappings
      * ``AuthorizationSmartVaultSession:`` a session to manage smart
        authorization vaults

      * ``FunctionLookupSession:`` a session to look up ``Functions``
      * ``FunctionQuerySession:`` a session to query ``Functions``
      * ``FunctionSearchSession:`` a session to search ``Functions``
      * ``FunctionAdminSession:`` a session to create, modify and delete
        ``Functions``
      * ``FunctionNotificationSession: a`` session to receive messages
        pertaining to ``Function`` changes
      * ``FunctionVaultSession:`` a session for looking up function and
        vault mappings
      * ``FunctionVaultAssignmentSession:`` a session for managing
        function and vault mappings
      * ``FunctionSmartVaultSession:`` a session to manage dynamic
        function vaults

      * ``QualifierLookupSession:`` a session to look up ``Qualifiers``
      * ``QualifierQuerySession:`` a session to query ``Qualifiers``
      * ``QualifierSearchSession:`` a session to search ``Qualifiers``
      * ``QualifierAdminSession:`` a session to create, modify and
        delete ``Qualifiers``
      * ``QualifierNotificationSession: a`` session to receive messages
        pertaining to ``Qualifier`` changes
      * ``QualifierHierarchySession:`` a session for traversing
        qualifier hierarchies
      * ``QualifierHierarchyDesignSession:`` a session for managing
        qualifier hierarchies
      * ``QualifierVaultSession:`` a session for looking up qualifier
        and vault mappings
      * ``QualifierVaultAssignmentSession:`` a session for managing
        qualifier and vault mappings
      * ``QualifierSmartVaultSession:`` a session to manage dynamic
        qualifier vaults

      * ``VaultLookupSession:`` a session to lookup vaults
      * ``VaultQuerySession:`` a session to query Vaults
      * ``VaultSearchSession`` : a session to search vaults
      * ``VaultAdminSession`` : a session to create, modify and delete
        vaults
      * ``VaultNotificationSession`` : a session to receive messages
        pertaining to ``Vault`` changes
      * ``VaultHierarchySession`` : a session to traverse the ``Vault``
        hierarchy
      * ``VaultHierarchyDesignSession`` : a session to manage the
        ``Vault`` hierarchy

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_authorization_session(self):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks.

        return: (osid.authorization.AuthorizationSession) - an
                authorization session for this service
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` is ``true``.*

        """
        if not self.supports_authorization():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationSession(runtime=self._runtime)

    authorization_session = property(fget=get_authorization_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_authorization_session_for_vault(self, vault_id):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationSession) - ``an
                _authorization_session``
        raise:  NotFound - ``vault_id``
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationSession(vault_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_authorization_lookup_session(self):
        """Gets the ``OsidSession`` associated with the authorization lookup service.

        return: (osid.authorization.AuthorizationLookupSession) - an
                ``AuthorizationLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` is ``true``.*

        """
        if not self.supports_authorization_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationLookupSession(runtime=self._runtime)

    authorization_lookup_session = property(fget=get_authorization_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_authorization_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization lookup service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationLookupSession) - ``an
                _authorization_lookup_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationLookupSession(vault_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_authorization_query_session(self):
        """Gets the ``OsidSession`` associated with the authorization query service.

        return: (osid.authorization.AuthorizationQuerySession) - an
                ``AuthorizationQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` is ``true``.*

        """
        if not self.supports_authorization_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationQuerySession(runtime=self._runtime)

    authorization_query_session = property(fget=get_authorization_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_authorization_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization query service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationQuerySession) - ``an
                _authorization_query_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationQuerySession(vault_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_authorization_admin_session(self):
        """Gets the ``OsidSession`` associated with the authorization administration service.

        return: (osid.authorization.AuthorizationAdminSession) - an
                ``AuthorizationAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` is ``true``.*

        """
        if not self.supports_authorization_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationAdminSession(runtime=self._runtime)

    authorization_admin_session = property(fget=get_authorization_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_authorization_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization admin service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationAdminSession) - ``an
                _authorization_admin_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationAdminSession(vault_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_authorization_vault_session(self):
        """Gets the session for retrieving authorization to vault mappings.

        return: (osid.authorization.AuthorizationVaultSession) - an
                ``AuthorizationVaultSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault()`` is ``true``.*

        """
        if not self.supports_authorization_vault():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationVaultSession(runtime=self._runtime)

    authorization_vault_session = property(fget=get_authorization_vault_session)

    @utilities.remove_null_proxy_kwarg
    def get_authorization_vault_assignment_session(self):
        """Gets the session for assigning authorizations to vault mappings.

        return: (osid.authorization.AuthorizationVaultAssignmentSession)
                - a ``AuthorizationVaultAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_authorization_vault_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault_assignment()`` is ``true``.*

        """
        if not self.supports_authorization_vault_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationVaultAssignmentSession(runtime=self._runtime)

    authorization_vault_assignment_session = property(fget=get_authorization_vault_assignment_session)

    @utilities.remove_null_proxy_kwarg
    def get_vault_lookup_session(self):
        """Gets the OsidSession associated with the vault lookup service.

        return: (osid.authorization.VaultLookupSession) - a
                ``VaultLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_lookup() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_lookup()`` is true.*

        """
        if not self.supports_vault_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultLookupSession(runtime=self._runtime)

    vault_lookup_session = property(fget=get_vault_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_vault_query_session(self):
        """Gets the OsidSession associated with the vault query service.

        return: (osid.authorization.VaultQuerySession) - a
                ``VaultQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_query() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_query()`` is true.*

        """
        if not self.supports_vault_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultQuerySession(runtime=self._runtime)

    vault_query_session = property(fget=get_vault_query_session)

    @utilities.remove_null_proxy_kwarg
    def get_vault_admin_session(self):
        """Gets the OsidSession associated with the vault administration service.

        return: (osid.authorization.VaultAdminSession) - a
                ``VaultAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_admin() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_admin()`` is true.*

        """
        if not self.supports_vault_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultAdminSession(runtime=self._runtime)

    vault_admin_session = property(fget=get_vault_admin_session)

    @utilities.remove_null_proxy_kwarg
    def get_vault_hierarchy_session(self):
        """Gets the session traversing vault hierarchies.

        return: (osid.authorization.VaultHierarchySession) - a
                ``VaultHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_hierarchy() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy()`` is true.*

        """
        if not self.supports_vault_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultHierarchySession(runtime=self._runtime)

    vault_hierarchy_session = property(fget=get_vault_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
    def get_vault_hierarchy_design_session(self):
        """Gets the session designing vault hierarchies.

        return: (osid.authorization.VaultHierarchyDesignSession) - a
                ``VaultHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_hierarchy_design() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy_design()`` is true.*

        """
        if not self.supports_vault_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultHierarchyDesignSession(runtime=self._runtime)

    vault_hierarchy_design_session = property(fget=get_vault_hierarchy_design_session)

    def get_authorization_batch_manager(self):
        """Gets an ``AuthorizationBatchManager``.

        return: (osid.authorization.batch.AuthorizationBatchManager) -
                an ``AuthorizationBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_batch() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_batch()`` is true.*

        """
        raise errors.Unimplemented()

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    def get_authorization_rules_manager(self):
        """Gets an ``AuthorizationRulesManager``.

        return: (osid.authorization.rules.AuthorizationRulesManager) -
                an ``AuthorizationRulesManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_rules() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_rules()`` is true.*

        """
        raise errors.Unimplemented()

    authorization_rules_manager = property(fget=get_authorization_rules_manager)


class AuthorizationProxyManager(osid_managers.OsidProxyManager, AuthorizationProfile, authorization_managers.AuthorizationProxyManager):
    """The authorization manager provides access to authorization sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AuthorizationSession:`` a session to performs authorization
        checks
      * ``AuthorizationLookupSession:`` a session to look up
        ``Authorizations``
      * ``AuthorizationSearchSession:`` a session to search
        ``Authorizations``
      * ``AuthorizationAdminSession:`` a session to create, modify and
        delete ``Authorizations``
      * ``AuthorizationNotificationSession: a`` session to receive
        messages pertaining to ``Authorization`` changes
      * ``AuthorizationVaultSession:`` a session to look up
        authorization to vault mappings
      * ``AuthorizationVaultAssignmentSession:`` a session to manage
        authorization to vault mappings
      * ``AuthorizationSmartVaultSession:`` a session to manage smart
        authorization vault

      * ``FunctionLookupSession:`` a session to look up ``Functions``
      * ``FunctionQuerySession:`` a session to query ``Functions``
      * ``FunctionSearchSession:`` a session to search ``Functions``
      * ``FunctionAdminSession:`` a session to create, modify and delete
        ``Functions``
      * ``FunctionNotificationSession: a`` session to receive messages
        pertaining to ``Function`` changes
      * ``FunctionVaultSession:`` a session for looking up function and
        vault mappings
      * ``FunctionVaultAssignmentSession:`` a session for managing
        function and vault mappings
      * ``FunctionSmartVaultSession:`` a session to manage dynamic
        function vaults

      * ``QualifierLookupSession:`` a session to look up ``Qualifiers``
      * ``QualifierQuerySession:`` a session to query ``Qualifiers``
      * ``QualifierSearchSession:`` a session to search ``Qualifiers``
      * ``QualifierAdminSession:`` a session to create, modify and
        delete ``Qualifiers``
      * ``QualifierNotificationSession: a`` session to receive messages
        pertaining to ``Qualifier`` changes
      * ``QualifierHierarchySession:`` a session for traversing
        qualifier hierarchies
      * ``QualifierHierarchyDesignSession:`` a session for managing
        qualifier hierarchies
      * ``QualifierVaultSession:`` a session for looking up qualifier
        and vault mappings
      * ``QualifierVaultAssignmentSession:`` a session for managing
        qualifier and vault mappings
      * ``QualifierSmartVaultSession:`` a session to manage dynamic
        qualifier vaults

      * ``VaultLookupSession:`` a session to lookup vaults
      * ``VaultQuerySession:`` a session to query Vaults
      * ``VaultSearchSession`` : a session to search vaults
      * ``VaultAdminSession`` : a session to create, modify and delete
        vaults
      * ``VaultNotificationSession`` : a session to receive messages
        pertaining to ``Vault`` changes
      * ``VaultHierarchySession`` : a session to traverse the ``Vault``
        hierarchy
      * ``VaultHierarchyDesignSession`` : a session to manage the
        ``Vault`` hierarchy

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_authorization_session(self, proxy):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationSession) - an
                authorization session for this service
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` is ``true``.*

        """
        if not self.supports_authorization():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorization_session_for_vault(self, vault_id, proxy):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationSession) - ``an
                _authorization_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationSession(vault_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_authorization_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationLookupSession) - an
                ``AuthorizationLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` is ``true``.*

        """
        if not self.supports_authorization_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorization_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization lookup service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationLookupSession) - ``an
                _authorization_lookup_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationLookupSession(vault_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_authorization_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationQuerySession) - an
                ``AuthorizationQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` is ``true``.*

        """
        if not self.supports_authorization_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorization_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization query service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationQuerySession) - ``an
                _authorization_query_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationQuerySession(vault_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_authorization_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationAdminSession) - an
                ``AuthorizationAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` is ``true``.*

        """
        if not self.supports_authorization_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorization_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization admin service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationAdminSession) - ``an
                _authorization_admin_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_authorization_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AuthorizationAdminSession(vault_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_authorization_vault_session(self, proxy):
        """Gets the session for retrieving authorization to vault mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationVaultSession) - an
                ``AuthorizationVaultSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault()`` is ``true``.*

        """
        if not self.supports_authorization_vault():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationVaultSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorization_vault_assignment_session(self, proxy):
        """Gets the session for assigning authorization to vault mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationVaultAssignmentSession)
                - a ``AuthorizationVaultAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_authorization_vault_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault_assignment()`` is ``true``.*

        """
        if not self.supports_authorization_vault_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AuthorizationVaultAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vault_lookup_session(self, proxy):
        """Gets the OsidSession associated with the vault lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultLookupSession) - a
                ``VaultLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_lookup() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_lookup()`` is true.*

        """
        if not self.supports_vault_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vault_query_session(self, proxy):
        """Gets the OsidSession associated with the vault query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultQuerySession) - a
                ``VaultQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_query() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_query()`` is true.*

        """
        if not self.supports_vault_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vault_admin_session(self, proxy):
        """Gets the OsidSession associated with the vault administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultAdminSession) - a
                ``VaultAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_admin() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_admin()`` is true.*

        """
        if not self.supports_vault_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vault_hierarchy_session(self, proxy):
        """Gets the session traversing vault hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultHierarchySession) - a
                ``VaultHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_hierarchy() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy()`` is true.*

        """
        if not self.supports_vault_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vault_hierarchy_design_session(self, proxy):
        """Gets the session designing vault hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultHierarchyDesignSession) - a
                ``VaultHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_hierarchy_design() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy_design()`` is true.*

        """
        if not self.supports_vault_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.VaultHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    def get_authorization_batch_proxy_manager(self):
        """Gets an ``AuthorizationBatchProxyManager``.

        return:
                (osid.authorization.batch.AuthorizationBatchProxyManager
                ) - an ``AuthorizationBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_batch() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_batch()`` is true.*

        """
        raise errors.Unimplemented()

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    def get_authorization_rules_proxy_manager(self):
        """Gets an ``AuthorizationRulesProxyManager``.

        return:
                (osid.authorization.rules.AuthorizationRulesProxyManager
                ) - an ``AuthorizationRulesProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_rules() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_rules()`` is true.*

        """
        raise errors.Unimplemented()

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)
