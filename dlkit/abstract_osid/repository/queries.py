"""Implementations of repository abstract base class queries."""
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


class AssetQuery:
    """This is the query for searching assets.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``. The query record is
    identified by the ``Asset Type``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_title(self, title, string_match_type, match):
        """Adds a title for this query.

        :param title: title string to match
        :type title: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``title`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``title`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_title(self, match):
        """Matches a title that has any value.

        :param match: ``true`` to match assets with any title, ``false`` to match assets with no title
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_title_terms(self):
        """Clears the title terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    title_terms = property(fdel=clear_title_terms)

    @abc.abstractmethod
    def match_public_domain(self, public_domain):
        """Matches assets marked as public domain.

        :param public_domain: public domain flag
        :type public_domain: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_public_domain(self, match):
        """Matches assets with any public domain value.

        :param match: ``true`` to match assets with any public domain value, ``false`` to match assets with no public domain value
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_public_domain_terms(self):
        """Clears the public domain terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    public_domain_terms = property(fdel=clear_public_domain_terms)

    @abc.abstractmethod
    def match_copyright(self, copyright_, string_match_type, match):
        """Adds a copyright for this query.

        :param copyright: copyright string to match
        :type copyright: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``copyright`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``copyright`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_copyright(self, match):
        """Matches assets with any copyright statement.

        :param match: ``true`` to match assets with any copyright value, ``false`` to match assets with no copyright value
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_copyright_terms(self):
        """Clears the copyright terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_terms = property(fdel=clear_copyright_terms)

    @abc.abstractmethod
    def match_copyright_registration(self, registration, string_match_type, match):
        """Adds a copyright registration for this query.

        :param registration: copyright registration string to match
        :type registration: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``registration`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``registration`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_copyright_registration(self, match):
        """Matches assets with any copyright registration.

        :param match: ``true`` to match assets with any copyright registration value, ``false`` to match assets with no copyright registration value
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_copyright_registration_terms(self):
        """Clears the copyright registration terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_registration_terms = property(fdel=clear_copyright_registration_terms)

    @abc.abstractmethod
    def match_distribute_verbatim(self, distributable):
        """Matches assets marked as distributable.

        :param distributable: distribute verbatim rights flag
        :type distributable: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distribute_verbatim_terms(self):
        """Clears the distribute verbatim terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_verbatim_terms = property(fdel=clear_distribute_verbatim_terms)

    @abc.abstractmethod
    def match_distribute_alterations(self, alterable):
        """Matches assets that whose alterations can be distributed.

        :param alterable: distribute alterations rights flag
        :type alterable: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distribute_alterations_terms(self):
        """Clears the distribute alterations terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_alterations_terms = property(fdel=clear_distribute_alterations_terms)

    @abc.abstractmethod
    def match_distribute_compositions(self, composable):
        """Matches assets that can be distributed as part of other compositions.

        :param composable: distribute compositions rights flag
        :type composable: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distribute_compositions_terms(self):
        """Clears the distribute compositions terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distribute_compositions_terms = property(fdel=clear_distribute_compositions_terms)

    @abc.abstractmethod
    def match_source_id(self, source_id, match):
        """Sets the source ``Id`` for this query.

        :param source_id: the source ``Id``
        :type source_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_source_id_terms(self):
        """Clears the source ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_id_terms = property(fdel=clear_source_id_terms)

    @abc.abstractmethod
    def supports_source_query(self):
        """Tests if a ``ResourceQuery`` is available for the source.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_source_query(self):
        """Gets the query for the source.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the source query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_source_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_source_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    source_query = property(fget=get_source_query)

    @abc.abstractmethod
    def match_any_source(self, match):
        """Matches assets with any source.

        :param match: ``true`` to match assets with any source, ``false`` to match assets with no sources
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_source_terms(self):
        """Clears the source terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_terms = property(fdel=clear_source_terms)

    @abc.abstractmethod
    def match_created_date(self, start, end, match):
        """Match assets that are created between the specified time period.

        :param start: start time of the query
        :type start: ``osid.calendaring.DateTime``
        :param end: end time of the query
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is les than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_created_date(self, match):
        """Matches assets with any creation time.

        :param match: ``true`` to match assets with any created time, ``false`` to match assets with no cerated time
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_created_date_terms(self):
        """Clears the created time terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    created_date_terms = property(fdel=clear_created_date_terms)

    @abc.abstractmethod
    def match_published(self, published):
        """Marks assets that are marked as published.

        :param published: published flag
        :type published: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_published_terms(self):
        """Clears the published terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_terms = property(fdel=clear_published_terms)

    @abc.abstractmethod
    def match_published_date(self, start, end, match):
        """Match assets that are published between the specified time period.

        :param start: start time of the query
        :type start: ``osid.calendaring.DateTime``
        :param end: end time of the query
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is les than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_published_date(self, match):
        """Matches assets with any published time.

        :param match: ``true`` to match assets with any published time, ``false`` to match assets with no published time
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_published_date_terms(self):
        """Clears the published time terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    published_date_terms = property(fdel=clear_published_date_terms)

    @abc.abstractmethod
    def match_principal_credit_string(self, credit, string_match_type, match):
        """Adds a principal credit string for this query.

        :param credit: credit string to match
        :type credit: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``credit`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``credit`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_principal_credit_string(self, match):
        """Matches a principal credit string that has any value.

        :param match: ``true`` to match assets with any principal credit string, ``false`` to match assets with no principal credit string
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_principal_credit_string_terms(self):
        """Clears the principal credit string terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    principal_credit_string_terms = property(fdel=clear_principal_credit_string_terms)

    @abc.abstractmethod
    def match_temporal_coverage(self, start, end, match):
        """Match assets that whose coverage falls between the specified time period inclusive.

        :param start: start time of the query
        :type start: ``osid.calendaring.DateTime``
        :param end: end time of the query
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_temporal_coverage(self, match):
        """Matches assets with any temporal coverage.

        :param match: ``true`` to match assets with any temporal coverage, ``false`` to match assets with no temporal coverage
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_temporal_coverage_terms(self):
        """Clears the temporal coverage terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    temporal_coverage_terms = property(fdel=clear_temporal_coverage_terms)

    @abc.abstractmethod
    def match_location_id(self, location_id, match):
        """Sets the location ``Id`` for this query of spatial coverage.

        :param location_id: the location ``Id``
        :type location_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_location_id_terms(self):
        """Clears the location ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    location_id_terms = property(fdel=clear_location_id_terms)

    @abc.abstractmethod
    def supports_location_query(self):
        """Tests if a ``LocationQuery`` is available for the provider.

        :return: ``true`` if a location query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_query(self):
        """Gets the query for a location.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` is ``true``.*

        """
        return  # osid.mapping.LocationQuery

    location_query = property(fget=get_location_query)

    @abc.abstractmethod
    def match_any_location(self, match):
        """Matches assets with any provider.

        :param match: ``true`` to match assets with any location, ``false`` to match assets with no locations
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_location_terms(self):
        """Clears the location terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    location_terms = property(fdel=clear_location_terms)

    @abc.abstractmethod
    def match_spatial_coverage(self, spatial_unit, match):
        """Matches assets that are contained within the given spatial unit.

        :param spatial_unit: the spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``Unsupported`` -- ``spatial_unit`` is not suppoted

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_spatial_coverage_terms(self):
        """Clears the spatial coverage terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_coverage_terms = property(fdel=clear_spatial_coverage_terms)

    @abc.abstractmethod
    def match_spatial_coverage_overlap(self, spatial_unit, match):
        """Matches assets that overlap or touch the given spatial unit.

        :param spatial_unit: the spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``Unsupported`` -- ``spatial_unit`` is not suppoted

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_spatial_coverage(self, match):
        """Matches assets with no spatial coverage.

        :param match: ``true`` to match assets with any spatial coverage, ``false`` to match assets with no spatial coverage
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_spatial_coverage_overlap_terms(self):
        """Clears the spatial coverage overlap terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_coverage_overlap_terms = property(fdel=clear_spatial_coverage_overlap_terms)

    @abc.abstractmethod
    def match_asset_content_id(self, asset_content_id, match):
        """Sets the asset content ``Id`` for this query.

        :param asset_content_id: the asset content ``Id``
        :type asset_content_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_content_id_terms(self):
        """Clears the asset content ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_content_id_terms = property(fdel=clear_asset_content_id_terms)

    @abc.abstractmethod
    def supports_asset_content_query(self):
        """Tests if an ``AssetContentQuery`` is available.

        :return: ``true`` if an asset content query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_content_query(self):
        """Gets the query for the asset content.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the asset contents query
        :rtype: ``osid.repository.AssetContentQuery``
        :raise: ``Unimplemented`` -- ``supports_asset_content_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_content_query()`` is ``true``.*

        """
        return  # osid.repository.AssetContentQuery

    asset_content_query = property(fget=get_asset_content_query)

    @abc.abstractmethod
    def match_any_asset_content(self, match):
        """Matches assets with any content.

        :param match: ``true`` to match assets with any content, ``false`` to match assets with no content
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_content_terms(self):
        """Clears the asset content terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_content_terms = property(fdel=clear_asset_content_terms)

    @abc.abstractmethod
    def match_composition_id(self, composition_id, match):
        """Sets the composition ``Id`` for this query to match assets that are a part of the composition.

        :param composition_id: the composition ``Id``
        :type composition_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_composition_id_terms(self):
        """Clears the composition ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_id_terms = property(fdel=clear_composition_id_terms)

    @abc.abstractmethod
    def supports_composition_query(self):
        """Tests if a ``CompositionQuery`` is available.

        :return: ``true`` if a composition query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_composition_query(self):
        """Gets the query for a composition.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        return  # osid.repository.CompositionQuery

    composition_query = property(fget=get_composition_query)

    @abc.abstractmethod
    def match_any_composition(self, match):
        """Matches assets with any composition mappings.

        :param match: ``true`` to match assets with any composition, ``false`` to match assets with no composition mappings
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_composition_terms(self):
        """Clears the composition terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_terms = property(fdel=clear_composition_terms)

    @abc.abstractmethod
    def match_repository_id(self, repository_id, match):
        """Sets the repository ``Id`` for this query.

        :param repository_id: the repository ``Id``
        :type repository_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_repository_id_terms(self):
        """Clears the repository ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    repository_id_terms = property(fdel=clear_repository_id_terms)

    @abc.abstractmethod
    def supports_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        :return: ``true`` if a repository query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_repository_query(self):
        """Gets the query for a repository.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``
        :raise: ``Unimplemented`` -- ``supports_repository_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_query()`` is ``true``.*

        """
        return  # osid.repository.RepositoryQuery

    repository_query = property(fget=get_repository_query)

    @abc.abstractmethod
    def clear_repository_terms(self):
        """Clears the repository terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    repository_terms = property(fdel=clear_repository_terms)

    @abc.abstractmethod
    def get_asset_query_record(self, asset_record_type):
        """Gets the asset query record corresponding to the given ``Asset`` record ``Type``.

        Multiuple retrievals produce a nested ``OR`` term.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the asset query record
        :rtype: ``osid.repository.records.AssetQueryRecord``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetQueryRecord


class AssetContentQuery:
    """This is the query for searching asset contents.

    Each method forms an ``AND`` term while multiple invocations of the
    same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_accessibility_type(self, accessibility_type, match):
        """Sets the accessibility types for this query.

        Supplying multiple types behaves like a boolean OR among the
        elements.

        :param accessibility_type: an accessibilityType
        :type accessibility_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``accessibility_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_accessibility_type(self, match):
        """Matches asset content that has any accessibility type.

        :param match: ``true`` to match content with any accessibility type, ``false`` to match content with no accessibility type
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_accessibility_type_terms(self):
        """Clears the accessibility terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    accessibility_type_terms = property(fdel=clear_accessibility_type_terms)

    @abc.abstractmethod
    def match_data_length(self, low, high, match):
        """Matches content whose length of the data in bytes are inclusive of the given range.

        :param low: low range
        :type low: ``cardinal``
        :param high: high range
        :type high: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_data_length(self, match):
        """Matches content that has any data length.

        :param match: ``true`` to match content with any data length, ``false`` to match content with no data length
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_data_length_terms(self):
        """Clears the data length terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    data_length_terms = property(fdel=clear_data_length_terms)

    @abc.abstractmethod
    def match_data(self, data, match, partial):
        """Matches data in this content.

        :param data: list of matching strings
        :type data: ``byte[]``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :param partial: ``true`` for a partial match, ``false`` for a complete match
        :type partial: ``boolean``
        :raise: ``NullArgument`` -- ``data`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_data(self, match):
        """Matches content that has any data.

        :param match: ``true`` to match content with any data, ``false`` to match content with no data
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_data_terms(self):
        """Clears the data terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    data_terms = property(fdel=clear_data_terms)

    @abc.abstractmethod
    def match_url(self, url, string_match_type, match):
        """Sets the url for this query.

        Supplying multiple strings behaves like a boolean ``OR`` among
        the elements each which must correspond to the
        ``stringMatchType``.

        :param url: url string to match
        :type url: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``url`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``url`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(url)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_url(self, match):
        """Matches content that has any url.

        :param match: ``true`` to match content with any url, ``false`` to match content with no url
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_url_terms(self):
        """Clears the url terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    url_terms = property(fdel=clear_url_terms)

    @abc.abstractmethod
    def get_asset_content_query_record(self, asset_content_record_type):
        """Gets the asset content query record corresponding to the given ``AssetContent`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param asset_content_record_type: an asset content record type
        :type asset_content_record_type: ``osid.type.Type``
        :return: the asset content query record
        :rtype: ``osid.repository.records.AssetContentQueryRecord``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetContentQueryRecord


class CompositionQuery:
    """This is the query for searching compositions.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_asset_id(self, asset_id, match):
        """Sets the asset ``Id`` for this query.

        :param asset_id: the asset ``Id``
        :type asset_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_id_terms(self):
        """Clears the asset ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_id_terms = property(fdel=clear_asset_id_terms)

    @abc.abstractmethod
    def supports_asset_query(self):
        """Tests if an ``AssetQuery`` is available.

        :return: ``true`` if an asset query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_query(self):
        """Gets the query for an asset.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuery

    asset_query = property(fget=get_asset_query)

    @abc.abstractmethod
    def match_any_asset(self, match):
        """Matches compositions that has any asset mapping.

        :param match: ``true`` to match compositions with any asset, ``false`` to match compositions with no asset
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_terms(self):
        """Clears the asset terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_terms = property(fdel=clear_asset_terms)

    @abc.abstractmethod
    def match_containing_composition_id(self, composition_id, match):
        """Sets the composition ``Id`` for this query to match compositions that have the specified composition as an ancestor.

        :param composition_id: a composition ``Id``
        :type composition_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_containing_composition_id_terms(self):
        """Clears the containing composition ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_composition_id_terms = property(fdel=clear_containing_composition_id_terms)

    @abc.abstractmethod
    def supports_containing_composition_query(self):
        """Tests if an ``CompositionQuery`` is available.

        :return: ``true`` if a composition query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_containing_composition_query(self):
        """Gets the query for a composition.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``Unimplemented`` -- ``supports_containing_composition_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_containing_composition_query()`` is ``true``.*

        """
        return  # osid.repository.CompositionQuery

    containing_composition_query = property(fget=get_containing_composition_query)

    @abc.abstractmethod
    def match_any_containing_composition(self, match):
        """Matches compositions with any ancestor.

        :param match: ``true`` to match composition with any ancestor, ``false`` to match root compositions
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_containing_composition_terms(self):
        """Clears the containing composition terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_composition_terms = property(fdel=clear_containing_composition_terms)

    @abc.abstractmethod
    def match_contained_composition_id(self, composition_id, match):
        """Sets the composition ``Id`` for this query to match compositions that contain the specified composition.

        :param composition_id: a composition ``Id``
        :type composition_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_contained_composition_id_terms(self):
        """Clears the contained composition ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    contained_composition_id_terms = property(fdel=clear_contained_composition_id_terms)

    @abc.abstractmethod
    def supports_contained_composition_query(self):
        """Tests if an ``CompositionQuery`` is available.

        :return: ``true`` if a composition query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_contained_composition_query(self):
        """Gets the query for a composition.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``Unimplemented`` -- ``supports_contained_composition_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_contained_composition_query()`` is ``true``.*

        """
        return  # osid.repository.CompositionQuery

    contained_composition_query = property(fget=get_contained_composition_query)

    @abc.abstractmethod
    def match_any_contained_composition(self, match):
        """Matches compositions that contain any other compositions.

        :param match: ``true`` to match composition with any descendant, ``false`` to match leaf compositions
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_contained_composition_terms(self):
        """Clears the contained composition terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    contained_composition_terms = property(fdel=clear_contained_composition_terms)

    @abc.abstractmethod
    def match_repository_id(self, repository_id, match):
        """Sets the repository ``Id`` for this query.

        :param repository_id: the repository ``Id``
        :type repository_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_repository_id_terms(self):
        """Clears the repository ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    repository_id_terms = property(fdel=clear_repository_id_terms)

    @abc.abstractmethod
    def supports_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        :return: ``true`` if a repository query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_repository_query(self):
        """Gets the query for a repository.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``
        :raise: ``Unimplemented`` -- ``supports_repository_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_query()`` is ``true``.*

        """
        return  # osid.repository.RepositoryQuery

    repository_query = property(fget=get_repository_query)

    @abc.abstractmethod
    def clear_repository_terms(self):
        """Clears the repository terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    repository_terms = property(fdel=clear_repository_terms)

    @abc.abstractmethod
    def get_composition_query_record(self, composition_record_type):
        """Gets the composition query record corresponding to the given ``Composition`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the composition query record
        :rtype: ``osid.repository.records.CompositionQueryRecord``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(composition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionQueryRecord


class RepositoryQuery:
    """This is the query for searching repositories.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_asset_id(self, asset_id, match):
        """Sets the asset ``Id`` for this query.

        :param asset_id: an asset ``Id``
        :type asset_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_id_terms(self):
        """Clears the asset ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_id_terms = property(fdel=clear_asset_id_terms)

    @abc.abstractmethod
    def supports_asset_query(self):
        """Tests if an ``AssetQuery`` is available.

        :return: ``true`` if an asset query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_query(self):
        """Gets the query for an asset.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuery

    asset_query = property(fget=get_asset_query)

    @abc.abstractmethod
    def match_any_asset(self, match):
        """Matches repositories that has any asset mapping.

        :param match: ``true`` to match repositories with any asset, ``false`` to match repositories with no asset
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_terms(self):
        """Clears the asset terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_terms = property(fdel=clear_asset_terms)

    @abc.abstractmethod
    def match_composition_id(self, composition_id, match):
        """Sets the composition ``Id`` for this query.

        :param composition_id: a composition ``Id``
        :type composition_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_composition_id_terms(self):
        """Clears the composition ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_id_terms = property(fdel=clear_composition_id_terms)

    @abc.abstractmethod
    def supports_composition_query(self):
        """Tests if a ``CompositionQuery`` is available.

        :return: ``true`` if a composition query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_composition_query(self):
        """Gets the query for a composition.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        return  # osid.repository.CompositionQuery

    composition_query = property(fget=get_composition_query)

    @abc.abstractmethod
    def match_any_composition(self, match):
        """Matches repositories that has any composition mapping.

        :param match: ``true`` to match repositories with any composition, ``false`` to match repositories with no composition
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_composition_terms(self):
        """Clears the composition terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    composition_terms = property(fdel=clear_composition_terms)

    @abc.abstractmethod
    def match_ancestor_repository_id(self, repository_id, match):
        """Sets the repository ``Id`` for this query to match repositories that have the specified repository as an ancestor.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_repository_id_terms(self):
        """Clears the ancestor repository ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_repository_id_terms = property(fdel=clear_ancestor_repository_id_terms)

    @abc.abstractmethod
    def supports_ancestor_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        :return: ``true`` if a repository query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_repository_query(self):
        """Gets the query for a repository.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_repository_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_repository_query()`` is ``true``.*

        """
        return  # osid.repository.RepositoryQuery

    ancestor_repository_query = property(fget=get_ancestor_repository_query)

    @abc.abstractmethod
    def match_any_ancestor_repository(self, match):
        """Matches repositories with any ancestor.

        :param match: ``true`` to match repositories with any ancestor, ``false`` to match root repositories
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_repository_terms(self):
        """Clears the ancestor repository terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_repository_terms = property(fdel=clear_ancestor_repository_terms)

    @abc.abstractmethod
    def match_descendant_repository_id(self, repository_id, match):
        """Sets the repository ``Id`` for this query to match repositories that have the specified repository as a descendant.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_repository_id_terms(self):
        """Clears the descendant repository ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_repository_id_terms = property(fdel=clear_descendant_repository_id_terms)

    @abc.abstractmethod
    def supports_descendant_repository_query(self):
        """Tests if a ``RepositoryQuery`` is available.

        :return: ``true`` if a repository query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_repository_query(self):
        """Gets the query for a repository.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_repository_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_repository_query()`` is ``true``.*

        """
        return  # osid.repository.RepositoryQuery

    descendant_repository_query = property(fget=get_descendant_repository_query)

    @abc.abstractmethod
    def match_any_descendant_repository(self, match):
        """Matches repositories with any descendant.

        :param match: ``true`` to match repositories with any descendant, ``false`` to match leaf repositories
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_repository_terms(self):
        """Clears the descendant repository terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_repository_terms = property(fdel=clear_descendant_repository_terms)

    @abc.abstractmethod
    def get_repository_query_record(self, repository_record_type):
        """Gets the repository query record corresponding to the given ``Repository`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository query record
        :rtype: ``osid.repository.records.RepositoryQueryRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositoryQueryRecord
