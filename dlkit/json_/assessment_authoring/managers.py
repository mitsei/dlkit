"""JSON implementations of assessment.authoring managers."""

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
from dlkit.manager_impls.assessment_authoring import managers as assessment_authoring_managers


class AssessmentAuthoringProfile(osid_managers.OsidProfile, assessment_authoring_managers.AssessmentAuthoringProfile):
    """The ``AssessmentAuthoringProfile`` describes the interoperability among assessment authoring services."""

    def supports_assessment_part_lookup(self):
        """Tests if looking up assessment part is supported.

        return: (boolean) - ``true`` if assessment part lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_lookup' in profile.SUPPORTS

    def supports_assessment_part_query(self):
        """Tests if querying assessment part is supported.

        return: (boolean) - ``true`` if assessment part query is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_query' in profile.SUPPORTS

    def supports_assessment_part_admin(self):
        """Tests if an assessment part administrative service is supported.

        return: (boolean) - ``true`` if assessment part administration
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_admin' in profile.SUPPORTS

    def supports_assessment_part_bank(self):
        """Tests if an assessment part bank lookup service is supported.

        return: (boolean) - ``true`` if an assessment part bank lookup
                service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_bank' in profile.SUPPORTS

    def supports_assessment_part_bank_assignment(self):
        """Tests if an assessment part bank service is supported.

        return: (boolean) - ``true`` if assessment part bank assignment
                service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_bank_assignment' in profile.SUPPORTS

    def supports_assessment_part_item(self):
        """Tests if an assessment part item service is supported for looking up assessment part and item mappings.

        return: (boolean) - ``true`` if assessment part item service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_item' in profile.SUPPORTS

    def supports_assessment_part_item_design(self):
        """Tests if an assessment part item design session is supported.

        return: (boolean) - ``true`` if an assessment part item design
                service is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_assessment_part_item_design' in profile.SUPPORTS

    def supports_sequence_rule_lookup(self):
        """Tests if looking up sequence rule is supported.

        return: (boolean) - ``true`` if sequence rule lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_sequence_rule_lookup' in profile.SUPPORTS

    def supports_sequence_rule_admin(self):
        """Tests if a sequence rule administrative service is supported.

        return: (boolean) - ``true`` if sequence rule administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_sequence_rule_admin' in profile.SUPPORTS

    def get_assessment_part_record_types(self):
        """Gets the supported ``AssessmentPart`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``AssessmentPart`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('ASSESSMENT_PART_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    assessment_part_record_types = property(fget=get_assessment_part_record_types)

    def get_assessment_part_search_record_types(self):
        """Gets the supported ``AssessmentPart`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``AssessmentPart`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('ASSESSMENT_PART_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    assessment_part_search_record_types = property(fget=get_assessment_part_search_record_types)

    def get_sequence_rule_record_types(self):
        """Gets the supported ``SequenceRule`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``SequenceRule`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('SEQUENCE_RULE_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    sequence_rule_record_types = property(fget=get_sequence_rule_record_types)

    def get_sequence_rule_search_record_types(self):
        """Gets the supported ``SequenceRule`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``SequenceRule`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('SEQUENCE_RULE_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    sequence_rule_search_record_types = property(fget=get_sequence_rule_search_record_types)

    def get_sequence_rule_enabler_record_types(self):
        """Gets the supported ``SequenceRuleEnabler`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``SequenceRuleEnabler`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('SEQUENCE_RULE_ENABLER_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    sequence_rule_enabler_record_types = property(fget=get_sequence_rule_enabler_record_types)

    def get_sequence_rule_enabler_search_record_types(self):
        """Gets the supported ``SequenceRuleEnabler`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``SequenceRuleEnabler`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('SEQUENCE_RULE_ENABLER_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    sequence_rule_enabler_search_record_types = property(fget=get_sequence_rule_enabler_search_record_types)


class AssessmentAuthoringManager(osid_managers.OsidManager, AssessmentAuthoringProfile, assessment_authoring_managers.AssessmentAuthoringManager):
    """The assessment authoring manager provides access to assessment authoring sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AssessmentPartLookupSession:`` a session to retrieve
        assessment part
      * ``AssessmentPartQuerySession:`` a session to query for
        assessment part
      * ``AssessmentPartSearchSession:`` a session to search for
        assessment part
      * ``AssessmentPartAdminSession:`` a session to create and delete
        assessment part
      * ``AssessmentPartNotificationSession:`` a session to receive
        notifications pertaining to assessment part changes
      * ``AssessmentPartBankSession:`` a session to look up assessment
        part bank mappings
      * ``AssessmentPartBankAssignmentSession:`` a session to manage
        assessment part to bank mappings
      * ``AssessmentPartSmartBankSession:`` a session to manage dynamic
        bank of assessment part
      * ``AssessmentPartItemSession:`` a session to look up assessment
        part to item mappings
      * ``AssessmentPartItemDesignSession:`` a session to map items to
        assessment parts

      * ``SequenceRuleLookupSession:`` a session to retrieve sequence
        rule
      * ``SequenceRuleQuerySession:`` a session to query for sequence
        rule
      * ``SequenceRuleSearchSession:`` a session to search for sequence
        rule
      * ``SequenceRuleAdminSession:`` a session to create and delete
        sequence rule
      * ``SequenceRuleNotificationSession:`` a session to receive
        notifications pertaining to sequence rule changes
      * ``SequenceRuleBankSession:`` a session to look up sequence rule
        bank mappings
      * ``SequenceRuleBankAssignmentSession:`` a session to manage
        sequence rule to bank mappings
      * ``SequenceRuleSmartBankSession:`` a session to manage dynamic
        bank of sequence rule

      * ``SequenceRuleEnablerLookupSession:`` a session to retrieve
        sequence rule enablers
      * ``SequenceRuleEnablerQuerySession:`` a session to query for
        sequence rule enablers
      * ``SequenceRuleEnablerSearchSession:`` a session to search for
        sequence rule enablers
      * ``SequenceRuleEnablerAdminSession:`` a session to create and
        delete sequence rule enablers
      * ``SequenceRuleEnablerNotificationSession:`` a session to receive
        notifications pertaining to sequence rule enabler changes
      * ``SequenceRuleEnablerBankSession:`` a session to look up
        sequence rule enabler bank mappings
      * ``SequenceRuleEnablerBankAssignmentSession:`` a session to
        manage sequence rule enabler to bank mappings
      * ``SequenceRuleEnablerSmartBankSession:`` a session to manage
        dynamic bank of sequence rule enablers
      * ``SequenceRuleEnableRuleLookupSession:`` a session to look up
        sequence rule enabler mappings
      * ``SequenceRuleEnablerRuleApplicationSession:`` a session to
        apply sequence rule enablers

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_assessment_part_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment part lookup service.

        return: (osid.assessment.authoring.AssessmentPartLookupSession)
                - an ``AssessmentPartLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        """
        if not self.supports_assessment_part_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartLookupSession(runtime=self._runtime)

    assessment_part_lookup_session = property(fget=get_assessment_part_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part lookup service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartLookupSession)
                - an ``AssessmentPartLookupSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AssessmentPartLookupSession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_assessment_part_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment part query service.

        return: (osid.assessment.authoring.AssessmentPartQuerySession) -
                an ``AssessmentPartQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_query()`` is ``true``.*

        """
        if not self.supports_assessment_part_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartQuerySession(runtime=self._runtime)

    assessment_part_query_session = property(fget=get_assessment_part_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part query service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartQuerySession) -
                an ``AssessmentPartQuerySession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AssessmentPartQuerySession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_assessment_part_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment part administration service.

        return: (osid.assessment.authoring.AssessmentPartAdminSession) -
                an ``AssessmentPartAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_admin()`` is ``true``.*

        """
        if not self.supports_assessment_part_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartAdminSession(runtime=self._runtime)

    assessment_part_admin_session = property(fget=get_assessment_part_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part administration service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartAdminSession) -
                an ``AssessmentPartAdminSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AssessmentPartAdminSession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_assessment_part_bank_session(self):
        """Gets the ``OsidSession`` to lookup assessment part/bank mappings for assessment parts.

        return: (osid.assessment.authoring.AssessmentPartBankSession) -
                an ``AssessmentPartBankSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_bank()`` is ``true``.*

        """
        if not self.supports_assessment_part_bank():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartBankSession(runtime=self._runtime)

    assessment_part_bank_session = property(fget=get_assessment_part_bank_session)

    @utilities.remove_null_proxy_kwarg
    def get_assessment_part_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning assessment part to bank.

        return:
                (osid.assessment.authoring.AssessmentPartBankAssignmentS
                ession) - an ``AssessmentPartBankAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_assessment_part_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_bank_assignment()`` is ``true``.*

        """
        if not self.supports_assessment_part_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartBankAssignmentSession(runtime=self._runtime)

    assessment_part_bank_assignment_session = property(fget=get_assessment_part_bank_assignment_session)

    @utilities.remove_null_proxy_kwarg
    def get_sequence_rule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service.

        return: (osid.assessment.authoring.SequenceRuleLookupSession) -
                a ``SequenceRuleLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_lookup()`` is ``true``.*

        """
        if not self.supports_sequence_rule_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.SequenceRuleLookupSession(runtime=self._runtime)

    sequence_rule_lookup_session = property(fget=get_sequence_rule_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_sequence_rule_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.SequenceRuleLookupSession) -
                a ``SequenceRuleLookupSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_sequence_rule_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.SequenceRuleLookupSession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_sequence_rule_admin_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule administration service.

        return: (osid.assessment.authoring.SequenceRuleAdminSession) - a
                ``SequenceRuleAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_admin()`` is ``true``.*

        """
        if not self.supports_sequence_rule_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.SequenceRuleAdminSession(runtime=self._runtime)

    sequence_rule_admin_session = property(fget=get_sequence_rule_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_sequence_rule_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule administration service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.SequenceRuleAdminSession) - a
                ``SequenceRuleAdminSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_sequence_rule_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.SequenceRuleAdminSession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_session(self, *args, **kwargs):
        """Gets the ``OsidSession`` associated with the assessment part item service.

        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(runtime=self._runtime)

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_session_for_bank(self, bank_id, *args, **kwargs):
        """Gets the ``OsidSession`` associated with the assessment part item service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_design_session(self, *args, **kwargs):
        """Gets the ``OsidSession`` associated with the assessment part item design service.

        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(runtime=self._runtime)

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_design_session_for_bank(self, bank_id, *args, **kwargs):
        """Gets the ``OsidSession`` associated with the assessment part item design service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(bank_id, runtime=self._runtime)


class AssessmentAuthoringProxyManager(osid_managers.OsidProxyManager, AssessmentAuthoringProfile, assessment_authoring_managers.AssessmentAuthoringProxyManager):
    """The assessment authoring manager provides access to assessment authoring sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AssessmentPartLookupSession:`` a session to retrieve
        assessment part
      * ``AssessmentPartQuerySession:`` a session to query for
        assessment part
      * ``AssessmentPartSearchSession:`` a session to search for
        assessment part
      * ``AssessmentPartAdminSession:`` a session to create and delete
        assessment part
      * ``AssessmentPartNotificationSession:`` a session to receive
        notifications pertaining to assessment part changes
      * ``AssessmentPartBankSession:`` a session to look up assessment
        part bank mappings
      * ``AssessmentPartBankAssignmentSession:`` a session to manage
        assessment part to bank mappings
      * ``AssessmentPartSmartBankSession:`` a session to manage dynamic
        bank of assessment part
      * ``AssessmentPartItemSession:`` a session to look up assessment
        part to item mappings
      * ``AssessmentPartItemDesignSession:`` a session to map items to
        assessment parts

      * ``SequenceRuleLookupSession:`` a session to retrieve sequence
        rule
      * ``SequenceRuleQuerySession:`` a session to query for sequence
        rule
      * ``SequenceRuleSearchSession:`` a session to search for sequence
        rule
      * ``SequenceRuleAdminSession:`` a session to create and delete
        sequence rule
      * ``SequenceRuleNotificationSession:`` a session to receive
        notifications pertaining to sequence rule changes
      * ``SequenceRuleBankSession:`` a session to look up sequence rule
        bank mappings
      * ``SequenceRuleBankAssignmentSession:`` a session to manage
        sequence rule to bank mappings
      * ``SequenceRuleSmartBankSession:`` a session to manage dynamic
        bank of sequence rule

      * ``SequenceRuleEnablerLookupSession:`` a session to retrieve
        sequence rule enablers
      * ``SequenceRuleEnablerQuerySession:`` a session to query for
        sequence rule enablers
      * ``SequenceRuleEnablerSearchSession:`` a session to search for
        sequence rule enablers
      * ``SequenceRuleEnablerAdminSession:`` a session to create and
        delete sequence rule enablers
      * ``SequenceRuleEnablerNotificationSession:`` a session to receive
        notifications pertaining to sequence rule enabler changes
      * ``SequenceRuleEnablerBankSession:`` a session to look up
        sequence rule enabler bank mappings
      * ``SequenceRuleEnablerBankAssignmentSession:`` a session to
        manage sequence rule enabler to bank mappings
      * ``SequenceRuleEnablerSmartBankSession:`` a session to manage
        dynamic bank of sequence rule enablers
      * ``SequenceRuleEnableRuleLookupSession:`` a session to look up
        sequence rule enabler mappings
      * ``SequenceRuleEnablerRuleApplicationSession:`` a session to
        apply sequence rule enablers

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_assessment_part_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartLookupSession)
                - an ``AssessmentPartLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        """
        if not self.supports_assessment_part_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part lookup service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartLookupSession)
                - an ``AssessmentPartLookupSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id or proxy is null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AssessmentPartLookupSession(bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartQuerySession) -
                an ``AssessmentPartQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_query()`` is ``true``.*

        """
        if not self.supports_assessment_part_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part query service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartQuerySession) -
                an ``AssessmentPartQuerySession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id or proxy is null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AssessmentPartQuerySession(bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartAdminSession) -
                an ``AssessmentPartAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_admin()`` is ``true``.*

        """
        if not self.supports_assessment_part_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part administration service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartAdminSession) -
                an ``AssessmentPartAdminSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id or proxy is null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.AssessmentPartAdminSession(bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_bank_session(self, proxy):
        """Gets the ``OsidSession`` to lookup assessment part/bank mappings for assessment parts.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.AssessmentPartBankSession) -
                an ``AssessmentPartBankSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_bank()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_bank()`` is ``true``.*

        """
        if not self.supports_assessment_part_bank():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartBankSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning assessment part to bank.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return:
                (osid.assessment.authoring.AssessmentPartBankAssignmentS
                ession) - an ``AssessmentPartBankAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_assessment_part_bank_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_bank_assignment()`` is ``true``.*

        """
        if not self.supports_assessment_part_bank_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartBankAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_sequence_rule_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.SequenceRuleLookupSession) -
                a ``SequenceRuleLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_lookup()`` is ``true``.*

        """
        if not self.supports_sequence_rule_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.SequenceRuleLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_sequence_rule_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.SequenceRuleLookupSession) -
                a ``SequenceRuleLookupSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id or proxy is null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_sequence_rule_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.SequenceRuleLookupSession(bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_sequence_rule_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.SequenceRuleAdminSession) - a
                ``SequenceRuleAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_admin()`` is ``true``.*

        """
        if not self.supports_sequence_rule_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.SequenceRuleAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_sequence_rule_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule administration service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.assessment.authoring.SequenceRuleAdminSession) - a
                ``SequenceRuleAdminSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id or proxy is null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_sequence_rule_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_sequence_rule_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_sequence_rule_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.SequenceRuleAdminSession(bank_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_item_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part item service.

        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(proxy=proxy, runtime=self._runtime)

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    @utilities.arguments_not_none
    def get_assessment_part_item_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part item service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(bank_id, proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_item_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part item design service.

        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(proxy=proxy, runtime=self._runtime)

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    @utilities.arguments_not_none
    def get_assessment_part_item_design_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part item design service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(bank_id, proxy=proxy, runtime=self._runtime)
