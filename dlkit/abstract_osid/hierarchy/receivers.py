"""Implementations of hierarchy abstract base class receivers."""
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


class HierarchyStructureReceiver:
    """The hierarchy receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted hierarchy nodes."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_nodes(self, notification_id, node_ids):
        """The callback for notifications of new hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param node_ids: the ``Ids`` of the new nodes
        :type node_ids: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_nodes(self, notification_id, node_ids):
        """the callback for notification of deleted hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param node_ids: the ``Ids`` of the deleted nodes
        :type node_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_nodes(self, notification_id, node_ids):
        """The callback for notifications of changes to children of hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param node_ids: the ``Ids`` of the nodes whose children have changed
        :type node_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class HierarchyReceiver:
    """The hierarchy receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Hierarchy`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_hierarchies(self, notification_id, hierarchy_ids):
        """The callback for notifications of new hierarchies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param hierarchy_ids: the ``Ids`` of the new ``Hierarchies``
        :type hierarchy_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_hierarchies(self, notification_id, hierarchy_ids):
        """The callback for notification of updated hierarchies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param hierarchy_ids: the ``Ids`` of the updated ``Hierarchies``
        :type hierarchy_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_hierarchies(self, notification_id, hierarchy_ids):
        """the callback for notification of deleted hierarchies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param hierarchy_ids: the ``Ids`` of the deleted ``Hierarchies``
        :type hierarchy_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
