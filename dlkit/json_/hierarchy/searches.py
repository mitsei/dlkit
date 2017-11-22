"""JSON implementations of hierarchy searches."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import objects
from . import queries
from .. import utilities
from ..osid import searches as osid_searches
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.hierarchy import searches as abc_hierarchy_searches
from dlkit.abstract_osid.osid import errors


class HierarchySearch(abc_hierarchy_searches.HierarchySearch, osid_searches.OsidSearch):
    """``HierarchySearch`` defines the interface for specifying hierarchy search options."""
    _namespace = 'hierarchy.Hierarchy'

    def __init__(self, **kwargs):
        # Removed on 10/5/17:
        # self._namespace = 'hierarchy.Hierarchy'
        # self._runtime = runtime
        # record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        # self._record_type_data_sets = record_type_data_sets
        # self._all_supported_record_type_data_sets = record_type_data_sets
        # self._all_supported_record_type_ids = []
        # for data_set in record_type_data_sets:
        #     self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        self._id_list = None
        osid_searches.OsidSearch.__init__(self, **kwargs)

    @utilities.arguments_not_none
    def search_among_hierarchies(self, hierarchy_ids):
        """Execute this search using a given list of hierarchies.

        arg:    hierarchy_ids (osid.id.IdList): list of hierarchies
        raise:  NullArgument - ``hierarchy_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = hierarchy_ids

    @utilities.arguments_not_none
    def order_hierarchy_results(self, hierarchy_search_order):
        """Specify an ordering to the search results.

        arg:    hierarchy_search_order
                (osid.hierarchy.HierarchySearchOrder): hierarchy search
                order
        raise:  NullArgument - ``hierarchy_search_order`` is ``null``
        raise:  Unsupported - ``hierarchy_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_hierarchy_search_record(self, hierarchy_search_record_type):
        """Gets the hierarchy search record corresponding to the given hierarchy search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    hierarchy_search_record_type (osid.type.Type): a
                hierarchy search record type
        return: (osid.hierarchy.records.HierarchySearchRecord) - the
                hierarchy search record
        raise:  NullArgument - ``hierarchy_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(hierarchy_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class HierarchySearchResults(abc_hierarchy_searches.HierarchySearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    _namespace = 'hierarchy.Hierarchy'

    def __init__(self, **kwargs):  # removed results, query_terms, runtime on 10/18/17
        # # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # # self._results = [r for r in results]
        # self._results = results
        # self._query_terms = query_terms
        # self.retrieved = False
        osid_searches.OsidSearchResults.__init__(self, **kwargs)

    def get_hierarchies(self):
        """Gets the hierarchy list resulting from the search.

        return: (osid.hierarchy.HierarchyList) - the hierarchy list
        raise:  IllegalState - the hierarchy list was already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.HierarchyList(self._results, runtime=self._runtime)

    hierarchies = property(fget=get_hierarchies)

    def get_hierarchy_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.hierarchy.HierarchyQueryInspector) - the hierarchy
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.HierarchyQueryInspector(self._query_terms, runtime=self._runtime)

    hierarchy_query_inspector = property(fget=get_hierarchy_query_inspector)

    @utilities.arguments_not_none
    def get_hierarchy_search_results_record(self, hierarchy_search_record_type):
        """Gets the hierarchy search results record corresponding to the given hierarchy search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    hierarchy_search_record_type (osid.type.Type): a
                hierarchy search record type
        return: (osid.hierarchy.records.HierarchySearchResultsRecord) -
                the hierarchy search results record
        raise:  NullArgument - ``hierarchy_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(hierarchy_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
