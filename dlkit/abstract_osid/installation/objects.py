"""Implementations of installation abstract base class objects."""
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


class Package:
    """A ``Package`` represents an installation bundle in a depot."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_version(self):
        """Gets the version of this package.

        :return: the package version
        :rtype: ``osid.installation.Version``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    version = property(fget=get_version)

    @abc.abstractmethod
    def get_copyright(self):
        """Gets the copyright of this package.

        :return: the copyright
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    copyright_ = property(fget=get_copyright)

    @abc.abstractmethod
    def requests_license_acknowledgement(self):
        """Tests if the provider requests acknowledgement of the license.

        :return: ``true`` if the consumer should acknowledge the terms in the license, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_creator_id(self):
        """Gets the creator or author of this package.

        :return: the creator ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    creator_id = property(fget=get_creator_id)

    @abc.abstractmethod
    def get_creator(self):
        """Gets the creator ``Id`` of this package.

        :return: the creator
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    creator = property(fget=get_creator)

    @abc.abstractmethod
    def get_release_date(self):
        """Gets the release date of this package.

        :return: the timestamp of this package
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    release_date = property(fget=get_release_date)

    @abc.abstractmethod
    def get_dependency_ids(self):
        """Gets the package ``Ids`` on which this package directly depends.

        :return: the package dependency ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    dependency_ids = property(fget=get_dependency_ids)

    @abc.abstractmethod
    def get_dependencies(self):
        """Gets the packages on which this package directly depends.

        :return: the package dependencies
        :rtype: ``osid.installation.PackageList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    dependencies = property(fget=get_dependencies)

    @abc.abstractmethod
    def get_url(self):
        """Gets a url for this package.

        The url may point to an external project or product site. If no
        url is available an empty string is returned.

        :return: the url for this package
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    url = property(fget=get_url)

    @abc.abstractmethod
    def get_installation_content_ids(self):
        """Gets the installation content ``Ids``.

        :return: the installation content ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    installation_content_ids = property(fget=get_installation_content_ids)

    @abc.abstractmethod
    def get_installation_contents(self):
        """Gets the installation contents.

        :return: the installation contents
        :rtype: ``osid.installation.InstallationContentList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContentList

    installation_contents = property(fget=get_installation_contents)

    @abc.abstractmethod
    def get_package_record(self, package_record_type):
        """Gets the package record corresponding to the given ``Package`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``package_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(package_record_type)`` is ``true`` .

        :param package_record_type: the type of the record to retrieve
        :type package_record_type: ``osid.type.Type``
        :return: the package record
        :rtype: ``osid.installation.records.PackageRecord``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.PackageRecord


class PackageForm:
    """This is the form for creating and updating ``Packages``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``PackageAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_version_metadata(self):
        """Gets the metadata for a version.

        :return: metadata for the version
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    version_metadata = property(fget=get_version_metadata)

    @abc.abstractmethod
    def set_version(self, version):
        """Sets the version.

        :param version: the new version
        :type version: ``osid.installation.Version``
        :raise: ``InvalidArgument`` -- ``version`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``version`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_version(self):
        """Clears the version.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    version = property(fset=set_version, fdel=clear_version)

    @abc.abstractmethod
    def get_copyright_metadata(self):
        """Gets the metadata for a copyright.

        :return: metadata for the copyright
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    copyright_metadata = property(fget=get_copyright_metadata)

    @abc.abstractmethod
    def set_copyright(self, copyright_):
        """Sets the copyright.

        :param copyright: the new copyright
        :type copyright: ``string``
        :raise: ``InvalidArgument`` -- ``copyright`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``copyright`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_copyright(self):
        """Clears the version.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    copyright_ = property(fset=set_copyright, fdel=clear_copyright)

    @abc.abstractmethod
    def get_requires_license_acknowledgement_metadata(self):
        """Gets the metadata for the requires license acknowledgement flag.

        :return: metadata for the acknowledgement flag
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    requires_license_acknowledgement_metadata = property(fget=get_requires_license_acknowledgement_metadata)

    @abc.abstractmethod
    def set_requires_license_acknowledgement(self, requires_license_acknowledgement):
        """Sets the requires license acknowledgement flag.

        :param requires_license_acknowledgement: the new ackknowledgement flag
        :type requires_license_acknowledgement: ``boolean``
        :raise: ``InvalidArgument`` -- ``requires_license_acknowledgement`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_requires_license_acknowledgement(self):
        """Clears the acknowledgement flag.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    requires_license_acknowledgement = property(fset=set_requires_license_acknowledgement, fdel=clear_requires_license_acknowledgement)

    @abc.abstractmethod
    def get_creator_metadata(self):
        """Gets the metadata for a creator resource.

        :return: metadata for the creator resource
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    creator_metadata = property(fget=get_creator_metadata)

    @abc.abstractmethod
    def set_creator(self, resource_id):
        """Sets the creator resource.

        :param resource_id: the new creator resource
        :type resource_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``resource_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_creator(self):
        """Clears the creator.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    creator = property(fset=set_creator, fdel=clear_creator)

    @abc.abstractmethod
    def get_release_date_metadata(self):
        """Gets the metadata for the release date.

        :return: metadata for the release date
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    release_date_metadata = property(fget=get_release_date_metadata)

    @abc.abstractmethod
    def set_release_date(self, release_date):
        """Sets the publisher release date.

        :param release_date: the new release date
        :type release_date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``release_date`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``release_date`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_release_date(self):
        """Clears the release date.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    release_date = property(fset=set_release_date, fdel=clear_release_date)

    @abc.abstractmethod
    def get_dependencies_metadata(self):
        """Gets the metadata for the package dependencies.

        :return: metadata for the package dependencies
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    dependencies_metadata = property(fget=get_dependencies_metadata)

    @abc.abstractmethod
    def set_dependencies(self, package_ids):
        """Sets the dependencies.

        :param package_ids: the new package dependencies
        :type package_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``package_ids`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``package_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependencies(self):
        """Clears the package dependencies.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependencies = property(fset=set_dependencies, fdel=clear_dependencies)

    @abc.abstractmethod
    def get_url_metadata(self):
        """Gets the metadata for the url.

        :return: metadata for the url
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    url_metadata = property(fget=get_url_metadata)

    @abc.abstractmethod
    def set_url(self, url):
        """Sets the url.

        :param url: the new url
        :type url: ``string``
        :raise: ``InvalidArgument`` -- ``url`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``url`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_url(self):
        """Clears the url.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    url = property(fset=set_url, fdel=clear_url)

    @abc.abstractmethod
    def get_package_form_record(self, package_record_type):
        """Gets the ``PackageFormRecord`` corresponding to the given package record ``Type``.

        :param package_record_type: the package record type
        :type package_record_type: ``osid.type.Type``
        :return: the package form record
        :rtype: ``osid.installation.records.PackageFormRecord``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.PackageFormRecord


class PackageList:
    """Like all ``OsidLists,``  ``PackageList`` provides a means for accessing ``Package`` elements sequentially either one at
        a time or many at a time.

    Examples: while (pl.hasNext()) { Package package =
    pl.getNextPackage(); }

    or
      while (pl.hasNext()) {
           Package[] packages = pl.getNextPackages(pl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_package(self):
        """Gets the next ``Package`` in this list.

        :return: the next ``Package`` in this list. The ``has_next()`` method should be used to test that a next
        ``Package`` is available before calling this method.
        :rtype: ``osid.installation.Package``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Package

    next_package = property(fget=get_next_package)

    @abc.abstractmethod
    def get_next_packages(self, n):
        """Gets the next set of ``Package`` elements in this list which must be less than or equal to the number
        returned from ``available()``.

        :param n: the number of ``Package`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Package`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.installation.Package``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Package


class InstallationContent:
    """An installation content contains information about the installation data."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_package_id(self):
        """Gets the ``Package Id`` corresponding to this content.

        :return: the package ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    package_id = property(fget=get_package_id)

    @abc.abstractmethod
    def get_package(self):
        """Gets the ``Package`` corresponding to this content.

        :return: the package
        :rtype: ``osid.installation.Package``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Package

    package = property(fget=get_package)

    @abc.abstractmethod
    def has_data_length(self):
        """Tests if a data length is available.

        :return: ``true`` if a length is available for this content, ``false`` otherwise.
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_data_length(self):
        """Gets the length of the data represented by this content in bytes.

        :return: the length of the data stream
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_data_length()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    data_length = property(fget=get_data_length)

    @abc.abstractmethod
    def get_data(self):
        """Gets the asset content data.

        :return: the length of the content data
        :rtype: ``osid.transport.DataInputStream``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.DataInputStream

    data = property(fget=get_data)

    @abc.abstractmethod
    def get_installation_content_record(self, installation_content_record_type):
        """Gets the installation content record corresponding to the given ``InstallationContent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``installation_content_record_type`` may
        be the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(installation_content_record_type)`` is
        ``true`` .

        :param installation_content_record_type: an installation content record type
        :type installation_content_record_type: ``osid.type.Type``
        :return: the installation content record
        :rtype: ``osid.installation.records.InstallationContentRecord``
        :raise: ``NullArgument`` -- ``installation_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationContentRecord


class InstallationContentForm:
    """This is the form for creating and updating ``InstallationContents``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``InstallationContentsAdminSession``. For each data element that may
    be set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_data_metadata(self):
        """Gets the metadata for the content data.

        :return: metadata for the content data
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    data_metadata = property(fget=get_data_metadata)

    @abc.abstractmethod
    def set_data(self, data):
        """Sets the content data.

        :param data: the content data
        :type data: ``osid.transport.DataInputStream``
        :raise: ``InvalidArgument`` -- ``data`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``data`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_data(self):
        """Removes the content data.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    data = property(fset=set_data, fdel=clear_data)

    @abc.abstractmethod
    def get_installation_content_form_record(self, installation_content_record_type):
        """Gets the ``InstallationContentFormRecord`` corresponding to the given installation content record ``Type``.

        :param installation_content_record_type: the installation content record type
        :type installation_content_record_type: ``osid.type.Type``
        :return: the installation content form record
        :rtype: ``osid.installation.records.InstallationContentFormRecord``
        :raise: ``NullArgument`` -- ``installation_content_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_content_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationContentFormRecord


class InstallationContentList:
    """Like all ``OsidLists,``  ``InstallationContentList`` provides a means for accessing ``InstallationContent`` elements
        sequentially either one at a time or many at a time.

    Examples: while (icl.hasNext()) { InstallationContent content =
    ifl.getNextInstallationContent(); }

    or
      while (icl.hasNext()) {
           InstallationContent[] content = icl.getNextInstallationContents(icl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_installation_content(self):
        """Gets the next ``InstallationContent`` in this list.

        :return: the next ``InstallationContent`` in this list. The ``has_next()`` method should be used to test that a
        next ``InstallationContent`` is available before calling this method.
        :rtype: ``osid.installation.InstallationContent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContent

    next_installation_content = property(fget=get_next_installation_content)

    @abc.abstractmethod
    def get_next_installation_contents(self, n):
        """Gets the next set of ``InstallationContent`` elements in this list which must be less than or equal to the
        number returned from ``available()``.

        :param n: the number of ``InstallationContent`` elements requested which should be less than or equal to
        ``available()``
        :type n: ``cardinal``
        :return: an array of ``InstallationContent`` elements.The length of the array is less than or equal to the
        number specified.
        :rtype: ``osid.installation.InstallationContent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContent


class Depot:
    """A depot defines a collection of packages."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_record(self, depot_record_type):
        """Gets the depot record corresponding to the given ``Depot`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``depot_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(depot_record_type)``
        is ``true`` .

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the depot record
        :rtype: ``osid.installation.records.DepotRecord``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.DepotRecord


class DepotForm:
    """This is the form for creating and updating depots.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``DepotAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_form_record(self, depot_record_type):
        """Gets the ``DepotFormRecord`` corresponding to the given depot record ``Type``.

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the depot form record
        :rtype: ``osid.installation.records.DepotFormRecord``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.DepotFormRecord


class DepotList:
    """Like all ``OsidLists,``  ``DepotList`` provides a means for accessing ``Depot`` elements sequentially either one at a
        time or many at a time.

    Examples: while (dl.hasNext()) { Depot depot = dl.getNextDepot(); }

    or
      while (dl.hasNext()) {
           Depot[] depots = dl.getNextDepots(dl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_depot(self):
        """Gets the next ``Depot`` in this list.

        :return: the next ``Depot`` in this list. The ``has_next()`` method should be used to test that a next ``Depot``
        is available before calling this method.
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    next_depot = property(fget=get_next_depot)

    @abc.abstractmethod
    def get_next_depots(self, n):
        """Gets the next set of ``Depot`` elements in this list which must be less than or equal to the return from
        ``available()``.

        :param n: the number of ``Depot`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Depot`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot


class DepotNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``DepotHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot(self):
        """Gets the ``Depot`` at this node.

        :return: the depot represented by this node
        :rtype: ``osid.installation.Depot``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def get_parent_depot_nodes(self):
        """Gets the parents of this depot.

        :return: the parents of the ``id``
        :rtype: ``osid.installation.DepotNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotNodeList

    parent_depot_nodes = property(fget=get_parent_depot_nodes)

    @abc.abstractmethod
    def get_child_depot_nodes(self):
        """Gets the children of this depot.

        :return: the children of this depot
        :rtype: ``osid.installation.DepotNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotNodeList

    child_depot_nodes = property(fget=get_child_depot_nodes)


class DepotNodeList:
    """Like all ``OsidLists,``  ``DepotNodeList`` provides a means for accessing ``DepotNode`` elements sequentially either one
        at a time or many at a time.

    Examples: while (dnl.hasNext()) { DepotNode node =
    dnl.getNextDepotNode(); }

    or
      while (dnl.hasNext()) {
           DepotNode[] nodes = dnl.getNextDepotNodes(dnl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_depot_node(self):
        """Gets the next ``DepotNode`` in this list.

        :return: the next ``DepotNode`` in this list. The ``has_next()`` method should be used to test that a next
        ``DepotNode`` is available before calling this method.
        :rtype: ``osid.installation.DepotNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotNode

    next_depot_node = property(fget=get_next_depot_node)

    @abc.abstractmethod
    def get_next_depot_nodes(self, n):
        """Gets the next set of ``DepotNode`` elements in this list which must be less than or equal to the return from
        ``available()``.

        :param n: the number of ``DepotNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``DepotNode`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.installation.DepotNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotNode


class Installation:
    """A ``Installation`` represents a ``Package`` installed on a ``Site``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id(self):
        """Gets the ``Site Id`` in which this installation is installed.

        :return: the site ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    site_id = property(fget=get_site_id)

    @abc.abstractmethod
    def get_site(self):
        """Gets the ``Site`` in which this installation is installed.

        :return: the package site
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    site = property(fget=get_site)

    @abc.abstractmethod
    def get_package_id(self):
        """Gets the package ``Id`` of this installation.

        :return: the package ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    package_id = property(fget=get_package_id)

    @abc.abstractmethod
    def get_package(self):
        """Gets the package.

        :return: the package
        :rtype: ``osid.installation.Package``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Package

    package = property(fget=get_package)

    @abc.abstractmethod
    def get_depot_id(self):
        """Gets the ``Id`` of depot from which the package was installed.

        :return: the depot ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_id = property(fget=get_depot_id)

    @abc.abstractmethod
    def get_depot(self):
        """Gets the depot from which the package was installed.

        :return: the depot
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def get_install_date(self):
        """Gets the date the package was installed.

        :return: the installation date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    install_date = property(fget=get_install_date)

    @abc.abstractmethod
    def get_agent_id(self):
        """Gets the ``Id`` of the agent who installed this package.

        :return: the agent ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agent_id = property(fget=get_agent_id)

    @abc.abstractmethod
    def get_agent(self):
        """Gets the agent who installed this package.

        :return: the agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    agent = property(fget=get_agent)

    @abc.abstractmethod
    def get_last_check_date(self):
        """Gets the date the installation was last checked for updates.

        :return: the last check date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    last_check_date = property(fget=get_last_check_date)

    @abc.abstractmethod
    def get_installation_record(self, installation_record_type):
        """Gets the installation record corresponding to the given ``Installation`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``installation_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(installation_record_type)`` is ``true`` .

        :param installation_record_type: the type of the record to retrieve
        :type installation_record_type: ``osid.type.Type``
        :return: the installation record
        :rtype: ``osid.installation.records.InstallationRecord``
        :raise: ``NullArgument`` -- ``installation_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.InstallationRecord


class InstallationList:
    """Like all ``OsidLists,``  ``InstallationList`` provides a means for accessing ``Installation`` elements sequentially
        either one at a time or many at a time.

    Examples: while (il.hasNext()) { Installation install =
    il.getNextInstallation(); }

    or
      while (il.hasNext()) {
           Installation[] installs = il.getNextInstallations(il.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_installation(self):
        """Gets the next ``Installation`` in this list.

        :return: the next ``Installation`` in this list. The ``has_next()`` method should be used to test that a next
        ``Installation`` is available before calling this method.
        :rtype: ``osid.installation.Installation``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Installation

    next_installation = property(fget=get_next_installation)

    @abc.abstractmethod
    def get_next_installations(self, n):
        """Gets the next set of ``Installation`` elements in this list which must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Installation`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Installation`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.installation.Installation``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Installation


class Site:
    """A ``Site`` represents an installation location."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_path(self):
        """Gets the path to this site.

        :return: the path
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    path = property(fget=get_path)

    @abc.abstractmethod
    def get_site_record(self, site_record_type):
        """Gets the site record corresponding to the given ``Site`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``site_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(site_record_type)``
        is ``true`` .

        :param site_record_type: the type of the record to retrieve
        :type site_record_type: ``osid.type.Type``
        :return: the site record
        :rtype: ``osid.installation.records.SiteRecord``
        :raise: ``NullArgument`` -- ``site_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(site_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.records.SiteRecord


class SiteList:
    """Like all ``OsidLists,``  ``SiteList`` provides a means for accessing ``Site`` elements sequentially either one at a time
        or many at a time.

    Examples: while (sl.hasNext()) { Site site = sl.getNextSite(); }

    or
      while (sl.hasNext()) {
           Site[] sites = sl.getNextSites(sl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_site(self):
        """Gets the next ``Site`` in this list.

        :return: the next ``Site`` in this list. The ``has_next()`` method should be used to test that a next ``Site``
        is available before calling this method.
        :rtype: ``osid.installation.Site``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    next_site = property(fget=get_next_site)

    @abc.abstractmethod
    def get_next_sites(self, n):
        """Gets the next set of ``Site`` elements in this list which must be less than or equal to the return from
        ``available()``.

        :param n: the number of ``Site`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Site`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.installation.Site``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site
