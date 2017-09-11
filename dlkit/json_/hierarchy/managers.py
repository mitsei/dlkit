"""JSON implementations of hierarchy managers."""

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
from dlkit.manager_impls.hierarchy import managers as hierarchy_managers


class HierarchyProfile(osid_managers.OsidProfile, hierarchy_managers.HierarchyProfile):
    """The hierarchy profile describes the interoperability among hierarchy services."""

    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.

        return: (boolean) - ``true`` if hierarchy traversal is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_hierarchy_traversal' in profile.SUPPORTS

    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.

        return: (boolean) - ``true`` if hierarchy design is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_hierarchy_design' in profile.SUPPORTS

    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.

        return: (boolean) - ``true`` if hierarchy lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_hierarchy_lookup' in profile.SUPPORTS

    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.

        return: (boolean) - ``true`` if hierarchy administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_hierarchy_admin' in profile.SUPPORTS

    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Hierarchy`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('HIERARCHY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Hierarchy`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('HIERARCHY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)


class HierarchyManager(osid_managers.OsidManager, HierarchyProfile, hierarchy_managers.HierarchyManager):
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
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_hierarchy_traversal_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        return: (osid.hierarchy.HierarchyTraversalSession) - a
                ``HierarchyTraversalSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_traversal()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` is ``true``.*

        """
        if not self.supports_hierarchy_traversal():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyTraversalSession(runtime=self._runtime)

    hierarchy_traversal_session = property(fget=get_hierarchy_traversal_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the hierarchy
        return: (osid.hierarchy.HierarchyTraversalSession) - the new
                ``HierarchyTraversalSession``
        raise:  NotFound - ``hierarchy_id`` not found
        raise:  NullArgument - ``hierarchyid`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_hierarchy_traversal()`` or
                ``supports_visible_fedaration()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_hierarchy_traversal():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.HierarchyTraversalSession(hierarchy_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        return: (osid.hierarchy.HierarchyDesignSession) - a
                ``HierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyDesignSession(runtime=self._runtime)

    hierarchy_design_session = property(fget=get_hierarchy_design_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the graph
        return: (osid.hierarchy.HierarchyDesignSession) - a
                ``HierarchyDesignSession``
        raise:  NotFound - ``hierarchy_id`` is not found
        raise:  NullArgument - ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_hierarchy_design():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.HierarchyDesignSession(hierarchy_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_hierarchy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        return: (osid.hierarchy.HierarchyLookupSession) - a
                ``HierarchyLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_lookup()`` is ``true``.*

        """
        if not self.supports_hierarchy_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyLookupSession(runtime=self._runtime)

    hierarchy_lookup_session = property(fget=get_hierarchy_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_hierarchy_admin_session(self):
        """Gets the hierarchy administrative session.

        return: (osid.hierarchy.HierarchyAdminSession) - a
                ``HierarchyAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_admin()`` is ``true``.*

        """
        if not self.supports_hierarchy_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyAdminSession(runtime=self._runtime)

    hierarchy_admin_session = property(fget=get_hierarchy_admin_session)


class HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile, hierarchy_managers.HierarchyProxyManager):
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
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_hierarchy_traversal_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.hierarchy.HierarchyTraversalSession) - a
                ``HierarchyTraversalSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_traversal()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` is ``true``.*

        """
        if not self.supports_hierarchy_traversal():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyTraversalSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the hierarchy
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.hierarchy.HierarchyTraversalSession) - a
                ``HierarchyTraversalSession``
        raise:  NotFound - ``hierarchyid`` not found
        raise:  NullArgument - ``hierarchy_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_hierarchy_traversal()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_hierarchy_traversal():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.HierarchyTraversalSession(hierarchy_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.hierarchy.HierarchyDesignSession) - a
                ``HierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the hierarchy
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.hierarchy.HierarchyDesignSession) - a
                ``HierarchyDesignSession``
        raise:  NotFound - ``hierarchy_id`` is not found
        raise:  NullArgument - ``hierarchy_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_hierarchy_design():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.HierarchyDesignSession(hierarchy_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_hierarchy_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.hierarchy.HierarchyLookupSession) - a
                ``HierarchyLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_lookup()`` is ``true``.*

        """
        if not self.supports_hierarchy_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_hierarchy_admin_session(self, proxy):
        """Gets the hierarchy administrative session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.hierarchy.HierarchyAdminSession) - a
                ``HierarchyAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_admin()`` is ``true``.*

        """
        if not self.supports_hierarchy_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.HierarchyAdminSession(proxy=proxy, runtime=self._runtime)
