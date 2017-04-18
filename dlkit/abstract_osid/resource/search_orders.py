"""Implementations of resource abstract base class search_orders."""
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


class ResourceSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_group(self, style):
        """Groups the search results by resources that are groups.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_demographic(self, style):
        """Groups the search results by resources that are demographics.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_avatar(self, style):
        """Orders the result set by avatar.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_avatar_search_order(self):
        """Tests if an ``AssetSearchOrder`` is available.

        :return: ``true`` if an asset search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_avatar_search_order(self):
        """Gets the search order for an asset.

        :return: the asset search order
        :rtype: ``osid.repository.AssetSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_avatar_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_avatar_search_order()`` is ``true``.*

        """
        return  # osid.repository.AssetSearchOrder

    avatar_search_order = property(fget=get_avatar_search_order)

    @abc.abstractmethod
    def get_resource_search_order_record(self, resource_record_type):
        """Gets the resource search record corresponding to the given resource record ``Type``.

        Multiple retrievals return the same underlying object.

        :param resource_record_type: a resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the resource search order record
        :rtype: ``osid.resource.records.ResourceSearchOrderRecord``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceSearchOrderRecord


class ResourceRelationshipSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_source_resource(self, style):
        """Specified a preference for ordering results by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_source_resource_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_source_resource_search_order(self):
        """Gets the search order for a resource.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_source_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_source_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    source_resource_search_order = property(fget=get_source_resource_search_order)

    @abc.abstractmethod
    def order_by_destination_resource(self, style):
        """Specified a preference for ordering results by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_destination_resource_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_destination_resource_search_order(self):
        """Gets the search order for a peer resource.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_destination_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_destination_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    destination_resource_search_order = property(fget=get_destination_resource_search_order)

    @abc.abstractmethod
    def get_resource_relationship_search_order_record(self, resource_relationship_record_type):
        """Gets the resource relationship search order record corresponding to the given resource relationship record ``Type``.

        Multiple retrievals return the same underlying object.

        :param resource_relationship_record_type: a resource relationship record type
        :type resource_relationship_record_type: ``osid.type.Type``
        :return: the resource relationship search order record
        :rtype: ``osid.resource.records.ResourceRelationshipSearchOrderRecord``
        :raise: ``NullArgument`` -- ``resource_relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(_resource_relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceRelationshipSearchOrderRecord


class BinSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bin_search_order_record(self, bin_record_type):
        """Gets the bin search record corresponding to the given bin record ``Type``.

        Multiple retrievals return the same underlying object.

        :param bin_record_type: a bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin search order record
        :rtype: ``osid.resource.records.BinSearchOrderRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.BinSearchOrderRecord
