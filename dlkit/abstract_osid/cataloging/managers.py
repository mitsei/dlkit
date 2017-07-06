"""Implementations of cataloging abstract base class managers."""
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


class CatalogingProfile:
    """The cataloging profile describes the interoperability among cataloging services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if any billing federation is exposed.

        Federation is exposed when a specific catalog may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of catalogs appears as a
        single catalog.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog(self):
        """Tests for the availability of a cataloging service retrieving ``Id`` to ``Catalog`` mappings.

        :return: ``true`` if cataloging is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_assignment(self):
        """Tests for the availability of a cataloging service for mapping ``Ids`` to ``Catalogs``.

        :return: ``true`` if catalog assignment is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_entry_notification(self):
        """Tests for the availability of a cataloging notification service for mapping ``Ids`` to ``Catalogs``.

        :return: ``true`` if catalog entry notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_lookup(self):
        """Tests for the availability of a catalog lookup service.

        :return: ``true`` if catalog lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_query(self):
        """Tests for the availability of a catalog query service that defines more comprehensive queries.

        :return: ``true`` if catalog query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_search(self):
        """Tests for the availability of a catalog search service that defines more comprehensive queries.

        :return: ``true`` if catalog search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_admin(self):
        """Tests for the availability of a catalog administration service for the addition and deletion of catalogs.

        :return: ``true`` if catalog administration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_notification(self):
        """Tests for the availability of a catalog notification service.

        :return: ``true`` if catalog notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_hierarchy(self):
        """Tests for the availability of a catalog hierarchy traversal service.

        :return: ``true`` if catalog hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_catalog_hierarchy_design(self):
        """Tests for the availability of a catalog hierarchy design service.

        :return: ``true`` if catalog hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_cataloging_rules(self):
        """Tests if the cataloging rules sub services is supported.

        :return: ``true`` if cataloging rules is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_catalog_record_types(self):
        """Gets the supported ``Catalog`` record types.

        :return: a list containing the supported ``Catalog`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    catalog_record_types = property(fget=get_catalog_record_types)

    @abc.abstractmethod
    def supports_catalog_record_type(self, catalog_record_type):
        """Tests if the given ``Catalog`` record type is supported.

        :param catalog_record_type: a ``Type`` indicating a ``Catalog`` record type
        :type catalog_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_catalog_search_record_types(self):
        """Gets the supported catalog search reciord types.

        :return: a list containing the supported search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    catalog_search_record_types = property(fget=get_catalog_search_record_types)

    @abc.abstractmethod
    def supports_catalog_search_record_type(self, catalog_search_record_type):
        """Tests if the given catalog search record type is supported.

        :param catalog_search_record_type: a ``Type`` indicating a catalog search record type
        :type catalog_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``catalog_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class CatalogingManager:
    """The cataloging manager provides access to cataloging sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``CatalogSession:`` a session to lookup mappings to catalogs
      * ``CatalogAssignmentSession:`` a session to manage Id to Catalog
        mappings
      * ``CatalogEntryNotificationSession:`` a session to receive
        notification of changed mappings
      * ``CatalogLookupSession:`` a session to retrieve catalogs
      * ``CatalogQuerySession:`` a session to query catalogs
      * ``CatalogSearchSession:`` a session to search for catalogs
      * ``CatalogAdminSession:`` a session to create, update and delete
        catalogs
      * ``CatalogNotificationSession:`` a session to receive
        notifications for changes in catalogs
      * ``CatalogHierarchyTraversalSession:`` a session to traverse
        hierarchies of catalogs
      * ``CatalogHierarchyDesignSession:`` a session to manage
        hierarchues of catalogs


    The cataloging manager also provides a profile for determing the
    supported search types supported by this service.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_session(self):
        """Gets the cataloging session for retrieving mappings to catalogs.

        :return: a ``CatalogSession``
        :rtype: ``osid.cataloging.CatalogSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogSession

    catalog_session = property(fget=get_catalog_session)

    @abc.abstractmethod
    def get_catalog_assignment_session(self):
        """Gets the cataloging session for adding and removing mappings to catalogs.

        :return: a ``CatalogAssignmentSession``
        :rtype: ``osid.cataloging.CatalogAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_assignment()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogAssignmentSession

    catalog_assignment_session = property(fget=get_catalog_assignment_session)

    @abc.abstractmethod
    def get_catalog_entry_notification_session(self, catalog_entry_receiver):
        """Gets the notification session for subscribing to changes to catalogs.

        :param catalog_entry_receiver: the notification callback
        :type catalog_entry_receiver: ``osid.cataloging.CatalogEntryReceiver``
        :return: a ``CatalogEntryNotificationSession``
        :rtype: ``osid.cataloging.CatalogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``catalog_entry_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_entry_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogEntryNotificationSession

    @abc.abstractmethod
    def get_catalog_entry_notification_session_for_catalog(self, catalog_entry_receiver, catalog_id):
        """Gets the notification session for subscribing to changes to catalogs for the given catalog.

        :param catalog_entry_receiver: the notification callback
        :type catalog_entry_receiver: ``osid.cataloging.CatalogEntryReceiver``
        :param catalog_id: the ``Id`` of the ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :return: a ``CatalogEntryNotificationSession``
        :rtype: ``osid.cataloging.CatalogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``catalog_entry_receiver`` or ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.cataloging.CatalogEntryNotificationSession

    @abc.abstractmethod
    def get_catalog_lookup_session(self):
        """Gets the catalog lookup session.

        :return: a ``CatalogLookupSession``
        :rtype: ``osid.cataloging.CatalogLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_lookup()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogLookupSession

    catalog_lookup_session = property(fget=get_catalog_lookup_session)

    @abc.abstractmethod
    def get_catalog_query_session(self):
        """Gets the catalog query session.

        :return: a ``CatalogQuerySession``
        :rtype: ``osid.cataloging.CatalogQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_query()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogQuerySession

    catalog_query_session = property(fget=get_catalog_query_session)

    @abc.abstractmethod
    def get_catalog_search_session(self):
        """Gets the catalog search session.

        :return: a ``CatalogSearchSession``
        :rtype: ``osid.cataloging.CatalogSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_search()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogSearchSession

    catalog_search_session = property(fget=get_catalog_search_session)

    @abc.abstractmethod
    def get_catalog_admin_session(self):
        """Gets the catalog administrative session for creating, updating and deleting catalogs.

        :return: a ``CatalogAdminSession``
        :rtype: ``osid.cataloging.CatalogAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_admin()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogAdminSession

    catalog_admin_session = property(fget=get_catalog_admin_session)

    @abc.abstractmethod
    def get_catalog_notification_session(self, catalog_receiver):
        """Gets the notification session for subscribing to changes to catalogs.

        :param catalog_receiver: the notification callback
        :type catalog_receiver: ``osid.cataloging.CatalogReceiver``
        :return: a ``CatalogNotificationSession``
        :rtype: ``osid.cataloging.CatalogNotificationSession``
        :raise: ``NullArgument`` -- ``catalog_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_notification()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogNotificationSession

    @abc.abstractmethod
    def get_catalog_hierarchy_session(self):
        """Gets the catalog hierarchy traversal session.

        :return: a ``CatalogHierarchySession``
        :rtype: ``osid.cataloging.CatalogHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogHierarchySession

    catalog_hierarchy_session = property(fget=get_catalog_hierarchy_session)

    @abc.abstractmethod
    def get_catalog_hierarchy_design_session(self):
        """Gets the catalog hierarchy design session.

        :return: a ``CatalogHierarchyDesignSession``
        :rtype: ``osid.cataloging.CatalogHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy_design()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogHierarchyDesignSession

    catalog_hierarchy_design_session = property(fget=get_catalog_hierarchy_design_session)

    @abc.abstractmethod
    def get_cataloging_rules_manager(self):
        """Gets the cataloging rules manager.

        :return: a ``CatalogingRulesManager``
        :rtype: ``osid.cataloging.rules.CatalogingRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_cataloging_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_cataloging_rules()`` is ``true``.*

        """
        return  # osid.cataloging.rules.CatalogingRulesManager

    cataloging_rules_manager = property(fget=get_cataloging_rules_manager)


class CatalogingProxyManager:
    """The cataloging manager provides access to cataloging sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for the
    purposes of passing information from server environments.

      * ``CatalogSession:`` a session to lookup mappings to catalogs
      * ``CatalogAssignmentSession:`` a session to manage Id to Catalog
        mappings
      * ``CatalogEntryNotificationSession:`` a session to receive
        notification of changed mappings
      * ``CatalogLookupSession:`` a session to retrieve catalogs
      * ``CatalogQuerySession:`` a session to query catalogs
      * ``CatalogSearchSession:`` a session to search for catalogs
      * ``CatalogAdminSession:`` a session to create, update and delete
        catalogs
      * ``CatalogNotificationSession:`` a session to receive
        notifications for changes in catalogs
      * ``CatalogHierarchyTraversalSession:`` a session to traverse
        hierarchies of catalogs
      * ``CatalogHierarchyDesignSession:`` a session to manage
        hierarchues of catalogs


    The cataloging manager also provides a profile for determing the
    supported search types supported by this service.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_session(self, proxy):
        """Gets the catalog session for retrieving ``Id`` to ``Catalog`` mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogSession``
        :rtype: ``osid.cataloging.CatalogSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogSession

    @abc.abstractmethod
    def get_catalog_assignment_session(self, proxy):
        """Gets the catalog session for mapping ``Ids`` to ``Catalogs``.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogAssignmentSession``
        :rtype: ``osid.cataloging.CatalogAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_assignment()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogAssignmentSession

    @abc.abstractmethod
    def get_catalog_entry_notification_session(self, catalog_entry_receiver, proxy):
        """Gets the catalog session for mapping ``Ids`` to ``Catalogs``.

        :param catalog_entry_receiver: the notification callback
        :type catalog_entry_receiver: ``osid.cataloging.CatalogEntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogEntryNotificationSession``
        :rtype: ``osid.cataloging.CatalogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``catalog_entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_entryt_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogEntryNotificationSession

    @abc.abstractmethod
    def get_catalog_entry_notification_session_for_catalog(self, catalog_entry_receiver, catalog_id, proxy):
        """Gets the notification session for subscribing to changes to catalogs for the given catalog.

        :param catalog_entry_receiver: the notification callback
        :type catalog_entry_receiver: ``osid.cataloging.CatalogEntryReceiver``
        :param catalog_id: the ``Id`` of the ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogEntryNotificationSession``
        :rtype: ``osid.cataloging.CatalogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``catalog_entry_receiver, catalog_id,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.cataloging.CatalogEntryNotificationSession

    @abc.abstractmethod
    def get_catalog_lookup_session(self, proxy):
        """Gets the catalog lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogLookupSession``
        :rtype: ``osid.cataloging.CatalogLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_lookup()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogLookupSession

    @abc.abstractmethod
    def get_catalog_query_session(self, proxy):
        """Gets the catalog query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogQuerySession``
        :rtype: ``osid.cataloging.CatalogQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_query()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogQuerySession

    @abc.abstractmethod
    def get_catalog_search_session(self, proxy):
        """Gets the catalog search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogSearchSession``
        :rtype: ``osid.cataloging.CatalogSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_search()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogSearchSession

    @abc.abstractmethod
    def get_catalog_admin_session(self, proxy):
        """Gets the catalog administrative session for creating, updating and deleting catalogs.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogAdminSession``
        :rtype: ``osid.cataloging.CatalogAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_admin()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogAdminSession

    @abc.abstractmethod
    def get_catalog_notification_session(self, catalog_receiver, proxy):
        """Gets the notification session for subscribing to changes to catalogs.

        :param catalog_receiver: the notification callback
        :type catalog_receiver: ``osid.cataloging.CatalogReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogNotificationSession``
        :rtype: ``osid.cataloging.CatalogNotificationSession``
        :raise: ``NullArgument`` -- ``catalog_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_notification()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogNotificationSession

    @abc.abstractmethod
    def get_catalog_hierarchy_session(self, proxy):
        """Gets the catalog hierarchy traversal session.

        :param proxy: proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogHierarchySession``
        :rtype: ``osid.cataloging.CatalogHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogHierarchySession

    @abc.abstractmethod
    def get_catalog_hierarchy_design_session(self, proxy):
        """Gets the catalog hierarchy design session.

        :param proxy: proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CatalogHierarchyDesignSession``
        :rtype: ``osid.cataloging.CatalogHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_catalog_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy_design()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogHierarchyDesignSession

    @abc.abstractmethod
    def get_cataloging_rules_proxy_manager(self):
        """Gets the cataloging rules proxy manager.

        :return: a ``CatalogingRulesManager``
        :rtype: ``osid.cataloging.rules.CatalogingRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_cataloging_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_cataloging_rules()`` is ``true``.*

        """
        return  # osid.cataloging.rules.CatalogingRulesProxyManager

    cataloging_rules_proxy_manager = property(fget=get_cataloging_rules_proxy_manager)
