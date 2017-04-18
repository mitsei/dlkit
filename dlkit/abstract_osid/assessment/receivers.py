"""Implementations of assessment abstract base class receivers."""
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


class ItemReceiver:
    """The item receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Items``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_items(self, notification_id, item_ids):
        """The callback for notifications of new items.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param item_ids: the Id of the new ``Items``
        :type item_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_items(self, notification_id, item_ids):
        """The callback for notification of updated items.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param item_ids: the Id of the updated ``Items``
        :type item_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_items(self, notification_id, item_ids):
        """The callback for notification of deleted items.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param item_ids: the Id of the deleted ``Items``
        :type item_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentReceiver:
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Assessment`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_assessments(self, notification_id, assessment_ids):
        """The callback for notifications of new assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_ids: the ``Ids`` of the new ``Assessments``
        :type assessment_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_assessments(self, notification_id, assessment_ids):
        """The callback for notification of updated assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_ids: the ``Ids`` of the updated ``Assessments``
        :type assessment_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_assessments(self, notification_id, assessment_ids):
        """the callback for notification of deleted assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_ids: the ``Ids`` of the deleted ``Assessments``
        :type assessment_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentOfferedReceiver:
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``AssessmentOffered`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_assessments_offered(self, notification_id, assessment_offered_ids):
        """The callback for notifications of new offered assessments.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param assessment_offered_ids: the ``Id`` of the new ``AssessmentsOffered``
        :type assessment_offered_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_assessments_offered(self, notification_id, assessment_offered_ids):
        """The callback for notification of updated offered assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_offered_ids: the ``Id`` of the updated ``AssessmentsOffered``
        :type assessment_offered_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_assessments_offered(self, notification_id, assessment_offered_ids):
        """the callback for notification of deleted offered assessments.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param assessment_offered_ids: the ``Id`` of the deleted ``AssessmentsOffered``
        :type assessment_offered_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentTakenReceiver:
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``AssessmentTaken`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_assessments_taken(self, notification_id, assessment_taken_ids):
        """The callback for notifications of new taken assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_taken_ids: the ``Ids`` of the new ``AssessmentsTaken``
        :type assessment_taken_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_assessmenst_taken(self, notification_id, assessment_taken_ids):
        """The callback for notification of updated taken assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_taken_ids: the ``Ids`` of the updated ``AssessmentsTaken``
        :type assessment_taken_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_assessmenst_taken(self, notification_id, assessment_taken_ids):
        """the callback for notification of deleted taken assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_taken_ids: the ``Ids`` of the deleted ``AssessmentsTaken``
        :type assessment_taken_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BankReceiver:
    """The bank receiver is the consumer supplied interface for receiving notifications pertaining to new, updated, or deleted Bank objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_banks(self, notification_id, bank_ids):
        """The callback for notifications of new banks.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks``
        :type bank_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_banks(self, notification_id, bank_ids):
        """The callback for notification of updated banks.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks``
        :type bank_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_banks(self, notification_id, bank_ids):
        """The callback for notification of deleted banks.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks``
        :type bank_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_banks(self, notification_id, bank_ids):
        """The callback for notifications of changes to children of bank hierarchy nodes.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks`` whose children have changed
        :type bank_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
