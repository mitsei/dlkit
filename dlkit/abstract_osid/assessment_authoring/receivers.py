"""Implementations of assessment.authoring abstract base class receivers."""
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


class AssessmentPartReceiver:
    """The assessment part receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted assessment parts."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_assessment_parts(self, notification_id, assessment_part_ids):
        """The callback for notifications of new assessment parts.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_part_ids: the ``Id`` of the new ``AssessmentParts``
        :type assessment_part_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_assessment_parts(self, notification_id, assessment_part_ids):
        """The callback for notification of updated assessment parts.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param assessment_part_ids: the ``Id`` of the updated ``AssessmentParts``
        :type assessment_part_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_assessment_parts(self, notification_id, assessment_part_ids):
        """The callback for notification of deleted assessment parts.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param assessment_part_ids: the ``Id`` of the deleted ``AssessmentParts``
        :type assessment_part_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleReceiver:
    """The sequence rule receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted sequence rules."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_sequence_rules(self, notification_id, sequence_rule_ids):
        """The callback for notifications of new sequence rules.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param sequence_rule_ids: the ``Ids`` of the new ``SequenceRules``
        :type sequence_rule_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_sequence_rules(self, notification_id, sequence_rule_ids):
        """The callback for notification of updated sequence rules.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param sequence_rule_ids: the ``Ids`` of the updated ``SequenceRules``
        :type sequence_rule_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_sequence_rules(self, notification_id, sequence_rule_ids):
        """The callback for notification of deleted sequence rules.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param sequence_rule_ids: the ``Ids`` of the deleted ``SequenceRules``
        :type sequence_rule_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleEnablerReceiver:
    """The sequence rule enabler receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted sequence rule enablers."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_sequence_rule_enablers(self, notification_id, sequence_rule_enabler_ids):
        """The callback for notifications of new sequence rule enablers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param sequence_rule_enabler_ids: the ``Ids`` of the new ``SequenceRuleEnablers``
        :type sequence_rule_enabler_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_sequence_rule_enablers(self, notification_id, sequence_rule_enabler_ids):
        """The callback for notification of updated sequence rule enablers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param sequence_rule_enabler_ids: the ``Ids`` of the updated ``SequenceRuleEnablers``
        :type sequence_rule_enabler_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_sequence_rule_enablers(self, notification_id, sequence_rule_enabler_ids):
        """The callback for notification of deleted sequence rule enablers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param sequence_rule_enabler_ids: the ``Ids`` of the deleted ``SequenceRuleEnablers``
        :type sequence_rule_enabler_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
