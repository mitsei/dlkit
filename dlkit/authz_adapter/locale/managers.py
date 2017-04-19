"""AuthZ Adapter implementations of locale managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from ..osid.osid_errors import Unimplemented, OperationFailed
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.locale import managers as locale_managers


class LocaleProfile(osid_managers.OsidProfile, locale_managers.LocaleProfile):
    """Adapts underlying LocaleProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_no_catalog_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_no_catalog_hierarchy_session()
        except Unimplemented:
            return None

    @raise_null_argument
    def get_language_types_for_source(self, source_language_type, source_script_type):
        raise Unimplemented()

    def get_source_language_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_language_types()

    source_language_types = property(fget=get_source_language_types)

    @raise_null_argument
    def get_script_types_for_language_type(self, language_type):
        raise Unimplemented()

    def get_numeric_format_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_numeric_format_types()

    numeric_format_types = property(fget=get_numeric_format_types)

    def get_calendar_types_for_formatting(self):
        raise Unimplemented()

    calendar_types_for_formatting = property(fget=get_calendar_types_for_formatting)

    @raise_null_argument
    def get_date_format_types_for_calendar_type(self, calendar_type):
        raise Unimplemented()

    def get_time_types_for_formatting(self):
        raise Unimplemented()

    time_types_for_formatting = property(fget=get_time_types_for_formatting)

    @raise_null_argument
    def get_time_format_types_for_time_type(self, time_type):
        raise Unimplemented()

    def get_currency_types_for_formatting(self):
        raise Unimplemented()

    currency_types_for_formatting = property(fget=get_currency_types_for_formatting)

    @raise_null_argument
    def get_currency_format_types_for_currency_type(self, currency_type):
        raise Unimplemented()

    def get_coordinate_types_for_formatting(self):
        raise Unimplemented()

    coordinate_types_for_formatting = property(fget=get_coordinate_types_for_formatting)

    @raise_null_argument
    def get_coordinate_format_types_for_coordinate_type(self, coordinate_type):
        raise Unimplemented()

    @raise_null_argument
    def get_unit_types_for_source(self, source_unit_type):
        raise Unimplemented()

    def get_source_unit_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_unit_types()

    source_unit_types = property(fget=get_source_unit_types)

    @raise_null_argument
    def get_currency_types_for_source(self, source_currency_type):
        raise Unimplemented()

    def get_source_currency_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_currency_types()

    source_currency_types = property(fget=get_source_currency_types)

    @raise_null_argument
    def get_calendar_types_for_source(self, source_calendar_type):
        raise Unimplemented()

    def get_source_calendar_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_calendar_types()

    source_calendar_types = property(fget=get_source_calendar_types)

    @raise_null_argument
    def get_time_types_for_source(self, source_time_type):
        raise Unimplemented()

    def get_source_time_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_time_types()

    source_time_types = property(fget=get_source_time_types)

    @raise_null_argument
    def get_time_types_for_calendar_type(self, calendar_type):
        raise Unimplemented()

    @raise_null_argument
    def get_calendar_types_for_time_type(self, time_type):
        raise Unimplemented()

    @raise_null_argument
    def get_coordinate_types_for_source(self, source_coordinate_type):
        raise Unimplemented()

    def get_source_coordinate_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_coordinate_types()

    source_coordinate_types = property(fget=get_source_coordinate_types)

    @raise_null_argument
    def get_spatial_unit_record_types_for_source(self, source_spatial_unit_record_type):
        raise Unimplemented()

    def get_source_spatial_unit_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_source_spatial_unit_record_types()

    source_spatial_unit_record_types = property(fget=get_source_spatial_unit_record_types)

    @raise_null_argument
    def get_format_types_for_source(self, source_format_type):
        raise Unimplemented()

    def get_source_format_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_source_format_types()

    source_format_types = property(fget=get_source_format_types)


class LocaleManager(osid_managers.OsidManager, LocaleProfile, locale_managers.LocaleManager):
    """Adapts underlying LocaleManager methodswith authorization checks."""
    def __init__(self):
        LocaleProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:localeProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('LOCALE', provider_impl)
        # need to add version argument


class LocaleProxyManager(osid_managers.OsidProxyManager, LocaleProfile, locale_managers.LocaleProxyManager):
    """Adapts underlying LocaleProxyManager methodswith authorization checks."""
    def __init__(self):
        LocaleProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:localeProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('LOCALE', provider_impl)
        # need to add version argument
