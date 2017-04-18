"""Implementations of installation abstract base class search_orders."""
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


class PackageSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_version(self, style):
        """Specified a preference for ordering results by the version.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_copyright(self, style):
        """Specified a preference for ordering results by the copyright.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_requires_license_acknowledgement(self, style):
        """Specified a preference for ordering results by the license acknowledgement flag.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_creator(self, style):
        """Specified a preference for ordering results by the creator.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_creator_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available for creator resources.

        :return: ``true`` if a creator resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_creator_search_order(self):
        """Gets the search order for a creator resource.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_creator_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_creator_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    creator_search_order = property(fget=get_creator_search_order)

    @abc.abstractmethod
    def order_by_release_date(self, style):
        """Specified a preference for ordering results by the release date.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_url(self, style):
        """Specified a preference for ordering results by the url.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_package_search_order_record(self, package_record_type):
        """Gets the package search order record corresponding to the given package record ``Type``.

        Multiple retrievals return the same underlying object.

        :param package_record_type: a package record type
        :type package_record_type: ``osid.type.Type``
        :return: the package search order record
        :rtype: ``osid.installation.records.PackageSearchOrderRecord``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.PackageSearchOrderRecord


class DepotSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_search_order_record(self, depot_record_type):
        """Gets the depot search order record corresponding to the given depot record ``Type``.

        Multiple retrievals return the same underlying object.

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the depot search order record
        :rtype: ``osid.installation.records.DepotSearchOrderRecord``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.DepotSearchOrderRecord


class InstallationSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_site(self, style):
        """Specified a preference for ordering results by the site.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_site_search_order(self):
        """Tests if a ``SiteSearchOrder`` is available for sites.

        :return: ``true`` if a site search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_site_search_order(self):
        """Gets the search order for a site.

        :return: the site search order
        :rtype: ``osid.installation.SiteSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_site_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_site_search_order()`` is ``true``.*

        """
        return  # osid.installation.SiteSearchOrder

    site_search_order = property(fget=get_site_search_order)

    @abc.abstractmethod
    def order_by_package(self, style):
        """Specified a preference for ordering results by the package.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_package_search_order(self):
        """Tests if a ``PackageSearchOrder`` is available for packages.

        :return: ``true`` if a package search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_search_order(self):
        """Gets the search order for a package.

        :return: the package search order
        :rtype: ``osid.installation.PackageSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_package_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_search_order()`` is ``true``.*

        """
        return  # osid.installation.PackageSearchOrder

    package_search_order = property(fget=get_package_search_order)

    @abc.abstractmethod
    def order_by_install_date(self, style):
        """Specified a preference for ordering results by the install date.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_agent(self, style):
        """Specified a preference for ordering results by the agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_agent_search_order(self):
        """Tests if an ``AgenteSearchOrder`` is available for agents.

        :return: ``true`` if an agent search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_search_order(self):
        """Gets the search order for an agent.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_agent_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_search_order()`` is ``true``.*

        """
        return  # osid.authentication.AgentSearchOrder

    agent_search_order = property(fget=get_agent_search_order)

    @abc.abstractmethod
    def order_by_last_check_date(self, style):
        """Specified a preference for ordering results by the last checked date.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_installation_search_order_record(self, installation_record_type):
        """Gets the installation search order record corresponding to the given installation record ``Type``.

        Multiple retrievals return the same underlying object.

        :param installation_record_type: an installation record type
        :type installation_record_type: ``osid.type.Type``
        :return: the installation search order record
        :rtype: ``osid.installation.records.InstallationSearchOrderRecord``
        :raise: ``NullArgument`` -- ``installation_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationSearchOrderRecord


class SiteSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_search_order_record(self, site_record_type):
        """Gets the site search order record corresponding to the given package record ``Type``.

        Multiple retrievals return the same underlying object.

        :param site_record_type: a site record type
        :type site_record_type: ``osid.type.Type``
        :return: the site search order record
        :rtype: ``osid.installation.records.SiteSearchOrderRecord``
        :raise: ``NullArgument`` -- ``site_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(site_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.SiteSearchOrderRecord
