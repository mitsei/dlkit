"""Implementations of repository abstract base class query_inspectors."""
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


class AssetQueryInspector:
    """This is the query inspector for examining asset queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_title_terms(self):
        """Gets the title query terms.

        :return: the title terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    title_terms = property(fget=get_title_terms)

    @abc.abstractmethod
    def get_public_domain_terms(self):
        """Gets the public domain query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    public_domain_terms = property(fget=get_public_domain_terms)

    @abc.abstractmethod
    def get_copyright_terms(self):
        """Gets the copyright query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    copyright_terms = property(fget=get_copyright_terms)

    @abc.abstractmethod
    def get_copyright_registration_terms(self):
        """Gets the copyright registration query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    copyright_registration_terms = property(fget=get_copyright_registration_terms)

    @abc.abstractmethod
    def get_distribute_verbatim_terms(self):
        """Gets the verbatim distribution query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    distribute_verbatim_terms = property(fget=get_distribute_verbatim_terms)

    @abc.abstractmethod
    def get_distribute_alterations_terms(self):
        """Gets the alteration distribution query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    distribute_alterations_terms = property(fget=get_distribute_alterations_terms)

    @abc.abstractmethod
    def get_distribute_compositions_terms(self):
        """Gets the composition distribution query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    distribute_compositions_terms = property(fget=get_distribute_compositions_terms)

    @abc.abstractmethod
    def get_source_id_terms(self):
        """Gets the source ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    source_id_terms = property(fget=get_source_id_terms)

    @abc.abstractmethod
    def get_source_terms(self):
        """Gets the source query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    source_terms = property(fget=get_source_terms)

    @abc.abstractmethod
    def get_created_date_terms(self):
        """Gets the created time query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    created_date_terms = property(fget=get_created_date_terms)

    @abc.abstractmethod
    def get_published_terms(self):
        """Gets the published query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    published_terms = property(fget=get_published_terms)

    @abc.abstractmethod
    def get_published_date_terms(self):
        """Gets the published time query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    published_date_terms = property(fget=get_published_date_terms)

    @abc.abstractmethod
    def get_principal_credit_string_terms(self):
        """Gets the principal credit string query terms.

        :return: the principal credit string terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    principal_credit_string_terms = property(fget=get_principal_credit_string_terms)

    @abc.abstractmethod
    def get_temporal_coverage_terms(self):
        """Gets the temporal coverage query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    temporal_coverage_terms = property(fget=get_temporal_coverage_terms)

    @abc.abstractmethod
    def get_location_id_terms(self):
        """Gets the location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    location_id_terms = property(fget=get_location_id_terms)

    @abc.abstractmethod
    def get_location_terms(self):
        """Gets the location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    location_terms = property(fget=get_location_terms)

    @abc.abstractmethod
    def get_spatial_coverage_terms(self):
        """Gets the spatial coverage query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    spatial_coverage_terms = property(fget=get_spatial_coverage_terms)

    @abc.abstractmethod
    def get_spatial_coverage_overlap_terms(self):
        """Gets the spatial coverage overlap query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    spatial_coverage_overlap_terms = property(fget=get_spatial_coverage_overlap_terms)

    @abc.abstractmethod
    def get_asset_content_id_terms(self):
        """Gets the asset content ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    asset_content_id_terms = property(fget=get_asset_content_id_terms)

    @abc.abstractmethod
    def get_asset_content_terms(self):
        """Gets the asset content query terms.

        :return: the query terms
        :rtype: ``osid.repository.AssetContentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetContentQueryInspector

    asset_content_terms = property(fget=get_asset_content_terms)

    @abc.abstractmethod
    def get_composition_id_terms(self):
        """Gets the composition ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    composition_id_terms = property(fget=get_composition_id_terms)

    @abc.abstractmethod
    def get_composition_terms(self):
        """Gets the composition query terms.

        :return: the query terms
        :rtype: ``osid.repository.CompositionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionQueryInspector

    composition_terms = property(fget=get_composition_terms)

    @abc.abstractmethod
    def get_repository_id_terms(self):
        """Gets the repository ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    repository_id_terms = property(fget=get_repository_id_terms)

    @abc.abstractmethod
    def get_repository_terms(self):
        """Gets the repository query terms.

        :return: the query terms
        :rtype: ``osid.repository.RepositoryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQueryInspector

    repository_terms = property(fget=get_repository_terms)

    @abc.abstractmethod
    def get_asset_query_inspector_record(self, asset_record_type):
        """Gets the asset query inspector record corresponding to the given ``Asset`` record ``Type``.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the asset query inspector record
        :rtype: ``osid.repository.records.AssetQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetQueryInspectorRecord


class AssetContentQueryInspector:
    """This is the query inspector for examining asset content queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_accessibility_type_terms(self):
        """Gets the accesibility type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    accessibility_type_terms = property(fget=get_accessibility_type_terms)

    @abc.abstractmethod
    def get_data_length_terms(self):
        """Gets the data length query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CardinalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalRangeTerm

    data_length_terms = property(fget=get_data_length_terms)

    @abc.abstractmethod
    def get_data_terms(self):
        """Gets the data query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BytesTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BytesTerm

    data_terms = property(fget=get_data_terms)

    @abc.abstractmethod
    def get_url_terms(self):
        """Gets the url query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    url_terms = property(fget=get_url_terms)

    @abc.abstractmethod
    def get_asset_content_query_inspector_record(self, asset_content_record_type):
        """Gets the asset content query inspector corresponding to the given ``AssetContent`` record ``Type``.

        :param asset_content_record_type: an asset content record type
        :type asset_content_record_type: ``osid.type.Type``
        :return: the asset content query inspector record
        :rtype: ``osid.repository.records.AssetContentQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetContentQueryInspectorRecord


class CompositionQueryInspector:
    """This is the query inspector for examining composition queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_asset_id_terms(self):
        """Gets the asset ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    asset_id_terms = property(fget=get_asset_id_terms)

    @abc.abstractmethod
    def get_asset_terms(self):
        """Gets the asset query terms.

        :return: the query terms
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQueryInspector

    asset_terms = property(fget=get_asset_terms)

    @abc.abstractmethod
    def get_containing_composition_id_terms(self):
        """Gets the containing composition ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    containing_composition_id_terms = property(fget=get_containing_composition_id_terms)

    @abc.abstractmethod
    def get_containing_composition_terms(self):
        """Gets the containing composition query terms.

        :return: the query terms
        :rtype: ``osid.repository.CompositionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionQueryInspector

    containing_composition_terms = property(fget=get_containing_composition_terms)

    @abc.abstractmethod
    def get_contained_composition_id_terms(self):
        """Gets the contained composition ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    contained_composition_id_terms = property(fget=get_contained_composition_id_terms)

    @abc.abstractmethod
    def get_contained_composition_terms(self):
        """Gets the contained composition query terms.

        :return: the query terms
        :rtype: ``osid.repository.CompositionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionQueryInspector

    contained_composition_terms = property(fget=get_contained_composition_terms)

    @abc.abstractmethod
    def get_repository_id_terms(self):
        """Gets the repository ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    repository_id_terms = property(fget=get_repository_id_terms)

    @abc.abstractmethod
    def get_repository_terms(self):
        """Gets the repository query terms.

        :return: the query terms
        :rtype: ``osid.repository.RepositoryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQueryInspector

    repository_terms = property(fget=get_repository_terms)

    @abc.abstractmethod
    def get_composition_query_inspector_record(self, composition_record_type):
        """Gets the composition query inspector record corresponding to the given ``Composition`` record ``Type``.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the composition query inspector record
        :rtype: ``osid.repository.records.CompositionQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(composition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionQueryInspectorRecord


class RepositoryQueryInspector:
    """This is the query inspector for examining repository queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_asset_id_terms(self):
        """Gets the asset ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    asset_id_terms = property(fget=get_asset_id_terms)

    @abc.abstractmethod
    def get_asset_terms(self):
        """Gets the asset query terms.

        :return: the query terms
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQueryInspector

    asset_terms = property(fget=get_asset_terms)

    @abc.abstractmethod
    def get_composition_id_terms(self):
        """Gets the composition ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    composition_id_terms = property(fget=get_composition_id_terms)

    @abc.abstractmethod
    def get_composition_terms(self):
        """Gets the composition query terms.

        :return: the query terms
        :rtype: ``osid.repository.CompositionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.CompositionQueryInspector

    composition_terms = property(fget=get_composition_terms)

    @abc.abstractmethod
    def get_ancestor_repository_id_terms(self):
        """Gets the ancestor repository ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_repository_id_terms = property(fget=get_ancestor_repository_id_terms)

    @abc.abstractmethod
    def get_ancestor_repository_terms(self):
        """Gets the ancestor repository query terms.

        :return: the query terms
        :rtype: ``osid.repository.RepositoryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQueryInspector

    ancestor_repository_terms = property(fget=get_ancestor_repository_terms)

    @abc.abstractmethod
    def get_descendant_repository_id_terms(self):
        """Gets the descendant repository ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_repository_id_terms = property(fget=get_descendant_repository_id_terms)

    @abc.abstractmethod
    def get_descendant_repository_terms(self):
        """Gets the descendant repository query terms.

        :return: the query terms
        :rtype: ``osid.repository.RepositoryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.RepositoryQueryInspector

    descendant_repository_terms = property(fget=get_descendant_repository_terms)

    @abc.abstractmethod
    def get_repository_query_inspector_record(self, repository_record_type):
        """Gets the repository query inspector record corresponding to the given ``Repository`` record ``Type``.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository query inspector record
        :rtype: ``osid.repository.records.RepositoryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositoryQueryInspectorRecord
