"""Implementations of repository abstract base class search_orders."""
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


class AssetSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_title(self, style):
        """Specifies a preference for ordering the result set by asset title.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_public_domain(self, style):
        """Specifies a preference for grouping the result set by published domain.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_copyright(self, style):
        """Specifies a preference for grouping the result set by copyright.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_copyright_registration(self, style):
        """Specifies a preference for grouping the result set by copyright registration.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_distribute_verbatim(self, style):
        """Specifies a preference for grouping the result set by the ability to distribute copies.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_distribute_alterations(self, style):
        """Specifies a preference for grouping the result set by the ability to distribute alterations.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_distribute_compositions(self, style):
        """Specifies a preference for grouping the result set by the ability to distribute compositions.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_source(self, style):
        """Specifies a preference for ordering the result set by asset source.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_source_search_order(self):
        """Tests if a source order interface is available.

        :return: ``true`` if a source search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_source_search_order(self):
        """Gets the source order.

        :return: the resource search order for the source
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_source_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_source_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    source_search_order = property(fget=get_source_search_order)

    @abc.abstractmethod
    def order_by_created_date(self, style):
        """Specifies a preference for ordering the result set by created date.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_published(self, style):
        """Specifies a preference for grouping the result set by published status.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_published_date(self, style):
        """Specifies a preference for ordering the result set by published date.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_principal_credit_string(self, style):
        """Specifies a preference for ordering the result set by the principal credit string.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_temporal_coverage(self, style):
        """Specifies a preference for ordering the result set by temporal coverage.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_asset_search_order_record(self, asset_record_type):
        """Gets the asset search order record corresponding to the given asset record ``Type``.

        Multiple retrievals return the same underlying object.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the asset search order record
        :rtype: ``osid.repository.records.AssetSearchOrderRecord``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.AssetSearchOrderRecord


class CompositionSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_composition_search_order_record(self, composition_record_type):
        """Gets the composition search order record corresponding to the given repository record ``Type``.

        Multiple retrievals return the same underlying object.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the composition search order record
        :rtype: ``osid.repository.records.CompositionSearchOrderRecord``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(composition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.CompositionSearchOrderRecord


class RepositorySearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_repository_search_order_record(self, repository_record_type):
        """Gets the repository search order record corresponding to the given repository record ``Type``.

        Multiple retrievals return the same underlying object.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository search order record
        :rtype: ``osid.repository.records.RepositorySearchOrderRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.records.RepositorySearchOrderRecord
