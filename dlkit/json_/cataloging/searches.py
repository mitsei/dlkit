"""JSON implementations of cataloging searches."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..osid import searches as osid_searches
from dlkit.abstract_osid.cataloging import searches as abc_cataloging_searches


class CatalogSearch(abc_cataloging_searches.CatalogSearch, osid_searches.OsidSearch):
    """The search interface for governing the search query for ``Catalogs``."""

    @utilities.arguments_not_none
    def search_among_catalogs(self, catalog_ids):
        """Execute this search among the given list of catalogs.

        arg:    catalog_ids (osid.id.IdList): list of catalogs
        raise:  NullArgument - ``catalog_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

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

    def get_catalogs(self):
        """Gets the catalog list resulting from the search.

        return: (osid.cataloging.CatalogList) - the catalogs list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    catalogs = property(fget=get_catalogs)

    def get_catalog_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.cataloging.CatalogQueryInspector) - the catalog
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

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
