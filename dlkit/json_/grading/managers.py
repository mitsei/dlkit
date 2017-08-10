"""JSON implementations of grading managers."""

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
from dlkit.manager_impls.grading import managers as grading_managers


class GradingProfile(osid_managers.OsidProfile, grading_managers.GradingProfile):
    """The ``GradingProfile`` describes the interoperability among grading services."""

    def supports_grade_system_lookup(self):
        """Tests if a grade system lookup service is supported.

        return: (boolean) - true if grade system lookup is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_system_lookup' in profile.SUPPORTS

    def supports_grade_system_query(self):
        """Tests if a grade system query service is supported.

        return: (boolean) - ``true`` if grade system query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_system_query' in profile.SUPPORTS

    def supports_grade_system_admin(self):
        """Tests if a grade system administrative service is supported.

        return: (boolean) - ``true`` if grade system admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_system_admin' in profile.SUPPORTS

    def supports_grade_system_gradebook(self):
        """Tests if a grade system to gradebook lookup session is available.

        return: (boolean) - ``true`` if grade system gradebook lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_system_gradebook' in profile.SUPPORTS

    def supports_grade_system_gradebook_assignment(self):
        """Tests if a grade system to gradebook assignment session is available.

        return: (boolean) - ``true`` if grade system gradebook
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_system_gradebook_assignment' in profile.SUPPORTS

    def supports_grade_entry_lookup(self):
        """Tests if a grade entry lookup service is supported.

        return: (boolean) - true if grade entry lookup is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_entry_lookup' in profile.SUPPORTS

    def supports_grade_entry_query(self):
        """Tests if a grade entry query service is supported.

        return: (boolean) - true if grade entry query is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_entry_query' in profile.SUPPORTS

    def supports_grade_entry_admin(self):
        """Tests if a grade entry administrative service is supported.

        return: (boolean) - ``true`` if grade entry admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_grade_entry_admin' in profile.SUPPORTS

    def supports_gradebook_column_lookup(self):
        """Tests if a gradebook column lookup service is supported.

        return: (boolean) - true if gradebook column lookup is
                supported, false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_column_lookup' in profile.SUPPORTS

    def supports_gradebook_column_query(self):
        """Tests if a gradebook column query service is supported.

        return: (boolean) - ``true`` if grade system query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_column_query' in profile.SUPPORTS

    def supports_gradebook_column_admin(self):
        """Tests if a gradebook column administrative service is supported.

        return: (boolean) - ``true`` if gradebook column admin is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_column_admin' in profile.SUPPORTS

    def supports_gradebook_column_gradebook(self):
        """Tests if a gradebook column to gradebook lookup session is available.

        return: (boolean) - ``true`` if gradebook column gradebook
                lookup session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_column_gradebook' in profile.SUPPORTS

    def supports_gradebook_column_gradebook_assignment(self):
        """Tests if a gradebook column to gradebook assignment session is available.

        return: (boolean) - ``true`` if gradebook column gradebook
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_column_gradebook_assignment' in profile.SUPPORTS

    def supports_gradebook_lookup(self):
        """Tests if a gradebook lookup service is supported.

        return: (boolean) - ``true`` if gradebook lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_lookup' in profile.SUPPORTS

    def supports_gradebook_admin(self):
        """Tests if a gradebook administrative service is supported.

        return: (boolean) - ``true`` if gradebook admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_admin' in profile.SUPPORTS

    def supports_gradebook_hierarchy(self):
        """Tests if a gradebook hierarchy traversal is supported.

        return: (boolean) - ``true`` if a gradebook hierarchy traversal
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_hierarchy' in profile.SUPPORTS

    def supports_gradebook_hierarchy_design(self):
        """Tests if gradebook hierarchy design is supported.

        return: (boolean) - ``true`` if a gradebook hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_gradebook_hierarchy_design' in profile.SUPPORTS

    def get_grade_record_types(self):
        """Gets the supported ``Grade`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Grade`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADE_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    grade_record_types = property(fget=get_grade_record_types)

    def get_grade_system_record_types(self):
        """Gets the supported ``GradeSystem`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeSystem`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADE_SYSTEM_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    grade_system_record_types = property(fget=get_grade_system_record_types)

    def get_grade_system_search_record_types(self):
        """Gets the supported ``GradeSystem`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeSystem`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADE_SYSTEM_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    def get_grade_entry_record_types(self):
        """Gets the supported ``GradeEntry`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeEntry`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADE_ENTRY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    def get_grade_entry_search_record_types(self):
        """Gets the supported ``GradeEntry`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeEntry`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADE_ENTRY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    def get_gradebook_column_record_types(self):
        """Gets the supported ``GradebookColumn`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradebookColumn`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADEBOOK_COLUMN_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    def get_gradebook_column_search_record_types(self):
        """Gets the supported gradebook column search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradebookColumn`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADEBOOK_COLUMN_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    def get_gradebook_column_summary_record_types(self):
        """Gets the supported ``GradebookColumnSummary`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradebookColumnSummary`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADEBOOK_COLUMN_SUMMARY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    def get_gradebook_record_types(self):
        """Gets the supported ``Gradebook`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Gradebook`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADEBOOK_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    gradebook_record_types = property(fget=get_gradebook_record_types)

    def get_gradebook_search_record_types(self):
        """Gets the supported gradebook search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Gradebook`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('GRADEBOOK_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)


class GradingManager(osid_managers.OsidManager, GradingProfile, grading_managers.GradingManager):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``GradeSystemLookupSession:`` a session to look up grades and
        grade systems
      * ``GradeSystemQuerySession:`` a session to query grade systems
        ``None``
      * ``GradeSystemSearchSession:`` a session to search grade systems
      * ``GradeSystemAdminSession:`` a session to manage grade systems
      * ``GradeSystemNotificationSession`` a session for subscribing to
        new or deleted grades or grade systems
      * ``GradeSystemGradebookSession:`` a session for retrieving grade
        system to gradebook mappings
      * ``GradeSystemGradebookAssignmentSession:`` a session for
        managing grade system to gradebook mappings
      * ``GradeSystemSmartGradebookSession:`` a session for managing
        smart gradebooks of grade systems

      * ``GradeEntryLookupSession:`` a session to look up grade entries
      * ``GradeEntryQuerySession:`` a session to query grade entries
        ``None``
      * ``GradeEntrySearchSession:`` a session to search grade entries
      * ``GradeEntryAdminSession:`` a session to create, modify and
        delete grade entries ``None``
      * ``GradeEntryNotificationSession: a`` session to receive messages
        pertaining to grade entry ```` changes

      * ``GradebookColumnLookupSession:`` a session to look up gradebook
        columns
      * ``GradebookColumnQuerySession:`` a session to query gradebook
        columns ``None``
      * ``GradebookColumnSearchSession:`` a session to search gradebook
        columns
      * ``GradebookColumnAdminSession:`` a session to manage gradebook
        columns
      * ``GradebookColumnNotificationSession`` a session for subscribing
        to new or deleted gradebook columns
      * ``GradebookColumnGradebookSession:`` a session for retrieving
        gradebook column to gradebook mappings
      * ``GradebookColumnGradebookAssignmentSession:`` a session for
        managing gradebook column to gradebook mappings
      * ``GradebookColumnSmartGradebookSession:`` a session for managing
        smart gradebooks of gradebook columns

      * ``GradebookLookupSession:`` a session to lookup gradebooks
      * ``GradebookQuerySession:`` a session to query gradebooks
      * ``GradebookSearchSession`` : a session to search gradebooks
      * ``GradebookAdminSession`` : a session to create, modify and
        delete gradebooks
      * ``GradebookNotificationSession`` : a session to receive messages
        pertaining to gradebook changes
      * ``GradebookHierarchySession:`` a session to traverse the
        gradebook hierarchy
      * ``GradebookHierarchyDesignSession:`` a session to manage the
        gradebook hierarchy

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_grade_system_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        return: (osid.grading.GradeSystemLookupSession) - a
                ``GradeSystemLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        if not self.supports_grade_system_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemLookupSession(runtime=self._runtime)

    grade_system_lookup_session = property(fget=get_grade_system_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemLookupSession) - ``a
                GradeSystemLookupSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_system_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeSystemLookupSession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_grade_system_query_session(self):
        """Gets the ``OsidSession`` associated with the grade system query service.

        return: (osid.grading.GradeSystemQuerySession) - a
                ``GradeSystemQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        if not self.supports_grade_system_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemQuerySession(runtime=self._runtime)

    grade_system_query_session = property(fget=get_grade_system_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_grade_system_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemQuerySession) - ``a
                GradeSystemQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_system_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeSystemQuerySession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_grade_system_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        return: (osid.grading.GradeSystemAdminSession) - a
                ``GradeSystemAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        if not self.supports_grade_system_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemAdminSession(runtime=self._runtime)

    grade_system_admin_session = property(fget=get_grade_system_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_grade_system_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemAdminSession) - ``a
                GradeSystemAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_system_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeSystemAdminSession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_grade_system_gradebook_session(self):
        """Gets the session for retrieving grade system to gradebook mappings.

        return: (osid.grading.GradeSystemGradebookSession) - a
                ``GradeSystemGradebookSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_gradebook()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        if not self.supports_grade_system_gradebook():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemGradebookSession(runtime=self._runtime)

    grade_system_gradebook_session = property(fget=get_grade_system_gradebook_session)

    @utilities.remove_null_proxy_kwarg
    def get_grade_system_gradebook_assignment_session(self):
        """Gets the session for assigning grade system to gradebook mappings.

        return: (osid.grading.GradeSystemGradebookSession) - a
                ``GradeSystemGradebookAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_grade_system_gradebook_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        if not self.supports_grade_system_gradebook_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemGradebookAssignmentSession(runtime=self._runtime)

    grade_system_gradebook_assignment_session = property(fget=get_grade_system_gradebook_assignment_session)

    @utilities.remove_null_proxy_kwarg
    def get_grade_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        return: (osid.grading.GradeEntryLookupSession) - a
                ``GradeEntryLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        if not self.supports_grade_entry_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeEntryLookupSession(runtime=self._runtime)

    grade_entry_lookup_session = property(fget=get_grade_entry_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryLookupSession) - ``a
                GradeEntryLookupSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_entry_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeEntryLookupSession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_grade_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        return: (osid.grading.GradeEntryQuerySession) - a
                ``GradeEntryQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        if not self.supports_grade_entry_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeEntryQuerySession(runtime=self._runtime)

    grade_entry_query_session = property(fget=get_grade_entry_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_grade_entry_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryQuerySession) - ``a
                GradeEntryQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_entry_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeEntryQuerySession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_grade_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        return: (osid.grading.GradeEntryAdminSession) - a
                ``GradeEntryAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        if not self.supports_grade_entry_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeEntryAdminSession(runtime=self._runtime)

    grade_entry_admin_session = property(fget=get_grade_entry_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryAdminSession) - ``a
                GradeEntryAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_entry_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeEntryAdminSession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_column_lookup_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        return: (osid.grading.GradebookColumnLookupSession) - a
                ``GradebookColumnLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_lookup()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        if not self.supports_gradebook_column_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnLookupSession(runtime=self._runtime)

    gradebook_column_lookup_session = property(fget=get_gradebook_column_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnLookupSession) - ``a
                _gradebook_column_lookup_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_lookup()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_gradebook_column_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradebookColumnLookupSession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_column_query_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        return: (osid.grading.GradebookColumnQuerySession) - a
                ``GradebookColumnQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        if not self.supports_gradebook_column_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnQuerySession(runtime=self._runtime)

    gradebook_column_query_session = property(fget=get_gradebook_column_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnQuerySession) - ``a
                GradebookColumnQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_gradebook_column_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradebookColumnQuerySession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_column_admin_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        return: (osid.grading.GradebookColumnAdminSession) - a
                ``GradebookColumnAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        if not self.supports_gradebook_column_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnAdminSession(runtime=self._runtime)

    gradebook_column_admin_session = property(fget=get_gradebook_column_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnAdminSession) - ``a
                GradebookColumnAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_gradebook_column_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradebookColumnAdminSession(gradebook_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_column_gradebook_session(self):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        return: (osid.grading.GradebookColumnGradebookSession) - a
                ``GradebookColumnGradebookSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_gradebook()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        if not self.supports_gradebook_column_gradebook():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnGradebookSession(runtime=self._runtime)

    gradebook_column_gradebook_session = property(fget=get_gradebook_column_gradebook_session)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_column_gradebook_assignment_session(self):
        """Gets the session for assigning gradebook column to gradebook mappings.

        return: (osid.grading.GradebookColumnGradebookAssignmentSession)
                - a ``GradebookColumnGradebookAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_gradebook_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        if not self.supports_gradebook_column_gradebook_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnGradebookAssignmentSession(runtime=self._runtime)

    gradebook_column_gradebook_assignment_session = property(fget=get_gradebook_column_gradebook_assignment_session)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_lookup_session(self):
        """Gets the OsidSession associated with the gradebook lookup service.

        return: (osid.grading.GradebookLookupSession) - a
                ``GradebookLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_lookup() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        if not self.supports_gradebook_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookLookupSession(runtime=self._runtime)

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_admin_session(self):
        """Gets the OsidSession associated with the gradebook administration service.

        return: (osid.grading.GradebookAdminSession) - a
                ``GradebookAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_admin() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        if not self.supports_gradebook_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookAdminSession(runtime=self._runtime)

    gradebook_admin_session = property(fget=get_gradebook_admin_session)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_hierarchy_session(self):
        """Gets the session traversing gradebook hierarchies.

        return: (osid.grading.GradebookHierarchySession) - a
                ``GradebookHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_hierarchy() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        if not self.supports_gradebook_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookHierarchySession(runtime=self._runtime)

    gradebook_hierarchy_session = property(fget=get_gradebook_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
    def get_gradebook_hierarchy_design_session(self):
        """Gets the session designing gradebook hierarchies.

        return: (osid.grading.GradebookHierarchyDesignSession) - a
                ``GradebookHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_hierarchy_design()
                is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        if not self.supports_gradebook_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookHierarchyDesignSession(runtime=self._runtime)

    gradebook_hierarchy_design_session = property(fget=get_gradebook_hierarchy_design_session)

    def get_grading_batch_manager(self):
        """Gets the ``GradingBatchManager``.

        return: (osid.grading.batch.GradingBatchManager) - a
                ``GradingBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_batch() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        raise errors.Unimplemented()

    grading_batch_manager = property(fget=get_grading_batch_manager)

    def get_grading_calculation_manager(self):
        """Gets the ``GradingCalculationManager``.

        return: (osid.grading.calculation.GradingCalculationManager) - a
                ``GradingCalculationManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_calculation() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        raise errors.Unimplemented()

    grading_calculation_manager = property(fget=get_grading_calculation_manager)

    def get_grading_transform_manager(self):
        """Gets the ``GradingTransformManager``.

        return: (osid.grading.transform.GradingTransformManager) - a
                ``GradingTransformManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_transform() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        raise errors.Unimplemented()

    grading_transform_manager = property(fget=get_grading_transform_manager)


class GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile, grading_managers.GradingProxyManager):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from server environments.The sessions included in this manager are:

      * ``GradeSystemLookupSession:`` a session to look up grades and
        grade systems
      * ``GradeSystemQuerySession:`` a session to query grade systems
        ``None``
      * ``GradeSystemSearchSession:`` a session to search grade systems
      * ``GradeSystemAdminSession:`` a session to manage grade systems
      * ``GradeSystemNotificationSession`` a session for subscribing to
        new or deleted grades or grade systems
      * ``GradeSystemGradebookSession:`` a session for retrieving grade
        system to gradebook mappings
      * ``GradeSystemGradebookAssignmentSession:`` a session for
        managing grade system to gradebook mappings
      * ``GradeSystemSmartGradebookSession:`` a session for managing
        smart gradebooks of grade systems

      * ``GradeEntryLookupSession:`` a session to look up grade entries
      * ``GradeEntryQuerySession:`` a session to query grade entries
        ``None``
      * ``GradeEntrySearchSession:`` a session to search grade entries
      * ``GradeEntryAdminSession:`` a session to create, modify and
        delete grade entries ``None``
      * ``GradeEntryNotificationSession: a`` session to receive messages
        pertaining to grade entry ```` changes

      * ``GradebookColumnLookupSession:`` a session to look up gradebook
        columns
      * ``GradebookColumnQuerySession:`` a session to query gradebook
        columns ``None``
      * ``GradebookColumnSearchSession:`` a session to search gradebook
        columns
      * ``GradebookColumnAdminSession:`` a session to manage gradebook
        columns
      * ``GradebookColumnDerivationSession:`` a session to manage
        derived gradebook columns
      * ``GradebookColumnNotificationSession`` a session for subscribing
        to new or deleted gradebook columns
      * ``GradebookColumnGradebookSession:`` a session for retrieving
        gradebook column to gradebook mappings
      * ``GradebookColumnGradebookAssignmentSession:`` a session for
        managing gradebook column to gradebook mappings
      * ``GradebookColumnSmartGradebookSession:`` a session for managing
        smart gradebooks of gradebook columns

      * ``GradebookLookupSession:`` a session to lookup gradebooks
      * ``GradebookQuerySession:`` a session to query gradebooks
      * ``GradebookSearchSession`` : a session to search gradebooks
      * ``GradebookAdminSession`` : a session to create, modify and
        delete gradebooks
      * ``GradebookNotificationSession`` : a session to receive messages
        pertaining to gradebook changes
      * ``GradebookHierarchySession:`` a session to traverse the
        gradebook hierarchy
      * ``GradebookHierarchyDesignSession:`` a session to manage the
        gradebook hierarchy

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_grade_system_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemLookupSession) - a
                ``GradeSystemLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        if not self.supports_grade_system_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemLookupSession) - ``a
                GradeSystemLookupSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_system_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeSystemLookupSession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemQuerySession) - a
                ``GradeSystemQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        if not self.supports_grade_system_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemQuerySession) - ``a
                GradeSystemQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_system_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeSystemQuerySession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemAdminSession) - a
                ``GradeSystemAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        if not self.supports_grade_system_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemAdminSession) - ``a
                GradeSystemAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_system_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeSystemAdminSession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_gradebook_session(self, proxy):
        """Gets the session for retrieving grade system to gradebook mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemGradebookSession) - a
                ``GradeSystemGradebookSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_gradebook()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        if not self.supports_grade_system_gradebook():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemGradebookSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_system_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning grade system to gradebook mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeSystemGradebookSession) - a
                ``GradeSystemGradebookAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_grade_system_gradebook_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        if not self.supports_grade_system_gradebook_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeSystemGradebookAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeEntryLookupSession) - a
                ``GradeEntryLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        if not self.supports_grade_entry_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeEntryLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeEntryLookupSession) - ``a
                GradeEntryLookupSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_entry_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeEntryLookupSession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_grade_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeEntryQuerySession) - a
                ``GradeEntryQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        if not self.supports_grade_entry_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeEntryQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entry_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeEntryQuerySession) - ``a
                GradeEntryQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_entry_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeEntryQuerySession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_grade_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeEntryAdminSession) - a
                ``GradeEntryAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        if not self.supports_grade_entry_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradeEntryAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradeEntryAdminSession) - ``a
                GradeEntryAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_grade_entry_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradeEntryAdminSession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnLookupSession) - a
                ``GradebookColumnLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_lookup()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        if not self.supports_gradebook_column_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnLookupSession) - ``a
                _gradebook_column_lookup_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_lookup()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_gradebook_column_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradebookColumnLookupSession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnQuerySession) - a
                ``GradebookColumnQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        if not self.supports_gradebook_column_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnQuerySession) - a
                ``GradebookColumnQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_gradebook_column_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradebookColumnQuerySession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnAdminSession) - a
                ``GradebookColumnAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        if not self.supports_gradebook_column_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnAdminSession) - ``a
                GradebookColumnAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_gradebook_column_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.GradebookColumnAdminSession(gradebook_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_gradebook_session(self, proxy):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnGradebookSession) - a
                ``GradebookColumnGradebookSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_gradebook()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        if not self.supports_gradebook_column_gradebook():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnGradebookSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_column_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning gradebook column to gradebook mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookColumnGradebookAssignmentSession)
                - a ``GradebookColumnGradebookAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_gradebook_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        if not self.supports_gradebook_column_gradebook_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookColumnGradebookAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_lookup_session(self, proxy):
        """Gets the OsidSession associated with the gradebook lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookLookupSession) - a
                ``GradebookLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_lookup() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        if not self.supports_gradebook_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_admin_session(self, proxy):
        """Gets the OsidSession associated with the gradebook administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookAdminSession) - a
                ``GradebookAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_admin() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        if not self.supports_gradebook_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_hierarchy_session(self, proxy):
        """Gets the session traversing gradebook hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookHierarchySession) - a
                ``GradebookHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_hierarchy() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        if not self.supports_gradebook_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_gradebook_hierarchy_design_session(self, proxy):
        """Gets the session designing gradebook hierarchies.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.grading.GradebookHierarchyDesignSession) - a
                ``GradebookHierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_hierarchy_design()
                is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        if not self.supports_gradebook_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.GradebookHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    def get_grading_batch_proxy_manager(self):
        """Gets the ``GradingBatchProxyManager``.

        return: (osid.grading.batch.GradingBatchProxyManager) - a
                ``GradingBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_batch() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        raise errors.Unimplemented()

    grading_batch_proxy_manager = property(fget=get_grading_batch_proxy_manager)

    def get_grading_calculation_proxy_manager(self):
        """Gets the ``GradingCalculationProxyManager``.

        return:
                (osid.grading.calculation.GradingCalculationProxyManager
                ) - a ``GradingCalculationProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_calculation() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        raise errors.Unimplemented()

    grading_calculation_proxy_manager = property(fget=get_grading_calculation_proxy_manager)

    def get_grading_transform_proxy_manager(self):
        """Gets the ``GradingTransformProxyManager``.

        return: (osid.grading.transform.GradingTransformProxyManager) -
                a ``GradingTransformManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_transform() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        raise errors.Unimplemented()

    grading_transform_proxy_manager = property(fget=get_grading_transform_proxy_manager)
