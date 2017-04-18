"""Implementations of relationship abstract base class managers."""
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


class RelationshipProfile:
    """The relationship profile describes the interoperability among relationship services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if any family federation is exposed.

        Federation is exposed when a specific family may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of families appears as a
        single family.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_lookup(self):
        """Tests if looking up relationships is supported.

        :return: ``true`` if relationship lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_query(self):
        """Tests if querying relationships is supported.

        :return: ``true`` if relationship query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_search(self):
        """Tests if searching relationships is supported.

        :return: ``true`` if relationship search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_admin(self):
        """Tests if relationship administrative service is supported.

        :return: ``true`` if relationship administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_notification(self):
        """Tests if a relationship notification service is supported.

        :return: ``true`` if relationship notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_family(self):
        """Tests if a relationship family cataloging service is supported.

        :return: ``true`` if relationship families are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_family_assignment(self):
        """Tests if a relationship cataloging service is supported.

        A relationship cataloging service maps relationships to
        families.

        :return: ``true`` if relationship families are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_smart_family(self):
        """Tests if a relationship smart family cataloging service is supported.

        :return: ``true`` if relationship smart families are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_lookup(self):
        """Tests if looking up families is supported.

        :return: ``true`` if family lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_query(self):
        """Tests if querying families is supported.

        :return: ``true`` if family query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_search(self):
        """Tests if searching families is supported.

        :return: ``true`` if family search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_admin(self):
        """Tests if familyadministrative service is supported.

        :return: ``true`` if family administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_notification(self):
        """Tests if a family notification service is supported.

        :return: ``true`` if family notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_hierarchy(self):
        """Tests for the availability of a family hierarchy traversal service.

        :return: ``true`` if family hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_family_hierarchy_design(self):
        """Tests for the availability of a family hierarchy design service.

        :return: ``true`` if family hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_batch(self):
        """Tests for the availability of a relationship batch service.

        :return: ``true`` if a relationship batch service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_relationship_rules(self):
        """Tests if a relationship rules service is supported.

        :return: ``true`` if relationship rules service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_relationship_record_types(self):
        """Gets the supported ``Relationship`` record types.

        :return: a list containing the supported ``Relationship`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    relationship_record_types = property(fget=get_relationship_record_types)

    @abc.abstractmethod
    def supports_relationship_record_type(self, relationship_record_type):
        """Tests if the given ``Relationship`` record type is supported.

        :param relationship_record_type: a ``Type`` indicating a ``Relationship`` record type
        :type relationship_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_relationship_search_record_types(self):
        """Gets the supported ``Relationship`` search record types.

        :return: a list containing the supported ``Relationship`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    @abc.abstractmethod
    def supports_relationship_search_record_type(self, relationship_search_record_type):
        """Tests if the given ``Relationship`` search record type is supported.

        :param relationship_search_record_type: a ``Type`` indicating a ``Relationship`` search record type
        :type relationship_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_family_record_types(self):
        """Gets the supported ``Family`` record types.

        :return: a list containing the supported ``Family`` types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    family_record_types = property(fget=get_family_record_types)

    @abc.abstractmethod
    def supports_family_record_type(self, family_record_type):
        """Tests if the given ``Family`` record type is supported.

        :param family_record_type: a ``Type`` indicating a ``Family`` record type
        :type family_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_family_search_record_types(self):
        """Gets the supported ``Family`` search record types.

        :return: a list containing the supported ``Family`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    family_search_record_types = property(fget=get_family_search_record_types)

    @abc.abstractmethod
    def supports_family_search_record_type(self, family_search_record_type):
        """Tests if the given ``Family`` search record type is supported.

        :param family_search_record_type: a ``Type`` indicating a ``Family`` search record type
        :type family_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``family_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class RelationshipManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipLookupSession

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    @abc.abstractmethod
    def get_relationship_lookup_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipLookupSession

    @abc.abstractmethod
    def get_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the relationship query service.

        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipQuerySession

    relationship_query_session = property(fget=get_relationship_query_session)

    @abc.abstractmethod
    def get_relationship_query_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipQuerySession

    @abc.abstractmethod
    def get_relationship_search_session(self):
        """Gets the ``OsidSession`` associated with the relationship search service.

        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_search()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipSearchSession

    relationship_search_session = property(fget=get_relationship_search_session)

    @abc.abstractmethod
    def get_relationship_search_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship search service for the given family.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipSearchSession

    @abc.abstractmethod
    def get_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipAdminSession

    relationship_admin_session = property(fget=get_relationship_admin_session)

    @abc.abstractmethod
    def get_relationship_admin_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipAdminSession

    @abc.abstractmethod
    def get_relationship_notification_session(self, relationship_receiver):
        """Gets the ``OsidSession`` associated with the relationship notification service.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``relationship_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_notification()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipNotificationSession

    @abc.abstractmethod
    def get_relationship_notification_session_for_family(self, relationship_receiver, family_id):
        """Gets the ``OsidSession`` associated with the relationship notification service for the given family.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``relationship_receiver`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipNotificationSession

    @abc.abstractmethod
    def get_relationship_family_session(self):
        """Gets the ``OsidSession`` to lookup relationship/family mappings.

        :return: a ``RelationshipFamilySession``
        :rtype: ``osid.relationship.RelationshipFamilySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_family()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipFamilySession

    relationship_family_session = property(fget=get_relationship_family_session)

    @abc.abstractmethod
    def get_relationship_family_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning relationships to families.

        :return: a ``RelationshipFamilyAssignmentSession``
        :rtype: ``osid.relationship.RelationshipFamilyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_family_assignment()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipFamilyAssignmentSession

    relationship_family_assignment_session = property(fget=get_relationship_family_assignment_session)

    @abc.abstractmethod
    def get_relationship_smart_family_session(self, family_id):
        """Gets the ``OsidSession`` to manage dynamic families of retlationships.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipSmartFamilySession``
        :rtype: ``osid.relationship.RelationshipSmartFamilySession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_smart_family()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_smart_family()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipSmartFamilySession

    @abc.abstractmethod
    def get_family_lookup_session(self):
        """Gets the ``OsidSession`` associated with the family lookup service.

        :return: a ``FamilyLookupSession``
        :rtype: ``osid.relationship.FamilyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_lookup()`` is ``true``.*

        """
        return  # osid.relationship.FamilyLookupSession

    family_lookup_session = property(fget=get_family_lookup_session)

    @abc.abstractmethod
    def get_family_query_session(self):
        """Gets the ``OsidSession`` associated with the family query service.

        :return: a ``FamilyQuerySession``
        :rtype: ``osid.relationship.FamilyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_query()`` is ``true``.*

        """
        return  # osid.relationship.FamilyQuerySession

    family_query_session = property(fget=get_family_query_session)

    @abc.abstractmethod
    def get_family_search_session(self):
        """Gets the ``OsidSession`` associated with the family search service.

        :return: a ``FamilySearchSession``
        :rtype: ``osid.relationship.FamilySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_search()`` is ``true``.*

        """
        return  # osid.relationship.FamilySearchSession

    family_search_session = property(fget=get_family_search_session)

    @abc.abstractmethod
    def get_family_admin_session(self):
        """Gets the ``OsidSession`` associated with the family administrative service.

        :return: a ``FamilyAdminSession``
        :rtype: ``osid.relationship.FamilyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_admin()`` is ``true``.*

        """
        return  # osid.relationship.FamilyAdminSession

    family_admin_session = property(fget=get_family_admin_session)

    @abc.abstractmethod
    def get_family_notification_session(self, family_receiver):
        """Gets the ``OsidSession`` associated with the family notification service.

        :param family_receiver: the receiver
        :type family_receiver: ``osid.relationship.FamilyReceiver``
        :return: a ``FamilyNotificationSession``
        :rtype: ``osid.relationship.FamilyNotificationSession``
        :raise: ``NullArgument`` -- ``family_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_notification()`` is ``true``.*

        """
        return  # osid.relationship.FamilyNotificationSession

    @abc.abstractmethod
    def get_family_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        :return: a ``FamilyHierarchySession`` for families
        :rtype: ``osid.relationship.FamilyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy()`` is ``true``.*

        """
        return  # osid.relationship.FamilyHierarchySession

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    @abc.abstractmethod
    def get_family_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        :return: a ``HierarchyDesignSession`` for families
        :rtype: ``osid.relationship.FamilyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy_design()`` is ``true``.*

        """
        return  # osid.relationship.FamilyHierarchyDesignSession

    family_hierarchy_design_session = property(fget=get_family_hierarchy_design_session)

    @abc.abstractmethod
    def get_relationship_batch_manager(self):
        """Gets the relationship batch manager.

        :return: a ``RelationshipBatchManager``
        :rtype: ``osid.relationship.batch.RelationshipBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_batch()`` is ``true``.*

        """
        return  # osid.relationship.batch.RelationshipBatchManager

    relationship_batch_manager = property(fget=get_relationship_batch_manager)

    @abc.abstractmethod
    def get_relationship_rules_manager(self):
        """Gets the relationship rules manager.

        :return: a ``RelationshipRulesManager``
        :rtype: ``osid.relationship.rules.RelationshipRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_rules()`` is ``true``.*

        """
        return  # osid.relationship.rules.RelationshipRulesManager

    relationship_rules_manager = property(fget=get_relationship_rules_manager)


class RelationshipProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_relationship_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipLookupSession

    @abc.abstractmethod
    def get_relationship_lookup_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipLookupSession

    @abc.abstractmethod
    def get_relationship_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipQuerySession

    @abc.abstractmethod
    def get_relationship_query_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipQuerySession

    @abc.abstractmethod
    def get_relationship_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_search()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipSearchSession

    @abc.abstractmethod
    def get_relationship_search_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship search service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipSearchSession

    @abc.abstractmethod
    def get_relationship_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipAdminSession

    @abc.abstractmethod
    def get_relationship_admin_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipAdminSession

    @abc.abstractmethod
    def get_relationship_notification_session(self, relationship_receiver, proxy):
        """Gets the ``OsidSession`` associated with the relationship notification service.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``relationship_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_notification()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipNotificationSession

    @abc.abstractmethod
    def get_relationship_notification_session_for_family(self, relationship_receiver, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship notification service for the given family.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``relationship_receiver, family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.relationship.RelationshipNotificationSession

    @abc.abstractmethod
    def get_relationship_family_session(self, proxy):
        """Gets the ``OsidSession`` to lookup relationship/family mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipFamilySession``
        :rtype: ``osid.relationship.RelationshipFamilySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_family()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipFamilySession

    @abc.abstractmethod
    def get_relationship_family_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning relationships to families.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipFamilyAssignmentSession``
        :rtype: ``osid.relationship.RelationshipFamilyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_family_assignment()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipFamilyAssignmentSession

    @abc.abstractmethod
    def get_relationship_smart_family_session(self, family_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic families of retlationships.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipSmartFamilySession``
        :rtype: ``osid.relationship.RelationshipSmartFamilySession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_smart_family()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_smart_family()`` is ``true``.*

        """
        return  # osid.relationship.RelationshipSmartFamilySession

    @abc.abstractmethod
    def get_family_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyLookupSession``
        :rtype: ``osid.relationship.FamilyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_lookup()`` is ``true``.*

        """
        return  # osid.relationship.FamilyLookupSession

    @abc.abstractmethod
    def get_family_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyQuerySession``
        :rtype: ``osid.relationship.FamilyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_famil_query()`` is ``true``.*

        """
        return  # osid.relationship.FamilyQuerySession

    @abc.abstractmethod
    def get_family_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilySearchSession``
        :rtype: ``osid.relationship.FamilySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_search()`` is ``true``.*

        """
        return  # osid.relationship.FamilySearchSession

    @abc.abstractmethod
    def get_family_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyAdminSession``
        :rtype: ``osid.relationship.FamilyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_admin()`` is ``true``.*

        """
        return  # osid.relationship.FamilyAdminSession

    @abc.abstractmethod
    def get_family_notification_session(self, family_receiver, proxy):
        """Gets the ``OsidSession`` associated with the family notification service.

        :param family_receiver: the receiver
        :type family_receiver: ``osid.relationship.FamilyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyNotificationSession``
        :rtype: ``osid.relationship.FamilyNotificationSession``
        :raise: ``NullArgument`` -- ``family_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_notification()`` is ``true``.*

        """
        return  # osid.relationship.FamilyNotificationSession

    @abc.abstractmethod
    def get_family_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyHierarchySession`` for families
        :rtype: ``osid.relationship.FamilyHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy()`` is ``true``.*

        """
        return  # osid.relationship.FamilyHierarchySession

    @abc.abstractmethod
    def get_family_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for families
        :rtype: ``osid.relationship.FamilyHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_family_hierarchy_design()`` is ``true``.*

        """
        return  # osid.relationship.FamilyHierarchyDesignSession

    @abc.abstractmethod
    def get_relationship_batch_proxy_manager(self):
        """Gets the relationship batch proxy manager.

        :return: a ``RelationshipBatchProxyManager``
        :rtype: ``osid.relationship.batch.RelationshipBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_rules()`` is ``true``.*

        """
        return  # osid.relationship.batch.RelationshipBatchProxyManager

    relationship_batch_proxy_manager = property(fget=get_relationship_batch_proxy_manager)

    @abc.abstractmethod
    def get_relationship_rules_proxy_manager(self):
        """Gets the relationship rules proxy manager.

        :return: a ``RelationshipRulesProxyManager``
        :rtype: ``osid.relationship.rules.RelationshipRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_relationship_rules()`` is ``true``.*

        """
        return  # osid.relationship.rules.RelationshipRulesProxyManager

    relationship_rules_proxy_manager = property(fget=get_relationship_rules_proxy_manager)
