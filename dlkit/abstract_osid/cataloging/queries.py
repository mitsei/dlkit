"""Implementations of cataloging abstract base class queries."""
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


class CatalogQuery:
    """This is the query for searching catalogs.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_id(self, id_, match):
        """Matches an ``Id`` in this catalog.

        Multiple Ids are treated as a boolean ``OR``.

        :param id: ``Id`` to match
        :type id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_id(self, match):
        """Matches catalogs that have any ``Id`` mapping.

        :param match: ``true`` to match catalogs with any ``Id`` mapping, ``false`` to match catalogs with no ``Id`` mapping
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_id_terms(self):
        """Clears the ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    id_terms = property(fdel=clear_id_terms)

    @abc.abstractmethod
    def match_ancestor_catalog_id(self, catalog_id, match):
        """Sets the catalog ``Id`` for this query to match catalogs that have the specified catalog as an ancestor.

        :param catalog_id: a catalog ``Id``
        :type catalog_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_catalog_id_terms(self):
        """Clears the ancestor ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_catalog_id_terms = property(fdel=clear_ancestor_catalog_id_terms)

    @abc.abstractmethod
    def supports_ancestor_catalog_query(self):
        """Tests if a ``CatalogQuery`` is available.

        :return: ``true`` if a catalog query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_catalog_query(self):
        """Gets the query for a catalog.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the catalog query
        :rtype: ``osid.cataloging.CatalogQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_catalog_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_catalog_query()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogQuery

    ancestor_catalog_query = property(fget=get_ancestor_catalog_query)

    @abc.abstractmethod
    def match_any_ancestor_catalog(self, match):
        """Matches catalogs with any ancestor.

        :param match: ``true`` to match catalogs with any ancestor, ``false`` to match root catalogs
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_catalog_terms(self):
        """Clears the ancestor query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_catalog_terms = property(fdel=clear_ancestor_catalog_terms)

    @abc.abstractmethod
    def match_descendant_catalog_id(self, catalog_id, match):
        """Sets the catalog ``Id`` for this query to match catalogs that have the specified catalog as an descendant.

        :param catalog_id: a catalog ``Id``
        :type catalog_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_catalog_id_terms(self):
        """Clears the descendant ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_catalog_id_terms = property(fdel=clear_descendant_catalog_id_terms)

    @abc.abstractmethod
    def supports_descendant_catalog_query(self):
        """Tests if a ``CatalogQuery`` is available.

        :return: ``true`` if a catalog query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_catalog_query(self):
        """Gets the query for a catalog.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the catalog query
        :rtype: ``osid.cataloging.CatalogQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_catalog_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_catalog_query()`` is ``true``.*

        """
        return  # osid.cataloging.CatalogQuery

    descendant_catalog_query = property(fget=get_descendant_catalog_query)

    @abc.abstractmethod
    def match_any_descendant_catalog(self, match):
        """Matches catalogs with any descendant.

        :param match: ``true`` to match catalogs with any descendant, ``false`` to match leaf catalogs
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_catalog_terms(self):
        """Clears the descendant query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_catalog_terms = property(fdel=clear_descendant_catalog_terms)

    @abc.abstractmethod
    def get_catalog_query_record(self, catalog_record_type):
        """Gets the catalog query record corresponding to the given ``Catalog`` record ``Type``.

        Multiple record retrievals produce a boolean ``OR`` term.

        :param catalog_record_type: a catalog record type
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog query record
        :rtype: ``osid.cataloging.records.CatalogQueryRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogQueryRecord
