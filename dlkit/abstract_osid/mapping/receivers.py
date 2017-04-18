"""Implementations of mapping abstract base class receivers."""
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


class LocationReceiver:
    """The location receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted locations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_locations(self, notification_id, location_ids):
        """The callback for notifications of new locations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param location_ids: the ``Ids`` of the new ``Locations``
        :type location_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_locations(self, notification_id, location_ids):
        """The callback for notification of updated locations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param location_ids: the ``Ids`` of the updated ``Locations``
        :type location_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_locations(self, notification_id, location_ids):
        """The callback for notification of deleted locations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param location_ids: the ``Ids`` of the deleted ``Locations``
        :type location_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_locations(self, notification_id, location_ids):
        """The callback for notifications of changes to children of location hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param location_ids: the ``Ids`` of the ``Locations`` whose children have changed
        :type location_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class MapReceiver:
    """The map receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Map`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_maps(self, notification_id, map_ids):
        """The callback for notifications of new maps.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param map_ids: the ``Ids`` of the new ``Maps``
        :type map_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_maps(self, notification_id, map_ids):
        """The callback for notification of updated map.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param map_ids: the ``Ids`` of the updated ``Maps``
        :type map_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_maps(self, notification_id, map_ids):
        """The callback for notification of deleted maps.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param map_ids: the ``Ids`` of the deleted ``Maps``
        :type map_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_maps(self, notification_id, map_ids):
        """The callback for notifications of changes to children of map hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param map_ids: the ``Ids`` of the ``Maps`` whose children have changed
        :type map_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourceLocationReceiver:
    """The resource location receiver is the consumer supplied interface for receiving notifications pertaining to location changes of resources."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def entered_location(self, notification_id, location_id, resource_id):
        """The callback for notifications of resources entering locations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def exited_location(self, notification_id, route_id, resource_id):
        """The callback for notifications of resources exiting locations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param route_id: the ``Id`` of the ``Location``
        :type route_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def new_resource_coordinate(self, notification_id, coordinate, resource_id):
        """The callback for notifications of resources changing coordinates.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param coordinate: the new coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourcePositionReceiver:
    """The resource location receiver is the consumer supplied interface for receiving notifications pertaining to position changes of resources."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def moved_resource(self, notification_id, resource_id, coordinate):
        """The callback for notifications of resources entering locations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param coordinate: the ``Id`` of the ``Coordinate``
        :type coordinate: ``osid.mapping.Coordinate``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def entered_spatial_unit(self, notification_id, resource_id, spatial_unit):
        """The callback for notifications of resources entering spatial units.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``Id`` of the ``SpatialUnit``
        :type spatial_unit: ``osid.mapping.SpatialUnit``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def exited_spatial_unit(self, notification_id, resource_id, spatial_unit):
        """The callback for notifications of resources exiting spatial units.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``Id`` of the ``SpatialUnit``
        :type spatial_unit: ``osid.mapping.SpatialUnit``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
