"""Manager utility implementations of authorization managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import NullArgument
from ..osid.osid_errors import Unimplemented
from ..type.objects import TypeList
from dlkit.abstract_osid.authorization import managers as abc_authorization_managers


class AuthorizationProfile(abc_authorization_managers.AuthorizationProfile, osid_managers.OsidProfile):
    """The ``AuthorizationProfile`` describes the interoperability among authorization services."""

    def supports_visible_federation(self):
        """Tests if federation is visible.

        return: (boolean) - ``true`` if visible federation is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization(self):
        """Tests for the availability of an authorization service which is the basic service for checking authorizations.

        return: (boolean) - ``true`` if authorization is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_lookup(self):
        """Tests if an authorization lookup service is supported.

        An authorization lookup service defines methods to access
        authorizations.

        return: (boolean) - true if authorization lookup is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_query(self):
        """Tests if an authorization query service is supported.

        return: (boolean) - ``true`` if authorization query is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_search(self):
        """Tests if an authorization search service is supported.

        return: (boolean) - ``true`` if authorization search is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_admin(self):
        """Tests if an authorization administrative service is supported.

        return: (boolean) - ``true`` if authorization admin is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_notification(self):
        """Tests if authorization notification is supported.

        Messages may be sent when authorizations are created, modified,
        or deleted.

        return: (boolean) - ``true`` if authorization notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_vault(self):
        """Tests if an authorization to vault lookup session is available.

        return: (boolean) - ``true`` if authorization vault lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_vault_assignment(self):
        """Tests if an authorization to vault assignment session is available.

        return: (boolean) - ``true`` if authorization vault assignment
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_smart_vault(self):
        """Tests if an authorization smart vaulting session is available.

        return: (boolean) - ``true`` if authorization smart vaulting is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_lookup(self):
        """Tests if a function lookup service is supported.

        A function lookup service defines methods to access
        authorization functions.

        return: (boolean) - ``true`` if function lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_query(self):
        """Tests if a function query service is supported.

        return: (boolean) - ``true`` if function query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_search(self):
        """Tests if a function search service is supported.

        return: (boolean) - ``true`` if function search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_admin(self):
        """Tests if a function administrative service is supported.

        return: (boolean) - ``true`` if function admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_notification(self):
        """Tests if function notification is supported.

        Messages may be sent when functions are created, modified, or
        deleted.

        return: (boolean) - ``true`` if function notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_vault(self):
        """Tests if a function to vault lookup session is available.

        return: (boolean) - ``true`` if function vault lookup session is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_vault_assignment(self):
        """Tests if a function to vault assignment session is available.

        return: (boolean) - ``true`` if function vault assignment is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_function_smart_vault(self):
        """Tests if a function smart vaulting session is available.

        return: (boolean) - ``true`` if function smart vaulting is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_lookup(self):
        """Tests if a qualifier lookup service is supported.

        A function lookup service defines methods to access
        authorization qualifiers.

        return: (boolean) - ``true`` if qualifier lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_query(self):
        """Tests if a qualifier query service is supported.

        return: (boolean) - ``true`` if qualifier query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_search(self):
        """Tests if a qualifier search service is supported.

        return: (boolean) - ``true`` if qualifier search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_admin(self):
        """Tests if a qualifier administrative service is supported.

        return: (boolean) - ``true`` if qualifier admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_notification(self):
        """Tests if qualifier notification is supported.

        Messages may be sent when qualifiers are created, modified, or
        deleted.

        return: (boolean) - ``true`` if qualifier notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_hierarchy(self):
        """Tests if a qualifier hierarchy traversal is supported.

        return: (boolean) - ``true`` if a qualifier hierarchy traversal
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_hierarchy_design(self):
        """Tests if qualifier hierarchy design is supported.

        return: (boolean) - ``true`` if a qualifier hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_vault(self):
        """Tests if a qualifier to vault lookup session is available.

        return: (boolean) - ``true`` if qualifier vault lookup session
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_vault_assignment(self):
        """Tests if a qualifier to vault assignment session is available.

        return: (boolean) - ``true`` if qualifier vault assignment is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_qualifier_smart_vault(self):
        """Tests if a qualifier smart vaulting session is available.

        return: (boolean) - ``true`` if qualifier smart vault session is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_lookup(self):
        """Tests if a vault lookup service is supported.

        A vault lookup service defines methods to access authorization
        vaults.

        return: (boolean) - ``true`` if function lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_query(self):
        """Tests if a vault query service is supported.

        return: (boolean) - ``true`` if vault query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_search(self):
        """Tests if a vault search service is supported.

        return: (boolean) - ``true`` if vault search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_admin(self):
        """Tests if a vault administrative service is supported.

        return: (boolean) - ``true`` if vault admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_notification(self):
        """Tests if vault notification is supported.

        Messages may be sent when vaults are created, modified, or
        deleted.

        return: (boolean) - ``true`` if vault notification is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_hierarchy(self):
        """Tests if a vault hierarchy traversal is supported.

        return: (boolean) - ``true`` if a vault hierarchy traversal is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_vault_hierarchy_design(self):
        """Tests if vault hierarchy design is supported.

        return: (boolean) - ``true`` if a function hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_batch(self):
        """Tests if an authorization batch service is supported.

        return: (boolean) - ``true`` if an authorization batch service
                design is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authorization_rules(self):
        """Tests if an authorization rules service is supported.

        return: (boolean) - ``true`` if an authorization rules service
                design is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_authorization_record_types(self):
        """Gets the supported ``Authorization`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                authorization record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    authorization_record_types = property(fget=get_authorization_record_types)

    def supports_authorization_record_type(self, authorization_record_type=None):
        """Tests if the given authorization record type is supported.

        arg:    authorization_record_type (osid.type.Type): a ``Type``
                indicating an authorization record type
        return: (boolean) - ``true`` if the given record Type is
                supported, ``false`` otherwise
        raise:  NullArgument - ``authorization_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if authorization_record_type is None:
            raise NullArgument()
        return False

    def get_authorization_search_record_types(self):
        """Gets the supported ``Authorization`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                authorization search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def supports_authorization_search_record_type(self, authorization_search_record_type=None):
        """Tests if the given authorization search record type is supported.

        arg:    authorization_search_record_type (osid.type.Type): a
                ``Type`` indicating an authorization search record type
        return: (boolean) - ``true`` if the given search record Type is
                supported, ``false`` otherwise
        raise:  NullArgument - ``authorization_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if authorization_search_record_type is None:
            raise NullArgument()
        return False

    def get_function_record_types(self):
        """Gets the supported ``Function`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Function`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    function_record_types = property(fget=get_function_record_types)

    def supports_function_record_type(self, function_record_type=None):
        """Tests if the given ``Function`` record type is supported.

        arg:    function_record_type (osid.type.Type): a ``Type``
                indicating a ``Function`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``function_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if function_record_type is None:
            raise NullArgument()
        return False

    def get_function_search_record_types(self):
        """Gets the supported ``Function`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Function`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    function_search_record_types = property(fget=get_function_search_record_types)

    def supports_function_search_record_type(self, function_search_record_type=None):
        """Tests if the given ``Function`` search record type is supported.

        arg:    function_search_record_type (osid.type.Type): a ``Type``
                indicating a ``Function`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``function_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if function_search_record_type is None:
            raise NullArgument()
        return False

    def get_qualifier_record_types(self):
        """Gets the supported ``Qualifier`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Qualifier`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def supports_qualifier_record_type(self, qualifier_record_type=None):
        """Tests if the given ``Qualifier`` record type is supported.

        arg:    qualifier_record_type (osid.type.Type): a ``Type``
                indicating a ``Qualifier`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``qualifier_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if qualifier_record_type is None:
            raise NullArgument()
        return False

    def get_qualifier_search_record_types(self):
        """Gets the supported ``Qualifier`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Qualifier`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def supports_qualifier_search_record_type(self, qualifier_search_record_type=None):
        """Tests if the given ``Qualifier`` search record type is supported.

        arg:    qualifier_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``Qualifier`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``qualifier_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if qualifier_search_record_type is None:
            raise NullArgument()
        return False

    def get_vault_record_types(self):
        """Gets the supported ``Vault`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Vault`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    vault_record_types = property(fget=get_vault_record_types)

    def supports_vault_record_type(self, vault_record_type=None):
        """Tests if the given ``Vault`` record type is supported.

        arg:    vault_record_type (osid.type.Type): a ``Type``
                indicating a ``Vault`` type
        return: (boolean) - ``true`` if the given vault record ``Type``
                is supported, ``false`` otherwise
        raise:  NullArgument - ``vault_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if vault_record_type is None:
            raise NullArgument()
        return False

    def get_vault_search_record_types(self):
        """Gets the supported vault search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Vault`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def supports_vault_search_record_type(self, vault_search_record_type=None):
        """Tests if the given vault search record type is supported.

        arg:    vault_search_record_type (osid.type.Type): a ``Type``
                indicating a ``Vault`` search record type
        return: (boolean) - ``true`` if the given search record ``Type``
                is supported, ``false`` otherwise
        raise:  NullArgument - ``vault_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if vault_search_record_type is None:
            raise NullArgument()
        return False

    def get_authorization_condition_record_types(self):
        """Gets the supported ``AuthorizationCondition`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``AuthorizationCondition`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)

    def supports_authorization_condition_record_type(self, authorization_condition_record_type=None):
        """Tests if the given ``AuthorizationCondition`` record type is supported.

        arg:    authorization_condition_record_type (osid.type.Type): a
                ``Type`` indicating an ``AuthorizationCondition`` record
                type
        return: (boolean) - ``true`` if the given authorization
                condition record ``Type`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``authorization_condition_record_type``
                is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if authorization_condition_record_type is None:
            raise NullArgument()
        return False


class AuthorizationManager(abc_authorization_managers.AuthorizationManager, osid_managers.OsidManager, AuthorizationProfile):
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
        raise Unimplemented()

    authorization_session = property(fget=get_authorization_session)

    def get_authorization_session_for_vault(self, vault_id=None):
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
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

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
        raise Unimplemented()

    authorization_lookup_session = property(fget=get_authorization_lookup_session)

    def get_authorization_lookup_session_for_vault(self, vault_id=None):
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
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

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
        raise Unimplemented()

    authorization_query_session = property(fget=get_authorization_query_session)

    def get_authorization_query_session_for_vault(self, vault_id=None):
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
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_search_session(self):
        """Gets the ``OsidSession`` associated with the authorization search service.

        return: (osid.authorization.AuthorizationSearchSession) - an
                ``AuthorizationSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` is ``true``.*

        """
        raise Unimplemented()

    authorization_search_session = property(fget=get_authorization_search_session)

    def get_authorization_search_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the authorization search service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationSearchSession) - ``an
                _authorization_search_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

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
        raise Unimplemented()

    authorization_admin_session = property(fget=get_authorization_admin_session)

    def get_authorization_admin_session_for_vault(self, vault_id=None):
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
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_notification_session(self, authorization_receiver=None):
        """Gets the notification session for notifications pertaining to authorization changes.

        arg:    authorization_receiver
                (osid.authorization.AuthorizationReceiver): the
                authorization receiver
        return: (osid.authorization.AuthorizationNotificationSession) -
                an ``AuthorizationNotificationSession``
        raise:  NullArgument - ``authorization_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_authorization_notification()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_authorization_notification_session_for_vault(self, authorization_receiver=None, vault_id=None):
        """Gets the ``OsidSession`` associated with the authorization notification service for the given vault.

        arg:    authorization_receiver
                (osid.authorization.AuthorizationReceiver): the
                authorization receiver
        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationNotificationSession) -
                ``an _authorization_notification_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``authorization_receiver`` or
                ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_authorization_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if authorization_receiver is None:
            raise NullArgument
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

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
        raise Unimplemented()

    authorization_vault_session = property(fget=get_authorization_vault_session)

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
        raise Unimplemented()

    authorization_vault_assignment_session = property(fget=get_authorization_vault_assignment_session)

    def get_authorization_smart_vault_session(self, vault_id=None):
        """Gets the session for managing dynamic authorization vaults.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.AuthorizationSmartVaultSession) - a
                ``AuthorizationSmartVaultSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_smart_vault()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_smart_vault()`` is ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_lookup_session(self):
        """Gets the ``OsidSession`` associated with the function lookup service.

        return: (osid.authorization.FunctionLookupSession) - a
                ``FunctionLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    function_lookup_session = property(fget=get_function_lookup_session)

    def get_function_lookup_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the function lookup service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.FunctionLookupSession) - ``a
                FunctionLookupSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_query_session(self):
        """Gets the ``OsidSession`` associated with the function query service.

        return: (osid.authorization.FunctionQuerySession) - a
                ``FunctionQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` is ``true``.*

        """
        raise Unimplemented()

    function_query_session = property(fget=get_function_query_session)

    def get_function_query_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the function query service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.FunctionQuerySession) - a
                ``FunctionQuerySession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_search_session(self):
        """Gets the ``OsidSession`` associated with the function search service.

        return: (osid.authorization.FunctionSearchSession) - a
                ``FunctionSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` is ``true``.*

        """
        raise Unimplemented()

    function_search_session = property(fget=get_function_search_session)

    def get_function_search_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the function search service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.FunctionSearchSession) - a
                ``FunctionSearchSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_admin_session(self):
        """Gets the ``OsidSession`` associated with the function administration service.

        return: (osid.authorization.FunctionAdminSession) - a
                ``FunctionAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` is ``true``.*

        """
        raise Unimplemented()

    function_admin_session = property(fget=get_function_admin_session)

    def get_function_admin_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the function admin service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.FunctionAdminSession) - ``a
                FunctionAdminSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_notification_session(self, function_receiver=None):
        """Gets the notification session for notifications pertaining to function changes.

        arg:    function_receiver (osid.authorization.FunctionReceiver):
                the function receiver
        return: (osid.authorization.FunctionNotificationSession) - a
                ``FunctionNotificationSession``
        raise:  NullArgument - ``function_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_function_notification_session_for_vault(self, function_receiver=None, vault_id=None):
        """Gets the ``OsidSession`` associated with the function notification service for the given vault.

        arg:    function_receiver (osid.authorization.FunctionReceiver):
                the function receiver
        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.FunctionNotificationSession) - ``a
                FunctionNotificationSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``function_receiver`` or ``vault_id`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if function_receiver is None:
            raise NullArgument
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_vault_session(self):
        """Gets the session for retrieving function to vault mappings.

        return: (osid.authorization.FunctionVaultSession) - a
                ``FunctionVaultSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_vault()`` is ``true``.*

        """
        raise Unimplemented()

    function_vault_session = property(fget=get_function_vault_session)

    def get_function_vault_assignment_session(self):
        """Gets the session for assigning function to vault mappings.

        return: (osid.authorization.FunctionVaultAssignmentSession) - a
                ``FunctionVaultAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_vault_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_vault_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    function_vault_assignment_session = property(fget=get_function_vault_assignment_session)

    def get_function_smart_vault_session(self, vault_id=None):
        """Gets the session associated with the function smart vault for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.FunctionSmartVaultSession) - a
                ``FunctionSmartVaultSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_smart_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_smart_vault()`` is ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_lookup_session(self):
        """Gets the ``OsidSession`` associated with the qualifier lookup service.

        return: (osid.authorization.QualifierLookupSession) - a
                ``QualifierLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    qualifier_lookup_session = property(fget=get_qualifier_lookup_session)

    def get_qualifier_lookup_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the qualifier lookup service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.QualifierLookupSession) - a
                ``QualifierLookupSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_query_session(self):
        """Gets the ``OsidSession`` associated with the qualifier query service.

        return: (osid.authorization.QualifierQuerySession) - a
                ``QualifierQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_query()`` is ``true``.*

        """
        raise Unimplemented()

    qualifier_query_session = property(fget=get_qualifier_query_session)

    def get_qualifier_query_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the qualifier query service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.QualifierQuerySession) - a
                ``QualifierQuerySession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_search_session(self):
        """Gets the ``OsidSession`` associated with the qualifier search service.

        return: (osid.authorization.QualifierSearchSession) - a
                ``QualifierSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` is ``true``.*

        """
        raise Unimplemented()

    qualifier_search_session = property(fget=get_qualifier_search_session)

    def get_qualifier_search_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the qualifier search service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.QualifierSearchSession) - a
                ``QualifierSearchSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_admin_session(self):
        """Gets the ``OsidSession`` associated with the qualifier administration service.

        return: (osid.authorization.QualifierAdminSession) - a
                ``QualifierAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` is ``true``.*

        """
        raise Unimplemented()

    qualifier_admin_session = property(fget=get_qualifier_admin_session)

    def get_qualifier_admin_session_for_vault(self, vault_id=None):
        """Gets the ``OsidSession`` associated with the qualifier admin service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.QualifierAdminSession) - a
                ``QualifierAdminSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_notification_session(self, qualifier_receiver=None):
        """Gets the notification session for notifications pertaining to qualifier changes.

        arg:    qualifier_receiver
                (osid.authorization.QualifierReceiver): the qualifier
                receiver
        return: (osid.authorization.QualifierNotificationSession) - a
                ``QualifierNotificationSession``
        raise:  NullArgument - ``qualifier_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_qualifier_notification_session_for_vault(self, qualifier_receiver=None, vault_id=None):
        """Gets the ``OsidSession`` associated with the qualifier notification service for the given vault.

        arg:    qualifier_receiver
                (osid.authorization.QualifierReceiver): the qualifier
                receiver
        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.QualifierNotificationSession) - a
                ``QualifierNotificationSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``qualifier_receiver`` or ``vault_id`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if qualifier_receiver is None:
            raise NullArgument
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_hierarchy_session(self, qualifier_hierarchy_id=None):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy traversal service.

        The authorization service uses distinct hierarchies that can be
        managed through a Hierarchy OSID.

        arg:    qualifier_hierarchy_id (osid.id.Id): the ``Id`` of a
                qualifier hierarchy
        return: (osid.authorization.QualifierHierarchySession) - a
                ``QualifierHierarchySession``
        raise:  NotFound - ``qualifier_hierarchy_id`` not found
        raise:  NullArgument - ``qualifier_hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy()`` is ``true``.*

        """
        raise Unimplemented()

    def get_qualifier_hierarchy_design_session(self, qualifier_hierarchy_id=None):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy design service.

        arg:    qualifier_hierarchy_id (osid.id.Id): the ``Id`` of a
                qualifier hierarchy
        return: (osid.authorization.QualifierHierarchyDesignSession) - a
                ``QualifierHierarchyDesignSession``
        raise:  NotFound - ``qualifier_hierarchy_id`` not found
        raise:  NullArgument - ``qualifier_hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_qualifier_hierarchy_design()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy_design()`` is ``true``.*

        """
        raise Unimplemented()

    def get_qualifier_vault_session(self):
        """Gets the session for retrieving qualifier to vault mappings.

        return: (osid.authorization.QualifierVaultSession) - a
                ``QualifierVaultSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault()`` is ``true``.*

        """
        raise Unimplemented()

    qualifier_vault_session = property(fget=get_qualifier_vault_session)

    def get_qualifier_vault_assignment_session(self):
        """Gets the session for assigning qualifier to vault mappings.

        return: (osid.authorization.QualifierVaultSession) - a
                ``QualifierVaultAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_qualifier_vault_assignment()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    qualifier_vault_assignment_session = property(fget=get_qualifier_vault_assignment_session)

    def get_qualifier_smart_vault_session(self, vault_id=None):
        """Gets the session associated with the qualifier smart vault for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        return: (osid.authorization.QualifierSmartVaultSession) - a
                ``QualifierSmartVaultSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_smart_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_smart_vault()`` is ``true``.*

        """
        if vault_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_vault_lookup_session(self):
        """Gets the OsidSession associated with the vault lookup service.

        return: (osid.authorization.VaultLookupSession) - a
                ``VaultLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_lookup() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_lookup()`` is true.*

        """
        raise Unimplemented()

    vault_lookup_session = property(fget=get_vault_lookup_session)

    def get_vault_query_session(self):
        """Gets the OsidSession associated with the vault query service.

        return: (osid.authorization.VaultQuerySession) - a
                ``VaultQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_query() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_query()`` is true.*

        """
        raise Unimplemented()

    vault_query_session = property(fget=get_vault_query_session)

    def get_vault_search_session(self):
        """Gets the OsidSession associated with the vault search service.

        return: (osid.authorization.VaultSearchSession) - a
                ``VaultSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_search() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_search()`` is true.*

        """
        raise Unimplemented()

    vault_search_session = property(fget=get_vault_search_session)

    def get_vault_admin_session(self):
        """Gets the OsidSession associated with the vault administration service.

        return: (osid.authorization.VaultAdminSession) - a
                ``VaultAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_admin() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_admin()`` is true.*

        """
        raise Unimplemented()

    vault_admin_session = property(fget=get_vault_admin_session)

    def get_vault_notification_session(self, vaultreceiver=None):
        """Gets the notification session for notifications pertaining to vault service changes.

        arg:    vaultreceiver (osid.authorization.VaultReceiver): the
                vault receiver
        return: (osid.authorization.VaultNotificationSession) - a
                ``VaultNotificationSession``
        raise:  NullArgument - ``vault_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_notification() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_notification()`` is true.*

        """
        raise Unimplemented()

    def get_vault_hierarchy_session(self):
        """Gets the session traversing vault hierarchies.

        return: (osid.authorization.VaultHierarchySession) - a
                ``VaultHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_hierarchy() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy()`` is true.*

        """
        raise Unimplemented()

    vault_hierarchy_session = property(fget=get_vault_hierarchy_session)

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
        raise Unimplemented()

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
        raise Unimplemented()

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
        raise Unimplemented()

    authorization_rules_manager = property(fget=get_authorization_rules_manager)


class AuthorizationProxyManager(abc_authorization_managers.AuthorizationProxyManager, osid_managers.OsidProxyManager, AuthorizationProfile):
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

    def get_authorization_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_session_for_vault(self, vault_id=None, proxy=None):
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
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_lookup_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_lookup_session_for_vault(self, vault_id=None, proxy=None):
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
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_query_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_query_session_for_vault(self, vault_id=None, proxy=None):
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
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the authorization search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationSearchSession) - an
                ``AuthorizationSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_search_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the authorization search service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationSearchSession) - ``an
                _authorization_search_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_authorization_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_admin_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_admin_session_for_vault(self, vault_id=None, proxy=None):
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
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_notification_session(self, authorization_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to authorization changes.

        arg:    authorization_receiver
                (osid.authorization.AuthorizationReceiver): the
                authorization receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationNotificationSession) -
                an ``AuthorizationNotificationSession``
        raise:  NullArgument - ``authorization_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_authorization_notification()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_notification_session_for_vault(self, authorization_receiver=None, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the authorization notification service for the given vault.

        arg:    authorization_receiver
                (osid.authorization.AuthorizationReceiver): the
                authorization receiver
        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationNotificationSession) -
                ``an _authorization_notification_session``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``authorization_receiver`` or
                ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_authorization_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if authorization_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_authorization_vault_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_vault_assignment_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authorization_smart_vault_session(self, vault_id=None, proxy=None):
        """Gets the session for managing dynamic authorization vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.AuthorizationSmartVaultSession) - a
                ``AuthorizationSmartVaultSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authorization_smart_vault()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authorization_smart_vault()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the function lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionLookupSession) - a
                ``FunctionLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_lookup_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the function lookup service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionLookupSession) - ``a
                FunctionLookupSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the function query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionQuerySession) - a
                ``FunctionQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_query_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the function query service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionQuerySession) - a
                ``FunctionQuerySession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the function search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionSearchSession) - a
                ``FunctionSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_search_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the function search service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionSearchSession) - a
                ``FunctionSearchSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the function administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionAdminSession) - a
                ``FunctionAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_admin_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the function admin service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionAdminSession) - ``a
                FunctionAdminSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_notification_session(self, function_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to function changes.

        arg:    function_receiver (osid.authorization.FunctionReceiver):
                the function receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionNotificationSession) - a
                ``FunctionNotificationSession``
        raise:  NullArgument - ``function_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_notification_session_for_vault(self, function_receiver=None, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the function notification service for the given vault.

        arg:    function_receiver (osid.authorization.FunctionReceiver):
                the function receiver
        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionNotificationSession) - ``a
                FunctionNotificationSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``function_receiver`` or ``vault_id`` or
                ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_function_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if function_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_function_vault_session(self, proxy=None):
        """Gets the session for retrieving function to vault mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionVaultSession) - a
                ``FunctionVaultSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_vault()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_vault_assignment_session(self, proxy=None):
        """Gets the session for assigning function to vault mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionVaultAssignmentSession) - a
                ``FunctionVaultAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_vault_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_vault_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_function_smart_vault_session(self, vault_id=None, proxy=None):
        """Gets the session for managing dynamic function vaults for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of a vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.FunctionSmartVaultSession) -
                ``vault_id`` not found
        raise:  NotFound - ``vault_id`` or ``proxy`` is ``null``
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_function_smart_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_function_smart_vault()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierLookupSession) - a
                ``QualifierLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_lookup_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier lookup service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierLookupSession) - a
                ``QualifierLookupSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierQuerySession) - a
                ``QualifierQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_query_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier query service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierQuerySession) - a
                ``QualifierQuerySession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierSearchSession) - a
                ``QualifierSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_search_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier search service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierSearchSession) - a
                ``QualifierSearchSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierAdminSession) - a
                ``QualifierAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_admin_session_for_vault(self, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier admin service for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierAdminSession) - a
                ``QualifierAdminSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if vault_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_notification_session(self, qualifier_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to qualifier changes.

        arg:    qualifier_receiver
                (osid.authorization.QualifierReceiver): the qualifier
                receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierNotificationSession) - a
                ``QualifierNotificationSession``
        raise:  NullArgument - ``qualifier_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_notification_session_for_vault(self, qualifier_receiver=None, vault_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier notification service for the given vault.

        arg:    qualifier_receiver
                (osid.authorization.QualifierReceiver): the qualifier
                receiver
        arg:    vault_id (osid.id.Id): the ``Id`` of the vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierNotificationSession) - a
                ``QualifierNotificationSession``
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``qualifier_receiver`` or ``vault_id`` or
                ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_qualifier_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if qualifier_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_qualifier_hierarchy_session(self, qualifier_hierarchy_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy traversal service.

        The authorization service uses distinct hierarchies that can be
        managed through a Hierarchy OSID.

        arg:    qualifier_hierarchy_id (osid.id.Id): the ``Id`` of a
                qualifier hierarchy
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierHierarchySession) - a
                ``QualifierHierarchySession``
        raise:  NotFound - ``qualifier_hierarchy_id`` not found
        raise:  NullArgument - ``qualifier_hierarchy_id`` or ``proxy``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_hierarchy_design_session(self, qualifier_hierarchy_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy design service.

        arg:    qualifier_hierarchy_id (osid.id.Id): the ``Id`` of a
                qualifier hierarchy
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierHierarchyDesignSession) - a
                ``QualifierHierarchyDesignSession``
        raise:  NotFound - ``qualifier_hierarchy_id`` not found
        raise:  NullArgument - ``qualifier_hierarchy_id`` or ``proxy``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_qualifier_hierarchy_design()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy_design()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_vault_session(self, proxy=None):
        """Gets the session for retrieving qualifier to vault mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierVaultSession) - a
                ``QualifierVaultSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_vault_assignment_session(self, proxy=None):
        """Gets the session for assigning qualifier to vault mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierVaultSession) - a
                ``QualifierVaultAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_qualifier_vault_assignment()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_qualifier_smart_vault_session(self, vault_id=None, proxy=None):
        """Gets the session for managing dynamic qualifier vaults for the given vault.

        arg:    vault_id (osid.id.Id): the ``Id`` of a vault
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.QualifierSmartVaultSession) -
                ``vault_id`` not found
        raise:  NotFound - ``vault_id`` or ``proxy`` is ``null``
        raise:  NullArgument - ``vault_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_qualifier_smart_vault()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_smart_vault()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_lookup_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_query_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_search_session(self, proxy=None):
        """Gets the OsidSession associated with the vault search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultSearchSession) - a
                ``VaultSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_search() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_search()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_admin_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_notification_session(self, vault_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to vault service changes.

        arg:    vault_receiver (osid.authorization.VaultReceiver): the
                vault receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authorization.VaultNotificationSession) - a
                ``VaultNotificationSession``
        raise:  NullArgument - ``vault_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_vault_notification() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_vault_notification()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_hierarchy_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_vault_hierarchy_design_session(self, proxy=None):
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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

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
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)
