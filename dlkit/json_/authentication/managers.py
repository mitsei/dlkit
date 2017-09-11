"""JSON implementations of authentication managers."""

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
from dlkit.manager_impls.authentication import managers as authentication_managers


class AuthenticationProfile(osid_managers.OsidProfile, authentication_managers.AuthenticationProfile):
    """The ``AuthenticationProfile`` describes the interoperability among authentication services."""

    def supports_agent_lookup(self):
        """Tests if an agent lookup service is supported.

        An agent lookup service defines methods to access agents.

        return: (boolean) - ``true`` if agent lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_agent_lookup' in profile.SUPPORTS

    def get_agent_record_types(self):
        """Gets the supported ``Agent`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Agent`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AGENT_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    agent_record_types = property(fget=get_agent_record_types)

    def get_agent_search_record_types(self):
        """Gets the supported ``Agent`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Agent`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AGENT_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    agent_search_record_types = property(fget=get_agent_search_record_types)

    def get_agency_record_types(self):
        """Gets the supported ``Agency`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Agency`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AGENCY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    agency_record_types = property(fget=get_agency_record_types)

    def get_agency_search_record_types(self):
        """Gets the supported ``Agency`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Agency`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AGENCY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    agency_search_record_types = property(fget=get_agency_search_record_types)


class AuthenticationManager(osid_managers.OsidManager, AuthenticationProfile, authentication_managers.AuthenticationManager):
    """The authentication manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AgentLookupSession:`` a session to look up ``Agents``
      * ``AgentQuerySession:`` a session to query ``Agents``
      * ``AgentSearchSession:`` a session to search ``Agents``
      * ``AgentAdminSession:`` a session to create, modify and delete
        ``Agents``
      * ``AgentNotificationSession: a`` session to receive messages
        pertaining to ``Agent`` changes

      * ``AgentAgencySession:`` a session to retrieve ``Agent`` to
        ``Agency`` mappings
      * ``AgentAgencyAssignmentSession:`` a session to manage ``Agent``
        to ``Agency`` mappings
      * ``AgentSmartAgencySession:`` a session to create dynamic
        agencies
      * ``AgencyLookupSession:`` a session to lookup agencies
      * ``AgencyQuerySession:`` a session to query agencies
      * ``AgencySearchSession`` : a session to search agencies
      * ``AgencyAdminSession`` : a session to create, modify and delete
        agencies
      * ``AgencyNotificationSession`` : a session to receive messages
        pertaining to ``Agency`` changes
      * ``AgencyHierarchySession`` : a session to traverse the
        ``Agency`` hierarchy
      * ``AgencyHierarchyDesignSession`` : a session to manage the
        ``Agency`` hierarchy

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_agent_lookup_session(self):
        """Gets the ``OsidSession`` associated with the agent lookup service.

        return: (osid.authentication.AgentLookupSession) - an
                ``AgentLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_agent_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_lookup()`` is ``true``.*

        """
        if not self.supports_agent_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AgentLookupSession(runtime=self._runtime)

    agent_lookup_session = property(fget=get_agent_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_agent_lookup_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent lookup service for the given agency.

        arg:    agency_id (osid.id.Id): the ``Id`` of the agency
        return: (osid.authentication.AgentLookupSession) - ``an
                _agent_lookup_session``
        raise:  NotFound - ``agency_id`` not found
        raise:  NullArgument - ``agency_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_agent_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_agent_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AgentLookupSession(agency_id, runtime=self._runtime)

    def get_authentication_batch_manager(self):
        """Gets an ``AuthenticationBatchManager``.

        return: (osid.authentication.batch.AuthenticationBatchManager) -
                an ``AuthenticationBatchManager``.
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authentication_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    authentication_batch_manager = property(fget=get_authentication_batch_manager)

    def get_authentication_keys_manager(self):
        """Gets an ``AuthenticationKeysManager``.

        return: (osid.authentication.keys.AuthenticationKeysManager) -
                an ``AuthenticationKeysManager``.
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_keys()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authentication_keys()`` is ``true``.*

        """
        raise errors.Unimplemented()

    authentication_keys_manager = property(fget=get_authentication_keys_manager)

    def get_authentication_process_manager(self):
        """Gets an ``AuthenticationProcessManager``.

        return:
                (osid.authentication.process.AuthenticationProcessManage
                r) - an ``AuthenticationProcessManager``.
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_process()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authentication_process()`` is ``true``.*

        """
        raise errors.Unimplemented()

    authentication_process_manager = property(fget=get_authentication_process_manager)


class AuthenticationProxyManager(osid_managers.OsidProxyManager, AuthenticationProfile, authentication_managers.AuthenticationProxyManager):
    """The authentication proxy manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AgentLookupSession:`` session to look up ``Agents``
      * ``AgentQuerySession`` : a session to query ``Agents``
      * ``AgentSearchSession:`` session to search ``Agents``
      * ``AgentAdminSession:`` session to create, modify and delete
        ``Agents``
      * Agent ``NotificationSession:`` session to receive messages
        pertaining to ``Agent`` changes

      * ``AgentAgencySession:`` a session to retrieve ``Agent`` to
        ``Agency`` mappings
      * ``AgentAgencyAssignmentSession:`` a session to manage ``Agent``
        to ``Agency`` mappings
      * ``AgentSmartAgencySession:`` a session to create dynamic
        agencies
      * ``AgencyLookupSession:`` a session to lookup agencies
      * ``AgencyQuerySession:`` a session to query agencies
      * ``AgencySearchSession`` : a session to search agencies
      * ``AgencyAdminSession`` : a session to create, modify and delete
        agencies
      * ``AgencyNotificationSession`` : a session to receive messages
        pertaining to ``Agency`` changes
      * ``AgencyHierarchySession`` : a session to traverse the
        ``Agency`` hierarchy
      * ``AgencyHierarchyDesignSession`` : a session to manage the
        ``Agency`` hierarchy

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_agent_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authentication.AgentLookupSession) - an
                ``AgentLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_agent_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_lookup()`` is ``true``.*

        """
        if not self.supports_agent_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AgentLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_agent_lookup_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent lookup service for the given agency.

        arg:    agency_id (osid.id.Id): the ``Id`` of the agency
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authentication.AgentLookupSession) - ``an
                _agent_lookup_session``
        raise:  NotFound - ``agency_id`` not found
        raise:  NullArgument - ``agency_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_agent_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_agent_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AgentLookupSession(agency_id, proxy, self._runtime)

    def get_authentication_batch_proxy_manager(self):
        """Gets an ``AuthenticationBatchProxyManager``.

        return:
                (osid.authentication.batch.AuthenticationBatchProxyManag
                er) - an ``AuthenticationBatchProxyManager``.
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authentication_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    authentication_batch_proxy_manager = property(fget=get_authentication_batch_proxy_manager)

    def get_authentication_keys_proxy_manager(self):
        """Gets an ``AuthenticationKeysProxyManager``.

        return:
                (osid.authentication.keys.AuthenticationKeysProxyManager
                ) - an ``AuthenticationKeysProxyManager``.
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_keys()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authentication_keys()`` is ``true``.*

        """
        raise errors.Unimplemented()

    authentication_keys_proxy_manager = property(fget=get_authentication_keys_proxy_manager)

    def get_authentication_process_proxy_manager(self):
        """Gets an ``AuthenticationProcessProxyManager``.

        return:
                (osid.authentication.process.AuthenticationProcessProxyM
                anager) - an ``AuthenticationProcessproxyManager``.
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_process()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_authentication_process()`` is ``true``.*

        """
        raise errors.Unimplemented()

    authentication_process_proxy_manager = property(fget=get_authentication_process_proxy_manager)
