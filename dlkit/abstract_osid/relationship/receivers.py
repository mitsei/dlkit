"""Implementations of relationship abstract base class receivers."""
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


class RelationshipReceiver:
    """The relationship receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Relationship`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_relationships(self, notification_id, relationship_ids):
        """The callback for notifications of new relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param relationship_ids: the ``Ids`` of the new ``Relationships``
        :type relationship_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_relationships(self, notification_id, relationship_ids):
        """The callback for notification of updated relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param relationship_ids: the ``Ids`` of the updated ``Relationships``
        :type relationship_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_relationships(self, notification_id, relationship_ids):
        """the callback for notification of deleted relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param relationship_ids: the ``Ids`` of the deleted ``Relationships``
        :type relationship_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FamilyReceiver:
    """The family receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Family`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_families(self, notification_id, family_ids):
        """The callback for notifications of new families.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the new ``Families``
        :type family_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_families(self, notification_id, family_ids):
        """The callback for notification of updated families.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the updated ``Families``
        :type family_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_families(self, notification_id, family_ids):
        """the callback for notification of deleted familys.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the registered ``Families``
        :type family_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_families(self, notification_id, family_ids):
        """The callback for notifications of changes to children of family hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the ``Families`` whose children have changed
        :type family_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
