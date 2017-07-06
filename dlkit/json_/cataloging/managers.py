"""JSON implementations of cataloging managers."""

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
from dlkit.manager_impls.cataloging import managers as cataloging_managers


class CatalogingProfile(osid_managers.OsidProfile, cataloging_managers.CatalogingProfile):
    """The cataloging profile describes the interoperability among cataloging services."""

    def supports_catalog_lookup(self):
        """Tests for the availability of a catalog lookup service.

        return: (boolean) - ``true`` if catalog lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_catalog_lookup' in profile.SUPPORTS

    def supports_catalog_query(self):
        """Tests for the availability of a catalog query service that defines more comprehensive queries.

        return: (boolean) - ``true`` if catalog query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_catalog_query' in profile.SUPPORTS

    def supports_catalog_admin(self):
        """Tests for the availability of a catalog administration service for the addition and deletion of catalogs.

        return: (boolean) - ``true`` if catalog administration is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_catalog_admin' in profile.SUPPORTS

    def supports_catalog_hierarchy(self):
        """Tests for the availability of a catalog hierarchy traversal service.

        return: (boolean) - ``true`` if catalog hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_catalog_hierarchy' in profile.SUPPORTS

    def supports_catalog_hierarchy_design(self):
        """Tests for the availability of a catalog hierarchy design service.

        return: (boolean) - ``true`` if catalog hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_catalog_hierarchy_design' in profile.SUPPORTS

    def get_catalog_record_types(self):
        """Gets the supported ``Catalog`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Catalog`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('CATALOG_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    catalog_record_types = property(fget=get_catalog_record_types)

    def get_catalog_search_record_types(self):
        """Gets the supported catalog search reciord types.

        return: (osid.type.TypeList) - a list containing the supported
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('CATALOG_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    catalog_search_record_types = property(fget=get_catalog_search_record_types)


class CatalogingManager(osid_managers.OsidManager, CatalogingProfile, cataloging_managers.CatalogingManager):
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
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_catalog_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogLookupSession(runtime=self._runtime)

    catalog_lookup_session = property(fget=get_catalog_lookup_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_catalog_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogQuerySession(runtime=self._runtime)

    catalog_query_session = property(fget=get_catalog_query_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_catalog_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogAdminSession(runtime=self._runtime)

    catalog_admin_session = property(fget=get_catalog_admin_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_catalog_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogHierarchySession(runtime=self._runtime)

    catalog_hierarchy_session = property(fget=get_catalog_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_catalog_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogHierarchyDesignSession(runtime=self._runtime)

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
        raise errors.Unimplemented()

    cataloging_rules_manager = property(fget=get_cataloging_rules_manager)


class CatalogingProxyManager(osid_managers.OsidProxyManager, CatalogingProfile, cataloging_managers.CatalogingProxyManager):
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
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_catalog_lookup_session(self, proxy):
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
        if not self.supports_catalog_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_catalog_query_session(self, proxy):
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
        if not self.supports_catalog_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_catalog_admin_session(self, proxy):
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
        if not self.supports_catalog_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_catalog_hierarchy_session(self, proxy):
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
        if not self.supports_catalog_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_catalog_hierarchy_design_session(self, proxy):
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
        if not self.supports_catalog_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CatalogHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

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
        raise errors.Unimplemented()

    cataloging_rules_proxy_manager = property(fget=get_cataloging_rules_proxy_manager)
