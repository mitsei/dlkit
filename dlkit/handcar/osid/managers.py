# -*- coding: utf-8 -*-

# This module contains all the Manager classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service.
# Note that it includes the core OsidProfile typically found in the osid
# package as well as the learning package managers.

from ...abstract_osid.osid import managers as abc_osid_managers
from . import markers
from .. import profile
from .. import settings
from ..primitives import Id, DisplayText, Type
from ..proxy.rules import Proxy
from .osid_errors import NotFound, NullArgument, OperationFailed, Unimplemented, IllegalState


class OsidProfile(abc_osid_managers.OsidProfile, markers.Sourceable):
    """The OsidProfile defines the interoperability areas of an OSID.

    An OsidProfile is implemented by an OsidManager. The top level
    OsidProfile tests for version compatibility. Each OSID extends this
    interface to include its own interoperability definitions within its
    managers.

    """

    def get_id(self):
        """Gets an identifier for this service implementation.
        The identifier is unique among services but multiple
        instantiations of the same service use the same Id. This
        identifier is the same identifier used in managing OSID
        installations.
        return: (osid.id.Id) - the Id
        compliance: mandatory - This method must be implemented.

        """
        return Id(**profile.ID)

    def get_display_name(self):
        """Gets a display name for this service implementation.

        return: (osid.locale.DisplayText) - a display name
        compliance: mandatory - This method must be implemented.

        """
        return DisplayText({'text': profile.DISPLAYNAME,
                            'languageTypeId': profile.LANGUAGETYPEID,
                            'scriptTypeId': profile.SCRIPTTYPEID,
                            'formatTypeId': profile.FORMATTYPEID})

    def get_description(self):
        """Gets a description of this service implementation.

        return: (osid.locale.DisplayText) - a description
        compliance: mandatory - This method must be implemented.

        """
        return DisplayText({'text': profile.DESCRIPTION,
                            'languageTypeId': profile.LANGUAGETYPEID,
                            'scriptTypeId': profile.SCRIPTTYPEID,
                            'formatTypeId': profile.FORMATTYPEID})

    def get_version(self):
        """Gets the version of this service implementation.

        return: (osid.installation.Version) - the service implementation
                version
        compliance: mandatory - This method must be implemented.

        """
        # Need to implement installation.Version primitive
        pass

    def get_release_date(self):
        """Gets the date this service implementation was released.

        return: (osid.calendaring.DateTime) - the release date
        compliance: mandatory - This method must be implemented.

        """
        # Need to implement calendar.DataTime primitive
        raise Unimplemented()

    def supports_osid_version(self, version=None):
        """Test for support of an OSID specification version.

        arg:    version (osid.installation.Version): the specification
                version to test
        return: (boolean) - true if this manager supports the given OSID
                version, false otherwise
        compliance: mandatory - This method must be implemented.
        implementation notes: An implementation may support multiple
        versions of an OSID.

        """
        # Need to implement installation.Version primitive
        raise Unimplemented()

    def get_locales(self):
        """Gets the locales supported in this service.

        return: (osid.locale.LocaleList) - list of locales supported
        compliance: mandatory - This method must be implemented.

        """
        # Need to implement locale.Locale object
        raise Unimplemented()

    def supports_journal_rollback(self):
        """Test for support of a journaling rollback service.

        return: (boolean) - true if this manager supports the journal
                rollback, false otherwise
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will support journaling!!!
        return False

    def supports_journal_branching(self):
        """Test for support of a journal branching service.

        return: (boolean) - true if this manager supports the journal
                branching, false otherwise
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will support journaling!!!
        return False

    def get_branch_id(self):
        """Gets the Branch Id representing this service branch.

        return: (osid.id.Id) - the branch Id
        raise:  Unimplemented - supports_journal_branching() is false
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will support journaling!!!
        raise Unimplemented()

    def get_branch(self):
        """Gets this service branch.

        return: (osid.journaling.Branch) - the service branch
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - supports_journal_branching() is false
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will support journaling
        raise Unimplemented()

    def get_proxy_record_types(self):
        """Gets the proxy record Types supported in this service.
        If no proxy manager is available, an empty list is returned.
        return: (osid.type.TypeList) - list of proxy record types
                supported
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will know what to do.
        from objects import TypeList
        return TypeList([])

    def supports_proxy_record_type(self, proxy_record_type=None):
        """Test for support of a proxy type.

        arg:    proxyRecordType (osid.type.Type): a proxy record type
        return: (boolean) - true if this service supports the given
                proxy record type, false otherwise
        raise:  NullArgument - proxyRecordType is null
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will know what to do.
        raise Unimplemented()

    id_ = property(get_id)
    ident = property(get_id)
    display_name = property(get_display_name)
    description = property(get_description)
    version = property(get_version)
    release_date = property(get_release_date)
    locales = property(get_locales)
    branch_id = property(get_branch_id)
    branch = property(get_branch)
    proxy_record_types = property(get_proxy_record_types)


class OsidManager(abc_osid_managers.OsidManager, OsidProfile):
    """The OsidManager is the top level interface for all OSID managers.

    An OSID manager is instantiated through the OsidRuntimeManager and
    represents an instance of a service. An OSID manager is responsible
    for implementing a profile for a service and creating sessions that,
    in general, correspond to the profile. An application need only
    create a single OsidManager per service and implementors must ensure
    the OsidManager is thread-safe . The OsidSessions spawned from an
    OSID manager are dedicated to single processing threads. The
    OsidManager defines methods in common throughout all OSID managers
    which implement this interface.

    """
    def __init__(self):
        self._host = settings.HOST
        self._app_key = settings.APP_KEYS[self._host.lower()]
        self._runtime = None

    def initialize(self, runtime=None):
        """Initializes this manager.
        A manager is initialized once at the time of creation.
        arg:    runtime (osid.OsidRuntimeManager): the runtime
                environment
        raise:  CONFIGURATION_ERROR - an error with implementation
                configuration
        raise:  ILLEGAL_STATE - this manager has already been
                initialized by the OsidRuntime
        raise:  NullArgument - runtime is null
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.
        implementation notes: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        initialize() and must set an ILLEGAL_STATE error.

        """
        if self._runtime is not None:
            raise IllegalState()
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:hostName@dlkit_service')
        host = config.get_value_by_parameter(parameter_id).get_string_value()
        if host is not None:
            self._host = host
        parameter_id = Id('parameter:appKey@dlkit_service')
        app_key = config.get_value_by_parameter(parameter_id).get_string_value()
        if app_key is not None:
            self._app_key = app_key

    def rollback_service(self, rollback_time=None):
        """Rolls back this service to a point in time.

        arg:    rollbackTime (timestamp): the requested time
        return: (osid.journaling.JournalEntry) - the journal entry
                corresponding to the actual state of this service
        raise:  OperationFailed - unable to complete request
        raise:  PERMISSION_DENIED - authorization failure occurred
        raise:  Unimplemented - supports_journal_rollback() is false
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will support journaling
        raise Unimplemented()

    def change_branch(self, branch_id=None):
        """Changes the service branch.

        arg:    branchId (osid.id.Id): the new service branch
        raise:  NotFound - branchId not found
        raise:  NullArgument - branchId is null
        raise:  OperationFailed - unable to complete request
        raise:  PERMISSION_DENIED - authorization failure occurred
        raise:  Unimplemented - supports_journal_branching() is false
        compliance: mandatory - This method must be implemented.

        """
        # Perhaps someday I will support journaling
        raise Unimplemented()


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
        self._converted_proxy = None
        self._host = settings.HOST
        self._app_key = settings.APP_KEYS[self._host.lower()]
        self._runtime = None

    def _convert_proxy(self, proxy):
        if self._converted_proxy is None:
            self._converted_proxy = Proxy(proxy, self._host, self._app_key)
        return self._converted_proxy

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
        if self._runtime is not None:
            raise IllegalState()
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:hostName@dlkit_service')
        host = config.get_value_by_parameter(parameter_id).get_string_value()
        if host is not None:
            self._host = host
        parameter_id = Id('parameter:appKey@dlkit_service')
        app_key = config.get_value_by_parameter(parameter_id).get_string_value()
        if app_key is not None:
            self._app_key = app_key

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
        :raise: ``Unimplemented`` -- ``supports_journal_rollback()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        # Perhaps someday I will support journaling
        raise Unimplemented()

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
        # Perhaps someday I will support journaling
        raise Unimplemented()
