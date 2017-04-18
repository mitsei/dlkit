"""Implementations of assessment.authoring abstract base class searches."""
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


class AssessmentPartSearch:
    """The search interface for governing assessment part searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_assessment_parts(self, bank_ids):
        """Execute this search among the given list of assessment parts.

        :param bank_ids: list of assessment parts
        :type bank_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_assessment_part_results(self, assessment_part_search_order):
        """Specify an ordering to the search results.

        :param assessment_part_search_order: assessment part search order
        :type assessment_part_search_order: ``osid.assessment.authoring.AssessmentPartSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_part_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_part_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part_search_record(self, assessment_part_search_record_type):
        """Gets the assessment part search record corresponding to the given assessment part search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_part_search_record_type: an assessment part search record type
        :type assessment_part_search_record_type: ``osid.type.Type``
        :return: the assessment part search record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartSearchRecord``
        :raise: ``NullArgument`` -- ``assessment_part_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.AssessmentPartSearchRecord


class AssessmentPartSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_parts(self):
        """Gets the ``AssessmentPartList`` resulting from a search.

        :return: the assessment part list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    assessment_parts = property(fget=get_assessment_parts)

    @abc.abstractmethod
    def get_assessment_part_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the assessment part query inspector
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartQueryInspector

    assessment_part_query_inspector = property(fget=get_assessment_part_query_inspector)

    @abc.abstractmethod
    def get_assessment_part_search_results_record(self, assessment_part_search_record_type):
        """Gets the assessment part search results record corresponding to the given assessment part search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record.

        :param assessment_part_search_record_type: an assessment part search record type
        :type assessment_part_search_record_type: ``osid.type.Type``
        :return: the assessment part search results record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartSearchResultsRecord``
        :raise: ``NullArgument`` -- ``assessment_part_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.AssessmentPartSearchResultsRecord


class SequenceRuleSearch:
    """The search interface for governing sequence rule searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_sequence_rules(self, bank_ids):
        """Execute this search among the given list of sequence rules.

        :param bank_ids: list of sequence rules
        :type bank_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_sequence_rule_results(self, sequence_rule_search_order):
        """Specify an ordering to the search results.

        :param sequence_rule_search_order: sequence rule search order
        :type sequence_rule_search_order: ``osid.assessment.authoring.SequenceRuleSearchOrder``
        :raise: ``NullArgument`` -- ``sequence_rule_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``sequence_rule_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_search_record(self, sequence_rule_search_record_type):
        """Gets the sequence rule search record corresponding to the given sequence rule search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param sequence_rule_search_record_type: a sequence rule search record type
        :type sequence_rule_search_record_type: ``osid.type.Type``
        :return: the sequence rule search record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleSearchRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleSearchRecord


class SequenceRuleSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rules(self):
        """Gets the ``SequenceRuleList`` resulting from a search.

        :return: the sequence rule list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    sequence_rules = property(fget=get_sequence_rules)

    @abc.abstractmethod
    def get_sequence_rule_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the sequence rule query inspector
        :rtype: ``osid.assessment.authoring.SequenceRuleQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleQueryInspector

    sequence_rule_query_inspector = property(fget=get_sequence_rule_query_inspector)

    @abc.abstractmethod
    def get_sequence_rule_search_results_record(self, sequence_rule_search_record_type):
        """Gets the sequence rule search results record corresponding to the given sequence rule search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record.

        :param sequence_rule_search_record_type: a sequence rule search record type
        :type sequence_rule_search_record_type: ``osid.type.Type``
        :return: the sequence rule search results record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleSearchResultsRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleSearchResultsRecord


class SequenceRuleEnablerSearch:
    """The search interface for governing sequence rule enabler searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_sequence_rule_enablers(self, sequence_rule_enabler_ids):
        """Execute this search among the given list of sequence rule enablers.

        :param sequence_rule_enabler_ids: list of sequence rule enablers
        :type sequence_rule_enabler_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_sequence_rule_enabler_results(self, sequence_rule_enabler_search_order):
        """Specify an ordering to the search results.

        :param sequence_rule_enabler_search_order: sequence rule enabler search order
        :type sequence_rule_enabler_search_order: ``osid.assessment.authoring.SequenceRuleEnablerSearchOrder``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_enabler_search_record(self, sequence_rule_enabler_search_record_type):
        """Gets the sequence rule enabler search record corresponding to the given sequence rule enabler search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param sequence_rule_enabler_search_record_type: a sequence rule enabler search record type
        :type sequence_rule_enabler_search_record_type: ``osid.type.Type``
        :return: the sequence rule enabler search record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerSearchRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleEnablerSearchRecord


class SequenceRuleEnablerSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rule_enablers(self):
        """Gets the ``SequenceRuleEnablerList`` resulting from a search.

        :return: the sequence rule enabler list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    sequence_rule_enablers = property(fget=get_sequence_rule_enablers)

    @abc.abstractmethod
    def get_sequence_rule_enabler_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the sequence rule enabler query inspector
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerQueryInspector

    sequence_rule_enabler_query_inspector = property(fget=get_sequence_rule_enabler_query_inspector)

    @abc.abstractmethod
    def get_sequence_rule_enabler_search_results_record(self, sequence_rule_enabler_search_record_type):
        """Gets the sequence rule enabler search results record corresponding to the given sequence rule enabler search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record.

        :param sequence_rule_enabler_search_record_type: a sequence rule enabler search record type
        :type sequence_rule_enabler_search_record_type: ``osid.type.Type``
        :return: the sequence rule enabler search results record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerSearchResultsRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleEnablerSearchResultsRecord
