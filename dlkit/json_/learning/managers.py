"""JSON implementations of learning managers."""

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
from dlkit.manager_impls.learning import managers as learning_managers


class LearningProfile(osid_managers.OsidProfile, learning_managers.LearningProfile):
    """The ``LearningProfile`` describes the interoperability among learning services."""

    def supports_objective_lookup(self):
        """Tests if an objective lookup service is supported.

        An objective lookup service defines methods to access
        objectives.

        return: (boolean) - true if objective lookup is supported, false
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_lookup' in profile.SUPPORTS

    def supports_objective_query(self):
        """Tests if an objective query service is supported.

        return: (boolean) - ``true`` if objective query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_query' in profile.SUPPORTS

    def supports_objective_admin(self):
        """Tests if an objective administrative service is supported.

        return: (boolean) - ``true`` if objective admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_admin' in profile.SUPPORTS

    def supports_objective_hierarchy(self):
        """Tests if an objective hierarchy traversal is supported.

        return: (boolean) - ``true`` if an objective hierarchy traversal
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_hierarchy' in profile.SUPPORTS

    def supports_objective_hierarchy_design(self):
        """Tests if an objective hierarchy design is supported.

        return: (boolean) - ``true`` if an objective hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_hierarchy_design' in profile.SUPPORTS

    def supports_objective_sequencing(self):
        """Tests if an objective sequencing design is supported.

        return: (boolean) - ``true`` if objective sequencing is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_sequencing' in profile.SUPPORTS

    def supports_objective_objective_bank(self):
        """Tests if an objective to objective bank lookup session is available.

        return: (boolean) - ``true`` if objective objective bank lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_objective_bank' in profile.SUPPORTS

    def supports_objective_objective_bank_assignment(self):
        """Tests if an objective to objective bank assignment session is available.

        return: (boolean) - ``true`` if objective objective bank
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_objective_bank_assignment' in profile.SUPPORTS

    def supports_objective_requisite(self):
        """Tests if an objective requisite service is supported.

        return: (boolean) - ``true`` if objective requisite service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_requisite' in profile.SUPPORTS

    def supports_objective_requisite_assignment(self):
        """Tests if an objective requisite assignment service is supported.

        return: (boolean) - ``true`` if objective requisite assignment
                service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_requisite_assignment' in profile.SUPPORTS

    def supports_activity_lookup(self):
        """Tests if an activity lookup service is supported.

        return: (boolean) - ``true`` if activity lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_activity_lookup' in profile.SUPPORTS

    def supports_activity_query(self):
        """Tests if an activity query service is supported.

        return: (boolean) - ``true`` if activity query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_activity_query' in profile.SUPPORTS

    def supports_activity_admin(self):
        """Tests if an activity administrative service is supported.

        return: (boolean) - ``true`` if activity admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_activity_admin' in profile.SUPPORTS

    def supports_activity_objective_bank(self):
        """Tests if an activity to objective bank lookup session is available.

        return: (boolean) - ``true`` if activity objective bank lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_activity_objective_bank' in profile.SUPPORTS

    def supports_activity_objective_bank_assignment(self):
        """Tests if an activity to objective bank assignment session is available.

        return: (boolean) - ``true`` if activity objective bank
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_activity_objective_bank_assignment' in profile.SUPPORTS

    def supports_proficiency_lookup(self):
        """Tests if looking up proficiencies is supported.

        return: (boolean) - ``true`` if proficiency lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_proficiency_lookup' in profile.SUPPORTS

    def supports_proficiency_query(self):
        """Tests if querying proficiencies is supported.

        return: (boolean) - ``true`` if proficiency query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_proficiency_query' in profile.SUPPORTS

    def supports_proficiency_admin(self):
        """Tests if proficiencyadministrative service is supported.

        return: (boolean) - ``true`` if proficiency administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_proficiency_admin' in profile.SUPPORTS

    def supports_proficiency_objective_bank_assignment(self):
        """Tests if a proficiency objective bank mapping service is supported.

        return: (boolean) - ``true`` if proficiency to objective bank
                mapping service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_proficiency_objective_bank_assignment' in profile.SUPPORTS

    def supports_objective_bank_lookup(self):
        """Tests if an objective bank lookup service is supported.

        return: (boolean) - ``true`` if objective bank lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_bank_lookup' in profile.SUPPORTS

    def supports_objective_bank_admin(self):
        """Tests if an objective bank administrative service is supported.

        return: (boolean) - ``true`` if objective bank admin is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_bank_admin' in profile.SUPPORTS

    def supports_objective_bank_hierarchy(self):
        """Tests if an objective bank hierarchy traversal is supported.

        return: (boolean) - ``true`` if an objective bank hierarchy
                traversal is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_bank_hierarchy' in profile.SUPPORTS

    def supports_objective_bank_hierarchy_design(self):
        """Tests if objective bank hierarchy design is supported.

        return: (boolean) - ``true`` if an objective bank hierarchy
                design is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_objective_bank_hierarchy_design' in profile.SUPPORTS

    def get_objective_record_types(self):
        """Gets the supported ``Objective`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Objective`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('OBJECTIVE_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    objective_record_types = property(fget=get_objective_record_types)

    def get_objective_search_record_types(self):
        """Gets the supported ``Objective`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Objective`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('OBJECTIVE_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def get_activity_record_types(self):
        """Gets the supported ``Activity`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Activity`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('ACTIVITY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    activity_record_types = property(fget=get_activity_record_types)

    def get_activity_search_record_types(self):
        """Gets the supported ``Activity`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Activity`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('ACTIVITY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def get_proficiency_record_types(self):
        """Gets the supported ``Proficiency`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Proficiency`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('PROFICIENCY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def get_proficiency_search_record_types(self):
        """Gets the supported ``Proficiency`` search types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Proficiency`` search types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('PROFICIENCY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def get_objective_bank_record_types(self):
        """Gets the supported ``ObjectiveBank`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ObjectiveBank`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('OBJECTIVE_BANK_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def get_objective_bank_search_record_types(self):
        """Gets the supported objective bank search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ObjectiveBank`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('OBJECTIVE_BANK_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    objective_bank_search_record_types = property(fget=get_objective_bank_search_record_types)


class LearningManager(osid_managers.OsidManager, LearningProfile, learning_managers.LearningManager):
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
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveLookupSession(runtime=self._runtime)

    objective_lookup_session = property(fget=get_objective_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveLookupSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveQuerySession(runtime=self._runtime)

    objective_query_session = property(fget=get_objective_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_query_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveQuerySession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveAdminSession(runtime=self._runtime)

    objective_admin_session = property(fget=get_objective_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_admin_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveAdminSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchySession(runtime=self._runtime)

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_hierarchy():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchySession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchyDesignSession(runtime=self._runtime)

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_hierarchy_design():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchyDesignSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_sequencing():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveSequencingSession(runtime=self._runtime)

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_sequencing():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveSequencingSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_objective_bank():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveObjectiveBankSession(runtime=self._runtime)

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_objective_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveObjectiveBankAssignmentSession(runtime=self._runtime)

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_requisite():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteSession(runtime=self._runtime)

    objective_requisite_session = property(fget=get_objective_requisite_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_requisite():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_requisite_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteAssignmentSession(runtime=self._runtime)

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_objective_requisite_assignment():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteAssignmentSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_activity_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityLookupSession(runtime=self._runtime)

    activity_lookup_session = property(fget=get_activity_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_activity_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ActivityLookupSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_activity_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityQuerySession(runtime=self._runtime)

    activity_query_session = property(fget=get_activity_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_activity_query_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_activity_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ActivityQuerySession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_activity_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityAdminSession(runtime=self._runtime)

    activity_admin_session = property(fget=get_activity_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_activity_admin_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_activity_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ActivityAdminSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_activity_objective_bank():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityObjectiveBankSession(runtime=self._runtime)

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_activity_objective_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityObjectiveBankAssignmentSession(runtime=self._runtime)

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_proficiency_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyLookupSession(runtime=self._runtime)

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_proficiency_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ProficiencyLookupSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_proficiency_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyQuerySession(runtime=self._runtime)

    proficiency_query_session = property(fget=get_proficiency_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_proficiency_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ProficiencyQuerySession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_proficiency_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyAdminSession(runtime=self._runtime)

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id):
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
        if not self.supports_proficiency_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ProficiencyAdminSession(objective_bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_proficiency_objective_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyObjectiveBankAssignmentSession(runtime=self._runtime)

    proficiency_objective_bank_assignment_session = property(fget=get_proficiency_objective_bank_assignment_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_bank_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankLookupSession(runtime=self._runtime)

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_bank_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankAdminSession(runtime=self._runtime)

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_bank_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankHierarchySession(runtime=self._runtime)

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_objective_bank_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankHierarchyDesignSession(runtime=self._runtime)

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
        raise errors.Unimplemented()

    learning_batch_manager = property(fget=get_learning_batch_manager)


class LearningProxyManager(osid_managers.OsidProxyManager, LearningProfile, learning_managers.LearningProxyManager):
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
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_objective_lookup_session(self, proxy):
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
        if not self.supports_objective_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveLookupSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_query_session(self, proxy):
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
        if not self.supports_objective_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_query_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveQuerySession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_admin_session(self, proxy):
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
        if not self.supports_objective_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_admin_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveAdminSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_hierarchy_session(self, proxy):
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
        if not self.supports_objective_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_hierarchy():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchySession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_hierarchy_design_session(self, proxy):
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
        if not self.supports_objective_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_hierarchy_design():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveHierarchyDesignSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_sequencing_session(self, proxy):
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
        if not self.supports_objective_sequencing():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveSequencingSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_sequencing():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveSequencingSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_objective_bank_session(self, proxy):
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
        if not self.supports_objective_objective_bank():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveObjectiveBankSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_objective_bank_assignment_session(self, proxy):
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
        if not self.supports_objective_objective_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveObjectiveBankAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_requisite_session(self, proxy):
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
        if not self.supports_objective_requisite():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_requisite():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_objective_requisite_assignment_session(self, proxy):
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
        if not self.supports_objective_requisite_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_objective_requisite_assignment():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ObjectiveRequisiteAssignmentSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_activity_lookup_session(self, proxy):
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
        if not self.supports_activity_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_activity_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ActivityLookupSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_activity_query_session(self, proxy):
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
        if not self.supports_activity_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_activity_query_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_activity_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ActivityQuerySession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_activity_admin_session(self, proxy):
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
        if not self.supports_activity_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_activity_admin_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_activity_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ActivityAdminSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_activity_objective_bank_session(self, proxy):
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
        if not self.supports_activity_objective_bank():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityObjectiveBankSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_activity_objective_bank_assignment_session(self, proxy):
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
        if not self.supports_activity_objective_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ActivityObjectiveBankAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_lookup_session(self, proxy):
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
        if not self.supports_proficiency_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_proficiency_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ProficiencyLookupSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_query_session(self, proxy):
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
        if not self.supports_proficiency_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_proficiency_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ProficiencyQuerySession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_admin_session(self, proxy):
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
        if not self.supports_proficiency_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id, proxy):
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
        if not self.supports_proficiency_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.ProficiencyAdminSession(objective_bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_proficiency_objective_bank_assignment_session(self, proxy):
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
        if not self.supports_proficiency_objective_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProficiencyObjectiveBankAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_bank_lookup_session(self, proxy):
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
        if not self.supports_objective_bank_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_bank_admin_session(self, proxy):
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
        if not self.supports_objective_bank_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_bank_hierarchy_session(self, proxy):
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
        if not self.supports_objective_bank_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_objective_bank_hierarchy_design_session(self, proxy):
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
        if not self.supports_objective_bank_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ObjectiveBankHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    def get_learning_batch_proxy_manager(self):
        """Gets a ``LearningBatchProxyManager``.

        return: (osid.learning.batch.LearningBatchProxyManager) - a
                ``LearningBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_learning_batch() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_learning_batch()`` is true.*

        """
        raise errors.Unimplemented()

    learning_batch_proxy_manager = property(fget=get_learning_batch_proxy_manager)
