"""Implementations of osid abstract base class managers."""
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


class OsidProfile:
    """The ``OsidProfile`` defines the interoperability areas of an OSID.

    An ``OsidProfile`` is implemented by an ``OsidManager``. The top
    level ``OsidProfile`` tests for version compatibility. Each OSID
    extends this interface to include its own interoperability
    definitions within its managers.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_id(self):
        """Gets an identifier for this service implementation.

        The identifier is unique among services but multiple
        instantiations of the same service use the same ``Id``. This
        identifier is the same identifier used in managing OSID
        installations.

        :return: the ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    @abc.abstractmethod
    def get_display_name(self):
        """Gets a display name for this service implementation.

        :return: a display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    @abc.abstractmethod
    def get_description(self):
        """Gets a description of this service implementation.

        :return: a description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    description = property(fget=get_description)

    @abc.abstractmethod
    def get_version(self):
        """Gets the version of this service implementation.

        :return: the service implementation version
        :rtype: ``osid.installation.Version``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    version = property(fget=get_version)

    @abc.abstractmethod
    def get_release_date(self):
        """Gets the date this service implementation was released.

        :return: the release date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    release_date = property(fget=get_release_date)

    @abc.abstractmethod
    def supports_osid_version(self, version):
        """Test for support of an OSID specification version.

        :param version: the specification version to test
        :type version: ``osid.installation.Version``
        :return: ``true`` if this manager supports the given OSID version, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: An implementation may support multiple
        versions of an OSID.

        """
        return  # boolean

    @abc.abstractmethod
    def get_locales(self):
        """Gets the locales supported in this service.

        :return: list of locales supported
        :rtype: ``osid.locale.LocaleList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.LocaleList

    locales = property(fget=get_locales)

    @abc.abstractmethod
    def supports_journal_rollback(self):
        """Test for support of a journaling rollback service.

        :return: ``true`` if this manager supports the journal rollback, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_journal_branching(self):
        """Test for support of a journal branching service.

        :return: ``true`` if this manager supports the journal branching, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_branch_id(self):
        """Gets the ``Branch Id`` representing this service branch.

        :return: the branch ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    branch_id = property(fget=get_branch_id)

    @abc.abstractmethod
    def get_branch(self):
        """Gets this service branch.

        :return: the service branch
        :rtype: ``osid.journaling.Branch``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.journaling.Branch

    branch = property(fget=get_branch)

    @abc.abstractmethod
    def get_proxy_record_types(self):
        """Gets the proxy record ``Types`` supported in this service.

        If no proxy manager is available, an empty list is returned.

        :return: list of proxy record types supported
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    proxy_record_types = property(fget=get_proxy_record_types)

    @abc.abstractmethod
    def supports_proxy_record_type(self, proxy_record_type):
        """Test for support of a proxy type.

        :param proxy_record_type: a proxy record type
        :type proxy_record_type: ``osid.type.Type``
        :return: ``true`` if this service supports the given proxy record type, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class OsidManager:
    """The ``OsidManager`` is the top level interface for all OSID managers.

    An OSID manager is instantiated through the ``OsidRuntimeManager``
    and represents an instance of a service. An OSID manager is
    responsible for implementing a profile for a service and creating
    sessions that, in general, correspond to the profile. An application
    need only create a single ``OsidManager`` per service and
    implementors must ensure the ``OsidManager`` is thread-safe ````.
    The ``OsidSessions`` spawned from an OSID manager are dedicated to
    single processing threads. The ``OsidManager`` defines methods in
    common throughout all OSID managers which implement this interface.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def initialize(self, runtime):
        """Initializes this manager.

        A manager is initialized once at the time of creation.

        :param runtime: the runtime environment
        :type runtime: ``osid.OsidRuntimeManager``
        :raise: ``ConfigurationError`` -- an error with implementation configuration
        :raise: ``IllegalState`` -- this manager has already been initialized by the ``OsidRuntime``
        :raise: ``NullArgument`` -- ``runtime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        ``initialize()`` and must set an ``IllegalState`` error.

        """
        pass

    @abc.abstractmethod
    def rollback_service(self, rollback_time):
        """Rolls back this service to a point in time.

        :param rollback_time: the requested time
        :type rollback_time: ``timestamp``
        :return: the journal entry corresponding to the actual state of this service
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_rollback()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.journaling.JournalEntry

    @abc.abstractmethod
    def change_branch(self, branch_id):
        """Changes the service branch.

        :param branch_id: the new service branch
        :type branch_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidProxyManager:
    """The ``OsidProxyManager`` is the top level interface for all OSID proxy managers.

    A proxy manager accepts parameters to pass through end-user
    authentication credentials and other necessary request parameters in
    a server environment. Native applications should use an
    ``OsidManager`` to maintain a higher degree of interoperability by
    avoiding this coupling.

    An OSID proxy manager is instantiated through the
    ``OsidRuntimeManager`` and represents an instance of a service. An
    OSID manager is responsible for defining clusters of
    interoperability within a service and creating sessions that
    generally correspond to these clusters, An application need only
    create a single ``OsidProxyManager`` per service and implementors
    must ensure the ``OsidProxyManager`` is thread-safe ````. The
    ``OsidSessions`` spawned from an OSID manager are dedicated to
    single processing threads. The ``OsidProxyManager`` defines methods
    in common throughout all OSID managers which implement this
    interface.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def initialize(self, runtime):
        """Initializes this manager.

        A manager is initialized once at the time of creation.

        :param runtime: the runtime environment
        :type runtime: ``osid.OsidRuntimeManager``
        :raise: ``ConfigurationError`` -- an error with implementation configuration
        :raise: ``IllegalState`` -- this manager has already been initialized by the ``OsidRuntime``
        :raise: ``NullArgument`` -- ``runtime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        ``initialize()`` and must set an ``IllegalState`` error.

        """
        pass

    @abc.abstractmethod
    def rollback_service(self, rollback_time, proxy):
        """Rolls back this service to a point in time.

        :param rollback_time: the requested time
        :type rollback_time: ``timestamp``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the journal entry corresponding to the actual state of this service
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_rollback()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.journaling.JournalEntry

    @abc.abstractmethod
    def change_branch(self, branch_id, proxy):
        """Changes the service branch.

        :param branch_id: the new service branch
        :type branch_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidRuntimeProfile:
    """The ``OsidRuntimeProfile`` defines the service aspects of the OSID runtime service."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_configuration(self):
        """Tests if a configuration service is provided within this runtime environment.

        :return: ``true`` if a configuration service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class OsidRuntimeManager:
    """The ``OsidRuntimeManager`` represents and OSID platform and contains the information required for running OSID implementations such as search paths and configurations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_manager(self, osid, impl_class_name, version):
        """Finds, loads and instantiates providers of OSID managers.

        Providers must conform to an OsidManager interface. The
        interfaces are defined in the OSID enumeration. For all OSID
        requests, an instance of ``OsidManager`` that implements the
        ``OsidManager`` interface is returned. In bindings where
        permitted, this can be safely cast into the requested manager.

        :param osid: represents the OSID
        :type osid: ``osid.OSID``
        :param impl_class_name: the name of the implementation
        :type impl_class_name: ``string``
        :param version: the minimum required OSID specification version
        :type version: ``osid.installation.Version``
        :return: the manager of the service
        :rtype: ``osid.OsidManager``
        :raise: ``ConfigurationError`` -- an error in configuring the implementation
        :raise: ``NotFound`` -- the implementation class was not found
        :raise: ``NullArgument`` -- ``impl_class_name`` or ``version`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``impl_class_name`` does not support the requested OSID

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: After finding and instantiating the
        requested ``OsidManager,`` providers must invoke
        ``OsidManager.initialize(OsidRuntimeManager)`` where the
        environment is an instance of the current environment that
        includes the configuration for the service being initialized.
        The ``OsidRuntimeManager`` passed may include information useful
        for the configuration such as the identity of the service being
        instantiated.

        """
        return  # osid.OsidManager

    @abc.abstractmethod
    def get_proxy_manager(self, osid, implementation, version):
        """Finds, loads and instantiates providers of OSID managers.

        Providers must conform to an ``OsidManager`` interface. The
        interfaces are defined in the OSID enumeration. For all OSID
        requests, an instance of ``OsidManager`` that implements the
        ``OsidManager`` interface is returned. In bindings where
        permitted, this can be safely cast into the requested manager.

        :param osid: represents the OSID
        :type osid: ``osid.OSID``
        :param implementation: the name of the implementation
        :type implementation: ``string``
        :param version: the minimum required OSID specification version
        :type version: ``osid.installation.Version``
        :return: the manager of the service
        :rtype: ``osid.OsidProxyManager``
        :raise: ``ConfigurationError`` -- an error in configuring the implementation
        :raise: ``NotFound`` -- the implementation class was not found
        :raise: ``NullArgument`` -- ``implementation`` or ``version`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``implementation`` does not support the requested OSID

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: After finding and instantiating the
        requested ``OsidManager,`` providers must invoke
        ``OsidManager.initialize(OsidRuntimeManager)`` where the
        environment is an instance of the current environment that
        includes the configuration for the service being initialized.
        The ``OsidRuntimeManager`` passed may include information useful
        for the configuration such as the identity of the service being
        instantiated.

        """
        return  # osid.OsidProxyManager

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the current configuration in the runtime environment.

        :return: a configuration
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- an authorization failure occured
        :raise: ``Unimplemented`` -- a configuration service is not supported

        *compliance: optional -- This method must be implemented if
        ``supports_configuration()`` is ``true``.*

        """
        return  # osid.configuration.ValueLookupSession

    configuration = property(fget=get_configuration)
