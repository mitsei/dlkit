"""repository.queries"""
# pylint: disable=too-many-lines,too-many-ancestors,too-many-public-methods

from ...abstract_osid.repository import queries as abc_repository_queries
from ..osid import queries as osid_queries


class AssetQuery(abc_repository_queries.AssetQuery,
                 osid_queries.OsidObjectQuery,
                 osid_queries.OsidAggregateableQuery,
                 osid_queries.OsidSourceableQuery):
    """This is the query for searching assets.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``. The query record is
    identified by the ``Asset Type``.

    """
    def __init__(self):
        super(AssetQuery, self).__init__()

    def match_title(self, title=None, string_match_type=None, match=None):
        """Adds a title for this query.

        arg:    title (string): title string to match
        arg:    string_match_type (osid.type.Type): the string match
                type
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``title`` not of ``string_match_type``
        raise:  NullArgument - ``title`` or ``string_match_type`` is
                ``null``
        raise:  Unsupported -
                ``supports_string_match_type(string_match_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_title(self, match=None):
        """Matches a title that has any value.

        arg:    match (boolean): ``true`` to match assets with any
                title, ``false`` to match assets with no title
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_title_terms(self):
        """Clears the title terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    title_terms = property(fdel=clear_title_terms)

    def match_public_domain(self, public_domain=None):
        """Matches assets marked as public domain.

        arg:    public_domain (boolean): public domain flag
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_public_domain(self, match=None):
        """Matches assets with any public domain value.

        arg:    match (boolean): ``true`` to match assets with any
                public domain value, ``false`` to match assets with no
                public domain value
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_public_domain_terms(self):
        """Clears the public domain terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    public_domain_terms = property(fdel=clear_public_domain_terms)

    def match_copyright(self, copyright_=None, string_match_type=None, match=None):
        """Adds a copyright for this query.

        arg:    copyright (string): copyright string to match
        arg:    string_match_type (osid.type.Type): the string match
                type
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``copyright`` not of
                ``string_match_type``
        raise:  NullArgument - ``copyright`` or ``string_match_type`` is
                ``null``
        raise:  Unsupported -
                ``supports_string_match_type(string_match_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_copyright(self, match=None):
        """Matches assets with any copyright statement.

        arg:    match (boolean): ``true`` to match assets with any
                copyright value, ``false`` to match assets with no
                copyright value
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_copyright_terms(self):
        """Clears the copyright terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_terms = property(fdel=clear_copyright_terms)

    def match_copyright_registration(self,
                                     registration=None,
                                     string_match_type=None,
                                     match=None):
        """Adds a copyright registration for this query.

        arg:    registration (string): copyright registration string to
                match
        arg:    string_match_type (osid.type.Type): the string match
                type
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``registration`` not of
                ``string_match_type``
        raise:  NullArgument - ``registration`` or ``string_match_type``
                is ``null``
        raise:  Unsupported -
                ``supports_string_match_type(string_match_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_copyright_registration(self, match=None):
        """Matches assets with any copyright registration.

        arg:    match (boolean): ``true`` to match assets with any
                copyright registration value, ``false`` to match assets
                with no copyright registration value
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_copyright_registration_terms(self):
        """Clears the copyright registration terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_registration_terms = property(fdel=clear_copyright_registration_terms)

    def match_distribute_verbatim(self, distributable=None):
        """Matches assets marked as distributable.

        arg:    distributable (boolean): distribute verbatim rights flag
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_distribute_verbatim_terms(self):
        """Clears the distribute verbatim terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_verbatim_terms = property(fdel=clear_distribute_verbatim_terms)

    def match_distribute_alterations(self, alterable=None):
        """Matches assets that whose alterations can be distributed.

        arg:    alterable (boolean): distribute alterations rights flag
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_distribute_alterations_terms(self):
        """Clears the distribute alterations terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_alterations_terms = property(fdel=clear_distribute_alterations_terms)

    def match_distribute_compositions(self, composable=None):
        """Matches assets that can be distributed as part of other compositions.

        arg:    composable (boolean): distribute compositions rights
                flag
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_distribute_compositions_terms(self):
        """Clears the distribute compositions terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_compositions_terms = property(fdel=clear_distribute_compositions_terms)

    def match_source_id(self, source_id=None, match=None):
        """Sets the source ``Id`` for this query.

        arg:    source_id (osid.id.Id): the source ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``source_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_source_id_terms(self):
        """Clears the source ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_id_terms = property(fdel=clear_source_id_terms)

    def supports_source_query(self):
        """Tests if a ``ResourceQuery`` is available for the source.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_source_query(self):
        """Gets the query for the source.

        Multiple queries can be retrieved for a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the source query
        raise:  Unimplemented - ``supports_source_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_source_query()`` is ``true``.*

        """
        pass

    source_query = property(fget=get_source_query)

    def match_any_source(self, match=None):
        """Matches assets with any source.

        arg:    match (boolean): ``true`` to match assets with any
                source, ``false`` to match assets with no sources
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_source_terms(self):
        """Clears the source terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_terms = property(fdel=clear_source_terms)

    def match_created_date(self, start=None, end=None, match=None):
        """Match assets that are created between the specified time period.

        arg:    start (osid.calendaring.DateTime): start time of the
                query
        arg:    end (osid.calendaring.DateTime): end time of the query
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``end`` is les than ``start``
        raise:  NullArgument - ``start`` or ``end`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_created_date(self, match=None):
        """Matches assets with any creation time.

        arg:    match (boolean): ``true`` to match assets with any
                created time, ``false`` to match assets with no cerated
                time
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_created_date_terms(self):
        """Clears the created time terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    created_date_terms = property(fdel=clear_created_date_terms)

    def match_published(self, published=None):
        """Marks assets that are marked as published.

        arg:    published (boolean): published flag
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_published_terms(self):
        """Clears the published terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_terms = property(fdel=clear_published_terms)

    def match_published_date(self, start=None, end=None, match=None):
        """Match assets that are published between the specified time period.

        arg:    start (osid.calendaring.DateTime): start time of the
                query
        arg:    end (osid.calendaring.DateTime): end time of the query
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``end`` is les than ``start``
        raise:  NullArgument - ``start`` or ``end`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_published_date(self, match=None):
        """Matches assets with any published time.

        arg:    match (boolean): ``true`` to match assets with any
                published time, ``false`` to match assets with no
                published time
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_published_date_terms(self):
        """Clears the published time terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_date_terms = property(fdel=clear_published_date_terms)

    def match_principal_credit_string(self,
                                      credit=None,
                                      string_match_type=None,
                                      match=None):
        """Adds a principal credit string for this query.

        arg:    credit (string): credit string to match
        arg:    string_match_type (osid.type.Type): the string match
                type
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``credit`` not of
                ``string_match_type``
        raise:  NullArgument - ``credit`` or ``string_match_type`` is
                ``null``
        raise:  Unsupported -
                ``supports_string_match_type(string_match_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_principal_credit_string(self, match=None):
        """Matches a principal credit string that has any value.

        arg:    match (boolean): ``true`` to match assets with any
                principal credit string, ``false`` to match assets with
                no principal credit string
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_principal_credit_string_terms(self):
        """Clears the principal credit string terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    principal_credit_string_terms = property(fdel=clear_principal_credit_string_terms)

    def match_temporal_coverage(self, start=None, end=None, match=None):
        """Match assets that whose coverage falls between the specified time
        period inclusive.

        arg:    start (osid.calendaring.DateTime): start time of the
                query
        arg:    end (osid.calendaring.DateTime): end time of the query
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``end`` is less than ``start``
        raise:  NullArgument - ``start`` or ``end`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_temporal_coverage(self, match=None):
        """Matches assets with any temporal coverage.

        arg:    match (boolean): ``true`` to match assets with any
                temporal coverage, ``false`` to match assets with no
                temporal coverage
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_temporal_coverage_terms(self):
        """Clears the temporal coverage terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    temporal_coverage_terms = property(fdel=clear_temporal_coverage_terms)

    def match_location_id(self, location_id=None, match=None):
        """Sets the location ``Id`` for this query of spatial coverage.

        arg:    location_id (osid.id.Id): the location ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``location_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_location_id_terms(self):
        """Clears the location ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    location_id_terms = property(fdel=clear_location_id_terms)

    def supports_location_query(self):
        """Tests if a ``LocationQuery`` is available for the provider.

        return: (boolean) - ``true`` if a location query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_location_query(self):
        """Gets the query for a location.

        Multiple queries can be retrieved for a nested ``OR`` term.

        return: (osid.mapping.LocationQuery) - the location query
        raise:  Unimplemented - ``supports_location_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` is ``true``.*

        """
        pass

    location_query = property(fget=get_location_query)

    def match_any_location(self, match=None):
        """Matches assets with any provider.

        arg:    match (boolean): ``true`` to match assets with any
                location, ``false`` to match assets with no locations
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_location_terms(self):
        """Clears the location terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    location_terms = property(fdel=clear_location_terms)

    def match_spatial_coverage(self, spatial_unit=None, match=None):
        """Matches assets that are contained within the given spatial unit.

        arg:    spatial_unit (osid.mapping.SpatialUnit): the spatial
                unit
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``spatial_unit`` is ``null``
        raise:  Unsupported - ``spatial_unit`` is not suppoted
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_spatial_coverage_terms(self):
        """Clears the spatial coverage terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_coverage_terms = property(fdel=clear_spatial_coverage_terms)

    def match_spatial_coverage_overlap(self, spatial_unit=None, match=None):
        """Matches assets that overlap or touch the given spatial unit.

        arg:    spatial_unit (osid.mapping.SpatialUnit): the spatial
                unit
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``spatial_unit`` is ``null``
        raise:  Unsupported - ``spatial_unit`` is not suppoted
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_spatial_coverage(self, match=None):
        """Matches assets with no spatial coverage.

        arg:    match (boolean): ``true`` to match assets with any
                spatial coverage, ``false`` to match assets with no
                spatial coverage
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_spatial_coverage_overlap_terms(self):
        """Clears the spatial coverage overlap terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_coverage_overlap_terms = property(fdel=clear_spatial_coverage_overlap_terms)

    def match_asset_content_id(self, asset_content_id=None, match=None):
        """Sets the asset content ``Id`` for this query.

        arg:    asset_content_id (osid.id.Id): the asset content ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``asset_content_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_asset_content_id_terms(self):
        """Clears the asset content ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_content_id_terms = property(fdel=clear_asset_content_id_terms)

    def supports_asset_content_query(self):
        """Tests if an ``AssetContentQuery`` is available.

        return: (boolean) - ``true`` if an asset content query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_asset_content_query(self):
        """Gets the query for the asset content.

        Multiple queries can be retrieved for a nested ``OR`` term.

        return: (osid.repository.AssetContentQuery) - the asset contents
                query
        raise:  Unimplemented - ``supports_asset_content_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_content_query()`` is ``true``.*

        """
        pass

    asset_content_query = property(fget=get_asset_content_query)

    def match_any_asset_content(self, match=None):
        """Matches assets with any content.

        arg:    match (boolean): ``true`` to match assets with any
                content, ``false`` to match assets with no content
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_asset_content_terms(self):
        """Clears the asset content terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_content_terms = property(fdel=clear_asset_content_terms)

    def match_composition_id(self, composition_id=None, match=None):
        """Sets the composition ``Id`` for this query to match assets that
        are a part of the composition.

        arg:    composition_id (osid.id.Id): the composition ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``composition_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_composition_id_terms(self):
        """Clears the composition ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_id_terms = property(fdel=clear_composition_id_terms)

    def supports_composition_query(self):
        """Tests if a ``CompositionQuery`` is available.

        return: (boolean) - ``true`` if a composition query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_composition_query(self):
        """Gets the query for a composition.

        Multiple queries can be retrieved for a nested ``OR`` term.

        return: (osid.repository.CompositionQuery) - the composition
                query
        raise:  Unimplemented - ``supports_composition_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        pass

    composition_query = property(fget=get_composition_query)

    def match_any_composition(self, match=None):
        """Matches assets with any composition mappings.

        arg:    match (boolean): ``true`` to match assets with any
                composition, ``false`` to match assets with no
                composition mappings
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_composition_terms(self):
        """Clears the composition terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_terms = property(fdel=clear_composition_terms)

    def match_repository_id(self, repository_id=None, match=None):
        """Sets the repository ``Id`` for this query.

        arg:    repository_id (osid.id.Id): the repository ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_repository_id_terms(self):
        """Clears the repository ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    repository_id_terms = property(fdel=clear_repository_id_terms)

    def supports_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        return: (boolean) - ``true`` if a repository query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_repository_query(self):
        """Gets the query for a repository.

        Multiple queries can be retrieved for a nested ``OR`` term.

        return: (osid.repository.RepositoryQuery) - the repository query
        raise:  Unimplemented - ``supports_repository_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_query()`` is ``true``.*

        """
        pass

    repository_query = property(fget=get_repository_query)

    def clear_repository_terms(self):
        """Clears the repository terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    repository_terms = property(fdel=clear_repository_terms)

    def get_asset_query_record(self, asset_record_type=None):
        """Gets the asset query record corresponding to the given ``Asset`` record ``Type``.

        Multiuple retrievals produce a nested ``OR`` term.

        arg:    asset_record_type (osid.type.Type): an asset record type
        return: (osid.repository.records.AssetQueryRecord) - the asset
                query record
        raise:  NullArgument - ``asset_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(asset_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssetContentQuery(abc_repository_queries.AssetContentQuery,
                        osid_queries.OsidObjectQuery,
                        osid_queries.OsidSubjugateableQuery):
    """This is the query for searching asset contents.

    Each method forms an ``AND`` term while multiple invocations of the
    same method produce a nested ``OR``.

    """
    def __init__(self):
        super(AssetContentQuery, self).__init__()

    def match_accessibility_type(self, accessibility_type=None, match=None):
        """Sets the accessibility types for this query.

        Supplying multiple types behaves like a boolean OR among the
        elements.

        arg:    accessibility_type (osid.type.Type): an
                accessibilityType
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``accessibility_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_accessibility_type(self, match=None):
        """Matches asset content that has any accessibility type.

        arg:    match (boolean): ``true`` to match content with any
                accessibility type, ``false`` to match content with no
                accessibility type
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_accessibility_type_terms(self):
        """Clears the accessibility terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    accessibility_type_terms = property(fdel=clear_accessibility_type_terms)

    def match_data_length(self, low=None, high=None, match=None):
        """Matches content whose length of the data in bytes are inclusive
        of the given range.

        arg:    low (cardinal): low range
        arg:    high (cardinal): high range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_data_length(self, match=None):
        """Matches content that has any data length.

        arg:    match (boolean): ``true`` to match content with any data
                length, ``false`` to match content with no data length
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_data_length_terms(self):
        """Clears the data length terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    data_length_terms = property(fdel=clear_data_length_terms)

    def match_data(self, data=None, match=None, partial=None):
        """Matches data in this content.

        arg:    data (byte[]): list of matching strings
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        arg:    partial (boolean): ``true`` for a partial match,
                ``false`` for a complete match
        raise:  NullArgument - ``data`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_data(self, match=None):
        """Matches content that has any data.

        arg:    match (boolean): ``true`` to match content with any
                data, ``false`` to match content with no data
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_data_terms(self):
        """Clears the data terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    data_terms = property(fdel=clear_data_terms)

    def match_url(self, url=None, string_match_type=None, match=None):
        """Sets the url for this query.

        Supplying multiple strings behaves like a boolean ``OR`` among
        the elements each which must correspond to the
        ``stringMatchType``.

        arg:    url (string): url string to match
        arg:    string_match_type (osid.type.Type): the string match
                type
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``url`` not of ``string_match_type``
        raise:  NullArgument - ``url`` or ``string_match_type`` is
                ``null``
        raise:  Unsupported - ``supports_string_match_type(url)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def match_any_url(self, match=None):
        """Matches content that has any url.

        arg:    match (boolean): ``true`` to match content with any url,
                ``false`` to match content with no url
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_url_terms(self):
        """Clears the url terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    url_terms = property(fdel=clear_url_terms)

    def get_asset_content_query_record(self, asset_content_record_type=None):
        """Gets the asset content query record corresponding to the given
        ``AssetContent`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        arg:    asset_content_record_type (osid.type.Type): an asset
                content record type
        return: (osid.repository.records.AssetContentQueryRecord) - the
                asset content query record
        raise:  NullArgument - ``asset_content_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(asset_content_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class RepositoryQuery(abc_repository_queries.RepositoryQuery,
                      osid_queries.OsidCatalogQuery):
    """This is the query for searching repositories.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def __init__(self):
        super(RepositoryQuery, self).__init__()

    def match_asset_id(self, asset_id=None, match=None):
        """Sets the asset ``Id`` for this query.

        arg:    asset_id (osid.id.Id): an asset ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``asset_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_asset_id_terms(self):
        """Clears the asset ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_id_terms = property(fdel=clear_asset_id_terms)

    def supports_asset_query(self):
        """Tests if an ``AssetQuery`` is available.

        return: (boolean) - ``true`` if an asset query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_asset_query(self):
        """Gets the query for an asset.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.repository.AssetQuery) - the asset query
        raise:  Unimplemented - ``supports_asset_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` is ``true``.*

        """
        pass

    asset_query = property(fget=get_asset_query)

    def match_any_asset(self, match=None):
        """Matches repositories that has any asset mapping.

        arg:    match (boolean): ``true`` to match repositories with any
                asset, ``false`` to match repositories with no asset
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_asset_terms(self):
        """Clears the asset terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_terms = property(fdel=clear_asset_terms)

    def match_composition_id(self, composition_id=None, match=None):
        """Sets the composition ``Id`` for this query.

        arg:    composition_id (osid.id.Id): a composition ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``composition_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_composition_id_terms(self):
        """Clears the composition ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_id_terms = property(fdel=clear_composition_id_terms)

    def supports_composition_query(self):
        """Tests if a ``CompositionQuery`` is available.

        return: (boolean) - ``true`` if a composition query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_composition_query(self):
        """Gets the query for a composition.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.repository.CompositionQuery) - the composition
                query
        raise:  Unimplemented - ``supports_composition_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        pass

    composition_query = property(fget=get_composition_query)

    def match_any_composition(self, match=None):
        """Matches repositories that has any composition mapping.

        arg:    match (boolean): ``true`` to match repositories with any
                composition, ``false`` to match repositories with no
                composition
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_composition_terms(self):
        """Clears the composition terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_terms = property(fdel=clear_composition_terms)

    def match_ancestor_repository_id(self, repository_id=None, match=None):
        """Sets the repository ``Id`` for this query to match repositories
        that have the specified repository as an ancestor.

        arg:    repository_id (osid.id.Id): a repository ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_ancestor_repository_id_terms(self):
        """Clears the ancestor repository ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_repository_id_terms = property(fdel=clear_ancestor_repository_id_terms)

    def supports_ancestor_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        return: (boolean) - ``true`` if a repository query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_ancestor_repository_query(self):
        """Gets the query for a repository.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.repository.RepositoryQuery) - the repository query
        raise:  Unimplemented - ``supports_ancestor_repository_query()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_repository_query()`` is ``true``.*

        """
        pass

    ancestor_repository_query = property(fget=get_ancestor_repository_query)

    def match_any_ancestor_repository(self, match=None):
        """Matches repositories with any ancestor.

        arg:    match (boolean): ``true`` to match repositories with any
                ancestor, ``false`` to match root repositories
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_ancestor_repository_terms(self):
        """Clears the ancestor repository terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_repository_terms = property(fdel=clear_ancestor_repository_terms)

    def match_descendant_repository_id(self, repository_id=None, match=None):
        """Sets the repository ``Id`` for this query to match repositories
        that have the specified repository as a descendant.

        arg:    repository_id (osid.id.Id): a repository ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_descendant_repository_id_terms(self):
        """Clears the descendant repository ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_repository_id_terms = property(fdel=clear_descendant_repository_id_terms)

    def supports_descendant_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        return: (boolean) - ``true`` if a repository query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_descendant_repository_query(self):
        """Gets the query for a repository.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.repository.RepositoryQuery) - the repository query
        raise:  Unimplemented -
                ``supports_descendant_repository_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_repository_query()`` is ``true``.*

        """
        pass

    descendant_repository_query = property(fget=get_descendant_repository_query)

    def match_any_descendant_repository(self, match=None):
        """Matches repositories with any descendant.

        arg:    match (boolean): ``true`` to match repositories with any
                descendant, ``false`` to match leaf repositories
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_descendant_repository_terms(self):
        """Clears the descendant repository terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_repository_terms = property(fdel=clear_descendant_repository_terms)

    def get_repository_query_record(self, repository_record_type=None):
        """Gets the repository query record corresponding to the given
        ``Repository`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        arg:    repository_record_type (osid.type.Type): a repository
                record type
        return: (osid.repository.records.RepositoryQueryRecord) - the
                repository query record
        raise:  NullArgument - ``repository_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(repository_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass
