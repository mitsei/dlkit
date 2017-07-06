"""Implementations of cataloging abstract base class query_inspectors."""
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


class CatalogQueryInspector:
    """This is the query inspector for examining catalog queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_id_terms(self):
        """Gets the ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    id_terms = property(fget=get_id_terms)

    @abc.abstractmethod
    def get_ancestor_catalog_id_terms(self):
        """Gets the ancestor catalog ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_catalog_id_terms = property(fget=get_ancestor_catalog_id_terms)

    @abc.abstractmethod
    def get_ancestor_catalog_terms(self):
        """Gets the ancestor catalog query terms.

        :return: the query terms
        :rtype: ``osid.cataloging.CatalogQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogQueryInspector

    ancestor_catalog_terms = property(fget=get_ancestor_catalog_terms)

    @abc.abstractmethod
    def get_descendant_catalog_id_terms(self):
        """Gets the descendant catalog ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_catalog_id_terms = property(fget=get_descendant_catalog_id_terms)

    @abc.abstractmethod
    def get_descendant_catalog_terms(self):
        """Gets the descendant catalog query terms.

        :return: the query terms
        :rtype: ``osid.cataloging.CatalogQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogQueryInspector

    descendant_catalog_terms = property(fget=get_descendant_catalog_terms)

    @abc.abstractmethod
    def get_catalog_query_inspector_record(self, catalog_record_type):
        """Gets the catalog query inspector record corresponding to the given ``Catalog`` record ``Type``.

        :param catalog_record_type: a catalog record type
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog query inspector record
        :rtype: ``osid.cataloging.records.CatalogQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogQueryInspectorRecord
