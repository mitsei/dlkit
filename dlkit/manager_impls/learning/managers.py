"""Manager utility implementations of learning managers."""
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
from dlkit.abstract_osid.learning import managers as abc_learning_managers


class LearningProfile(abc_learning_managers.LearningProfile, osid_managers.OsidProfile):
    """The ``LearningProfile`` describes the interoperability among learning services."""

    def supports_visible_federation(self):
        """Tests if federation is visible.

        return: (boolean) - ``true`` if visible federation is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_lookup(self):
        """Tests if an objective lookup service is supported.

        An objective lookup service defines methods to access
        objectives.

        return: (boolean) - true if objective lookup is supported, false
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_query(self):
        """Tests if an objective query service is supported.

        return: (boolean) - ``true`` if objective query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_search(self):
        """Tests if an objective search service is supported.

        return: (boolean) - ``true`` if objective search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_admin(self):
        """Tests if an objective administrative service is supported.

        return: (boolean) - ``true`` if objective admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_notification(self):
        """Tests if objective notification is supported.

        Messages may be sent when objectives are created, modified, or
        deleted.

        return: (boolean) - ``true`` if objective notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_hierarchy(self):
        """Tests if an objective hierarchy traversal is supported.

        return: (boolean) - ``true`` if an objective hierarchy traversal
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_hierarchy_design(self):
        """Tests if an objective hierarchy design is supported.

        return: (boolean) - ``true`` if an objective hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_sequencing(self):
        """Tests if an objective sequencing design is supported.

        return: (boolean) - ``true`` if objective sequencing is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_objective_bank(self):
        """Tests if an objective to objective bank lookup session is available.

        return: (boolean) - ``true`` if objective objective bank lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_objective_bank_assignment(self):
        """Tests if an objective to objective bank assignment session is available.

        return: (boolean) - ``true`` if objective objective bank
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_smart_objective_bank(self):
        """Tests if an objective smart objective bank cataloging service is supported.

        return: (boolean) - ``true`` if objective smart objective banks
                are supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_requisite(self):
        """Tests if an objective requisite service is supported.

        return: (boolean) - ``true`` if objective requisite service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_requisite_assignment(self):
        """Tests if an objective requisite assignment service is supported.

        return: (boolean) - ``true`` if objective requisite assignment
                service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_lookup(self):
        """Tests if an activity lookup service is supported.

        return: (boolean) - ``true`` if activity lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_query(self):
        """Tests if an activity query service is supported.

        return: (boolean) - ``true`` if activity query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_search(self):
        """Tests if an activity search service is supported.

        return: (boolean) - ``true`` if activity search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_admin(self):
        """Tests if an activity administrative service is supported.

        return: (boolean) - ``true`` if activity admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_notification(self):
        """Tests if activity notification is supported.

        Messages may be sent when activities are created, modified, or
        deleted.

        return: (boolean) - ``true`` if activity notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_objective_bank(self):
        """Tests if an activity to objective bank lookup session is available.

        return: (boolean) - ``true`` if activity objective bank lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_objective_bank_assignment(self):
        """Tests if an activity to objective bank assignment session is available.

        return: (boolean) - ``true`` if activity objective bank
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_activity_smart_objective_bank(self):
        """Tests if an activity smart objective bank cataloging service is supported.

        return: (boolean) - ``true`` if activity smart objective banks
                are supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_lookup(self):
        """Tests if looking up proficiencies is supported.

        return: (boolean) - ``true`` if proficiency lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_query(self):
        """Tests if querying proficiencies is supported.

        return: (boolean) - ``true`` if proficiency query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_search(self):
        """Tests if searching proficiencies is supported.

        return: (boolean) - ``true`` if proficiency search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_admin(self):
        """Tests if proficiencyadministrative service is supported.

        return: (boolean) - ``true`` if proficiency administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_notification(self):
        """Tests if a proficiencynotification service is supported.

        return: (boolean) - ``true`` if proficiency notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_objective_bank(self):
        """Tests if a proficiency objective bank mapping lookup service is supported.

        return: (boolean) - ``true`` if a proficiency objective bank
                lookup service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_objective_bank_assignment(self):
        """Tests if a proficiency objective bank mapping service is supported.

        return: (boolean) - ``true`` if proficiency to objective bank
                mapping service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_proficiency_smart_objective_bank(self):
        """Tests if a proficiency smart objective bank cataloging service is supported.

        return: (boolean) - ``true`` if proficiency smart objective
                banks are supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_my_learning_path(self):
        """Tests if a learning path service is supported for the authenticated agent.

        return: (boolean) - ``true`` if learning path is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_learning_path(self):
        """Tests if a learning path service is supported.

        return: (boolean) - ``true`` if learning path is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_lookup(self):
        """Tests if an objective bank lookup service is supported.

        return: (boolean) - ``true`` if objective bank lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_query(self):
        """Tests if an objective bank query service is supported.

        return: (boolean) - ``true`` if objective bank query is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_search(self):
        """Tests if an objective bank search service is supported.

        return: (boolean) - ``true`` if objective bank search is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_admin(self):
        """Tests if an objective bank administrative service is supported.

        return: (boolean) - ``true`` if objective bank admin is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_notification(self):
        """Tests if objective bank notification is supported.

        Messages may be sent when objective banks are created, modified,
        or deleted.

        return: (boolean) - ``true`` if objective bank notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_hierarchy(self):
        """Tests if an objective bank hierarchy traversal is supported.

        return: (boolean) - ``true`` if an objective bank hierarchy
                traversal is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_objective_bank_hierarchy_design(self):
        """Tests if objective bank hierarchy design is supported.

        return: (boolean) - ``true`` if an objective bank hierarchy
                design is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_learning_batch(self):
        """Tests if a learning batch service is supported.

        return: (boolean) - ``true`` if a learning batch service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_objective_record_types(self):
        """Gets the supported ``Objective`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Objective`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    objective_record_types = property(fget=get_objective_record_types)

    def supports_objective_record_type(self, objective_record_type=None):
        """Tests if the given ``Objective`` record type is supported.

        arg:    objective_record_type (osid.type.Type): a ``Type``
                indicating an ``Objective`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``objective_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if objective_record_type is None:
            raise NullArgument()
        return False

    def get_objective_search_record_types(self):
        """Gets the supported ``Objective`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Objective`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def supports_objective_search_record_type(self, objective_search_record_type=None):
        """Tests if the given ``Objective`` search record type is supported.

        arg:    objective_search_record_type (osid.type.Type): a
                ``Type`` indicating an ``Objective`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``objective_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if objective_search_record_type is None:
            raise NullArgument()
        return False

    def get_activity_record_types(self):
        """Gets the supported ``Activity`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Activity`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    activity_record_types = property(fget=get_activity_record_types)

    def supports_activity_record_type(self, activity_record_type=None):
        """Tests if the given ``Activity`` record type is supported.

        arg:    activity_record_type (osid.type.Type): a ``Type``
                indicating a ``Activity`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``activity_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if activity_record_type is None:
            raise NullArgument()
        return False

    def get_activity_search_record_types(self):
        """Gets the supported ``Activity`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Activity`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def supports_activity_search_record_type(self, activity_search_record_type=None):
        """Tests if the given ``Activity`` search record type is supported.

        arg:    activity_search_record_type (osid.type.Type): a ``Type``
                indicating a ``Activity`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``activity_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if activity_search_record_type is None:
            raise NullArgument()
        return False

    def get_proficiency_record_types(self):
        """Gets the supported ``Proficiency`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Proficiency`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def supports_proficiency_record_type(self, proficiency_record_type=None):
        """Tests if the given ``Proficiency`` record type is supported.

        arg:    proficiency_record_type (osid.type.Type): a ``Type``
                indicating a ``Proficiency`` record type
        return: (boolean) - ``true`` if the given record type is
                supported, ``false`` otherwise
        raise:  NullArgument - ``proficiency_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if proficiency_record_type is None:
            raise NullArgument()
        return False

    def get_proficiency_search_record_types(self):
        """Gets the supported ``Proficiency`` search types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Proficiency`` search types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def supports_proficiency_search_record_type(self, proficiency_search_record_type=None):
        """Tests if the given ``Proficiency`` search type is supported.

        arg:    proficiency_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``Proficiency`` search type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``proficiency_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if proficiency_search_record_type is None:
            raise NullArgument()
        return False

    def get_objective_bank_record_types(self):
        """Gets the supported ``ObjectiveBank`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ObjectiveBank`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def supports_objective_bank_record_type(self, objective_bank_record_type=None):
        """Tests if the given ``ObjectiveBank`` record type is supported.

        arg:    objective_bank_record_type (osid.type.Type): a ``Type``
                indicating an ``ObjectiveBank`` type
        return: (boolean) - ``true`` if the given objective bank record
                ``Type`` is supported, ``false`` otherwise
        raise:  NullArgument - ``objective_bank_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if objective_bank_record_type is None:
            raise NullArgument()
        return False

    def get_objective_bank_search_record_types(self):
        """Gets the supported objective bank search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ObjectiveBank`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    objective_bank_search_record_types = property(fget=get_objective_bank_search_record_types)

    def supports_objective_bank_search_record_type(self, objective_bank_search_record_type=None):
        """Tests if the given objective bank search record type is supported.

        arg:    objective_bank_search_record_type (osid.type.Type): a
                ``Type`` indicating an ``ObjectiveBank`` search record
                type
        return: (boolean) - ``true`` if the given search record ``Type``
                is supported, ``false`` otherwise
        raise:  NullArgument - ``objective_bank_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if objective_bank_search_record_type is None:
            raise NullArgument()
        return False


class LearningManager(abc_learning_managers.LearningManager, osid_managers.OsidManager, LearningProfile):
    """The learning manager provides access to learning sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ObjectiveLookupSession:`` a session to look up objectives
      * ``ObjectiveLookupSession:`` a session to query objectives
        ``None``
      * ``ObjectiveSearchSession:`` a session to search objectives
      * ``ObjectiveAdminSession:`` a session to create, modify and
        delete objectives ``None``
      * ``ObjectiveNotificationSession: a`` session to receive messages
        pertaining to objective ```` changes
      * ``ObjectiveHierarchySession:`` a session to traverse objective
        hierarchies
      * ``ObjectiveHierarchyDesignSession:`` a session to design
        objective hierarchies
      * ``ObjectiveSequencingSession:`` a session to sequence objectives
      * ``ObjectiveObjectiveBankSession:`` a session for retriieving
        objective and objective bank mappings
      * ``ObjectiveObjectiveBankAssignmentSession:`` a session for
        managing objective and objective bank mappings
      * ``ObjectiveSmartObjectiveBankSession:`` a session for managing
        dynamic objective banks
      * ``ObjectiveRequisiteSession:`` a session to examine objective
        requisites
      * ``ObjectiveRequisiteAssignmentSession:`` a session to manage
        objective requisites

      * ``ActivityLookupSession:`` a session to look up activities
      * ``ActivityQuerySession:`` a session to query activities ``None``
      * ``ActivitySearchSession:`` a session to search activities
      * ``ActivityAdminSession:`` a session to create, modify and delete
        activities ``None``
      * ``ActivityNotificationSession: a`` session to receive messages
        pertaining to activity ```` changes
      * ``ActivityObjectiveBankSession:`` a session for retriieving
        activity and objective bank mappings
      * ``ActivityObjectiveBankAssignmentSession:`` a session for
        managing activity and objective bank mappings
      * ``ActivitySmartObjectiveBankSession:`` a session for managing
        dynamic objective banks of activities

      * ``ProficiencyLookupSession:`` a session to retrieve
        proficiencies
      * ``ProficiencyQuerySession:`` a session to query proficiencies
      * ``ProficiencySearchSession:`` a session to search for
        proficiencies
      * ``ProficiencyAdminSession:`` a session to create, update, and
        delete proficiencies
      * ``ProficiencyNotificationSession:`` a session to receive
        notifications pertaining to proficiency changes
      * ``ProficiencyObjectiveBankSession:`` a session to look up
        proficiency to objective bank mappings
      * ``ProficiencyObjectiveBankAssignmentSession:`` a session to
        manage proficiency to objective bank mappings
      * ``ProficiencySmartObjectiveBankSession:`` a session to manage
        smart objective banks of proficiencies
      * ``MyLearningPathSession:`` a session to examine learning paths
        of objectives
      * ``LearningPathSession:`` a session to examine learning paths of
        objectives

      * ``ObjectiveBankLookupSession:`` a session to lookup objective
        banks
      * ``ObjectiveBankQuerySession:`` a session to query objective
        banks
      * ``ObjectiveBankSearchSession`` : a session to search objective
        banks
      * ``ObjectiveBankAdminSession`` : a session to create, modify and
        delete objective banks
      * ``ObjectiveBankNotificationSession`` : a session to receive
        messages pertaining to objective bank changes
      * ``ObjectiveBankHierarchySession:`` a session to traverse the
        objective bank hierarchy
      * ``ObjectiveBankHierarchyDesignSession:`` a session to manage the
        objective bank hierarchy

    """

    def get_objective_lookup_session(self):
        """Gets the ``OsidSession`` associated with the objective lookup service.

        return: (osid.learning.ObjectiveLookupSession) - an
                ``ObjectiveLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    objective_lookup_session = property(fget=get_objective_lookup_session)

    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective lookup service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveLookupSession) - ``an
                _objective_lookup_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_query_session(self):
        """Gets the ``OsidSession`` associated with the objective query service.

        return: (osid.learning.ObjectiveQuerySession) - an
                ``ObjectiveQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        raise Unimplemented()

    objective_query_session = property(fget=get_objective_query_session)

    def get_objective_query_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective query service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveQuerySession) - ``an
                _objective_query_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_search_session(self):
        """Gets the ``OsidSession`` associated with the objective search service.

        return: (osid.learning.ObjectiveSearchSession) - an
                ``ObjectiveSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` is ``true``.*

        """
        raise Unimplemented()

    objective_search_session = property(fget=get_objective_search_session)

    def get_objective_search_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective search service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveSearchSession) - ``an
                _objective_search_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_admin_session(self):
        """Gets the ``OsidSession`` associated with the objective administration service.

        return: (osid.learning.ObjectiveAdminSession) - an
                ``ObjectiveAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` is ``true``.*

        """
        raise Unimplemented()

    objective_admin_session = property(fget=get_objective_admin_session)

    def get_objective_admin_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective admin service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveAdminSession) - ``an
                _objective_admin_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_notification_session(self, objective_receiver=None):
        """Gets the notification session for notifications pertaining to objective changes.

        arg:    objective_receiver (osid.learning.ObjectiveReceiver):
                the objective receiver
        return: (osid.learning.ObjectiveNotificationSession) - an
                ``ObjectiveNotificationSession``
        raise:  NullArgument - ``objective_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_objective_notification_session_for_objective_bank(self, objective_receiver=None, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective notification service for the given objective bank.

        arg:    objective_receiver (osid.learning.ObjectiveReceiver):
                the objective receiver
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveNotificationSession) - ``an
                _objective_notification_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_receiver`` or
                ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_receiver is None:
            raise NullArgument
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_hierarchy_session(self):
        """Gets the session for traversing objective hierarchies.

        return: (osid.learning.ObjectiveHierarchySession) - an
                ``ObjectiveHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` is ``true``.*

        """
        raise Unimplemented()

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective hierarchy traversal service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveHierarchySession) - an
                ``ObjectiveHierarchySession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_hierarchy()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_hierarchy_design_session(self):
        """Gets the session for designing objective hierarchies.

        return: (osid.learning.ObjectiveHierarchyDesignSession) - an
                ``ObjectiveHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_hierarchy_design()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` is ``true``.*

        """
        raise Unimplemented()

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective hierarchy design service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveHierarchyDesignSession) - an
                ``ObjectiveHierarchyDesignSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_objective_hierarchy_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_sequencing_session(self):
        """Gets the session for sequencing objectives.

        return: (osid.learning.ObjectiveSequencingSession) - an
                ``ObjectiveSequencingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_sequencing()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` is ``true``.*

        """
        raise Unimplemented()

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveSequencingSession) - an
                ``ObjectiveSequencingSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_sequencing()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_objective_bank_session(self):
        """Gets the session for retrieving objective to objective bank mappings.

        return: (osid.learning.ObjectiveObjectiveBankSession) - an
                ``ObjectiveObjectiveBankSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_objective_bank()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank()`` is ``true``.*

        """
        raise Unimplemented()

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    def get_objective_objective_bank_assignment_session(self):
        """Gets the session for assigning objective to objective bank mappings.

        return: (osid.learning.ObjectiveObjectiveBankAssignmentSession)
                - an ``ObjectiveObjectiveBankAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_objective_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    def get_objective_smart_objective_bank_session(self, objective_bank_id=None):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ObjectiveSmartObjectiveBankSession) - an
                ``ObjectiveSmartObjectiveBankSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_smart_objective_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_smart_objective_bank()`` is ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_requisite_session(self):
        """Gets the session for examining objective requisites.

        return: (osid.learning.ObjectiveRequisiteSession) - an
                ``ObjectiveRequisiteSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_requisite()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` is ``true``.*

        """
        raise Unimplemented()

    objective_requisite_session = property(fget=get_objective_requisite_session)

    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveRequisiteSession) - an
                ``ObjectiveRequisiteSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_requisite()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_requisite_assignment_session(self):
        """Gets the session for managing objective requisites.

        return: (osid.learning.ObjectiveRequisiteAssignmentSession) - an
                ``ObjectiveRequisiteAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_requisite_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ObjectiveRequisiteAssignmentSession) - an
                ``ObjectiveRequisiteAssignmentSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_objective_requisite_assignment()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_lookup_session(self):
        """Gets the ``OsidSession`` associated with the activity lookup service.

        return: (osid.learning.ActivityLookupSession) - an
                ``ActivityLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    activity_lookup_session = property(fget=get_activity_lookup_session)

    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the activity lookup service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ActivityLookupSession) - an
                ``ActivityLookupSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_query_session(self):
        """Gets the ``OsidSession`` associated with the activity query service.

        return: (osid.learning.ActivityQuerySession) - a
                ``ActivityQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` is ``true``.*

        """
        raise Unimplemented()

    activity_query_session = property(fget=get_activity_query_session)

    def get_activity_query_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the activity query service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ActivityQuerySession) - an
                ``ActivityQuerySession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_search_session(self):
        """Gets the ``OsidSession`` associated with the activity search service.

        return: (osid.learning.ActivitySearchSession) - a
                ``ActivitySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` is ``true``.*

        """
        raise Unimplemented()

    activity_search_session = property(fget=get_activity_search_session)

    def get_activity_search_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the activity search service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ActivitySearchSession) - an
                ``ActivitySearchSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_admin_session(self):
        """Gets the ``OsidSession`` associated with the activity administration service.

        return: (osid.learning.ActivityAdminSession) - a
                ``ActivityAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` is ``true``.*

        """
        raise Unimplemented()

    activity_admin_session = property(fget=get_activity_admin_session)

    def get_activity_admin_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the activity admin service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ActivityAdminSession) - an
                ``ActivityAdminSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_notification_session(self, activity_receiver=None):
        """Gets the notification session for notifications pertaining to activity changes.

        arg:    activity_receiver (osid.learning.ActivityReceiver): the
                activity receiver
        return: (osid.learning.ActivityNotificationSession) - an
                ``ActivityNotificationSession``
        raise:  NullArgument - ``activity_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_activity_notification_session_for_objective_bank(self, activity_receiver=None, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the activity notification service for the given objective bank.

        arg:    activity_receiver (osid.learning.ActivityReceiver): the
                activity receiver
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        return: (osid.learning.ActivityNotificationSession) - ``an
                _activity_notification_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``activity_receiver`` or
                ``objective_bank_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if activity_receiver is None:
            raise NullArgument
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_objective_bank_session(self):
        """Gets the session for retrieving activity to objective bank mappings.

        return: (osid.learning.ActivityObjectiveBankSession) - an
                ``ActivityObjectiveBankSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_objective_bank()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank()`` is ``true``.*

        """
        raise Unimplemented()

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    def get_activity_objective_bank_assignment_session(self):
        """Gets the session for assigning activity to objective bank mappings.

        return: (osid.learning.ActivityObjectiveBankAssignmentSession) -
                an ``ActivityObjectiveBankAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_activity_objective_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    def get_activity_smart_objective_bank_session(self, objective_bank_id=None):
        """Gets the ``OsidSession`` to manage dynamic objective banks of activities.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ActivitySmartObjectiveBankSession) - an
                ``ActivitySmartObjectiveBankSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_activity_smart_objective_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_smart_objective_bank()`` is ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_lookup_session(self):
        """Gets the ``OsidSession`` associated with the proficiency lookup service.

        return: (osid.learning.ProficiencyLookupSession) - a
                ``ProficiencyLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the proficiency lookup service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                obective bank
        return: (osid.learning.ProficiencyLookupSession) - a
                ``ProficiencyLookupSession``
        raise:  NotFound - no ``ObjectiveBank`` found by the given
                ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_query_session(self):
        """Gets the ``OsidSession`` associated with the proficiency query service.

        return: (osid.learning.ProficiencyQuerySession) - a
                ``ProficiencyQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` is ``true``.*

        """
        raise Unimplemented()

    proficiency_query_session = property(fget=get_proficiency_query_session)

    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the proficiency query service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                obective bank
        return: (osid.learning.ProficiencyQuerySession) - a
                ``ProficiencyQuerySession``
        raise:  NotFound - no ``ObjectiveBank`` found by the given
                ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_search_session(self):
        """Gets the ``OsidSession`` associated with the proficiency search service.

        return: (osid.learning.ProficiencySearchSession) - a
                ``ProficiencySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` is ``true``.*

        """
        raise Unimplemented()

    proficiency_search_session = property(fget=get_proficiency_search_session)

    def get_proficiency_search_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the proficiency search service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ProficiencySearchSession) - a
                ``ProficiencySearchSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_admin_session(self):
        """Gets the ``OsidSession`` associated with the proficiency administration service.

        return: (osid.learning.ProficiencyAdminSession) - a
                ``ProficiencyAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` is ``true``.*

        """
        raise Unimplemented()

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the proficiency administration service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ProficiencyAdminSession) - a
                ``ProficiencyAdminSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_notification_session(self, proficiency_receiver=None):
        """Gets the ``OsidSession`` associated with the proficiency notification service.

        arg:    proficiency_receiver
                (osid.learning.ProficiencyReceiver): the notification
                callback
        return: (osid.learning.ProficiencyNotificationSession) - a
                ``ProficiencyNotificationSession``
        raise:  NullArgument - ``proficiency_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_proficiency_notification_session_for_objective_bank(self, proficiency_receiver=None, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the proficiency notification service for the given objective bank.

        arg:    proficiency_receiver
                (osid.learning.ProficiencyReceiver): the notification
                callback
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ProficiencyNotificationSession) - a
                ``ProficiencyNotificationSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``proficiency_receiver`` or
                ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if proficiency_receiver is None:
            raise NullArgument
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_objective_bank_session(self):
        """Gets the ``OsidSession`` to lookup proficiency/objective bank mappings.

        return: (osid.learning.ProficiencyObjectiveBankSession) - a
                ``ProficiencyObjectiveBankSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_proficiency_objective_bank()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank()`` is ``true``.*

        """
        raise Unimplemented()

    proficiency_objective_bank_session = property(fget=get_proficiency_objective_bank_session)

    def get_proficiency_objective_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning proficiencys to objective banks.

        return:
                (osid.learning.ProficiencyObjectiveBankAssignmentSession
                ) - a ``ProficiencyObjectiveBankAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_proficiency_objective_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank_assignment()`` is
        ``true``.*

        """
        raise Unimplemented()

    proficiency_objective_bank_assignment_session = property(fget=get_proficiency_objective_bank_assignment_session)

    def get_proficiency_smart_objective_bank_session(self, objective_bank_id=None):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ProficiencySmartObjectiveBankSession) - a
                ``ProficiencySmartObjectiveBankSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_proficiency_smart_objective_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_smart_objective_bank()`` is ``true``.*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_my_learning_path_session(self):
        """Gets the ``OsidSession`` associated with the my learning path service.

        return: (osid.learning.MyLearningPathSession) - a
                ``MyLearningPathSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_my_learning_path()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` is ``true``.*

        """
        raise Unimplemented()

    my_learning_path_session = property(fget=get_my_learning_path_session)

    def get_my_learning_path_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the my learning path service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.MyLearningPathSession) - a
                ``MyLearningPathSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_my_learning_path()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_learning_path_session(self):
        """Gets the ``OsidSession`` associated with the learning path service.

        return: (osid.learning.LearningPathSession) - a
                ``LearningPathSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_learning_path()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` is ``true``.*

        """
        raise Unimplemented()

    learning_path_session = property(fget=get_learning_path_session)

    def get_learning_path_session_for_objective_bank(self, objective_bank_id=None):
        """Gets the ``OsidSession`` associated with the learning path service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.LearningPathSession) - a
                ``LearningPathSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supporty_learning_path()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_bank_lookup_session(self):
        """Gets the OsidSession associated with the objective bank lookup service.

        return: (osid.learning.ObjectiveBankLookupSession) - an
                ``ObjectiveBankLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_lookup() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_lookup()`` is true.*

        """
        raise Unimplemented()

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    def get_objective_bank_query_session(self):
        """Gets the OsidSession associated with the objective bank query service.

        return: (osid.learning.ObjectiveBankQuerySession) - an
                ``ObjectiveBankQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_query() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is true.*

        """
        raise Unimplemented()

    objective_bank_query_session = property(fget=get_objective_bank_query_session)

    def get_objective_bank_search_session(self):
        """Gets the OsidSession associated with the objective bank search service.

        return: (osid.learning.ObjectiveBankSearchSession) - an
                ``ObjectiveBankSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_search() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_search()`` is true.*

        """
        raise Unimplemented()

    objective_bank_search_session = property(fget=get_objective_bank_search_session)

    def get_objective_bank_admin_session(self):
        """Gets the OsidSession associated with the objective bank administration service.

        return: (osid.learning.ObjectiveBankAdminSession) - an
                ``ObjectiveBankAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_admin() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_admin()`` is true.*

        """
        raise Unimplemented()

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    def get_objective_bank_notification_session(self, objective_bank_receiver=None):
        """Gets the notification session for notifications pertaining to objective bank service changes.

        arg:    objective_bank_receiver
                (osid.learning.ObjectiveBankReceiver): the objective
                bank receiver
        return: (osid.learning.ObjectiveBankNotificationSession) - an
                ``ObjectiveBankNotificationSession``
        raise:  NullArgument - ``objective_bank_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_notification()
                is false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_notification()`` is true.*

        """
        raise Unimplemented()

    def get_objective_bank_hierarchy_session(self):
        """Gets the session traversing objective bank hierarchies.

        return: (osid.learning.ObjectiveBankHierarchySession) - an
                ``ObjectiveBankHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_hierarchy() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy()`` is true.*

        """
        raise Unimplemented()

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    def get_objective_bank_hierarchy_design_session(self):
        """Gets the session designing objective bank hierarchies.

        return: (osid.learning.ObjectiveBankHierarchyDesignSession) - an
                ``ObjectiveBankHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_bank_hierarchy_design() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy_design()`` is true.*

        """
        raise Unimplemented()

    objective_bank_hierarchy_design_session = property(fget=get_objective_bank_hierarchy_design_session)

    def get_learning_batch_manager(self):
        """Gets a ``LearningBatchManager``.

        return: (osid.learning.batch.LearningBatchManager) - a
                ``LearningBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_learning_batch() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_batch()`` is true.*

        """
        raise Unimplemented()

    learning_batch_manager = property(fget=get_learning_batch_manager)


class LearningProxyManager(abc_learning_managers.LearningProxyManager, osid_managers.OsidProxyManager, LearningProfile):
    """The learning manager provides access to learning sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ObjectiveLookupSession:`` a session to look up objectives
      * ``ObjectiveLookupSession:`` a session to query objectives
        ``None``
      * ``ObjectiveSearchSession:`` a session to search objectives
      * ``ObjectiveAdminSession:`` a session to create, modify and
        delete objectives ``None``
      * ``ObjectiveNotificationSession: a`` session to receive messages
        pertaining to objective ```` changes
      * ``ObjectiveHierarchySession:`` a session to traverse objective
        hierarchies
      * ``ObjectiveHierarchyDesignSession:`` a session to design
        objective hierarchies
      * ``ObjectiveSequencingSession:`` a session to sequence objectives
      * ``ObjectiveObjectiveBankSession:`` a session for retriieving
        objective and objective bank mappings
      * ``ObjectiveObjectiveBankAssignmentSession:`` a session for
        managing objective and objective bank mappings
      * ``ObjectiveSmartObjectiveBankSession:`` a session for managing
        dynamic objective banks
      * ``ObjectiveRequisiteSession:`` a session to examine objective
        requisites
      * ``ObjectiveRequisiteAssignmentSession:`` a session to manage
        objective requisites

      * ``ActivityLookupSession:`` a session to look up activities
      * ``ActivityQuerySession:`` a session to query activities ``None``
      * ``ActivitySearchSession:`` a session to search activities
      * ``ActivityAdminSession:`` a session to create, modify and delete
        activities ``None``
      * ``ActivityNotificationSession: a`` session to receive messages
        pertaining to activity ```` changes
      * ``ActivityObjectiveBankSession:`` a session for retriieving
        activity and objective bank mappings
      * ``ActivityObjectiveBankAssignmentSession:`` a session for
        managing activity and objective bank mappings
      * ``ActivitySmartObjectiveBankSession:`` a session for managing
        dynamic objective banks of activities

      * ``ProficiencyLookupSession:`` a session to retrieve
        proficiencies
      * ``ProficiencyQuerySession:`` a session to query proficiencies
      * ``ProficiencySearchSession:`` a session to search for
        proficiencies
      * ``ProficiencyAdminSession:`` a session to create, update, and
        delete proficiencies
      * ``ProficiencyNotificationSession:`` a session to receive
        notifications pertaining to proficiency changes
      * ``ProficiencyObjectiveBankSession:`` a session to look up
        proficiency to objective bank mappings
      * ``ProficiencyObjectiveBankAssignmentSession:`` a session to
        manage proficiency to objective bank mappings
      * ``ProficiencySmartObjectiveBankSession:`` a session to manage
        smart objective banks of proficiencies
      * ``MyLearningPathSession:`` a session to examine learning paths
        of objectives
      * ``LearningPathSession:`` a session to examine learning paths of
        objectives

      * ``ObjectiveBankLookupSession:`` a session to lookup objective
        banks
      * ``ObjectiveBankQuerySession:`` a session to query objective
        banks
      * ``ObjectiveBankSearchSession`` : a session to search objective
        banks
      * ``ObjectiveBankAdminSession`` : a session to create, modify and
        delete objective banks
      * ``ObjectiveBankNotificationSession`` : a session to receive
        messages pertaining to objective bank changes
      * ``ObjectiveBankHierarchySession:`` a session to traverse the
        objective bank hierarchy
      * ``ObjectiveBankHierarchyDesignSession:`` a session to manage the
        objective bank hierarchy

    """

    def get_objective_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the objective lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveLookupSession) - an
                ``ObjectiveLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective lookup service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveLookupSession) - ``an
                _objective_lookup_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the objective query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveQuerySession) - an
                ``ObjectiveQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_query_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective query service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveQuerySession) - ``an
                _objective_query_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the objective search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveSearchSession) - an
                ``ObjectiveSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_search_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective search service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveSearchSession) - ``an
                _objective_search_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the objective administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveAdminSession) - an
                ``ObjectiveAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_admin_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective admin service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveAdminSession) - ``an
                _objective_admin_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_notification_session(self, objective_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to objective changes.

        arg:    objective_receiver (osid.learning.ObjectiveReceiver):
                the objective receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveNotificationSession) - an
                ``ObjectiveNotificationSession``
        raise:  NullArgument - ``objective_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_notification_session_for_objective_bank(self, objective_receiver=None, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective notification service for the given objective bank.

        arg:    objective_receiver (osid.learning.ObjectiveReceiver):
                the objective receiver
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveNotificationSession) - ``an
                _objective_notification_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_receiver, objective_bank_id``
                or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_hierarchy_session(self, proxy=None):
        """Gets the session for traversing objective hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveHierarchySession) - an
                ``ObjectiveHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective hierarchy traversal service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveHierarchySession) - an
                ``ObjectiveHierarchySession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_hierarchy()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_hierarchy_design_session(self, proxy=None):
        """Gets the session for designing objective hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveHierarchyDesignSession) - an
                ``ObjectiveHierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_hierarchy_design()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective hierarchy design service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveHierarchyDesignSession) - an
                ``ObjectiveHierarchyDesignSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_objective_hierarchy_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_sequencing_session(self, proxy=None):
        """Gets the session for sequencing objectives.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveSequencingSession) - an
                ``ObjectiveSequencingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_sequencing()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveSequencingSession) - an
                ``ObjectiveSequencingSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_sequencing()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_objective_bank_session(self, proxy=None):
        """Gets the session for retrieving objective to objective bank mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveObjectiveBankSession) - an
                ``ObjectiveObjectiveBankSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_objective_bank()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_objective_bank_assignment_session(self, proxy=None):
        """Gets the session for assigning objective to objective bank mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveObjectiveBankAssignmentSession)
                - an ``ObjectiveObjectiveBankAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_objective_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_smart_objective_bank_session(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivitySmartObjectiveBankSession) - an
                ``ObjectiveSmartObjectiveBankSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_smart_objective_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_smart_objective_bank()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_requisite_session(self, proxy=None):
        """Gets the session for examining objective requisites.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveRequisiteSession) - an
                ``ObjectiveRequisiteSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_requisite()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveRequisiteSession) - an
                ``ObjectiveRequisiteSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_objective_requisite()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_requisite_assignment_session(self, proxy=None):
        """Gets the session for managing objective requisites.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveRequisiteAssignmentSession) - an
                ``ObjectiveRequisiteAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_requisite_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveRequisiteAssignmentSession) - an
                ``ObjectiveRequisiteAssignmentSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_objective_requisite_assignment()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the activity lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityLookupSession) - an
                ``ActivityLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the activity lookup service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityLookupSession) - an
                ``ActivityLookupSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the activity query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityQuerySession) - an
                ``ActivityQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_query_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the activity query service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityQuerySession) - an
                ``ActivityQuerySession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the activity search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivitySearchSession) - an
                ``ActivitySearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_search_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the activity search service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivitySearchSession) - an
                ``ActivitySearchSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the activity administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityAdminSession) - an
                ``ActivityAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_admin_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the activity admin service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityAdminSession) - a
                ``ActivityAdminSession``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_notification_session(self, activity_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to activity changes.

        arg:    activity_receiver (osid.learning.ActivityReceiver): the
                activity receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityNotificationSession) - an
                ``ActivityNotificationSession``
        raise:  NullArgument - ``activity_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_notification_session_for_objective_bank(self, activity_receiver=None, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the activity notification service for the given objective bank.

        arg:    activity_receiver (osid.learning.ActivityReceiver): the
                activity receiver
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                objective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityNotificationSession) - ``an
                _activity_notification_session``
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``activity_receiver, objective_bank_id``
                or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_activity_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if activity_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_activity_objective_bank_session(self, proxy=None):
        """Gets the session for retrieving activity to objective bank mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityObjectiveBankSession) - an
                ``ActivityObjectiveBankSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_activity_objective_bank()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_objective_bank_assignment_session(self, proxy=None):
        """Gets the session for assigning activity to objective bank mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivityObjectiveBankAssignmentSession) -
                an ``ActivityObjectiveBankAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_activity_objective_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_activity_smart_objective_bank_session(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` to manage dynamic objective banks of activities.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ActivitySmartObjectiveBankSession) - an
                ``ActivitySmartObjectiveBankSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_activity_smart_objective_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_activity_smart_objective_bank()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyLookupSession) - a
                ``ProficiencyLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency lookup service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                obective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyLookupSession) - a
                ``ProficiencyLookupSession``
        raise:  NotFound - no ``ObjectiveBank`` found by the given
                ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyQuerySession) - a
                ``ProficiencyQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency query service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                obective bank
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyQuerySession) - a
                ``ProficiencyQuerySession``
        raise:  NotFound - no ``ObjectiveBank`` found by the given
                ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencySearchSession) - a
                ``ProficiencySearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_search_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency search service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencySearchSession) - a
                ``ProficiencySearchSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyAdminSession) - a
                ``ProficiencyAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency administration service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyAdminSession) - a
                ``ProficiencyAdminSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_notification_session(self, proficiency_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency notification service.

        arg:    proficiency_receiver
                (osid.learning.ProficiencyReceiver): the notification
                callback
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyNotificationSession) - a
                ``ProficiencyNotificationSession``
        raise:  NullArgument - ``proficiency_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_notification_session_for_objective_bank(self, proficiency_receiver=None, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the proficiency notification service for the given objective bank.

        arg:    proficiency_receiver
                (osid.learning.ProficiencyReceiver): the notification
                callback
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyNotificationSession) - a
                ``ProficiencyNotificationSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``proficiency_receiver,
                objective_bank_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proficiency_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if proficiency_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_proficiency_objective_bank_session(self, proxy=None):
        """Gets the ``OsidSession`` to lookup proficiency/objective bank mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencyObjectiveBankSession) - a
                ``ProficiencyObjectiveBankSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_proficiency_objective_bank()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_objective_bank_assignment_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with assigning proficiencies to objective banks.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return:
                (osid.learning.ProficiencyObjectiveBankAssignmentSession
                ) - a ``ProficiencyObjectiveBankAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_proficiency_objective_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank_assignment()`` is
        ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_proficiency_smart_objective_bank_session(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` to manage dynamic objective banks of proficiencies.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ProficiencySmartObjectiveBankSession) - a
                ``ProficiencySmartObjectiveBankSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_proficiency_smart_objective_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_smart_objective_bank()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_my_learning_path_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the my learning path service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.MyLearningPathSession) - a
                ``MyLearningPathSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_my_learning_path()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_my_learning_path_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the my learning path service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.MyLearningPathSession) - a
                ``MyLearningPathSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_my_learning_path()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_learning_path_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the learning path service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.LearningPathSession) - a
                ``LearningPathSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_learning_path()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_learning_path_session_for_objective_bank(self, objective_bank_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the learning path service for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.LearningPathSession) - a
                ``LearningPathSession``
        raise:  NotFound - no objective bank found by the given ``Id``
        raise:  NullArgument - ``objective_bank_id`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supporty_learning_path()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if objective_bank_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_objective_bank_lookup_session(self, proxy=None):
        """Gets the OsidSession associated with the objective bank lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankLookupSession) - an
                ``ObjectiveBankLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_lookup() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_lookup()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_bank_query_session(self, proxy=None):
        """Gets the OsidSession associated with the objective bank query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankQuerySession) - an
                ``ObjectiveBankQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_query() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_bank_search_session(self, proxy=None):
        """Gets the OsidSession associated with the objective bank search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankSearchSession) - an
                ``ObjectiveBankSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_search() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_search()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_bank_admin_session(self, proxy=None):
        """Gets the OsidSession associated with the objective bank administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankAdminSession) - an
                ``ObjectiveBankAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_admin() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_admin()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_bank_notification_session(self, objective_bank_receiver=None, proxy=None):
        """Gets the notification session for notifications pertaining to objective bank service changes.

        arg:    objective_bank_receiver
                (osid.learning.ObjectiveBankReceiver): the objective
                bank receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankNotificationSession) - an
                ``ObjectiveBankNotificationSession``
        raise:  NullArgument - ``objective_bank_receiver`` or ``proxy``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_notification()
                is false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_notification()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_bank_hierarchy_session(self, proxy=None):
        """Gets the session traversing objective bank hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankHierarchySession) - an
                ``ObjectiveBankHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_objective_bank_hierarchy() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_objective_bank_hierarchy_design_session(self, proxy=None):
        """Gets the session designing objective bank hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.learning.ObjectiveBankHierarchyDesignSession) - an
                ``ObjectiveBankHierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_objective_bank_hierarchy_design() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy_design()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_learning_batch_proxy_manager(self):
        """Gets a ``LearningBatchProxyManager``.

        return: (osid.learning.batch.LearningBatchProxyManager) - a
                ``LearningBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_learning_batch() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_batch()`` is true.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    learning_batch_proxy_manager = property(fget=get_learning_batch_proxy_manager)
