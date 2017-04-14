"""AWS Adapter osid manager implementations."""

from ...abstract_osid.osid import managers as abc_osid_managers
from ..osid import markers as osid_markers
from ..primitives import Id
from ..osid.osid_errors import NullArgument, IllegalState


class OsidProfile(abc_osid_managers.OsidProfile, osid_markers.Sourceable):
    """The ``OsidProfile`` defines the interoperability areas of an OSID.

    An ``OsidProfile`` is implemented by an ``OsidManager``. The top
    level ``OsidProfile`` tests for version compatibility. Each OSID
    extends this interface to include its own interoperability
    definitions within its managers.

    """

    def __init__(self):
        self._my_runtime = None
        self._provider_manager = None
        self._config_map = {}

    def _initialize(self, runtime):
        """Common initializer for OsidManager and OsidProxyManager"""

        if runtime is None:
            raise NullArgument()
        if self._my_runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._my_runtime = runtime
        config = runtime.get_configuration()

        cf_public_key_param_id = Id('parameter:cloudFrontPublicKey@aws_adapter')
        cf_private_key_param_id = Id('parameter:cloudFrontPrivateKey@aws_adapter')
        cf_keypair_id_param_id = Id('parameter:cloudFrontSigningKeypairId@aws_adapter')
        cf_private_key_file_param_id = Id('parameter:cloudFrontSigningPrivateKeyFile@aws_adapter')
        cf_distro_param_id = Id('parameter:cloudFrontDistro@aws_adapter')
        cf_distro_id_param_id = Id('parameter:cloudFrontDistroId@aws_adapter')
        s3_public_key_param_id = Id('parameter:S3PublicKey@aws_adapter')
        s3_private_key_param_id = Id('parameter:S3PrivateKey@aws_adapter')
        s3_bucket_param_id = Id('parameter:S3Bucket@aws_adapter')

        cf_public_key = config.get_value_by_parameter(cf_public_key_param_id).get_string_value()
        cf_private_key = config.get_value_by_parameter(cf_private_key_param_id).get_string_value()
        cf_keypair_id = config.get_value_by_parameter(cf_keypair_id_param_id).get_string_value()
        cf_private_key_file = config.get_value_by_parameter(
            cf_private_key_file_param_id).get_string_value()
        cf_distro = config.get_value_by_parameter(cf_distro_param_id).get_string_value()
        cf_distro_id = config.get_value_by_parameter(cf_distro_id_param_id).get_string_value()
        s3_public_key = config.get_value_by_parameter(s3_public_key_param_id).get_string_value()
        s3_private_key = config.get_value_by_parameter(s3_private_key_param_id).get_string_value()
        s3_bucket = config.get_value_by_parameter(s3_bucket_param_id).get_string_value()

        self._config_map['cloudfront_public_key'] = cf_public_key
        self._config_map['cloudfront_private_key'] = cf_private_key
        self._config_map['cloudfront_keypair_id'] = cf_keypair_id
        self._config_map['cloudfront_private_key_file'] = cf_private_key_file
        self._config_map['cloudfront_distro'] = cf_distro
        self._config_map['cloudfront_distro_id'] = cf_distro_id
        self._config_map['put_public_key'] = s3_public_key
        self._config_map['put_private_key'] = s3_private_key
        self._config_map['s3_bucket'] = s3_bucket

    def get_id(self):
        """Gets an identifier for this service implementation.

        The identifier is unique among services but multiple
        instantiations of the same service use the same ``Id``. This
        identifier is the same identifier used in managing OSID
        installations.

        return: (osid.id.Id) - the ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_id()

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def get_display_name(self):
        """Gets a display name for this service implementation.

        return: (osid.locale.DisplayText) - a display name
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_display_name()

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Gets a description of this service implementation.

        return: (osid.locale.DisplayText) - a description
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_description()

    description = property(fget=get_description)

    def get_version(self):
        """Gets the version of this service implementation.

        return: (osid.installation.Version) - the service implementation
                version
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_version()

    version = property(fget=get_version)

    def get_release_date(self):
        """Gets the date this service implementation was released.

        return: (osid.calendaring.DateTime) - the release date
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_release_date()

    release_date = property(fget=get_release_date)

    def supports_osid_version(self, version):
        """Test for support of an OSID specification version.

        arg:    version (osid.installation.Version): the specification
                version to test
        return: (boolean) - ``true`` if this manager supports the given
                OSID version, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: An implementation may support multiple
        versions of an OSID.

        """
        return self._provider_manager.supports_osid_version(version)

    def get_locales(self):
        """Gets the locales supported in this service.

        return: (osid.locale.LocaleList) - list of locales supported
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_locales()

    locales = property(fget=get_locales)

    def supports_journal_rollback(self):
        """Test for support of a journaling rollback service.

        return: (boolean) - ``true`` if this manager supports the
                journal rollback, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.supports_journal_rollback()

    def supports_journal_branching(self):
        """Test for support of a journal branching service.

        return: (boolean) - ``true`` if this manager supports the
                journal branching, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.supports_journal_branching()

    def get_branch_id(self):
        """Gets the ``Branch Id`` representing this service branch.

        return: (osid.id.Id) - the branch ``Id``
        raise:  Unimplemented - ``supports_journal_branching()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_branch_id()

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        """Gets this service branch.

        return: (osid.journaling.Branch) - the service branch
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_journal_branching()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_branch()

    branch = property(fget=get_branch)

    def get_proxy_record_types(self):
        """Gets the proxy record ``Types`` supported in this service.

        If no proxy manager is available, an empty list is returned.

        return: (osid.type.TypeList) - list of proxy record types
                supported
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.get_proxy_record_types()

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, proxy_record_type):
        """Test for support of a proxy type.

        arg:    proxy_record_type (osid.type.Type): a proxy record type
        return: (boolean) - ``true`` if this service supports the given
                proxy record type, ``false`` otherwise
        raise:  NullArgument - ``proxy_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.supports_proxy_record_type(proxy_record_type)


class OsidManager(abc_osid_managers.OsidManager, OsidProfile):
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

    def __init__(self):
        OsidProfile.__init__(self)

    def initialize(self, runtime):
        """Initializes this manager.

        A manager is initialized once at the time of creation.

        arg:    runtime (osid.OsidRuntimeManager): the runtime
                environment
        raise:  ConfigurationError - an error with implementation
                configuration
        raise:  IllegalState - this manager has already been initialized
                by the ``OsidRuntime``
        raise:  NullArgument - ``runtime`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        ``initialize()`` and must set an ``IllegalState`` error.

        """
        OsidProfile._initialize(self, runtime)

    def rollback_service(self, rollback_time):
        """Rolls back this service to a point in time.

        arg:    rollback_time (timestamp): the requested time
        return: (osid.journaling.JournalEntry) - the journal entry
                corresponding to the actual state of this service
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unimplemented - ``supports_journal_rollback()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.rollback_service(rollback_time)

    def change_branch(self, branch_id):
        """Changes the service branch.

        arg:    branch_id (osid.id.Id): the new service branch
        raise:  NotFound - ``branch_id`` not found
        raise:  NullArgument - ``branch_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unimplemented - ``supports_journal_branching()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.change_branch(branch_id)


class OsidProxyManager(abc_osid_managers.OsidProxyManager, OsidProfile):
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

    def __init__(self):
        OsidProfile.__init__(self)

    def initialize(self, runtime):
        """Initializes this manager.

        A manager is initialized once at the time of creation.

        arg:    runtime (osid.OsidRuntimeManager): the runtime
                environment
        raise:  ConfigurationError - an error with implementation
                configuration
        raise:  IllegalState - this manager has already been initialized
                by the ``OsidRuntime``
        raise:  NullArgument - ``runtime`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        ``initialize()`` and must set an ``IllegalState`` error.

        """
        OsidProfile._initialize(self, runtime)

    def rollback_service(self, rollback_time, proxy):
        """Rolls back this service to a point in time.

        arg:    rollback_time (timestamp): the requested time
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.journaling.JournalEntry) - the journal entry
                corresponding to the actual state of this service
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unimplemented - ``supports_journal_rollback()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.rollback_service(rollback_time)

    def change_branch(self, branch_id, proxy):
        """Changes the service branch.

        arg:    branch_id (osid.id.Id): the new service branch
        arg:    proxy (osid.proxy.Proxy): a proxy
        raise:  NotFound - ``branch_id`` not found
        raise:  NullArgument - ``branch_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unimplemented - ``supports_journal_branching()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._provider_manager.change_branch(branch_id)
