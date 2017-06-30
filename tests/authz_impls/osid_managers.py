"""osid Managers for stupid authz impls"""

from dlkit.abstract_osid.osid import managers as abc_osid_managers
from dlkit.abstract_osid.osid import markers as abc_osid_markers
from . import profile
from .osid_errors import Unimplemented, NullArgument, IllegalState
from .primitives import Id, Type, DisplayText


class Sourceable(abc_osid_markers.Sourceable):
    """osid Sourceable for stupid authz impls"""

    def get_provider_id(self):
        raise Unimplemented()

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        raise Unimplemented()

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        raise Unimplemented()

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        raise Unimplemented()

    branding = property(fget=get_branding)

    def get_license(self):
        raise Unimplemented()

    license_ = property(fget=get_license)


class OsidProfile(abc_osid_managers.OsidProfile, Sourceable):
    """osid OsidProfile for stupid authz impls"""

    def get_id(self):
        return Id(**profile.ID)

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def get_display_name(self):
        return DisplayText(text=profile.DISPLAYNAME,
                           language_type=Type(**profile.LANGUAGETYPE),
                           script_type=Type(**profile.SCRIPTTYPE),
                           format_type=Type(**profile.FORMATTYPE))

    display_name = property(fget=get_display_name)

    def get_description(self):
        return DisplayText(text=profile.DESCRIPTION,
                           language_type=Type(**profile.LANGUAGETYPE),
                           script_type=Type(**profile.SCRIPTTYPE),
                           format_type=Type(**profile.FORMATTYPE))

    description = property(fget=get_description)

    def get_version(self):
        # THIS ALL NEEDS TO BE FIXED:
        # try:
        #    from ..installation.primitives import Version
        # except:
        #    from .common import Version
        # try:
        #    from ..type.primitives import Type
        # except:
        #    from .common import Type
        # return Version(components = profile.VERSIONCOMPONENTS,
        #               scheme = Type(**profile.VERSIONSCHEME))
        raise Unimplemented()

    version = property(fget=get_version)

    def get_release_date(self):
        raise Unimplemented()

    release_date = property(fget=get_release_date)

    def supports_osid_version(self, version=None):
        # THIS ALL NEEDS TO BE FIXED:
        # try:
        #    from ..installation.primitives import Version
        # except:
        #    from .common import Version
        # try:
        #    from ..type.primitives import Type
        # except:
        #    from .common import Type
        # return Version(components = profile.OSIDVERSION,
        #               scheme = Type(**profile.VERSIONSCHEME))
        raise Unimplemented()

    def get_locales(self):
        # NEED TO IMPLEMENT
        raise Unimplemented()

    locales = property(fget=get_locales)

    def supports_journal_rollback(self):
        # Perhaps someday I will support journaling
        return False

    def supports_journal_branching(self):
        # Perhaps someday I will support journaling
        return False

    def get_branch_id(self):
        raise Unimplemented()

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        raise Unimplemented()

    branch = property(fget=get_branch)

    def get_proxy_record_types(self):
        raise Unimplemented()

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, proxy_record_type=None):
        raise Unimplemented()


class OsidManager(abc_osid_managers.OsidManager, OsidProfile):
    """osid OsidManager for stupid authz impls"""

    def __init__(self):
        self._config = None
        self._runtime = None

    def initialize(self, runtime=None):
        if runtime is None:
            raise NullArgument()
        if self._runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._runtime = runtime
        self._config = runtime.get_configuration()

    def rollback_service(self, rollback_time=None):
        raise Unimplemented()

    def change_branch(self, branch_id=None):
        raise Unimplemented()


class OsidProxyManager(abc_osid_managers.OsidProxyManager, OsidProfile):
    """osid OsidProxyManager for stupid authz impls"""

    def __init__(self):
        self._config = None
        self._runtime = None

    def initialize(self, runtime=None):
        if runtime is None:
            raise NullArgument()
        if self._runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._runtime = runtime
        self._config = runtime.get_configuration()

    def rollback_service(self, rollback_time=None, proxy=None):
        raise Unimplemented()

    def change_branch(self, branch_id=None, proxy=None):
        raise Unimplemented()
