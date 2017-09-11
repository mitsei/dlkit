"""JSON implementations of cataloging searches."""

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
from dlkit.abstract_osid.cataloging import searches as abc_cataloging_searches
from dlkit.abstract_osid.osid import errors


class CatalogSearch(abc_cataloging_searches.CatalogSearch, osid_searches.OsidSearch):
    """The search interface for governing the search query for ``Catalogs``."""
    def __init__(self, runtime):
        self._namespace = 'cataloging.Catalog'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_catalogs(self, catalog_ids):
        """Execute this search among the given list of catalogs.

        arg:    catalog_ids (osid.id.IdList): list of catalogs
        raise:  NullArgument - ``catalog_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = catalog_ids

    @utilities.arguments_not_none
    def order_catalog_results(self, catalog_search_order):
        """Specify an ordering to the search results.

        arg:    catalog_search_order
                (osid.cataloging.CatalogSearchOrder): catalog search
                order
        raise:  NullArgument - ``catalog_search_order`` is ``null``
        raise:  Unsupported - ``catalog_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_catalog_search_record(self, catalog_search_record_type):
        """Gets the catalog search record corresponding to the given catalog search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    catalog_search_record_type (osid.type.Type): a catalog
                search record type
        return: (osid.cataloging.records.CatalogSearchRecord) - the
                catalog search record
        raise:  NullArgument - ``catalog_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(catalog_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class CatalogSearchResults(abc_cataloging_searches.CatalogSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'cataloging.Catalog'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_catalogs(self):
        """Gets the catalog list resulting from the search.

        return: (osid.cataloging.CatalogList) - the catalogs list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.CatalogList(self._results, runtime=self._runtime)

    catalogs = property(fget=get_catalogs)

    def get_catalog_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.cataloging.CatalogQueryInspector) - the catalog
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.CatalogQueryInspector(self._query_terms, runtime=self._runtime)

    catalog_query_inspector = property(fget=get_catalog_query_inspector)

    @utilities.arguments_not_none
    def get_catalog_search_results_record(self, catalog_search_record_type):
        """Gets the catalog search results record corresponding to the given catalog search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    catalog_search_record_type (osid.type.Type): a catalog
                search record type
        return: (osid.cataloging.records.CatalogSearchResultsRecord) -
                the catalog search results record
        raise:  NullArgument - ``catalog_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(catalog_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
