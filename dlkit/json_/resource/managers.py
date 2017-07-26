"""JSON implementations of resource managers."""

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
from dlkit.manager_impls.resource import managers as resource_managers


class ResourceProfile(osid_managers.OsidProfile, resource_managers.ResourceProfile):
    """The resource profile describes interoperability among resource services."""

    def supports_resource_lookup(self):
        """Tests if resource lookup is supported.

        return: (boolean) - ``true`` if resource lookup is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_lookup' in profile.SUPPORTS

    def supports_resource_query(self):
        """Tests if resource query is supported.

        return: (boolean) - ``true`` if resource query is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_query' in profile.SUPPORTS

    def supports_resource_search(self):
        """Tests if resource search is supported.

        return: (boolean) - ``true`` if resource search is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_search' in profile.SUPPORTS

    def supports_resource_admin(self):
        """Tests if resource administration is supported.

        return: (boolean) - ``true`` if resource administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_admin' in profile.SUPPORTS

    def supports_resource_notification(self):
        """Tests if resource notification is supported.

        Messages may be sent when resources are created, modified, or
        deleted.

        return: (boolean) - ``true`` if resource notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_notification' in profile.SUPPORTS

    def supports_resource_bin(self):
        """Tests if retrieving mappings of resource and bins is supported.

        return: (boolean) - ``true`` if resource bin mapping retrieval
                is supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_bin' in profile.SUPPORTS

    def supports_resource_bin_assignment(self):
        """Tests if managing mappings of resource and bins is supported.

        return: (boolean) - ``true`` if resource bin assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_bin_assignment' in profile.SUPPORTS

    def supports_resource_agent(self):
        """Tests if retrieving mappings of resource and agents is supported.

        return: (boolean) - ``true`` if resource agent mapping retrieval
                is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_agent' in profile.SUPPORTS

    def supports_resource_agent_assignment(self):
        """Tests if managing mappings of resources and agents is supported.

        return: (boolean) - ``true`` if resource agent assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_resource_agent_assignment' in profile.SUPPORTS

    def supports_bin_lookup(self):
        """Tests if bin lookup is supported.

        return: (boolean) - ``true`` if bin lookup is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_bin_lookup' in profile.SUPPORTS

    def supports_bin_query(self):
        """Tests if bin query is supported.

        return: (boolean) - ``true`` if bin query is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_bin_query' in profile.SUPPORTS

    def supports_bin_admin(self):
        """Tests if bin administration is supported.

        return: (boolean) - ``true`` if bin administration is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_bin_admin' in profile.SUPPORTS

    def supports_bin_hierarchy(self):
        """Tests if a bin hierarchy traversal is supported.

        return: (boolean) - ``true`` if a bin hierarchy traversal is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_bin_hierarchy' in profile.SUPPORTS

    def supports_bin_hierarchy_design(self):
        """Tests if a bin hierarchy design is supported.

        return: (boolean) - ``true`` if a bin hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return 'supports_bin_hierarchy_design' in profile.SUPPORTS

    def get_resource_record_types(self):
        """Gets all the resource record types supported.

        return: (osid.type.TypeList) - the list of supported resource
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        record_type_maps = get_registry('RESOURCE_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    resource_record_types = property(fget=get_resource_record_types)

    def get_resource_search_record_types(self):
        """Gets all the resource search record types supported.

        return: (osid.type.TypeList) - the list of supported resource
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        record_type_maps = get_registry('RESOURCE_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def get_resource_relationship_record_types(self):
        """Gets the supported ``ResourceRelationship`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ResourceRelationship`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        record_type_maps = get_registry('RESOURCE_RELATIONSHIP_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def get_resource_relationship_search_record_types(self):
        """Gets the supported ``ResourceRelationship`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ResourceRelationship`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        record_type_maps = get_registry('RESOURCE_RELATIONSHIP_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def get_bin_record_types(self):
        """Gets all the bin record types supported.

        return: (osid.type.TypeList) - the list of supported bin record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        record_type_maps = get_registry('BIN_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    bin_record_types = property(fget=get_bin_record_types)

    def get_bin_search_record_types(self):
        """Gets all the bin search record types supported.

        return: (osid.type.TypeList) - the list of supported bin search
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        record_type_maps = get_registry('BIN_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    bin_search_record_types = property(fget=get_bin_search_record_types)


class ResourceManager(osid_managers.OsidManager, ResourceProfile, resource_managers.ResourceManager):
    """The resource manager provides access to resource lookup and creation sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings

      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins

      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_resource_lookup_session(self, **kwargs):
        """Gets the ``OsidSession`` associated with the resource lookup service.

        return: (osid.resource.ResourceLookupSession) - ``a
                ResourceLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        if not self.supports_resource_lookup():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceLookupSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceLookupSession(runtime=self._runtime)

    resource_lookup_session = property(fget=get_resource_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_lookup_session_for_bin(self, bin_id, **kwargs):
        """Gets the ``OsidSession`` associated with the resource lookup service for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceLookupSession) - ``a
                ResourceLookupSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        if not self.supports_resource_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceLookupSession(
                bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime)
        return sessions.ResourceLookupSession(bin_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_resource_query_session(self, **kwargs):
        """Gets a resource query session.

        return: (osid.resource.ResourceQuerySession) - ``a
                ResourceQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        if not self.supports_resource_query():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceQuerySession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceQuerySession(runtime=self._runtime)

    resource_query_session = property(fget=get_resource_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_query_session_for_bin(self, bin_id, **kwargs):
        """Gets a resource query session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceQuerySession) - ``a
                ResourceQuerySession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        if not self.supports_resource_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceQuerySession(
                bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime)
        return sessions.ResourceQuerySession(bin_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_resource_search_session(self, **kwargs):
        """Gets a resource search session.

        return: (osid.resource.ResourceSearchSession) - ``a
                ResourceSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_resource_search():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceSearchSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceSearchSession(runtime=self._runtime)

    resource_search_session = property(fget=get_resource_search_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_search_session_for_bin(self, bin_id, **kwargs):
        """Gets a resource search session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceSearchSession) - ``a
                ResourceSearchSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        if not self.supports_resource_search():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceSearchSession(
                bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime)
        return sessions.ResourceSearchSession(bin_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_resource_admin_session(self, **kwargs):
        """Gets a resource administration session for creating, updating and deleting resources.

        return: (osid.resource.ResourceAdminSession) - ``a
                ResourceAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_resource_admin():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceAdminSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceAdminSession(runtime=self._runtime)

    resource_admin_session = property(fget=get_resource_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_admin_session_for_bin(self, bin_id, **kwargs):
        """Gets a resource administration session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceAdminSession) - ``a
                ResourceAdminSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        if not self.supports_resource_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceAdminSession(
                bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime)
        return sessions.ResourceAdminSession(bin_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_notification_session(self, resource_receiver, **kwargs):
        """Gets the notification session for notifications pertaining to resource changes.

        arg:    resource_receiver (osid.resource.ResourceReceiver): the
                notification callback
        return: (osid.resource.ResourceNotificationSession) - ``a
                ResourceNotificationSession``
        raise:  NullArgument - ``resource_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_notification()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_notification_session
        if not self.supports_resource_notification():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceNotificationSession(
                proxy=kwargs['proxy'],
                runtime=self._runtime,
                receiver=resource_receiver)
        return sessions.ResourceNotificationSession(runtime=self._runtime, receiver=resource_receiver)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id, **kwargs):
        """Gets the resource notification session for the given bin.

        arg:    resource_receiver (osid.resource.ResourceReceiver): the
                notification callback
        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceNotificationSession) - ``a
                ResourceNotificationSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``resource_receiver`` or ``bin_id`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_notification_session_for_catalog
        if not self.supports_resource_notification():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceNotificationSession(
                catalog_id=bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime,
                receiver=resource_receiver)
        return sessions.ResourceNotificationSession(
            catalog_id=bin_id,
            runtime=self._runtime,
            receiver=resource_receiver)

    @utilities.remove_null_proxy_kwarg
    def get_resource_bin_session(self, **kwargs):
        """Gets the session for retrieving resource to bin mappings.

        return: (osid.resource.ResourceBinSession) - a
                ``ResourceBinSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_bin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_resource_bin():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceBinSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceBinSession(runtime=self._runtime)

    resource_bin_session = property(fget=get_resource_bin_session)

    @utilities.remove_null_proxy_kwarg
    def get_resource_bin_assignment_session(self, **kwargs):
        """Gets the session for assigning resource to bin mappings.

        return: (osid.resource.ResourceBinAssignmentSession) - a
                ``ResourceBinAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_bin_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin_assignment()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_resource_bin_assignment():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceBinAssignmentSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceBinAssignmentSession(runtime=self._runtime)

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)

    @utilities.remove_null_proxy_kwarg
    def get_resource_agent_session(self, **kwargs):
        """Gets the session for retrieving resource agent mappings.

        return: (osid.resource.ResourceAgentSession) - a
                ``ResourceAgentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_resource_agent():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceAgentSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceAgentSession(runtime=self._runtime)

    resource_agent_session = property(fget=get_resource_agent_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_agent_session_for_bin(self, bin_id, **kwargs):
        """Gets a resource agent session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceAgentSession) - a
                ``ResourceAgentSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        if not self.supports_resource_agent():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceAgentSession(
                bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime)
        return sessions.ResourceAgentSession(bin_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_resource_agent_assignment_session(self, **kwargs):
        """Gets the session for assigning agents to resources.

        return: (osid.resource.ResourceAgentAssignmentSession) - a
                ``ResourceAgentAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_resource_agent_assignment():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.ResourceAgentAssignmentSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.ResourceAgentAssignmentSession(runtime=self._runtime)

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_resource_agent_assignment_session_for_bin(self, bin_id, **kwargs):
        """Gets a resource agent session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceAgentAssignmentSession) - a
                ``ResourceAgentAssignmentSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent_assignment()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        if not self.supports_resource_agent_assignment():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        if 'proxy' in kwargs:
            return sessions.ResourceAgentAssignmentSession(
                bin_id,
                proxy=kwargs['proxy'],
                runtime=self._runtime)
        return sessions.ResourceAgentAssignmentSession(bin_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_bin_lookup_session(self, **kwargs):
        """Gets the bin lookup session.

        return: (osid.resource.BinLookupSession) - a
                ``BinLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_lookup()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_bin_lookup():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.BinLookupSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.BinLookupSession(runtime=self._runtime)

    bin_lookup_session = property(fget=get_bin_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_bin_query_session(self, **kwargs):
        """Gets the bin query session.

        return: (osid.resource.BinQuerySession) - a ``BinQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_bin_query():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.BinQuerySession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.BinQuerySession(runtime=self._runtime)

    bin_query_session = property(fget=get_bin_query_session)

    @utilities.remove_null_proxy_kwarg
    def get_bin_admin_session(self, **kwargs):
        """Gets the bin administrative session for creating, updating and deleteing bins.

        return: (osid.resource.BinAdminSession) - a ``BinAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_admin()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_bin_admin():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.BinAdminSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.BinAdminSession(runtime=self._runtime)

    bin_admin_session = property(fget=get_bin_admin_session)

    @utilities.remove_null_proxy_kwarg
    def get_bin_hierarchy_session(self, **kwargs):
        """Gets the bin hierarchy traversal session.

        return: (osid.resource.BinHierarchySession) - ``a
                BinHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_bin_hierarchy():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.BinHierarchySession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.BinHierarchySession(runtime=self._runtime)

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
    def get_bin_hierarchy_design_session(self, **kwargs):
        """Gets the bin hierarchy design session.

        return: (osid.resource.BinHierarchyDesignSession) - a
                ``BinHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy_design()`` is ``true``.*

        """
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        if not self.supports_bin_hierarchy_design():
            raise errors.Unimplemented()
        if 'proxy' in kwargs:
            return sessions.BinHierarchyDesignSession(proxy=kwargs['proxy'], runtime=self._runtime)
        return sessions.BinHierarchyDesignSession(runtime=self._runtime)

    bin_hierarchy_design_session = property(fget=get_bin_hierarchy_design_session)

    def get_resource_batch_manager(self):
        """Gets the ``ResourceBatchManager``.

        return: (osid.resource.batch.ResourceBatchManager) - a
                ``ResourceBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    resource_batch_manager = property(fget=get_resource_batch_manager)

    def get_resource_demographic_manager(self):
        """Gets the ``ResourceDemographicManager``.

        return: (osid.resource.demographic.ResourceDemographicManager) -
                a ``ResourceDemographicManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_demographic()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*

        """
        raise errors.Unimplemented()

    resource_demographic_manager = property(fget=get_resource_demographic_manager)


class ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile, ResourceManager, resource_managers.ResourceProxyManager):
    """The resource manager provides access to resource lookup and creation session and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy``. The sessions included in
    this manager are:

      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings

      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins

      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies

    """
    # Built from: templates/osid_managers.GenericProxyManager.init_template
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)
