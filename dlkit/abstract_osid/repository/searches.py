"""Implementations of repository abstract base class searches."""
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


class AssetSearch:
    """The search interface for governing asset searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_assets(self, asset_ids):
        """Execute this search among the given list of assets.

        :param asset_ids: list of asset ``Ids``
        :type asset_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_asset_results(self, asset_search_order):
        """Specify an ordering to the search results.

        :param asset_search_order: asset search order
        :type asset_search_order: ``osid.repository.AssetSearchOrder``
        :raise: ``NullArgument`` -- ``asset_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``asset_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_asset_search_record(self, asset_search_record_type):
        """Gets the asset search record corresponding to the given asset search record ``Type``.

        This method used to retrieve an object implementing the
        requested record.

        :param asset_search_record_type: an asset search record type
        :type asset_search_record_type: ``osid.type.Type``
        :return: the asset search record
        :rtype: ``osid.repository.records.AssetSearchRecord``
        :raise: ``NullArgument`` -- ``asset_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetSearchRecord


class AssetSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assets(self):
        """Gets the asset list resulting from a search.

        :return: the asset list
        :rtype: ``osid.repository.AssetList``
        :raise: ``IllegalState`` -- the list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetList

    assets = property(fget=get_assets)

    @abc.abstractmethod
    def get_asset_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQueryInspector

    asset_query_inspector = property(fget=get_asset_query_inspector)

    @abc.abstractmethod
    def get_asset_search_results_record(self, asset_search_record_type):
        """Gets the asset search results record corresponding to the given asset search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param asset_search_record_type: an asset search record type
        :type asset_search_record_type: ``osid.type.Type``
        :return: the asset search results record
        :rtype: ``osid.repository.records.AssetSearchResultsRecord``
        :raise: ``NullArgument`` -- ``asset_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetSearchResultsRecord


class CompositionSearch:
    """The interface for governing composition searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_compositions(self, composition_ids):
        """Execute this search among the given list of compositions.

        :param composition_ids: list of compositions
        :type composition_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``composition_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_composition_results(self, composition_search_order):
        """Specify an ordering to the search results.

        :param composition_search_order: composition search order
        :type composition_search_order: ``osid.repository.CompositionSearchOrder``
        :raise: ``NullArgument`` -- ``composition_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``composition_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_composition_search_record(self, composition_search_record_type):
        """Gets the composition search record corresponding to the given composition search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param composition_search_record_type: a composition search record type
        :type composition_search_record_type: ``osid.type.Type``
        :return: the composition search record
        :rtype: ``osid.repository.records.CompositionSearchRecord``
        :raise: ``NullArgument`` -- ``composition_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(composition_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionSearchRecord


class CompositionSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_compositions(self):
        """Gets the composition list resulting from a search.

        :return: the composition list
        :rtype: ``osid.repository.CompositionList``
        :raise: ``IllegalState`` -- the list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionList

    compositions = property(fget=get_compositions)

    @abc.abstractmethod
    def get_composition_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.repository.CompositionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionQueryInspector

    composition_query_inspector = property(fget=get_composition_query_inspector)

    @abc.abstractmethod
    def get_composition_search_results_record(self, composition_search_record_type):
        """Gets the composition search results record corresponding to the given composition search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param composition_search_record_type: a composition search record type
        :type composition_search_record_type: ``osid.type.Type``
        :return: the composition search results record
        :rtype: ``osid.repository.records.CompositionSearchResultsRecord``
        :raise: ``NullArgument`` -- ``composition_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(composition_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionSearchResultsRecord


class RepositorySearch:
    """The interface for governing repository searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_repositories(self, repository_ids):
        """Execute this search among the given list of repositories.

        :param repository_ids: list of repositories
        :type repository_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_repository_results(self, repository_search_order):
        """Specify an ordering to the search results.

        :param repository_search_order: repository search order
        :type repository_search_order: ``osid.repository.RepositorySearchOrder``
        :raise: ``NullArgument`` -- ``repository_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``repository_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_repository_search_record(self, repository_search_record_type):
        """Gets the repository search record corresponding to the given repository search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param repository_search_record_type: a repository search record type
        :type repository_search_record_type: ``osid.type.Type``
        :return: the repository search record
        :rtype: ``osid.repository.records.RepositorySearchRecord``
        :raise: ``NullArgument`` -- ``repository_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositorySearchRecord


class RepositorySearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_repositories(self):
        """Gets the repository list resulting from the search.

        :return: the repository list
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``IllegalState`` -- the list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryList

    repositories = property(fget=get_repositories)

    @abc.abstractmethod
    def get_repository_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.repository.RepositoryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQueryInspector

    repository_query_inspector = property(fget=get_repository_query_inspector)

    @abc.abstractmethod
    def get_repository_search_results_record(self, repository_search_record_type):
        """Gets the repository search results record corresponding to the given repository search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param repository_search_record_type: a repository search record type
        :type repository_search_record_type: ``osid.type.Type``
        :return: the repository search results record
        :rtype: ``osid.repository.records.RepositorySearchResultsRecord``
        :raise: ``NullArgument`` -- ``repository_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositorySearchResultsRecord
