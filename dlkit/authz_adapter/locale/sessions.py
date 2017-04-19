"""AuthZ Adapter implementations of locale sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import sessions as osid_sessions
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.abstract_osid.locale import sessions as abc_locale_sessions


class TranslationSession(abc_locale_sessions.TranslationSession, osid_sessions.OsidSession):
    """Adapts underlying TranslationSession methodswith authorization checks."""

    def get_source_language_type(self):
        raise Unimplemented()

    source_language_type = property(fget=get_source_language_type)

    def get_source_script_type(self):
        raise Unimplemented()

    source_script_type = property(fget=get_source_script_type)

    def get_target_language_type(self):
        raise Unimplemented()

    target_language_type = property(fget=get_target_language_type)

    def get_target_script_type(self):
        raise Unimplemented()

    target_script_type = property(fget=get_target_script_type)

    def can_translate(self):
        raise Unimplemented()

    @raise_null_argument
    def get_translation(self, string):
        raise Unimplemented()

    @raise_null_argument
    def translate_string(self, string, default_string):
        raise Unimplemented()

    @raise_null_argument
    def translate_strings(self, strings, default_strings):
        raise Unimplemented()


class TranslationAdminSession(abc_locale_sessions.TranslationAdminSession, osid_sessions.OsidSession):
    """Adapts underlying TranslationAdminSession methodswith authorization checks."""

    def get_source_language_type(self):
        raise Unimplemented()

    source_language_type = property(fget=get_source_language_type)

    def get_source_script_type(self):
        raise Unimplemented()

    source_script_type = property(fget=get_source_script_type)

    def get_target_language_type(self):
        raise Unimplemented()

    target_language_type = property(fget=get_target_language_type)

    def get_target_script_type(self):
        raise Unimplemented()

    target_script_type = property(fget=get_target_script_type)

    def can_update_translation(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def add_translation(self, source_text, target_text):
        raise Unimplemented()

    @raise_null_argument
    def remove_translation(self, source_text):
        raise Unimplemented()


class NumericFormattingSession(abc_locale_sessions.NumericFormattingSession, osid_sessions.OsidSession):
    """Adapts underlying NumericFormattingSession methodswith authorization checks."""

    def get_numeric_format_type(self):
        raise Unimplemented()

    numeric_format_type = property(fget=get_numeric_format_type)

    def can_format_numbers(self):
        raise Unimplemented()

    @raise_null_argument
    def cardinal_to_string(self, c):
        raise Unimplemented()

    @raise_null_argument
    def cardinals_to_strings(self, c):
        raise Unimplemented()

    @raise_null_argument
    def string_to_cardinal(self, str_):
        raise Unimplemented()

    @raise_null_argument
    def decimal_to_string(self, d):
        raise Unimplemented()

    @raise_null_argument
    def decimals_to_strings(self, d):
        raise Unimplemented()

    @raise_null_argument
    def decimal_to_string(self, str_):
        raise Unimplemented()

    @raise_null_argument
    def integer_to_string(self, i):
        raise Unimplemented()

    @raise_null_argument
    def integers_to_strings(self, i):
        raise Unimplemented()

    @raise_null_argument
    def integer_to_string(self, str_):
        raise Unimplemented()


class CalendarFormattingSession(abc_locale_sessions.CalendarFormattingSession, osid_sessions.OsidSession):
    """Adapts underlying CalendarFormattingSession methodswith authorization checks."""

    def get_calendar_type(self):
        raise Unimplemented()

    calendar_type = property(fget=get_calendar_type)

    def get_time_type(self):
        raise Unimplemented()

    time_type = property(fget=get_time_type)

    def get_date_format_type(self):
        raise Unimplemented()

    date_format_type = property(fget=get_date_format_type)

    def get_time_format_type(self):
        raise Unimplemented()

    time_format_type = property(fget=get_time_format_type)

    def can_display_primitives(self):
        raise Unimplemented()

    @raise_null_argument
    def datetime_to_string(self, datetime):
        raise Unimplemented()

    @raise_null_argument
    def datetimes_to_strings(self, datetimes):
        raise Unimplemented()

    @raise_null_argument
    def string_to_date_time(self, s):
        raise Unimplemented()

    @raise_null_argument
    def time_to_string(self, time):
        raise Unimplemented()

    @raise_null_argument
    def times_to_strings(self, times):
        raise Unimplemented()

    @raise_null_argument
    def string_to_time(self, s):
        raise Unimplemented()

    @raise_null_argument
    def duration_to_string(self, duration):
        raise Unimplemented()

    @raise_null_argument
    def durations_to_strings(self, durations):
        raise Unimplemented()

    @raise_null_argument
    def string_to_duration(self, s):
        raise Unimplemented()


class CurrencyFormattingSession(abc_locale_sessions.CurrencyFormattingSession, osid_sessions.OsidSession):
    """Adapts underlying CurrencyFormattingSession methodswith authorization checks."""

    def get_currency_type(self):
        raise Unimplemented()

    currency_type = property(fget=get_currency_type)

    def get_numeric_format_type(self):
        raise Unimplemented()

    numeric_format_type = property(fget=get_numeric_format_type)

    def can_format_currencies(self):
        raise Unimplemented()

    @raise_null_argument
    def currency_to_string(self, amount):
        raise Unimplemented()

    @raise_null_argument
    def currencies_to_strings(self, amounts):
        raise Unimplemented()

    @raise_null_argument
    def string_to_currency(self, s):
        raise Unimplemented()


class CoordinateFormattingSession(abc_locale_sessions.CoordinateFormattingSession, osid_sessions.OsidSession):
    """Adapts underlying CoordinateFormattingSession methodswith authorization checks."""

    def get_coordinate_type(self):
        raise Unimplemented()

    coordinate_type = property(fget=get_coordinate_type)

    def get_coordinate_format_type(self):
        raise Unimplemented()

    coordinate_format_type = property(fget=get_coordinate_format_type)

    def can_format_coordinates(self):
        raise Unimplemented()

    @raise_null_argument
    def coordinate_to_string(self, coordinate):
        raise Unimplemented()

    @raise_null_argument
    def ccoordinates_to_strings(self, coordinates):
        raise Unimplemented()

    @raise_null_argument
    def string_to_coordinate(self, s):
        raise Unimplemented()


class UnitConversionSession(abc_locale_sessions.UnitConversionSession, osid_sessions.OsidSession):
    """Adapts underlying UnitConversionSession methodswith authorization checks."""

    def can_convert_units(self):
        raise Unimplemented()

    @raise_null_argument
    def convert_unit(self, source_unit, source_unit_type, target_unit_type):
        raise Unimplemented()

    @raise_null_argument
    def convert_units(self, source_units, source_unit_type, target_unit_type):
        raise Unimplemented()


class CurrencyConversionSession(abc_locale_sessions.CurrencyConversionSession, osid_sessions.OsidSession):
    """Adapts underlying CurrencyConversionSession methodswith authorization checks."""

    def get_source_currency_type(self):
        raise Unimplemented()

    source_currency_type = property(fget=get_source_currency_type)

    def get_target_currency_type(self):
        raise Unimplemented()

    target_currency_type = property(fget=get_target_currency_type)

    def can_convert_currency(self):
        raise Unimplemented()

    @raise_null_argument
    def convert_currency(self, source_currency_amount):
        raise Unimplemented()

    @raise_null_argument
    def convert_currencies(self, source_currency_amounts):
        raise Unimplemented()


class CalendarConversionSession(abc_locale_sessions.CalendarConversionSession, osid_sessions.OsidSession):
    """Adapts underlying CalendarConversionSession methodswith authorization checks."""

    def get_source_calendar_type(self):
        raise Unimplemented()

    source_calendar_type = property(fget=get_source_calendar_type)

    def get_source_time_type(self):
        raise Unimplemented()

    source_time_type = property(fget=get_source_time_type)

    def get_target_calendar_type(self):
        raise Unimplemented()

    target_calendar_type = property(fget=get_target_calendar_type)

    def get_target_time_type(self):
        raise Unimplemented()

    target_time_type = property(fget=get_target_time_type)

    def can_convert_calendars(self):
        raise Unimplemented()

    @raise_null_argument
    def convert_calendar(self, source_date):
        raise Unimplemented()

    @raise_null_argument
    def convert_calendars(self, source_date_list):
        raise Unimplemented()


class CoordinateConversionSession(abc_locale_sessions.CoordinateConversionSession, osid_sessions.OsidSession):
    """Adapts underlying CoordinateConversionSession methodswith authorization checks."""

    def get_source_coordinate_type(self):
        raise Unimplemented()

    source_coordinate_type = property(fget=get_source_coordinate_type)

    def get_target_coordinate_type(self):
        raise Unimplemented()

    target_coordinate_type = property(fget=get_target_coordinate_type)

    def can_convert_coordinates(self):
        raise Unimplemented()

    @raise_null_argument
    def convert_coordinate(self, source_coordinate):
        raise Unimplemented()

    @raise_null_argument
    def convert_coordinates(self, source_coordinate_list):
        raise Unimplemented()


class SpatialUnitConversionSession(abc_locale_sessions.SpatialUnitConversionSession, osid_sessions.OsidSession):
    """Adapts underlying SpatialUnitConversionSession methodswith authorization checks."""

    def get_source_spatial_unit_record_type(self):
        raise Unimplemented()

    source_spatial_unit_record_type = property(fget=get_source_spatial_unit_record_type)

    def get_target_spatial_unit_record_type(self):
        raise Unimplemented()

    target_spatial_unit_record_type = property(fget=get_target_spatial_unit_record_type)

    def can_convert_spatial_units(self):
        raise Unimplemented()

    @raise_null_argument
    def convert_spatial_unit(self, source_spatial_unit):
        raise Unimplemented()

    @raise_null_argument
    def convert_spatial_units(self, source_spatial_unit_list):
        raise Unimplemented()


class FormatConversionSession(abc_locale_sessions.FormatConversionSession, osid_sessions.OsidSession):
    """Adapts underlying FormatConversionSession methodswith authorization checks."""

    def get_source_format_type(self):
        raise Unimplemented()

    source_format_type = property(fget=get_source_format_type)

    def get_target_format_type(self):
        raise Unimplemented()

    target_format_type = property(fget=get_target_format_type)

    def can_convert_formats(self):
        raise Unimplemented()

    @raise_null_argument
    def convert_format(self, source_text):
        raise Unimplemented()

    @raise_null_argument
    def convert_formats(self, source_texts):
        raise Unimplemented()


class CalendarInfoSession(abc_locale_sessions.CalendarInfoSession, osid_sessions.OsidSession):
    """Adapts underlying CalendarInfoSession methodswith authorization checks."""

    def get_calendar_type(self):
        raise Unimplemented()

    calendar_type = property(fget=get_calendar_type)

    def get_time_type(self):
        raise Unimplemented()

    time_type = property(fget=get_time_type)

    def can_examine_calendars(self):
        raise Unimplemented()

    def get_calendar_info(self):
        raise Unimplemented()

    calendar_info = property(fget=get_calendar_info)

    def get_time_info(self):
        raise Unimplemented()

    time_info = property(fget=get_time_info)
