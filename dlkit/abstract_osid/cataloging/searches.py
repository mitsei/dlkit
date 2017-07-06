"""Implementations of cataloging abstract base class searches."""
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


class CatalogSearch:
    """The search interface for governing the search query for ``Catalogs``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_catalogs(self, catalog_ids):
        """Execute this search among the given list of catalogs.

        :param catalog_ids: list of catalogs
        :type catalog_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``catalog_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_catalog_results(self, catalog_search_order):
        """Specify an ordering to the search results.

        :param catalog_search_order: catalog search order
        :type catalog_search_order: ``osid.cataloging.CatalogSearchOrder``
        :raise: ``NullArgument`` -- ``catalog_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``catalog_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_catalog_search_record(self, catalog_search_record_type):
        """Gets the catalog search record corresponding to the given catalog search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param catalog_search_record_type: a catalog search record type
        :type catalog_search_record_type: ``osid.type.Type``
        :return: the catalog search record
        :rtype: ``osid.cataloging.records.CatalogSearchRecord``
        :raise: ``NullArgument`` -- ``catalog_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogSearchRecord


class CatalogSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalogs(self):
        """Gets the catalog list resulting from the search.

        :return: the catalogs list
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    catalogs = property(fget=get_catalogs)

    @abc.abstractmethod
    def get_catalog_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the catalog query inspector
        :rtype: ``osid.cataloging.CatalogQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogQueryInspector

    catalog_query_inspector = property(fget=get_catalog_query_inspector)

    @abc.abstractmethod
    def get_catalog_search_results_record(self, catalog_search_record_type):
        """Gets the catalog search results record corresponding to the given catalog search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param catalog_search_record_type: a catalog search record type
        :type catalog_search_record_type: ``osid.type.Type``
        :return: the catalog search results record
        :rtype: ``osid.cataloging.records.CatalogSearchResultsRecord``
        :raise: ``NullArgument`` -- ``catalog_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogSearchResultsRecord
