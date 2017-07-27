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


    def get_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def is_current(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')


class Extensible(abc_osid_markers.Extensible):
    """Extensible convenience adapter including related Session methods."""


    def get_record_types(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    record_types = property(fget=get_record_types)

    def has_record_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class Browsable(abc_osid_markers.Browsable):
    """Browsable convenience adapter including related Session methods."""

    def get_properties(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

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

    def get_provider_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    branding = property(fget=get_branding)

    def get_license(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

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


    def get_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def get_display_name(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    description = property(fget=get_description)

    def get_version(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    version = property(fget=get_version)

    def get_release_date(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    release_date = property(fget=get_release_date)

    def supports_osid_version(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_locales(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    locales = property(fget=get_locales)

    def supports_journal_rollback(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def supports_journal_branching(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_branch_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    branch = property(fget=get_branch)

    def get_proxy_record_types(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


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


class OsidProxyManager(abc_osid_managers.OsidProxyManager, OsidProfile, OsidManager):
    """OsidProxyManager convenience adapter including related Session methods."""
    pass


class OsidSession(abc_osid_sessions.OsidSession):
    """OsidSession convenience adapter including related Session methods."""


    def get_locale(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    locale = property(fget=get_locale)

    def is_authenticated(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_authenticated_agent_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

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
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def start_transaction(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')


class OsidObject(abc_osid_objects.OsidObject):
    """OsidObject convenience adapter including related Session methods."""


    def get_display_name(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    description = property(fget=get_description)

    def get_genus_type(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    genus_type = property(fget=get_genus_type)

    def is_of_genus_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class OsidCatalog(abc_osid_objects.OsidCatalog, OsidObject):
    """OsidCatalog convenience adapter including related Session methods."""
    pass


class OsidList(abc_osid_objects.OsidList):
    """OsidList convenience adapter including related Session methods."""


    def has_next(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def available(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def skip(self, n):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


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
