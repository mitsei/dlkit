"""Implementations of installation abstract base class receivers."""
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


class PackageReceiver:
    """The package receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted ``Packages``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_packages(self, package_ids):
        """The callback for notifications of new packages.

        :param package_ids: the ``Ids`` of the new ``Packages``
        :type package_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_packages(self, package_ids):
        """The callback for notification of updated packages.

        :param package_ids: the ``Ids`` of the updated ``Packages``
        :type package_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_packages(self, package_ids):
        """The callback for notification of deleted packages.

        :param package_ids: the ``Ids`` of the deleted ``Packages``
        :type package_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class DepotReceiver:
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted
        ``Depot`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_depots(self, depot_ids):
        """The callback for notifications of new depots.

        :param depot_ids: the ``Ids`` of the new ``Depots``
        :type depot_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_ancestor_depot(self, depot_id, ancestor_id):
        """The callback for notifications of new depot ancestors.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(depot_record_type) is false``
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_descendant_depot(self, depot_id, descendant_id):
        """The callback for notifications of new depot descendants.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Depot`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_depots(self, depot_ids):
        """The callback for notification of updated depots.

        :param depot_ids: the ``Ids`` of the updated ``Depots``
        :type depot_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_depots(self, depot_ids):
        """The callback for notification of deleted depots.

        :param depot_ids: the ``Ids`` of the deleted ``Depots``
        :type depot_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_ancestor_depot(self, depot_id, ancestor_id):
        """The callback for notifications of deleted depot ancestors.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Depot`` ancestor
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_descendant_depot(self, depot_id, descendant_id):
        """The callback for notifications of deleted depot descendants.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Depot`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def restructured_depot_hierarchy(self):
        """The callback for notifications of changes to a depot hierarchy where the hierarchy needs to refreshed.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class InstallationReceiver:
    """The installation receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted ``Installations``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_installations(self, installation_ids):
        """The callback for notifications of new installations.

        :param installation_ids: the ``Ids`` of the new ``Installations``
        :type installation_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_installations(self, installation_ids):
        """The callback for notification of deleted installations.

        :param installation_ids: the ``Ids`` of the deleted ``Installations``
        :type installation_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
