"""DLKit Services implementations of locale service."""
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


from . import osid
from .osid_errors import Unimplemented, IllegalState, InvalidArgument
from dlkit.manager_impls.locale import managers as locale_managers


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


class LocaleProfile(osid.OsidProfile, locale_managers.LocaleProfile):
    """LocaleProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def get_language_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_language_types(self):
        """Pass through to provider get_source_language_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_language_types()

    source_language_types = property(fget=get_source_language_types)

    def get_script_types_for_language_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_numeric_format_types(self):
        """Pass through to provider get_numeric_format_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_numeric_format_types()

    numeric_format_types = property(fget=get_numeric_format_types)

    def get_calendar_types_for_formatting(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    calendar_types_for_formatting = property(fget=get_calendar_types_for_formatting)

    def get_date_format_types_for_calendar_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_time_types_for_formatting(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    time_types_for_formatting = property(fget=get_time_types_for_formatting)

    def get_time_format_types_for_time_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_currency_types_for_formatting(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    currency_types_for_formatting = property(fget=get_currency_types_for_formatting)

    def get_currency_format_types_for_currency_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_coordinate_types_for_formatting(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    coordinate_types_for_formatting = property(fget=get_coordinate_types_for_formatting)

    def get_coordinate_format_types_for_coordinate_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_unit_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_unit_types(self):
        """Pass through to provider get_source_unit_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_unit_types()

    source_unit_types = property(fget=get_source_unit_types)

    def get_currency_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_currency_types(self):
        """Pass through to provider get_source_currency_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_currency_types()

    source_currency_types = property(fget=get_source_currency_types)

    def get_calendar_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_calendar_types(self):
        """Pass through to provider get_source_calendar_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_calendar_types()

    source_calendar_types = property(fget=get_source_calendar_types)

    def get_time_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_time_types(self):
        """Pass through to provider get_source_time_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_time_types()

    source_time_types = property(fget=get_source_time_types)

    def get_time_types_for_calendar_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_calendar_types_for_time_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_coordinate_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_coordinate_types(self):
        """Pass through to provider get_source_coordinate_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_coordinate_types()

    source_coordinate_types = property(fget=get_source_coordinate_types)

    def get_spatial_unit_record_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_spatial_unit_record_types(self):
        """Pass through to provider get_source_spatial_unit_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_source_spatial_unit_record_types()

    source_spatial_unit_record_types = property(fget=get_source_spatial_unit_record_types)

    def get_format_types_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_source_format_types(self):
        """Pass through to provider get_source_format_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_format_types()

    source_format_types = property(fget=get_source_format_types)


class LocaleManager(osid.OsidManager, osid.OsidSession, LocaleProfile, locale_managers.LocaleManager):
    """LocaleManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._no_catalog_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_no_catalog_view(self, session):
        """Sets the underlying no_catalog view to match current view"""
        if self._no_catalog_view == COMPARATIVE:
            try:
                session.use_comparative_no_catalog_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_no_catalog_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_no_catalog_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            try:
                session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                    proxy=self._proxy,
                                                    manager=manager)
            except AttributeError:
                session = self._instantiate_session('get_' + session_name,
                                                    proxy=self._proxy,
                                                    manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        if 'manager' in kwargs:
            session_class = getattr(kwargs['manager'], method_name)
            del kwargs['manager']
        else:
            session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:localeProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('LOCALE', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('LOCALE', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()


class LocaleProxyManager(osid.OsidProxyManager, LocaleProfile, locale_managers.LocaleProxyManager):
    """LocaleProxyManager convenience adapter including related Session methods."""
    pass
