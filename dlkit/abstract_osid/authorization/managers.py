"""Implementations of authorization abstract base class managers."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class AuthorizationProfile:
    """The ``AuthorizationProfile`` describes the interoperability among authorization services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization(self):
        """Tests for the availability of an authorization service which is the basic service for checking authorizations.

        :return: ``true`` if authorization is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_lookup(self):
        """Tests if an authorization lookup service is supported.

        An authorization lookup service defines methods to access
        authorizations.

        :return: true if authorization lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_query(self):
        """Tests if an authorization query service is supported.

        :return: ``true`` if authorization query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_search(self):
        """Tests if an authorization search service is supported.

        :return: ``true`` if authorization search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_admin(self):
        """Tests if an authorization administrative service is supported.

        :return: ``true`` if authorization admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_notification(self):
        """Tests if authorization notification is supported.

        Messages may be sent when authorizations are created, modified,
        or deleted.

        :return: ``true`` if authorization notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_vault(self):
        """Tests if an authorization to vault lookup session is available.

        :return: ``true`` if authorization vault lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_vault_assignment(self):
        """Tests if an authorization to vault assignment session is available.

        :return: ``true`` if authorization vault assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_smart_vault(self):
        """Tests if an authorization smart vaulting session is available.

        :return: ``true`` if authorization smart vaulting is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_lookup(self):
        """Tests if a function lookup service is supported.

        A function lookup service defines methods to access
        authorization functions.

        :return: ``true`` if function lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_query(self):
        """Tests if a function query service is supported.

        :return: ``true`` if function query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_search(self):
        """Tests if a function search service is supported.

        :return: ``true`` if function search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_admin(self):
        """Tests if a function administrative service is supported.

        :return: ``true`` if function admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_notification(self):
        """Tests if function notification is supported.

        Messages may be sent when functions are created, modified, or
        deleted.

        :return: ``true`` if function notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_vault(self):
        """Tests if a function to vault lookup session is available.

        :return: ``true`` if function vault lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_vault_assignment(self):
        """Tests if a function to vault assignment session is available.

        :return: ``true`` if function vault assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_function_smart_vault(self):
        """Tests if a function smart vaulting session is available.

        :return: ``true`` if function smart vaulting is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_lookup(self):
        """Tests if a qualifier lookup service is supported.

        A function lookup service defines methods to access
        authorization qualifiers.

        :return: ``true`` if qualifier lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_query(self):
        """Tests if a qualifier query service is supported.

        :return: ``true`` if qualifier query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_search(self):
        """Tests if a qualifier search service is supported.

        :return: ``true`` if qualifier search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_admin(self):
        """Tests if a qualifier administrative service is supported.

        :return: ``true`` if qualifier admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_notification(self):
        """Tests if qualifier notification is supported.

        Messages may be sent when qualifiers are created, modified, or
        deleted.

        :return: ``true`` if qualifier notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_hierarchy(self):
        """Tests if a qualifier hierarchy traversal is supported.

        :return: ``true`` if a qualifier hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_hierarchy_design(self):
        """Tests if qualifier hierarchy design is supported.

        :return: ``true`` if a qualifier hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_vault(self):
        """Tests if a qualifier to vault lookup session is available.

        :return: ``true`` if qualifier vault lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_vault_assignment(self):
        """Tests if a qualifier to vault assignment session is available.

        :return: ``true`` if qualifier vault assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_qualifier_smart_vault(self):
        """Tests if a qualifier smart vaulting session is available.

        :return: ``true`` if qualifier smart vault session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_lookup(self):
        """Tests if a vault lookup service is supported.

        A vault lookup service defines methods to access authorization
        vaults.

        :return: ``true`` if function lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_query(self):
        """Tests if a vault query service is supported.

        :return: ``true`` if vault query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_search(self):
        """Tests if a vault search service is supported.

        :return: ``true`` if vault search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_admin(self):
        """Tests if a vault administrative service is supported.

        :return: ``true`` if vault admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_notification(self):
        """Tests if vault notification is supported.

        Messages may be sent when vaults are created, modified, or
        deleted.

        :return: ``true`` if vault notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_hierarchy(self):
        """Tests if a vault hierarchy traversal is supported.

        :return: ``true`` if a vault hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_vault_hierarchy_design(self):
        """Tests if vault hierarchy design is supported.

        :return: ``true`` if a function hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_batch(self):
        """Tests if an authorization batch service is supported.

        :return: ``true`` if an authorization batch service design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authorization_rules(self):
        """Tests if an authorization rules service is supported.

        :return: ``true`` if an authorization rules service design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_record_types(self):
        """Gets the supported ``Authorization`` record types.

        :return: a list containing the supported authorization record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    authorization_record_types = property(fget=get_authorization_record_types)

    @abc.abstractmethod
    def supports_authorization_record_type(self, authorization_record_type):
        """Tests if the given authorization record type is supported.

        :param authorization_record_type: a ``Type`` indicating an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_search_record_types(self):
        """Gets the supported ``Authorization`` search record types.

        :return: a list containing the supported authorization search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    @abc.abstractmethod
    def supports_authorization_search_record_type(self, authorization_search_record_type):
        """Tests if the given authorization search record type is supported.

        :param authorization_search_record_type: a ``Type`` indicating an authorization search record type
        :type authorization_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_function_record_types(self):
        """Gets the supported ``Function`` record types.

        :return: a list containing the supported ``Function`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    function_record_types = property(fget=get_function_record_types)

    @abc.abstractmethod
    def supports_function_record_type(self, function_record_type):
        """Tests if the given ``Function`` record type is supported.

        :param function_record_type: a ``Type`` indicating a ``Function`` record type
        :type function_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_function_search_record_types(self):
        """Gets the supported ``Function`` search record types.

        :return: a list containing the supported ``Function`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    function_search_record_types = property(fget=get_function_search_record_types)

    @abc.abstractmethod
    def supports_function_search_record_type(self, function_search_record_type):
        """Tests if the given ``Function`` search record type is supported.

        :param function_search_record_type: a ``Type`` indicating a ``Function`` search record type
        :type function_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``function_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_record_types(self):
        """Gets the supported ``Qualifier`` record types.

        :return: a list containing the supported ``Qualifier`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    qualifier_record_types = property(fget=get_qualifier_record_types)

    @abc.abstractmethod
    def supports_qualifier_record_type(self, qualifier_record_type):
        """Tests if the given ``Qualifier`` record type is supported.

        :param qualifier_record_type: a ``Type`` indicating a ``Qualifier`` record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_search_record_types(self):
        """Gets the supported ``Qualifier`` search record types.

        :return: a list containing the supported ``Qualifier`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    @abc.abstractmethod
    def supports_qualifier_search_record_type(self, qualifier_search_record_type):
        """Tests if the given ``Qualifier`` search record type is supported.

        :param qualifier_search_record_type: a ``Type`` indicating a ``Qualifier`` search record type
        :type qualifier_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_vault_record_types(self):
        """Gets the supported ``Vault`` record types.

        :return: a list containing the supported ``Vault`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    vault_record_types = property(fget=get_vault_record_types)

    @abc.abstractmethod
    def supports_vault_record_type(self, vault_record_type):
        """Tests if the given ``Vault`` record type is supported.

        :param vault_record_type: a ``Type`` indicating a ``Vault`` type
        :type vault_record_type: ``osid.type.Type``
        :return: ``true`` if the given vault record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_vault_search_record_types(self):
        """Gets the supported vault search record types.

        :return: a list containing the supported ``Vault`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    vault_search_record_types = property(fget=get_vault_search_record_types)

    @abc.abstractmethod
    def supports_vault_search_record_type(self, vault_search_record_type):
        """Tests if the given vault search record type is supported.

        :param vault_search_record_type: a ``Type`` indicating a ``Vault`` search record type
        :type vault_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_condition_record_types(self):
        """Gets the supported ``AuthorizationCondition`` record types.

        :return: a list containing the supported ``AuthorizationCondition`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)

    @abc.abstractmethod
    def supports_authorization_condition_record_type(self, authorization_condition_record_type):
        """Tests if the given ``AuthorizationCondition`` record type is supported.

        :param authorization_condition_record_type: a ``Type`` indicating an ``AuthorizationCondition`` record type
        :type authorization_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given authorization condition record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_condition_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class AuthorizationManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authorization_session(self):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks.

        :return: an authorization session for this service
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationSession

    authorization_session = property(fget=get_authorization_session)

    @abc.abstractmethod
    def get_authorization_session_for_vault(self, vault_id):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_session``
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``NotFound`` -- ``vault_id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationSession

    @abc.abstractmethod
    def get_authorization_lookup_session(self):
        """Gets the ``OsidSession`` associated with the authorization lookup service.

        :return: an ``AuthorizationLookupSession``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationLookupSession

    authorization_lookup_session = property(fget=get_authorization_lookup_session)

    @abc.abstractmethod
    def get_authorization_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_lookup_session``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationLookupSession

    @abc.abstractmethod
    def get_authorization_query_session(self):
        """Gets the ``OsidSession`` associated with the authorization query service.

        :return: an ``AuthorizationQuerySession``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationQuerySession

    authorization_query_session = property(fget=get_authorization_query_session)

    @abc.abstractmethod
    def get_authorization_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_query_session``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationQuerySession

    @abc.abstractmethod
    def get_authorization_search_session(self):
        """Gets the ``OsidSession`` associated with the authorization search service.

        :return: an ``AuthorizationSearchSession``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationSearchSession

    authorization_search_session = property(fget=get_authorization_search_session)

    @abc.abstractmethod
    def get_authorization_search_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_search_session``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationSearchSession

    @abc.abstractmethod
    def get_authorization_admin_session(self):
        """Gets the ``OsidSession`` associated with the authorization administration service.

        :return: an ``AuthorizationAdminSession``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationAdminSession

    authorization_admin_session = property(fget=get_authorization_admin_session)

    @abc.abstractmethod
    def get_authorization_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_admin_session``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationAdminSession

    @abc.abstractmethod
    def get_authorization_notification_session(self, authorization_receiver):
        """Gets the notification session for notifications pertaining to authorization changes.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :return: an ``AuthorizationNotificationSession``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NullArgument`` -- ``authorization_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationNotificationSession

    @abc.abstractmethod
    def get_authorization_notification_session_for_vault(self, authorization_receiver, vault_id):
        """Gets the ``OsidSession`` associated with the authorization notification service for the given vault.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_notification_session``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``authorization_receiver`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationNotificationSession

    @abc.abstractmethod
    def get_authorization_vault_session(self):
        """Gets the session for retrieving authorization to vault mappings.

        :return: an ``AuthorizationVaultSession``
        :rtype: ``osid.authorization.AuthorizationVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationVaultSession

    authorization_vault_session = property(fget=get_authorization_vault_session)

    @abc.abstractmethod
    def get_authorization_vault_assignment_session(self):
        """Gets the session for assigning authorizations to vault mappings.

        :return: a ``AuthorizationVaultAssignmentSession``
        :rtype: ``osid.authorization.AuthorizationVaultAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault_assignment()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationVaultAssignmentSession

    authorization_vault_assignment_session = property(fget=get_authorization_vault_assignment_session)

    @abc.abstractmethod
    def get_authorization_smart_vault_session(self, vault_id):
        """Gets the session for managing dynamic authorization vaults.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``AuthorizationSmartVaultSession``
        :rtype: ``osid.authorization.AuthorizationSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_smart_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_smart_vault()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationSmartVaultSession

    @abc.abstractmethod
    def get_function_lookup_session(self):
        """Gets the ``OsidSession`` associated with the function lookup service.

        :return: a ``FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` is ``true``.*

        """
        return  # osid.authorization.FunctionLookupSession

    function_lookup_session = property(fget=get_function_lookup_session)

    @abc.abstractmethod
    def get_function_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``a FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionLookupSession

    @abc.abstractmethod
    def get_function_query_session(self):
        """Gets the ``OsidSession`` associated with the function query service.

        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` is ``true``.*

        """
        return  # osid.authorization.FunctionQuerySession

    function_query_session = property(fget=get_function_query_session)

    @abc.abstractmethod
    def get_function_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionQuerySession

    @abc.abstractmethod
    def get_function_search_session(self):
        """Gets the ``OsidSession`` associated with the function search service.

        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` is ``true``.*

        """
        return  # osid.authorization.FunctionSearchSession

    function_search_session = property(fget=get_function_search_session)

    @abc.abstractmethod
    def get_function_search_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionSearchSession

    @abc.abstractmethod
    def get_function_admin_session(self):
        """Gets the ``OsidSession`` associated with the function administration service.

        :return: a ``FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` is ``true``.*

        """
        return  # osid.authorization.FunctionAdminSession

    function_admin_session = property(fget=get_function_admin_session)

    @abc.abstractmethod
    def get_function_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``a FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionAdminSession

    @abc.abstractmethod
    def get_function_notification_session(self, function_receiver):
        """Gets the notification session for notifications pertaining to function changes.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :return: a ``FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NullArgument`` -- ``function_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` is ``true``.*

        """
        return  # osid.authorization.FunctionNotificationSession

    @abc.abstractmethod
    def get_function_notification_session_for_vault(self, function_receiver, vault_id):
        """Gets the ``OsidSession`` associated with the function notification service for the given vault.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``a FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``function_receiver`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionNotificationSession

    @abc.abstractmethod
    def get_function_vault_session(self):
        """Gets the session for retrieving function to vault mappings.

        :return: a ``FunctionVaultSession``
        :rtype: ``osid.authorization.FunctionVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_vault()`` is ``true``.*

        """
        return  # osid.authorization.FunctionVaultSession

    function_vault_session = property(fget=get_function_vault_session)

    @abc.abstractmethod
    def get_function_vault_assignment_session(self):
        """Gets the session for assigning function to vault mappings.

        :return: a ``FunctionVaultAssignmentSession``
        :rtype: ``osid.authorization.FunctionVaultAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_vault_assignment()`` is ``true``.*

        """
        return  # osid.authorization.FunctionVaultAssignmentSession

    function_vault_assignment_session = property(fget=get_function_vault_assignment_session)

    @abc.abstractmethod
    def get_function_smart_vault_session(self, vault_id):
        """Gets the session associated with the function smart vault for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``FunctionSmartVaultSession``
        :rtype: ``osid.authorization.FunctionSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_smart_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_smart_vault()`` is ``true``.*

        """
        return  # osid.authorization.FunctionSmartVaultSession

    @abc.abstractmethod
    def get_qualifier_lookup_session(self):
        """Gets the ``OsidSession`` associated with the qualifier lookup service.

        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` is ``true``.*

        """
        return  # osid.authorization.QualifierLookupSession

    qualifier_lookup_session = property(fget=get_qualifier_lookup_session)

    @abc.abstractmethod
    def get_qualifier_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierLookupSession

    @abc.abstractmethod
    def get_qualifier_query_session(self):
        """Gets the ``OsidSession`` associated with the qualifier query service.

        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_query()`` is ``true``.*

        """
        return  # osid.authorization.QualifierQuerySession

    qualifier_query_session = property(fget=get_qualifier_query_session)

    @abc.abstractmethod
    def get_qualifier_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierQuerySession

    @abc.abstractmethod
    def get_qualifier_search_session(self):
        """Gets the ``OsidSession`` associated with the qualifier search service.

        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` is ``true``.*

        """
        return  # osid.authorization.QualifierSearchSession

    qualifier_search_session = property(fget=get_qualifier_search_session)

    @abc.abstractmethod
    def get_qualifier_search_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierSearchSession

    @abc.abstractmethod
    def get_qualifier_admin_session(self):
        """Gets the ``OsidSession`` associated with the qualifier administration service.

        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` is ``true``.*

        """
        return  # osid.authorization.QualifierAdminSession

    qualifier_admin_session = property(fget=get_qualifier_admin_session)

    @abc.abstractmethod
    def get_qualifier_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierAdminSession

    @abc.abstractmethod
    def get_qualifier_notification_session(self, qualifier_receiver):
        """Gets the notification session for notifications pertaining to qualifier changes.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NullArgument`` -- ``qualifier_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` is ``true``.*

        """
        return  # osid.authorization.QualifierNotificationSession

    @abc.abstractmethod
    def get_qualifier_notification_session_for_vault(self, qualifier_receiver, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier notification service for the given vault.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_receiver`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierNotificationSession

    @abc.abstractmethod
    def get_qualifier_hierarchy_session(self, qualifier_hierarchy_id):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy traversal service.

        The authorization service uses distinct hierarchies that can be
        managed through a Hierarchy OSID.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :return: a ``QualifierHierarchySession``
        :rtype: ``osid.authorization.QualifierHierarchySession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy()`` is ``true``.*

        """
        return  # osid.authorization.QualifierHierarchySession

    @abc.abstractmethod
    def get_qualifier_hierarchy_design_session(self, qualifier_hierarchy_id):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy design service.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :return: a ``QualifierHierarchyDesignSession``
        :rtype: ``osid.authorization.QualifierHierarchyDesignSession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy_design()`` is ``true``.*

        """
        return  # osid.authorization.QualifierHierarchyDesignSession

    @abc.abstractmethod
    def get_qualifier_vault_session(self):
        """Gets the session for retrieving qualifier to vault mappings.

        :return: a ``QualifierVaultSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault()`` is ``true``.*

        """
        return  # osid.authorization.QualifierVaultSession

    qualifier_vault_session = property(fget=get_qualifier_vault_session)

    @abc.abstractmethod
    def get_qualifier_vault_assignment_session(self):
        """Gets the session for assigning qualifier to vault mappings.

        :return: a ``QualifierVaultAssignmentSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault_assignment()`` is ``true``.*

        """
        return  # osid.authorization.QualifierVaultSession

    qualifier_vault_assignment_session = property(fget=get_qualifier_vault_assignment_session)

    @abc.abstractmethod
    def get_qualifier_smart_vault_session(self, vault_id):
        """Gets the session associated with the qualifier smart vault for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierSmartVaultSession``
        :rtype: ``osid.authorization.QualifierSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_smart_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_smart_vault()`` is ``true``.*

        """
        return  # osid.authorization.QualifierSmartVaultSession

    @abc.abstractmethod
    def get_vault_lookup_session(self):
        """Gets the OsidSession associated with the vault lookup service.

        :return: a ``VaultLookupSession``
        :rtype: ``osid.authorization.VaultLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_lookup()`` is true.*

        """
        return  # osid.authorization.VaultLookupSession

    vault_lookup_session = property(fget=get_vault_lookup_session)

    @abc.abstractmethod
    def get_vault_query_session(self):
        """Gets the OsidSession associated with the vault query service.

        :return: a ``VaultQuerySession``
        :rtype: ``osid.authorization.VaultQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_query()`` is true.*

        """
        return  # osid.authorization.VaultQuerySession

    vault_query_session = property(fget=get_vault_query_session)

    @abc.abstractmethod
    def get_vault_search_session(self):
        """Gets the OsidSession associated with the vault search service.

        :return: a ``VaultSearchSession``
        :rtype: ``osid.authorization.VaultSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_search()`` is true.*

        """
        return  # osid.authorization.VaultSearchSession

    vault_search_session = property(fget=get_vault_search_session)

    @abc.abstractmethod
    def get_vault_admin_session(self):
        """Gets the OsidSession associated with the vault administration service.

        :return: a ``VaultAdminSession``
        :rtype: ``osid.authorization.VaultAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_admin()`` is true.*

        """
        return  # osid.authorization.VaultAdminSession

    vault_admin_session = property(fget=get_vault_admin_session)

    @abc.abstractmethod
    def get_vault_notification_session(self, vaultreceiver):
        """Gets the notification session for notifications pertaining to vault service changes.

        :param vaultreceiver: the vault receiver
        :type vaultreceiver: ``osid.authorization.VaultReceiver``
        :return: a ``VaultNotificationSession``
        :rtype: ``osid.authorization.VaultNotificationSession``
        :raise: ``NullArgument`` -- ``vault_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_notification()`` is true.*

        """
        return  # osid.authorization.VaultNotificationSession

    @abc.abstractmethod
    def get_vault_hierarchy_session(self):
        """Gets the session traversing vault hierarchies.

        :return: a ``VaultHierarchySession``
        :rtype: ``osid.authorization.VaultHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy()`` is true.*

        """
        return  # osid.authorization.VaultHierarchySession

    vault_hierarchy_session = property(fget=get_vault_hierarchy_session)

    @abc.abstractmethod
    def get_vault_hierarchy_design_session(self):
        """Gets the session designing vault hierarchies.

        :return: a ``VaultHierarchyDesignSession``
        :rtype: ``osid.authorization.VaultHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy_design()`` is true.*

        """
        return  # osid.authorization.VaultHierarchyDesignSession

    vault_hierarchy_design_session = property(fget=get_vault_hierarchy_design_session)

    @abc.abstractmethod
    def get_authorization_batch_manager(self):
        """Gets an ``AuthorizationBatchManager``.

        :return: an ``AuthorizationBatchManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_batch()`` is true.*

        """
        return  # osid.authorization.batch.AuthorizationBatchManager

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    @abc.abstractmethod
    def get_authorization_rules_manager(self):
        """Gets an ``AuthorizationRulesManager``.

        :return: an ``AuthorizationRulesManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_rules()`` is true.*

        """
        return  # osid.authorization.rules.AuthorizationRulesManager

    authorization_rules_manager = property(fget=get_authorization_rules_manager)


class AuthorizationProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authorization_session(self, proxy):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an authorization session for this service
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationSession

    @abc.abstractmethod
    def get_authorization_session_for_vault(self, vault_id, proxy):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_session``
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationSession

    @abc.abstractmethod
    def get_authorization_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationLookupSession``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationLookupSession

    @abc.abstractmethod
    def get_authorization_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_lookup_session``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationLookupSession

    @abc.abstractmethod
    def get_authorization_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationQuerySession``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationQuerySession

    @abc.abstractmethod
    def get_authorization_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_query_session``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationQuerySession

    @abc.abstractmethod
    def get_authorization_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationSearchSession``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationSearchSession

    @abc.abstractmethod
    def get_authorization_search_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_search_session``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationSearchSession

    @abc.abstractmethod
    def get_authorization_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationAdminSession``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationAdminSession

    @abc.abstractmethod
    def get_authorization_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_admin_session``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationAdminSession

    @abc.abstractmethod
    def get_authorization_notification_session(self, authorization_receiver, proxy):
        """Gets the notification session for notifications pertaining to authorization changes.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationNotificationSession``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NullArgument`` -- ``authorization_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationNotificationSession

    @abc.abstractmethod
    def get_authorization_notification_session_for_vault(self, authorization_receiver, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization notification service for the given vault.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_notification_session``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``authorization_receiver`` or ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.AuthorizationNotificationSession

    @abc.abstractmethod
    def get_authorization_vault_session(self, proxy):
        """Gets the session for retrieving authorization to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationVaultSession``
        :rtype: ``osid.authorization.AuthorizationVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationVaultSession

    @abc.abstractmethod
    def get_authorization_vault_assignment_session(self, proxy):
        """Gets the session for assigning authorization to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``AuthorizationVaultAssignmentSession``
        :rtype: ``osid.authorization.AuthorizationVaultAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_vault_assignment()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationVaultAssignmentSession

    @abc.abstractmethod
    def get_authorization_smart_vault_session(self, vault_id, proxy):
        """Gets the session for managing dynamic authorization vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``AuthorizationSmartVaultSession``
        :rtype: ``osid.authorization.AuthorizationSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_smart_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_smart_vault()`` is ``true``.*

        """
        return  # osid.authorization.AuthorizationSmartVaultSession

    @abc.abstractmethod
    def get_function_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` is ``true``.*

        """
        return  # osid.authorization.FunctionLookupSession

    @abc.abstractmethod
    def get_function_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionLookupSession

    @abc.abstractmethod
    def get_function_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` is ``true``.*

        """
        return  # osid.authorization.FunctionQuerySession

    @abc.abstractmethod
    def get_function_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionQuerySession

    @abc.abstractmethod
    def get_function_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` is ``true``.*

        """
        return  # osid.authorization.FunctionSearchSession

    @abc.abstractmethod
    def get_function_search_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionSearchSession

    @abc.abstractmethod
    def get_function_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` is ``true``.*

        """
        return  # osid.authorization.FunctionAdminSession

    @abc.abstractmethod
    def get_function_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionAdminSession

    @abc.abstractmethod
    def get_function_notification_session(self, function_receiver, proxy):
        """Gets the notification session for notifications pertaining to function changes.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NullArgument`` -- ``function_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` is ``true``.*

        """
        return  # osid.authorization.FunctionNotificationSession

    @abc.abstractmethod
    def get_function_notification_session_for_vault(self, function_receiver, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function notification service for the given vault.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``function_receiver`` or ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.FunctionNotificationSession

    @abc.abstractmethod
    def get_function_vault_session(self, proxy):
        """Gets the session for retrieving function to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionVaultSession``
        :rtype: ``osid.authorization.FunctionVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_vault()`` is ``true``.*

        """
        return  # osid.authorization.FunctionVaultSession

    @abc.abstractmethod
    def get_function_vault_assignment_session(self, proxy):
        """Gets the session for assigning function to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionVaultAssignmentSession``
        :rtype: ``osid.authorization.FunctionVaultAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_vault_assignment()`` is ``true``.*

        """
        return  # osid.authorization.FunctionVaultAssignmentSession

    @abc.abstractmethod
    def get_function_smart_vault_session(self, vault_id, proxy):
        """Gets the session for managing dynamic function vaults for the given vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``vault_id`` not found
        :rtype: ``osid.authorization.FunctionSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_smart_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_function_smart_vault()`` is ``true``.*

        """
        return  # osid.authorization.FunctionSmartVaultSession

    @abc.abstractmethod
    def get_qualifier_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` is ``true``.*

        """
        return  # osid.authorization.QualifierLookupSession

    @abc.abstractmethod
    def get_qualifier_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierLookupSession

    @abc.abstractmethod
    def get_qualifier_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` is ``true``.*

        """
        return  # osid.authorization.QualifierQuerySession

    @abc.abstractmethod
    def get_qualifier_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierQuerySession

    @abc.abstractmethod
    def get_qualifier_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` is ``true``.*

        """
        return  # osid.authorization.QualifierSearchSession

    @abc.abstractmethod
    def get_qualifier_search_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierSearchSession

    @abc.abstractmethod
    def get_qualifier_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` is ``true``.*

        """
        return  # osid.authorization.QualifierAdminSession

    @abc.abstractmethod
    def get_qualifier_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierAdminSession

    @abc.abstractmethod
    def get_qualifier_notification_session(self, qualifier_receiver, proxy):
        """Gets the notification session for notifications pertaining to qualifier changes.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NullArgument`` -- ``qualifier_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` is ``true``.*

        """
        return  # osid.authorization.QualifierNotificationSession

    @abc.abstractmethod
    def get_qualifier_notification_session_for_vault(self, qualifier_receiver, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier notification service for the given vault.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_receiver`` or ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authorization.QualifierNotificationSession

    @abc.abstractmethod
    def get_qualifier_hierarchy_session(self, qualifier_hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy traversal service.

        The authorization service uses distinct hierarchies that can be
        managed through a Hierarchy OSID.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierHierarchySession``
        :rtype: ``osid.authorization.QualifierHierarchySession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy()`` is ``true``.*

        """
        return  # osid.authorization.QualifierHierarchySession

    @abc.abstractmethod
    def get_qualifier_hierarchy_design_session(self, qualifier_hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy design service.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierHierarchyDesignSession``
        :rtype: ``osid.authorization.QualifierHierarchyDesignSession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy_design()`` is ``true``.*

        """
        return  # osid.authorization.QualifierHierarchyDesignSession

    @abc.abstractmethod
    def get_qualifier_vault_session(self, proxy):
        """Gets the session for retrieving qualifier to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierVaultSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault()`` is ``true``.*

        """
        return  # osid.authorization.QualifierVaultSession

    @abc.abstractmethod
    def get_qualifier_vault_assignment_session(self, proxy):
        """Gets the session for assigning qualifier to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierVaultAssignmentSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_vault_assignment()`` is ``true``.*

        """
        return  # osid.authorization.QualifierVaultSession

    @abc.abstractmethod
    def get_qualifier_smart_vault_session(self, vault_id, proxy):
        """Gets the session for managing dynamic qualifier vaults for the given vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``vault_id`` not found
        :rtype: ``osid.authorization.QualifierSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_smart_vault()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_smart_vault()`` is ``true``.*

        """
        return  # osid.authorization.QualifierSmartVaultSession

    @abc.abstractmethod
    def get_vault_lookup_session(self, proxy):
        """Gets the OsidSession associated with the vault lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultLookupSession``
        :rtype: ``osid.authorization.VaultLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_lookup()`` is true.*

        """
        return  # osid.authorization.VaultLookupSession

    @abc.abstractmethod
    def get_vault_query_session(self, proxy):
        """Gets the OsidSession associated with the vault query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultQuerySession``
        :rtype: ``osid.authorization.VaultQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_query()`` is true.*

        """
        return  # osid.authorization.VaultQuerySession

    @abc.abstractmethod
    def get_vault_search_session(self, proxy):
        """Gets the OsidSession associated with the vault search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultSearchSession``
        :rtype: ``osid.authorization.VaultSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_search()`` is true.*

        """
        return  # osid.authorization.VaultSearchSession

    @abc.abstractmethod
    def get_vault_admin_session(self, proxy):
        """Gets the OsidSession associated with the vault administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultAdminSession``
        :rtype: ``osid.authorization.VaultAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_admin()`` is true.*

        """
        return  # osid.authorization.VaultAdminSession

    @abc.abstractmethod
    def get_vault_notification_session(self, vault_receiver, proxy):
        """Gets the notification session for notifications pertaining to vault service changes.

        :param vault_receiver: the vault receiver
        :type vault_receiver: ``osid.authorization.VaultReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultNotificationSession``
        :rtype: ``osid.authorization.VaultNotificationSession``
        :raise: ``NullArgument`` -- ``vault_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_notification()`` is true.*

        """
        return  # osid.authorization.VaultNotificationSession

    @abc.abstractmethod
    def get_vault_hierarchy_session(self, proxy):
        """Gets the session traversing vault hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultHierarchySession``
        :rtype: ``osid.authorization.VaultHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy()`` is true.*

        """
        return  # osid.authorization.VaultHierarchySession

    @abc.abstractmethod
    def get_vault_hierarchy_design_session(self, proxy):
        """Gets the session designing vault hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultHierarchySession``
        :rtype: ``osid.authorization.VaultHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_vault_hierarchy_design()`` is true.*

        """
        return  # osid.authorization.VaultHierarchyDesignSession

    @abc.abstractmethod
    def get_authorization_batch_proxy_manager(self):
        """Gets an ``AuthorizationBatchProxyManager``.

        :return: an ``AuthorizationBatchProxyManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_batch()`` is true.*

        """
        return  # osid.authorization.batch.AuthorizationBatchProxyManager

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    @abc.abstractmethod
    def get_authorization_rules_proxy_manager(self):
        """Gets an ``AuthorizationRulesProxyManager``.

        :return: an ``AuthorizationRulesProxyManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_rules()`` is true.*

        """
        return  # osid.authorization.rules.AuthorizationRulesProxyManager

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)
