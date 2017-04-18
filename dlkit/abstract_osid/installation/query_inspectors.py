"""Implementations of installation abstract base class query_inspectors."""
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


class PackageQueryInspector:
    """This is the query inspector for examining package queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_version_terms(self):
        """Gets the version query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.VersionTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.VersionTerm

    version_terms = property(fget=get_version_terms)

    @abc.abstractmethod
    def get_version_since_terms(self):
        """Gets the version since terms.

        :return: the query terms
        :rtype: ``osid.search.terms.VersionTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.VersionTerm

    version_since_terms = property(fget=get_version_since_terms)

    @abc.abstractmethod
    def get_copyright_terms(self):
        """Gets the copyright terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    copyright_terms = property(fget=get_copyright_terms)

    @abc.abstractmethod
    def get_requires_license_acknowledgement_terms(self):
        """Gets the requires license acknowledgement terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    requires_license_acknowledgement_terms = property(fget=get_requires_license_acknowledgement_terms)

    @abc.abstractmethod
    def get_creator_id_terms(self):
        """Gets the creator ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    creator_id_terms = property(fget=get_creator_id_terms)

    @abc.abstractmethod
    def get_creator_terms(self):
        """Gets the creator query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    creator_terms = property(fget=get_creator_terms)

    @abc.abstractmethod
    def get_release_date_terms(self):
        """Gets the release date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    release_date_terms = property(fget=get_release_date_terms)

    @abc.abstractmethod
    def get_dependency_id_terms(self):
        """Gets the package dependency ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    dependency_id_terms = property(fget=get_dependency_id_terms)

    @abc.abstractmethod
    def get_dependency_terms(self):
        """Gets the package dependency query terms.

        :return: the query terms
        :rtype: ``osid.installation.PackageQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQueryInspector

    dependency_terms = property(fget=get_dependency_terms)

    @abc.abstractmethod
    def get_url_terms(self):
        """Gets the url terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    url_terms = property(fget=get_url_terms)

    @abc.abstractmethod
    def get_installation_id_terms(self):
        """Gets the installation ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    installation_id_terms = property(fget=get_installation_id_terms)

    @abc.abstractmethod
    def get_installation_terms(self):
        """Gets the installation query terms.

        :return: the query terms
        :rtype: ``osid.installation.InstallationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationQueryInspector

    installation_terms = property(fget=get_installation_terms)

    @abc.abstractmethod
    def get_dependent_id_terms(self):
        """Gets the dependent package ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    dependent_id_terms = property(fget=get_dependent_id_terms)

    @abc.abstractmethod
    def get_dependent_terms(self):
        """Gets the dependent package query terms.

        :return: the query terms
        :rtype: ``osid.installation.PackageQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQueryInspector

    dependent_terms = property(fget=get_dependent_terms)

    @abc.abstractmethod
    def get_versioned_package_id_terms(self):
        """Gets the versioned package ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    versioned_package_id_terms = property(fget=get_versioned_package_id_terms)

    @abc.abstractmethod
    def get_versioned_package_terms(self):
        """Gets the versioned package query terms.

        :return: the query terms
        :rtype: ``osid.installation.PackageQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQueryInspector

    versioned_package_terms = property(fget=get_versioned_package_terms)

    @abc.abstractmethod
    def get_installation_content_id_terms(self):
        """Gets the installation content ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    installation_content_id_terms = property(fget=get_installation_content_id_terms)

    @abc.abstractmethod
    def get_installation_content_terms(self):
        """Gets the installation content query terms.

        :return: the query terms
        :rtype: ``osid.installation.InstallationContentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContentQueryInspector

    installation_content_terms = property(fget=get_installation_content_terms)

    @abc.abstractmethod
    def get_depot_id_terms(self):
        """Gets the depot ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    depot_id_terms = property(fget=get_depot_id_terms)

    @abc.abstractmethod
    def get_depot_terms(self):
        """Gets the depot query terms.

        :return: the query terms
        :rtype: ``osid.installation.DepotQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotQueryInspector

    depot_terms = property(fget=get_depot_terms)

    @abc.abstractmethod
    def get_package_query_inspector_record(self, package_record_type):
        """Gets the package query inspector record corresponding to the given ``Package`` record ``Type``.

        :param package_record_type: a package query record type
        :type package_record_type: ``osid.type.Type``
        :return: the package query inspector record
        :rtype: ``osid.installation.records.PackageQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.PackageQueryInspectorRecord


class InstallationContentQueryInspector:
    """This is the query inspector for examining installation content queries."""
    __metaclass__ = abc.ABCMeta

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
    def get_installation_content_query_inspector_record(self, installation_content_record_type):
        """Gets the installation content query inspector record corresponding to the given ``InstallationContent``
        record ``Type``.

        :param installation_content_record_type: an installation content query record type
        :type installation_content_record_type: ``osid.type.Type``
        :return: the installation content query inspector record
        :rtype: ``osid.installation.records.InstallationContentQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``installation_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationContentQueryInspectorRecord


class DepotQueryInspector:
    """This is the query inspector for examining depot queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_package_id_terms(self):
        """Gets the package ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    package_id_terms = property(fget=get_package_id_terms)

    @abc.abstractmethod
    def get_package_terms(self):
        """Gets the package query terms.

        :return: the query terms
        :rtype: ``osid.installation.PackageQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQueryInspector

    package_terms = property(fget=get_package_terms)

    @abc.abstractmethod
    def get_ancestor_depot_id_terms(self):
        """Gets the ancestor depot ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_depot_id_terms = property(fget=get_ancestor_depot_id_terms)

    @abc.abstractmethod
    def get_ancestor_depot_terms(self):
        """Gets the ancestor depot query terms.

        :return: the query terms
        :rtype: ``osid.installation.DepotQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotQueryInspector

    ancestor_depot_terms = property(fget=get_ancestor_depot_terms)

    @abc.abstractmethod
    def get_descendant_depot_id_terms(self):
        """Gets the descendant depot ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_depot_id_terms = property(fget=get_descendant_depot_id_terms)

    @abc.abstractmethod
    def get_descendant_depot_terms(self):
        """Gets the descendant depot query terms.

        :return: the query terms
        :rtype: ``osid.installation.DepotQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotQueryInspector

    descendant_depot_terms = property(fget=get_descendant_depot_terms)

    @abc.abstractmethod
    def get_depot_query_inspector_record(self, depot_record_type):
        """Gets the depot query inspector record corresponding to the given ``Depot`` record ``Type``.

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the depot query inspector record
        :rtype: ``osid.installation.records.DepotQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.DepotQueryInspectorRecord


class InstallationQueryInspector:
    """This is the query inspector for examining installation queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id_terms(self):
        """Gets the site ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    site_id_terms = property(fget=get_site_id_terms)

    @abc.abstractmethod
    def get_site_terms(self):
        """Gets the site query terms.

        :return: the query terms
        :rtype: ``osid.installation.SiteQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.SiteQueryInspector

    site_terms = property(fget=get_site_terms)

    @abc.abstractmethod
    def get_package_id_terms(self):
        """Gets the package ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    package_id_terms = property(fget=get_package_id_terms)

    @abc.abstractmethod
    def get_package_terms(self):
        """Gets the package query terms.

        :return: the query terms
        :rtype: ``osid.installation.PackageQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQueryInspector

    package_terms = property(fget=get_package_terms)

    @abc.abstractmethod
    def get_install_date_terms(self):
        """Gets the install date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    install_date_terms = property(fget=get_install_date_terms)

    @abc.abstractmethod
    def get_agent_id_terms(self):
        """Gets the agent ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    agent_id_terms = property(fget=get_agent_id_terms)

    @abc.abstractmethod
    def get_agent_terms(self):
        """Gets the agent query terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQueryInspector

    agent_terms = property(fget=get_agent_terms)

    @abc.abstractmethod
    def get_last_check_date_terms(self):
        """Gets the check date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    last_check_date_terms = property(fget=get_last_check_date_terms)

    @abc.abstractmethod
    def get_installation_query_inspector_record(self, installation_record_type):
        """Gets the query inspector record corresponding to the given ``Installation`` record ``Type``.

        :param installation_record_type: an installation query record type
        :type installation_record_type: ``osid.type.Type``
        :return: the installation query inspector record
        :rtype: ``osid.installation.records.InstallationQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``installation_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationQueryInspectorRecord


class SiteQueryInspector:
    """This is the query inspector for examining installations queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_installation_id_terms(self):
        """Gets the installation ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    installation_id_terms = property(fget=get_installation_id_terms)

    @abc.abstractmethod
    def get_installation_terms(self):
        """Gets the installation query terms.

        :return: the query terms
        :rtype: ``osid.installation.InstallationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationQueryInspector

    installation_terms = property(fget=get_installation_terms)

    @abc.abstractmethod
    def get_site_query_inspector_record(self, site_record_type):
        """Gets the query inspector record corresponding to the given ``Site`` record ``Type``.

        :param site_record_type: a site query record type
        :type site_record_type: ``osid.type.Type``
        :return: the site query inspector record
        :rtype: ``osid.installation.records.SiteQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``site_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(site_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.SiteQueryInspectorRecord
