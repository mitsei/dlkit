"""Implementations of installation abstract base class managers."""
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


class InstallationProfile:
    """The ``InstallationProfile`` describes the interoperability among installation services."""
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
    def supports_installation_lookup(self):
        """Tests if an installation lookup service is supported.

        :return: true if installation lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_installation_query(self):
        """Tests if an installation query service is supported.

        :return: true if installation query is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_installation_search(self):
        """Tests if an installation search service is supported.

        :return: ``true`` if installation search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_installation_management(self):
        """Tests if an installation management service is supported.

        :return: ``true`` if package management is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_installation_update(self):
        """Tests if an installation update service is supported.

        :return: ``true`` if package update is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_installation_notification(self):
        """Tests if installation notification is supported.

        Messages may be sent when installations are installed or
        removed.

        :return: ``true`` if installation notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_site_lookup(self):
        """Tests if a site lookup service is supported.

        :return: true if site lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_lookup(self):
        """Tests if a package lookup service is supported.

        A package lookup service defines methods to access packages.

        :return: true if package lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_query(self):
        """Tests if querying packages is supported.

        :return: ``true`` if packages query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_search(self):
        """Tests if a package search service is supported.

        :return: ``true`` if package search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_admin(self):
        """Tests if a package administrative service is supported.

        :return: ``true`` if package admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_notification(self):
        """Tests if package notification is supported.

        Messages may be sent when packages are created, modified, or
        deleted.

        :return: ``true`` if package notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_depot(self):
        """Tests if a package to depot lookup session is available.

        :return: ``true`` if package depot lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_depot_assignment(self):
        """Tests if a package to depot assignment session is available.

        :return: ``true`` if package depot assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_package_smart_depot(self):
        """Tests if package smart depots are available.

        :return: ``true`` if package smart depots are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_lookup(self):
        """Tests if a depot lookup service is supported.

        :return: ``true`` if depot lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_query(self):
        """Tests if a depot query service is supported.

        :return: ``true`` if depot query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_search(self):
        """Tests if a depot search service is supported.

        :return: ``true`` if depot search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_admin(self):
        """Tests if a depot administrative service is supported.

        :return: ``true`` if depot admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_notification(self):
        """Tests if depot notification is supported.

        Messages may be sent when depots are created, modified, or
        deleted.

        :return: ``true`` if depot notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_hierarchy(self):
        """Tests if a depot hierarchy traversal is supported.

        :return: ``true`` if a depot hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_depot_hierarchy_design(self):
        """Tests if depot hierarchy design is supported.

        :return: ``true`` if a depot hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_installation_batch(self):
        """Tests if an installation batch service is supported.

        :return: ``true`` if an installation batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_record_types(self):
        """Gets the supported ``Installation`` record types.

        :return: a list containing the supported ``Installation`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    installation_record_types = property(fget=get_installation_record_types)

    @abc.abstractmethod
    def supports_installation_record_type(self, installation_record_type):
        """Tests if the given ``Installation`` record type is supported.

        :param installation_record_type: a ``Type`` indicating an ``Installation`` record type
        :type installation_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_search_record_types(self):
        """Gets the supported ``Installation`` search record types.

        :return: a list containing the supported ``Installation`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    installation_search_record_types = property(fget=get_installation_search_record_types)

    @abc.abstractmethod
    def supports_installation_search_record_type(self, installation_search_record_type):
        """Tests if the given ``Installation`` search record type is supported.

        :param installation_search_record_type: a ``Type`` indicating an ``Installation`` search record type
        :type installation_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_site_record_types(self):
        """Gets the supported ``Site`` record types.

        :return: a list containing the supported ``Site`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    site_record_types = property(fget=get_site_record_types)

    @abc.abstractmethod
    def supports_site_record_type(self, site_record_type):
        """Tests if the given ``Site`` record type is supported.

        :param site_record_type: a ``Type`` indicating a ``Site`` record type
        :type site_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``site_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_record_types(self):
        """Gets the supported ``Package`` record types.

        :return: a list containing the supported ``Package`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    package_record_types = property(fget=get_package_record_types)

    @abc.abstractmethod
    def supports_package_record_type(self, package_record_type):
        """Tests if the given ``Package`` record type is supported.

        :param package_record_type: a ``Type`` indicating a ``Package`` record type
        :type package_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_search_record_types(self):
        """Gets the supported ``Package`` search record types.

        :return: a list containing the supported ``Package`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    package_search_record_types = property(fget=get_package_search_record_types)

    @abc.abstractmethod
    def supports_package_search_record_type(self, package_search_record_type):
        """Tests if the given ``Package`` search record type is supported.

        :param package_search_record_type: a ``Type`` indicating a ``Package`` search record type
        :type package_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_content_record_types(self):
        """Gets the supported ``InstallationContent`` record types.

        :return: a list containing the supported ``InstallationContent`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    installation_content_record_types = property(fget=get_installation_content_record_types)

    @abc.abstractmethod
    def supports_installation_content_record_type(self, installation_content_record_type):
        """Tests if the given ``InstallationContent`` record type is supported.

        :param installation_content_record_type: a ``Type`` indicating an ``InstallationContent`` record type
        :type installation_content_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_content_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_record_types(self):
        """Gets the supported ``Depot`` record types.

        :return: a list containing the supported ``Depot`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    depot_record_types = property(fget=get_depot_record_types)

    @abc.abstractmethod
    def supports_depot_record_type(self, depot_record_type):
        """Tests if the given ``Depot`` record type is supported.

        :param depot_record_type: a ``Type`` indicating a ``Depot`` type
        :type depot_record_type: ``osid.type.Type``
        :return: ``true`` if the given depot record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_search_record_types(self):
        """Gets the supported depot search record types.

        :return: a list containing the supported ``Depot`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    depot_search_record_types = property(fget=get_depot_search_record_types)

    @abc.abstractmethod
    def supports_depot_search_record_type(self, depot_search_record_type):
        """Tests if the given depot search record type is supported.

        :param depot_search_record_type: a ``Type`` indicating a ``Depot`` search record type
        :type depot_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class InstallationManager:
    """The installation manager provides access to package installation sessions and provides interoperability tests for
        various aspects of this service.

    The sessions included in this manager are:

      * ``InstallationLookupSession:`` a session to look up local
        installations
      * ``InstallationQuerySession:`` a session to query local
        installations ``None``
      * ``InstallationSearchSession:`` a session to search local
        installations
      * ``InstallationManagementSession:`` a session to install and
        remove packages ``None``
      * ``InstallationUpdateSession`` : a session to get package updates
      * ``InstallationNotificationSession`` a session for subscribing to
        new or deleted installations
      * ``SiteLookupSession:`` a session for listing installation sites

      * ``PackageLookupSession:`` a session to look up packages ``None``
      * ``PackageQuerySession:`` a session to query packages
      * ``PackageSearchSession:`` a session to search packages
      * ``PackageAdminSession:`` a session to create, modify and delete
        packages ``None``
      * ``PackageNotificationSession: a`` session to receive messages
        pertaining to package ```` changes
      * ``PackageDepotSession:`` a session for retrieving package and
        depot mappings
      * ``PackageDepotAssignmentSession:`` a session for managing
        package and depot mappings
      * ``PackageSmartDepotSession:`` a session for managing smart
        depots of packages

      * ``DepotLookupSession:`` a session to lookup depots
      * ``DepotQuerySession:`` a session to query depots
      * ``DepotSearchSession`` : a session to search depots
      * ``DepotAdminSession`` : a session to create, modify and delete
        depots
      * ``DepotNotificationSession`` : a session to receive messages
        pertaining to depot changes
      * ``DepotHierarchySession:`` a session to traverse the depot
        hierarchy
      * ``DepotHierarchyDesignSession:`` a session to manage the depot
        hierarchy

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_installation_lookup_session(self):
        """Gets the ``OsidSession`` associated with the installation lookup service.

        :return: an ``InstallationLookupSession``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_lookup()`` is ``true``.*

        """
        return  # osid.installation.InstallationLookupSession

    installation_lookup_session = property(fget=get_installation_lookup_session)

    @abc.abstractmethod
    def get_installation_lookup_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation lookup service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_lookup_session``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationLookupSession

    @abc.abstractmethod
    def get_installation_query_session(self):
        """Gets the ``OsidSession`` associated with the installation query service.

        :return: an ``InstallationQuerySession``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_query()`` is ``true``.*

        """
        return  # osid.installation.InstallationQuerySession

    installation_query_session = property(fget=get_installation_query_session)

    @abc.abstractmethod
    def get_installation_query_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation query service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_query_session``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationQuerySession

    @abc.abstractmethod
    def get_installation_search_session(self):
        """Gets the ``OsidSession`` associated with the installation search service.

        :return: an ``InstallationSearchSession``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_search()`` is ``true``.*

        """
        return  # osid.installation.InstallationSearchSession

    installation_search_session = property(fget=get_installation_search_session)

    @abc.abstractmethod
    def get_installation_search_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation search service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_search_session``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationSearchSession

    @abc.abstractmethod
    def get_installation_management_session(self):
        """Gets the ``OsidSession`` associated with the installation management service.

        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_management()`` is ``true``.*

        """
        return  # osid.installation.InstallationManagementSession

    installation_management_session = property(fget=get_installation_management_session)

    @abc.abstractmethod
    def get_installation_management_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation management service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_admin_session``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_management()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationManagementSession

    @abc.abstractmethod
    def get_installation_update_session(self):
        """Gets the ``OsidSession`` associated with the installation update service.

        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_update()`` is ``true``.*

        """
        return  # osid.installation.InstallationUpdateSession

    installation_update_session = property(fget=get_installation_update_session)

    @abc.abstractmethod
    def get_installation_update_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation update service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_update_session``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_update()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationUpdateSession

    @abc.abstractmethod
    def get_installation_notification_session(self, installation_receiver):
        """Gets the notification session for notifications pertaining to installation changes.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :return: an ``InstallationNotificationSession``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NullArgument`` -- ``installation_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_notification()`` is ``true``.*

        """
        return  # osid.installation.InstallationNotificationSession

    @abc.abstractmethod
    def get_installation_notification_session_for_site(self, installation_receiver, site_id):
        """Gets the ``OsidSession`` associated with the installation notification service for the given site.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_notification_session``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``installation_receiver`` or ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationNotificationSession

    @abc.abstractmethod
    def get_site_lookup_session(self):
        """Gets the ``OsidSession`` associated with the site lookup service.

        :return: a ``SiteLookupSession``
        :rtype: ``osid.installation.SiteLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_site_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_site_lookup()`` is ``true``.*

        """
        return  # osid.installation.SiteLookupSession

    site_lookup_session = property(fget=get_site_lookup_session)

    @abc.abstractmethod
    def get_package_lookup_session(self):
        """Gets the ``OsidSession`` associated with the package lookup service.

        :return: a ``PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_lookup()`` is ``true``.*

        """
        return  # osid.installation.PackageLookupSession

    package_lookup_session = property(fget=get_package_lookup_session)

    @abc.abstractmethod
    def get_package_lookup_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package lookup service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageLookupSession

    @abc.abstractmethod
    def get_package_query_session(self):
        """Gets the ``OsidSession`` associated with the package query service.

        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuerySession

    package_query_session = property(fget=get_package_query_session)

    @abc.abstractmethod
    def get_package_query_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package query service for the given depot.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``NotFound`` -- no ``Depot`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.installation.PackageQuerySession

    @abc.abstractmethod
    def get_package_search_session(self):
        """Gets the ``OsidSession`` associated with the package search service.

        :return: a ``PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_search()`` is ``true``.*

        """
        return  # osid.installation.PackageSearchSession

    package_search_session = property(fget=get_package_search_session)

    @abc.abstractmethod
    def get_package_search_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package search service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageSearchSession

    @abc.abstractmethod
    def get_package_admin_session(self):
        """Gets the ``OsidSession`` associated with the package administration service.

        :return: a ``PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_admin()`` is ``true``.*

        """
        return  # osid.installation.PackageAdminSession

    package_admin_session = property(fget=get_package_admin_session)

    @abc.abstractmethod
    def get_package_admin_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package admin service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageAdminSession

    @abc.abstractmethod
    def get_package_notification_session(self, package_receiver):
        """Gets the notification session for notifications pertaining to package changes.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :return: a ``PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NullArgument`` -- ``package_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_notification()`` is ``true``.*

        """
        return  # osid.installation.PackageNotificationSession

    @abc.abstractmethod
    def get_package_notification_session_for_depot(self, package_receiver, depot_id):
        """Gets the ``OsidSession`` associated with the package notification service for the given depot.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``package_receiver`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageNotificationSession

    @abc.abstractmethod
    def get_package_depot_session(self):
        """Gets the session for retrieving package to depot mappings.

        :return: a ``PackageDepotSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_depot()`` is ``true``.*

        """
        return  # osid.installation.PackageDepotSession

    package_depot_session = property(fget=get_package_depot_session)

    @abc.abstractmethod
    def get_package_depot_assignment_session(self):
        """Gets the session for assigning package to depot mappings.

        :return: a ``PackageDepotAssignmentSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_depot_assignment()`` is ``true``.*

        """
        return  # osid.installation.PackageDepotSession

    package_depot_assignment_session = property(fget=get_package_depot_assignment_session)

    @abc.abstractmethod
    def get_package_smart_depot_session(self, depot_id):
        """Gets the session for managing dynamic package depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: a ``PackageSmartDepotSession``
        :rtype: ``osid.installation.PackageSmartDepotSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_smart_depot()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_smart_depot()`` is ``true``.*

        """
        return  # osid.installation.PackageSmartDepotSession

    @abc.abstractmethod
    def get_depot_lookup_session(self):
        """Gets the OsidSession associated with the depot lookup service.

        :return: a ``DepotLookupSession``
        :rtype: ``osid.installation.DepotLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_lookup()`` is true.*

        """
        return  # osid.installation.DepotLookupSession

    depot_lookup_session = property(fget=get_depot_lookup_session)

    @abc.abstractmethod
    def get_depot_query_session(self):
        """Gets the depot query session.

        :return: a ``DepotQuerySession``
        :rtype: ``osid.installation.DepotQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_query()`` is ``true``.*

        """
        return  # osid.installation.DepotQuerySession

    depot_query_session = property(fget=get_depot_query_session)

    @abc.abstractmethod
    def get_depot_search_session(self):
        """Gets the OsidSession associated with the depot search service.

        :return: a ``DepotSearchSession``
        :rtype: ``osid.installation.DepotSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_search()`` is true.*

        """
        return  # osid.installation.DepotSearchSession

    depot_search_session = property(fget=get_depot_search_session)

    @abc.abstractmethod
    def get_depot_admin_session(self):
        """Gets the OsidSession associated with the depot administration service.

        :return: a ``DepotAdminSession``
        :rtype: ``osid.installation.DepotAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_admin()`` is true.*

        """
        return  # osid.installation.DepotAdminSession

    depot_admin_session = property(fget=get_depot_admin_session)

    @abc.abstractmethod
    def get_depot_notification_session(self, depot_receiver):
        """Gets the notification session for notifications pertaining to depot service changes.

        :param depot_receiver: the depot receiver
        :type depot_receiver: ``osid.installation.DepotReceiver``
        :return: a ``DepotNotificationSession``
        :rtype: ``osid.installation.DepotNotificationSession``
        :raise: ``NullArgument`` -- ``depot_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_notification()`` is true.*

        """
        return  # osid.installation.DepotNotificationSession

    @abc.abstractmethod
    def get_depot_hierarchy_session(self):
        """Gets the session traversing depot hierarchies.

        :return: a ``DepotHierarchySession``
        :rtype: ``osid.installation.DepotHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_hierarchy()`` is true.*

        """
        return  # osid.installation.DepotHierarchySession

    depot_hierarchy_session = property(fget=get_depot_hierarchy_session)

    @abc.abstractmethod
    def get_depot_hierarchy_design_session(self):
        """Gets the session designing depot hierarchies.

        :return: a ``DepotHierarchyDesignSession``
        :rtype: ``osid.installation.DepotHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_hierarchy_design()`` is true.*

        """
        return  # osid.installation.DepotHierarchyDesignSession

    depot_hierarchy_design_session = property(fget=get_depot_hierarchy_design_session)

    @abc.abstractmethod
    def get_installation_batch_manager(self):
        """Gets an ``InstallationBatchManager``.

        :return: an ``InstallationBatchManager``
        :rtype: ``osid.installation.batch.InstallationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_batch()`` is true.*

        """
        return  # osid.installation.batch.InstallationBatchManager

    installation_batch_manager = property(fget=get_installation_batch_manager)


class InstallationProxyManager:
    """The installation manager provides access to package installation sessions and provides interoperability tests for
        various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from server environments. The sessions included in this manager are:

      * ``InstallationLookupSession:`` a session to look up local
        installations
      * ``InstallationQuerySession:`` a session to query local
        installations ``None``
      * ``InstallationSearchSession:`` a session to search local
        installations
      * ``InstallationManagementSession:`` a session to install and
        remove packages ``None``
      * ``InstallationUpdateSession:`` a session to get package updates
      * ``InstallationNotificationSession`` a session for subscribing to
        new or deleted installations
      * ``SiteLookupSession:`` a session for listing installation sites

      * ``PackageLookupSession:`` a session to look up packages ``None``
      * ``PackageQuerySession:`` a session to query packages
      * ``PackageSearchSession:`` a session to search packages
      * ``PackageAdminSession:`` a session to create, modify and delete
        packages ``None``
      * ``PackageNotificationSession: a`` session to receive messages
        pertaining to package ```` changes
      * ``PackageDepotSession:`` a session for retrieving package and
        depot mappings
      * ``PackageDepotAssignmentSession:`` a session for managing
        package and depot mappings
      * ``PackageSmartDepotSession:`` a session for managing smart
        depots of packages

      * ``DepotLookupSession:`` a session to lookup depots
      * ``DepotQuerySession:`` a session to query depots
      * ``DepotSearchSession`` : a session to search depots
      * ``DepotAdminSession`` : a session to create, modify and delete
        depots
      * ``DepotNotificationSession`` : a session to receive messages
        pertaining to depot changes
      * ``DepotHierarchySession:`` a session to traverse the depot
        hierarchy
      * ``DepotHierarchyDesignSession:`` a session to manage the depot
        hierarchy

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_installation_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationLookupSession``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_lookup()`` is ``true``.*

        """
        return  # osid.installation.InstallationLookupSession

    @abc.abstractmethod
    def get_installation_lookup_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation lookup service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_lookup_session``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationLookupSession

    @abc.abstractmethod
    def get_installation_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationQuerySession``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_query()`` is ``true``.*

        """
        return  # osid.installation.InstallationQuerySession

    @abc.abstractmethod
    def get_installation_query_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation query service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_query_session``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationQuerySession

    @abc.abstractmethod
    def get_installation_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationSearchSession``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_search()`` is ``true``.*

        """
        return  # osid.installation.InstallationSearchSession

    @abc.abstractmethod
    def get_installation_search_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation search service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_search_session``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationSearchSession

    @abc.abstractmethod
    def get_installation_management_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation management service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_management()`` is ``true``.*

        """
        return  # osid.installation.InstallationManagementSession

    @abc.abstractmethod
    def get_installation_management_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation management service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_admin_session``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_management()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationManagementSession

    @abc.abstractmethod
    def get_installation_update_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation update service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_update()`` is ``true``.*

        """
        return  # osid.installation.InstallationUpdateSession

    @abc.abstractmethod
    def get_installation_update_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation update service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_update_session``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_update()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationUpdateSession

    @abc.abstractmethod
    def get_installation_notification_session(self, installation_receiver, proxy):
        """Gets the notification session for notifications pertaining to installation changes.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationNotificationSession``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NullArgument`` -- ``installation_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_notification()`` is ``true``.*

        """
        return  # osid.installation.InstallationNotificationSession

    @abc.abstractmethod
    def get_installation_notification_session_for_site(self, installation_receiver, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation notification service for the given site.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_notification_session``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``installation_receiver, site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.InstallationNotificationSession

    @abc.abstractmethod
    def get_site_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the site lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SiteLookupSession``
        :rtype: ``osid.installation.SiteLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_site_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_site_lookup()`` is ``true``.*

        """
        return  # osid.installation.SiteLookupSession

    @abc.abstractmethod
    def get_package_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_lookup()`` is ``true``.*

        """
        return  # osid.installation.PackageLookupSession

    @abc.abstractmethod
    def get_package_lookup_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package lookup service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageLookupSession

    @abc.abstractmethod
    def get_package_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuerySession

    @abc.abstractmethod
    def get_package_query_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package query service for the given depot.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``NotFound`` -- no ``Depot`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.installation.PackageQuerySession

    @abc.abstractmethod
    def get_package_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_search()`` is ``true``.*

        """
        return  # osid.installation.PackageSearchSession

    @abc.abstractmethod
    def get_package_search_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package search service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageSearchSession

    @abc.abstractmethod
    def get_package_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_admin()`` is ``true``.*

        """
        return  # osid.installation.PackageAdminSession

    @abc.abstractmethod
    def get_package_admin_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package admin service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageAdminSession

    @abc.abstractmethod
    def get_package_notification_session(self, package_receiver, proxy):
        """Gets the notification session for notifications pertaining to package changes.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NullArgument`` -- ``package_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_notification()`` is ``true``.*

        """
        return  # osid.installation.PackageNotificationSession

    @abc.abstractmethod
    def get_package_notification_session_for_depot(self, package_receiver, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package notification service for the given depot.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``package_receiver, depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.installation.PackageNotificationSession

    @abc.abstractmethod
    def get_package_depot_session(self, proxy):
        """Gets the session for retrieving package to depot mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageDepotSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_depot()`` is ``true``.*

        """
        return  # osid.installation.PackageDepotSession

    @abc.abstractmethod
    def get_package_depot_assignment_session(self, proxy):
        """Gets the session for assigning package to depot mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageDepotAssignmentSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_depot_assignment()`` is ``true``.*

        """
        return  # osid.installation.PackageDepotSession

    @abc.abstractmethod
    def get_package_smart_depot_session(self, depot_id, proxy):
        """Gets the session for managing dynamic package depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageSmartDepotSession``
        :rtype: ``osid.installation.PackageSmartDepotSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_smart_depot()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_smart_depot()`` is ``true``.*

        """
        return  # osid.installation.PackageSmartDepotSession

    @abc.abstractmethod
    def get_depot_lookup_session(self, proxy):
        """Gets the OsidSession associated with the depot lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotLookupSession``
        :rtype: ``osid.installation.DepotLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_lookup()`` is true.*

        """
        return  # osid.installation.DepotLookupSession

    @abc.abstractmethod
    def get_depot_query_session(self, proxy):
        """Gets the depot query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotQuerySession``
        :rtype: ``osid.installation.DepotQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_query()`` is ``true``.*

        """
        return  # osid.installation.DepotQuerySession

    @abc.abstractmethod
    def get_depot_search_session(self, proxy):
        """Gets the OsidSession associated with the depot search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotSearchSession``
        :rtype: ``osid.installation.DepotSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_search()`` is true.*

        """
        return  # osid.installation.DepotSearchSession

    @abc.abstractmethod
    def get_depot_admin_session(self, proxy):
        """Gets the OsidSession associated with the depot administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotAdminSession``
        :rtype: ``osid.installation.DepotAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_admin()`` is true.*

        """
        return  # osid.installation.DepotAdminSession

    @abc.abstractmethod
    def get_depot_notification_session(self, depot_receiver, proxy):
        """Gets the notification session for notifications pertaining to depot service changes.

        :param depot_receiver: the depot receiver
        :type depot_receiver: ``osid.installation.DepotReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotNotificationSession``
        :rtype: ``osid.installation.DepotNotificationSession``
        :raise: ``NullArgument`` -- ``depot_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_notification()`` is true.*

        """
        return  # osid.installation.DepotNotificationSession

    @abc.abstractmethod
    def get_depot_hierarchy_session(self, proxy):
        """Gets the session traversing depot hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotHierarchySession``
        :rtype: ``osid.installation.DepotHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_hierarchy()`` is true.*

        """
        return  # osid.installation.DepotHierarchySession

    @abc.abstractmethod
    def get_depot_hierarchy_design_session(self, proxy):
        """Gets the session designing depot hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotHierarchyDesignSession``
        :rtype: ``osid.installation.DepotHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_hierarchy_design()`` is true.*

        """
        return  # osid.installation.DepotHierarchyDesignSession

    @abc.abstractmethod
    def get_installation_batch_proxy_manager(self):
        """Gets an ``InstallationBatchProxyManager``.

        :return: an ``InstallationBatchProxyManager``
        :rtype: ``osid.installation.batch.InstallationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_batch()`` is true.*

        """
        return  # osid.installation.batch.InstallationBatchProxyManager

    installation_batch_proxy_manager = property(fget=get_installation_batch_proxy_manager)
