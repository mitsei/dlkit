"""JSON implementations of cataloging queries."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..id.objects import IdList
from ..osid import queries as osid_queries
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.cataloging import queries as abc_cataloging_queries
from dlkit.abstract_osid.osid import errors


class CatalogQuery(abc_cataloging_queries.CatalogQuery, osid_queries.OsidCatalogQuery):
    """This is the query for searching catalogs.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produces a nested ``OR``.

    """
    def __init__(self, runtime):
        self._runtime = runtime
        record_type_data_sets = get_registry('CATALOG_RECORD_TYPES', runtime)
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_queries.OsidCatalogQuery.__init__(self, runtime)

    def _get_descendant_catalog_ids(self, catalog_id):
        hm = self._get_provider_manager('HIERARCHY')
        hts = hm.get_hierarchy_traversal_session_for_hierarchy(
            Id(authority='CATALOGING',
               namespace='CATALOG',
               identifier='CATALOG')
        )  # What about the Proxy?
        descendants = []
        if hts.has_children(catalog_id):
            for child_id in hts.get_children(catalog_id):
                descendants += list(self._get_descendant_catalog_ids(child_id))
                descendants.append(child_id)
        return IdList(descendants)

    @utilities.arguments_not_none
    def match_id(self, id_, match):
        """Matches an ``Id`` in this catalog.

        Multiple Ids are treated as a boolean ``OR``.

        arg:    id (osid.id.Id): ``Id`` to match
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def match_any_id(self, match):
        """Matches catalogs that have any ``Id`` mapping.

        arg:    match (boolean): ``true`` to match catalogs with any
                ``Id`` mapping, ``false`` to match catalogs with no
                ``Id`` mapping
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_id_terms(self):
        """Clears the ``Id`` query terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('id')

    id_terms = property(fdel=clear_id_terms)

    @utilities.arguments_not_none
    def match_ancestor_catalog_id(self, catalog_id, match):
        """Sets the catalog ``Id`` for this query to match catalogs that have the specified catalog as an ancestor.

        arg:    catalog_id (osid.id.Id): a catalog ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``catalog_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_ancestor_catalog_id_terms(self):
        """Clears the ancestor ``Id`` query terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('ancestorCatalogId')

    ancestor_catalog_id_terms = property(fdel=clear_ancestor_catalog_id_terms)

    def supports_ancestor_catalog_query(self):
        """Tests if a ``CatalogQuery`` is available.

        return: (boolean) - ``true`` if a catalog query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_ancestor_catalog_query(self):
        """Gets the query for a catalog.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.cataloging.CatalogQuery) - the catalog query
        raise:  Unimplemented - ``supports_ancestor_catalog_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_catalog_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    ancestor_catalog_query = property(fget=get_ancestor_catalog_query)

    @utilities.arguments_not_none
    def match_any_ancestor_catalog(self, match):
        """Matches catalogs with any ancestor.

        arg:    match (boolean): ``true`` to match catalogs with any
                ancestor, ``false`` to match root catalogs
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_ancestor_catalog_terms(self):
        """Clears the ancestor query terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('ancestorCatalog')

    ancestor_catalog_terms = property(fdel=clear_ancestor_catalog_terms)

    @utilities.arguments_not_none
    def match_descendant_catalog_id(self, catalog_id, match):
        """Sets the catalog ``Id`` for this query to match catalogs that have the specified catalog as an descendant.

        arg:    catalog_id (osid.id.Id): a catalog ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``catalog_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_descendant_catalog_id_terms(self):
        """Clears the descendant ``Id`` query terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('descendantCatalogId')

    descendant_catalog_id_terms = property(fdel=clear_descendant_catalog_id_terms)

    def supports_descendant_catalog_query(self):
        """Tests if a ``CatalogQuery`` is available.

        return: (boolean) - ``true`` if a catalog query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_descendant_catalog_query(self):
        """Gets the query for a catalog.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.cataloging.CatalogQuery) - the catalog query
        raise:  Unimplemented - ``supports_descendant_catalog_query()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_catalog_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    descendant_catalog_query = property(fget=get_descendant_catalog_query)

    @utilities.arguments_not_none
    def match_any_descendant_catalog(self, match):
        """Matches catalogs with any descendant.

        arg:    match (boolean): ``true`` to match catalogs with any
                descendant, ``false`` to match leaf catalogs
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_descendant_catalog_terms(self):
        """Clears the descendant query terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('descendantCatalog')

    descendant_catalog_terms = property(fdel=clear_descendant_catalog_terms)

    @utilities.arguments_not_none
    def get_catalog_query_record(self, catalog_record_type):
        """Gets the catalog query record corresponding to the given ``Catalog`` record ``Type``.

        Multiple record retrievals produce a boolean ``OR`` term.

        arg:    catalog_record_type (osid.type.Type): a catalog record
                type
        return: (osid.cataloging.records.CatalogQueryRecord) - the
                catalog query record
        raise:  NullArgument - ``catalog_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(catalog_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
