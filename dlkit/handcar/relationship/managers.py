# -*- coding: utf-8 -*-

# This module contains all the Manager classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Relationship Service.

from ...abstract_osid.relationship import managers as abc_relationship_managers
from ..osid import managers as osid_managers
from .. import profile
from ..primitives import Id, DisplayText, Type
from ..type.objects import TypeList
from ..osid.osid_errors import NotFound, NullArgument, OperationFailed, Unimplemented


class RelationshipProfile(abc_relationship_managers.RelationshipProfile, osid_managers.OsidProfile):
    """The relationship profile describes the interoperability among relationship services."""

    def supports_visible_federation(self):
        """Tests if any family federation is exposed.

        Federation is exposed when a specific family may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of families appears as a
        single family.

        return: (boolean) - ``true`` if visible federation is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_visible_federation' in profile.SUPPORTS

    def supports_relationship_lookup(self):
        """Tests if looking up relationships is supported.

        return: (boolean) - ``true`` if relationship lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_lookup' in profile.SUPPORTS

    def supports_relationship_query(self):
        """Tests if querying relationships is supported.

        return: (boolean) - ``true`` if relationship query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_query' in profile.SUPPORTS

    def supports_relationship_search(self):
        """Tests if searching relationships is supported.

        return: (boolean) - ``true`` if relationship search is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_search' in profile.SUPPORTS

    def supports_relationship_admin(self):
        """Tests if relationship administrative service is supported.

        return: (boolean) - ``true`` if relationship administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_admin' in profile.SUPPORTS

    def supports_relationship_notification(self):
        """Tests if a relationship notification service is supported.

        return: (boolean) - ``true`` if relationship notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_notification' in profile.SUPPORTS

    def supports_relationship_family(self):
        """Tests if a relationship family cataloging service is supported.

        return: (boolean) - ``true`` if relationship families are
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_family' in profile.SUPPORTS

    def supports_relationship_family_assignment(self):
        """Tests if a relationship cataloging service is supported.

        A relationship cataloging service maps relationships to
        families.

        return: (boolean) - ``true`` if relationship families are
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_family_assignment' in profile.SUPPORTS

    def supports_relationship_smart_family(self):
        """Tests if a relationship smart family cataloging service is supported.

        return: (boolean) - ``true`` if relationship smart families are
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_smart_family' in profile.SUPPORTS

    def supports_family_lookup(self):
        """Tests if looking up families is supported.

        return: (boolean) - ``true`` if family lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_family_lookup' in profile.SUPPORTS

    def supports_family_query(self):
        """Tests if querying families is supported.

        return: (boolean) - ``true`` if family query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_family_query' in profile.SUPPORTS

    def supports_family_search(self):
        """Tests if searching families is supported.

        return: (boolean) - ``true`` if family search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_family_search' in profile.SUPPORTS

    def supports_family_admin(self):
        """Tests if familyadministrative service is supported.

        return: (boolean) - ``true`` if family administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_family_admin' in profile.SUPPORTS

    def supports_family_notification(self):
        """Tests if a family notification service is supported.

        return: (boolean) - ``true`` if family notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_family_notification' in profile.SUPPORTS

    def supports_family_hierarchy(self):
        """Tests for the availability of a family hierarchy traversal service.

        return: (boolean) - ``true`` if family hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all providers.*

        """
        return 'supports_family_hierarchy' in profile.SUPPORTS

    def supports_family_hierarchy_design(self):
        """Tests for the availability of a family hierarchy design service.

        return: (boolean) - ``true`` if family hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_family_hierarchy_design' in profile.SUPPORTS

    def supports_relationship_batch(self):
        """Tests for the availability of a relationship batch service.

        return: (boolean) - ``true`` if a relationship batch service is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_batch' in profile.SUPPORTS

    def supports_relationship_rules(self):
        """Tests if a relationship rules service is supported.

        return: (boolean) - ``true`` if relationship rules service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_relationship_rules' in profile.SUPPORTS

    def get_relationship_record_types(self):
        """Gets the supported ``Relationship`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Relationship`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    def supports_relationship_record_type(self, relationship_record_type=None):
        """Tests if the given ``Relationship`` record type is supported.

        arg:    relationship_record_type (osid.type.Type): a ``Type``
                indicating a ``Relationship`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_relationship_search_record_types(self):
        """Gets the supported ``Relationship`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Relationship`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    def supports_relationship_search_record_type(self, relationship_search_record_type=None):
        """Tests if the given ``Relationship`` search record type is supported.

        arg:    relationship_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``Relationship`` search record
                type
        return: (boolean) - ``true`` if the given search record type is
                supported, ``false`` otherwise
        raise:  NullArgument - ``relationship_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_family_record_types(self):
        """Gets the supported ``Family`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Family`` types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    def supports_family_record_type(self, family_record_type=None):
        """Tests if the given ``Family`` record type is supported.

        arg:    family_record_type (osid.type.Type): a ``Type``
                indicating a ``Family`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``family_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_family_search_record_types(self):
        """Gets the supported ``Family`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Family`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    def supports_family_search_record_type(self, family_search_record_type=None):
        """Tests if the given ``Family`` search record type is supported.

        arg:    family_search_record_type (osid.type.Type): a ``Type``
                indicating a ``Family`` search record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``family_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return False


class RelationshipManager(abc_relationship_managers.RelationshipManager,
                          osid_managers.OsidManager,
                          RelationshipProfile):
    """The relationship manager provides access to relationship sessions and provides
        interoperability tests for various aspects of this service.

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

    def get_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_lookup()``
            is ``true``.*

        """
        if not self.supports_relationship_lookup():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipLookupSession(proxy=self._proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_lookup_session_for_family(self, family_id=None):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_lookup()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_lookup():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipLookupSession(family_id,
                                                         proxy=self._proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the relationship query service.

        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_query()`` is ``true``.*

        """
        if not self.supports_relationship_query():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipQuerySession(proxy=self._proxy,
                                                        runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_query_session_for_family(self, family_id=None):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_query()`` and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_query():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipQuerySession(family_id,
                                                        proxy=self._proxy,
                                                        runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_search_session(self):
        """Gets the ``OsidSession`` associated with the relationship search service.

        return: (osid.relationship.RelationshipSearchSession) - a
                ``RelationshipSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_search()`` is ``true``.*

        """
        if not self.supports_relationship_search():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipSearchSession(proxy=self._proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_search_session_for_family(self, family_id=None):
        """Gets the ``OsidSession`` associated with the relationship search service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.RelationshipSearchSession) - a
                ``RelationshipSearchSession``
        raise:  NotFound - no family found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_search()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_search():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipSearchSession(family_id,
                                                         proxy=self._proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_admin()`` is ``true``.*

        """
        if not self.supports_relationship_admin():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipAdminSession(proxy=self._proxy,
                                                        runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_admin_session_for_family(self, family_id=None):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  NotFound - no family found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_admin()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_admin():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipAdminSession(family_id,
                                                        proxy=self._proxy,
                                                        runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_notification_session(self, relationship_receiver=None):
        """Gets the ``OsidSession`` associated with the relationship notification service.

        arg:    relationship_receiver
                (osid.relationship.RelationshipReceiver): the receiver
        return: (osid.relationship.RelationshipNotificationSession) - a
                ``RelationshipNotificationSession``
        raise:  NullArgument - ``relationship_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_notification()`` is ``true``.*

        """
        pass

    def get_relationship_notification_session_for_family(self, relationship_receiver=None, family_id=None):
        """Gets the ``OsidSession`` associated with the relationship notification service for the given family.

        arg:    relationship_receiver
                (osid.relationship.RelationshipReceiver): the receiver
        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.RelationshipNotificationSession) - a
                ``RelationshipNotificationSession``
        raise:  NotFound - no family found by the given ``Id``
        raise:  NullArgument - ``relationship_receiver`` or
                ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_notification()``
            and ``supports_visible_federation()`` are ``true``*

        """
        pass

    def get_relationship_family_session(self):
        """Gets the ``OsidSession`` to lookup relationship/family mappings.

        return: (osid.relationship.RelationshipFamilySession) - a
                ``RelationshipFamilySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_family()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_family()`` is ``true``.*

        """
        if not self.supports_relationship_family():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipFamilySession(proxy=self._proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_family_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning relationships to families.

        return: (osid.relationship.RelationshipFamilyAssignmentSession)
                - a ``RelationshipFamilyAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_relationship_family_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_family_assignment()``
            is ``true``.*

        """
        if not self.supports_relationship_family_assignment():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.RelationshipFamilyAssignmentSession(proxy=self._proxy,
                                                                   runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_smart_family_session(self, family_id=None):
        """Gets the ``OsidSession`` to manage dynamic families of relationships.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.RelationshipSmartFamilySession) - a
                ``RelationshipSmartFamilySession``
        raise:  NotFound - no family found by the given ``Id``
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_smart_family()``
                is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_smart_family()``
            is ``true``.*

        """
        pass

    def get_family_lookup_session(self):
        """Gets the ``OsidSession`` associated with the family lookup service.

        return: (osid.relationship.FamilyLookupSession) - a
                ``FamilyLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_lookup()`` is ``true``.*

        """
        if not self.supports_family_lookup():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.FamilyLookupSession(proxy=self._proxy,
                                                   runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_query_session(self):
        """Gets the ``OsidSession`` associated with the family query service.

        return: (osid.relationship.FamilyQuerySession) - a
                ``FamilyQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_query()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_query()`` is ``true``.*

        """
        if not self.supports_family_query():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.FamilyQuerySession(proxy=self._proxy,
                                                  runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_search_session(self):
        """Gets the ``OsidSession`` associated with the family search service.

        return: (osid.relationship.FamilySearchSession) - a
                ``FamilySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_search()`` is ``true``.*

        """
        if not self.supports_family_search():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.FamilySearchSession(proxy=self._proxy,
                                                   runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_admin_session(self):
        """Gets the ``OsidSession`` associated with the family administrative service.

        return: (osid.relationship.FamilyAdminSession) - a
                ``FamilyAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_admin()`` is ``true``.*

        """
        if not self.supports_family_admin():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.FamilyAdminSession(proxy=self._proxy,
                                                  runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_notification_session(self, family_receiver=None):
        """Gets the ``OsidSession`` associated with the family notification service.

        arg:    family_receiver (osid.relationship.FamilyReceiver): the
                receiver
        return: (osid.relationship.FamilyNotificationSession) - a
                ``FamilyNotificationSession``
        raise:  NullArgument - ``family_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_notification()``
            is ``true``.*

        """
        pass

    def get_family_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        return: (osid.relationship.FamilyHierarchySession) - a
                ``FamilyHierarchySession`` for families
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_hierarchy()``
            is ``true``.*

        """
        if not self.supports_family_hierarchy():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.FamilyHierarchySession(proxy=self._proxy,
                                                      runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        return: (osid.relationship.FamilyHierarchyDesignSession) - a
                ``HierarchyDesignSession`` for families
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_hierarchy_design()``
            is ``true``.*

        """
        if not self.supports_family_hierarchy_design():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        try:
            session = sessions.FamilyHierarchyDesignSession(proxy=self._proxy,
                                                            runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_batch_manager(self):
        """Gets the relationship batch manager.

        return: (osid.relationship.batch.RelationshipBatchManager) - a
                ``RelationshipBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_batch()`` is ``true``.*

        """
        pass

    def get_relationship_rules_manager(self):
        """Gets the relationship rules manager.

        return: (osid.relationship.rules.RelationshipRulesManager) - a
                ``RelationshipRulesManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_rules()`` is ``true``.*

        """
        pass


class RelationshipProxyManager(abc_relationship_managers.RelationshipProxyManager,
                               osid_managers.OsidProxyManager,
                               RelationshipProfile):
    """The relationship manager provides access to relationship sessions and provides
        interoperability tests for various aspects of this service.

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

    def get_relationship_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipLookupSession) - a
                ``RelationshipLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_lookup()`` is ``true``.*

        """
        if not self.supports_relationship_lookup():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipLookupSession(proxy=proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_lookup_session_for_family(self, family_id=None, proxy=None, *args, **kwargs):
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
        *compliance: optional -- This method must be implemented if ``supports_relationship_lookup()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_lookup():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipLookupSession(family_id, proxy=proxy, runtime=self._runtime, **kwargs)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipQuerySession) - a
                ``RelationshipQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_query()`` is ``true``.*

        """
        if not self.supports_relationship_query():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipQuerySession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_query_session_for_family(self, family_id=None, proxy=None):
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
        *compliance: optional -- This method must be implemented if ``supports_relationship_query()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_query():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipQuerySession(family_id, proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipSearchSession) - a
                ``RelationshipSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_search()`` is ``true``.*

        """
        if not self.supports_relationship_search():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipSearchSession(proxy=proxy,
                                                         runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_search_session_for_family(self, family_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship search service for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of the family
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipSearchSession) - a
                ``RelationshipSearchSession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``family_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_search()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_search():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipSearchSession(family_id, proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipAdminSession) - a
                ``RelationshipAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_admin()`` is ``true``.*

        """
        if not self.supports_relationship_admin():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipAdminSession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_admin_session_for_family(self, family_id=None, proxy=None, *args, **kwargs):
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
        *compliance: optional -- This method must be implemented if ``supports_relationship_admin()``
            and ``supports_visible_federation()`` are ``true``*

        """
        if not family_id:
            raise NullArgument
        if not self.supports_relationship_admin():
            raise Unimplemented()
        ##
        # Need to include check to see if the familyId is found otherwise raise NotFound
        ##
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipAdminSession(family_id, proxy=proxy, runtime=self._runtime, **kwargs)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_notification_session(self, relationship_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship notification service.

        arg:    relationship_receiver
                (osid.relationship.RelationshipReceiver): the receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipNotificationSession) - a
                ``RelationshipNotificationSession``
        raise:  NullArgument - ``relationship_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_notification()``
            is ``true``.*

        """
        pass

    def get_relationship_notification_session_for_family(self, relationship_receiver=None, family_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the relationship notification service for the given family.

        arg:    relationship_receiver
                (osid.relationship.RelationshipReceiver): the receiver
        arg:    family_id (osid.id.Id): the ``Id`` of the family
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipNotificationSession) - a
                ``RelationshipNotificationSession``
        raise:  NotFound - no ``Family`` found by the given ``Id``
        raise:  NullArgument - ``relationship_receiver, family_id`` or
                ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_notification()``
            and ``supports_visible_federation()`` are ``true``*

        """
        pass

    def get_relationship_family_session(self, proxy=None):
        """Gets the ``OsidSession`` to lookup relationship/family mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipFamilySession) - a
                ``RelationshipFamilySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_family()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_family()``
            is ``true``.*

        """
        if not self.supports_relationship_family():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipFamilySession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_family_assignment_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with assigning relationships to families.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipFamilyAssignmentSession)
                - a ``RelationshipFamilyAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_relationship_family_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_family_assignment()``
            is ``true``.*

        """
        if not self.supports_relationship_family_assignment():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.RelationshipFamilyAssignmentSession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_smart_family_session(self, family_id=None, proxy=None):
        """Gets the ``OsidSession`` to manage dynamic families of relationships.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.RelationshipSmartFamilySession) - a
                ``RelationshipSmartFamilySession``
        raise:  NotFound - no family found by the given ``Id``
        raise:  NullArgument - ``family_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_smart_family()``
                is ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_smart_family()``
            is ``true``.*

        """
        pass

    def get_family_lookup_session(self, proxy=None, *args, **kwargs):
        """Gets the ``OsidSession`` associated with the family lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyLookupSession) - a
                ``FamilyLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_lookup()`` is ``true``.*

        """
        if not self.supports_family_lookup():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.FamilyLookupSession(proxy=proxy, runtime=self._runtime, **kwargs)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the family query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyQuerySession) - a
                ``FamilyQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_query()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_query()`` is ``true``.*

        """
        if not self.supports_family_query():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.FamilyQuerySession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the family search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilySearchSession) - a
                ``FamilySearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_search()`` is ``true``.*

        """
        if not self.supports_family_search():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.FamilySearchSession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the family administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyAdminSession) - a
                ``FamilyAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_admin()`` is ``true``.*

        """
        if not self.supports_family_admin():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.FamilyAdminSession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_notification_session(self, family_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the family notification service.

        arg:    family_receiver (osid.relationship.FamilyReceiver): the
                receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyNotificationSession) - a
                ``FamilyNotificationSession``
        raise:  NullArgument - ``family_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_notification()`` is ``true``.*

        """
        pass

    def get_family_hierarchy_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyHierarchySession) - a
                ``FamilyHierarchySession`` for families
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_hierarchy()`` is ``true``.*

        """
        if not self.supports_family_hierarchy():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.FamilyHierarchySession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_family_hierarchy_design_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.relationship.FamilyHierarchyDesignSession) - a
                ``HierarchyDesignSession`` for families
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_family_hierarchy_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if ``supports_family_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_family_hierarchy_design():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise OperationFailed()
        proxy = self._convert_proxy(proxy)
        try:
            session = sessions.FamilyHierarchyDesignSession(proxy=proxy, runtime=self._runtime)
        except AttributeError:
            raise OperationFailed()
        return session

    def get_relationship_batch_proxy_manager(self):
        """Gets the relationship batch proxy manager.

        return: (osid.relationship.batch.RelationshipBatchProxyManager)
                - a ``RelationshipBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_rules()`` is ``true``.*

        """
        pass

    def get_relationship_rules_proxy_manager(self):
        """Gets the relationship rules proxy manager.

        return: (osid.relationship.rules.RelationshipRulesProxyManager)
                - a ``RelationshipRulesProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_relationship_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if ``supports_relationship_rules()`` is ``true``.*

        """
        pass
