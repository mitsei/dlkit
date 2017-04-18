"""Implementations of resource abstract base class receivers."""
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


class ResourceReceiver:
    """The resource receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Resource`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_resources(self, notification_id, resource_ids):
        """The callback for notifications of new resources.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_ids: the ``Ids`` of the new ``Resources``
        :type resource_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_resources(self, notification_id, resource_ids):
        """The callback for notification of updated resources.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_ids: the ``Ids`` of the updated ``Resources``
        :type resource_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_resources(self, notification_id, resource_ids):
        """the callback for notification of deleted resources.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_ids: the ``Ids`` of the deleted ``Resources``
        :type resource_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class GroupReceiver:
    """The resource group receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted members."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_member(self, group_id, member_id):
        """The callback for notifications of new resource members.

        :param group_id: the ``Id`` of the ``Resource`` group
        :type group_id: ``osid.id.Id``
        :param member_id: the ``Id`` of the new ``Resource`` member
        :type member_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_member(self, group_id, member_id):
        """the callback for notification of deleted resource members.

        :param group_id: the ``Id`` of the ``Resource`` group
        :type group_id: ``osid.id.Id``
        :param member_id: the ``Id`` of the new ``Resource`` member
        :type member_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourceRelationshipReceiver:
    """The resource relationship receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``ResourceRelationships``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_resource_relationships(self, notification_id, resource_relationship_ids):
        """The callback for notifications of new relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_relationship_ids: the ``Ids`` of the new ``ResourceRelationships``
        :type resource_relationship_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_resource_relationships(self, notification_id, resource_relationship_ids):
        """The callback for notification of updated relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_relationship_ids: the ``Ids`` of the updated ``ResourceRelationships``
        :type resource_relationship_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_resource_relationships(self, notification_id, resource_relationship_ids):
        """The callback for notification of deleted relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_relationship_ids: the ``Ids`` of the deleted ``ResourceRelationships``
        :type resource_relationship_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BinReceiver:
    """The bin receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Bin`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_bins(self, notification_id, bin_ids):
        """The callback for notifications of new bins.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param bin_ids: the ``Ids`` of the new ``Bins``
        :type bin_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_ancestor_bin(self, bin_id, ancestor_id):
        """The callback for notifications of new bin ancestors.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Bin`` ancestor
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_descendant_bin(self, bin_id, descendant_id):
        """The callback for notifications of new bin descendants.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Bin`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_bins(self, notification_id, bin_ids):
        """The callback for notification of updated bins.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param bin_ids: the ``Ids`` of the updated ``Bins``
        :type bin_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_bins(self, notification_id, bin_ids):
        """The callback for notification of deleted bins.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param bin_ids: the ``Ids`` of the deleted ``Bins``
        :type bin_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_ancestor_bin(self, bin_id, ancestor_id):
        """The callback for notifications of deleted bin ancestors.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Bin`` ancestor
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_descendant_bin(self, bin_id, descendant_id):
        """The callback for notifications of deleted bin descendants.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Bin`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def restructured_bin_hierarchy(self):
        """The callback for notifications of changes to a bin hierarchy where the hierarchy needs to refreshed.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass
