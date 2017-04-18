"""Implementations of installation abstract base class queries."""
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


class PackageQuery:
    """This is the query for searching packages.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_version(self, version, match):
        """Matches a version.

        :param version: the version
        :type version: ``osid.installation.Version``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``version`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- version type not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_version(self, match):
        """Matches packages with any version.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_version_terms(self):
        """Clears the version query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    version_terms = property(fdel=clear_version_terms)

    @abc.abstractmethod
    def match_version_since(self, version, match):
        """Matches packages with versions including and more recent than the given version.

        :param version: the version
        :type version: ``osid.installation.Version``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``version`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- version type not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_version_since_terms(self):
        """Clears the version since query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    version_since_terms = property(fdel=clear_version_since_terms)

    @abc.abstractmethod
    def match_copyright(self, copyright_, string_match_type, match):
        """Matches the copyright.

        :param copyright: copyright string
        :type copyright: ``string``
        :param string_match_type: string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``copyright`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``copyright`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_copyright(self, match):
        """Matches packages with any copyright.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_copyright_terms(self):
        """Clears the copyright query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_terms = property(fdel=clear_copyright_terms)

    @abc.abstractmethod
    def match_requires_license_acknowledgement(self, match):
        """Matches packages that require license acknowledgement.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_requires_license_acknowledgement(self, match):
        """Matches packages that have any acknowledgement value.

        :param match: ``true`` to match packages that have any acknowledgement value, ``false`` for to match packages
        that have no value
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_requires_license_acknowledgement_terms(self):
        """Clears the license acknowledgement query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    requires_license_acknowledgement_terms = property(fdel=clear_requires_license_acknowledgement_terms)

    @abc.abstractmethod
    def match_creator_id(self, resource_id, match):
        """Sets the creator resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_creator_id_terms(self):
        """Clears the creator ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    creator_id_terms = property(fdel=clear_creator_id_terms)

    @abc.abstractmethod
    def supports_creator_query(self):
        """Tests if a ``ResourceQuery`` is available for querying creators.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_creator_query(self):
        """Gets the query for a creator resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the creator resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_creator_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_creator_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    creator_query = property(fget=get_creator_query)

    @abc.abstractmethod
    def match_any_creator(self, match):
        """Matches packages with any creator.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_creator_terms(self):
        """Clears the creator query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    creator_terms = property(fdel=clear_creator_terms)

    @abc.abstractmethod
    def match_release_date(self, from_, to, match):
        """Matches the release date between the given times inclusive.

        :param from: starting range
        :type from: ``osid.calendaring.DateTime``
        :param to: ending range
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is ``less than from``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_release_date(self, match):
        """Matches packages that have any release date.

        :param match: ``true`` to match packages with any release date, ``false`` to match packages with no release date
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_release_date_terms(self):
        """Clears the release date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    release_date_terms = property(fdel=clear_release_date_terms)

    @abc.abstractmethod
    def match_dependency_id(self, package_id, match):
        """Sets the package ``Id`` to match packages on which a package depends.

        :param package_id: a state ``Id``
        :type package_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependency_id_terms(self):
        """Clears the dependency ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependency_id_terms = property(fdel=clear_dependency_id_terms)

    @abc.abstractmethod
    def supports_dependency_query(self):
        """Tests if a ``PackageQuery`` is available.

        :return: ``true`` if a package query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_dependency_query(self):
        """Gets the query for a dependency.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``Unimplemented`` -- ``supports_dependency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_dependency_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuery

    dependency_query = property(fget=get_dependency_query)

    @abc.abstractmethod
    def match_any_dependency(self, match):
        """Matches packages that have any dependency.

        :param match: ``true`` to match packages with any dependency, ``false`` to match packages with no dependencies
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependency_terms(self):
        """Clears the dependency query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependency_terms = property(fdel=clear_dependency_terms)

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
        """Matches packages that have any url.

        :param match: ``true`` to match packages with any url, ``false`` to match packages with no url
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_url_terms(self):
        """Clears the url query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    url_terms = property(fdel=clear_url_terms)

    @abc.abstractmethod
    def match_installation_id(self, installation_id, match):
        """Sets the installation ``Id`` for this query.

        :param installation_id: an installation ``Id``
        :type installation_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_installation_id_terms(self):
        """Clears the installation ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    installation_id_terms = property(fdel=clear_installation_id_terms)

    @abc.abstractmethod
    def supports_installation_query(self):
        """Tests if an ``InstallationQuery`` is available.

        :return: ``true`` if an installation query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_query(self):
        """Gets the query for an installation.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the installation query
        :rtype: ``osid.installation.InstallationQuery``
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_query()`` is ``true``.*

        """
        return  # osid.installation.InstallationQuery

    installation_query = property(fget=get_installation_query)

    @abc.abstractmethod
    def match_any_installation(self, match):
        """Matches any packages that are installed.

        :param match: ``true`` to match installed packages, ``false`` for uninstalled packages
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_installation_terms(self):
        """Clears the installation query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    installation_terms = property(fdel=clear_installation_terms)

    @abc.abstractmethod
    def match_dependent_id(self, package_id, match):
        """Sets the package ``Id`` to match packages on which other packages depend.

        :param package_id: a package ``Id``
        :type package_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependent_id_terms(self):
        """Clears the dependent ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependent_id_terms = property(fdel=clear_dependent_id_terms)

    @abc.abstractmethod
    def supports_dependent_query(self):
        """Tests if a ``PackageQuery`` is available.

        :return: ``true`` if a package query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_dependent_query(self):
        """Gets the query for a dependent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``Unimplemented`` -- ``supports_dependent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_dependent_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuery

    dependent_query = property(fget=get_dependent_query)

    @abc.abstractmethod
    def match_any_dependent(self, match):
        """Matches packages that have any depenents.

        :param match: ``true`` to match packages with any dependents, ``false`` to match packages with no dependents
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependent_terms(self):
        """Clears the dependent query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependent_terms = property(fdel=clear_dependent_terms)

    @abc.abstractmethod
    def match_versioned_package_id(self, package_id, match):
        """Sets the package ``Id`` to match packages in the version chain.

        :param package_id: a state ``Id``
        :type package_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_versioned_package_id_terms(self):
        """Clears the versioned package ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    versioned_package_id_terms = property(fdel=clear_versioned_package_id_terms)

    @abc.abstractmethod
    def supports_versioned_package_query(self):
        """Tests if a ``PackageQuery`` is available.

        :return: ``true`` if a package query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_versioned_package_query(self):
        """Gets the query for a version chain.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``Unimplemented`` -- ``supports_version_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_version_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuery

    versioned_package_query = property(fget=get_versioned_package_query)

    @abc.abstractmethod
    def match_any_versioned_package(self, match):
        """Matches packages that have any versions.

        :param match: ``true`` to match packages with any versions, ``false`` to match packages with no versions
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_versioned_package_terms(self):
        """Clears the versioned package query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    versioned_package_terms = property(fdel=clear_versioned_package_terms)

    @abc.abstractmethod
    def match_installation_content_id(self, installation_content_id, match):
        """Sets the installation content ``Id`` for this query.

        :param installation_content_id: the installation content ``Id``
        :type installation_content_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``installation_content_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_installation_content_id_terms(self):
        """Clears the installation content ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    installation_content_id_terms = property(fdel=clear_installation_content_id_terms)

    @abc.abstractmethod
    def supports_installation_content_query(self):
        """Tests if an ``InstallationContentQuery`` is available.

        :return: ``true`` if an installation content query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_content_query(self):
        """Gets the query for the installation content.

        Multiple queries can be retrieved for a nested ``OR`` term.

        :return: the installation content query
        :rtype: ``osid.installation.InstallationContentQuery``
        :raise: ``Unimplemented`` -- ``supports_installation_content_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_content_query()`` is ``true``.*

        """
        return  # osid.installation.InstallationContentQuery

    installation_content_query = property(fget=get_installation_content_query)

    @abc.abstractmethod
    def match_any_installation_content(self, match):
        """Matches packages with any content.

        :param match: ``true`` to match packages with any content, ``false`` to match packages with no content
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_installation_content_terms(self):
        """Clears the installation content terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    installation_content_terms = property(fdel=clear_installation_content_terms)

    @abc.abstractmethod
    def match_depot_id(self, depot_id, match):
        """Sets the depot ``Id`` for this query.

        :param depot_id: a depot ``Id``
        :type depot_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_depot_id_terms(self):
        """Clears the depot ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    depot_id_terms = property(fdel=clear_depot_id_terms)

    @abc.abstractmethod
    def supports_depot_query(self):
        """Tests if a ``DepotQuery`` is available for querying resources.

        :return: ``true`` if a depot query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_query(self):
        """Gets the query for a depot.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the depot query
        :rtype: ``osid.installation.DepotQuery``
        :raise: ``Unimplemented`` -- ``supports_depot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_depot_query()`` is ``true``.*

        """
        return  # osid.installation.DepotQuery

    depot_query = property(fget=get_depot_query)

    @abc.abstractmethod
    def clear_depot_terms(self):
        """Clears the depot query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    depot_terms = property(fdel=clear_depot_terms)

    @abc.abstractmethod
    def get_package_query_record(self, package_record_type):
        """Gets the package query record corresponding to the given ``Package`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param package_record_type: a package query record type
        :type package_record_type: ``osid.type.Type``
        :return: the package query record
        :rtype: ``osid.installation.records.PackageQueryRecord``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.PackageQueryRecord


class InstallationContentQuery:
    """This is the query for searching installation contents.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

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
    def get_installation_content_query_record(self, installation_content_record_type):
        """Gets the installation content query record corresponding to the given ``InstallationContent`` record
        ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param installation_content_record_type: an installation content query record type
        :type installation_content_record_type: ``osid.type.Type``
        :return: the installation content query record
        :rtype: ``osid.installation.records.InstallationContentQueryRecord``
        :raise: ``NullArgument`` -- ``installation_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationContentQueryRecord


class DepotQuery:
    """This is the query for searching depots.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_package_id(self, package_id, match):
        """Sets the package ``Id`` for this query.

        :param package_id: a package ``Id``
        :type package_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_package_id_terms(self):
        """Clears the package ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    package_id_terms = property(fdel=clear_package_id_terms)

    @abc.abstractmethod
    def supports_package_query(self):
        """Tests if a ``PackageQuery`` is available.

        :return: ``true`` if a package query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_query(self):
        """Gets the query for a package.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``Unimplemented`` -- ``supports_package_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuery

    package_query = property(fget=get_package_query)

    @abc.abstractmethod
    def match_any_package(self, match):
        """Matches depots that have any package.

        :param match: ``true`` to match depots with any packages, ``false`` to match depots with no packages
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_package_terms(self):
        """Clears the package query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    package_terms = property(fdel=clear_package_terms)

    @abc.abstractmethod
    def match_ancestor_depot_id(self, depot_id, match):
        """Sets the depot ``Id`` for this query to match depots that have the specified depot as an ancestor.

        :param depot_id: a depot ``Id``
        :type depot_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_depot_id_terms(self):
        """Clears the ancestor depot ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_depot_id_terms = property(fdel=clear_ancestor_depot_id_terms)

    @abc.abstractmethod
    def supports_ancestor_depot_query(self):
        """Tests if a ``DepotQuery`` is available.

        :return: ``true`` if a depot query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_depot_query(self):
        """Gets the query for a Depot.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the depot query
        :rtype: ``osid.installation.DepotQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_depot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_depot_query()`` is ``true``.*

        """
        return  # osid.installation.DepotQuery

    ancestor_depot_query = property(fget=get_ancestor_depot_query)

    @abc.abstractmethod
    def match_any_ancestor_depot(self, match):
        """Matches depots with any ancestor.

        :param match: ``true`` to match depots with any ancestor, ``false`` to match root depots
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_depot_terms(self):
        """Clears the ancestor depot query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_depot_terms = property(fdel=clear_ancestor_depot_terms)

    @abc.abstractmethod
    def match_descendant_depot_id(self, depot_id, match):
        """Sets the depot ``Id`` for this query to match depots that have the specified depot as a descendant.

        :param depot_id: a depot ``Id``
        :type depot_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_depot_id_terms(self):
        """Clears the descendant depot ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_depot_id_terms = property(fdel=clear_descendant_depot_id_terms)

    @abc.abstractmethod
    def supports_descendant_depot_query(self):
        """Tests if a ``DepotQuery`` is available.

        :return: ``true`` if a depot query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_depot_query(self):
        """Gets the query for a Depot.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the depot query
        :rtype: ``osid.installation.DepotQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_depot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_depot_query()`` is ``true``.*

        """
        return  # osid.installation.DepotQuery

    descendant_depot_query = property(fget=get_descendant_depot_query)

    @abc.abstractmethod
    def match_any_descendant_depot(self, match):
        """Matches depots with any descendant.

        :param match: ``true`` to match depots with any descendant, ``false`` to match leaf depots
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_depot_terms(self):
        """Clears the descendant depot query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_depot_terms = property(fdel=clear_descendant_depot_terms)

    @abc.abstractmethod
    def get_depot_query_record(self, depot_record_type):
        """Gets the depot query record corresponding to the given ``Depot`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the depot query record
        :rtype: ``osid.installation.records.DepotQueryRecord``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.DepotQueryRecord


class InstallationQuery:
    """This is the query for searching installations.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_site_id(self, site_id, match):
        """Sets the site ``Id`` for this query.

        :param site_id: a site ``Id``
        :type site_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``site_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_site_id_terms(self):
        """Clears the site ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    site_id_terms = property(fdel=clear_site_id_terms)

    @abc.abstractmethod
    def supports_site_query(self):
        """Tests if a ``SiteQuery`` is available for querying sites.

        :return: ``true`` if a site query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_site_query(self):
        """Gets the query for a site.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the site query
        :rtype: ``osid.installation.SiteQuery``
        :raise: ``Unimplemented`` -- ``supports_site_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_site_query()`` is ``true``.*

        """
        return  # osid.installation.SiteQuery

    site_query = property(fget=get_site_query)

    @abc.abstractmethod
    def clear_site_terms(self):
        """Clears the site query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    site_terms = property(fdel=clear_site_terms)

    @abc.abstractmethod
    def match_package_id(self, package_id, match):
        """Sets the package ``Id`` for this query.

        :param package_id: a package ``Id``
        :type package_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_package_id_terms(self):
        """Clears the package ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    package_id_terms = property(fdel=clear_package_id_terms)

    @abc.abstractmethod
    def supports_package_query(self):
        """Tests if a ``PackageQuery`` is available for querying agents.

        :return: ``true`` if a package query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_query(self):
        """Gets the query for a package.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``Unimplemented`` -- ``supports_package_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_package_query()`` is ``true``.*

        """
        return  # osid.installation.PackageQuery

    package_query = property(fget=get_package_query)

    @abc.abstractmethod
    def clear_package_terms(self):
        """Clears the package query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    package_terms = property(fdel=clear_package_terms)

    @abc.abstractmethod
    def match_install_date(self, from_, to, match):
        """Matches the install date between the given times inclusive.

        :param from: starting range
        :type from: ``osid.calendaring.DateTime``
        :param to: ending range
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is ``less than from``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_install_date_terms(self):
        """Clears the install date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    install_date_terms = property(fdel=clear_install_date_terms)

    @abc.abstractmethod
    def match_agent_id(self, agent_id, match):
        """Sets the agent ``Id`` for this query.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_id_terms = property(fdel=clear_agent_id_terms)

    @abc.abstractmethod
    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available for querying agents.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    @abc.abstractmethod
    def clear_agent_terms(self):
        """Clears the agent query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_terms = property(fdel=clear_agent_terms)

    @abc.abstractmethod
    def match_last_check_date(self, from_, to, match):
        """Matches the last checked date between the given times inclusive.

        :param from: starting range
        :type from: ``osid.calendaring.DateTime``
        :param to: ending range
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is ``less than from``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_last_check_date_terms(self):
        """Clears the last check date query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    last_check_date_terms = property(fdel=clear_last_check_date_terms)

    @abc.abstractmethod
    def get_installation_query_record(self, installation_record_type):
        """Gets the installation query record corresponding to the given ``Installation`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param installation_record_type: an installation query record type
        :type installation_record_type: ``osid.type.Type``
        :return: the installation query record
        :rtype: ``osid.installation.records.InstallationQueryRecord``
        :raise: ``NullArgument`` -- ``installation_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationQueryRecord


class SiteQuery:
    """This is the query for searching installations.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_installation_id(self, installation_id, match):
        """Sets the installation ``Id`` for this query.

        :param installation_id: a site ``Id``
        :type installation_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_installation_id_terms(self):
        """Clears the installation ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    installation_id_terms = property(fdel=clear_installation_id_terms)

    @abc.abstractmethod
    def supports_installation_query(self):
        """Tests if an ``InstallationQuery`` is available for querying installations.

        :return: ``true`` if an installation query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_query(self):
        """Gets the query for an installation.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the site query
        :rtype: ``osid.installation.SiteQuery``
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_installation_query()`` is ``true``.*

        """
        return  # osid.installation.SiteQuery

    installation_query = property(fget=get_installation_query)

    @abc.abstractmethod
    def match_any_installation(self, match):
        """Matches sites with any installation.

        :param match: ``true`` to match sites with any package, ``false`` to match sites with no packages
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_installation_terms(self):
        """Clears the installation query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    installation_terms = property(fdel=clear_installation_terms)

    @abc.abstractmethod
    def get_site_query_record(self, site_record_type):
        """Gets the site query record corresponding to the given ``Site`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param site_record_type: a site query record type
        :type site_record_type: ``osid.type.Type``
        :return: the site query record
        :rtype: ``osid.installation.records.SiteQueryRecord``
        :raise: ``NullArgument`` -- ``site_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(site_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.SiteQueryRecord
