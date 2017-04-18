"""Implementations of hierarchy abstract base class managers."""
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


class HierarchyProfile:
    """The hierarchy profile describes the interoperability among hierarchy services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if federation is visible.

        Visible federation allows for selecting among multiple
        hierarchies.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.

        :return: ``true`` if hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.

        :return: ``true`` if hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_sequencing(self):
        """Tests if hierarchy sequencing is supported.

        :return: ``true`` if hierarchy sequencing is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_structure_notification(self):
        """Tests if hierarchy structure notification is supported.

        :return: ``true`` if hierarchy structure notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.

        :return: ``true`` if hierarchy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_query(self):
        """Tests if a hierarchy query is supported.

        :return: ``true`` if hierarchy query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_search(self):
        """Tests if a hierarchy search is supported.

        :return: ``true`` if hierarchy search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.

        :return: ``true`` if hierarchy administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_hierarchy_notification(self):
        """Tests if hierarchy notification is supported.

        Messages may be sent when hierarchies are created, modified, or
        deleted.

        :return: ``true`` if hierarchy notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.

        :return: a list containing the supported ``Hierarchy`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    @abc.abstractmethod
    def supports_hierarchy_record_type(self, hierarchy_record_type):
        """Tests if the given ``Hierarchy`` record type is supported.

        :param hierarchy_record_type: a ``Type`` indicating a ``Hierarchy`` record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.

        :return: a list containing the supported ``Hierarchy`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)

    @abc.abstractmethod
    def supports_hierarchy_search_record_type(self, hierarchy_search_record_type):
        """Tests if the given ``Hierarchy`` search record type is supported.

        :param hierarchy_search_record_type: a ``Type`` indicating a ``Hierarchy`` search record type
        :type hierarchy_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class HierarchyManager:
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.

    The sessions included in this manager are:

      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_hierarchy_traversal_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyTraversalSession

    hierarchy_traversal_session = property(fget=get_hierarchy_traversal_session)

    @abc.abstractmethod
    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :return: the new ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchyid`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` or ``supports_visible_fedaration()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchyTraversalSession

    @abc.abstractmethod
    def get_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyDesignSession

    hierarchy_design_session = property(fget=get_hierarchy_design_session)

    @abc.abstractmethod
    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchyDesignSession

    @abc.abstractmethod
    def get_hierarchy_sequencing_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy sequencing service.

        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_sequencing()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchySequencingSession

    hierarchy_sequencing_session = property(fget=get_hierarchy_sequencing_session)

    @abc.abstractmethod
    def get_hierarchy_sequencing_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the sequencing design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchySequencingSession

    @abc.abstractmethod
    def get_hierarchy_structure_notification_session(self, hierarchy_structure_receiver):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_structure_notification()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyStructureNotificationSession

    @abc.abstractmethod
    def get_hierarchy_structure_notification_session_for_hierarchy(self, hierarchy_structure_receiver, hierarchy_id):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure for the given hierarchy.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver`` or ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_structure_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchyStructureNotificationSession

    @abc.abstractmethod
    def get_hierarchy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        :return: a ``HierarchyLookupSession``
        :rtype: ``osid.hierarchy.HierarchyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_lookup()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyLookupSession

    hierarchy_lookup_session = property(fget=get_hierarchy_lookup_session)

    @abc.abstractmethod
    def get_hierarchy_query_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy query service.

        :return: a ``HierarchyQuerySession``
        :rtype: ``osid.hierarchy.HierarchyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_query()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyQuerySession

    hierarchy_query_session = property(fget=get_hierarchy_query_session)

    @abc.abstractmethod
    def get_hierarchy_search_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy search service.

        :return: a ``HierarchySearchSession``
        :rtype: ``osid.hierarchy.HierarchySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_search()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchySearchSession

    hierarchy_search_session = property(fget=get_hierarchy_search_session)

    @abc.abstractmethod
    def get_hierarchy_admin_session(self):
        """Gets the hierarchy administrative session.

        :return: a ``HierarchyAdminSession``
        :rtype: ``osid.hierarchy.HierarchyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_admin()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyAdminSession

    hierarchy_admin_session = property(fget=get_hierarchy_admin_session)

    @abc.abstractmethod
    def get_hierarchy_notification_session(self, hierarchy_receiver):
        """Gets a hierarchy notification session.

        :param hierarchy_receiver: notification callback
        :type hierarchy_receiver: ``osid.hierarchy.HierarchyReceiver``
        :return: a ``HierarchyNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_notification()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyNotificationSession


class HierarchyProxyManager:
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.

    Methods in this manager accept a ``Proxy`` to pass information from
    server environments. The sessions included in this manager are:

      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_hierarchy_traversal_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyTraversalSession

    @abc.abstractmethod
    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NotFound`` -- ``hierarchyid`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchyTraversalSession

    @abc.abstractmethod
    def get_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyDesignSession

    @abc.abstractmethod
    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchyDesignSession

    @abc.abstractmethod
    def get_hierarchy_sequencing_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy sequencing service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_sequencing()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchySequencingSession

    @abc.abstractmethod
    def get_hierarchy_sequencing_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the sequencing design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchySequencingSession

    @abc.abstractmethod
    def get_hierarchy_structure_notification_session(self, hierarchy_structure_receiver, proxy):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_structure_notification()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyStructureNotificationSession

    @abc.abstractmethod
    def get_hierarchy_structure_notification_session_for_hierarchy(self, hierarchy_structure_receiver, hierarchy_id, proxy):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure for the given hierarchy.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver, hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_structure_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.hierarchy.HierarchyStructureNotificationSession

    @abc.abstractmethod
    def get_hierarchy_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyLookupSession``
        :rtype: ``osid.hierarchy.HierarchyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_lookup()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyLookupSession

    @abc.abstractmethod
    def get_hierarchy_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyQuerySession``
        :rtype: ``osid.hierarchy.HierarchyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_query()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyQuerySession

    @abc.abstractmethod
    def get_hierarchy_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchySearchSession``
        :rtype: ``osid.hierarchy.HierarchySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_search()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchySearchSession

    @abc.abstractmethod
    def get_hierarchy_admin_session(self, proxy):
        """Gets the hierarchy administrative session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyAdminSession``
        :rtype: ``osid.hierarchy.HierarchyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_admin()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyAdminSession

    @abc.abstractmethod
    def get_hierarchy_notification_session(self, hierarchy_receiver, proxy):
        """Gets the hierarchy notification session.

        :param hierarchy_receiver: notification callback
        :type hierarchy_receiver: ``osid.hierarchy.HierarchyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_notification()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchyNotificationSession
