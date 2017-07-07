"""Manager utility implementations of cataloging managers."""
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
from dlkit.abstract_osid.cataloging import managers as abc_cataloging_managers


class CatalogingProfile(abc_cataloging_managers.CatalogingProfile, osid_managers.OsidProfile):
    """The cataloging profile describes the interoperability among cataloging services."""

    def supports_visible_federation(self):
        """Tests if any billing federation is exposed.

        Federation is exposed when a specific catalog may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of catalogs appears as a
        single catalog.

        return: (boolean) - ``true`` if visible federation is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog(self):
        """Tests for the availability of a cataloging service retrieving ``Id`` to ``Catalog`` mappings.

        return: (boolean) - ``true`` if cataloging is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_assignment(self):
        """Tests for the availability of a cataloging service for mapping ``Ids`` to ``Catalogs``.

        return: (boolean) - ``true`` if catalog assignment is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_entry_notification(self):
        """Tests for the availability of a cataloging notification service for mapping ``Ids`` to ``Catalogs``.

        return: (boolean) - ``true`` if catalog entry notification is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_lookup(self):
        """Tests for the availability of a catalog lookup service.

        return: (boolean) - ``true`` if catalog lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_query(self):
        """Tests for the availability of a catalog query service that defines more comprehensive queries.

        return: (boolean) - ``true`` if catalog query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_search(self):
        """Tests for the availability of a catalog search service that defines more comprehensive queries.

        return: (boolean) - ``true`` if catalog search is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_admin(self):
        """Tests for the availability of a catalog administration service for the addition and deletion of catalogs.

        return: (boolean) - ``true`` if catalog administration is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_notification(self):
        """Tests for the availability of a catalog notification service.

        return: (boolean) - ``true`` if catalog notification is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_hierarchy(self):
        """Tests for the availability of a catalog hierarchy traversal service.

        return: (boolean) - ``true`` if catalog hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_catalog_hierarchy_design(self):
        """Tests for the availability of a catalog hierarchy design service.

        return: (boolean) - ``true`` if catalog hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def supports_cataloging_rules(self):
        """Tests if the cataloging rules sub services is supported.

        return: (boolean) - ``true`` if cataloging rules is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_catalog_record_types(self):
        """Gets the supported ``Catalog`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Catalog`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    catalog_record_types = property(fget=get_catalog_record_types)

    def supports_catalog_record_type(self, catalog_record_type=None):
        """Tests if the given ``Catalog`` record type is supported.

        arg:    catalog_record_type (osid.type.Type): a ``Type``
                indicating a ``Catalog`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``catalog_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if catalog_record_type is None:
            raise NullArgument()
        return False

    def get_catalog_search_record_types(self):
        """Gets the supported catalog search reciord types.

        return: (osid.type.TypeList) - a list containing the supported
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    catalog_search_record_types = property(fget=get_catalog_search_record_types)

    def supports_catalog_search_record_type(self, catalog_search_record_type=None):
        """Tests if the given catalog search record type is supported.

        arg:    catalog_search_record_type (osid.type.Type): a ``Type``
                indicating a catalog search record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``catalog_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if catalog_search_record_type is None:
            raise NullArgument()
        return False


class CatalogingManager(abc_cataloging_managers.CatalogingManager, osid_managers.OsidManager, CatalogingProfile):
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

    def get_catalog_session(self):
        """Gets the cataloging session for retrieving mappings to catalogs.

        return: (osid.cataloging.CatalogSession) - a ``CatalogSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_session = property(fget=get_catalog_session)

    def get_catalog_assignment_session(self):
        """Gets the cataloging session for adding and removing mappings to catalogs.

        return: (osid.cataloging.CatalogAssignmentSession) - a
                ``CatalogAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_assignment_session = property(fget=get_catalog_assignment_session)

    def get_catalog_entry_notification_session(self, catalog_entry_receiver=None):
        """Gets the notification session for subscribing to changes to catalogs.

        arg:    catalog_entry_receiver
                (osid.cataloging.CatalogEntryReceiver): the notification
                callback
        return: (osid.cataloging.CatalogEntryNotificationSession) - a
                ``CatalogEntryNotificationSession``
        raise:  NullArgument - ``catalog_entry_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_catalog_entry_notification()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_catalog_entry_notification_session_for_catalog(self, catalog_entry_receiver=None, catalog_id=None):
        """Gets the notification session for subscribing to changes to catalogs for the given catalog.

        arg:    catalog_entry_receiver
                (osid.cataloging.CatalogEntryReceiver): the notification
                callback
        arg:    catalog_id (osid.id.Id): the ``Id`` of the ``Catalog``
        return: (osid.cataloging.CatalogEntryNotificationSession) - a
                ``CatalogEntryNotificationSession``
        raise:  NullArgument - ``catalog_entry_receiver`` or
                ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_catalog_entry_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if catalog_entry_receiver is None:
            raise NullArgument
        if catalog_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_catalog_lookup_session(self):
        """Gets the catalog lookup session.

        return: (osid.cataloging.CatalogLookupSession) - a
                ``CatalogLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_lookup_session = property(fget=get_catalog_lookup_session)

    def get_catalog_query_session(self):
        """Gets the catalog query session.

        return: (osid.cataloging.CatalogQuerySession) - a
                ``CatalogQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_query()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_query_session = property(fget=get_catalog_query_session)

    def get_catalog_search_session(self):
        """Gets the catalog search session.

        return: (osid.cataloging.CatalogSearchSession) - a
                ``CatalogSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_search()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_search_session = property(fget=get_catalog_search_session)

    def get_catalog_admin_session(self):
        """Gets the catalog administrative session for creating, updating and deleting catalogs.

        return: (osid.cataloging.CatalogAdminSession) - a
                ``CatalogAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_admin()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_admin_session = property(fget=get_catalog_admin_session)

    def get_catalog_notification_session(self, catalog_receiver=None):
        """Gets the notification session for subscribing to changes to catalogs.

        arg:    catalog_receiver (osid.cataloging.CatalogReceiver): the
                notification callback
        return: (osid.cataloging.CatalogNotificationSession) - a
                ``CatalogNotificationSession``
        raise:  NullArgument - ``catalog_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_catalog_hierarchy_session(self):
        """Gets the catalog hierarchy traversal session.

        return: (osid.cataloging.CatalogHierarchySession) - a
                ``CatalogHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_hierarchy_session = property(fget=get_catalog_hierarchy_session)

    def get_catalog_hierarchy_design_session(self):
        """Gets the catalog hierarchy design session.

        return: (osid.cataloging.CatalogHierarchyDesignSession) - a
                ``CatalogHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_hierarchy_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy_design()`` is ``true``.*

        """
        raise Unimplemented()

    catalog_hierarchy_design_session = property(fget=get_catalog_hierarchy_design_session)

    def get_cataloging_rules_manager(self):
        """Gets the cataloging rules manager.

        return: (osid.cataloging.rules.CatalogingRulesManager) - a
                ``CatalogingRulesManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_cataloging_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_cataloging_rules()`` is ``true``.*

        """
        raise Unimplemented()

    cataloging_rules_manager = property(fget=get_cataloging_rules_manager)


class CatalogingProxyManager(abc_cataloging_managers.CatalogingProxyManager, osid_managers.OsidProxyManager, CatalogingProfile):
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

    def get_catalog_session(self, proxy=None):
        """Gets the catalog session for retrieving ``Id`` to ``Catalog`` mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogSession) - a ``CatalogSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_assignment_session(self, proxy=None):
        """Gets the catalog session for mapping ``Ids`` to ``Catalogs``.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogAssignmentSession) - a
                ``CatalogAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_entry_notification_session(self, catalog_entry_receiver=None, proxy=None):
        """Gets the catalog session for mapping ``Ids`` to ``Catalogs``.

        arg:    catalog_entry_receiver
                (osid.cataloging.CatalogEntryReceiver): the notification
                callback
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogEntryNotificationSession) - a
                ``CatalogEntryNotificationSession``
        raise:  NullArgument - ``catalog_entry_receiver`` or ``proxy``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_catalog_entryt_notification()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_entry_notification_session_for_catalog(self, catalog_entry_receiver=None, catalog_id=None, proxy=None):
        """Gets the notification session for subscribing to changes to catalogs for the given catalog.

        arg:    catalog_entry_receiver
                (osid.cataloging.CatalogEntryReceiver): the notification
                callback
        arg:    catalog_id (osid.id.Id): the ``Id`` of the ``Catalog``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogEntryNotificationSession) - a
                ``CatalogEntryNotificationSession``
        raise:  NullArgument - ``catalog_entry_receiver, catalog_id,``
                or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_catalog_entry_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if catalog_entry_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_catalog_lookup_session(self, proxy=None):
        """Gets the catalog lookup session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogLookupSession) - a
                ``CatalogLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_query_session(self, proxy=None):
        """Gets the catalog query session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogQuerySession) - a
                ``CatalogQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_search_session(self, proxy=None):
        """Gets the catalog search session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogSearchSession) - a
                ``CatalogSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_admin_session(self, proxy=None):
        """Gets the catalog administrative session for creating, updating and deleting catalogs.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogAdminSession) - a
                ``CatalogAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_notification_session(self, catalog_receiver=None, proxy=None):
        """Gets the notification session for subscribing to changes to catalogs.

        arg:    catalog_receiver (osid.cataloging.CatalogReceiver): the
                notification callback
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.cataloging.CatalogNotificationSession) - a
                ``CatalogNotificationSession``
        raise:  NullArgument - ``catalog_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_hierarchy_session(self, proxy=None):
        """Gets the catalog hierarchy traversal session.

        arg:    proxy (osid.proxy.Proxy): proxy
        return: (osid.cataloging.CatalogHierarchySession) - a
                ``CatalogHierarchySession``
        raise:  NullArgument - ``proxy`` is null
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_catalog_hierarchy_design_session(self, proxy=None):
        """Gets the catalog hierarchy design session.

        arg:    proxy (osid.proxy.Proxy): proxy
        return: (osid.cataloging.CatalogHierarchyDesignSession) - a
                ``CatalogHierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is null
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_catalog_hierarchy_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_catalog_hierarchy_design()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_cataloging_rules_proxy_manager(self):
        """Gets the cataloging rules proxy manager.

        return: (osid.cataloging.rules.CatalogingRulesProxyManager) - a
                ``CatalogingRulesManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_cataloging_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_cataloging_rules()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    cataloging_rules_proxy_manager = property(fget=get_cataloging_rules_proxy_manager)
