"""Implementations of hierarchy abstract base class searches."""
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


class HierarchySearch:
    """``HierarchySearch`` defines the interface for specifying hierarchy search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_hierarchies(self, hierarchy_ids):
        """Execute this search using a given list of hierarchies.

        :param hierarchy_ids: list of hierarchies
        :type hierarchy_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``hierarchy_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_hierarchy_results(self, hierarchy_search_order):
        """Specify an ordering to the search results.

        :param hierarchy_search_order: hierarchy search order
        :type hierarchy_search_order: ``osid.hierarchy.HierarchySearchOrder``
        :raise: ``NullArgument`` -- ``hierarchy_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``hierarchy_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_hierarchy_search_record(self, hierarchy_search_record_type):
        """Gets the hierarchy search record corresponding to the given hierarchy search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param hierarchy_search_record_type: a hierarchy search record type
        :type hierarchy_search_record_type: ``osid.type.Type``
        :return: the hierarchy search record
        :rtype: ``osid.hierarchy.records.HierarchySearchRecord``
        :raise: ``NullArgument`` -- ``hierarchy_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.records.HierarchySearchRecord


class HierarchySearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_hierarchies(self):
        """Gets the hierarchy list resulting from the search.

        :return: the hierarchy list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``IllegalState`` -- the hierarchy list was already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.HierarchyList

    hierarchies = property(fget=get_hierarchies)

    @abc.abstractmethod
    def get_hierarchy_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the hierarchy query inspector
        :rtype: ``osid.hierarchy.HierarchyQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.HierarchyQueryInspector

    hierarchy_query_inspector = property(fget=get_hierarchy_query_inspector)

    @abc.abstractmethod
    def get_hierarchy_search_results_record(self, hierarchy_search_record_type):
        """Gets the hierarchy search results record corresponding to the given hierarchy search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param hierarchy_search_record_type: a hierarchy search record type
        :type hierarchy_search_record_type: ``osid.type.Type``
        :return: the hierarchy search results record
        :rtype: ``osid.hierarchy.records.HierarchySearchResultsRecord``
        :raise: ``NullArgument`` -- ``hierarchy_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.records.HierarchySearchResultsRecord
