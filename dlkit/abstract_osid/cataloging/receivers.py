"""Implementations of cataloging abstract base class receivers."""
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


class CatalogReceiver:
    """The catalog receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Catalog`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_catalogs(self, notification_id, catalog_ids):
        """The callback for notifications of new catalogs.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param catalog_ids: the ``Ids`` of the new ``Catalogs``
        :type catalog_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_catalogs(self, notification_id, catalog_ids):
        """The callback for notification of updated catalogs.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param catalog_ids: the ``Ids`` of the updated ``Catalogs``
        :type catalog_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_catalogs(self, notification_id, catalog_ids):
        """the callback for notification of deleted catalogs.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param catalog_ids: the ``Ids`` of the deleted ``Catalogs``
        :type catalog_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_catalogs(self, notification_id, catalog_ids):
        """The callback for notifications of changes to children of catalog hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param catalog_ids: the ``Ids`` of the ``Catalogs`` whose children have changed
        :type catalog_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CatalogEntryReceiver:
    """The catalog receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Ids`` in ``Catalogs``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_catalog_entries(self, notification_id, entry_ids):
        """The callback for notifications of new catalogs entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param entry_ids: the ``Ids`` of the new entries
        :type entry_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_catalog_entries(self, notification_id, entry_ids):
        """the callback for notification of deleted catalog entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param entry_ids: the ``Ids`` of the deleted entries
        :type entry_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
