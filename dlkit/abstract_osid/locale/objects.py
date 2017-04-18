"""Implementations of locale abstract base class objects."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class CalendarInfo:
    """This interface defines methods to examine a calendar.

    A calendar is organized into "years," "months," and "days." A
    calendar system may offer a diffreent designation for these
    divisions which may or may not vary in duration.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_calendar_type(self):
        """Gets the calendar type.

        :return: the calendar type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    @abc.abstractmethod
    def get_display_name(self):
        """Gets the display name for this calendar.

        :return: the display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    @abc.abstractmethod
    def get_description(self):
        """Gets a description of this calendar.

        :return: the description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    description = property(fget=get_description)

    @abc.abstractmethod
    def get_common_era_name(self):
        """Gets the string for the common era in which years are positive.

        :return: the common era label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    common_era_name = property(fget=get_common_era_name)

    @abc.abstractmethod
    def get_common_era_abbrev(self):
        """Gets the abbreviation for the common era in which years are positive.

        :return: the common era label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    common_era_abbrev = property(fget=get_common_era_abbrev)

    @abc.abstractmethod
    def get_before_common_era_name(self):
        """Gets the string for before the common era in which years are negative.

        :return: the before common era label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    before_common_era_name = property(fget=get_before_common_era_name)

    @abc.abstractmethod
    def get_before_common_era_abbrev(self):
        """Gets the abbreviation for before the common era in which years are negative.

        :return: the before common era label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    before_common_era_abbrev = property(fget=get_before_common_era_abbrev)

    @abc.abstractmethod
    def get_first_year_in_common_era(self):
        """Gets the year number for the first year.

        :return: the first year
        :rtype: ``integer``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    first_year_in_common_era = property(fget=get_first_year_in_common_era)

    @abc.abstractmethod
    def get_last_year_before_common_era(self):
        """Gets the year number for the year before the common era.

        :return: the last bce year
        :rtype: ``integer``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    last_year_before_common_era = property(fget=get_last_year_before_common_era)

    @abc.abstractmethod
    def get_year_name(self):
        """Gets the display name for a calendar "year.

        "

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    year_name = property(fget=get_year_name)

    @abc.abstractmethod
    def get_month_name(self):
        """Gets the display name for a calendar "month.

        "

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    month_name = property(fget=get_month_name)

    @abc.abstractmethod
    def has_variable_months(self):
        """Tests if this calendar has a variable number of months in a year.

        :return: ``true`` if the number of months varies, ``false`` if the number of months is constant
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_num_months(self):
        """Gets the number of months of the year.

        For a variable month calendar, the number of all defined months
        are returned. If there are no "months" in this calendar system
        then this value may be zero.

        :return: the number of months
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    num_months = property(fget=get_num_months)

    @abc.abstractmethod
    def get_num_months_for_year(self, year):
        """Gets the number of months in the given year.

        :param year: a year
        :type year: ``integer``
        :return: the number of months
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``year`` is greater than ``get_last_year_before_common_era()`` and less then ``get_first_year_in_common_era()``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def get_months(self):
        """Gets the months of the year in order of the calendar.

        For a variable month calendar, all defined months are returned.
        If there are no "months" in this calendar system then the list
        may be empty.

        :return: the months
        :rtype: ``osid.locale.CalendarUnit``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.CalendarUnit

    months = property(fget=get_months)

    @abc.abstractmethod
    def get_months_for_year(self, year):
        """Gets the months of the year in order of the calendar.

        :param year: a year
        :type year: ``integer``
        :return: the months
        :rtype: ``osid.locale.CalendarUnit``
        :raise: ``IllegalState`` -- ``year`` is greater than ``get_last_year_before_common_era()`` and less then ``get_first_year_in_common_era()``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.CalendarUnit

    @abc.abstractmethod
    def get_day_name(self):
        """Gets the display name for a calendar "day.

        "

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    day_name = property(fget=get_day_name)

    @abc.abstractmethod
    def has_variable_days(self):
        """Tests if this calendar has a variable number of days in a month.

        :return: ``true`` if the number of days per month varies, ``false`` if the number of days is constant
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_num_days(self):
        """Gets the number of days in a year.

        For a variable day calendar, the number of all defined days are
        returned. If there are no "days" in this calendar system then
        this value may be zero. If there are no "months" defined then
        the number of days is the number of days in a year.

        :return: the number of days
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    num_days = property(fget=get_num_days)

    @abc.abstractmethod
    def get_num_days_for_month(self, year, month):
        """Gets the number of days in the given month.

        :param year: a year
        :type year: ``integer``
        :param month: a ``DateTime`` month code
        :type month: ``cardinal``
        :return: the number of days
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``year`` is greater than ``get_last_year_before_common_era()`` and less then ``get_first_year_in_common_era()`` , or ``month`` is greater than ``get_months_for_year(year)``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def get_days(self):
        """Gets the days of the month in order of the calendar.

        For a variable day calendar, all defined days are returned. If
        there are no "days" in this time system then this value may be
        zero. If there are no "months" defined then the number of days
        applies to the entire year.

        :return: the days
        :rtype: ``osid.locale.CalendarUnit``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.CalendarUnit

    days = property(fget=get_days)

    @abc.abstractmethod
    def get_days_for_month(self, year, month):
        """Gets the days of the given month in order of the calendar.

        :param year: a year
        :type year: ``integer``
        :param month: a ``DateTime`` month code
        :type month: ``cardinal``
        :return: the days
        :rtype: ``osid.locale.CalendarUnit``
        :raise: ``IllegalState`` -- ``year`` is greater than ``get_last_year_before_common_era()`` and less then ``get_first_year_in_common_era()`` , or ``month`` is greater than or equal to than ``get_months_for_year(year)``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.CalendarUnit

    @abc.abstractmethod
    def get_first_day_of_year(self):
        """Gets the first day of the calendar year.

        :return: the first day of the year
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    first_day_of_year = property(fget=get_first_day_of_year)

    @abc.abstractmethod
    def get_end_of_days_name(self):
        """Gets the display name for the end of the calendar.

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    end_of_days_name = property(fget=get_end_of_days_name)

    @abc.abstractmethod
    def get_origin(self):
        """Gets the start of the "common era" for this calendar.

        :return: start of the calendar
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    origin = property(fget=get_origin)

    @abc.abstractmethod
    def get_end_of_days(self):
        """Gets the end of the world as specified by this calendar.

        :return: end of days
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    end_of_days = property(fget=get_end_of_days)

    @abc.abstractmethod
    def get_weekdays(self):
        """Gets the days of the week in order of the calendar.

        :return: the week days
        :rtype: ``osid.locale.CalendarUnit``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.CalendarUnit

    weekdays = property(fget=get_weekdays)


class TimeInfo:
    """This interface defines methods to examine a time.

    Time is organized intro "hours," "minutes," and "seconds." A time
    system may offer a different designation for these divisions which
    may or may not vary in duration.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_time_type(self):
        """Gets the time type.

        :return: the time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_type = property(fget=get_time_type)

    @abc.abstractmethod
    def get_display_name(self):
        """Gets the display name for this time system.

        :return: the display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    @abc.abstractmethod
    def get_display_label(self):
        """Gets a short label for this time system.

        :return: the label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    @abc.abstractmethod
    def get_description(self):
        """Gets a description of this time system.

        :return: the description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    description = property(fget=get_description)

    @abc.abstractmethod
    def get_hour_name(self):
        """Gets the display name for "hours.

        "

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    hour_name = property(fget=get_hour_name)

    @abc.abstractmethod
    def get_hour_abbrev(self):
        """Gets the abbreviation for "hours.

        "

        :return: the abbreviation
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    hour_abbrev = property(fget=get_hour_abbrev)

    @abc.abstractmethod
    def get_hour_initial(self):
        """Gets the initial for "hours.

        "

        :return: the initial
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    hour_initial = property(fget=get_hour_initial)

    @abc.abstractmethod
    def has_variable_hours(self):
        """Tests if this time system has a variable number of hours in a day.

        :return: ``true`` if the number of hours per day varies, ``false`` if the number of hours per day is constant
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_num_hours(self):
        """Gets the number of hours in a day.

        For a variable hour time system, the number of hours defined is
        returned. If there are no "hours" in this time system then this
        value may be zero.

        :return: the number of hours
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    num_hours = property(fget=get_num_hours)

    @abc.abstractmethod
    def get_num_hours_for_day(self, year, month, day):
        """Gets the number of hours for a given day.

        :param year: a year
        :type year: ``integer``
        :param month: a ``DateTime`` month code
        :type month: ``cardinal``
        :param day: a ``DateTime`` day code
        :type day: ``cardinal``
        :return: the number of hours
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``year`` is greater than ``CalendarInfo.getLastYearBeforeCommonEra()`` and less then ``CalendarInfo.getFirstYearInCommonEra()`` , or ``month`` is greater than or equal to
``CalendarInfo.getNumMonthsForYear(year)`` , or ``day`` is greater than or equal to ``CalendarInfo.getDaysInMonth(year, month)``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def get_minute_name(self):
        """Gets the display name for "minutes.

        "

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    minute_name = property(fget=get_minute_name)

    @abc.abstractmethod
    def get_minute_abbrev(self):
        """Gets the abbreviation for "minutes.

        "

        :return: the abbreviation
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    minute_abbrev = property(fget=get_minute_abbrev)

    @abc.abstractmethod
    def get_minute_initial(self):
        """Gets the initial for "minutes.

        "

        :return: the initial
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    minute_initial = property(fget=get_minute_initial)

    @abc.abstractmethod
    def has_variable_minutes(self):
        """Tests if this time system has a variable number of minutes in an hour.

        :return: ``true`` if the number of minutes per hour varies, ``false`` if the number of minutes per hour is constant
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_num_minutes(self):
        """Gets the number of minutes in an hour.

        For a variable minute time system, the number of minutes defined
        is returned. If there are no "minutes" in this time system then
        this value may be zero. If there are no "hours" defined then the
        number of minutes is the number of minutes in a day.

        :return: the number of minutes
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    num_minutes = property(fget=get_num_minutes)

    @abc.abstractmethod
    def get_num_minutes_for_hour(self, year, month, day, hour):
        """Gets the minutes for a given hour.

        :param year: a year
        :type year: ``integer``
        :param month: a ``DateTime`` month code
        :type month: ``cardinal``
        :param day: a ``DateTime`` day code
        :type day: ``cardinal``
        :param hour: an hour
        :type hour: ``cardinal``
        :return: the number of minutes
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``year`` is greater than ``CalendarInfo.getLastYearBeforeCommonEra()`` and less then ``CalendarInfo.getFirstYearInCommonEra(),`` or ``month`` is greater than or equal to
``CalendarInfo.getNumMonthsForYear(year)`` , or ``day`` is greater than or equal to ``CalendarInfo.getDaysInMonth(year, month)`` , or ``hour`` is greater than or equal to ``get_num_hours_in_day(year,
month, day)``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def get_second_name(self):
        """Gets the display name for "seconds.

        "

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    second_name = property(fget=get_second_name)

    @abc.abstractmethod
    def get_second_abbrev(self):
        """Gets the abbreviation for "seconds.

        "

        :return: the abbreviation
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    second_abbrev = property(fget=get_second_abbrev)

    @abc.abstractmethod
    def get_second_initial(self):
        """Gets the initial for "seconds.

        "

        :return: the initial
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    second_initial = property(fget=get_second_initial)

    @abc.abstractmethod
    def has_variable_seconds(self):
        """Tests if this time system has a variable number of seconds in a minute.

        :return: ``true`` if the number of seconds per minute varies, ``false`` if the number of seconds per minute is constant
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_num_seconds(self):
        """Gets the number of seconds in a minute.

        For a variable second time system, the number of seconds defined
        is returned. If there are no "seconds" in this time system then
        this value may be zero. If there are no "minutes" defined then
        the number of seconds is the number of seconds in an hour.

        :return: the number of seconds
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    num_seconds = property(fget=get_num_seconds)

    @abc.abstractmethod
    def get_num_seconds_for_minute(self, year, month, day, hour, minute):
        """Gets the seconds for a given minute.

        :param year: a year
        :type year: ``integer``
        :param month: a ``DateTime`` month code
        :type month: ``cardinal``
        :param day: a ``DateTime`` day code
        :type day: ``cardinal``
        :param hour: an hour
        :type hour: ``cardinal``
        :param minute: a minute
        :type minute: ``cardinal``
        :return: the number of seconds
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``year`` is greater than ``get_last_year_before_common_era()`` and less then ``get_first_year_in_common_era()`` , or ``month`` is greater than or equal to ``CalendarInfo.getNumMonthsForYear(year)`` ,
or ``day`` is greater than or equal to ``CalendarInfo.getDaysInMonth(year, month)`` , or ``hour`` is greater than or equal to ``get_num_hours_in_day(year, month, day)`` , or ``minute`` is greater than
or equal to ``get_num_minutes_inhour(year, month, day, hour)``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal


class CalendarUnit:
    """A description of a calendar unit."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_name(self):
        """Gets the full name of this unit.

        :return: the name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    name = property(fget=get_name)

    @abc.abstractmethod
    def get_abbrev3(self):
        """Gets a 3-letter abbreviation for this unit.

        :return: the abbreviation
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    abbrev3 = property(fget=get_abbrev3)

    @abc.abstractmethod
    def get_abbrev2(self):
        """Gets a 2-letter abbreviation for this unit.

        :return: the abbreviation
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    abbrev2 = property(fget=get_abbrev2)

    @abc.abstractmethod
    def get_initial(self):
        """Gets a single letter abbreviation for this unit.

        :return: the initial
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    initial = property(fget=get_initial)

    @abc.abstractmethod
    def get_date_time_code(self):
        """Gets the number of this unit used in ``DateTime``.

        :return: the code
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    date_time_code = property(fget=get_date_time_code)

    @abc.abstractmethod
    def get_description(self):
        """Gets a description of this unit.

        :return: the description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    description = property(fget=get_description)


class Locale:
    """A locale is a collection of types.

    ``Locale`` defines a set of types that together define the
    formatting, language, calendaring, and currency for a locale or
    culture.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_language_type(self):
        """Gets the language ``Type``.

        :return: the language type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    language_type = property(fget=get_language_type)

    @abc.abstractmethod
    def get_script_type(self):
        """Gets the script ``Type``.

        :return: the script type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    script_type = property(fget=get_script_type)

    @abc.abstractmethod
    def get_calendar_type(self):
        """Gets the calendar ``Type``.

        :return: the calendar type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    @abc.abstractmethod
    def get_time_type(self):
        """Gets the time ``Type``.

        :return: the time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_type = property(fget=get_time_type)

    @abc.abstractmethod
    def get_currency_type(self):
        """Gets the currency ``Type``.

        :return: the currency type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    currency_type = property(fget=get_currency_type)

    @abc.abstractmethod
    def get_unit_system_type(self):
        """Gets the unit system ``Type``.

        :return: the unit system type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    unit_system_type = property(fget=get_unit_system_type)

    @abc.abstractmethod
    def get_numeric_format_type(self):
        """Gets the numeric format ``Type``.

        :return: the numeric format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    numeric_format_type = property(fget=get_numeric_format_type)

    @abc.abstractmethod
    def get_calendar_format_type(self):
        """Gets the calendar format ``Type``.

        :return: the calendar format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    calendar_format_type = property(fget=get_calendar_format_type)

    @abc.abstractmethod
    def get_time_format_type(self):
        """Gets the time format ``Type``.

        :return: the time format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_format_type = property(fget=get_time_format_type)

    @abc.abstractmethod
    def get_currency_format_type(self):
        """Gets the currency format ``Type``.

        :return: the currency format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    currency_format_type = property(fget=get_currency_format_type)

    @abc.abstractmethod
    def get_coordinate_format_type(self):
        """Gets the coordinate format ``Type``.

        :return: the coordinate format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    coordinate_format_type = property(fget=get_coordinate_format_type)


class LocaleList:
    """Like all ``OsidLists,``  ``LocaleList`` provides a means for accessing ``Locale`` elements sequentially either one at a time or many at a time.

    Examples: while (ll.hasNext()) { Locale locale = ll.getNextLocale();
    }

    or
      while (ll.hasNext()) {
           Locale[] locales = ll.getNextLocales(ll.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_locale(self):
        """Gets the next ``Locale`` in this list.

        :return: the next ``Locale`` in this list. The ``has_next()`` method should be used to test that a next ``Locale`` is available before calling this method.
        :rtype: ``osid.locale.Locale``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.Locale

    next_locale = property(fget=get_next_locale)

    @abc.abstractmethod
    def get_next_locales(self, n):
        """Gets the next set of ``Locale`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Locale`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Locale`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.locale.Locale``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.Locale
