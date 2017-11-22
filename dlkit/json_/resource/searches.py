"""JSON implementations of resource searches."""

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
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.resource import searches as abc_resource_searches


class ResourceSearch(abc_resource_searches.ResourceSearch, osid_searches.OsidSearch):
    """The search interface for governing resource searches."""
    _namespace = 'resource.Resource'

    def __init__(self, **kwargs):
        # Removed on 10/5/17:
        # self._namespace = 'resource.Resource'
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
    def search_among_resources(self, resource_ids):
        """Execute this search among the given list of resources.

        arg:    resource_ids (osid.id.IdList): list of resource ``Ids``
        raise:  NullArgument - ``resource_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = resource_ids

    @utilities.arguments_not_none
    def order_resource_results(self, resource_search_order):
        """Specify an ordering to the search results.

        arg:    resource_search_order
                (osid.resource.ResourceSearchOrder): resource search
                order
        raise:  NullArgument - ``order`` is ``null``
        raise:  Unsupported - ``order`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_resource_search_record(self, resource_search_record_type):
        """Gets the resource search record corresponding to the given resource search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    resource_search_record_type (osid.type.Type): a resource
                search record type
        return: (osid.resource.records.ResourceSearchRecord) - the
                resource search record
        raise:  NullArgument - ``resource_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type_type(resource_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ResourceSearchResults(abc_resource_searches.ResourceSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    _namespace = 'resource.Resource'

    def __init__(self, **kwargs):  # removed results, query_terms, runtime on 10/18/17
        # # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # # self._results = [r for r in results]
        # self._results = results
        # self._query_terms = query_terms
        # self.retrieved = False
        osid_searches.OsidSearchResults.__init__(self, **kwargs)

    def get_resources(self):
        """Gets the resource list resulting from a search.

        return: (osid.resource.ResourceList) - the resource list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.ResourceList(self._results, runtime=self._runtime)

    resources = property(fget=get_resources)

    def get_resource_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.resource.ResourceQueryInspector) - the resource
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.ResourceQueryInspector(self._query_terms, runtime=self._runtime)

    resource_query_inspector = property(fget=get_resource_query_inspector)

    @utilities.arguments_not_none
    def get_resource_search_results_record(self, resource_search_record_type):
        """Gets the resource search results record corresponding to the given resource search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    resource_search_record_type (osid.type.Type): a resource
                search record type
        return: (osid.resource.records.ResourceSearchResultsRecord) -
                the resource search results record
        raise:  NullArgument - ``resource_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type_type(resource_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BinSearch(abc_resource_searches.BinSearch, osid_searches.OsidSearch):
    """The interface for governing bin searches."""
    _namespace = 'resource.Bin'

    def __init__(self, **kwargs):
        # Removed on 10/5/17:
        # self._namespace = 'resource.Bin'
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
    def search_among_bins(self, bin_ids):
        """Execute this search among the given list of bins.

        arg:    bin_ids (osid.id.IdList): list of bins
        raise:  NullArgument - ``bin_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = bin_ids

    @utilities.arguments_not_none
    def order_bin_results(self, bin_search_order):
        """Specify an ordering to the search results.

        arg:    bin_search_order (osid.resource.BinSearchOrder): bin
                search order
        raise:  NullArgument - ``bin_search_order`` is ``null``
        raise:  Unsupported - ``bin_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_bin_search_record(self, bin_search_record_type):
        """Gets the bin search record corresponding to the given bin search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    bin_search_record_type (osid.type.Type): a bin search
                record type
        return: (osid.resource.records.BinSearchRecord) - the bin search
                record
        raise:  NullArgument - ``bin_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(bin_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BinSearchResults(abc_resource_searches.BinSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    _namespace = 'resource.Bin'

    def __init__(self, **kwargs):  # removed results, query_terms, runtime on 10/18/17
        # # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # # self._results = [r for r in results]
        # self._results = results
        # self._query_terms = query_terms
        # self.retrieved = False
        osid_searches.OsidSearchResults.__init__(self, **kwargs)

    def get_bins(self):
        """Gets the bin list resulting from the search.

        return: (osid.resource.BinList) - the bin list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.BinList(self._results, runtime=self._runtime)

    bins = property(fget=get_bins)

    def get_bin_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.resource.BinQueryInspector) - the bin query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.BinQueryInspector(self._query_terms, runtime=self._runtime)

    bin_query_inspector = property(fget=get_bin_query_inspector)

    @utilities.arguments_not_none
    def get_bin_search_results_record(self, bin_search_record_type):
        """Gets the bin search results record corresponding to the given bin search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    bin_search_record_type (osid.type.Type): a bin search
                record type
        return: (osid.resource.records.BinSearchResultsRecord) - the bin
                search results record
        raise:  NullArgument - ``bin_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(bin_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
