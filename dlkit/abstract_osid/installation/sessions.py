"""Implementations of installation abstract base class sessions."""
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


class InstallationLookupSession:
    """The session defines methods for retrieving ``Installations`` from installation ``Sites``.

    An ``Installation`` represents a ``Package`` installed on a
    ``Site``.

    Two views are defined in this session:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * normalized version view: multiple versions of the same package
        are suppressed
      * denormalized version vew: all versions of an installation are
        returned


    Installations may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Installation``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id(self):
        """Gets the ``Site``  ``Id`` associated with this session.

        :return: the ``Site Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    site_id = property(fget=get_site_id)

    @abc.abstractmethod
    def get_site(self):
        """Gets the ``Site`` associated with this session.

        :return: the ``Site`` associated with this session
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    site = property(fget=get_site)

    @abc.abstractmethod
    def can_lookup_installations(self):
        """Tests if this user can perform ``Installation`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_installation_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_installation_view(self):
        """A complete view of the ``Installation`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_version_view(self):
        """The returns from the lookup methods may omit multiple versions of the same installation.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_version_view(self):
        """All versions of the same installation are returned.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_installation(self, installation_id):
        """Gets the ``Installation`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Installation`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Installation`` and
        retained for compatibility.

        :param installation_id: ``Id`` of the ``Installation``
        :type installation_id: ``osid.id.Id``
        :return: the installation
        :rtype: ``osid.installation.Installation``
        :raise: ``NotFound`` -- ``installation_id`` not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.installation.Installation

    @abc.abstractmethod
    def get_installations_by_ids(self, installation_ids):
        """Gets an ``InstallationList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        installations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Installations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param installation_ids: the list of ``Ids`` to retrieve
        :type installation_ids: ``osid.id.IdList``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``installation_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    @abc.abstractmethod
    def get_installations_by_genus_type(self, installation_genus_type):
        """Gets an ``InstallationList`` corresponding to the given installation genus ``Type`` which does not include
        installations of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session.

        :param installation_genus_type: an installation genus type
        :type installation_genus_type: ``osid.type.Type``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    @abc.abstractmethod
    def get_installations_by_parent_genus_type(self, installation_genus_type):
        """Gets an ``InstallationList`` corresponding to the given installation genus ``Type`` and include any
        additional installations with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session.

        :param installation_genus_type: an installation genus type
        :type installation_genus_type: ``osid.type.Type``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    @abc.abstractmethod
    def get_installations_by_record_type(self, installation_record_type):
        """Gets an ``InstallationList`` containing the given installation record ``Type``.

        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session.

        :param installation_record_type: an installation record type
        :type installation_record_type: ``osid.type.Type``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    @abc.abstractmethod
    def get_installations_by_package(self, package_id):
        """Gets an ``InstallationList`` corresponding to the given ``Package``.

        In plenary mode, the returned list contains all of the
        installations for the specified package, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Installations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param package_id: ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    @abc.abstractmethod
    def get_installations(self):
        """Gets all ``Installations``.

        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session. In both cases, the order of the set is not
        specified.

        :return: an ``InstallationList``
        :rtype: ``osid.installation.InstallationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    installations = property(fget=get_installations)


class InstallationQuerySession:
    """This session provides methods for searching ``Installations``.

    The search query is constructed using the ``InstallationQuery``. The
    installation record ``Type`` also specifies the record for the
    installation query.

    Installations may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``InstallationQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id(self):
        """Gets the ``Site``  ``Id`` associated with this session.

        :return: the ``Site Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    site_id = property(fget=get_site_id)

    @abc.abstractmethod
    def get_site(self):
        """Gets the ``Site`` associated with this session.

        :return: the ``Site`` associated with this session
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    site = property(fget=get_site)

    @abc.abstractmethod
    def can_search_installations(self):
        """Tests if this user can perform ``Installation`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_normalized_version_view(self):
        """The returns from the lookup methods may omit multiple versions of the same installation.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_version_view(self):
        """All versions of the same installation are returned.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_dependency_view(self):
        """A normalized view uses a single ``Installation`` to represent a set of package dependencies.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_dependency_view(self):
        """A denormalized view returns all dependencies.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_installation_query(self):
        """Gets an installation query.

        :return: the installation query
        :rtype: ``osid.installation.InstallationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationQuery

    installation_query = property(fget=get_installation_query)

    @abc.abstractmethod
    def get_installations_by_query(self, installation_query):
        """Gets a list of ``Installations`` matching the given installation query.

        :param installation_query: the installation query
        :type installation_query: ``osid.installation.InstallationQuery``
        :return: the returned ``InstallationList``
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList


class InstallationSearchSession:
    """This session provides methods for searching ``Installations``.

    The search query is constructed using the ``InstallationQuery``. The
    installation record ``Type`` also specifies the record for the
    installation query.

    ``get_installations_by_query()`` is the basic search method and
    returns a list of ``Installations``. A more advanced search may be
    performed with ``getInstallationsBySearch()``. It accepts an
    ``InstallationSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_installations_by_search()`` returns an
    ``InstallationSearchResults`` that can be used to access the
    resulting ``InstallationList`` or be used to perform a search within
    the result set through ``InstallationSearch``.

    Installations may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``InstallationQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_installation_search(self):
        """Gets an installation search.

        :return: the installation search
        :rtype: ``osid.installation.InstallationSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationSearch

    installation_search = property(fget=get_installation_search)

    @abc.abstractmethod
    def get_installation_search_order(self):
        """Gets an installation search order.

        The ``InstallationSearchOrder`` is supplied to an
        ``InstallationSearch`` to specify the ordering of results.

        :return: the installation search order
        :rtype: ``osid.installation.InstallationSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationSearchOrder

    installation_search_order = property(fget=get_installation_search_order)

    @abc.abstractmethod
    def get_installations_by_search(self, installation_query, installation_search):
        """Gets the search results matching the given search query using the given search.

        :param installation_query: the installation query
        :type installation_query: ``osid.installation.InstallationQuery``
        :param installation_search: the installation search
        :type installation_search: ``osid.installation.InstallationSearch``
        :return: the returned search results
        :rtype: ``osid.installation.InstallationSearchResults``
        :raise: ``NullArgument`` -- ``installation_query`` or ``installation_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_search`` or ``installation_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationSearchResults

    @abc.abstractmethod
    def get_installations_query_from_inspector(self, installaton_query_inspector):
        """Gets a installation query from an inspector.

        The inspector is available from a ``InstallationSearchResults``.

        :param installaton_query_inspector: a installation query inspector
        :type installaton_query_inspector: ``osid.installation.InstallationQueryInspector``
        :return: the installaton query
        :rtype: ``osid.installation.InstallationQuery``
        :raise: ``NullArgument`` -- ``installation_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``installation_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationQuery


class InstallationManagementSession:
    """This session defines methods to manage installations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id(self):
        """Gets the ``Site``  ``Id`` associated with this session.

        :return: the ``Site Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    site_id = property(fget=get_site_id)

    @abc.abstractmethod
    def get_site(self):
        """Gets the ``Site`` associated with this session.

        :return: the ``Site`` associated with this session
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    site = property(fget=get_site)

    @abc.abstractmethod
    def can_manage_installations(self):
        """Tests if this user can manage installations A return of true does not guarantee successful authorization.

        A return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer management
        operations to unauthorized users.

        :return: ``false`` if ``Package`` installation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def install_package(self, package_id):
        """Installs a package at a default site.

        :param package_id: an ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: the resulting ``Installation``
        :rtype: ``osid.installation.Installation``
        :raise: ``AlreadyExists`` -- package is already installed
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Installation

    @abc.abstractmethod
    def remove_installation(self, installation_id):
        """Removes an installation.

        :param installation_id: an ``Id`` of an ``Installation``
        :type installation_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``installation_id`` is not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_installations(self):
        """Removes all installations at the site.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class InstallationUpdateSession:
    """This session defines methods to manage installations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id(self):
        """Gets the ``Site``  ``Id`` associated with this session.

        :return: the ``Site Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    site_id = property(fget=get_site_id)

    @abc.abstractmethod
    def get_site(self):
        """Gets the ``Site`` associated with this session.

        :return: the ``Site`` associated with this session
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    site = property(fget=get_site)

    @abc.abstractmethod
    def can_get_installation_updates(self):
        """Tests if this user can get installation updates.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer update
        operations to unauthorized users.

        :return: ``false`` if package updates are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_installation_current(self):
        """Tests if the given installation is current.

        :return: ``true`` if the installation is up to date, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installations_to_update(self):
        """Gets a list of installations requiring update.

        This just returns installations that are out of date.
        ``get_packages_to_update()`` or
        ``get_packages_to_update_for_installation()`` should be used to
        acquire the packages to install.

        :return: the resulting ``InstallationList``
        :rtype: ``osid.installation.InstallationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    installations_to_update = property(fget=get_installations_to_update)

    @abc.abstractmethod
    def get_current_packages(self):
        """Gets the packages to install to bring the site up to date.

        :return: the next packages to install
        :rtype: ``osid.installation.PackageList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    current_packages = property(fget=get_current_packages)

    @abc.abstractmethod
    def get_current_packages_for_installation(self, installation_id):
        """Gets the packages to install to bring the specified installation up to date.

        :param installation_id: an ``Id`` of an ``Installation``
        :type installation_id: ``osid.id.Id``
        :return: the next packages to install
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``installation_id`` is not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def is_installation_obsolete(self):
        """Tests if the given installation is obsolete.

        :return: ``true`` if the installation is obsolete, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_obsolete_installations(self):
        """Gets the installations whose packages are obsolete.

        :return: the obsolete installations
        :rtype: ``osid.installation.InstallationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationList

    obsolete_installations = property(fget=get_obsolete_installations)

    @abc.abstractmethod
    def update_installation(self, installation_id):
        """Updates a single installation.

        :param installation_id: an ``Id`` of an ``Installation``
        :type installation_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``installation_id`` is not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def synchronize_installations(self):
        """Performs an auto-update by adding all new updated installations and removing of all obsolete installations on
        the site.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class InstallationNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Installation`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_site_id(self):
        """Gets the ``Site``  ``Id`` associated with this session.

        :return: the ``Site Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    site_id = property(fget=get_site_id)

    @abc.abstractmethod
    def get_site(self):
        """Gets the ``Site`` associated with this session.

        :return: the ``Site`` associated with this session
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Site

    site = property(fget=get_site)

    @abc.abstractmethod
    def can_register_for_installation_notifications(self):
        """Tests if this user can register for ``Installation`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer notification
        functions to unauthorized users.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def register_for_new_installations(self):
        """Register for notifications of new installations.

        ``InstallationReceiver.newInstallations()`` is invoked when a
        new installation is installed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_installations(self):
        """Registers for notification of deleted installations.

        ``InstallationReceiver.deletedInstallations()`` is invoked when
        a installation is removed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_installation(self, installation_id):
        """Registers for notification of a deleted installation.

        ``InstallationReceiver.deletedInstallations()`` is invoked when
        the specified installation is removed.

        :param installation_id: the ``Id`` of the ``Installation`` to monitor
        :type installation_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``installation_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SiteLookupSession:
    """This session provides methods for retrieving ``Site`` objects.

    The ``Site`` represents a collection of ``Installations``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Sites may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Site``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_sites(self):
        """Tests if this user can perform ``Site`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_site_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_site_view(self):
        """A complete view of the ``Site`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_site(self, site_id):
        """Gets the ``Site`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Site`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Site`` and retained for compatibility.

        :param site_id: ``Id`` of the ``Site``
        :type site_id: ``osid.id.Id``
        :return: the site
        :rtype: ``osid.installation.Site``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.installation.Site

    @abc.abstractmethod
    def get_sites(self):
        """Gets all ``Sites``.

        In plenary mode, the returned list contains all known sites or
        an error results. Otherwise, the returned list may contain only
        those sites that are accessible through this session.

        :return: a ``SiteList``
        :rtype: ``osid.installation.SiteList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.SiteList

    sites = property(fget=get_sites)


class PackageLookupSession:
    """This session provides methods for retrieving ``Package`` s from remote ``Depots``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_id(self):
        """Gets the ``Depot``  ``Id`` associated with this session.

        :return: the ``Depot Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_id = property(fget=get_depot_id)

    @abc.abstractmethod
    def get_depot(self):
        """Gets the ``Depot`` associated with this session.

        :return: the ``Depot`` associated with this session
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def can_lookup_packages(self):
        """Tests if this user can perform ``Package`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_package_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_package_view(self):
        """A complete view of the ``Package`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_depot_view(self):
        """Federates the view for methods in this session.

        A federated view will include packages in depots which are
        children of this depot in the depot hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_depot_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this depot only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_version_view(self):
        """The returns from the lookup methods may omit multiple versions of the same package.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_version_view(self):
        """All versions of the same package are returned.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_package(self, package_id):
        """Gets the ``Package`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Package`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Package`` and retained for
        compatibility.

        :param package_id: ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: the package
        :rtype: ``osid.installation.Package``
        :raise: ``NotFound`` -- ``package_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.installation.Package

    @abc.abstractmethod
    def get_packages_by_ids(self, package_ids):
        """Gets a ``PackageList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the packages
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Packages`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param package_ids: the list of ``Ids`` to retrieve
        :type package_ids: ``osid.id.IdList``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``package_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_packages_by_genus_type(self, package_genus_type):
        """Gets a ``PackageList`` corresponding to the given package genus ``Type`` which does not include packages of
        genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param package_genus_type: a package genus type
        :type package_genus_type: ``osid.type.Type``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_packages_by_parent_genus_type(self, package_genus_type):
        """Gets a ``PackageList`` corresponding to the given package genus ``Type`` and include any additional package
        with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param package_genus_type: a package genus type
        :type package_genus_type: ``osid.type.Type``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_packages_by_record_type(self, package_record_type):
        """Gets a ``PackageList`` containing the given package record ``Type``.

        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param package_record_type: a package record type
        :type package_record_type: ``osid.type.Type``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_packages_by_provider(self, resource_id):
        """Gets a ``PackageList`` for the given provider.

        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_dependent_packages(self, package_id):
        """Gets a list of packages depending on the given package.

        :param package_id: an ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of package dependents
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_package_versions(self, package_id):
        """Gets a list of packages in the specified package version chain.

        :param package_id: an ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of dependencies
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_packages(self):
        """Gets all ``Packages``.

        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :return: a ``PackageList``
        :rtype: ``osid.installation.PackageList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    packages = property(fget=get_packages)


class PackageQuerySession:
    """This session provides methods for searching ``Package`` objects.

    The search query is constructed using the ``PackageQuery``. The
    package record ``Type`` also specifies the record for the package
    query.

    This session defines views that offer differing behaviors for
    searching.

      * federated depot view: searches include packages in depots of
        which this depot is a ancestor in the depot hierarchy
      * isolated depot view: searches are restricted to packages in this
        depot
      * normalized version view: multiple versions of the same package
        are suppressed
      * denormalized version vew: all versions of an installation are
        returned
      * normalized dependency view: supporting installations upon which
        other installations depend are suppressed
      * denormalized dependency view: all dependencies are returned


    Packages may have a query record indicated by their respective
    record types. The query record is accessed via the ``PackageQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_id(self):
        """Gets the ``Depot``  ``Id`` associated with this session.

        :return: the ``Depot Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_id = property(fget=get_depot_id)

    @abc.abstractmethod
    def get_depot(self):
        """Gets the ``Depot`` associated with this session.

        :return: the ``Depot`` associated with this session
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def can_search_packages(self):
        """Tests if this user can perform ``Package`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_depot_view(self):
        """Federates the view for methods in this session.

        A federated view will include packages in depots which are
        children of this depot in the depot hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_depot_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this depot only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_version_view(self):
        """The returns from the lookup methods may omit multiple versions of the same package.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_version_view(self):
        """All versions of the same package are returned.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_dependency_view(self):
        """A normalized view uses a single ``Package`` to represent a set of package dependencies.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_dependency_view(self):
        """A denormalized view returns all dependencies.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_package_query(self):
        """Gets a package query.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQuery

    package_query = property(fget=get_package_query)

    @abc.abstractmethod
    def get_packages_by_query(self, package_query):
        """Gets a list of ``Packages`` matching the given package query.

        :param package_query: the package query
        :type package_query: ``osid.installation.PackageQuery``
        :return: the returned ``PackageList``
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList


class PackageSearchSession:
    """This session provides methods for searching ``Package`` objects.

    The search query is constructed using the ``PackageQuery``. The
    package record ``Type`` also specifies the record for the package
    query.

    ``get_packages_by_query()`` is the basic search method and returns a
    list of ``Packages``. A more advanced search may be performed with
    ``getPackagesBySearch()``. It accepts a ``PackageSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_packages_by_search()`` returns a ``PackageSearchResults`` that
    can be used to access the resulting ``PackageList`` or be used to
    perform a search within the result set through ``PackageSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated depot view: searches include packages in depots of
        which this depot is a ancestor in the depot hierarchy
      * isolated depot view: searches are restricted to packages in this
        depot
      * normalized version view: multiple versions of the same package
        are suppressed
      * denormalized version vew: all versions of an installation are
        returned
      * normalized dependency view: supporting installations upon which
        other installations depend are suppressed
      * denormalized dependency view: all dependencies are returned


    Packages may have a query record indicated by their respective
    record types. The query record is accessed via the ``PackageQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_package_search(self):
        """Gets a package search.

        :return: the package search
        :rtype: ``osid.installation.PackageSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageSearch

    package_search = property(fget=get_package_search)

    @abc.abstractmethod
    def get_package_search_order(self):
        """Gets a package search order.

        The ``PackageSearchOrder`` is supplied to a ``PackageSearch`` to
        specify the ordering of results.

        :return: the package search order
        :rtype: ``osid.installation.PackageSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageSearchOrder

    package_search_order = property(fget=get_package_search_order)

    @abc.abstractmethod
    def get_packages_by_search(self, package_query, package_search):
        """Gets the search results matching the given search query using the given search.

        :param package_query: the package query
        :type package_query: ``osid.installation.PackageQuery``
        :param package_search: the package search
        :type package_search: ``osid.installation.PackageSearch``
        :return: the returned search results
        :rtype: ``osid.installation.PackageSearchResults``
        :raise: ``NullArgument`` -- ``package_query`` or ``package_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_search`` or ``package_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageSearchResults

    @abc.abstractmethod
    def get_package_query_from_inspector(self, package_query_inspector):
        """Gets a package query from an inspector.

        The inspector is available from a ``PackageeSearchResults``.

        :param package_query_inspector: a package query inspector
        :type package_query_inspector: ``osid.installation.PackageQueryInspector``
        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``NullArgument`` -- ``package_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``package_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQuery


class PackageAdminSession:
    """This session creates, updates, and deletes ``Packages``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Package,`` a ``PackagetForm`` is requested using
    ``get_package_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``PackageForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``PackageForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``PackageForm``
    corresponds to an attempted transaction.

    For updates, ``PackageForms`` are requested to the ``Package``
    ``Id`` that is to be updated using ``getPackageFormForUpdate()``.
    Similarly, the ``PackageForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``PackageForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Packages``. To unmap a ``Package``
    from the current ``Depot,`` the ``PackageDepotAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Package`` itself thus removing it from all known ``Depot``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_id(self):
        """Gets the ``Depot``  ``Id`` associated with this session.

        :return: the ``Depot Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_id = property(fget=get_depot_id)

    @abc.abstractmethod
    def get_depot(self):
        """Gets the ``Depot`` associated with this session.

        :return: the ``Depot`` associated with this session
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def can_create_packages(self):
        """Tests if this user can create ``Packages``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Package`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_package_with_record_types(self, package_record_types):
        """Tests if this user can create a single ``Package`` using the desired record types.

        While ``InstallationManager.getPackageRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Package``. Providing an empty array tests if a ``Package`` can
        be created with no records.

        :param package_record_types: array of package record types
        :type package_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Package`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_form_for_create(self, package_record_types):
        """Gets the package form for creating new packages.

        A new form should be requested for each create transaction.

        :param package_record_types: array of package record types
        :type package_record_types: ``osid.type.Type[]``
        :return: the package form
        :rtype: ``osid.installation.PackageForm``
        :raise: ``NullArgument`` -- ``package_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageForm

    @abc.abstractmethod
    def create_package(self, package_form):
        """Creates a new ``Package``.

        :param package_form: the form for this ``Package``
        :type package_form: ``osid.installation.PackageForm``
        :return: the new ``Package``
        :rtype: ``osid.installation.Package``
        :raise: ``IllegalState`` -- ``package_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``package_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_form`` did not originate from ``get_package_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Package

    @abc.abstractmethod
    def can_update_packages(self):
        """Tests if this user can update ``Packages``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if package modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_update_package(self, package_id):
        """Tests if this user can update a specified package.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the package
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer an update
        operation to an unauthorized user for this function.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: ``false`` if package modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If the ``package_id`` is not found, then
        it is acceptable to return false to indicate the lack of an
        update available.

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_form_for_update(self, package_id):
        """Gets the package form for updating an existing package.

        A new package form should be requested for each update
        transaction.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: the package form
        :rtype: ``osid.installation.PackageForm``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageForm

    @abc.abstractmethod
    def update_package(self, package_form):
        """Updates an existing package.

        :param package_form: the form containing the elements to be updated
        :type package_form: ``osid.installation.PackageForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``package_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_form`` did not originate from ``get_package_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_packages(self):
        """Tests if this user can delete ``Packages``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Package`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_delete_package(self, package_id):
        """Tests if this user can delete a specified ``Package``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer a
        delete operation to an unauthorized user for this function.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: ``false`` if ``Package`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If the ``package_id`` is not found, then
        it is acceptable to return false to indicate the lack of a
        delete available.

        """
        return  # boolean

    @abc.abstractmethod
    def delete_package(self, package_id):
        """Deletes the ``Package`` identified by the given ``Id``.

        :param package_id: the ``Id`` of the ``Package`` to delete
        :type package_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Package`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_package_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Packages``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Package`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_package(self, package_id, alias_id):
        """Adds an ``Id`` to a ``Package`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Package`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another package it is
        reassigned to the given package ``Id``.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``package_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_create_installation_content(self):
        """Tests if this user can create content for ``Packages``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``InstallationContent`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``installation`` content creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_installation_content_with_record_types(self, installation_content_record_types):
        """Tests if this user can create an ``InstallationContent`` using the desired record types.

        While
        ``InstallationManager.getInstallationContentRecordTypes()`` can
        be used to test which records are supported, this method tests
        which records are required for creating a specific
        ``InstallationContent``. Providing an empty array tests if an
        ``InstallationContent`` can be created with no records.

        :param installation_content_record_types: array of installation content record types
        :type installation_content_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``InstallationContent`` creation using the specified ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_content_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_content_form_for_create(self, package_id, installation_content_record_types):
        """Gets an installation content form for creating new installation contents.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param installation_content_record_types: array of installation content record types
        :type installation_content_record_types: ``osid.type.Type[]``
        :return: the installation content form
        :rtype: ``osid.installation.InstallationContentForm``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` or ``installation_content_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContentForm

    @abc.abstractmethod
    def create_installation_content(self, installation_content_form):
        """Creates new ``InstallationContent`` for a given package.

        :param installation_content_form: the form for this ``InstallationContent``
        :type installation_content_form: ``osid.installation.InstallationContentForm``
        :return: the new ``InstallationContent``
        :rtype: ``osid.installation.InstallationContent``
        :raise: ``IllegalState`` -- ``installation_content_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``installation_content_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_content_form`` did not originate from
        ``get_installation_content_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContent

    @abc.abstractmethod
    def can_update_installation_contents(self):
        """Tests if this user can update ``InstallationContent``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``InstallationContent`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``InstallationContent`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_installation_content_form_for_update(self, installation_content_id):
        """Gets the installation content form for updating an existing installation content.

        A new installation content form should be requested for each
        update transaction.

        :param installation_content_id: the ``Id`` of the ``InstallationContent``
        :type installation_content_id: ``osid.id.Id``
        :return: the v content form
        :rtype: ``osid.installation.InstallationContentForm``
        :raise: ``NotFound`` -- ``installation_content_id`` is not found
        :raise: ``NullArgument`` -- ``installation_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.InstallationContentForm

    @abc.abstractmethod
    def update_installation_content(self, installation_content_form):
        """Updates an existing installation content.

        :param installation_content_form: the form containing the elements to be updated
        :type installation_content_form: ``osid.installation.InstallationContentForm``
        :raise: ``IllegalState`` -- ``installation_content_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``installation_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_content_form`` did not originate from
        ``get_installation_content_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_installation_contents(self):
        """Tests if this user can delete ``InstallationContents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``InstallationContent`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``InstallationContent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_installation_content(self, installation_content_id):
        """Deletes content from a package.

        :param installation_content_id: the ``Id`` of the ``InstallationContent``
        :type installation_content_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``installation_content_id`` is not found
        :raise: ``NullArgument`` -- ``installation_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_package_versions(self):
        """Tests if this user can manage package versions.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known version methods will
        result in a ``PermissionDenied``. This is intended as a hint to
        an application that may opt not to offer delete operations to an
        unauthorized user.

        :return: ``false`` if package versioning is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_package_version(self, package_id, next_package_id):
        """Sets the given package to be the next version of another package.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param next_package_id: the ``Id`` of the net package version
        :type next_package_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``next_package_id`` or ``package_id`` already part of a version chain
        :raise: ``NotFound`` -- ``package_id`` or ``next_package_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` or ``next_package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_package_version(self, package_id, next_package_id):
        """Removes a package from being the next version of another package.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param next_package_id: the ``Id`` of the net package version
        :type next_package_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``next_package_id`` does not follow ``package_id``
        :raise: ``NullArgument`` -- ``package_id`` or ``dependency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class PackageNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Package`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``PackageLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_id(self):
        """Gets the ``Depot``  ``Id`` associated with this session.

        :return: the ``Depot Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_id = property(fget=get_depot_id)

    @abc.abstractmethod
    def get_depot(self):
        """Gets the ``Depot`` associated with this session.

        :return: the ``Depot`` associated with this session
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def can_register_for_package_notifications(self):
        """Tests if this user can register for ``Package`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_depot_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for packages in
        depots which are children of this depot in the depot hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_depot_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this depot only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_packages(self):
        """Register for notifications of new packages.

        ``PackageReceiver.newPackages()`` is invoked when a new package
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_packages(self):
        """Registers for notification of updated packages.

        ``PackageReceiver.changedPackages()`` is invoked when a package
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_package(self, package_id):
        """Registers for notification of an updated package.

        ``PackageReceiver.changedPackages()`` is invoked when the
        specified package is changed.

        :param package_id: the ``Id`` of the ``Package`` to monitor
        :type package_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``package_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_packages(self):
        """Registers for notification of deleted packages.

        ``PackageReceiver.deletedPackages()`` is invoked when a package
        is removed from this depot.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_package(self, package_id):
        """Registers for notification of a deleted package.

        ``PackageReceiver.deletedPackages()`` is invoked when the
        specified package is removed from this depot.

        :param package_id: the ``Id`` of the ``Package`` to monitor
        :type package_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``package_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class PackageDepotSession:
    """This session provides methods to retrieve ``Package`` to ``Depot`` mappings.

    A ``Package`` may appear in multiple ``Depots``. Each ``Depot`` may
    have its own authorizations governing who is allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_package_depot_mappings(self):
        """Tests if this user can perform lookups of package/depot mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_depot_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_depot_view(self):
        """A complete view of the ``Package`` and ``Depot`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_version_view(self):
        """The returns from the lookup methods may omit multiple versions of the same package.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_version_view(self):
        """All versions of the same package are returned.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_normalized_dependency_view(self):
        """A normalized view uses a single ``Package`` to represent a set of package dependencies.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_denormalized_dependency_view(self):
        """A denormalized view returns all dependencies.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_package_ids_by_depot(self, depot_id):
        """Gets the list of ``Package``  ``Ids`` associated with a ``Depot``.

        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: list of related package ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_packages_by_depot(self, depot_id):
        """Gets the list of ``Packages`` associated with a ``Depot``.

        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: list of related packages
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_package_ids_by_depots(self, depot_ids):
        """Gets the list of ``Package Ids`` corresponding to a list of ``Depots``.

        :param depot_ids: list of depot ``Ids``
        :type depot_ids: ``osid.id.IdList``
        :return: list of package ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_packages_by_depots(self, depot_ids):
        """Gets the list of ``Packages`` corresponding to a list of ``Depots``.

        :param depot_ids: list of depot ``Ids``
        :type depot_ids: ``osid.id.IdList``
        :return: list of packages
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageList

    @abc.abstractmethod
    def get_depot_ids_by_package(self, package_id):
        """Gets the list of ``Depot``  ``Ids`` mapped to a ``Package``.

        :param package_id: ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_depots_by_package(self, package_id):
        """Gets the list of ``Depots`` mapped to a ``Package``.

        :param package_id: ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of depots
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList


class PackageDepotAssignmentSession:
    """This session provides methods to re-assign ``Packages`` to ``Depots``.

    A ``Package`` may map to multiple ``Depots`` and removing the last
    reference to an ``Package`` is the equivalent of deleting it. Each
    ``Depot`` may have its own authorizations governing who is allowed
    to operate on it.

    Moving or adding a reference of a ``Package`` to another ``Depot``
    is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_packages(self):
        """Tests if this user can alter package/depot mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_packages_to_depot(self, depot_id):
        """Tests if this user can alter package/depot mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_depot_ids(self, depot_id):
        """Gets a list of depot including and under the given depot node in which any package can be assigned.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: list of assignable depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_depot_ids_for_package(self, depot_id, package_id):
        """Gets a list of depot including and under the given depot node in which a specific package can be assigned.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of assignable depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_id`` or ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_package_to_depot(self, package_id, depot_id):
        """Adds an existing ``Package`` to a ``Depot``.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``package_id`` is already assigned to ``depot_id``
        :raise: ``NotFound`` -- ``package_id`` or ``depot_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_package_from_depot(self, package_id, depot_id):
        """Removes a ``Package`` from a ``Depot``.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``package_id`` or ``depot_id`` not found or ``package_id`` not assigned to ``depot_id``
        :raise: ``NullArgument`` -- ``package_id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class PackageSmartDepotSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``PackageQuery`` can be retrieved from this session and mapped to
    this ``Depot`` to create a virtual collection of ``Packages``. The
    packages may be sequenced using the ``PackageSearchOrder`` from this
    session.

    This ``Depot`` has a default query that matches any package and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``PackageQueryInspector``. The query may be
    modified by converting the inspector back to a ``PackageQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_id(self):
        """Gets the ``Depot``  ``Id`` associated with this session.

        :return: the ``Depot Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_id = property(fget=get_depot_id)

    @abc.abstractmethod
    def get_depot(self):
        """Gets the ``Depot`` associated with this session.

        :return: the ``Depot`` associated with this session
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    depot = property(fget=get_depot)

    @abc.abstractmethod
    def can_manage_smart_depot(self):
        """Tests if this user can manage smart depot.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart depot management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_package_query(self):
        """Gets a package query.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQuery

    package_query = property(fget=get_package_query)

    @abc.abstractmethod
    def get_package_search_order(self):
        """Gets a package search order.

        :return: the package search order
        :rtype: ``osid.installation.PackageSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageSearchOrder

    package_search_order = property(fget=get_package_search_order)

    @abc.abstractmethod
    def apply_package_query(self, package_query):
        """Applies a package query to this depot.

        :param package_query: the package query
        :type package_query: ``osid.installation.PackageQuery``
        :raise: ``NullArgument`` -- ``package_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``package_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_package_query(self):
        """Gets a package query inspector for this depot.

        :return: the package query inspector
        :rtype: ``osid.installation.PackageQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQueryInspector

    @abc.abstractmethod
    def apply_package_sequencing(self, package_search_order):
        """Applies a package search order to this depot.

        :param package_search_order: the package search order
        :type package_search_order: ``osid.installation.PackageSearchOrder``
        :raise: ``NullArgument`` -- ``package_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``package_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_package_query_from_inspector(self, package_query_inspector):
        """Gets a package query from an inspector.

        :param package_query_inspector: a package query inspector
        :type package_query_inspector: ``osid.installation.PackageQueryInspector``
        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``NullArgument`` -- ``package_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``package_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.PackageQuery


class DepotLookupSession:
    """This session provides methods for retrieving ``Depot`` objects.

    The ``Depot`` represents a collection of ``Packages``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Depots`` it can access, without breaking execution.
    However, an administrative application may require all ``Depot``
    elements to be available.

    Depots may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Depot``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_depots(self):
        """Tests if this user can perform ``Depot`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_depot_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_depot_view(self):
        """A complete view of the ``Depot`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_depot(self, depot_id):
        """Gets the ``Depot`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Depot`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Depot`` and retained for compatility.

        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: the depot
        :rtype: ``osid.installation.Depot``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.installation.Depot

    @abc.abstractmethod
    def get_depots_by_ids(self, depot_ids):
        """Gets a ``DepotList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the depots
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Depot`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param depot_ids: the list of ``Ids`` to retrieve
        :type depot_ids: ``osid.id.IdList``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def get_depots_by_genus_type(self, depot_genus_type):
        """Gets a ``DepotList`` corresponding to the given depot genus ``Type`` which does not include depots of types
        derived from the specified ``Type``.

        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param depot_genus_type: a depot genus type
        :type depot_genus_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def get_depots_by_parent_genus_type(self, depot_genus_type):
        """Gets a ``DepotList`` corresponding to the given depot genus ``Type`` and include any additional depots with
        genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param depot_genus_type: a depot genus type
        :type depot_genus_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def get_depots_by_record_type(self, depot_record_type):
        """Gets a ``DepotList`` containing the given depot record ``Type``.

        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def get_depots_by_provider(self, resource_id):
        """Gets a ``DepotList`` for the given provider ````.

        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def get_depots(self):
        """Gets all ``Depots``.

        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :return: a ``DepotList``
        :rtype: ``osid.installation.DepotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    depots = property(fget=get_depots)


class DepotQuerySession:
    """This session provides methods for searching among ``Depot`` objects.

    The search query is constructed using the ``DepotQuery``.

    Depots may have a query record indicated by their respective record
    types. The query record is accessed via the ``DepotQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_depots(self):
        """Tests if this user can perform ``Depot`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_query(self):
        """Gets a depot query.

        :return: a depot query
        :rtype: ``osid.installation.DepotQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotQuery

    depot_query = property(fget=get_depot_query)

    @abc.abstractmethod
    def get_depots_by_query(self, depot_query):
        """Gets a list of ``Depot`` objects matching the given depot query.

        :param depot_query: the depot query
        :type depot_query: ``osid.installation.DepotQuery``
        :return: the returned ``DepotList``
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList


class DepotSearchSession:
    """This session provides methods for searching among ``Depot`` objects.

    The search query is constructed using the ``DepotQuery``.

    ``get_depots_by_query()`` is the basic search method and returns a
    list of ``Depot`` objects.A more advanced search may be performed
    with ``getDepotsBySearch()``. It accepts a ``DepotSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_depots_by_search()`` returns a ``DepotSearchResults`` that can
    be used to access the resulting ``DepotList`` or be used to perform
    a search within the result set through ``DepotSearch``.

    Depots may have a query record indicated by their respective record
    types. The query record is accessed via the ``DepotQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_search(self):
        """Gets a depot search.

        :return: a depot search
        :rtype: ``osid.installation.DepotSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotSearch

    depot_search = property(fget=get_depot_search)

    @abc.abstractmethod
    def get_depot_search_order(self):
        """Gets a depot search order.

        The ``DepotSearchOrder`` is supplied to a ``DepotSearch`` to
        specify the ordering of results.

        :return: the depot search order
        :rtype: ``osid.installation.DepotSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotSearchOrder

    depot_search_order = property(fget=get_depot_search_order)

    @abc.abstractmethod
    def get_depots_by_search(self, depot_query, depot_search):
        """Gets the search results matching the given search query using the given search.

        :param depot_query: the depot query
        :type depot_query: ``osid.installation.DepotQuery``
        :param depot_search: the depot search
        :type depot_search: ``osid.installation.DepotSearch``
        :return: the depot search results
        :rtype: ``osid.installation.DepotSearchResults``
        :raise: ``NullArgument`` -- ``depot_query`` or ``depot_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_query`` or ``depot_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotSearchResults

    @abc.abstractmethod
    def get_depot_query_from_inspector(self, depot_query_inspector):
        """Gets a depot query from an inspector.

        The inspector is available from a ``DepotSearchResults``.

        :param depot_query_inspector: a depot query inspector
        :type depot_query_inspector: ``osid.installation.DepotQueryInspector``
        :return: the depot query
        :rtype: ``osid.installation.DepotQuery``
        :raise: ``NullArgument`` -- ``depot_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``depot_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotQuery


class DepotAdminSession:
    """This session creates, updates, and deletes ``Depots``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Depot,`` a ``DepotForm`` is requested using
    ``get_depot_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``DepotForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``DepotForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``DepotForm`` corresponds
    to an attempted transaction.

    For updates, ``DepotForms`` are requested to the ``Depot``  ``Id``
    that is to be updated using ``getDepotFormForUpdate()``. Similarly,
    the ``DepotForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``Depot`` can only be used once for a successful update and cannot
    be reused.

    The delete operations delete ``Depots``. This session also includes
    an ``Id`` aliasing mechanism to assign an external ``Id`` to an
    internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_depots(self):
        """Tests if this user can create ``Depots``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Depot`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_depot_with_record_types(self, depot_record_types):
        """Tests if this user can create a single ``Depot`` using the desired record types.

        While ``InstallationManager.getDepotRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Depot``.
        Providing an empty array tests if a ``Depot`` can be created
        with no records.

        :param depot_record_types: array of depot record types
        :type depot_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Depot`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_form_for_create(self, depot_record_types):
        """Gets the depot form for creating new depots.

        A new form should be requested for each create transaction.

        :param depot_record_types: array of depot record types
        :type depot_record_types: ``osid.type.Type[]``
        :return: the depot form
        :rtype: ``osid.installation.DepotForm``
        :raise: ``NullArgument`` -- ``depot_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotForm

    @abc.abstractmethod
    def create_depot(self, depot_form):
        """Creates a new ``Depot``.

        :param depot_form: the form for this ``Depot``
        :type depot_form: ``osid.installation.DepotForm``
        :return: the new ``Depot``
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- ``depot_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``depot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_form`` did not originate from ``get_depot_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Depot

    @abc.abstractmethod
    def can_update_depots(self):
        """Tests if this user can update ``Depots``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Depot`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_update_depot(self, depot_id):
        """Tests if this user can update a specified ``Depot``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the
        ``Depot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if depot modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If the ``depot_id`` is not found, then
        it is acceptable to return false to indicate the lack of an
        update available.

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_form_for_update(self, depot_id):
        """Gets the depot form for updating an existing depot.

        A new depot form should be requested for each update
        transaction.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: the depot form
        :rtype: ``osid.installation.DepotForm``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotForm

    @abc.abstractmethod
    def update_depot(self, depot_form):
        """Updates an existing depot.

        :param depot_form: the form containing the elements to be updated
        :type depot_form: ``osid.installation.DepotForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``depot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_form`` did not originate from ``get_depot_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_depots(self):
        """Tests if this user can delete depots.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Depot`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_delete_depot(self, depot_id):
        """Tests if this user can delete a specified ``Depot``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Depot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if deletion of this ``Depot`` is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If the ``depot_id`` is not found, then
        it is acceptable to return false to indicate the lack of a
        delete available.

        """
        return  # boolean

    @abc.abstractmethod
    def delete_depot(self, depot_id):
        """Deletes a ``Depot``.

        :param depot_id: the ``Id`` of the ``Depot`` to remove
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_depot_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Depots``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Depot`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_depot(self, depot_id, alias_id):
        """Adds an ``Id`` to a ``Depot`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Depot`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another depot it is
        reassigned to the given depot ``Id``.

        :param depot_id: the ``Id`` of a ``Depot``
        :type depot_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class DepotNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Depot`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_depot_notifications(self):
        """Tests if this user can register for ``Depot`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def register_for_new_depots(self):
        """Register for notifications of new depots.

        ``DepotReceiver.newDepots()`` is invoked when a new ``Depot`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_depot_ancestors(self, depot_id):
        """Registers for notification if an ancestor is added to the specified depot in the depot hierarchy.

        ``DepotReceiver.newDepotAncestor()`` is invoked when the
        specified depot experiences an addition in ancestry.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_depot_descendants(self, depot_id):
        """Registers for notification if a descendant is added to the specified depot in the depot hierarchy.

        ``DepotReceiver.newDepotDescendant()`` is invoked when the
        specified depot experiences an addition in descendants.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_depots(self):
        """Registers for notification of updated depots.

        ``DepotReceiver.changedDepots()`` is invoked when a depot is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_depot(self, depot_id):
        """Registers for notification of an updated depot.

        ``DepotReceiver.changedDepots()`` is invoked when the specified
        depot is changed.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_depots(self):
        """Registers for notification of deleted depots.

        ``DepotReceiver.deletedDepots()`` is invoked when a depot is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_depot(self, depot_id):
        """Registers for notification of a deleted depot.

        ``DepotReceiver.deletedDepots()`` is invoked when the specified
        depot is deleted.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_depot_ancestors(self, depot_id):
        """Registers for notification if an ancestor is removed from the specified depot in the depot hierarchy.

        ``DepotReceiver.deletedDepotAncestor()`` is invoked when the
        specified depot experiences a removal of an ancestor.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_depot_descendants(self, depot_id):
        """Registers for notification if a descendant is removed from fthe specified depot in the depot hierarchy.

        ``DepotReceiver.deletedDepotDescednant()`` is invoked when the
        specified depot experiences a removal of one of its descendants.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class DepotHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Depot`` objects.

    Each node in the hierarchy is a unique ``Depot``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_depots()`` and ``getChildDepots()``. To relate these
    ``Ids`` to another OSID, ``get_depot_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Depot`` available in the Depoting OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_depots()`` or ``get_child_depots()`` in lieu
    of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: depot elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_hierarchy_id = property(fget=get_depot_hierarchy_id)

    @abc.abstractmethod
    def get_depot_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    depot_hierarchy = property(fget=get_depot_hierarchy)

    @abc.abstractmethod
    def can_access_depot_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_depot_view(self):
        """The returns from the depot methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_depot_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_depot_ids(self):
        """Gets the root depot ``Ids`` in this hierarchy.

        :return: the root depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_depot_ids = property(fget=get_root_depot_ids)

    @abc.abstractmethod
    def get_root_depots(self):
        """Gets the root depots in this depot hierarchy.

        :return: the root depots
        :rtype: ``osid.installation.DepotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.installation.DepotList

    root_depots = property(fget=get_root_depots)

    @abc.abstractmethod
    def has_parent_depots(self, depot_id):
        """Tests if the ``Depot`` has any parents.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the depot has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is a direct parent of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_depot_ids(self, depot_id):
        """Gets the parent ``Ids`` of the given depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_depots(self, depot_id):
        """Gets the parents of the given depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: the parents of the depot
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def is_ancestor_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is an ancestor of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_depots(self, depot_id):
        """Tests if a depot has any children.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``depot_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_depot(self, id_, depot_id):
        """Tests if a depot is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_depot_ids(self, depot_id):
        """Gets the child ``Ids`` of the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_depots(self, depot_id):
        """Gets the children of the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotList

    @abc.abstractmethod
    def is_descendant_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is a descendant of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_depot_node_ids(self, depot_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a depot node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_depot_nodes(self, depot_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a depot node
        :rtype: ``osid.installation.DepotNode``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.DepotNode


class DepotHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Depot`` objects.

    Each node in the hierarchy is a unique ``Depot``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_depot_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    depot_hierarchy_id = property(fget=get_depot_hierarchy_id)

    @abc.abstractmethod
    def get_depot_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    depot_hierarchy = property(fget=get_depot_hierarchy)

    @abc.abstractmethod
    def can_modify_depot_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_depot(self, depot_id):
        """Adds a root depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``depot_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_depot(self, depot_id):
        """Removes a root depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` is not a root
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_depot(self, depot_id, child_id):
        """Adds a child to a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``depot_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``depot_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_depot(self, depot_id, child_id):
        """Removes a child from a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``depot_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_depots(self, depot_id):
        """Removes all children from a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
