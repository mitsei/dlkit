"""Implementations of cataloging abstract base class search_orders."""
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


class CatalogSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_search_order_record(self, catalog_record_type):
        """Gets the catalog search order record corresponding to the given subject record ``Type``.

        Multiple retrievals return the same underlying object.

        :param catalog_record_type: a catalog record type
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog search order record
        :rtype: ``osid.cataloging.records.CatalogSearchOrderRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogSearchOrderRecord
