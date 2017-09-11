"""DLKit Services implementations of osid service."""
# pylint: disable=no-init
#     osid specification includes some 'marker' interfaces.
# pylint: disable=too-many-ancestors
#     number of ancestors defined in spec.
# pylint: disable=too-few-public-methods,too-many-public-methods
#     number of methods defined in spec. Worse yet, these are aggregates.
# pylint: disable=invalid-name
#     method and class names defined in spec.
# pylint: disable=no-self-use,unused-argument
#     to catch unimplemented methods.
# pylint: disable=super-init-not-called
#     it just isn't.


from .osid_errors import Unimplemented, IllegalState, InvalidArgument
from dlkit.abstract_osid.osid import managers as abc_osid_managers
from dlkit.abstract_osid.osid import markers as abc_osid_markers
from dlkit.abstract_osid.osid import objects as abc_osid_objects
from dlkit.abstract_osid.osid import sessions as abc_osid_sessions


DEFAULT = 0
COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
ANY_STATUS = 0
ACTIVE = 1
UNSEQUESTERED = 0
SEQUESTERED = 1
AUTOMATIC = 0
MANDATORY = 1
DISABLED = -1


class OsidPrimitive(abc_osid_markers.OsidPrimitive):
    """OsidPrimitive convenience adapter including related Session methods."""
    pass


class Identifiable(abc_osid_markers.Identifiable):
    """Identifiable convenience adapter including related Session methods."""
    def __init__(self, osid_object):  # I will never be called :(
        self._osid_object = osid_object

    def get_id(self):
        return self._osid_object.get_id()

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def is_current(self):
        return self._osid_object.is_current()

    current = property(is_current)


class Extensible(abc_osid_markers.Extensible):
    """Extensible convenience adapter including related Session methods."""
    def __init__(self, osid_object):  # I will never be called :(
        self._osid_object = osid_object

    def get_record_types(self):
        return self._osid_object.get_record_types()

    record_types = property(fget=get_record_types)

    def has_record_type(self, *args, **kwargs):
        return self._osid_object.has_record_type(*args, **kwargs)


class Browsable(abc_osid_markers.Browsable):
    """Browsable convenience adapter including related Session methods."""
    def __init__(self, osid_object):  # I will never be called :(
        self._osid_object = osid_object

    def get_properties(self):
        return self._osid_object.get_properties()

    properties = property(fget=get_properties)

    def get_properties_by_record_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class Suppliable(abc_osid_markers.Suppliable):
    """Suppliable convenience adapter including related Session methods."""
    pass


class Temporal(abc_osid_markers.Temporal):
    """Temporal convenience adapter including related Session methods."""

    def is_effective(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_start_date(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    start_date = property(fget=get_start_date)

    def get_end_date(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    end_date = property(fget=get_end_date)


class Subjugateable(abc_osid_markers.Subjugateable):
    """Subjugateable convenience adapter including related Session methods."""
    pass


class Aggregateable(abc_osid_markers.Aggregateable):
    """Aggregateable convenience adapter including related Session methods."""
    pass


class Containable(abc_osid_markers.Containable):
    """Containable convenience adapter including related Session methods."""

    def is_sequestered(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')


class Sourceable(abc_osid_markers.Sourceable):
    """Sourceable convenience adapter including related Session methods."""
    def __init__(self, osid_object):  # I will never be called :(
        self._osid_object = osid_object

    def get_provider_id(self):
        return self._osid_object.get_provider_id()

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        return self._osid_object.get_provider()

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        return self._osid_object.get_branding_ids()

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        return self._osid_object.get_branding()

    branding = property(fget=get_branding)

    def get_license(self):
        return self._osid_object.get_license()

    license_ = property(fget=get_license)


class Federateable(abc_osid_markers.Federateable):
    """Federateable convenience adapter including related Session methods."""
    pass


class Operable(abc_osid_markers.Operable):
    """Operable convenience adapter including related Session methods."""

    def is_active(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def is_enabled(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def is_disabled(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def is_operational(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')


class OsidProfile(abc_osid_managers.OsidProfile):
    """OsidProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def get_id(self):
        pass

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def get_display_name(self):
        return self._provider_manager.get_display_name()

    display_name = property(fget=get_display_name)

    def get_description(self):
        return self._provider_manager.get_description()

    description = property(fget=get_description)

    def get_version(self):
        return self._provider_manager.get_version()

    version = property(fget=get_version)

    def get_release_date(self):
        return self._provider_manager.get_release_date()

    release_date = property(fget=get_release_date)

    def supports_osid_version(self, *args, **kwargs):
        return self._provider_manager.supports_osid_version(*args, **kwargs)

    def get_locales(self):
        return self._provider_manager.get_locales()

    locales = property(fget=get_locales)

    def supports_journal_rollback(self):
        return self._provider_manager.supports_journal_rollback()

    def supports_journal_branching(self):
        return self._provider_manager.supports_journal_branching()

    def get_branch_id(self):
        return self._provider_manager.get_branch_id()

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        return self._provider_manager.get_branch()

    branch = property(fget=get_branch)

    def get_proxy_record_types(self):
        return self._provider_manager.get_proxy_record_types()

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, *args, **kwargs):
        return self._provider_manager.supports_proxy_record_type(*args, **kwargs)


class OsidManager(abc_osid_managers.OsidManager, OsidProfile):
    """OsidManager convenience adapter including related Session methods."""

    def initialize(self, runtime):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def rollback_service(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def change_branch(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class OsidProxyManager(abc_osid_managers.OsidProxyManager, OsidProfile):
    """OsidProxyManager convenience adapter including related Session methods."""

    def initialize(self, runtime):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def rollback_service(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def change_branch(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class OsidSession(abc_osid_sessions.OsidSession):
    """OsidSession convenience adapter including related Session methods."""
    COMPARATIVE = 0
    PLENARY = 1
    FEDERATED = 0
    ISOLATED = 1

    def __init__(self, proxy):
        self._proxy = proxy

    def _get_agent_key(self, proxy=None):
        """Gets an agent key for session management.

        Side effect of setting a new proxy if one is sent along,
        and initializing the provider session map if agent key has
        not been seen before

        """
        if self._proxy is None:
            self._proxy = proxy
        if self._proxy is not None and self._proxy.has_effective_agent():
            agent_key = self._proxy.get_effective_agent_id()
        else:
            agent_key = None
        if agent_key not in self._provider_sessions:
            self._provider_sessions[agent_key] = dict()
        return agent_key

    def _get_provider_sessions(self):
        """Gets list of all known provider sessions."""
        agent_key = self._get_agent_key()
        sessions = []
        for session_name in self._provider_sessions[agent_key]:
            sessions.append(self._provider_sessions[agent_key][session_name])
        return sessions

    def set_proxy(self, proxy):
        """Sets a new Proxy."""
        self._proxy = proxy

    def clear_proxy(self):
        """Sets proxy to None."""
        self._proxy = None

    def get_locale(self):
        pass

    locale = property(fget=get_locale)

    def is_authenticated(self):
        if self._proxy is None:
            return False
        elif self._proxy.has_authentication():
            return self._proxy.get_authentication().is_valid()
        else:
            return False

    def get_authenticated_agent_id(self):
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent_id()
        else:
            raise IllegalState()

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent()
        else:
            raise IllegalState()

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        from .primitives import Id
        if self.is_authenticated():
            if self._proxy.has_effective_agent():
                return self._proxy.get_effective_agent_id()
            else:
                return self._proxy.get_authentication().get_agent_id()
        else:
            return Id(identifier='MC3GUE$T@MIT.EDU',
                      namespace='agent.Agent',
                      authority='MIT-OEIT')

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        # from dlkit.services_impls.authentication.objects import Agent # This may want to be in Primordium?
        # effective_agent_id = self.get_effective_agent_id()
        # This may want to be extended to get the Agent directly from the Authentication
        # if available and if not effective agent is available in the proxy
        # return Agent(identifier=effective_agent_id.get_identifier(),
        #             namespace=effective_agent_id.get_identifier_namespace(),
        #             authority=effective_agent_id.get_authority())
        raise Unimplemented()

    effective_agent = property(fget=get_effective_agent)

    def get_date(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    date = property(fget=get_date)

    def get_clock_rate(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    clock_rate = property(fget=get_clock_rate)

    def get_format_type(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    format_type = property(fget=get_format_type)

    def supports_transactions(self):
        raise Unimplemented()

    def start_transaction(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')


class OsidObject(abc_osid_objects.OsidObject):
    """OsidObject convenience adapter including related Session methods."""
    def __init__(self, osid_object):
        self._osid_object = osid_object

    def get_display_name(self):
        return self._osid_object.get_display_name()

    display_name = property(fget=get_display_name)

    def get_description(self):
        return self._osid_object.get_description()

    description = property(fget=get_description)

    def get_genus_type(self):
        return self._osid_object.get_genus_type()

    genus_type = property(fget=get_genus_type)

    def is_of_genus_type(self, *args, **kwargs):
        return self._osid_object.is_of_genus_type(*args, **kwargs)


class OsidCatalog(abc_osid_objects.OsidCatalog, OsidObject):
    """OsidCatalog convenience adapter including related Session methods."""
    pass


class OsidList(abc_osid_objects.OsidList):
    """OsidList convenience adapter including related Session methods."""
    def __init__(self, iter_object=None, count=None):
        if iter_object is None:
            iter_object = []
        if count is not None:
            self._count = count
        elif isinstance(iter_object, dict) or isinstance(iter_object, list):
            self._count = len(iter_object)
        self._iter_object = iter(iter_object)

    def __iter__(self):
        return self

    def next(self):
        next_object = next(self._iter_object)
        if self._count is not None:
            self._count -= 1
        return next_object

    __next__ = next

    def len(self):
        return self.available()

    def has_next(self):
        if self._count is not None:
            # If count is available, use it
            return bool(self._count)
        else:
            # otherwise we have no idea
            return True

    def available(self):
        if self._count is not None:
            # If count is available, use it
            return self._count
        else:
            # We have no idea.
            return 0  # Don't know what to do here

    def skip(self, n):
        # STILL NEED TO IMPLEMENT THIS ###
        pass


class OsidRuntimeProfile(abc_osid_managers.OsidRuntimeProfile, OsidProfile):
    """OsidRuntimeProfile convenience adapter including related Session methods."""

    def supports_configuration(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')


class OsidRuntimeManager(abc_osid_managers.OsidRuntimeManager, OsidManager, OsidRuntimeProfile):
    """OsidRuntimeManager convenience adapter including related Session methods."""

    def get_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_configuration(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    configuration = property(fget=get_configuration)
