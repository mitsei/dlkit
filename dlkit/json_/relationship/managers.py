"""JSON implementations of relationship managers."""

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
from dlkit.manager_impls.relationship import managers as relationship_managers


class RelationshipProfile(osid_managers.OsidProfile, relationship_managers.RelationshipProfile):
    """The relationship profile describes the interoperability among relationship services."""

    def supports_relationship_lookup(self):
        """Tests if looking up relationships is supported.

        return: (boolean) - ``true`` if relationship lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_relationship_lookup' in profile.SUPPORTS

    def supports_relationship_query(self):
        """Tests if querying relationships is supported.

        return: (boolean) - ``true`` if relationship query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_relationship_query' in profile.SUPPORTS

    def supports_relationship_admin(self):
        """Tests if relationship administrative service is supported.

        return: (boolean) - ``true`` if relationship administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_relationship_admin' in profile.SUPPORTS

    def supports_family_lookup(self):
        """Tests if looking up families is supported.

        return: (boolean) - ``true`` if family lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_family_lookup' in profile.SUPPORTS

    def supports_family_admin(self):
        """Tests if familyadministrative service is supported.

        return: (boolean) - ``true`` if family administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_family_admin' in profile.SUPPORTS

    def supports_family_hierarchy(self):
        """Tests for the availability of a family hierarchy traversal service.

        return: (boolean) - ``true`` if family hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_family_hierarchy' in profile.SUPPORTS

    def supports_family_hierarchy_design(self):
        """Tests for the availability of a family hierarchy design service.

        return: (boolean) - ``true`` if family hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_family_hierarchy_design' in profile.SUPPORTS

    def get_relationship_record_types(self):
        """Gets the supported ``Relationship`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Relationship`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('RELATIONSHIP_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    relationship_record_types = property(fget=get_relationship_record_types)

    def get_relationship_search_record_types(self):
        """Gets the supported ``Relationship`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Relationship`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('RELATIONSHIP_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    def get_family_record_types(self):
        """Gets the supported ``Family`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Family`` types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('FAMILY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    family_record_types = property(fget=get_family_record_types)

    def get_family_search_record_types(self):
        """Gets the supported ``Family`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Family`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('FAMILY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    family_search_record_types = property(fget=get_family_search_record_types)


class RelationshipManager(osid_managers.OsidManager, RelationshipProfile, relationship_managers.RelationshipManager):
    """The relationship manager provides access to relationship sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``RelationshipLookupSession:`` a session to retrieve and examine
        relationships
      * ``RelationshipQuerySession:`` a session to query relationships
      * ``RelationshipSearchSession:`` a session to search for
        relationships
      * ``RelationshipAdminSession:`` a session to manage relationships
      * ``RelationshipNotificationSession:`` a session to receive
        notifications pertaining to relationship changes
      * ``RelationshipFamilySession:`` a session to look up relationship
        to family mappings
      * ``RelationshipFamilyAssignmentSession:`` a session to manage
        relationship to family catalog mappings
      * ``RelationshipSmartFamilySession:`` a session to manage dynamic
        relationship families

      * ``FamilyLookupSession:`` a session to retrieve families
      * ``FamilyQuerySession:`` a session to query families
      * ``FamilySearchSession:`` a session to search for families
      * ``FamilyAdminSession:`` a session to create and delete families
      * ``FamilyNotificationSession:`` a session to receive
        notifications pertaining to family changes
      * ``FamilyHierarchySession:`` a session to traverse a hierarchy of
        families
      * ``FamilyHierarchyDesignSession:`` a session to manage a family
        hierarchy

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` is ``true``.*

        """
        if not self.supports_relationship_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.RelationshipLookupSession(runtime=self._runtime)

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_relationship_lookup_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_relationship_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.RelationshipLookupSession(family_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the relationship query service.

        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` is ``true``.*

        """
        if not self.supports_relationship_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.RelationshipQuerySession(runtime=self._runtime)

    relationship_query_session = property(fget=get_relationship_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_relationship_query_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_relationship_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.RelationshipQuerySession(family_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` is ``true``.*

        """
        if not self.supports_relationship_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.RelationshipAdminSession(runtime=self._runtime)

    relationship_admin_session = property(fget=get_relationship_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_relationship_admin_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  NotFound - no family found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_relationship_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.RelationshipAdminSession(family_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_family_lookup_session(self):
        """Gets the ``OsidSession`` associated with the family lookup service.

        return: (osid.relationship.FamilyLookupSession) - a
                ``FamilyLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_lookup()`` is ``true``.*

        """
        if not self.supports_family_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyLookupSession(runtime=self._runtime)

    family_lookup_session = property(fget=get_family_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_family_admin_session(self):
        """Gets the ``OsidSession`` associated with the family administrative service.

        return: (osid.relationship.FamilyAdminSession) - a
                ``FamilyAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_admin()`` is ``true``.*

        """
        if not self.supports_family_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyAdminSession(runtime=self._runtime)

    family_admin_session = property(fget=get_family_admin_session)

    @utilities.remove_null_proxy_kwarg
    def get_family_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        return: (osid.relationship.FamilyHierarchySession) - a
                ``FamilyHierarchySession`` for families
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy()`` is ``true``.*

        """
        if not self.supports_family_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyHierarchySession(runtime=self._runtime)

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
    def get_family_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        return: (osid.relationship.FamilyHierarchyDesignSession) - a
                ``HierarchyDesignSession`` for families
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_family_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyHierarchyDesignSession(runtime=self._runtime)

    family_hierarchy_design_session = property(fget=get_family_hierarchy_design_session)

    def get_relationship_batch_manager(self):
        """Gets the relationship batch manager.

        return: (osid.relationship.batch.RelationshipBatchManager) - a
                ``RelationshipBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    relationship_batch_manager = property(fget=get_relationship_batch_manager)

    def get_relationship_rules_manager(self):
        """Gets the relationship rules manager.

        return: (osid.relationship.rules.RelationshipRulesManager) - a
                ``RelationshipRulesManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_rules()`` is ``true``.*

        """
        raise errors.Unimplemented()

    relationship_rules_manager = property(fget=get_relationship_rules_manager)


class RelationshipProxyManager(osid_managers.OsidProxyManager, RelationshipProfile, relationship_managers.RelationshipProxyManager):
    """The relationship manager provides access to relationship sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a Proxy. The sessions
    included in this manager are:

      * ``RelationshipLookupSession:`` a session to retrieve and examine
        relationships
      * ``RelationshipQuerySession:`` a session to query relationships
      * ``RelationshipSearchSession:`` a session to search for
        relationships
      * ``RelationshipAdminSession:`` a session to manage relationships
      * ``RelationshipNotificationSession:`` a session to receive
        notifications pertaining to relationship changes
      * ``RelationshipFamilySession:`` a session to look up relationship
        to family mappings
      * ``RelationshipFamilyAssignmentSession:`` a session to manage
        relationship to family catalog mappings
      * ``RelationshipSmartFamilySession:`` a session to manage dynamic
        relationship families

      * ``FamilyLookupSession:`` a session to retrieve families
      * ``FamilyQuerySession:`` a session to query families
      * ``FamilySearchSession:`` a session to search for families
      * ``FamilyAdminSession:`` a session to create and delete families
      * ``FamilyNotificationSession:`` a session to receive
        notifications pertaining to family changes
      * ``FamilyHierarchySession:`` a session to traverse a hierarchy of
        families
      * ``FamilyHierarchyDesignSession:`` a session to manage a family
        hierarchy

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_relationship_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` is ``true``.*

        """
        if not self.supports_relationship_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.RelationshipLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationship_lookup_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_relationship_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.RelationshipLookupSession(family_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_relationship_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` is ``true``.*

        """
        if not self.supports_relationship_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.RelationshipQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationship_query_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_relationship_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.RelationshipQuerySession(family_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_relationship_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` is ``true``.*

        """
        if not self.supports_relationship_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.RelationshipAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationship_admin_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_relationship_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.RelationshipAdminSession(family_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_family_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyLookupSession) - a
                ``FamilyLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_lookup()`` is ``true``.*

        """
        if not self.supports_family_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_family_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyAdminSession) - a
                ``FamilyAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_admin()`` is ``true``.*

        """
        if not self.supports_family_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_family_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyHierarchySession) - a
                ``FamilyHierarchySession`` for families
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy()`` is ``true``.*

        """
        if not self.supports_family_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_family_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyHierarchyDesignSession) - a
                ``HierarchyDesignSession`` for families
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_family_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.FamilyHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    def get_relationship_batch_proxy_manager(self):
        """Gets the relationship batch proxy manager.

        return: (osid.relationship.batch.RelationshipBatchProxyManager)
                - a ``RelationshipBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_rules()`` is ``true``.*

        """
        raise errors.Unimplemented()

    relationship_batch_proxy_manager = property(fget=get_relationship_batch_proxy_manager)

    def get_relationship_rules_proxy_manager(self):
        """Gets the relationship rules proxy manager.

        return: (osid.relationship.rules.RelationshipRulesProxyManager)
                - a ``RelationshipRulesProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_rules()`` is ``true``.*

        """
        raise errors.Unimplemented()

    relationship_rules_proxy_manager = property(fget=get_relationship_rules_proxy_manager)
