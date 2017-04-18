"""Implementations of assessment.authoring abstract base class search_orders."""
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


class AssessmentPartSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_assessment(self, style):
        """Specifies a preference for ordering the result set by the assessment.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_assessment_search_order(self):
        """Tests if an assessment search order is available.

        :return: ``true`` if an assessment search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_search_order(self):
        """Gets the assessment order.

        :return: the assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_assessment_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search_order()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSearchOrder

    assessment_search_order = property(fget=get_assessment_search_order)

    @abc.abstractmethod
    def order_by_section(self, style):
        """Specifies a preference for ordering the result set by the section.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_weight(self, style):
        """Specifies a preference for ordering the result set by the weight.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_allocated_time(self, style):
        """Specifies a preference for ordering the result set by the allocated time.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part_search_order_record(self, assessment_part_record_type):
        """Gets the assessment part search order record corresponding to the given assessment part record ``Type``.

        Multiple retrievals return the same underlying object.

        :param assessment_part_record_type: an assessment part record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the assessment part search order record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartSearchOrderRecord``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.AssessmentPartSearchOrderRecord


class SequenceRuleSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_assessment_part(self, style):
        """Specifies a preference for ordering the result set by the assessment part.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_assessment_part_search_order(self):
        """Tests if an assessment part search order is available.

        :return: ``true`` if an assessment part search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_part_search_order(self):
        """Gets the assessment order.

        :return: the assessment part search order
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_assessment_part_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_search_order()`` is ``true``.*

        """
        return  # osid.assessment.authoring.AssessmentPartSearchOrder

    assessment_part_search_order = property(fget=get_assessment_part_search_order)

    @abc.abstractmethod
    def order_by_next_assessment_part(self, style):
        """Specifies a preference for ordering the result set by the assessment part.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_next_assessment_part_search_order(self):
        """Tests if an assessment part search order is available.

        :return: ``true`` if an assessment part search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_next_assessment_part_search_order(self):
        """Gets the assessment order.

        :return: the assessment part search order
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_next_assessment_part_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_next_assessment_part_search_order()`` is ``true``.*

        """
        return  # osid.assessment.authoring.AssessmentPartSearchOrder

    next_assessment_part_search_order = property(fget=get_next_assessment_part_search_order)

    @abc.abstractmethod
    def order_by_minimum_score(self, style):
        """Specifies a preference for ordering the result set by the minimum score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_maximum_score(self, style):
        """Specifies a preference for ordering the result set by the maximum score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_cumulative(self, style):
        """Specifies a preference for ordering the result set by the cumulative.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_search_order_record(self, sequence_rule_record_type):
        """Gets the sequence rule search order record corresponding to the given sequence rule record ``Type``.

        Multiple retrievals return the same underlying object.

        :param sequence_rule_record_type: a sequence rule record type
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: the sequence rule search order record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleSearchOrderRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleSearchOrderRecord


class SequenceRuleEnablerSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rule_enabler_search_order_record(self, sequence_rule_enabler_record_type):
        """Gets the sequence rule enabler search order record corresponding to the given sequence rule enabler record ``Type``.

        Multiple retrievals return the same underlying object.

        :param sequence_rule_enabler_record_type: a sequence rule enabler record type
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: the sequence rule enabler search order record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerSearchOrderRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleEnablerSearchOrderRecord
