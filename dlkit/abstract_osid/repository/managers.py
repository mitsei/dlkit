"""Implementations of repository abstract base class managers."""
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


class RepositoryProfile:
    """The repository profile describes interoperability among repository services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_lookup(self):
        """Tests if asset lookup is supported.

        :return: ``true`` if asset lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_query(self):
        """Tests if asset query is supported.

        :return: ``true`` if asset query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_search(self):
        """Tests if asset search is supported.

        :return: ``true`` if asset search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_admin(self):
        """Tests if asset administration is supported.

        :return: ``true`` if asset administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_notification(self):
        """Tests if asset notification is supported.

        A repository may send messages when assets are created,
        modified, or deleted.

        :return: ``true`` if asset notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_repository(self):
        """Tests if retrieving mappings of assets and repositories is supported.

        :return: ``true`` if asset repository mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_repository_assignment(self):
        """Tests if managing mappings of assets and repositories is supported.

        :return: ``true`` if asset repository assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_smart_repository(self):
        """Tests if asset smart repository is supported.

        :return: ``true`` if asset smart repository is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_temporal(self):
        """Tests if retrieving mappings of assets and time coverage is supported.

        :return: ``true`` if asset temporal mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_temporal_assignment(self):
        """Tests if managing mappings of assets and time ocverage is supported.

        :return: ``true`` if asset temporal assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_spatial(self):
        """Tests if retrieving mappings of assets and spatial coverage is supported.

        :return: ``true`` if asset spatial mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_spatial_assignment(self):
        """Tests if managing mappings of assets and spatial ocverage is supported.

        :return: ``true`` if asset spatial assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_composition(self):
        """Tests if assets are included in compositions.

        :return: ``true`` if asset composition supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_asset_composition_design(self):
        """Tests if mapping assets to compositions is supported.

        :return: ``true`` if designing asset compositions is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_lookup(self):
        """Tests if composition lookup is supported.

        :return: ``true`` if composition lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_query(self):
        """Tests if composition query is supported.

        :return: ``true`` if composition query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_search(self):
        """Tests if composition search is supported.

        :return: ``true`` if composition search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_admin(self):
        """Tests if composition administration is supported.

        :return: ``true`` if composition administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_notification(self):
        """Tests if composition notification is supported.

        :return: ``true`` if composition notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_repository(self):
        """Tests if retrieval of composition to repository mappings is supported.

        :return: ``true`` if composition to repository mapping is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_repository_assignment(self):
        """Tests if assigning composition to repository mappings is supported.

        :return: ``true`` if composition to repository assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_composition_smart_repository(self):
        """Tests if composition smart repository is supported.

        :return: ``true`` if composition smart repository is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_lookup(self):
        """Tests if repository lookup is supported.

        :return: ``true`` if repository lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_query(self):
        """Tests if repository query is supported.

        :return: ``true`` if repository query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_search(self):
        """Tests if repository search is supported.

        :return: ``true`` if repository search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_admin(self):
        """Tests if repository administration is supported.

        :return: ``true`` if repository administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_notification(self):
        """Tests if repository notification is supported.

        Messages may be sent when ``Repository`` objects are created,
        deleted or updated. Notifications for assets within repositories
        are sent via the asset notification session.

        :return: ``true`` if repository notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_hierarchy(self):
        """Tests if a repository hierarchy traversal is supported.

        :return: ``true`` if a repository hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_hierarchy_design(self):
        """Tests if a repository hierarchy design is supported.

        :return: ``true`` if a repository hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_batch(self):
        """Tests if a repository batch service is supported.

        :return: ``true`` if a repository batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_repository_rules(self):
        """Tests if a repository rules service is supported.

        :return: ``true`` if a repository rules service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_record_types(self):
        """Gets all the asset record types supported.

        :return: the list of supported asset record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    asset_record_types = property(fget=get_asset_record_types)

    @abc.abstractmethod
    def supports_asset_record_type(self, asset_record_type):
        """Tests if a given asset type is supported.

        :param asset_record_type: the asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: ``true`` if the asset record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_search_record_types(self):
        """Gets all the asset search record types supported.

        :return: the list of supported asset search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    asset_search_record_types = property(fget=get_asset_search_record_types)

    @abc.abstractmethod
    def supports_asset_search_record_type(self, asset_search_record_type):
        """Tests if a given asset search record type is supported.

        :param asset_search_record_type: the asset search record type
        :type asset_search_record_type: ``osid.type.Type``
        :return: ``true`` if the asset search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_content_record_types(self):
        """Gets all the asset content record types supported.

        :return: the list of supported asset content record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    asset_content_record_types = property(fget=get_asset_content_record_types)

    @abc.abstractmethod
    def supports_asset_content_record_type(self, asset_content_record_type):
        """Tests if a given asset content record type is supported.

        :param asset_content_record_type: the asset content record type
        :type asset_content_record_type: ``osid.type.Type``
        :return: ``true`` if the asset content record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_composition_record_types(self):
        """Gets all the composition record types supported.

        :return: the list of supported composition record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    composition_record_types = property(fget=get_composition_record_types)

    @abc.abstractmethod
    def supports_composition_record_type(self, composition_record_type):
        """Tests if a given composition record type is supported.

        :param composition_record_type: the composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: ``true`` if the composition record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_composition_search_record_types(self):
        """Gets all the composition search record types supported.

        :return: the list of supported composition search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    composition_search_record_types = property(fget=get_composition_search_record_types)

    @abc.abstractmethod
    def supports_composition_search_record_type(self, composition_search_record_type):
        """Tests if a given composition search record type is supported.

        :param composition_search_record_type: the composition serach type
        :type composition_search_record_type: ``osid.type.Type``
        :return: ``true`` if the composition search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``composition_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_repository_record_types(self):
        """Gets all the repository record types supported.

        :return: the list of supported repository record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    repository_record_types = property(fget=get_repository_record_types)

    @abc.abstractmethod
    def supports_repository_record_type(self, repository_record_type):
        """Tests if a given repository record type is supported.

        :param repository_record_type: the repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: ``true`` if the repository record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_repository_search_record_types(self):
        """Gets all the repository search record types supported.

        :return: the list of supported repository search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    repository_search_record_types = property(fget=get_repository_search_record_types)

    @abc.abstractmethod
    def supports_repository_search_record_type(self, repository_search_record_type):
        """Tests if a given repository search record type is supported.

        :param repository_search_record_type: the repository search type
        :type repository_search_record_type: ``osid.type.Type``
        :return: ``true`` if the repository search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_spatial_unit_record_types(self):
        """Gets all the spatial unit record types supported.

        :return: the list of supported spatial unit record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    @abc.abstractmethod
    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if a given spatial unit record type is supported.

        :param spatial_unit_record_type: the spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the spatial unit record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_coordinate_types(self):
        """Gets all the coordinate types supported.

        :return: the list of supported coordinate types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    coordinate_types = property(fget=get_coordinate_types)

    @abc.abstractmethod
    def supports_coordinate_type(self, coordinate_type):
        """Tests if a given coordinate type is supported.

        :param coordinate_type: the coordinate type
        :type coordinate_type: ``osid.type.Type``
        :return: ``true`` if the coordinate type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class RepositoryManager:
    """The repository manager provides access to asset lookup and creation session and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AssetLookupSession:`` a session to retrieve assets
      * ``AssetQuerySession:`` a session to query assets
      * ``AssetSearchSession:`` a session to search for assets
      * ``AssetAdminSession:`` a session to create and delete assets
      * ``AssetNotificationSession:`` a session to receive notifications
        pertaining to asset changes
      * ``AssetRepositorySession:`` a session to look up asset to
        repository mappings
      * ``AssetRepositoryAssignmentSession:`` a session to manage asset
        to repository mappings
      * ``AssetSmartRepositorySession:`` a session to manage dynamic
        repositories of assets
      * ``AssetTemporalSession:`` a session to access the temporal
        coverage of an asset
      * ``AssetTemporalAssignmentSession:`` a session to manage the
        temporal coverage of an asset
      * ``AssetSpatialSession:`` a session to access the spatial
        coverage of an asset
      * ``AssetSpatialAssignmentSession:`` a session to manage the
        spatial coverage of an asset
      * ``AssetCompositionSession:`` a session to look up asset
        composition mappings
      * ``AssetCompositionDesignSession:`` a session to map assets to
        compositions

      * ``CompositionLookupSession: a`` session to retrieve compositions
      * ``CompositionQuerySession:`` a session to query compositions
      * ``CompositionSearchSession:`` a session to search for
        compositions
      * ``CompositionAdminSession:`` a session to create, update and
        delete compositions
      * ``CompositionNotificationSession:`` a session to receive
        notifications pertaining to changes in compositions
      * ``CompositionRepositorySession:`` a session to retrieve
        composition repository mappings
      * ``CompositionRepositoryAssignmentSession:`` a session to manage
        composition repository mappings
      * ``CompositionSmartRepositorySession:`` a session to manage
        dynamic repositories of compositions

      * ``RepositoryLookupSession: a`` session to retrieve repositories
      * ``RepositoryQuerySession:`` a session to query repositories
      * ``RepositorySearchSession:`` a session to search for
        repositories
      * ``RepositoryAdminSession:`` a session to create, update and
        delete repositories
      * ``RepositoryNotificationSession:`` a session to receive
        notifications pertaining to changes in repositories
      * ``RepositoryHierarchySession:`` a session to traverse repository
        hierarchies
      * ``RepositoryHierarchyDesignSession:`` a session to manage
        repository hierarchies

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_asset_lookup_session(self):
        """Gets the ``OsidSession`` associated with the asset lookup service.

        :return: the new ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_lookup()`` is ``true``.*

        """
        return  # osid.repository.AssetLookupSession

    asset_lookup_session = property(fget=get_asset_lookup_session)

    @abc.abstractmethod
    def get_asset_lookup_session_for_repository(self, repository_id):
        """Gets the ``OsidSession`` associated with the asset lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: the new ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetLookupSession

    @abc.abstractmethod
    def get_asset_query_session(self):
        """Gets an asset query session.

        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuerySession

    asset_query_session = property(fget=get_asset_query_session)

    @abc.abstractmethod
    def get_asset_query_session_for_repository(self, repository_id):
        """Gets an asset query session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.repository.AssetQuerySession

    @abc.abstractmethod
    def get_asset_search_session(self):
        """Gets an asset search session.

        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_search()`` is ``true``.*

        """
        return  # osid.repository.AssetSearchSession

    asset_search_session = property(fget=get_asset_search_session)

    @abc.abstractmethod
    def get_asset_search_session_for_repository(self, repository_id):
        """Gets an asset search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetSearchSession

    @abc.abstractmethod
    def get_asset_admin_session(self):
        """Gets an asset administration session for creating, updating and deleting assets.

        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_admin()`` is ``true``.*

        """
        return  # osid.repository.AssetAdminSession

    asset_admin_session = property(fget=get_asset_admin_session)

    @abc.abstractmethod
    def get_asset_admin_session_for_repository(self, repository_id):
        """Gets an asset administration session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.repository.AssetAdminSession

    @abc.abstractmethod
    def get_asset_notification_session(self, asset_receiver):
        """Gets the notification session for notifications pertaining to asset changes.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NullArgument`` -- ``asset_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_notification()`` is ``true``.*

        """
        return  # osid.repository.AssetNotificationSession

    @abc.abstractmethod
    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id):
        """Gets the asset notification session for the given repository.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``asset_receiver`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetNotificationSession

    @abc.abstractmethod
    def get_asset_repository_session(self):
        """Gets the session for retrieving asset to repository mappings.

        :return: an ``AssetRepositorySession``
        :rtype: ``osid.repository.AssetRepositorySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_repository()`` is ``true``.*

        """
        return  # osid.repository.AssetRepositorySession

    asset_repository_session = property(fget=get_asset_repository_session)

    @abc.abstractmethod
    def get_asset_repository_assignment_session(self):
        """Gets the session for assigning asset to repository mappings.

        :return: an ``AssetRepositoryAsignmentSession``
        :rtype: ``osid.repository.AssetRepositoryAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_repository_assignment()`` is ``true``.*

        """
        return  # osid.repository.AssetRepositoryAssignmentSession

    asset_repository_assignment_session = property(fget=get_asset_repository_assignment_session)

    @abc.abstractmethod
    def get_asset_smart_repository_session(self, repository_id):
        """Gets an asset smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSmartRepositorySession``
        :rtype: ``osid.repository.AssetSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_smart_repository()``  ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_smart_repository()`` is ``true``.*

        """
        return  # osid.repository.AssetSmartRepositorySession

    @abc.abstractmethod
    def get_asset_temporal_session(self):
        """Gets the session for retrieving temporal coverage of an asset.

        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal()`` is ``true``.*

        """
        return  # osid.repository.AssetTemporalSession

    asset_temporal_session = property(fget=get_asset_temporal_session)

    @abc.abstractmethod
    def get_asset_temporal_session_for_repository(self, repository_id):
        """Gets the session for retrieving temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetTemporalSession

    @abc.abstractmethod
    def get_asset_temporal_assignment_session(self):
        """Gets the session for assigning temporal coverage to an asset.

        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal_assignment()`` is ``true``.*

        """
        return  # osid.repository.AssetTemporalAssignmentSession

    asset_temporal_assignment_session = property(fget=get_asset_temporal_assignment_session)

    @abc.abstractmethod
    def get_asset_temporal_assignment_session_for_repository(self, repository_id):
        """Gets the session for assigning temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetTemporalAssignmentSession

    @abc.abstractmethod
    def get_asset_spatial_session(self):
        """Gets the session for retrieving spatial coverage of an asset.

        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_assets()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_spatial_assets()`` is ``true``.*

        """
        return  # osid.repository.AssetSpatialSession

    asset_spatial_session = property(fget=get_asset_spatial_session)

    @abc.abstractmethod
    def get_asset_spatial_session_for_repository(self, repository_id):
        """Gets the session for retrieving spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetSpatialSession

    @abc.abstractmethod
    def get_asset_spatial_assignment_session(self):
        """Gets the session for assigning spatial coverage to an asset.

        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial_assignment()`` is ``true``.*

        """
        return  # osid.repository.AssetSpatialAssignmentSession

    asset_spatial_assignment_session = property(fget=get_asset_spatial_assignment_session)

    @abc.abstractmethod
    def get_asset_spatial_assignment_session_for_repository(self, repository_id):
        """Gets the session for assigning spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetSpatialAssignmentSession

    @abc.abstractmethod
    def get_asset_composition_session(self):
        """Gets the session for retrieving asset compositions.

        :return: an ``AssetCompositionSession``
        :rtype: ``osid.repository.AssetCompositionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_composition()`` is ``true``.*

        """
        return  # osid.repository.AssetCompositionSession

    asset_composition_session = property(fget=get_asset_composition_session)

    @abc.abstractmethod
    def get_asset_composition_design_session(self):
        """Gets the session for creating asset compositions.

        :return: an ``AssetCompositionDesignSession``
        :rtype: ``osid.repository.AssetCompositionDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_composition_design()`` is ``true``.*

        """
        return  # osid.repository.AssetCompositionDesignSession

    asset_composition_design_session = property(fget=get_asset_composition_design_session)

    @abc.abstractmethod
    def get_composition_lookup_session(self):
        """Gets the ``OsidSession`` associated with the composition lookup service.

        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_lookup()`` is ``true``.*

        """
        return  # osid.repository.CompositionLookupSession

    composition_lookup_session = property(fget=get_composition_lookup_session)

    @abc.abstractmethod
    def get_composition_lookup_session_for_repository(self, repository_id):
        """Gets the ``OsidSession`` associated with the composition lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionLookupSession

    @abc.abstractmethod
    def get_composition_query_session(self):
        """Gets a composition query session.

        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        return  # osid.repository.CompositionQuerySession

    composition_query_session = property(fget=get_composition_query_session)

    @abc.abstractmethod
    def get_composition_query_session_for_repository(self, repository_id):
        """Gets a composition query session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionQuerySession

    @abc.abstractmethod
    def get_composition_search_session(self):
        """Gets a composition search session.

        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_search()`` is ``true``.*

        """
        return  # osid.repository.CompositionSearchSession

    composition_search_session = property(fget=get_composition_search_session)

    @abc.abstractmethod
    def get_composition_search_session_for_repository(self, repository_id):
        """Gets a composition search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionSearchSession

    @abc.abstractmethod
    def get_composition_admin_session(self):
        """Gets a composition administration session for creating, updating and deleting compositions.

        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_admin()`` is ``true``.*

        """
        return  # osid.repository.CompositionAdminSession

    composition_admin_session = property(fget=get_composition_admin_session)

    @abc.abstractmethod
    def get_composition_admin_session_for_repository(self, repository_id):
        """Gets a composiiton administrative session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionAdminSession

    @abc.abstractmethod
    def get_composition_notification_session(self, composition_receiver):
        """Gets the notification session for notifications pertaining to composition changes.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NullArgument`` -- ``composition_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_notification()`` is ``true``.*

        """
        return  # osid.repository.CompositionNotificationSession

    @abc.abstractmethod
    def get_composition_notification_session_for_repository(self, composition_receiver, repository_id):
        """Gets the composition notification session for the given repository.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``composition_receiver`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionNotificationSession

    @abc.abstractmethod
    def get_composition_repository_session(self):
        """Gets the session for retrieving composition to repository mappings.

        :return: a ``CompositionRepositorySession``
        :rtype: ``osid.repository.CompositionRepositorySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_repository()`` is ``true``.*

        """
        return  # osid.repository.CompositionRepositorySession

    composition_repository_session = property(fget=get_composition_repository_session)

    @abc.abstractmethod
    def get_composition_repository_assignment_session(self):
        """Gets the session for assigning composition to repository mappings.

        :return: a ``CompositionRepositoryAssignmentSession``
        :rtype: ``osid.repository.CompositionRepositoryAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_repository_assignment()`` is ``true``.*

        """
        return  # osid.repository.CompositionRepositoryAssignmentSession

    composition_repository_assignment_session = property(fget=get_composition_repository_assignment_session)

    @abc.abstractmethod
    def get_composition_smart_repository_session(self, repository_id):
        """Gets a composition smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionSmartRepositorySession``
        :rtype: ``osid.repository.CompositionSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_smart_repository()``  ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_smart_repository()`` is ``true``.*

        """
        return  # osid.repository.CompositionSmartRepositorySession

    @abc.abstractmethod
    def get_repository_lookup_session(self):
        """Gets the repository lookup session.

        :return: a ``RepositoryLookupSession``
        :rtype: ``osid.repository.RepositoryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_lookup()`` is ``true``.*

        """
        return  # osid.repository.RepositoryLookupSession

    repository_lookup_session = property(fget=get_repository_lookup_session)

    @abc.abstractmethod
    def get_repository_query_session(self):
        """Gets the repository query session.

        :return: a ``RepositoryQuerySession``
        :rtype: ``osid.repository.RepositoryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_query()`` is ``true``.*

        """
        return  # osid.repository.RepositoryQuerySession

    repository_query_session = property(fget=get_repository_query_session)

    @abc.abstractmethod
    def get_repository_search_session(self):
        """Gets the repository search session.

        :return: a ``RepositorySearchSession``
        :rtype: ``osid.repository.RepositorySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_search()`` is ``true``.*

        """
        return  # osid.repository.RepositorySearchSession

    repository_search_session = property(fget=get_repository_search_session)

    @abc.abstractmethod
    def get_repository_admin_session(self):
        """Gets the repository administrative session for creating, updating and deleteing repositories.

        :return: a ``RepositoryAdminSession``
        :rtype: ``osid.repository.RepositoryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_admin()`` is ``true``.*

        """
        return  # osid.repository.RepositoryAdminSession

    repository_admin_session = property(fget=get_repository_admin_session)

    @abc.abstractmethod
    def get_repository_notification_session(self, repository_receiver):
        """Gets the notification session for subscribing to changes to a repository.

        :param repository_receiver: the notification callback
        :type repository_receiver: ``osid.repository.RepositoryReceiver``
        :return: a ``RepositoryNotificationSession``
        :rtype: ``osid.repository.RepositoryNotificationSession``
        :raise: ``NullArgument`` -- ``repository_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_notification()`` is ``true``.*

        """
        return  # osid.repository.RepositoryNotificationSession

    @abc.abstractmethod
    def get_repository_hierarchy_session(self):
        """Gets the repository hierarchy traversal session.

        :return: ``a RepositoryHierarchySession``
        :rtype: ``osid.repository.RepositoryHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_hierarchy()`` is ``true``.*

        """
        return  # osid.repository.RepositoryHierarchySession

    repository_hierarchy_session = property(fget=get_repository_hierarchy_session)

    @abc.abstractmethod
    def get_repository_hierarchy_design_session(self):
        """Gets the repository hierarchy design session.

        :return: a ``RepostoryHierarchyDesignSession``
        :rtype: ``osid.repository.RepositoryHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_hierarchy_design()`` is ``true``.*

        """
        return  # osid.repository.RepositoryHierarchyDesignSession

    repository_hierarchy_design_session = property(fget=get_repository_hierarchy_design_session)

    @abc.abstractmethod
    def get_repository_batch_manager(self):
        """Gets a ``RepositoryBatchManager``.

        :return: a ``RepostoryBatchManager``
        :rtype: ``osid.repository.batch.RepositoryBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_batch()`` is ``true``.*

        """
        return  # osid.repository.batch.RepositoryBatchManager

    repository_batch_manager = property(fget=get_repository_batch_manager)

    @abc.abstractmethod
    def get_repository_rules_manager(self):
        """Gets a ``RepositoryRulesManager``.

        :return: a ``RepostoryRulesManager``
        :rtype: ``osid.repository.rules.RepositoryRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_rules()`` is ``true``.*

        """
        return  # osid.repository.rules.RepositoryRulesManager

    repository_rules_manager = property(fget=get_repository_rules_manager)


class RepositoryProxyManager:
    """The repository manager provides access to asset lookup and creation session and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for the
    purposes of passing information from a server environment. The
    sessions included in this manager are:

      * ``AssetLookupSession:`` a session to retrieve assets
      * ``AssetQuerySession:`` a session to query assets
      * ``AssetSearchSession:`` a session to search for assets
      * ``AssetAdminSession:`` a session to create and delete assets
      * ``AssetNotificationSession:`` a session to receive notifications
        pertaining to asset changes
      * ``AssetRepositorySession:`` a session to look up asset to
        repository mappings
      * ``AssetRepositoryAssignmentSession:`` a session to manage asset
        to repository mappings
      * ``AssetSmartRepositorySession:`` a session to manage dynamic
        repositories of assets
      * ``AssetTemporalSession:`` a session to access the temporal
        coverage of an asset
      * ``AssetTemporalAssignmentSession:`` a session to manage the
        temporal coverage of an asset
      * ``AssetSpatialSession:`` a session to access the spatial
        coverage of an asset
      * ``AssetSpatialAssignmentSession:`` a session to manage the
        spatial coverage of an asset
      * ``AssetCompositionSession:`` a session to look up asset
        composition mappings
      * ``AssetCompositionDesignSession:`` a session to map assets to
        compositions

      * ``CompositionLookupSession: a`` session to retrieve compositions
      * ``CompositionQuerySession:`` a session to query compositions
      * ``CompositionSearchSession:`` a session to search for
        compositions
      * ``CompositionAdminSession:`` a session to create, update and
        delete compositions
      * ``CompositionNotificationSession:`` a session to receive
        notifications pertaining to changes in compositions
      * ``CompositionRepositorySession:`` a session to retrieve
        composition repository mappings
      * ``CompositionRepositoryAssignmentSession:`` a session to manage
        composition repository mappings
      * ``CompositionSmartRepositorySession:`` a session to manage
        dynamic repositories of compositions

      * ``RepositoryLookupSession: a`` session to retrieve repositories
      * ``RepositoryQuerySession:`` a session to query repositories
      * ``RepositorySearchSession:`` a session to search for
        repositories
      * ``RepositoryAdminSession:`` a session to create, update and
        delete repositories
      * ``RepositoryNotificationSession:`` a session to receive
        notifications pertaining to changes in repositories
      * ``RepositoryHierarchySession:`` a session to traverse repository
        hierarchies
      * ``RepositoryHierarchyDesignSession:`` a session to manage
        repository hierarchies

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_asset_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the asset lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_lookup()`` is ``true``.*

        """
        return  # osid.repository.AssetLookupSession

    @abc.abstractmethod
    def get_asset_lookup_session_for_repository(self, repository_id, proxy):
        """Gets the ``OsidSession`` associated with the asset lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetLookupSession

    @abc.abstractmethod
    def get_asset_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the asset query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuerySession

    @abc.abstractmethod
    def get_asset_query_session_for_repository(self, repository_id, proxy):
        """Gets the ``OsidSession`` associated with the asset query service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.repository.AssetQuerySession

    @abc.abstractmethod
    def get_asset_search_session(self, proxy):
        """Gets an asset search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_search()`` is ``true``.*

        """
        return  # osid.repository.AssetSearchSession

    @abc.abstractmethod
    def get_asset_search_session_for_repository(self, repository_id, proxy):
        """Gets an asset search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetSearchSession

    @abc.abstractmethod
    def get_asset_admin_session(self, proxy):
        """Gets an asset administration session for creating, updating and deleting assets.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_admin()`` is ``true``.*

        """
        return  # osid.repository.AssetAdminSession

    @abc.abstractmethod
    def get_asset_admin_session_for_repository(self, repository_id, proxy):
        """Gets an asset administration session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.repository.AssetAdminSession

    @abc.abstractmethod
    def get_asset_notification_session(self, asset_receiver, proxy):
        """Gets the notification session for notifications pertaining to asset changes.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NullArgument`` -- ``asset_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_notification()`` is ``true``.*

        """
        return  # osid.repository.AssetNotificationSession

    @abc.abstractmethod
    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id, proxy):
        """Gets the asset notification session for the given repository.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``asset_receiver, repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetNotificationSession

    @abc.abstractmethod
    def get_asset_repository_session(self, proxy):
        """Gets the session for retrieving asset to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetRepositorySession``
        :rtype: ``osid.repository.AssetRepositorySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_repository()`` is ``true``.*

        """
        return  # osid.repository.AssetRepositorySession

    @abc.abstractmethod
    def get_asset_repository_assignment_session(self, proxy):
        """Gets the session for assigning asset to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetRepositoryAsignmentSession``
        :rtype: ``osid.repository.AssetRepositoryAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_repository_assignment()`` is ``true``.*

        """
        return  # osid.repository.AssetRepositoryAssignmentSession

    @abc.abstractmethod
    def get_asset_smart_repository_session(self, repository_id, proxy):
        """Gets an asset smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSmartRepositorySession``
        :rtype: ``osid.repository.AssetSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_smart_repository()``  ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_smart_repository()`` is ``true``.*

        """
        return  # osid.repository.AssetSmartRepositorySession

    @abc.abstractmethod
    def get_asset_temporal_session(self, proxy):
        """Gets the session for retrieving temporal coverage of an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal()`` is ``true``.*

        """
        return  # osid.repository.AssetTemporalSession

    @abc.abstractmethod
    def get_asset_temporal_session_for_repository(self, repository_id, proxy):
        """Gets the session for retrieving temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetTemporalSession

    @abc.abstractmethod
    def get_asset_temporal_assignment_session(self, proxy):
        """Gets the session for assigning temporal coverage to an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal_assignment()`` is ``true``.*

        """
        return  # osid.repository.AssetTemporalAssignmentSession

    @abc.abstractmethod
    def get_asset_temporal_assignment_session_for_repository(self, repository_id, proxy):
        """Gets the session for assigning temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetTemporalAssignmentSession

    @abc.abstractmethod
    def get_asset_spatial_session(self, proxy):
        """Gets the session for retrieving spatial coverage of an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_assets()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_spatial_assets()`` is ``true``.*

        """
        return  # osid.repository.AssetSpatialSession

    @abc.abstractmethod
    def get_asset_spatial_session_for_repository(self, repository_id, proxy):
        """Gets the session for retrieving spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetSpatialSession

    @abc.abstractmethod
    def get_asset_spatial_assignment_session(self, proxy):
        """Gets the session for assigning spatial coverage to an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial_assignment()`` is ``true``.*

        """
        return  # osid.repository.AssetSpatialAssignmentSession

    @abc.abstractmethod
    def get_asset_spatial_assignment_session_for_repository(self, repository_id, proxy):
        """Gets the session for assigning spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.AssetSpatialAssignmentSession

    @abc.abstractmethod
    def get_asset_composition_session(self, proxy):
        """Gets the session for retrieving asset compositions.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetCompositionSession``
        :rtype: ``osid.repository.AssetCompositionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_composition()`` is ``true``.*

        """
        return  # osid.repository.AssetCompositionSession

    @abc.abstractmethod
    def get_asset_composition_design_session(self, proxy):
        """Gets the session for creating asset compositions.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetCompositionDesignSession``
        :rtype: ``osid.repository.AssetCompositionDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_asset_composition_design()`` is ``true``.*

        """
        return  # osid.repository.AssetCompositionDesignSession

    @abc.abstractmethod
    def get_composition_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the composition lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_lookup()`` is ``true``.*

        """
        return  # osid.repository.CompositionLookupSession

    @abc.abstractmethod
    def get_composition_lookup_session_for_repository(self, repository_id, proxy):
        """Gets the ``OsidSession`` associated with the composition lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionLookupSession

    @abc.abstractmethod
    def get_composition_query_session(self, proxy):
        """Gets a composition query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        return  # osid.repository.CompositionQuerySession

    @abc.abstractmethod
    def get_composition_query_session_for_repository(self, repository_id, proxy):
        """Gets a composition query session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionQuerySession

    @abc.abstractmethod
    def get_composition_search_session(self, proxy):
        """Gets a composition search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_search()`` is ``true``.*

        """
        return  # osid.repository.CompositionSearchSession

    @abc.abstractmethod
    def get_composition_search_session_for_repository(self, repository_id, proxy):
        """Gets a composition search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionSearchSession

    @abc.abstractmethod
    def get_composition_admin_session(self, proxy):
        """Gets a composition administration session for creating, updating and deleting compositions.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_admin()`` is ``true``.*

        """
        return  # osid.repository.CompositionAdminSession

    @abc.abstractmethod
    def get_composition_admin_session_for_repository(self, repository_id, proxy):
        """Gets a composiiton administrative session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionAdminSession

    @abc.abstractmethod
    def get_composition_notification_session(self, composition_receiver, proxy):
        """Gets the notification session for notifications pertaining to composition changes.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NullArgument`` -- ``composition_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_notification()`` is ``true``.*

        """
        return  # osid.repository.CompositionNotificationSession

    @abc.abstractmethod
    def get_composition_notification_session_for_repository(self, composition_receiver, repository_id, proxy):
        """Gets the composition notification session for the given repository.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``composition_receiver, repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.repository.CompositionNotificationSession

    @abc.abstractmethod
    def get_composition_repository_session(self, proxy):
        """Gets the session for retrieving composition to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionRepositorySession``
        :rtype: ``osid.repository.CompositionRepositorySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_repository()`` is ``true``.*

        """
        return  # osid.repository.CompositionRepositorySession

    @abc.abstractmethod
    def get_composition_repository_assignment_session(self, proxy):
        """Gets the session for assigning composition to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionRepositoryAssignmentSession``
        :rtype: ``osid.repository.CompositionRepositoryAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_repository_assignment()`` is ``true``.*

        """
        return  # osid.repository.CompositionRepositoryAssignmentSession

    @abc.abstractmethod
    def get_composition_smart_repository_session(self, repository_id, proxy):
        """Gets a composition smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionSmartRepositorySession``
        :rtype: ``osid.repository.CompositionSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_smart_repository()``  ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_composition_smart_repository()`` is ``true``.*

        """
        return  # osid.repository.CompositionSmartRepositorySession

    @abc.abstractmethod
    def get_repository_lookup_session(self, proxy):
        """Gets the repository lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryLookupSession``
        :rtype: ``osid.repository.RepositoryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_lookup()`` is ``true``.*

        """
        return  # osid.repository.RepositoryLookupSession

    @abc.abstractmethod
    def get_repository_query_session(self, proxy):
        """Gets the repository query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryQuerySession``
        :rtype: ``osid.repository.RepositoryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_query()`` is ``true``.*

        """
        return  # osid.repository.RepositoryQuerySession

    @abc.abstractmethod
    def get_repository_search_session(self, proxy):
        """Gets the repository search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositorySearchSession``
        :rtype: ``osid.repository.RepositorySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_search()`` is ``true``.*

        """
        return  # osid.repository.RepositorySearchSession

    @abc.abstractmethod
    def get_repository_admin_session(self, proxy):
        """Gets the repository administrative session for creating, updating and deleteing repositories.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryAdminSession``
        :rtype: ``osid.repository.RepositoryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_admin()`` is ``true``.*

        """
        return  # osid.repository.RepositoryAdminSession

    @abc.abstractmethod
    def get_repository_notification_session(self, repository_receiver, proxy):
        """Gets the notification session for subscribing to changes to a repository.

        :param repository_receiver: the notification callback
        :type repository_receiver: ``osid.repository.RepositoryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryNotificationSession``
        :rtype: ``osid.repository.RepositoryNotificationSession``
        :raise: ``NullArgument`` -- ``repository_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_notification()`` is ``true``.*

        """
        return  # osid.repository.RepositoryNotificationSession

    @abc.abstractmethod
    def get_repository_hierarchy_session(self, proxy):
        """Gets the repository hierarchy traversal session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a RepositoryHierarchySession``
        :rtype: ``osid.repository.RepositoryHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_hierarchy()`` is ``true``.*

        """
        return  # osid.repository.RepositoryHierarchySession

    @abc.abstractmethod
    def get_repository_hierarchy_design_session(self, proxy):
        """Gets the repository hierarchy design session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepostoryHierarchyDesignSession``
        :rtype: ``osid.repository.RepositoryHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_hierarchy_design()`` is ``true``.*

        """
        return  # osid.repository.RepositoryHierarchyDesignSession

    @abc.abstractmethod
    def get_repository_batch_proxy_manager(self):
        """Gets a ``RepositoryBatchProxyManager``.

        :return: a ``RepostoryBatchProxyManager``
        :rtype: ``osid.repository.batch.RepositoryBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_batch()`` is ``true``.*

        """
        return  # osid.repository.batch.RepositoryBatchProxyManager

    repository_batch_proxy_manager = property(fget=get_repository_batch_proxy_manager)

    @abc.abstractmethod
    def get_repository_rules_proxy_manager(self):
        """Gets a ``RepositoryRulesProxyManager``.

        :return: a ``RepostoryRulesProxyManager``
        :rtype: ``osid.repository.rules.RepositoryRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_rules()`` is ``true``.*

        """
        return  # osid.repository.rules.RepositoryRulesProxyManager

    repository_rules_proxy_manager = property(fget=get_repository_rules_proxy_manager)
