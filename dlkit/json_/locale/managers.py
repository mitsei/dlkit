"""JSON implementations of locale managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import profile
from . import sessions
from .. import utilities
from ..osid import managers as osid_managers
from ..primitives import Type
from ..type.objects import TypeList
from ..utilities import get_registry
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.locale import managers as locale_managers


class LocaleProfile(osid_managers.OsidProfile, locale_managers.LocaleProfile):
    """The locale profile describes the interoperability of locale services."""

    @utilities.arguments_not_none
    def get_language_types_for_source(self, source_language_type, source_script_type):
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
        raise errors.Unimplemented()

    def get_source_language_types(self):
        """Gets all the source language types supported.

        return: (osid.type.TypeList) - the list of supported language
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_language_types = property(fget=get_source_language_types)

    @utilities.arguments_not_none
    def get_script_types_for_language_type(self, language_type):
        """Gets the list of script types available for a given language type.

        arg:    language_type (osid.type.Type): the type of the language
        return: (osid.type.TypeList) - the list of supported script
                types for the given language type
        raise:  NullArgument - ``language_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_numeric_format_types(self):
        """Gets all the numeric format types supported.

        return: (osid.type.TypeList) - the list of supported numeric
                format types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    numeric_format_types = property(fget=get_numeric_format_types)

    def get_calendar_types_for_formatting(self):
        """Gets all the calendar types for which formats are available.

        return: (osid.type.TypeList) - the list of calendar types
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    calendar_types_for_formatting = property(fget=get_calendar_types_for_formatting)

    @utilities.arguments_not_none
    def get_date_format_types_for_calendar_type(self, calendar_type):
        """Gets the list of date format types for a given calendar type.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        return: (osid.type.TypeList) - the list of supported date format
                types
        raise:  NullArgument - ``calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_time_types_for_formatting(self):
        """Gets all the time types for which formatting is available.

        return: (osid.type.TypeList) - the list of time types
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    time_types_for_formatting = property(fget=get_time_types_for_formatting)

    @utilities.arguments_not_none
    def get_time_format_types_for_time_type(self, time_type):
        """Gets the list of time format types for a given time type.

        arg:    time_type (osid.type.Type): the type of the time
        return: (osid.type.TypeList) - the list of supported time format
                types
        raise:  NullArgument - ``time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_currency_types_for_formatting(self):
        """Gets all the currency types for which formatting is available.

        return: (osid.type.TypeList) - the list of currency types
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    currency_types_for_formatting = property(fget=get_currency_types_for_formatting)

    @utilities.arguments_not_none
    def get_currency_format_types_for_currency_type(self, currency_type):
        """Gets the list of currency format types for a given currency type.

        arg:    currency_type (osid.type.Type): the type of the currency
        return: (osid.type.TypeList) - the list of supported currency
                format types
        raise:  NullArgument - ``currency_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_coordinate_types_for_formatting(self):
        """Gets all the coordinate types for which formatting is available.

        return: (osid.type.TypeList) - the list of coordinate types
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    coordinate_types_for_formatting = property(fget=get_coordinate_types_for_formatting)

    @utilities.arguments_not_none
    def get_coordinate_format_types_for_coordinate_type(self, coordinate_type):
        """Gets the list of coordinate format types for a given coordinate type.

        arg:    coordinate_type (osid.type.Type): the type of the
                coordinate
        return: (osid.type.TypeList) - the list of supported coordinate
                format types
        raise:  NullArgument - ``coordinater_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_unit_types_for_source(self, source_unit_type):
        """Gets the list of target measure types for a given source measure type.

        arg:    source_unit_type (osid.type.Type): the type of the
                source measure
        return: (osid.type.TypeList) - the list of supported target
                measure types
        raise:  NullArgument - ``source_unit_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_unit_types(self):
        """Gets all the source unit types supported.

        return: (osid.type.TypeList) - the list of supported source unit
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_unit_types = property(fget=get_source_unit_types)

    @utilities.arguments_not_none
    def get_currency_types_for_source(self, source_currency_type):
        """Gets the list of target currency types for a given source currency type.

        arg:    source_currency_type (osid.type.Type): the type of the
                source currency
        return: (osid.type.TypeList) - the list of supported currency
                types
        raise:  NullArgument - ``source_currency_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_currency_types(self):
        """Gets the list of source currency types.

        return: (osid.type.TypeList) - the list of supported source
                currency types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_currency_types = property(fget=get_source_currency_types)

    @utilities.arguments_not_none
    def get_calendar_types_for_source(self, source_calendar_type):
        """Gets the list of target calendar types for a given source calendar type.

        arg:    source_calendar_type (osid.type.Type): the type of the
                source calendar
        return: (osid.type.TypeList) - the list of supported calendar
                types
        raise:  NullArgument - ``source_calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_calendar_types(self):
        """Gets the list of source calendar types.

        return: (osid.type.TypeList) - the list of supported source
                calendar types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_calendar_types = property(fget=get_source_calendar_types)

    @utilities.arguments_not_none
    def get_time_types_for_source(self, source_time_type):
        """Gets the list of target time types for a given source time type.

        arg:    source_time_type (osid.type.Type): the type of the
                source time
        return: (osid.type.TypeList) - the list of supported time types
        raise:  NullArgument - ``source_time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_time_types(self):
        """Gets the list of source time types.

        return: (osid.type.TypeList) - the list of supported source time
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_time_types = property(fget=get_source_time_types)

    @utilities.arguments_not_none
    def get_time_types_for_calendar_type(self, calendar_type):
        """Gets the list of time types supported for a given calendar type where they are both used in a ``DateTime``.

        arg:    calendar_type (osid.type.Type): the type of the calendar
        return: (osid.type.TypeList) - the list of supported time types
        raise:  NullArgument - ``calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_calendar_types_for_time_type(self, time_type):
        """Gets the list of calendar types supported for a given time type where they are both used in a ``DateTime``.

        arg:    time_type (osid.type.Type): the type of the time system
        return: (osid.type.TypeList) - the list of supported calendar
                types
        raise:  NullArgument - ``time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_coordinate_types_for_source(self, source_coordinate_type):
        """Gets the list of target coordinate types for a given source coordinate type.

        arg:    source_coordinate_type (osid.type.Type): the type of the
                source coordinate
        return: (osid.type.TypeList) - the list of supported target
                coordinate types
        raise:  NullArgument - ``source_coordinate_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_coordinate_types(self):
        """Gets the list of source coordinate types.

        return: (osid.type.TypeList) - the list of supported source
                coordinate types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_coordinate_types = property(fget=get_source_coordinate_types)

    @utilities.arguments_not_none
    def get_spatial_unit_record_types_for_source(self, source_spatial_unit_record_type):
        """Gets the list of target spatial unit types for a given source spatial unit type.

        arg:    source_spatial_unit_record_type (osid.type.Type): the
                type of the source spatial unit record
        return: (osid.type.TypeList) - the list of supported target
                spatial unit record types
        raise:  NullArgument - ``source_spatial_unit_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_spatial_unit_record_types(self):
        """Gets the list of source spatial unit record types.

        return: (osid.type.TypeList) - the list of supported source
                spatial unit record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('SOURCE_SPATIAL_UNIT_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    source_spatial_unit_record_types = property(fget=get_source_spatial_unit_record_types)

    @utilities.arguments_not_none
    def get_format_types_for_source(self, source_format_type):
        """Gets the list of target format types for a given source spatial unit type.

        arg:    source_format_type (osid.type.Type): the type of the
                source format
        return: (osid.type.TypeList) - the list of supported target
                format types
        raise:  NullArgument - ``source_format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_source_format_types(self):
        """Gets the list of source format types.

        return: (osid.type.TypeList) - the list of supported source
                format types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    source_format_types = property(fget=get_source_format_types)


class LocaleManager(osid_managers.OsidManager, LocaleProfile, locale_managers.LocaleManager):
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
    def __init__(self):
        osid_managers.OsidManager.__init__(self)


class LocaleProxyManager(osid_managers.OsidProxyManager, LocaleProfile, locale_managers.LocaleProxyManager):
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
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)
