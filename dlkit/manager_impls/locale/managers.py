"""Manager utility implementations of locale managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import NullArgument
from ..osid.osid_errors import Unimplemented
from ..type.objects import TypeList
from dlkit.abstract_osid.locale import managers as abc_locale_managers


class LocaleProfile(abc_locale_managers.LocaleProfile, osid_managers.OsidProfile):
    """The locale profile describes the interoperability of locale services."""

    def supports_visible_federation(self):
        """Tests if visible federation is supported.

        return: (boolean) - ``true`` if visible federation is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_translation(self):
        """Tests if translation is supported.

        return: (boolean) - ``true`` if translation is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_translation_admin(self):
        """Tests if translation administration is supported.

        return: (boolean) - ``true`` if translation administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_numeric_formatting(self):
        """Tests if numeric formatting is supported.

        return: (boolean) - ``true`` if numeric formatting is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_calendar_formatting(self):
        """Tests if calendar formatting is supported.

        return: (boolean) - ``true`` if calendar formatting is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_currency_formatting(self):
        """Tests if currency formatting is supported.

        return: (boolean) - ``true`` if currency formatting is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_coordinate_formatting(self):
        """Tests if coordinate formatting is supported.

        return: (boolean) - ``true`` if coordinate formatting is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_unit_conversion(self):
        """Tests if unit conversion is supported.

        return: (boolean) - ``true`` if unit conversion is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_currency_conversion(self):
        """Tests if currency conversion is supported.

        return: (boolean) - ``true`` if currency conversion is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_calendar_conversion(self):
        """Tests if calendar conversion is supported.

        return: (boolean) - ``true`` if calendar conversion is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_coordinate_conversion(self):
        """Tests if coordnate conversion is supported.

        return: (boolean) - ``true`` if coordinate conversion is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_spatial_unit_conversion(self):
        """Tests if spatial unit conversion is supported.

        return: (boolean) - ``true`` if spatial unit conversion is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_format_conversion(self):
        """Tests if format conversion is supported.

        return: (boolean) - ``true`` if format conversion is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_calendar_info(self):
        """Tests if a calendar informational service is supported.

        return: (boolean) - ``true`` if calendar info is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_language_types_for_translation(self, source_language_type=None, source_script_type=None, target_language_type=None, target_script_type=None):
        """Tests if a given language translation is supported.

        arg:    source_language_type (osid.type.Type): the type of the
                source language
        arg:    source_script_type (osid.type.Type): the type of the
                source script
        arg:    target_language_type (osid.type.Type): the type of the
                target language
        arg:    target_script_type (osid.type.Type): the type of the
                target script
        return: (boolean) - ``true`` if the given source and target
                translation is supported, ``false`` otherwise
        raise:  NullArgument - ``source_language_type,
                source_script_type, target_language_type`` or
                ``target_script_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_language_types_for_source(self, source_language_type=None, source_script_type=None):
        """Gets the list of target language types for a given source language type.

        arg:    source_language_type (osid.type.Type): the type of the
                source language
        arg:    source_script_type (osid.type.Type): the type of the
                source script
        return: (osid.type.TypeList) - the list of supported types for
                the given source language type
        raise:  NullArgument - ``source_language_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_language_types(self):
        """Gets all the source language types supported.

        return: (osid.type.TypeList) - the list of supported language
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_language_types = property(fget=get_source_language_types)

    def get_script_types_for_language_type(self, language_type=None):
        """Gets the list of script types available for a given language type.

        arg:    language_type (osid.type.Type): the type of the language
        return: (osid.type.TypeList) - the list of supported script
                types for the given language type
        raise:  NullArgument - ``language_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def supports_numeric_format_types(self, numeric_format_type=None):
        """Tests if a given numeric format type is supported.

        arg:    numeric_format_type (osid.type.Type): the type of the
                numeric format
        return: (boolean) - ``true`` if the given numeric format type is
                supported, ``false`` otherwise
        raise:  NullArgument - ``numeric_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_numeric_format_types(self):
        """Gets all the numeric format types supported.

        return: (osid.type.TypeList) - the list of supported numeric
                format types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    numeric_format_types = property(fget=get_numeric_format_types)

    def supports_calendar_types_for_formatting(self, calendar_type=None, time_type=None, date_format_type=None, time_format_type=None):
        """Tests if a given calendaring formatting is supported.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        arg:    time_type (osid.type.Type): the type of the time system
        arg:    date_format_type (osid.type.Type): the type of the
                output date format
        arg:    time_format_type (osid.type.Type): the type of the
                output time format
        return: (boolean) - ``true`` if formatting with the given types
                is supported, ``false`` otherwise
        raise:  NullArgument - ``calendar_type, calendar_format_type,
                time_type,`` or ``time_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_calendar_types_for_formatting(self):
        """Gets all the calendar types for which formats are available.

        return: (osid.type.TypeList) - the list of calendar types
        *compliance: mandatory -- This method must be implemented.*

        """

    calendar_types_for_formatting = property(fget=get_calendar_types_for_formatting)

    def get_date_format_types_for_calendar_type(self, calendar_type=None):
        """Gets the list of date format types for a given calendar type.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        return: (osid.type.TypeList) - the list of supported date format
                types
        raise:  NullArgument - ``calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_time_types_for_formatting(self):
        """Gets all the time types for which formatting is available.

        return: (osid.type.TypeList) - the list of time types
        *compliance: mandatory -- This method must be implemented.*

        """

    time_types_for_formatting = property(fget=get_time_types_for_formatting)

    def get_time_format_types_for_time_type(self, time_type=None):
        """Gets the list of time format types for a given time type.

        arg:    time_type (osid.type.Type): the type of the time
        return: (osid.type.TypeList) - the list of supported time format
                types
        raise:  NullArgument - ``time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def supports_currency_types_for_formatting(self, currency_type=None, numeric_format_type=None):
        """Tests if a given currency formatting is supported.

        arg:    currency_type (osid.type.Type): the type of the currency
        arg:    numeric_format_type (osid.type.Type): the type of the
                output currency format
        return: (boolean) - ``true`` if formatting with the given types
                is supported, ``false`` otherwise
        raise:  NullArgument - ``currency_type`` or
                ``numeric_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_currency_types_for_formatting(self):
        """Gets all the currency types for which formatting is available.

        return: (osid.type.TypeList) - the list of currency types
        *compliance: mandatory -- This method must be implemented.*

        """

    currency_types_for_formatting = property(fget=get_currency_types_for_formatting)

    def get_currency_format_types_for_currency_type(self, currency_type=None):
        """Gets the list of currency format types for a given currency type.

        arg:    currency_type (osid.type.Type): the type of the currency
        return: (osid.type.TypeList) - the list of supported currency
                format types
        raise:  NullArgument - ``currency_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def supports_coordinate_types_for_formatting(self, coordinate_type=None, coordinate_format_type=None):
        """Tests if a given coordinate formatting is supported.

        arg:    coordinate_type (osid.type.Type): the type of the
                coordinate
        arg:    coordinate_format_type (osid.type.Type): the type of the
                output coordinate format
        return: (boolean) - ``true`` if formatting with the given types
                is supported, ``false`` otherwise
        raise:  NullArgument - ``cooridinate_type`` or
                ``coodinate_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_coordinate_types_for_formatting(self):
        """Gets all the coordinate types for which formatting is available.

        return: (osid.type.TypeList) - the list of coordinate types
        *compliance: mandatory -- This method must be implemented.*

        """

    coordinate_types_for_formatting = property(fget=get_coordinate_types_for_formatting)

    def get_coordinate_format_types_for_coordinate_type(self, coordinate_type=None):
        """Gets the list of coordinate format types for a given coordinate type.

        arg:    coordinate_type (osid.type.Type): the type of the
                coordinate
        return: (osid.type.TypeList) - the list of supported coordinate
                format types
        raise:  NullArgument - ``coordinater_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def supports_unit_types_for_conversion(self, source_unit_type=None, target_unit_type=None):
        """Tests if a given measure conversion is supported.

        arg:    source_unit_type (osid.type.Type): the type of the
                source measure
        arg:    target_unit_type (osid.type.Type): the type of the
                target measure
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_unit_type`` or
                ``target_unit_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_unit_types_for_source(self, source_unit_type=None):
        """Gets the list of target measure types for a given source measure type.

        arg:    source_unit_type (osid.type.Type): the type of the
                source measure
        return: (osid.type.TypeList) - the list of supported target
                measure types
        raise:  NullArgument - ``source_unit_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_unit_types(self):
        """Gets all the source unit types supported.

        return: (osid.type.TypeList) - the list of supported source unit
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_unit_types = property(fget=get_source_unit_types)

    def supports_currency_types_for_conversion(self, source_currency_type=None, target_currency_type=None):
        """Tests if a given currency conversion is supported.

        arg:    source_currency_type (osid.type.Type): the type of the
                source currency
        arg:    target_currency_type (osid.type.Type): the type of the
                target currency
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_currency_type`` or
                ``target_currency_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_currency_types_for_source(self, source_currency_type=None):
        """Gets the list of target currency types for a given source currency type.

        arg:    source_currency_type (osid.type.Type): the type of the
                source currency
        return: (osid.type.TypeList) - the list of supported currency
                types
        raise:  NullArgument - ``source_currency_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_currency_types(self):
        """Gets the list of source currency types.

        return: (osid.type.TypeList) - the list of supported source
                currency types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_currency_types = property(fget=get_source_currency_types)

    def supports_calendar_types_for_conversion(self, source_calendar_type=None, target_calendar_type=None):
        """Tests if a given calendar conversion is supported.

        arg:    source_calendar_type (osid.type.Type): the type of the
                source calendar
        arg:    target_calendar_type (osid.type.Type): the type of the
                target calendar
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_calendar_type`` or
                ``target_calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_calendar_types_for_source(self, source_calendar_type=None):
        """Gets the list of target calendar types for a given source calendar type.

        arg:    source_calendar_type (osid.type.Type): the type of the
                source calendar
        return: (osid.type.TypeList) - the list of supported calendar
                types
        raise:  NullArgument - ``source_calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_calendar_types(self):
        """Gets the list of source calendar types.

        return: (osid.type.TypeList) - the list of supported source
                calendar types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_calendar_types = property(fget=get_source_calendar_types)

    def supports_time_types_for_conversion(self, source_time_type=None, target_time_type=None):
        """Tests if a given time conversion is supported.

        arg:    source_time_type (osid.type.Type): the type of the
                source time
        arg:    target_time_type (osid.type.Type): the type of the
                target time
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_time_type`` or
                ``target_time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_time_types_for_source(self, source_time_type=None):
        """Gets the list of target time types for a given source time type.

        arg:    source_time_type (osid.type.Type): the type of the
                source time
        return: (osid.type.TypeList) - the list of supported time types
        raise:  NullArgument - ``source_time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_time_types(self):
        """Gets the list of source time types.

        return: (osid.type.TypeList) - the list of supported source time
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_time_types = property(fget=get_source_time_types)

    def get_time_types_for_calendar_type(self, calendar_type=None):
        """Gets the list of time types supported for a given calendar type where they are both used in a ``DateTime``.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        return: (osid.type.TypeList) - the list of supported time types
        raise:  NullArgument - ``calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_calendar_types_for_time_type(self, time_type=None):
        """Gets the list of calendar types supported for a given time type where they are both used in a ``DateTime``.

        arg:    time_type (osid.type.Type): the type of the time system
        return: (osid.type.TypeList) - the list of supported calendar
                types
        raise:  NullArgument - ``time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def supports_calendar_time_types(self, calendar_type=None, time_type=None):
        """Tests if a given calendar and time type are used together in a ``DateTime``.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        arg:    time_type (osid.type.Type): the type of the time system
        return: (boolean) - ``true`` if the given calendar and time
                types are supported, ``false`` otherwise
        raise:  NullArgument - ``calendar_type`` or ``time_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def supports_coordinate_types_for_conversion(self, source_coordinate_type=None, target_coordinate_type=None):
        """Tests if a given coordinate type for conversion is supported.

        arg:    source_coordinate_type (osid.type.Type): the type of the
                source coordinate
        arg:    target_coordinate_type (osid.type.Type): the type of the
                target coordinate
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_coordinate_type`` or
                ``target_coordinate_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_coordinate_types_for_source(self, source_coordinate_type=None):
        """Gets the list of target coordinate types for a given source coordinate type.

        arg:    source_coordinate_type (osid.type.Type): the type of the
                source coordinate
        return: (osid.type.TypeList) - the list of supported target
                coordinate types
        raise:  NullArgument - ``source_coordinate_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_coordinate_types(self):
        """Gets the list of source coordinate types.

        return: (osid.type.TypeList) - the list of supported source
                coordinate types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_coordinate_types = property(fget=get_source_coordinate_types)

    def supports_spatial_unit_record_types_for_conversion(self, source_spatial_unit_record_type=None, target_spatial_unit_record_type=None):
        """Tests if a given spatial unit conversion is supported.

        arg:    source_spatial_unit_record_type (osid.type.Type): the
                type of the source spatial unit record
        arg:    target_spatial_unit_record_type (osid.type.Type): the
                type of the target spatial unit record
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_spatial_unit_record_type`` or
                ``target_spatial_unit_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_spatial_unit_record_types_for_source(self, source_spatial_unit_record_type=None):
        """Gets the list of target spatial unit types for a given source spatial unit type.

        arg:    source_spatial_unit_record_type (osid.type.Type): the
                type of the source spatial unit record
        return: (osid.type.TypeList) - the list of supported target
                spatial unit record types
        raise:  NullArgument - ``source_spatial_unit_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_spatial_unit_record_types(self):
        """Gets the list of source spatial unit record types.

        return: (osid.type.TypeList) - the list of supported source
                spatial unit record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_spatial_unit_record_types = property(fget=get_source_spatial_unit_record_types)

    def supports_format_types_for_conversion(self, source_format_type=None, target_format_type=None):
        """Tests if a given format conversion is supported.

        arg:    source_format_type (osid.type.Type): the type of the
                source format
        arg:    target_format_type (osid.type.Type): the type of the
                target format
        return: (boolean) - ``true`` if the given source and target
                conversion is supported, ``false`` otherwise
        raise:  NullArgument - ``source_format_type`` or
                ``target_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_format_types_for_source(self, source_format_type=None):
        """Gets the list of target format types for a given source spatial unit type.

        arg:    source_format_type (osid.type.Type): the type of the
                source format
        return: (osid.type.TypeList) - the list of supported target
                format types
        raise:  NullArgument - ``source_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """

    def get_source_format_types(self):
        """Gets the list of source format types.

        return: (osid.type.TypeList) - the list of supported source
                format types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    source_format_types = property(fget=get_source_format_types)


class LocaleManager(abc_locale_managers.LocaleManager, osid_managers.OsidManager, LocaleProfile):
    """The locale manager provides access to locale sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``TranslationSession:`` a session translate strings
      * ``TranslationAdminSession: a`` session to update the string
        translations for a locale
      * ``NumericFormattingSession:`` a session for formatting and
        parsing numbers
      * ``CalendarFormattingSession:`` a session for formatting and
        parsing dates and times
      * ``CurrencyFormattingSession`` : a session for formatting and
        parsing currency amounts
      * ``CoordinateFormattingSession:`` a session for formatting and
        parsing coordinates
      * ``UnitConversionSession:`` a session to convert measurement
        units ``None``
      * ``CurrencyConversionSession:`` a session to convert currency
      * ``CalendarConversionSession:`` a session to convert dates across
        calendars
      * ``CoordinateConversionSession:`` a session to convert coordinate
        systems
      * ``SpatialUnitConversionSession:`` a session to convert spatial
        units
      * ``FormatConversionSession:`` a session to convert text formats
      * ``CalendarInfoSession:`` a session for examining calendaring and
        time systems

    """

    def get_translation_session(self):
        """Gets an ``OsidSession`` associated with the language translation service.

        return: (osid.locale.TranslationSession) - a
                ``TranslationSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation()`` is ``true``.*

        """
        raise Unimplemented()

    translation_session = property(fget=get_translation_session)

    def get_translation_session_for_type(self, source_language_type=None, source_script_type=None, target_language_type=None, target_script_type=None):
        """Gets an ``OsidSession`` associated with the language translation service and the given language and script types.

        arg:    source_language_type (osid.type.Type): the type of the
                source language
        arg:    source_script_type (osid.type.Type): the type of the
                source script
        arg:    target_language_type (osid.type.Type): the type of the
                target language
        arg:    target_script_type (osid.type.Type): the type of the
                target script
        return: (osid.locale.TranslationSession) - a
                ``TranslationSession``
        raise:  NullArgument - ``source_language_type,
                source_script_type, target_language_type`` or
                ``target_script_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_language_types_for_translation(source_languag
                e_type, source_script_type, target_language_type,
                target_script_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation()`` and ``supports_visible_federation()``
        are ``true``.*

        """

    def get_translation_admin_session(self):
        """Gets a language translation administration service for updating a locale dictionary.

        return: (osid.locale.TranslationAdminSession) - a
                ``TranslationAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation_admin()`` is ``true``.*

        """
        raise Unimplemented()

    translation_admin_session = property(fget=get_translation_admin_session)

    def get_translation_admin_session_for_type(self, source_language_type=None, source_script_type=None, target_language_type=None, target_script_type=None):
        """Gets a language trabslation administration service for updating a locale dictionary using the given language and script types.

        arg:    source_language_type (osid.type.Type): the type of the
                source language
        arg:    source_script_type (osid.type.Type): the type of the
                source script
        arg:    target_language_type (osid.type.Type): the type of the
                target language
        arg:    target_script_type (osid.type.Type): the type of the
                target script
        return: (osid.locale.TranslationAdminSession) - a
                ``TranslationAdminSession``
        raise:  NullArgument - ``source_language_type,
                source_script_type, target_language_type`` or
                ``target_script_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation_admin()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_language_types_for_translation(source_languag
                e_type, source_script_type, target_language_type,
                target_script_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_numeric_formatting_session(self):
        """Gets an ``OsidSession`` associated with the numeric formatting service.

        return: (osid.locale.NumericFormattingSession) - a
                ``NumericFormattingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_numeric_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_numeric_formatting()`` is ``true``.*

        """
        raise Unimplemented()

    numeric_formatting_session = property(fget=get_numeric_formatting_session)

    def get_numeric_formatting_session_for_type(self, numeric_format_type=None):
        """Gets an ``OsidSession`` associated with the numeric formatting service and the given numeric format type.

        arg:    numeric_format_type (osid.type.Type): the type of the
                numeric format
        return: (osid.locale.NumericFormattingSession) - a
                ``NumericFormattingSession``
        raise:  NullArgument - ``numeric_format_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_numeric_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_numeric_format_type(numeric_format_type)`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_numeric_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_calendar_formatting_session(self):
        """Gets an ``OsidSession`` associated with the calendar formatting service.

        return: (osid.locale.CalendarFormattingSession) - a
                ``CalendarFormattingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_formatting()`` is ``true``.*

        """
        raise Unimplemented()

    calendar_formatting_session = property(fget=get_calendar_formatting_session)

    def get_calendar_formatting_session_for_type(self, calendar_type=None, calendar_format_type=None, time_type=None, time_format_type=None):
        """Gets an ``OsidSession`` associated with the calendar formatting service and the given calendar and time types.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        arg:    calendar_format_type (osid.type.Type): the type of the
                calendar format
        arg:    time_type (osid.type.Type): the type of the time system
        arg:    time_format_type (osid.type.Type): the type of the time
                format
        return: (osid.locale.CalendarFormattingSession) - a
                ``CalendarFormattingSession``
        raise:  NullArgument - ``calendar_type, calendar_format_type,
                time_type`` or ``time_format_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_calendar_types_for_formattinge(calendar_type,
                calendar_format_type, time_type, time_format_type)`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_currency_formatting_session(self):
        """Gets an ``OsidSession`` associated with the currency formatting service.

        return: (osid.locale.CurrencyFormattingSession) - a
                ``CurrencyFormattingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_formatting()`` is ``true``.*

        """
        raise Unimplemented()

    currency_formatting_session = property(fget=get_currency_formatting_session)

    def get_currency_formatting_session_for_type(self, currency_type=None, numeric_format_type=None):
        """Gets an ``OsidSession`` associated with the currency formatting service and the given currency and numeric format types.

        arg:    currency_type (osid.type.Type): the type of the currency
        arg:    numeric_format_type (osid.type.Type): the type of the
                numeric format
        return: (osid.locale.CurrencyFormattingSession) - a
                ``CurrencyFormattingSession``
        raise:  NullArgument - ``currency_type`` or
                ``numeric_format_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_currency_types_for_fomatting(currency_type,
                numeric_format_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_coordinate_formatting_session(self):
        """Gets an ``OsidSession`` associated with the coordinate formatting service.

        return: (osid.locale.CoordinateFormattingSession) - a
                ``CoordinateFormattingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_formatting()`` is ``true``.*

        """
        raise Unimplemented()

    coordinate_formatting_session = property(fget=get_coordinate_formatting_session)

    def get_coordinate_formatting_session_for_type(self, coordinate_type=None, coordinate_format_type=None):
        """Gets an ``OsidSession`` associated with the coordinate formatting service and the given coordinate and format types.

        arg:    coordinate_type (osid.type.Type): the type of the
                coordinate
        arg:    coordinate_format_type (osid.type.Type): the type of the
                coordinate format
        return: (osid.locale.CoordinateFormattingSession) - a
                ``CoordinateFormattingSession``
        raise:  NullArgument - ``coordinate_type`` or
                ``coordinate_format_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_coordinate_types_for_fomatting(coordinate_typ
                e, coordinate_format_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_unit_conversion_session(self):
        """Gets a unit conversion session.

        return: (osid.locale.UnitConversionSession) - a
                ``UnitConversionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_unit_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_unit_conversion()`` is ``true``.*

        """
        raise Unimplemented()

    unit_conversion_session = property(fget=get_unit_conversion_session)

    def get_currency_conversion_session(self):
        """Gets a currency conversion session.

        return: (osid.locale.CurrencyConversionSession) - a
                ``CurrencyConversionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_conversion()`` is ``true``.*

        """
        raise Unimplemented()

    currency_conversion_session = property(fget=get_currency_conversion_session)

    def get_currency_conversion_session_for_type(self, source_currency_type=None, target_currency_type=None):
        """Gets an ``OsidSession`` associated with the currency conversion service and the given currency types.

        arg:    source_currency_type (osid.type.Type): the type of the
                source currency
        arg:    target_currency_type (osid.type.Type): the type of the
                target currency
        return: (osid.locale.CurrencyConversionSession) - a
                ``CurrencyConversionSession``
        raise:  NullArgument - ``source_currency_type`` or
                ``target_currency_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_currency_types_for_conversion(source_currency
                _type, target_currency_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_calendar_conversion_session(self):
        """Gets a calendar conversion session.

        return: (osid.locale.CalendarConversionSession) - a
                ``CalendarConversionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_conversion()`` is ``true``.*

        """
        raise Unimplemented()

    calendar_conversion_session = property(fget=get_calendar_conversion_session)

    def get_calendar_conversion_session_for_type(self, source_calendar_type=None, source_time_type=None, target_calendar_type=None, target_time_type=None):
        """Gets an ``OsidSession`` associated with the calendar conversion service and the given calendar types.

        arg:    source_calendar_type (osid.type.Type): the type of the
                source calendar
        arg:    source_time_type (osid.type.Type): the type of the
                source time
        arg:    target_calendar_type (osid.type.Type): the type of the
                target calendar
        arg:    target_time_type (osid.type.Type): the type of the
                target time
        return: (osid.locale.CalendarConversionSession) - a
                ``CalendarConversionSession``
        raise:  NullArgument - ``source_calendar_type,
                source_time_type,``  ``target_calendar_type`` or
                ``target_time_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_calendar_types_for_conversion(source_calendar
                _type, target_calendar_type)`` or
                ``supports_time_types_for_conversion(source_time_type,
                target_time_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_coordinate_conversion_session(self):
        """Gets a coordinate conversion session.

        return: (osid.locale.CoordinateConversionSession) - a
                ``CoordinateConversionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_conversion()`` is ``true``.*

        """
        raise Unimplemented()

    coordinate_conversion_session = property(fget=get_coordinate_conversion_session)

    def get_coordinate_conversion_session_for_type(self, source_coordinate_type=None, target_coordinate_type=None):
        """Gets an ``OsidSession`` associated with the coordinate conversion service and the given coordinate types.

        arg:    source_coordinate_type (osid.type.Type): the type of the
                source coordinate
        arg:    target_coordinate_type (osid.type.Type): the type of the
                target coordinate
        return: (osid.locale.CoordinateConversionSession) - a
                ``CoordinateConversionSession``
        raise:  NullArgument - ``source_coordinate_type`` or
                ``target_coordinate_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported - ``supports_coordinate_record_types_for_con
                version(source_coordinate_type ,
                target_coordinate_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_spatial_unit_conversion_session(self):
        """Gets a spatial unit conversion session.

        return: (osid.locale.SpatialUnitConversionSession) - a
                ``SpatialUnitConversionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_spatial_unit_conversion()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_spatial_unit_conversion()`` is ``true``.*

        """
        raise Unimplemented()

    spatial_unit_conversion_session = property(fget=get_spatial_unit_conversion_session)

    def get_spatial_unit_conversion_session_for_type(self, source_spatial_unit_record_type=None, target_spatial_unit_record_type=None):
        """Gets an ``OsidSession`` associated with the spatial unit conversion service and the given spatial unit record types.

        arg:    source_spatial_unit_record_type (osid.type.Type): the
                type of the source spatial unit record
        arg:    target_spatial_unit_record_type (osid.type.Type): the
                type of the target spatial unit record
        return: (osid.locale.SpatialUnitConversionSession) - a
                ``SpatialUnitConversionSession``
        raise:  NullArgument - ``source_spatial_unit_record_type`` or
                ``target_spatial_unit_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_spatial_unit_conversion()``
                or ``supports_visible_federation()`` is ``false``
        raise:  Unsupported - ``supports_spatial_unit_record_types_for_c
                onversion(source_spatial_unit_ record_type,
                target_spatial_unit_record_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_spatial_unit_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_format_conversion_session(self):
        """Gets a text format conversion session.

        return: (osid.locale.FormatConversionSession) - a
                ``FormatConversionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_format_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_format_conversion()`` is ``true``.*

        """
        raise Unimplemented()

    format_conversion_session = property(fget=get_format_conversion_session)

    def get_format_conversion_session_for_type(self, source_format_type=None, target_format_type=None):
        """Gets an ``OsidSession`` associated with the text format conversion service and the given format types.

        arg:    source_format_type (osid.type.Type): the type of the
                text format
        arg:    target_format_type (osid.type.Type): the type of the
                text format
        return: (osid.locale.FormatConversionSession) - a
                ``FormatConversionSession``
        raise:  NullArgument - ``source_format_type`` or
                ``target_format_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_format_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_format_types_for_conversion(source_format_typ
                e, target_format_record_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_format_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_calendar_info_session(self):
        """Gets a calendar informational session session.

        return: (osid.locale.CalendarInfoSession) - a
                ``CalendarInfoSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_info()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_info()`` is ``true``.*

        """
        raise Unimplemented()

    calendar_info_session = property(fget=get_calendar_info_session)

    def get_calendar_info_session_for_type(self, calendar_type=None, time_type=None):
        """Gets an ``OsidSession`` associated with the calendar informational service and the given calendar and time types.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        arg:    time_type (osid.type.Type): the type of the time system
        return: (osid.locale.CalendarInfoSession) - a
                ``CalendarInfoSession``
        raise:  NullArgument - ``calendar_type`` or ``time_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_type()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_calendar_time_types(calendar_type,
                time_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_info()`` and
        ``supports_visible_federation()`` are ``true``.*

        """


class LocaleProxyManager(abc_locale_managers.LocaleProxyManager, osid_managers.OsidProxyManager, LocaleProfile):
    """The locale manager provides access to locale sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for
    passing information from server environments. The sessions included
    in this manager are:

      * ``TranslationSession:`` a session translate strings
      * ``TranslationAdminSession: a`` session to update the string
        translations for a locale
      * ``NumericFormattingSession:`` a session for formatting and
        parsing numbers
      * ``CalendarFormattingSession:`` a session for formatting and
        parsing dates and times
      * ``CurrencyFormattingSession`` : a session for formatting and
        parsing currency amounts
      * ``CoordinateFormattingSession:`` a session for formatting and
        parsing coordinates
      * ``UnitConversionSession:`` a session to convert measurement
        units ``None``
      * ``CurrencyConversionSession:`` a session to convert currency
      * ``CalendarConversionSession:`` a session to convert dates across
        calendars
      * ``CoordinateConversionSession:`` a session to convert coordinate
        systems
      * ``SpatialUnitConversionSession:`` a session to convert spatial
        units
      * ``FormatConversionSession:`` a session to convert text formats
      * ``CalendarInfoSession:`` a session for examining calendaring and
        time systems

    """

    def get_translation_session(self, proxy=None):
        """Gets an ``OsidSession`` associated with the language translation service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.TranslationSession) - a
                ``TranslationSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_translation_session_for_type(self, source_language_type=None, source_script_type=None, target_language_type=None, target_script_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the language translation service and the given language and script types.

        arg:    source_language_type (osid.type.Type): the type of the
                source language
        arg:    source_script_type (osid.type.Type): the type of the
                source script
        arg:    target_language_type (osid.type.Type): the type of the
                target language
        arg:    target_script_type (osid.type.Type): the type of the
                target script
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.TranslationSession) - a
                ``TranslationSession``
        raise:  NullArgument - ``source_language_type,
                source_script_type, target_language_type,
                target_script_type`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_language_types_for_translation(source_languag
                e_type, source_script_type, target_language_type,
                target_script_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation()`` and ``supports_visible_federation()``
        are ``true``.*

        """

    def get_translation_admin_session(self, proxy=None):
        """Gets a language translation administration service for updating a locale dictionary.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.TranslationAdminSession) - a
                ``TranslationAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_translation_admin_session_for_type(self, source_language_type=None, source_script_type=None, target_language_type=None, target_script_type=None, proxy=None):
        """Gets a language trabslation administration service for updating a locale dictionary using the given language and script types.

        arg:    source_language_type (osid.type.Type): the type of the
                source language
        arg:    source_script_type (osid.type.Type): the type of the
                source script
        arg:    target_language_type (osid.type.Type): the type of the
                target language
        arg:    target_script_type (osid.type.Type): the type of the
                target script
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.TranslationAdminSession) - a
                ``TranslationAdminSession``
        raise:  NullArgument - ``source_language_type,
                source_script_type, target_language_type,
                target_script_type`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_translation_admin()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_language_types_for_translation(source_languag
                e_type, source_script_type, target_language_type,
                target_script_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_translation_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_numeric_formatting_session(self, proxy=None):
        """Gets an ``OsidSession`` associated with the numeric formatting service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.NumericFormattingSession) - a
                ``NumericFormattingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_numeric_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_numeric_formatting()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_numeric_formatting_session_for_type(self, numeric_format_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the numeric formatting service and the given numeric format type.

        arg:    numeric_format_type (osid.type.Type): the type of the
                numeric format
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.NumericFormattingSession) - a
                ``NumericFormattingSession``
        raise:  NullArgument - ``numeric_format_type`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_numeric_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_numeric_format_type(numeric_format_type)`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_numeric_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_calendar_formatting_session(self, proxy=None):
        """Gets an ``OsidSession`` associated with the calendar formatting service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CalendarFormattingSession) - a
                ``CalendarFormattingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_formatting()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_calendar_formatting_session_for_type(self, calendar_type=None, calendar_format_type=None, time_type=None, time_format_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the calendar formatting service and the given calendar and time types.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        arg:    calendar_format_type (osid.type.Type): the type of the
                calendar format
        arg:    time_type (osid.type.Type): the type of the time system
        arg:    time_format_type (osid.type.Type): the type of the time
                format
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CalendarFormattingSession) - a
                ``CalendarFormattingSession``
        raise:  NullArgument - ``calendar_type, calendar_format_type,
                time_typ, time_format_type`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_calendar_types_for_formattinge(calendar_type,
                calendar_format_type, time_type, time_format_type)`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_currency_formatting_session(self, proxy=None):
        """Gets an ``OsidSession`` associated with the currency formatting service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CurrencyFormattingSession) - a
                ``CurrencyFormattingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_formatting()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_currency_formatting_session_for_type(self, currency_type=None, numeric_format_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the currency formatting service and the given currency and numeric format types.

        arg:    currency_type (osid.type.Type): the type of the currency
        arg:    numeric_format_type (osid.type.Type): the type of the
                numeric format
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CurrencyFormattingSession) - a
                ``CurrencyFormattingSession``
        raise:  NullArgument - ``currency_type, numeric_format_type`` or
                ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_currency_types_for_fomatting(currency_type,
                numeric_format_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_coordinate_formatting_session(self, proxy=None):
        """Gets an ``OsidSession`` associated with the coordinate formatting service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CoordinateFormattingSession) - a
                ``CoordinateFormattingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_formatting()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_formatting()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_coordinate_formatting_session_for_type(self, coordinate_type=None, coordinate_format_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the coordinate formatting service and the given coordinate and format types.

        arg:    coordinate_type (osid.type.Type): the type of the
                coordinate
        arg:    coordinate_format_type (osid.type.Type): the type of the
                coordinate format
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CoordinateFormattingSession) - a
                ``CoordinateFormattingSession``
        raise:  NullArgument - ``coordinate_type,
                coordinate_format_type,`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_formatting()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_coordinate_types_for_fomatting(coordinate_typ
                e, coordinate_format_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_formatting()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_unit_conversion_session(self, proxy=None):
        """Gets a unit conversion session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.UnitConversionSession) - a
                ``UnitConversionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_unit_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_unit_conversion()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_currency_conversion_session(self, proxy=None):
        """Gets a currency conversion session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CurrencyConversionSession) - a
                ``CurrencyConversionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_conversion()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_currency_conversion_session_for_type(self, source_currency_type=None, target_currency_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the currency conversion service and the given currency types.

        arg:    source_currency_type (osid.type.Type): the type of the
                source currency
        arg:    target_currency_type (osid.type.Type): the type of the
                target currency
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CurrencyConversionSession) - a
                ``CurrencyConversionSession``
        raise:  NullArgument - ``source_currency_type,
                target_currency_type`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_currency_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_currency_types_for_conversion(source_currency
                _type, target_currency_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_currency_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_calendar_conversion_session(self, proxy=None):
        """Gets a calendar conversion session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CalendarConversionSession) - a
                ``CalendarConversionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_conversion()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_calendar_conversion_session_for_type(self, source_calendar_type=None, source_time_type=None, target_calendar_type=None, target_time_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the calendar conversion service and the given calendar types.

        arg:    source_calendar_type (osid.type.Type): the type of the
                source calendar
        arg:    source_time_type (osid.type.Type): the type of the
                source time
        arg:    target_calendar_type (osid.type.Type): the type of the
                target calendar
        arg:    target_time_type (osid.type.Type): the type of the
                target time
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CalendarConversionSession) - a
                ``CalendarConversionSession``
        raise:  NullArgument - ``source_calendar_type, source_time_type,
                target_calendar_type, target_time_type`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_calendar_types_for_conversion(source_calendar
                _type, target_calendar_type)`` or
                ``supports_time_types_for_conversion(source_time_type,
                target_time_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_coordinate_conversion_session(self, proxy=None):
        """Gets a coordinate conversion session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CoordinateConversionSession) - a
                ``CoordinateConversionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_conversion()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_coordinate_conversion_session_for_type(self, source_coordinate_type=None, target_coordinate_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the coordinate conversion service and the given coordinate types.

        arg:    source_coordinate_type (osid.type.Type): the type of the
                source coordinate
        arg:    target_coordinate_type (osid.type.Type): the type of the
                target coordinate
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CoordinateConversionSession) - a
                ``CoordinateConversionSession``
        raise:  NullArgument - ``source_coordinate_type,``
                ``target_coordinate_type,`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_coordinate_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported - ``supports_coordinate_record_types_for_con
                version(source_coordinate_type ,
                target_coordinate_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_coordinate_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_spatial_unit_conversion_session(self, proxy=None):
        """Gets a spatial unit conversion session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.SpatialUnitConversionSession) - a
                ``SpatialUnitConversionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_spatial_unit_conversion()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_spatial_unit_conversion()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_spatial_unit_conversion_session_for_type(self, source_spatial_unit_record_type=None, target_spatial_unit_record_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the spatial unit conversion service and the given spatial unit record types.

        arg:    source_spatial_unit_record_type (osid.type.Type): the
                type of the source spatial unit record
        arg:    target_spatial_unit_record_type (osid.type.Type): the
                type of the target spatial unit record
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.SpatialUnitConversionSession) - a
                ``SpatialUnitConversionSession``
        raise:  NullArgument - ``source_spatial_unit_record_type,``
                ``target_spatial_unit_record_type or`` proxy is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_spatial_unit_conversion()``
                or ``supports_visible_federation()`` is ``false``
        raise:  Unsupported - ``supports_spatial_unit_record_types_for_c
                onversion(source_spatial_unit_ record_type,
                target_spatial_unit_record_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_spatial_unit_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_format_conversion_session(self, proxy=None):
        """Gets a text format conversion session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.FormatConversionSession) - a
                ``FormatConversionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_format_conversion()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_format_conversion()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_format_conversion_session_for_type(self, source_format_type=None, target_format_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the text format conversion service and the given format types.

        arg:    source_format_type (osid.type.Type): the type of the
                text format
        arg:    target_format_type (osid.type.Type): the type of the
                text format
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.FormatConversionSession) - a
                ``FormatConversionSession``
        raise:  NullArgument - ``source_format_type,
                target_format_type`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_format_conversion()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_format_types_for_conversion(source_format_typ
                e, target_format_record_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_format_conversion()`` and
        ``supports_visible_federation()`` are ``true``.*

        """

    def get_calendar_info_session(self, proxy=None):
        """Gets a calendar informational session session.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CalendarInfoSession) - a
                ``CalendarInfoSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_info()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_info()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_calendar_info_session_for_type(self, calendar_type=None, time_type=None, proxy=None):
        """Gets an ``OsidSession`` associated with the calendar informational service and the given calendar and time types.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        arg:    time_type (osid.type.Type): the type of the time system
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.locale.CalendarInfoSession) - a
                ``CalendarInfoSession``
        raise:  NullArgument - ``calendar_type, time_type`` or ``proxy``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_calendar_type()`` or
                ``supports_visible_federation()`` is ``false``
        raise:  Unsupported -
                ``supports_calendar_time_types(calendar_type,
                time_type)`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_calendar_info()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
