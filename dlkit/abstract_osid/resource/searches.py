"""Implementations of resource abstract base class searches."""
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


class ResourceSearch:
    """The search interface for governing resource searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_resources(self, resource_ids):
        """Execute this search among the given list of resources.

        :param resource_ids: list of resource ``Ids``
        :type resource_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_resource_results(self, resource_search_order):
        """Specify an ordering to the search results.

        :param resource_search_order: resource search order
        :type resource_search_order: ``osid.resource.ResourceSearchOrder``
        :raise: ``NullArgument`` -- ``order`` is ``null``
        :raise: ``Unsupported`` -- ``order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_resource_search_record(self, resource_search_record_type):
        """Gets the resource search record corresponding to the given resource search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param resource_search_record_type: a resource search record type
        :type resource_search_record_type: ``osid.type.Type``
        :return: the resource search record
        :rtype: ``osid.resource.records.ResourceSearchRecord``
        :raise: ``NullArgument`` -- ``resource_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type_type(resource_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceSearchRecord


class ResourceSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resources(self):
        """Gets the resource list resulting from a search.

        :return: the resource list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceList

    resources = property(fget=get_resources)

    @abc.abstractmethod
    def get_resource_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the resource query inspector
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    resource_query_inspector = property(fget=get_resource_query_inspector)

    @abc.abstractmethod
    def get_resource_search_results_record(self, resource_search_record_type):
        """Gets the resource search results record corresponding to the given resource search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param resource_search_record_type: a resource search record type
        :type resource_search_record_type: ``osid.type.Type``
        :return: the resource search results record
        :rtype: ``osid.resource.records.ResourceSearchResultsRecord``
        :raise: ``NullArgument`` -- ``resource_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type_type(resource_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceSearchResultsRecord


class ResourceRelationshipSearch:
    """``ResourceRelationshipSearch`` defines the interface for specifying relationship search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_resource_relationships(self, resource_relationship_ids):
        """Execute this search among the given list of resource relationships.

        :param resource_relationship_ids: list of resource relationships
        :type resource_relationship_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``resource_relationship_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_resource_relationship_results(self, resource_relationship_search_order):
        """Specify an ordering to the search results.

        :param resource_relationship_search_order: relationship search order
        :type resource_relationship_search_order: ``osid.resource.ResourceRelationshipSearchOrder``
        :raise: ``NullArgument`` -- ``resource_relationship_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``resource_relationship_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_resource_relationship_search_record(self, resource_relationship_search_record_type):
        """Gets the resource relationship search record corresponding to the given relationship search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param resource_relationship_search_record_type: a resource relationship search record type
        :type resource_relationship_search_record_type: ``osid.type.Type``
        :return: the resource relationship search record
        :rtype: ``osid.resource.records.ResourceRelationshipSearchRecord``
        :raise: ``NullArgument`` -- ``resource_relationship_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_relationship_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceRelationshipSearchRecord


class ResourceRelationshipSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resource_relationships(self):
        """Gets the resource relationship list resulting from the search.

        :return: the resource relationship list
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceRelationshipList

    resource_relationships = property(fget=get_resource_relationships)

    @abc.abstractmethod
    def get_resource_relationship_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the resource relationship query inspector
        :rtype: ``osid.resource.ResourceRelationshipQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceRelationshipQueryInspector

    resource_relationship_query_inspector = property(fget=get_resource_relationship_query_inspector)

    @abc.abstractmethod
    def get_resource_relationship_search_results_record(self, resource_relationship_search_record_type):
        """Gets the resource relationship search results record corresponding to the given resource relationship search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param resource_relationship_search_record_type: a resource relationship search record type
        :type resource_relationship_search_record_type: ``osid.type.Type``
        :return: the resource relationship search results record
        :rtype: ``osid.resource.records.ResourceRelationshipSearchResultsRecord``
        :raise: ``NullArgument`` -- ``resource_relationship_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_relationship_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceRelationshipSearchResultsRecord


class BinSearch:
    """The interface for governing bin searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_bins(self, bin_ids):
        """Execute this search among the given list of bins.

        :param bin_ids: list of bins
        :type bin_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_bin_results(self, bin_search_order):
        """Specify an ordering to the search results.

        :param bin_search_order: bin search order
        :type bin_search_order: ``osid.resource.BinSearchOrder``
        :raise: ``NullArgument`` -- ``bin_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``bin_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_bin_search_record(self, bin_search_record_type):
        """Gets the bin search record corresponding to the given bin search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param bin_search_record_type: a bin search record type
        :type bin_search_record_type: ``osid.type.Type``
        :return: the bin search record
        :rtype: ``osid.resource.records.BinSearchRecord``
        :raise: ``NullArgument`` -- ``bin_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.BinSearchRecord


class BinSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bins(self):
        """Gets the bin list resulting from the search.

        :return: the bin list
        :rtype: ``osid.resource.BinList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.BinList

    bins = property(fget=get_bins)

    @abc.abstractmethod
    def get_bin_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the bin query inspector
        :rtype: ``osid.resource.BinQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.BinQueryInspector

    bin_query_inspector = property(fget=get_bin_query_inspector)

    @abc.abstractmethod
    def get_bin_search_results_record(self, bin_search_record_type):
        """Gets the bin search results record corresponding to the given bin search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param bin_search_record_type: a bin search record type
        :type bin_search_record_type: ``osid.type.Type``
        :return: the bin search results record
        :rtype: ``osid.resource.records.BinSearchResultsRecord``
        :raise: ``NullArgument`` -- ``bin_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.BinSearchResultsRecord
