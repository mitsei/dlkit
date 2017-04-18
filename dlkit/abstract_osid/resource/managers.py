"""Implementations of resource abstract base class managers."""
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


class ResourceProfile:
    """The resource profile describes interoperability among resource services."""
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
    def supports_resource_lookup(self):
        """Tests if resource lookup is supported.

        :return: ``true`` if resource lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_query(self):
        """Tests if resource query is supported.

        :return: ``true`` if resource query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_search(self):
        """Tests if resource search is supported.

        :return: ``true`` if resource search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_admin(self):
        """Tests if resource administration is supported.

        :return: ``true`` if resource administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_notification(self):
        """Tests if resource notification is supported.

        Messages may be sent when resources are created, modified, or
        deleted.

        :return: ``true`` if resource notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_bin(self):
        """Tests if retrieving mappings of resource and bins is supported.

        :return: ``true`` if resource bin mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_bin_assignment(self):
        """Tests if managing mappings of resource and bins is supported.

        :return: ``true`` if resource bin assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_smart_bin(self):
        """Tests if resource smart bins are available.

        :return: ``true`` if resource smart bins are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_membership(self):
        """Tests if membership queries are supported.

        :return: ``true`` if membership queries are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_group(self):
        """Tests if group resources are supported.

        :return: ``true`` if group resources are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_group_assignment(self):
        """Tests if group resource assignment is supported.

        :return: ``true`` if group resource assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_group_notification(self):
        """Tests if group resource notification is supported.

        :return: ``true`` if group resource notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_group_hierarchy(self):
        """Tests if a group resource hierarchy service is supported.

        :return: ``true`` if group resource hierarchy is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_agent(self):
        """Tests if retrieving mappings of resource and agents is supported.

        :return: ``true`` if resource agent mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_agent_assignment(self):
        """Tests if managing mappings of resources and agents is supported.

        :return: ``true`` if resource agent assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_lookup(self):
        """Tests if looking up resource relationships is supported.

        :return: ``true`` if resource relationships lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_query(self):
        """Tests if querying resource relationships is supported.

        :return: ``true`` if resource relationships query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_search(self):
        """Tests if searching resource relationships is supported.

        :return: ``true`` if resource relationships search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_admin(self):
        """Tests if a resource relationshipsadministrative service is supported.

        :return: ``true`` if resource relationships administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_notification(self):
        """Tests if a resource relationshipsnotification service is supported.

        :return: ``true`` if resource relationships notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_bin(self):
        """Tests if retrieving mappings of resource relationships and bins is supported.

        :return: ``true`` if resource relationship bin mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_bin_assignment(self):
        """Tests if managing mappings of resource relationships and bins is supported.

        :return: ``true`` if resource relationship bin assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_relationship_smart_bin(self):
        """Tests if resource relationship smart bins are available.

        :return: ``true`` if resource relationship smart bins are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_lookup(self):
        """Tests if bin lookup is supported.

        :return: ``true`` if bin lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_query(self):
        """Tests if bin query is supported.

        :return: ``true`` if bin query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_search(self):
        """Tests if bin search is supported.

        :return: ``true`` if bin search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_admin(self):
        """Tests if bin administration is supported.

        :return: ``true`` if bin administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_notification(self):
        """Tests if bin notification is supported.

        Messages may be sent when ``Bin`` objects are created, deleted
        or updated. Notifications for resources within bins are sent via
        the resource notification session.

        :return: ``true`` if bin notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_hierarchy(self):
        """Tests if a bin hierarchy traversal is supported.

        :return: ``true`` if a bin hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bin_hierarchy_design(self):
        """Tests if a bin hierarchy design is supported.

        :return: ``true`` if a bin hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_batch(self):
        """Tests if a resource batch service is available.

        :return: ``true`` if a resource batch service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_demographic(self):
        """Tests if a resource demographic service is available.

        :return: ``true`` if a resource demographic service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_record_types(self):
        """Gets all the resource record types supported.

        :return: the list of supported resource record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    resource_record_types = property(fget=get_resource_record_types)

    @abc.abstractmethod
    def supports_resource_record_type(self, resource_record_type):
        """Tests if a given resource record type is supported.

        :param resource_record_type: the resource type
        :type resource_record_type: ``osid.type.Type``
        :return: ``true`` if the resource record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_search_record_types(self):
        """Gets all the resource search record types supported.

        :return: the list of supported resource search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    resource_search_record_types = property(fget=get_resource_search_record_types)

    @abc.abstractmethod
    def supports_resource_search_record_type(self, resource_search_record_type):
        """Tests if a given resource search type is supported.

        :param resource_search_record_type: the resource search type
        :type resource_search_record_type: ``osid.type.Type``
        :return: ``true`` if the resource search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_relationship_record_types(self):
        """Gets the supported ``ResourceRelationship`` record types.

        :return: a list containing the supported ``ResourceRelationship`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    @abc.abstractmethod
    def supports_resource_relationship_record_type(self, resource_relationship_record_type):
        """Tests if the given ``ResourceRelationship`` record type is supported.

        :param resource_relationship_record_type: a ``Type`` indicating a ``ResourceRelationship`` record type
        :type resource_relationship_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_relationship_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_relationship_search_record_types(self):
        """Gets the supported ``ResourceRelationship`` search record types.

        :return: a list containing the supported ``ResourceRelationship`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    @abc.abstractmethod
    def supports_resource_relationship_search_record_type(self, resource_relationship_search_record_type):
        """Tests if the given ``ResourceRelationship`` search record type is supported.

        :param resource_relationship_search_record_type: a ``Type`` indicating a ``ResourceRelationship`` search record type
        :type resource_relationship_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_relationship_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bin_record_types(self):
        """Gets all the bin record types supported.

        :return: the list of supported bin record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    bin_record_types = property(fget=get_bin_record_types)

    @abc.abstractmethod
    def supports_bin_record_type(self, bin_record_type):
        """Tests if a given bin record type is supported.

        :param bin_record_type: the bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: ``true`` if the bin record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bin_search_record_types(self):
        """Gets all the bin search record types supported.

        :return: the list of supported bin search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    bin_search_record_types = property(fget=get_bin_search_record_types)

    @abc.abstractmethod
    def supports_bin_search_record_type(self, bin_search_record_type):
        """Tests if a given bin search record type is supported.

        :param bin_search_record_type: the bin search record type
        :type bin_search_record_type: ``osid.type.Type``
        :return: ``true`` if the bin search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class ResourceManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resource_lookup_session(self):
        """Gets the ``OsidSession`` associated with the resource lookup service.

        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` is ``true``.*

        """
        return  # osid.resource.ResourceLookupSession

    resource_lookup_session = property(fget=get_resource_lookup_session)

    @abc.abstractmethod
    def get_resource_lookup_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource lookup service for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceLookupSession

    @abc.abstractmethod
    def get_resource_query_session(self):
        """Gets a resource query session.

        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuerySession

    resource_query_session = property(fget=get_resource_query_session)

    @abc.abstractmethod
    def get_resource_query_session_for_bin(self, bin_id):
        """Gets a resource query session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceQuerySession

    @abc.abstractmethod
    def get_resource_search_session(self):
        """Gets a resource search session.

        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchSession

    resource_search_session = property(fget=get_resource_search_session)

    @abc.abstractmethod
    def get_resource_search_session_for_bin(self, bin_id):
        """Gets a resource search session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceSearchSession

    @abc.abstractmethod
    def get_resource_admin_session(self):
        """Gets a resource administration session for creating, updating and deleting resources.

        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` is ``true``.*

        """
        return  # osid.resource.ResourceAdminSession

    resource_admin_session = property(fget=get_resource_admin_session)

    @abc.abstractmethod
    def get_resource_admin_session_for_bin(self, bin_id):
        """Gets a resource administration session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceAdminSession

    @abc.abstractmethod
    def get_resource_notification_session(self, resource_receiver):
        """Gets the notification session for notifications pertaining to resource changes.

        :param resource_receiver: the notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NullArgument`` -- ``resource_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_notification()`` is ``true``.*

        """
        return  # osid.resource.ResourceNotificationSession

    @abc.abstractmethod
    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id):
        """Gets the resource notification session for the given bin.

        :param resource_receiver: the notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_receiver`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceNotificationSession

    @abc.abstractmethod
    def get_resource_bin_session(self):
        """Gets the session for retrieving resource to bin mappings.

        :return: a ``ResourceBinSession``
        :rtype: ``osid.resource.ResourceBinSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceBinSession

    resource_bin_session = property(fget=get_resource_bin_session)

    @abc.abstractmethod
    def get_resource_bin_assignment_session(self):
        """Gets the session for assigning resource to bin mappings.

        :return: a ``ResourceBinAssignmentSession``
        :rtype: ``osid.resource.ResourceBinAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin_assignment()`` is ``true``.*

        """
        return  # osid.resource.ResourceBinAssignmentSession

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)

    @abc.abstractmethod
    def get_resource_smart_bin_session(self, bin_id):
        """Gets the session for managing dynamic resource bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceSmartBinSession``
        :rtype: ``osid.resource.ResourceSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_smart_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_smart_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceSmartBinSession

    @abc.abstractmethod
    def get_membership_session(self):
        """Gets the session for querying memberships.

        :return: a ``MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``support_membership()`` is ``true``.*

        """
        return  # osid.resource.MembershipSession

    membership_session = property(fget=get_membership_session)

    @abc.abstractmethod
    def get_membership_session_for_bin(self, bin_id):
        """Gets a resource membership session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_membership()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.resource.MembershipSession

    @abc.abstractmethod
    def get_group_session(self):
        """Gets the session for retrieving gropup memberships.

        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group()`` is ``true``.*

        """
        return  # osid.resource.GroupSession

    group_session = property(fget=get_group_session)

    @abc.abstractmethod
    def get_group_session_for_bin(self, bin_id):
        """Gets a group session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group()`` and ``supports_visible_federation()`` are
        ``true``.*

        """
        return  # osid.resource.GroupSession

    @abc.abstractmethod
    def get_group_assignment_session(self):
        """Gets the session for assigning resources to groups.

        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_assignment()`` is ``true``.*

        """
        return  # osid.resource.GroupAssignmentSession

    group_assignment_session = property(fget=get_group_assignment_session)

    @abc.abstractmethod
    def get_group_assignment_session_for_bin(self, bin_id):
        """Gets a group assignment session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.GroupAssignmentSession

    @abc.abstractmethod
    def get_group_notification_session(self, group_rceeiver):
        """Gets the notification session for notifications pertaining to resource changes.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NullArgument`` -- ``group_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_notification()`` is ``true``.*

        """
        return  # osid.resource.GroupNotificationSession

    @abc.abstractmethod
    def get_group_notification_session_for_bin(self, group_rceeiver, bin_id):
        """Gets the group notification session for the given bin.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``group_receiver`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.GroupNotificationSession

    @abc.abstractmethod
    def get_group_hierarchy_session(self):
        """Gets a session for retrieving gropup hierarchies.

        :return: ``a GroupHierarchySession``
        :rtype: ``osid.resource.GroupHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_hierarchy()`` is ``true``.*

        """
        return  # osid.resource.GroupHierarchySession

    group_hierarchy_session = property(fget=get_group_hierarchy_session)

    @abc.abstractmethod
    def get_group_hierarchy_session_for_bin(self, bin_id):
        """Gets a group hierarchy session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``GroupHierarchySession``
        :rtype: ``osid.resource.GroupHierarchySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.GroupHierarchySession

    @abc.abstractmethod
    def get_resource_agent_session(self):
        """Gets the session for retrieving resource agent mappings.

        :return: a ``ResourceAgentSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` is ``true``.*

        """
        return  # osid.resource.ResourceAgentSession

    resource_agent_session = property(fget=get_resource_agent_session)

    @abc.abstractmethod
    def get_resource_agent_session_for_bin(self, bin_id):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceAgentSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceAgentSession

    @abc.abstractmethod
    def get_resource_agent_assignment_session(self):
        """Gets the session for assigning agents to resources.

        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` is ``true``.*

        """
        return  # osid.resource.ResourceAgentAssignmentSession

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)

    @abc.abstractmethod
    def get_resource_agent_assignment_session_for_bin(self, bin_id):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceAgentAssignmentSession

    @abc.abstractmethod
    def get_resource_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service.

        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_lookup()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipLookupSession

    resource_relationship_lookup_session = property(fget=get_resource_relationship_lookup_session)

    @abc.abstractmethod
    def get_resource_relationship_lookup_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipLookupSession

    @abc.abstractmethod
    def get_resource_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship query service.

        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipQuerySession

    resource_relationship_query_session = property(fget=get_resource_relationship_query_session)

    @abc.abstractmethod
    def get_resource_relationship_query_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship query service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipQuerySession

    @abc.abstractmethod
    def get_resource_relationship_search_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship search service.

        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_search()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipSearchSession

    resource_relationship_search_session = property(fget=get_resource_relationship_search_session)

    @abc.abstractmethod
    def get_resource_relationship_search_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship search service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipSearchSession

    @abc.abstractmethod
    def get_resource_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship administration service.

        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_admin()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipAdminSession

    resource_relationship_admin_session = property(fget=get_resource_relationship_admin_session)

    @abc.abstractmethod
    def get_resource_relationship_admin_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship administration service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipAdminSession

    @abc.abstractmethod
    def get_resource_relationship_notification_session(self, resource_relationship_receiver):
        """Gets the ``OsidSession`` associated with the resource relationship notification service.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_notification()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipNotificationSession

    @abc.abstractmethod
    def get_resource_relationship_notification_session_for_bin(self, resource_relationship_receiver, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship notification service for the given bin.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationshipt_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipNotificationSession

    @abc.abstractmethod
    def get_resource_relationship_bin_session(self):
        """Gets the session for retrieving resource relationship to bin mappings.

        :return: a ``ResourceRelationshipBinSession``
        :rtype: ``osid.resource.ResourceRelationshipBinSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipBinSession

    resource_relationship_bin_session = property(fget=get_resource_relationship_bin_session)

    @abc.abstractmethod
    def get_resource_relationship_bin_assignment_session(self):
        """Gets the session for assigning resource relationships to bin mappings.

        :return: a ``ResourceRelationshipBinAssignmentSession``
        :rtype: ``osid.resource.ResourceRelationshipBinAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_bin_assignment()`` is
        ``true``.*

        """
        return  # osid.resource.ResourceRelationshipBinAssignmentSession

    resource_relationship_bin_assignment_session = property(fget=get_resource_relationship_bin_assignment_session)

    @abc.abstractmethod
    def get_resource_relationship_smart_bin_session(self, bin_id):
        """Gets the session for managing dynamic resource relationship bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipSmartBinSession``
        :rtype: ``osid.resource.ResourceRelationshipSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_smart_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_smart_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipSmartBinSession

    @abc.abstractmethod
    def get_bin_lookup_session(self):
        """Gets the bin lookup session.

        :return: a ``BinLookupSession``
        :rtype: ``osid.resource.BinLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_lookup()`` is ``true``.*

        """
        return  # osid.resource.BinLookupSession

    bin_lookup_session = property(fget=get_bin_lookup_session)

    @abc.abstractmethod
    def get_bin_query_session(self):
        """Gets the bin query session.

        :return: a ``BinQuerySession``
        :rtype: ``osid.resource.BinQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        return  # osid.resource.BinQuerySession

    bin_query_session = property(fget=get_bin_query_session)

    @abc.abstractmethod
    def get_bin_search_session(self):
        """Gets the bin search session.

        :return: a ``BinSearchSession``
        :rtype: ``osid.resource.BinSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_search()`` is ``true``.*

        """
        return  # osid.resource.BinSearchSession

    bin_search_session = property(fget=get_bin_search_session)

    @abc.abstractmethod
    def get_bin_admin_session(self):
        """Gets the bin administrative session for creating, updating and deleteing bins.

        :return: a ``BinAdminSession``
        :rtype: ``osid.resource.BinAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_admin()`` is ``true``.*

        """
        return  # osid.resource.BinAdminSession

    bin_admin_session = property(fget=get_bin_admin_session)

    @abc.abstractmethod
    def get_bin_notification_session(self, bin_receiver):
        """Gets the notification session for subscribing to changes to a bin.

        :param bin_receiver: the notification callback
        :type bin_receiver: ``osid.resource.BinReceiver``
        :return: a ``BinNotificationSession``
        :rtype: ``osid.resource.BinNotificationSession``
        :raise: ``NullArgument`` -- ``bin_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_notification()`` is ``true``.*

        """
        return  # osid.resource.BinNotificationSession

    @abc.abstractmethod
    def get_bin_hierarchy_session(self):
        """Gets the bin hierarchy traversal session.

        :return: ``a BinHierarchySession``
        :rtype: ``osid.resource.BinHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy()`` is ``true``.*

        """
        return  # osid.resource.BinHierarchySession

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)

    @abc.abstractmethod
    def get_bin_hierarchy_design_session(self):
        """Gets the bin hierarchy design session.

        :return: a ``BinHierarchyDesignSession``
        :rtype: ``osid.resource.BinHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy_design()`` is ``true``.*

        """
        return  # osid.resource.BinHierarchyDesignSession

    bin_hierarchy_design_session = property(fget=get_bin_hierarchy_design_session)

    @abc.abstractmethod
    def get_resource_batch_manager(self):
        """Gets the ``ResourceBatchManager``.

        :return: a ``ResourceBatchManager``
        :rtype: ``osid.resource.batch.ResourceBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*

        """
        return  # osid.resource.batch.ResourceBatchManager

    resource_batch_manager = property(fget=get_resource_batch_manager)

    @abc.abstractmethod
    def get_resource_demographic_manager(self):
        """Gets the ``ResourceDemographicManager``.

        :return: a ``ResourceDemographicManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*

        """
        return  # osid.resource.demographic.ResourceDemographicManager

    resource_demographic_manager = property(fget=get_resource_demographic_manager)


class ResourceProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resource_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` is ``true``.*

        """
        return  # osid.resource.ResourceLookupSession

    @abc.abstractmethod
    def get_resource_lookup_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource lookup service for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: ``a proxy``
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceLookupSession

    @abc.abstractmethod
    def get_resource_query_session(self, proxy):
        """Gets a resource query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuerySession

    @abc.abstractmethod
    def get_resource_query_session_for_bin(self, bin_id, proxy):
        """Gets a resource query session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceQuerySession

    @abc.abstractmethod
    def get_resource_search_session(self, proxy):
        """Gets a resource search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchSession

    @abc.abstractmethod
    def get_resource_search_session_for_bin(self, bin_id, proxy):
        """Gets a resource search session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceSearchSession

    @abc.abstractmethod
    def get_resource_admin_session(self, proxy):
        """Gets a resource administration session for creating, updating and deleting resources.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` is ``true``.*

        """
        return  # osid.resource.ResourceAdminSession

    @abc.abstractmethod
    def get_resource_admin_session_for_bin(self, bin_id, proxy):
        """Gets a resource administration session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceAdminSession

    @abc.abstractmethod
    def get_resource_notification_session(self, resource_receiver, proxy):
        """Gets the resource notification session for the given bin.

        :param resource_receiver: notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NullArgument`` -- ``resource_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_notification()`` is ``true``.*

        """
        return  # osid.resource.ResourceNotificationSession

    @abc.abstractmethod
    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id, proxy):
        """Gets the resource notification session for the given bin.

        :param resource_receiver: notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_receiver, bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceNotificationSession

    @abc.abstractmethod
    def get_resource_bin_session(self, proxy):
        """Gets the session for retrieving resource to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceBinSession``
        :rtype: ``osid.resource.ResourceBinSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceBinSession

    @abc.abstractmethod
    def get_resource_bin_assignment_session(self, proxy):
        """Gets the session for assigning resource to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceBinAssignmentSession``
        :rtype: ``osid.resource.ResourceBinAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin_assignment()`` is ``true``.*

        """
        return  # osid.resource.ResourceBinAssignmentSession

    @abc.abstractmethod
    def get_resource_smart_bin_session(self, bin_id, proxy):
        """Gets the session for managing dynamic resource bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceSmartBinSession``
        :rtype: ``osid.resource.ResourceSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_smart_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_smart_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceSmartBinSession

    @abc.abstractmethod
    def get_membership_session(self, proxy):
        """Gets the session for querying memberships.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``support_membership()`` is ``true``.*

        """
        return  # osid.resource.MembershipSession

    @abc.abstractmethod
    def get_membership_session_for_bin(self, bin_id, proxy):
        """Gets a resource membership session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_membership()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.resource.MembershipSession

    @abc.abstractmethod
    def get_group_session(self, proxy):
        """Gets the session for retrieving gropup memberships.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_groups()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_groups()`` is ``true``.*

        """
        return  # osid.resource.GroupSession

    @abc.abstractmethod
    def get_group_session_for_bin(self, bin_id, proxy):
        """Gets a group session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group()`` and ``supports_visible_federation()`` are
        ``true``.*

        """
        return  # osid.resource.GroupSession

    @abc.abstractmethod
    def get_group_assignment_session(self, proxy):
        """Gets the session for assigning resources to groups.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_assignment()`` is ``true``.*

        """
        return  # osid.resource.GroupAssignmentSession

    @abc.abstractmethod
    def get_group_assignment_session_for_bin(self, bin_id, proxy):
        """Gets a group assignment session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.GroupAssignmentSession

    @abc.abstractmethod
    def get_group_notification_session(self, group_rceeiver, proxy):
        """Gets the notification session for notifications pertaining to resource changes.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NullArgument`` -- ``group_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_notification()`` is ``true``.*

        """
        return  # osid.resource.GroupNotificationSession

    @abc.abstractmethod
    def get_group_notification_session_for_bin(self, group_rceeiver, bin_id, proxy):
        """Gets the group notification session for the given bin.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``group_receiver, bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.GroupNotificationSession

    @abc.abstractmethod
    def get_group_hierarchy_session(self, proxy):
        """Gets the group hierarchy traversal session for the given resource group.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GroupHierarchySession``
        :rtype: ``osid.resource.BinHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_hierarchy()`` is ``true``.*

        """
        return  # osid.resource.BinHierarchySession

    @abc.abstractmethod
    def get_group_hierarchy_session_for_bin(self, bin_id, proxy):
        """Gets a group hierarchy session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupHierarchySession``
        :rtype: ``osid.resource.GroupHierarchySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_group_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.GroupHierarchySession

    @abc.abstractmethod
    def get_resource_agent_session(self, proxy):
        """Gets the session for retrieving resource agent mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agents()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agents()`` is ``true``.*

        """
        return  # osid.resource.ResourceAgentSession

    @abc.abstractmethod
    def get_resource_agent_session_for_bin(self, bin_id, proxy):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceAgentSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceAgentSession

    @abc.abstractmethod
    def get_resource_agent_assignment_session(self, proxy):
        """Gets the session for assigning agents to resources.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` is ``true``.*

        """
        return  # osid.resource.ResourceAgentAssignmentSession

    @abc.abstractmethod
    def get_resource_agent_assignment_session_for_bin(self, bin_id, proxy):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.resource.ResourceAgentAssignmentSession

    @abc.abstractmethod
    def get_resource_relationship_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_lookup()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipLookupSession

    @abc.abstractmethod
    def get_resource_relationship_lookup_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipLookupSession

    @abc.abstractmethod
    def get_resource_relationship_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipQuerySession

    @abc.abstractmethod
    def get_resource_relationship_query_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship query service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipQuerySession

    @abc.abstractmethod
    def get_resource_relationship_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_search()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipSearchSession

    @abc.abstractmethod
    def get_resource_relationship_search_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship search service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipSearchSession

    @abc.abstractmethod
    def get_resource_relationship_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_admin()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipAdminSession

    @abc.abstractmethod
    def get_resource_relationship_admin_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship administration service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipAdminSession

    @abc.abstractmethod
    def get_resource_relationship_notification_session(self, resource_relationship_receiver, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship notification service.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_notification()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipNotificationSession

    @abc.abstractmethod
    def get_resource_relationship_notification_session_for_bin(self, resource_relationship_receiver, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship notification service for the given bin.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver, bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationshipt_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.resource.ResourceRelationshipNotificationSession

    @abc.abstractmethod
    def get_resource_relationship_bin_session(self, proxy):
        """Gets the session for retrieving resource relationship to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipBinSession``
        :rtype: ``osid.resource.ResourceRelationshipBinSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipBinSession

    @abc.abstractmethod
    def get_resource_relationship_bin_assignment_session(self, proxy):
        """Gets the session for assigning resource relationship to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipBinAssignmentSession``
        :rtype: ``osid.resource.ResourceRelationshipBinAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_bin_assignment()`` is
        ``true``.*

        """
        return  # osid.resource.ResourceRelationshipBinAssignmentSession

    @abc.abstractmethod
    def get_resource_relationship_smart_bin_session(self, bin_id, proxy):
        """Gets the session for managing dynamic resource relationship bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipSmartBinSession``
        :rtype: ``osid.resource.ResourceRelationshipSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_smart_bin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_smart_bin()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipSmartBinSession

    @abc.abstractmethod
    def get_bin_lookup_session(self, proxy):
        """Gets the bin lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinLookupSession``
        :rtype: ``osid.resource.BinLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_lookup()`` is ``true``.*

        """
        return  # osid.resource.BinLookupSession

    @abc.abstractmethod
    def get_bin_query_session(self, proxy):
        """Gets the bin query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinQuerySession``
        :rtype: ``osid.resource.BinQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        return  # osid.resource.BinQuerySession

    @abc.abstractmethod
    def get_bin_search_session(self, proxy):
        """Gets the bin search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinSearchSession``
        :rtype: ``osid.resource.BinSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_search()`` is ``true``.*

        """
        return  # osid.resource.BinSearchSession

    @abc.abstractmethod
    def get_bin_admin_session(self, proxy):
        """Gets the bin administrative session for creating, updating and deleteing bins.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinAdminSession``
        :rtype: ``osid.resource.BinAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_admin()`` is ``true``.*

        """
        return  # osid.resource.BinAdminSession

    @abc.abstractmethod
    def get_bin_notification_session(self, bin_receiver, proxy):
        """Gets the notification session for subscribing to changes to a bin.

        :param bin_receiver: notification callback
        :type bin_receiver: ``osid.resource.BinReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinNotificationSession``
        :rtype: ``osid.resource.BinNotificationSession``
        :raise: ``NullArgument`` -- ``bin_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_notification()`` is ``true``.*

        """
        return  # osid.resource.BinNotificationSession

    @abc.abstractmethod
    def get_bin_hierarchy_session(self, proxy):
        """Gets the bin hierarchy traversal session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BinHierarchySession``
        :rtype: ``osid.resource.BinHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy()`` is ``true``.*

        """
        return  # osid.resource.BinHierarchySession

    @abc.abstractmethod
    def get_bin_hierarchy_design_session(self, proxy):
        """Gets the bin hierarchy design session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinHierarchyDesignSession``
        :rtype: ``osid.resource.BinHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy_design()`` is ``true``.*

        """
        return  # osid.resource.BinHierarchyDesignSession

    @abc.abstractmethod
    def get_resource_batch_proxy_manager(self):
        """Gets the ``ResourceBatchProxyManager``.

        :return: a ``ResourceBatchProxyManager``
        :rtype: ``osid.resource.batch.ResourceBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*

        """
        return  # osid.resource.batch.ResourceBatchProxyManager

    resource_batch_proxy_manager = property(fget=get_resource_batch_proxy_manager)

    @abc.abstractmethod
    def get_resource_demographic_proxy_manager(self):
        """Gets the ``ResourceDemographicProxyManager``.

        :return: a ``ResourceDemographicProxyManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*

        """
        return  # osid.resource.demographic.ResourceDemographicProxyManager

    resource_demographic_proxy_manager = property(fget=get_resource_demographic_proxy_manager)
