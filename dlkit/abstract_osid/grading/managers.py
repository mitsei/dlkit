"""Implementations of grading abstract base class managers."""
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


class GradingProfile:
    """The ``GradingProfile`` describes the interoperability among grading services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_lookup(self):
        """Tests if a grade system lookup service is supported.

        :return: true if grade system lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_query(self):
        """Tests if a grade system query service is supported.

        :return: ``true`` if grade system query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_search(self):
        """Tests if a grade system search service is supported.

        :return: ``true`` if grade system search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_admin(self):
        """Tests if a grade system administrative service is supported.

        :return: ``true`` if grade system admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_notification(self):
        """Tests if grade system notification is supported.

        Messages may be sent when grade entries are created, modified,
        or deleted.

        :return: ``true`` if grade system notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_gradebook(self):
        """Tests if a grade system to gradebook lookup session is available.

        :return: ``true`` if grade system gradebook lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_gradebook_assignment(self):
        """Tests if a grade system to gradebook assignment session is available.

        :return: ``true`` if grade system gradebook assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_system_smart_gradebook(self):
        """Tests if a grade system smart gradebook session is available.

        :return: ``true`` if grade system smart gradebook is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_entry_lookup(self):
        """Tests if a grade entry lookup service is supported.

        :return: true if grade entry lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_entry_query(self):
        """Tests if a grade entry query service is supported.

        :return: true if grade entry query is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_entry_search(self):
        """Tests if a grade entry search service is supported.

        :return: ``true`` if grade entry search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_entry_admin(self):
        """Tests if a grade entry administrative service is supported.

        :return: ``true`` if grade entry admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grade_entry_notification(self):
        """Tests if grade entry notification is supported.

        :return: ``true`` if grade entry notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_lookup(self):
        """Tests if a gradebook column lookup service is supported.

        :return: true if gradebook column lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_query(self):
        """Tests if a gradebook column query service is supported.

        :return: ``true`` if grade system query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_search(self):
        """Tests if a gradebook column search service is supported.

        :return: ``true`` if grade system search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_admin(self):
        """Tests if a gradebook column administrative service is supported.

        :return: ``true`` if gradebook column admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_notification(self):
        """Tests if gradebook column notification is supported.

        Messages may be sent when grade entries are created, modified,
        or deleted.

        :return: ``true`` if gradebook column notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_gradebook(self):
        """Tests if a gradebook column to gradebook lookup session is available.

        :return: ``true`` if gradebook column gradebook lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_gradebook_assignment(self):
        """Tests if a gradebook column to gradebook assignment session is available.

        :return: ``true`` if gradebook column gradebook assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_column_smart_gradebook(self):
        """Tests if a gradebook column smart gradebookt session is available.

        :return: ``true`` if gradebook column amsrt gradebook is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_lookup(self):
        """Tests if a gradebook lookup service is supported.

        :return: ``true`` if gradebook lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_query(self):
        """Tests if a gradebook query service is supported.

        :return: ``true`` if gradebook query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_search(self):
        """Tests if a gradebook search service is supported.

        :return: ``true`` if gradebook search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_admin(self):
        """Tests if a gradebook administrative service is supported.

        :return: ``true`` if gradebook admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_notification(self):
        """Tests if gradebook notification is supported.

        Messages may be sent when gradebooks are created, modified, or
        deleted.

        :return: ``true`` if gradebook notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_hierarchy(self):
        """Tests if a gradebook hierarchy traversal is supported.

        :return: ``true`` if a gradebook hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_gradebook_hierarchy_design(self):
        """Tests if gradebook hierarchy design is supported.

        :return: ``true`` if a gradebook hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grading_batch(self):
        """Tests if a grading batch service is supported.

        :return: ``true`` if a grading batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grading_calculation(self):
        """Tests if a grading calculation service is supported.

        :return: ``true`` if a grading calculation service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_grading_transform(self):
        """Tests if a grade system transform service is supported.

        :return: ``true`` if a grading transform service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_record_types(self):
        """Gets the supported ``Grade`` record types.

        :return: a list containing the supported ``Grade`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    grade_record_types = property(fget=get_grade_record_types)

    @abc.abstractmethod
    def supports_grade_record_type(self, grade_record_type):
        """Tests if the given ``Grade`` record type is supported.

        :param grade_record_type: a ``Type`` indicating a ``Grade`` record type
        :type grade_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_record_types(self):
        """Gets the supported ``GradeSystem`` record types.

        :return: a list containing the supported ``GradeSystem`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    grade_system_record_types = property(fget=get_grade_system_record_types)

    @abc.abstractmethod
    def supports_grade_system_record_type(self, grade_system_record_type):
        """Tests if the given ``GradeSystem`` record type is supported.

        :param grade_system_record_type: a ``Type`` indicating a ``GradeSystem`` record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_search_record_types(self):
        """Gets the supported ``GradeSystem`` search record types.

        :return: a list containing the supported ``GradeSystem`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    @abc.abstractmethod
    def supports_grade_system_search_record_type(self, grade_system_search_record_type):
        """Tests if the given ``GradeSystem`` search record type is supported.

        :param grade_system_search_record_type: a ``Type`` indicating a ``GradeSystem`` search record type
        :type grade_system_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_entry_record_types(self):
        """Gets the supported ``GradeEntry`` record types.

        :return: a list containing the supported ``GradeEntry`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    @abc.abstractmethod
    def supports_grade_entry_record_type(self, grade_entry_record_type):
        """Tests if the given ``GradeEntry`` record type is supported.

        :param grade_entry_record_type: a ``Type`` indicating a ``GradeEntry`` record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_entry_search_record_types(self):
        """Gets the supported ``GradeEntry`` search record types.

        :return: a list containing the supported ``GradeEntry`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    @abc.abstractmethod
    def supports_grade_entry_search_record_type(self, grade_entry_search_record_type):
        """Tests if the given ``GradeEntry`` search record type is supported.

        :param grade_entry_search_record_type: a ``Type`` indicating a ``GradeEntry`` search record type
        :type grade_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_record_types(self):
        """Gets the supported ``GradebookColumn`` record types.

        :return: a list containing the supported ``GradebookColumn`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    @abc.abstractmethod
    def supports_gradebook_column_record_type(self, gradebook_column_record_type):
        """Tests if the given ``GradebookColumn`` record type is supported.

        :param gradebook_column_record_type: a ``Type`` indicating a ``GradebookColumn`` type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook column record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_search_record_types(self):
        """Gets the supported gradebook column search record types.

        :return: a list containing the supported ``GradebookColumn`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    @abc.abstractmethod
    def supports_gradebook_column_search_record_type(self, gradebook_column_search_record_type):
        """Tests if the given gradebook column search record type is supported.

        :param gradebook_column_search_record_type: a ``Type`` indicating a ``GradebookColumn`` search record type
        :type gradebook_column_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_summary_record_types(self):
        """Gets the supported ``GradebookColumnSummary`` record types.

        :return: a list containing the supported ``GradebookColumnSummary`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    @abc.abstractmethod
    def supports_gradebook_column_summary_record_type(self, gradebook_column_summary_record_type):
        """Tests if the given ``GradebookColumnSummary`` record type is supported.

        :param gradebook_column_summary_record_type: a ``Type`` indicating a ``GradebookColumnSummary`` type
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook column summary record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_record_types(self):
        """Gets the supported ``Gradebook`` record types.

        :return: a list containing the supported ``Gradebook`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    gradebook_record_types = property(fget=get_gradebook_record_types)

    @abc.abstractmethod
    def supports_gradebook_record_type(self, gradebook_record_type):
        """Tests if the given ``Gradebook`` record type is supported.

        :param gradebook_record_type: a ``Type`` indicating a ``Gradebook`` type
        :type gradebook_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_search_record_types(self):
        """Gets the supported gradebook search record types.

        :return: a list containing the supported ``Gradebook`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)

    @abc.abstractmethod
    def supports_gradebook_search_record_type(self, gradebook_search_record_type):
        """Tests if the given gradebook search record type is supported.

        :param gradebook_search_record_type: a ``Type`` indicating a ``Gradebook`` search record type
        :type gradebook_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class GradingManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        :return: a ``GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemLookupSession

    grade_system_lookup_session = property(fget=get_grade_system_lookup_session)

    @abc.abstractmethod
    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemLookupSession

    @abc.abstractmethod
    def get_grade_system_query_session(self):
        """Gets the ``OsidSession`` associated with the grade system query service.

        :return: a ``GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuerySession

    grade_system_query_session = property(fget=get_grade_system_query_session)

    @abc.abstractmethod
    def get_grade_system_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemQuerySession

    @abc.abstractmethod
    def get_grade_system_search_session(self):
        """Gets the ``OsidSession`` associated with the grade system search service.

        :return: a ``GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchSession

    grade_system_search_session = property(fget=get_grade_system_search_session)

    @abc.abstractmethod
    def get_grade_system_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemSearchSession

    @abc.abstractmethod
    def get_grade_system_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        :return: a ``GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemAdminSession

    grade_system_admin_session = property(fget=get_grade_system_admin_session)

    @abc.abstractmethod
    def get_grade_system_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemAdminSession

    @abc.abstractmethod
    def get_grade_system_notification_session(self, grade_system_receiver):
        """Gets the notification session for notifications pertaining to grade system changes.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :return: a ``GradeSystemNotificationSession``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NullArgument`` -- ``grade_system_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemNotificationSession

    @abc.abstractmethod
    def get_grade_system_notification_session_for_gradebook(self, grade_system_receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system notification service for the given gradebook.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _grade_system_notification_session``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_receiver`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemNotificationSession

    @abc.abstractmethod
    def get_grade_system_gradebook_session(self):
        """Gets the session for retrieving grade system to gradebook mappings.

        :return: a ``GradeSystemGradebookSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemGradebookSession

    grade_system_gradebook_session = property(fget=get_grade_system_gradebook_session)

    @abc.abstractmethod
    def get_grade_system_gradebook_assignment_session(self):
        """Gets the session for assigning grade system to gradebook mappings.

        :return: a ``GradeSystemGradebookAssignmentSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemGradebookSession

    grade_system_gradebook_assignment_session = property(fget=get_grade_system_gradebook_assignment_session)

    @abc.abstractmethod
    def get_grade_system_smart_gradebook_session(self, gradebook_id):
        """Gets the session for managing smart gradebooks of grade systems.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: a ``GradeSystemSmartGradebookSession``
        :rtype: ``osid.grading.GradeSystemSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_smart_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_smart_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSmartGradebookSession

    @abc.abstractmethod
    def get_grade_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        :return: a ``GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryLookupSession

    grade_entry_lookup_session = property(fget=get_grade_entry_lookup_session)

    @abc.abstractmethod
    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryLookupSession

    @abc.abstractmethod
    def get_grade_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        :return: a ``GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryQuerySession

    grade_entry_query_session = property(fget=get_grade_entry_query_session)

    @abc.abstractmethod
    def get_grade_entry_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryQuerySession

    @abc.abstractmethod
    def get_grade_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        :return: a ``GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` is ``true``.*

        """
        return  # osid.grading.GradeEntrySearchSession

    grade_entry_search_session = property(fget=get_grade_entry_search_session)

    @abc.abstractmethod
    def get_grade_entry_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntrySearchSession

    @abc.abstractmethod
    def get_grade_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        :return: a ``GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryAdminSession

    grade_entry_admin_session = property(fget=get_grade_entry_admin_session)

    @abc.abstractmethod
    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryAdminSession

    @abc.abstractmethod
    def get_grade_entry_notification_session(self, receiver):
        """Gets the notification session for notifications pertaining to grade entry changes.

        :param receiver: the grade entry receiver
        :type receiver: ``osid.grading.GradeEntryReceiver``
        :return: a ``GradeEntryNotificationSession``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NullArgument`` -- ``receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryNotificationSession

    @abc.abstractmethod
    def get_grade_entry_notification_session_for_gradebook(self, receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry notification service for the given gradebook.

        :param receiver: the grade entry receiver
        :type receiver: ``osid.grading.GradeEntryReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _grade_entry_notification_session``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``receiver`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryNotificationSession

    @abc.abstractmethod
    def get_gradebook_column_lookup_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        :return: a ``GradebookColumnLookupSession``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnLookupSession

    gradebook_column_lookup_session = property(fget=get_gradebook_column_lookup_session)

    @abc.abstractmethod
    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _gradebook_column_lookup_session``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnLookupSession

    @abc.abstractmethod
    def get_gradebook_column_query_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnQuerySession

    gradebook_column_query_session = property(fget=get_gradebook_column_query_session)

    @abc.abstractmethod
    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnQuerySession

    @abc.abstractmethod
    def get_gradebook_column_search_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        :return: a ``GradebookColumnSearchSession``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnSearchSession

    gradebook_column_search_session = property(fget=get_gradebook_column_search_session)

    @abc.abstractmethod
    def get_gradebook_column_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _gradebook_column_search_session``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnSearchSession

    @abc.abstractmethod
    def get_gradebook_column_admin_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        :return: a ``GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnAdminSession

    gradebook_column_admin_session = property(fget=get_gradebook_column_admin_session)

    @abc.abstractmethod
    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnAdminSession

    @abc.abstractmethod
    def get_gradebook_column_notification_session(self, gradebook_column_receiver):
        """Gets the notification session for notifications pertaining to gradebook column changes.

        :param gradebook_column_receiver: the grade system receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :return: a ``GradebookColumnNotificationSession``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnNotificationSession

    @abc.abstractmethod
    def get_gradebook_column_notification_session_for_gradebook(self, gradebook_column_receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column notification service for the given gradebook.

        :param gradebook_column_receiver: the gradebook column receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _gradebook_column_notification_session``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnNotificationSession

    @abc.abstractmethod
    def get_gradebook_column_gradebook_session(self):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        :return: a ``GradebookColumnGradebookSession``
        :rtype: ``osid.grading.GradebookColumnGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnGradebookSession

    gradebook_column_gradebook_session = property(fget=get_gradebook_column_gradebook_session)

    @abc.abstractmethod
    def get_gradebook_column_gradebook_assignment_session(self):
        """Gets the session for assigning gradebook column to gradebook mappings.

        :return: a ``GradebookColumnGradebookAssignmentSession``
        :rtype: ``osid.grading.GradebookColumnGradebookAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        return  # osid.grading.GradebookColumnGradebookAssignmentSession

    gradebook_column_gradebook_assignment_session = property(fget=get_gradebook_column_gradebook_assignment_session)

    @abc.abstractmethod
    def get_gradebook_column_smart_gradebook_session(self, gradebook_id):
        """Gets the session for managing smart gradebooks of gradebook columns.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: a ``GradebookColumnSmartGradebookSession``
        :rtype: ``osid.grading.GradebookColumnSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_smart_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_smart_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnSmartGradebookSession

    @abc.abstractmethod
    def get_gradebook_lookup_session(self):
        """Gets the OsidSession associated with the gradebook lookup service.

        :return: a ``GradebookLookupSession``
        :rtype: ``osid.grading.GradebookLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        return  # osid.grading.GradebookLookupSession

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)

    @abc.abstractmethod
    def get_gradebook_query_session(self):
        """Gets the OsidSession associated with the gradebook query service.

        :return: a ``GradebookQuerySession``
        :rtype: ``osid.grading.GradebookQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is true.*

        """
        return  # osid.grading.GradebookQuerySession

    gradebook_query_session = property(fget=get_gradebook_query_session)

    @abc.abstractmethod
    def get_gradebook_search_session(self):
        """Gets the OsidSession associated with the gradebook search service.

        :return: a ``GradebookSearchSession``
        :rtype: ``osid.grading.GradebookSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_search()`` is true.*

        """
        return  # osid.grading.GradebookSearchSession

    gradebook_search_session = property(fget=get_gradebook_search_session)

    @abc.abstractmethod
    def get_gradebook_admin_session(self):
        """Gets the OsidSession associated with the gradebook administration service.

        :return: a ``GradebookAdminSession``
        :rtype: ``osid.grading.GradebookAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        return  # osid.grading.GradebookAdminSession

    gradebook_admin_session = property(fget=get_gradebook_admin_session)

    @abc.abstractmethod
    def get_gradebook_notification_session(self, gradebook_receiver):
        """Gets the notification session for notifications pertaining to gradebook service changes.

        :param gradebook_receiver: the gradebook receiver
        :type gradebook_receiver: ``osid.grading.GradebookReceiver``
        :return: a ``GradebookNotificationSession``
        :rtype: ``osid.grading.GradebookNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_notification()`` is true.*

        """
        return  # osid.grading.GradebookNotificationSession

    @abc.abstractmethod
    def get_gradebook_hierarchy_session(self):
        """Gets the session traversing gradebook hierarchies.

        :return: a ``GradebookHierarchySession``
        :rtype: ``osid.grading.GradebookHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        return  # osid.grading.GradebookHierarchySession

    gradebook_hierarchy_session = property(fget=get_gradebook_hierarchy_session)

    @abc.abstractmethod
    def get_gradebook_hierarchy_design_session(self):
        """Gets the session designing gradebook hierarchies.

        :return: a ``GradebookHierarchyDesignSession``
        :rtype: ``osid.grading.GradebookHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        return  # osid.grading.GradebookHierarchyDesignSession

    gradebook_hierarchy_design_session = property(fget=get_gradebook_hierarchy_design_session)

    @abc.abstractmethod
    def get_grading_batch_manager(self):
        """Gets the ``GradingBatchManager``.

        :return: a ``GradingBatchManager``
        :rtype: ``osid.grading.batch.GradingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        return  # osid.grading.batch.GradingBatchManager

    grading_batch_manager = property(fget=get_grading_batch_manager)

    @abc.abstractmethod
    def get_grading_calculation_manager(self):
        """Gets the ``GradingCalculationManager``.

        :return: a ``GradingCalculationManager``
        :rtype: ``osid.grading.calculation.GradingCalculationManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_calculation() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        return  # osid.grading.calculation.GradingCalculationManager

    grading_calculation_manager = property(fget=get_grading_calculation_manager)

    @abc.abstractmethod
    def get_grading_transform_manager(self):
        """Gets the ``GradingTransformManager``.

        :return: a ``GradingTransformManager``
        :rtype: ``osid.grading.transform.GradingTransformManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_transform() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        return  # osid.grading.transform.GradingTransformManager

    grading_transform_manager = property(fget=get_grading_transform_manager)


class GradingProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemLookupSession

    @abc.abstractmethod
    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemLookupSession

    @abc.abstractmethod
    def get_grade_system_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuerySession

    @abc.abstractmethod
    def get_grade_system_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemQuerySession

    @abc.abstractmethod
    def get_grade_system_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchSession

    @abc.abstractmethod
    def get_grade_system_search_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemSearchSession

    @abc.abstractmethod
    def get_grade_system_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemAdminSession

    @abc.abstractmethod
    def get_grade_system_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemAdminSession

    @abc.abstractmethod
    def get_grade_system_notification_session(self, grade_system_receiver, proxy):
        """Gets the notification session for notifications pertaining to grade system changes.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemNotificationSession``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NullArgument`` -- ``grade_system_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemNotificationSession

    @abc.abstractmethod
    def get_grade_system_notification_session_for_gradebook(self, grade_system_receiver, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system notification service for the given gradebook.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _grade_system_notification_session``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_receiver, gradebook_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeSystemNotificationSession

    @abc.abstractmethod
    def get_grade_system_gradebook_session(self, proxy):
        """Gets the session for retrieving grade system to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemGradebookSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemGradebookSession

    @abc.abstractmethod
    def get_grade_system_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning grade system to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemGradebookAssignmentSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemGradebookSession

    @abc.abstractmethod
    def get_grade_system_smart_gradebook_session(self, gradebook_id, proxy):
        """Gets the session for managing smart gradebooks of grade systems.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemSmartGradebookSession``
        :rtype: ``osid.grading.GradeSystemSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_smart_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_smart_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSmartGradebookSession

    @abc.abstractmethod
    def get_grade_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryLookupSession

    @abc.abstractmethod
    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryLookupSession

    @abc.abstractmethod
    def get_grade_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryQuerySession

    @abc.abstractmethod
    def get_grade_entry_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryQuerySession

    @abc.abstractmethod
    def get_grade_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` is ``true``.*

        """
        return  # osid.grading.GradeEntrySearchSession

    @abc.abstractmethod
    def get_grade_entry_search_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntrySearchSession

    @abc.abstractmethod
    def get_grade_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryAdminSession

    @abc.abstractmethod
    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryAdminSession

    @abc.abstractmethod
    def get_grade_entry_notification_session(self, grade_entry_receiver, proxy):
        """Gets the notification session for notifications pertaining to grade entry changes.

        :param grade_entry_receiver: the grade entry receiver
        :type grade_entry_receiver: ``osid.grading.GradeEntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryNotificationSession``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NullArgument`` -- ``grade_entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryNotificationSession

    @abc.abstractmethod
    def get_grade_entry_notification_session_for_gradebook(self, grade_entry_receiver, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry notification service for the given gradebook.

        :param grade_entry_receiver: the grade entry receiver
        :type grade_entry_receiver: ``osid.grading.GradeEntryReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _grade_entry_notification_session``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_entry_receiver, gradebook_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradeEntryNotificationSession

    @abc.abstractmethod
    def get_gradebook_column_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnLookupSession``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnLookupSession

    @abc.abstractmethod
    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _gradebook_column_lookup_session``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnLookupSession

    @abc.abstractmethod
    def get_gradebook_column_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnQuerySession

    @abc.abstractmethod
    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnQuerySession

    @abc.abstractmethod
    def get_gradebook_column_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnSearchSession``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnSearchSession

    @abc.abstractmethod
    def get_gradebook_column_search_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _gradebook_column_search_session``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnSearchSession

    @abc.abstractmethod
    def get_gradebook_column_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnAdminSession

    @abc.abstractmethod
    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnAdminSession

    @abc.abstractmethod
    def get_gradebook_column_notification_session(self, gradebook_column_receiver, proxy):
        """Gets the notification session for notifications pertaining to gradebook column changes.

        :param gradebook_column_receiver: the grade system receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnNotificationSession``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnNotificationSession

    @abc.abstractmethod
    def get_gradebook_column_notification_session_for_gradebook(self, gradebook_column_receiver, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column notification service for the given gradebook.

        :param gradebook_column_receiver: the gradebook column receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _gradebook_column_notification_session``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_receiver, gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.grading.GradebookColumnNotificationSession

    @abc.abstractmethod
    def get_gradebook_column_gradebook_session(self, proxy):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnGradebookSession``
        :rtype: ``osid.grading.GradebookColumnGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnGradebookSession

    @abc.abstractmethod
    def get_gradebook_column_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning gradebook column to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnGradebookAssignmentSession``
        :rtype: ``osid.grading.GradebookColumnGradebookAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        return  # osid.grading.GradebookColumnGradebookAssignmentSession

    @abc.abstractmethod
    def get_gradebook_column_smart_gradebook_session(self, gradebook_id, proxy):
        """Gets the session for managing smart gradebooks of gradebook columns.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnSmartGradebookSession``
        :rtype: ``osid.grading.GradebookColumnSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_smart_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_smart_gradebook()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnSmartGradebookSession

    @abc.abstractmethod
    def get_gradebook_lookup_session(self, proxy):
        """Gets the OsidSession associated with the gradebook lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookLookupSession``
        :rtype: ``osid.grading.GradebookLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        return  # osid.grading.GradebookLookupSession

    @abc.abstractmethod
    def get_gradebook_query_session(self, proxy):
        """Gets the OsidSession associated with the gradebook query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookQuerySession``
        :rtype: ``osid.grading.GradebookQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is true.*

        """
        return  # osid.grading.GradebookQuerySession

    @abc.abstractmethod
    def get_gradebook_search_session(self, proxy):
        """Gets the OsidSession associated with the gradebook search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookSearchSession``
        :rtype: ``osid.grading.GradebookSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_search()`` is true.*

        """
        return  # osid.grading.GradebookSearchSession

    @abc.abstractmethod
    def get_gradebook_admin_session(self, proxy):
        """Gets the OsidSession associated with the gradebook administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookAdminSession``
        :rtype: ``osid.grading.GradebookAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        return  # osid.grading.GradebookAdminSession

    @abc.abstractmethod
    def get_gradebook_notification_session(self, gradebook_receiver, proxy):
        """Gets the notification session for notifications pertaining to gradebook service changes.

        :param gradebook_receiver: the gradebook receiver
        :type gradebook_receiver: ``osid.grading.GradebookReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookNotificationSession``
        :rtype: ``osid.grading.GradebookNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_notification()`` is true.*

        """
        return  # osid.grading.GradebookNotificationSession

    @abc.abstractmethod
    def get_gradebook_hierarchy_session(self, proxy):
        """Gets the session traversing gradebook hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookHierarchySession``
        :rtype: ``osid.grading.GradebookHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        return  # osid.grading.GradebookHierarchySession

    @abc.abstractmethod
    def get_gradebook_hierarchy_design_session(self, proxy):
        """Gets the session designing gradebook hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookHierarchyDesignSession``
        :rtype: ``osid.grading.GradebookHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        return  # osid.grading.GradebookHierarchyDesignSession

    @abc.abstractmethod
    def get_grading_batch_proxy_manager(self):
        """Gets the ``GradingBatchProxyManager``.

        :return: a ``GradingBatchProxyManager``
        :rtype: ``osid.grading.batch.GradingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        return  # osid.grading.batch.GradingBatchProxyManager

    grading_batch_proxy_manager = property(fget=get_grading_batch_proxy_manager)

    @abc.abstractmethod
    def get_grading_calculation_proxy_manager(self):
        """Gets the ``GradingCalculationProxyManager``.

        :return: a ``GradingCalculationProxyManager``
        :rtype: ``osid.grading.calculation.GradingCalculationProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_calculation() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        return  # osid.grading.calculation.GradingCalculationProxyManager

    grading_calculation_proxy_manager = property(fget=get_grading_calculation_proxy_manager)

    @abc.abstractmethod
    def get_grading_transform_proxy_manager(self):
        """Gets the ``GradingTransformProxyManager``.

        :return: a ``GradingTransformManager``
        :rtype: ``osid.grading.transform.GradingTransformProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_transform() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        return  # osid.grading.transform.GradingTransformProxyManager

    grading_transform_proxy_manager = property(fget=get_grading_transform_proxy_manager)
