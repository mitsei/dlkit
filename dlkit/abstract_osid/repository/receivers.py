"""Implementations of repository abstract base class receivers."""
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


class AssetReceiver:
    """The asset receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Asset`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_assets(self, notification_id, asset_ids):
        """The callback for notifications of new assets.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param asset_ids: the ``Ids`` of the new ``Assets``
        :type asset_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_assets(self, notification_id, asset_ids):
        """The callback for notification of updated assets.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param asset_ids: the ``Ids`` of the updated ``Assets``
        :type asset_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_assets(self, notification_id, asset_ids):
        """the callback for notification of deleted assets.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param asset_ids: the ``Ids`` of the deleted ``Assets``
        :type asset_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CompositionReceiver:
    """The composition receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Composition`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_compositions(self, notification_id, composition_ids):
        """The callback for notifications of new compositions.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param composition_ids: the ``Ids`` of the new ``Compositions``
        :type composition_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_compositions(self, notification_id, composition_ids):
        """The callback for notification of updated compositions.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param composition_ids: the ``Ids`` of the updated ``Compositions``
        :type composition_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_compositions(self, notification_id, composition_ids):
        """the callback for notification of deleted compositions.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param composition_ids: the ``Ids`` of the deleted ``Compositions``
        :type composition_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RepositoryReceiver:
    """The repository receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Repository`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_repositories(self, notification_id, repository_ids):
        """The callback for notifications of new repositories.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param repository_ids: the ``Ids`` of the new ``Repositories``
        :type repository_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_ancestor_repository(self, repository_id, ancestor_id):
        """The callback for notifications of new repository ancestors.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Repository`` ancestor
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_descendant_repository(self, repository_id, descendant_id):
        """The callback for notifications of new repository descendants.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Repository`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_repositories(self, notification_id, repository_ids):
        """The callback for notification of updated repositories.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param repository_ids: the ``Ids`` of the updated ``Repositories``
        :type repository_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_repositories(self, notification_id, repository_ids):
        """The callback for notification of deleted repositories.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param repository_ids: the ``Ids`` of the deleted ``Repositories``
        :type repository_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_ancestor_repository(self, repository_id, ancestor_id):
        """The callback for notifications of deleted repository ancestors.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Repository`` ancestor
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_descendant_repository(self, repository_id, descendant_id):
        """The callback for notifications of deleted repository descendants.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Repository`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def restructured_repository_hierarchy(self):
        """The callback for notifications of changes to a respository hierarchy where the hierarchy needs to refreshed.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass
