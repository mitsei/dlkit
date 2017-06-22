"""Implementations of assessment abstract base class managers."""
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


class AssessmentProfile:
    """The ``AssessmentProfile`` describes the interoperability among assessment services."""
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
    def supports_my_assessment_taken(self):
        """Tests if a session is available to lookup taken assessments for the authenticated agent.

        :return: ``true`` if my assessment taken session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment(self):
        """Tests for the availability of a assessment service which is the service for taking and examining assessments taken.

        :return: ``true`` if assessment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_results(self):
        """Tests for the availability of an assessment rsults service.

        :return: ``true`` if assessment results is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_lookup(self):
        """Tests if an item lookup service is supported.

        :return: true if item lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_query(self):
        """Tests if an item query service is supported.

        :return: ``true`` if item query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_search(self):
        """Tests if an item search service is supported.

        :return: ``true`` if item search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_admin(self):
        """Tests if an item administrative service is supported.

        :return: ``true`` if item admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_notification(self):
        """Tests if item notification is supported.

        Messages may be sent when items are created, modified, or
        deleted.

        :return: ``true`` if item notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_bank(self):
        """Tests if an item to bank lookup session is available.

        :return: ``true`` if item bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_bank_assignment(self):
        """Tests if an item to bank assignment session is available.

        :return: ``true`` if item bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_item_smart_bank(self):
        """Tests if an item smart bank session is available.

        :return: ``true`` if item smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_lookup(self):
        """Tests if an assessment lookup service is supported.

        An assessment lookup service defines methods to access
        assessments.

        :return: true if assessment lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_query(self):
        """Tests if an assessment query service is supported.

        :return: ``true`` if assessment query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_search(self):
        """Tests if an assessment search service is supported.

        :return: ``true`` if assessment search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_admin(self):
        """Tests if an assessment administrative service is supported.

        :return: ``true`` if assessment admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_notification(self):
        """Tests if assessment notification is supported.

        Messages may be sent when assessments are created, modified, or
        deleted.

        :return: ``true`` if assessment notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_bank(self):
        """Tests if an assessment to bank lookup session is available.

        :return: ``true`` if assessment bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_bank_assignment(self):
        """Tests if an assessment to bank assignment session is available.

        :return: ``true`` if assessment bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_smart_bank(self):
        """Tests if an assessment smart bank session is available.

        :return: ``true`` if assessment smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_basic_authoring(self):
        """Tests if an assessment basic authoring session is available.

        :return: ``true`` if assessment basic authoring is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_lookup(self):
        """Tests if an assessment offered lookup service is supported.

        :return: true if assessment offered lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_query(self):
        """Tests if an assessment offered query service is supported.

        :return: ``true`` if assessment offered query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_search(self):
        """Tests if an assessment offered search service is supported.

        :return: ``true`` if assessment offered search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_admin(self):
        """Tests if an assessment offered administrative service is supported.

        :return: ``true`` if assessment offered admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_notification(self):
        """Tests if assessment offered notification is supported.

        Messages may be sent when offered assessments are created,
        modified, or deleted.

        :return: ``true`` if assessment offered notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_bank(self):
        """Tests if an assessment offered to bank lookup session is available.

        :return: ``true`` if assessment offered bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_bank_assignment(self):
        """Tests if an assessment offered to bank assignment session is available.

        :return: ``true`` if assessment offered bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_offered_smart_bank(self):
        """Tests if an assessment offered smart bank session is available.

        :return: ``true`` if assessment offered smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_lookup(self):
        """Tests if an assessment taken lookup service is supported.

        :return: ``true`` if assessment taken lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_query(self):
        """Tests if an assessment taken query service is supported.

        :return: ``true`` if assessment taken query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_search(self):
        """Tests if an assessment taken search service is supported.

        :return: ``true`` if assessment taken search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_admin(self):
        """Tests if an assessment taken administrative service is supported which is used to instantiate an assessment offered.

        :return: ``true`` if assessment taken admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_notification(self):
        """Tests if assessment taken notification is supported.

        Messages may be sent when items are created, modified, or
        deleted.

        :return: ``true`` if assessment taken notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_bank(self):
        """Tests if an assessment taken to bank lookup session is available.

        :return: ``true`` if assessment taken bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_bank_assignment(self):
        """Tests if an assessment taken to bank assignment session is available.

        :return: ``true`` if assessment taken bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_taken_smart_bank(self):
        """Tests if an assessment taken smart bank session is available.

        :return: ``true`` if assessment taken smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_lookup(self):
        """Tests if a bank lookup service is supported.

        A bank lookup service defines methods to access assessment
        banks.

        :return: ``true`` if bank lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_query(self):
        """Tests if a bank query service is supported.

        :return: ``true`` if bank query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_search(self):
        """Tests if a bank search service is supported.

        :return: ``true`` if bank search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_admin(self):
        """Tests if a banlk administrative service is supported.

        :return: ``true`` if bank admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_notification(self):
        """Tests if bank notification is supported.

        Messages may be sent when items are created, modified, or
        deleted.

        :return: ``true`` if bank notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_hierarchy(self):
        """Tests if a bank hierarchy traversal is supported.

        :return: ``true`` if a bank hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_bank_hierarchy_design(self):
        """Tests if bank hierarchy design is supported.

        :return: ``true`` if a bank hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_authoring(self):
        """Tests if an assessment authoring service is supported.

        :return: ``true`` if an assessment authoring is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_assessment_batch(self):
        """Tests if an assessment batch service is supported.

        :return: ``true`` if an assessment batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_record_types(self):
        """Gets the supported ``Item`` record types.

        :return: a list containing the supported ``Item`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    item_record_types = property(fget=get_item_record_types)

    @abc.abstractmethod
    def supports_item_record_type(self, item_record_type):
        """Tests if the given ``Item`` record type is supported.

        :param item_record_type: a ``Type`` indicating a ``Item`` record type
        :type item_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_search_record_types(self):
        """Gets the supported ``Item`` search record types.

        :return: a list containing the supported ``Item`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    item_search_record_types = property(fget=get_item_search_record_types)

    @abc.abstractmethod
    def supports_item_search_record_type(self, item_search_record_type):
        """Tests if the given ``Item`` search record type is supported.

        :param item_search_record_type: a ``Type`` indicating an ``Item`` search record type
        :type item_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``item_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_record_types(self):
        """Gets the supported ``Assessment`` record types.

        :return: a list containing the supported ``Assessment`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_record_types = property(fget=get_assessment_record_types)

    @abc.abstractmethod
    def supports_assessment_record_type(self, assessment_record_type):
        """Tests if the given ``Assessment`` record type is supported.

        :param assessment_record_type: a ``Type`` indicating an ``Assessment`` record type
        :type assessment_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_search_record_types(self):
        """Gets the supported ``Assessment`` search record types.

        :return: a list containing the supported assessment search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_search_record_types = property(fget=get_assessment_search_record_types)

    @abc.abstractmethod
    def supports_assessment_search_record_type(self, assessment_search_record_type):
        """Tests if the given assessment search record type is supported.

        :param assessment_search_record_type: a ``Type`` indicating an assessment search record type
        :type assessment_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_record_types(self):
        """Gets the supported ``AssessmentOffered`` record types.

        :return: a list containing the supported ``AssessmentOffered`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_offered_record_types = property(fget=get_assessment_offered_record_types)

    @abc.abstractmethod
    def supports_assessment_offered_record_type(self, assessment_offered_record_type):
        """Tests if the given ``AssessmentOffered`` record type is supported.

        :param assessment_offered_record_type: a ``Type`` indicating an ``AssessmentOffered`` record type
        :type assessment_offered_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_search_record_types(self):
        """Gets the supported ``AssessmentOffered`` search record types.

        :return: a list containing the supported ``AssessmentOffered`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_offered_search_record_types = property(fget=get_assessment_offered_search_record_types)

    @abc.abstractmethod
    def supports_assessment_offered_search_record_type(self, assessment_offered_search_record_type):
        """Tests if the given ``AssessmentOffered`` search record type is supported.

        :param assessment_offered_search_record_type: a ``Type`` indicating an ``AssessmentOffered`` search record type
        :type assessment_offered_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_record_types(self):
        """Gets the supported ``AssessmentTaken`` record types.

        :return: a list containing the supported ``AssessmentTaken`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_taken_record_types = property(fget=get_assessment_taken_record_types)

    @abc.abstractmethod
    def supports_assessment_taken_record_type(self, assessment_taken_record_type):
        """Tests if the given ``AssessmentTaken`` record type is supported.

        :param assessment_taken_record_type: a ``Type`` indicating an ``AssessmentTaken`` record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_search_record_types(self):
        """Gets the supported ``AssessmentTaken`` search record types.

        :return: a list containing the supported ``AssessmentTaken`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_taken_search_record_types = property(fget=get_assessment_taken_search_record_types)

    @abc.abstractmethod
    def supports_assessment_taken_search_record_type(self, assessment_taken_search_record_type):
        """Tests if the given ``AssessmentTaken`` search record type is supported.

        :param assessment_taken_search_record_type: a ``Type`` indicating an ``AssessmentTaken`` search record type
        :type assessment_taken_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_section_record_types(self):
        """Gets the supported ``AssessmentSection`` record types.

        :return: a list containing the supported ``AssessmentSection`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    assessment_section_record_types = property(fget=get_assessment_section_record_types)

    @abc.abstractmethod
    def supports_assessment_section_record_type(self, assessment_section_record_type):
        """Tests if the given ``AssessmentSection`` record type is supported.

        :param assessment_section_record_type: a ``Type`` indicating an ``AssessmentSection`` record type
        :type assessment_section_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_section_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_record_types(self):
        """Gets the supported ``Bank`` record types.

        :return: a list containing the supported ``Bank`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    bank_record_types = property(fget=get_bank_record_types)

    @abc.abstractmethod
    def supports_bank_record_type(self, bank_record_type):
        """Tests if the given ``Bank`` record type is supported.

        :param bank_record_type: a ``Type`` indicating a ``Bank`` type
        :type bank_record_type: ``osid.type.Type``
        :return: ``true`` if the given key record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_search_record_types(self):
        """Gets the supported bank search record types.

        :return: a list containing the supported ``Bank`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    bank_search_record_types = property(fget=get_bank_search_record_types)

    @abc.abstractmethod
    def supports_bank_search_record_type(self, bank_search_record_type):
        """Tests if the given bank search record type is supported.

        :param bank_search_record_type: a ``Type`` indicating a ``Bank`` search record type
        :type bank_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class AssessmentManager:
    """The assessment manager provides access to assessment sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``MyAssessmentTakenSession:`` a session to get taken or in
        progress assessments for the current agent
      * ``AssessmentSession:`` a session to be assessed and examine
        assessments taken
      * ``AssessmentResultsSession:`` a session to retrieve assessment
        results

      * ``ItemLookupSession:`` a session to look up ``Items``
      * ``ItemQuerySession`` : a session to query ``Items``
      * ``ItemSearchSession:`` a session to search ``Items``
      * ``ItemAdminSession:`` a session to create, modify and delete
        ``Items``
      * ``ItemNotificationSession: a`` session to receive messages
        pertaining to ``Item`` changes
      * ``ItemBankSession:`` a session for looking up item and bank
        mappings
      * ``ItemBankAssignmentSession:`` a session for managing item and
        bank mappings
      * ``ItemSmartBankSession:`` a session for managing dynamic banks

      * ``AssessmentLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentQuerySession:`` a session to query ``Assessments``
      * ``AssessmentSearchSession:`` a session to search ``Assessments``
      * ``AssessmentAdminSession:`` a session to create, modify and
        delete ``Assessments``
      * ``AssessmentNotificationSession: a`` session to receive messages
        pertaining to ``Assessment`` changes

      * ``AssessmentBankSession:`` a session for looking up assessment
        and bank mappings
      * ``AssessmentBankAssignmentSession:`` a session for managing
        assessment and bank mappings
      * ``AssessmentSmartBankSession:`` a session for managing dynamic
        banks
      * ``AssessmentBasicAuthoringSession:`` a session for making simple
        mappings of assessment items to assessments

      * ``AssessmentOfferedLookupSession:`` a session to look up
        ``AssessmentsOffered``
      * ``AssessmentOfferedQuerySession:`` a session to query
        ``AssessmentsOffered``
      * ``AssessmentOfferedSearchSession`` : a session to search
        ``AssessmentsOffered``
      * ``AssessmentOfferedAdminSession:`` a session to create, modify
        and delete ``AssessmentsOffered``
      * ``AssessmentOfferedNotificationSession: a`` session to receive
        messages pertaining to ``AssessmentOffered`` changes
      * ``AssessmentOfferedBankSession:`` a session for looking up
        assessments offered and bank mappings
      * ``AssessmentOfferedBankAssignmentSession:`` a session for
        managing assessments offered and bank mappings
      * ``AssessmentOfferedSmartBankSession`` : a session to manage
        dynamic banks of assessments offered

      * ``AssessmentTakenLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentTakenQuerySession:`` a session to query
        ``Assessments``
      * ``AssessmentTakenSearchSession:`` a session to search
        Assessments
      * ``AssessmentTakenAdminSession:`` a session to create, modify and
        delete ``AssessmentsTaken``
      * ``AssessmentTakenNotificationSession: a`` session to receive
        messages pertaining to ``AssessmentTaken`` changes
      * ``AssessmentTakenBankSession:`` a session for looking up
        assessments taken and bank mappings
      * ``AssessmenttTakenBankAssignmentSession:`` a session for
        managing assessments taken and bank mappings
      * ``AssessmentTakenSmartBankSession:`` a session to manage dynamic
        banks of assessments taken

      * ``BankLookupSession:`` a session to lookup banks
      * ``BankQuerySession`` : a session to query banks
      * ``BankSearchSession:`` a session to search banks
      * ``BankAdminSession`` : a session to create, modify and delete
        banks
      * ``BankNotificationSession`` : a session to receive messages
        pertaining to ``Bank`` changes
      * ``BankHierarchySession`` : a session to traverse the ``Bank``
        hierarchy
      * ``BankHierarchyDesignSession`` : a session to manage the
        ``Bank`` hierarchy

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_my_assessment_taken_session(self):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent.

        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_assessment_taken()`` is ``true``.*

        """
        return  # osid.assessment.MyAssessmentTakenSession

    my_assessment_taken_session = property(fget=get_my_assessment_taken_session)

    @abc.abstractmethod
    def get_my_assessment_taken_session_for_bank(self, bank_id):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_assessment_taken()`` is ``true``.*

        """
        return  # osid.assessment.MyAssessmentTakenSession

    @abc.abstractmethod
    def get_assessment_session(self):
        """Gets an ``AssessmentSession`` which is responsible for taking assessments and examining responses from assessments taken.

        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSession

    assessment_session = property(fget=get_assessment_session)

    @abc.abstractmethod
    def get_assessment_session_for_bank(self, bank_id):
        """Gets an ``AssessmentSession`` which is responsible for performing assessments for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSession

    @abc.abstractmethod
    def get_assessment_results_session(self):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results.

        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_results()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentResultsSession

    assessment_results_session = property(fget=get_assessment_results_session)

    @abc.abstractmethod
    def get_assessment_results_session_for_bank(self, bank_id):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results for the given bank.

        :param bank_id: the ``Id`` of the assessment taken
        :type bank_id: ``osid.id.Id``
        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_results()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentResultsSession

    @abc.abstractmethod
    def get_item_lookup_session(self):
        """Gets the ``OsidSession`` associated with the item lookup service.

        :return: an ``ItemLookupSession``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_lookup()`` is ``true``.*

        """
        return  # osid.assessment.ItemLookupSession

    item_lookup_session = property(fget=get_item_lookup_session)

    @abc.abstractmethod
    def get_item_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_lookup_session``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_lookup()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemLookupSession

    @abc.abstractmethod
    def get_item_query_session(self):
        """Gets the ``OsidSession`` associated with the item query service.

        :return: an ``ItemQuerySession``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_query()`` is ``true``.*

        """
        return  # osid.assessment.ItemQuerySession

    item_query_session = property(fget=get_item_query_session)

    @abc.abstractmethod
    def get_item_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_query_session``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemQuerySession

    @abc.abstractmethod
    def get_item_search_session(self):
        """Gets the ``OsidSession`` associated with the item search service.

        :return: an ``ItemSearchSession``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_search()`` is ``true``.*

        """
        return  # osid.assessment.ItemSearchSession

    item_search_session = property(fget=get_item_search_session)

    @abc.abstractmethod
    def get_item_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_search_session``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_search()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemSearchSession

    @abc.abstractmethod
    def get_item_admin_session(self):
        """Gets the ``OsidSession`` associated with the item administration service.

        :return: an ``ItemAdminSession``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_admin()`` is ``true``.*

        """
        return  # osid.assessment.ItemAdminSession

    item_admin_session = property(fget=get_item_admin_session)

    @abc.abstractmethod
    def get_item_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_admin_session``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemAdminSession

    @abc.abstractmethod
    def get_item_notification_session(self, item_receiver):
        """Gets the notification session for notifications pertaining to item changes.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :return: an ``ItemNotificationSession``
        :rtype: ``osid.assessment.ItemNotificationSession``
        :raise: ``NullArgument`` -- ``item_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_notification()`` is ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_item_notification_session_for_bank(self, item_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the item notification service for the given bank.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``item_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_item_bank_session(self):
        """Gets the ``OsidSession`` associated with the item banking service.

        :return: an ``ItemBankSession``
        :rtype: ``osid.assessment.ItemBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_bank()`` is ``true``.*

        """
        return  # osid.assessment.ItemBankSession

    item_bank_session = property(fget=get_item_bank_session)

    @abc.abstractmethod
    def get_item_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with the item bank assignment service.

        :return: an ``ItemBankAssignmentSession``
        :rtype: ``osid.assessment.ItemBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.ItemBankAssignmentSession

    item_bank_assignment_session = property(fget=get_item_bank_assignment_session)

    @abc.abstractmethod
    def get_item_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the item smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``ItemSmartBankSession``
        :rtype: ``osid.assessment.ItemSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.ItemSmartBankSession

    @abc.abstractmethod
    def get_assessment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment lookup service.

        :return: an ``AssessmentLookupSession``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_lookup()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentLookupSession

    assessment_lookup_session = property(fget=get_assessment_lookup_session)

    @abc.abstractmethod
    def get_assessment_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_lookup_session``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentLookupSession

    @abc.abstractmethod
    def get_assessment_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment query service.

        :return: an ``AssessmentQuerySession``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuerySession

    assessment_query_session = property(fget=get_assessment_query_session)

    @abc.abstractmethod
    def get_assessment_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_query_session``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentQuerySession

    @abc.abstractmethod
    def get_assessment_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment search service.

        :return: an ``AssessmentSearchSession``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSearchSession

    assessment_search_session = property(fget=get_assessment_search_session)

    @abc.abstractmethod
    def get_assessment_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_search_session``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentSearchSession

    @abc.abstractmethod
    def get_assessment_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment administration service.

        :return: an ``AssessmentAdminSession``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_admin()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentAdminSession

    assessment_admin_session = property(fget=get_assessment_admin_session)

    @abc.abstractmethod
    def get_assessment_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_admin_session``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentAdminSession

    @abc.abstractmethod
    def get_assessment_notification_session(self, assessment_receiver):
        """Gets the notification session for notifications pertaining to assessment changes.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :return: an ``AssessmentNotificationSession``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_notification()`` is ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_assessment_notification_session_for_bank(self, assessment_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the assessment notification service for the given bank.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_assessment_bank_session(self):
        """Gets the ``OsidSession`` associated with the assessment banking service.

        :return: an ``AssessmentBankSession``
        :rtype: ``osid.assessment.AssessmentBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_bank()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBankSession

    assessment_bank_session = property(fget=get_assessment_bank_session)

    @abc.abstractmethod
    def get_assessment_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with the assessment bank assignment service.

        :return: an ``AssessmentBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBankAssignmentSession

    assessment_bank_assignment_session = property(fget=get_assessment_bank_assignment_session)

    @abc.abstractmethod
    def get_assessment_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentSmartBankSession``
        :rtype: ``osid.assessment.AssessmentSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSmartBankSession

    @abc.abstractmethod
    def get_assessment_basic_authoring_session(self):
        """Gets the ``OsidSession`` associated with the assessment authoring service.

        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_basic_authoring()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBasicAuthoringSession

    assessment_basic_authoring_session = property(fget=get_assessment_basic_authoring_session)

    @abc.abstractmethod
    def get_assessment_basic_authoring_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment authoring service for the given bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` or ``supports_visibe_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_basic_authoring()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBasicAuthoringSession

    @abc.abstractmethod
    def get_assessment_offered_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service.

        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_lookup()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedLookupSession

    assessment_offered_lookup_session = property(fget=get_assessment_offered_lookup_session)

    @abc.abstractmethod
    def get_assessment_offered_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedLookupSession

    @abc.abstractmethod
    def get_assessment_offered_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered query service.

        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuerySession

    assessment_offered_query_session = property(fget=get_assessment_offered_query_session)

    @abc.abstractmethod
    def get_assessment_offered_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuerySession

    @abc.abstractmethod
    def get_assessment_offered_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered search service.

        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_search()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSearchSession

    assessment_offered_search_session = property(fget=get_assessment_offered_search_session)

    @abc.abstractmethod
    def get_assessment_offered_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSearchSession

    @abc.abstractmethod
    def get_assessment_offered_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered administration service.

        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_admin()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedAdminSession

    assessment_offered_admin_session = property(fget=get_assessment_offered_admin_session)

    @abc.abstractmethod
    def get_assessment_offered_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedAdminSession

    @abc.abstractmethod
    def get_assessment_offered_notification_session(self, assessment_offered_receiver):
        """Gets the notification session for notifications pertaining to offered assessment changes.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :return: an ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_offered_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_notification()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedNotificationSession

    @abc.abstractmethod
    def get_assessment_offered_notification_session_for_bank(self, assessment_offered_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the offered assessment notification service for the given bank.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: a ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedNotificationSession

    @abc.abstractmethod
    def get_assessment_offered_bank_session(self):
        """Gets the session for retrieving offered assessments to bank mappings.

        :return: an ``AssessmentOfferedBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_bank()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedBankSession

    assessment_offered_bank_session = property(fget=get_assessment_offered_bank_session)

    @abc.abstractmethod
    def get_assessment_offered_bank_assignment_session(self):
        """Gets the session for assigning offered assessments to bank mappings.

        :return: an ``AssessmentOfferedBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedBankAssignmentSession

    assessment_offered_bank_assignment_session = property(fget=get_assessment_offered_bank_assignment_session)

    @abc.abstractmethod
    def get_assessment_offered_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedSmartBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSmartBankSession

    @abc.abstractmethod
    def get_assessment_taken_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service.

        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_lookup()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenLookupSession

    assessment_taken_lookup_session = property(fget=get_assessment_taken_lookup_session)

    @abc.abstractmethod
    def get_assessment_taken_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenLookupSession

    @abc.abstractmethod
    def get_assessment_taken_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken query service.

        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuerySession

    assessment_taken_query_session = property(fget=get_assessment_taken_query_session)

    @abc.abstractmethod
    def get_assessment_taken_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuerySession

    @abc.abstractmethod
    def get_assessment_taken_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken search service.

        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_search()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSearchSession

    assessment_taken_search_session = property(fget=get_assessment_taken_search_session)

    @abc.abstractmethod
    def get_assessment_taken_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSearchSession

    @abc.abstractmethod
    def get_assessment_taken_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken administration service.

        :return: an ``AssessmentTakenAdminSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_admin()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenAdminSession

    assessment_taken_admin_session = property(fget=get_assessment_taken_admin_session)

    @abc.abstractmethod
    def get_assessment_taken_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenAdminSession

    @abc.abstractmethod
    def get_assessment_taken_notification_session(self, assessment_taken_receiver):
        """Gets the notification session for notifications pertaining to taken assessment changes.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_taken_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_notification()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenNotificationSession

    @abc.abstractmethod
    def get_assessment_taken_notification_session_for_bank(self, assessment_taken_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the taken assessment notification service for the given bank.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenNotificationSession

    @abc.abstractmethod
    def get_assessment_taken_bank_session(self):
        """Gets the session for retrieving taken assessments to bank mappings.

        :return: an ``AssessmentTakenBankSession``
        :rtype: ``osid.assessment.AssessmentTakenBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_bank()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenBankSession

    assessment_taken_bank_session = property(fget=get_assessment_taken_bank_session)

    @abc.abstractmethod
    def get_assessment_taken_bank_assignment_session(self):
        """Gets the session for assigning taken assessments to bank mappings.

        :return: an ``AssessmentTakenBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentTakenBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenBankAssignmentSession

    assessment_taken_bank_assignment_session = property(fget=get_assessment_taken_bank_assignment_session)

    @abc.abstractmethod
    def get_assessment_taken_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenSmartBankSession``
        :rtype: ``osid.assessment.AssessmentTakenSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSmartBankSession

    @abc.abstractmethod
    def get_bank_lookup_session(self):
        """Gets the OsidSession associated with the bank lookup service.

        :return: a ``BankLookupSession``
        :rtype: ``osid.assessment.BankLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_lookup()`` is true.*

        """
        return  # osid.assessment.BankLookupSession

    bank_lookup_session = property(fget=get_bank_lookup_session)

    @abc.abstractmethod
    def get_bank_query_session(self):
        """Gets the OsidSession associated with the bank query service.

        :return: a ``BankQuerySession``
        :rtype: ``osid.assessment.BankQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_query()`` is true.*

        """
        return  # osid.assessment.BankQuerySession

    bank_query_session = property(fget=get_bank_query_session)

    @abc.abstractmethod
    def get_bank_search_session(self):
        """Gets the OsidSession associated with the bank search service.

        :return: a ``BankSearchSession``
        :rtype: ``osid.assessment.BankSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_search()`` is true.*

        """
        return  # osid.assessment.BankSearchSession

    bank_search_session = property(fget=get_bank_search_session)

    @abc.abstractmethod
    def get_bank_admin_session(self):
        """Gets the OsidSession associated with the bank administration service.

        :return: a ``BankAdminSession``
        :rtype: ``osid.assessment.BankAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_admin()`` is true.*

        """
        return  # osid.assessment.BankAdminSession

    bank_admin_session = property(fget=get_bank_admin_session)

    @abc.abstractmethod
    def get_bank_notification_session(self, bankreceiver):
        """Gets the notification session for notifications pertaining to bank service changes.

        :param bankreceiver: the bank receiver interface
        :type bankreceiver: ``osid.assessment.BankReceiver``
        :return: a ``BankNotificationSession``
        :rtype: ``osid.assessment.BankNotificationSession``
        :raise: ``NullArgument`` -- ``bank_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_notification()`` is true.*

        """
        return  # osid.assessment.BankNotificationSession

    @abc.abstractmethod
    def get_bank_hierarchy_session(self):
        """Gets the session traversing bank hierarchies.

        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_hierarchy()`` is true.*

        """
        return  # osid.assessment.BankHierarchySession

    bank_hierarchy_session = property(fget=get_bank_hierarchy_session)

    @abc.abstractmethod
    def get_bank_hierarchy_design_session(self):
        """Gets the session designing bank hierarchies.

        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_hierarchy_design()`` is true.*

        """
        return  # osid.assessment.BankHierarchyDesignSession

    bank_hierarchy_design_session = property(fget=get_bank_hierarchy_design_session)

    @abc.abstractmethod
    def get_assessment_authoring_manager(self):
        """Gets an ``AssessmentAuthoringManager``.

        :return: an ``AssessmentAuthoringManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_authoring()`` is true.*

        """
        return  # osid.assessment.authoring.AssessmentAuthoringManager

    assessment_authoring_manager = property(fget=get_assessment_authoring_manager)

    @abc.abstractmethod
    def get_assessment_batch_manager(self):
        """Gets an ``AssessmentBatchManager``.

        :return: an ``AssessmentBatchManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_batch()`` is true.*

        """
        return  # osid.assessment.batch.AssessmentBatchManager

    assessment_batch_manager = property(fget=get_assessment_batch_manager)


class AssessmentProxyManager:
    """The assessment manager provides access to assessment sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``MyAssessmentTakenSession:`` a session to get taken or in
        progress assessments for the current agent
      * ``AssessmentSession:`` a session to be assessed and examine
        assessments taken
      * ``AssessmentResultsSession:`` a session to retrieve assessment
        results

      * ``ItemLookupSession:`` a session to look up ``Items``
      * ``ItemQuerySession`` : a session to query ``Items``
      * ``ItemSearchSession:`` a session to search ``Items``
      * ``ItemAdminSession:`` a session to create, modify and delete
        ``Items``
      * ``ItemNotificationSession: a`` session to receive messages
        pertaining to ``Item`` changes
      * ``ItemBankSession:`` a session for looking up item and bank
        mappings
      * ``ItemBankAssignmentSession:`` a session for managing item and
        bank mappings
      * ``ItemSmartBankSession:`` a session for managing dynamic banks

      * ``AssessmentLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentQuerySession:`` a session to query ``Assessments``
      * ``AssessmentSearchSession:`` a session to search ``Assessments``
      * ``AssessmentAdminSession:`` a session to create, modify and
        delete ``Assessments``
      * ``AssessmentNotificationSession: a`` session to receive messages
        pertaining to ``Assessment`` changes

      * ``AssessmentBankSession:`` a session for looking up assessment
        and bank mappings
      * ``AssessmentBankAssignmentSession:`` a session for managing
        assessment and bank mappings
      * ``AssessmentSmartBankSession:`` a session for managing dynamic
        banks
      * ``AssessmentBasicAuthoringSession:`` a session for making simple
        mappings of assessment items to assessments

      * ``AssessmentOfferedLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentOfferedQuerySession:`` a session to query
        ``Assessments``
      * ``AssessmentOfferedSearchSession`` : a session to search
        ``Assessments``
      * ``AssessmentOfferedAdminSession:`` a session to create, modify
        and delete ``Assessments``
      * ``AssessmentOfferedNotificationSession: a`` session to receive
        messages pertaining to ``Assessment`` changes
      * ``AssessmentOfferedBankSession:`` a session for looking up
        assessment and bank mappings
      * ``AssessmentOfferedBankAssignmentSession:`` a session for
        managing assessment and bank mappings
      * ``AssessmentOfferedSmartBankSession`` : a session to manage
        dynamic banks

      * ``AssessmentTakenLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentTakenQuerySession:`` a session to query
        ``Assessments``
      * ``AssessmentTakenSearchSession:`` a session to search
        Assessments
      * ``AssessmentTakenAdminSession:`` a session to create, modify and
        delete ``AssessmentsTaken``
      * ``AssessmentTakenNotificationSession: a`` session to receive
        messages pertaining to ``AssessmentTaken`` changes
      * ``AssessmentTakenBankSession:`` a session for looking up
        assessments taken and bank mappings
      * ``AssessmenttTakenBankAssignmentSession:`` a session for
        managing assessments taken and bank mappings
      * ``AssessmentTakenSmartBankSession:`` a session to manage dynamic
        banks of assessments taken

      * ``BankLookupSession:`` a session to lookup banks
      * ``BankQuerySession`` : a session to query banks
      * ``BankSearchSession:`` a session to search banks
      * ``BankAdminSession`` : a session to create, modify and delete
        banks
      * ``BankNotificationSession`` : a session to receive messages
        pertaining to ``Bank`` changes
      * ``BankHierarchySession`` : a session to traverse the ``Bank``
        hierarchy
      * ``BankHierarchyDesignSession`` : a session to manage the
        ``Bank`` hierarchy

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_my_assessment_taken_session(self, proxy):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_assessment_taken()`` is ``true``.*

        """
        return  # osid.assessment.MyAssessmentTakenSession

    @abc.abstractmethod
    def get_my_assessment_taken_session_for_bank(self, bank_id, proxy):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_assessment_taken()`` is ``true``.*

        """
        return  # osid.assessment.MyAssessmentTakenSession

    @abc.abstractmethod
    def get_assessment_session(self, proxy):
        """Gets an ``AssessmentSession`` which is responsible for taking assessments and examining responses from assessments taken.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSession

    @abc.abstractmethod
    def get_assessment_session_for_bank(self, bank_id, proxy):
        """Gets an ``AssessmentSession`` which is responsible for performing assessments for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSession

    @abc.abstractmethod
    def get_assessment_results_session(self, proxy):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_results()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentResultsSession

    @abc.abstractmethod
    def get_assessment_results_session_for_bank(self, bank_id, proxy):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results for the given bank.

        :param bank_id: the ``Id`` of the assessment taken
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_results()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentResultsSession

    @abc.abstractmethod
    def get_item_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemLookupSession``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_lookup()`` is ``true``.*

        """
        return  # osid.assessment.ItemLookupSession

    @abc.abstractmethod
    def get_item_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_lookup_session``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_lookup()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemLookupSession

    @abc.abstractmethod
    def get_item_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemQuerySession``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_query()`` is ``true``.*

        """
        return  # osid.assessment.ItemQuerySession

    @abc.abstractmethod
    def get_item_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_query_session``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemQuerySession

    @abc.abstractmethod
    def get_item_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemSearchSession``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_search()`` is ``true``.*

        """
        return  # osid.assessment.ItemSearchSession

    @abc.abstractmethod
    def get_item_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_search_session``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_search()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemSearchSession

    @abc.abstractmethod
    def get_item_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemAdminSession``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_admin()`` is ``true``.*

        """
        return  # osid.assessment.ItemAdminSession

    @abc.abstractmethod
    def get_item_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_admin_session``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.assessment.ItemAdminSession

    @abc.abstractmethod
    def get_item_notification_session(self, item_receiver, proxy):
        """Gets the notification session for notifications pertaining to item changes.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemNotificationSession``
        :rtype: ``osid.assessment.ItemNotificationSession``
        :raise: ``NullArgument`` -- ``item_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_notification()`` is ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_item_notification_session_for_bank(self, item_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item notification service for the given bank.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``item_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_item_bank_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item banking service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemBankSession``
        :rtype: ``osid.assessment.ItemBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_bank()`` is ``true``.*

        """
        return  # osid.assessment.ItemBankSession

    @abc.abstractmethod
    def get_item_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item bank assignment service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemBankAssignmentSession``
        :rtype: ``osid.assessment.ItemBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.ItemBankAssignmentSession

    @abc.abstractmethod
    def get_item_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemSmartBankSession``
        :rtype: ``osid.assessment.ItemSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.ItemSmartBankSession

    @abc.abstractmethod
    def get_assessment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentLookupSession``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_lookup()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentLookupSession

    @abc.abstractmethod
    def get_assessment_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_lookup_session``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentLookupSession

    @abc.abstractmethod
    def get_assessment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentQuerySession``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuerySession

    @abc.abstractmethod
    def get_assessment_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_query_session``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentQuerySession

    @abc.abstractmethod
    def get_assessment_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentSearchSession``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSearchSession

    @abc.abstractmethod
    def get_assessment_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_search_session``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentSearchSession

    @abc.abstractmethod
    def get_assessment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentAdminSession``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_admin()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentAdminSession

    @abc.abstractmethod
    def get_assessment_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_admin_session``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentAdminSession

    @abc.abstractmethod
    def get_assessment_notification_session(self, assessment_receiver, proxy):
        """Gets the notification session for notifications pertaining to assessment changes.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentNotificationSession``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_notification()`` is ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_assessment_notification_session_for_bank(self, assessment_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment notification service for the given bank.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.ItemNotificationSession

    @abc.abstractmethod
    def get_assessment_bank_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment banking service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBankSession``
        :rtype: ``osid.assessment.AssessmentBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_bank()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBankSession

    @abc.abstractmethod
    def get_assessment_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment bank assignment service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBankAssignmentSession

    @abc.abstractmethod
    def get_assessment_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentSmartBankSession``
        :rtype: ``osid.assessment.AssessmentSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSmartBankSession

    @abc.abstractmethod
    def get_assessment_basic_authoring_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment authoring service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_basic_authoring()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBasicAuthoringSession

    @abc.abstractmethod
    def get_assessment_basic_authoring_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment authoring service for the given bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` or ``supports_visibe_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_basic_authoring()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentBasicAuthoringSession

    @abc.abstractmethod
    def get_assessment_offered_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_lookup()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedLookupSession

    @abc.abstractmethod
    def get_assessment_offered_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedLookupSession

    @abc.abstractmethod
    def get_assessment_offered_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuerySession

    @abc.abstractmethod
    def get_assessment_offered_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuerySession

    @abc.abstractmethod
    def get_assessment_offered_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_search()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSearchSession

    @abc.abstractmethod
    def get_assessment_offered_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or proxy is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSearchSession

    @abc.abstractmethod
    def get_assessment_offered_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_admin()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedAdminSession

    @abc.abstractmethod
    def get_assessment_offered_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedAdminSession

    @abc.abstractmethod
    def get_assessment_offered_notification_session(self, assessment_offered_receiver, proxy):
        """Gets the notification session for notifications pertaining to offered assessment changes.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_offered_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_notification()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedNotificationSession

    @abc.abstractmethod
    def get_assessment_offered_notification_session_for_bank(self, assessment_offered_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the offered assessment notification service for the given bank.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` or ``proxy`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedNotificationSession

    @abc.abstractmethod
    def get_assessment_offered_bank_session(self, proxy):
        """Gets the session for retrieving offered assessments to bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_bank()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedBankSession

    @abc.abstractmethod
    def get_assessment_offered_bank_assignment_session(self, proxy):
        """Gets the session for assigning offered assessments to bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedBankAssignmentSession

    @abc.abstractmethod
    def get_assessment_offered_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedSmartBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSmartBankSession

    @abc.abstractmethod
    def get_assessment_taken_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_lookup()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenLookupSession

    @abc.abstractmethod
    def get_assessment_taken_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenLookupSession

    @abc.abstractmethod
    def get_assessment_taken_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuerySession

    @abc.abstractmethod
    def get_assessment_taken_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuerySession

    @abc.abstractmethod
    def get_assessment_taken_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_search()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSearchSession

    @abc.abstractmethod
    def get_assessment_taken_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSearchSession

    @abc.abstractmethod
    def get_assessment_taken_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenAdminSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_admin()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenAdminSession

    @abc.abstractmethod
    def get_assessment_taken_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenAdminSession

    @abc.abstractmethod
    def get_assessment_taken_notification_session(self, assessment_taken_receiver, proxy):
        """Gets the notification session for notifications pertaining to taken assessment changes.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_taken_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_notification()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenNotificationSession

    @abc.abstractmethod
    def get_assessment_taken_notification_session_for_bank(self, assessment_taken_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the taken assessment notification service for the given bank.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.assessment.AssessmentTakenNotificationSession

    @abc.abstractmethod
    def get_assessment_taken_bank_session(self, proxy):
        """Gets the session for retrieving taken assessments to bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenBankSession``
        :rtype: ``osid.assessment.AssessmentTakenBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_bank()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenBankSession

    @abc.abstractmethod
    def get_assessment_taken_bank_assignment_session(self, proxy):
        """Gets the session for assigning taken assessments to bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentTakenBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_bank_assignment()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenBankAssignmentSession

    @abc.abstractmethod
    def get_assessment_taken_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSmartBankSession``
        :rtype: ``osid.assessment.AssessmentTakenSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_smart_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_smart_bank()`` and
        ``supports_visibe_federation()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSmartBankSession

    @abc.abstractmethod
    def get_bank_lookup_session(self, proxy):
        """Gets the OsidSession associated with the bank lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankLookupSession``
        :rtype: ``osid.assessment.BankLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_lookup()`` is true.*

        """
        return  # osid.assessment.BankLookupSession

    @abc.abstractmethod
    def get_bank_query_session(self, proxy):
        """Gets the OsidSession associated with the bank query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankQuerySession``
        :rtype: ``osid.assessment.BankQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_query()`` is true.*

        """
        return  # osid.assessment.BankQuerySession

    @abc.abstractmethod
    def get_bank_search_session(self, proxy):
        """Gets the OsidSession associated with the bank search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankSearchSession``
        :rtype: ``osid.assessment.BankSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_search()`` is true.*

        """
        return  # osid.assessment.BankSearchSession

    @abc.abstractmethod
    def get_bank_admin_session(self, proxy):
        """Gets the OsidSession associated with the bank administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankAdminSession``
        :rtype: ``osid.assessment.BankAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_admin()`` is true.*

        """
        return  # osid.assessment.BankAdminSession

    @abc.abstractmethod
    def get_bank_notification_session(self, bank_receiver, proxy):
        """Gets the notification session for notifications pertaining to bank service changes.

        :param bank_receiver: the bank receiver interface
        :type bank_receiver: ``osid.assessment.BankReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankNotificationSession``
        :rtype: ``osid.assessment.BankNotificationSession``
        :raise: ``NullArgument`` -- ``bank_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_notification()`` is true.*

        """
        return  # osid.assessment.BankNotificationSession

    @abc.abstractmethod
    def get_bank_hierarchy_session(self, proxy):
        """Gets the session traversing bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_hierarchy()`` is true.*

        """
        return  # osid.assessment.BankHierarchySession

    @abc.abstractmethod
    def get_bank_hierarchy_design_session(self, proxy):
        """Gets the session designing bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_hierarchy_design()`` is true.*

        """
        return  # osid.assessment.BankHierarchyDesignSession

    @abc.abstractmethod
    def get_assessment_authoring_proxy_manager(self):
        """Gets an ``AssessmentAuthoringProxyManager``.

        :return: an ``AssessmentAuthoringProxyManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_authoring()`` is true.*

        """
        return  # osid.assessment.authoring.AssessmentAuthoringProxyManager

    assessment_authoring_proxy_manager = property(fget=get_assessment_authoring_proxy_manager)

    @abc.abstractmethod
    def get_assessment_batch_proxy_manager(self):
        """Gets an ``AssessmentBatchProxyManager``.

        :return: an ``AssessmentBatchProxyManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_batch()`` is true.*

        """
        return  # osid.assessment.batch.AssessmentBatchProxyManager

    assessment_batch_proxy_manager = property(fget=get_assessment_batch_proxy_manager)
