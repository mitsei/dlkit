"""JSON implementations of repository searches."""

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
from dlkit.abstract_osid.repository import searches as abc_repository_searches


class AssetSearch(abc_repository_searches.AssetSearch, osid_searches.OsidSearch):
    """The search interface for governing asset searches."""
    def __init__(self, runtime):
        self._namespace = 'repository.Asset'
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
    def search_among_assets(self, asset_ids):
        """Execute this search among the given list of assets.

        arg:    asset_ids (osid.id.IdList): list of asset ``Ids``
        raise:  NullArgument - ``asset_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = asset_ids

    @utilities.arguments_not_none
    def order_asset_results(self, asset_search_order):
        """Specify an ordering to the search results.

        arg:    asset_search_order (osid.repository.AssetSearchOrder):
                asset search order
        raise:  NullArgument - ``asset_search_order`` is ``null``
        raise:  Unsupported - ``asset_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_asset_search_record(self, asset_search_record_type):
        """Gets the asset search record corresponding to the given asset search record ``Type``.

        This method used to retrieve an object implementing the
        requested record.

        arg:    asset_search_record_type (osid.type.Type): an asset
                search record type
        return: (osid.repository.records.AssetSearchRecord) - the asset
                search record
        raise:  NullArgument - ``asset_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(asset_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class AssetSearchResults(abc_repository_searches.AssetSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'repository.Asset'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_assets(self):
        """Gets the asset list resulting from a search.

        return: (osid.repository.AssetList) - the asset list
        raise:  IllegalState - the list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.AssetList(self._results, runtime=self._runtime)

    assets = property(fget=get_assets)

    def get_asset_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.repository.AssetQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.AssetQueryInspector(self._query_terms, runtime=self._runtime)

    asset_query_inspector = property(fget=get_asset_query_inspector)

    @utilities.arguments_not_none
    def get_asset_search_results_record(self, asset_search_record_type):
        """Gets the asset search results record corresponding to the given asset search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    asset_search_record_type (osid.type.Type): an asset
                search record type
        return: (osid.repository.records.AssetSearchResultsRecord) - the
                asset search results record
        raise:  NullArgument - ``asset_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(asset_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class CompositionSearch(abc_repository_searches.CompositionSearch, osid_searches.OsidSearch):
    """The interface for governing composition searches."""
    def __init__(self, runtime):
        self._namespace = 'repository.Composition'
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
    def search_among_compositions(self, composition_ids):
        """Execute this search among the given list of compositions.

        arg:    composition_ids (osid.id.IdList): list of compositions
        raise:  NullArgument - ``composition_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = composition_ids

    @utilities.arguments_not_none
    def order_composition_results(self, composition_search_order):
        """Specify an ordering to the search results.

        arg:    composition_search_order
                (osid.repository.CompositionSearchOrder): composition
                search order
        raise:  NullArgument - ``composition_search_order`` is ``null``
        raise:  Unsupported - ``composition_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_composition_search_record(self, composition_search_record_type):
        """Gets the composition search record corresponding to the given composition search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    composition_search_record_type (osid.type.Type): a
                composition search record type
        return: (osid.repository.records.CompositionSearchRecord) - the
                composition search record
        raise:  NullArgument - ``composition_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(composition_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class CompositionSearchResults(abc_repository_searches.CompositionSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'repository.Composition'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_compositions(self):
        """Gets the composition list resulting from a search.

        return: (osid.repository.CompositionList) - the composition list
        raise:  IllegalState - the list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.CompositionList(self._results, runtime=self._runtime)

    compositions = property(fget=get_compositions)

    def get_composition_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.repository.CompositionQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.CompositionQueryInspector(self._query_terms, runtime=self._runtime)

    composition_query_inspector = property(fget=get_composition_query_inspector)

    @utilities.arguments_not_none
    def get_composition_search_results_record(self, composition_search_record_type):
        """Gets the composition search results record corresponding to the given composition search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    composition_search_record_type (osid.type.Type): a
                composition search record type
        return: (osid.repository.records.CompositionSearchResultsRecord)
                - the composition search results record
        raise:  NullArgument - ``composition_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(composition_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class RepositorySearch(abc_repository_searches.RepositorySearch, osid_searches.OsidSearch):
    """The interface for governing repository searches."""
    def __init__(self, runtime):
        self._namespace = 'repository.Repository'
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
    def search_among_repositories(self, repository_ids):
        """Execute this search among the given list of repositories.

        arg:    repository_ids (osid.id.IdList): list of repositories
        raise:  NullArgument - ``repository_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = repository_ids

    @utilities.arguments_not_none
    def order_repository_results(self, repository_search_order):
        """Specify an ordering to the search results.

        arg:    repository_search_order
                (osid.repository.RepositorySearchOrder): repository
                search order
        raise:  NullArgument - ``repository_search_order`` is ``null``
        raise:  Unsupported - ``repository_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_repository_search_record(self, repository_search_record_type):
        """Gets the repository search record corresponding to the given repository search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    repository_search_record_type (osid.type.Type): a
                repository search record type
        return: (osid.repository.records.RepositorySearchRecord) - the
                repository search record
        raise:  NullArgument - ``repository_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(repository_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class RepositorySearchResults(abc_repository_searches.RepositorySearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'repository.Repository'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_repositories(self):
        """Gets the repository list resulting from the search.

        return: (osid.repository.RepositoryList) - the repository list
        raise:  IllegalState - the list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.RepositoryList(self._results, runtime=self._runtime)

    repositories = property(fget=get_repositories)

    def get_repository_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.repository.RepositoryQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.RepositoryQueryInspector(self._query_terms, runtime=self._runtime)

    repository_query_inspector = property(fget=get_repository_query_inspector)

    @utilities.arguments_not_none
    def get_repository_search_results_record(self, repository_search_record_type):
        """Gets the repository search results record corresponding to the given repository search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    repository_search_record_type (osid.type.Type): a
                repository search record type
        return: (osid.repository.records.RepositorySearchResultsRecord)
                - the repository search results record
        raise:  NullArgument - ``repository_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(repository_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
