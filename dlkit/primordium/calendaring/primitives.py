"""
Generic implementions of osid.calendaring primitives.

Can be used by implementations and consumer applications alike.

"""
# pylint: disable=too-many-public-methods
#    Number of public methods are defined in spec

import datetime
from dlkit.abstract_osid.calendaring import primitives as abc_calendaring_primitives
from dlkit.abstract_osid.osid.errors import Unimplemented
from ..osid.primitives import OsidPrimitive


class DateTime(datetime.datetime, abc_calendaring_primitives.DateTime, OsidPrimitive):
    """The DateTime interface defines a date and/or time.

    This interface provides a very broad range of dates, describes more
    or less precision, and/or conveys an uncertainty. A number of
    convenience methods for retrieving time elements are available but
    only those methods covered by the specified granularity are valid.

    A typical example is describing a day where the time isn't known,
    and the event did not occur at midnight.
      getMillennium() == 2
      getCentury() == 18
      getYear() == 1776
      getMonth() == 7
      getDay() == 4
      getHour() == 0
      getGranularity() == DateTimeResolution.DAY
      definesUncertainty() == false

    Another example showing that the time is probably 1pm but could have
    been as late as 3pm or early as noon.
      getMillennium() == 3
      getCentury() == 21
      getYear() == 2008
      getMonth() == 3
      getDay() == 17
      getHour() == 13
      getMinute() == 0
      getGranularity() == TimeResolution.MINUTE
      definesUncertainty() == true
      getUncertaintyGranularity() == DateTimeResolution.HOUR
      getUncertaintyMinus() == 1
      getUncertaintyPlus == 2



    An example marking the birth of the universe. 13.73 billion years
    +/- 120 million years. The granularity suggests that no more
    resolution than one million years can be inferred from the "clock",
    making errors in the exact number of millennia insignificant.
      getEpoch() == -13,730
      getMillennium() == 0
      getCentury() == 0
      getYear() == 0
      getGranularity() == TimeResolution.EPOCH
      definesUncertainty() == true
      getUncertaintyGranularity() == DateTimeResolution.EPOCH
      getUncertaintyMinus() == 120
      getUncertaintyPlus == 120



    """

    def get_calendar_type(self):
        """Gets the calendar type.

        return: (osid.type.Type) - the calendar type
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    calendar_type = property(fget=get_calendar_type)

    def get_aeon(self):
        """Gets the aeon starting from 1.

        An aeon is 1B years.

        return: (integer) - the aeon
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    aeon = property(fget=get_aeon)

    def get_epoch(self):
        """Gets the epoch starting from 1.

        An epoch is 1M years.

        return: (integer) - the eposh
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    epoch = property(fget=get_epoch)

    def get_millennium(self):
        """Gets the millennium starting from 1.

        A millenium is 1,000 years.

        return: (integer) - the millennium
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    millennium = property(fget=get_millennium)

    def get_century(self):
        """Gets the century starting from 1.

        return: (integer) - the century
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    century = property(fget=get_century)

    def get_year(self):
        """Gets the year starting from 1.

        return: (integer) - the year
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    year = property(fget=get_year)

    def get_month(self):
        """Gets the month number starting from 1.

        return: (cardinal) - the month
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    month = property(fget=get_month)

    def get_day(self):
        """Gets the day of the month starting from 1.

        return: (cardinal) - the day of the month
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    day = property(fget=get_day)

    def get_time_type(self):
        """Gets the time type.

        return: (osid.type.Type) - the time type
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    time_type = property(fget=get_time_type)

    def get_hour(self):
        """Gets the hour of the day 0-23.

        return: (cardinal) - the hour of the day
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    hour = property(fget=get_hour)

    def get_minute(self):
        """Gets the minute of the hour 0-59.

        return: (cardinal) - the minute of the hour
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    minute = property(fget=get_minute)

    def get_second(self):
        """Gets the second of the minute 0-59.

        return: (cardinal) - the second of the minute
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    second = property(fget=get_second)

    def get_milliseconds(self):
        """Gets the number of milliseconds in this second 0-999.

        A millisecond is one thousandth of a second.

        return: (cardinal) - the milliseconds of the second
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    milliseconds = property(fget=get_milliseconds)

    def get_microseconds(self):
        """Gets the number of microseconds of the second 0-999.

        A microsecond is one millionth of a second.

        return: (cardinal) - the micrseconds of the millisecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    microseconds = property(fget=get_microseconds)

    def get_nanoseconds(self):
        """Gets the number of nanoseconds of the microsecond 0-999.

        A nanosecond is one billionth of a second.

        return: (cardinal) - the nanoseconds of the microsecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    nanoseconds = property(fget=get_nanoseconds)

    def get_picoseconds(self):
        """Gets the number of picoseconds of the nanosecond 0-999.

        A picosecond is one trillionth of a second.

        return: (cardinal) - the picoseconds of the nanosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    picoseconds = property(fget=get_picoseconds)

    def get_femtoseconds(self):
        """Gets the number of femtoseconds of the picosecond 0-999.

        A femtosecond is one quadrillionth of a second.

        return: (cardinal) - the femtoseconds of the picosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    femtoseconds = property(fget=get_femtoseconds)

    def get_attoseconds(self):
        """Gets the number of attoseconds of the femtoseconds 0-999.

        An attosecond is one quintillionth of a second.

        return: (cardinal) - the attoseconds of the femtosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    attoseconds = property(fget=get_attoseconds)

    def get_zeptoseconds(self):
        """Gets the number of zeptoseconds of the attosecond 0-999.

        A zeptosecond is one sextillionth of a second.

        return: (cardinal) - the zeptoseconds of the attosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    zeptoseconds = property(fget=get_zeptoseconds)

    def get_yoctoseconds(self):
        """Gets the number of yoctoseconds of the picosecond 0-999.

        A yoctosecond is one septillionth of a second. This is getting
        quite small.

        return: (cardinal) - the yoctoseconds of the picosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    yoctoseconds = property(fget=get_yoctoseconds)

    def get_xoxxoseconds(self):
        """Gets the number of xoxxoseconds of the yoctosecond 0-999.

        A xoxxosecond is one octillionth of a second. We're going with
        Rudy Rucker here.

        return: (cardinal) - the xoxxoseconds of the yoctosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    xoxxoseconds = property(fget=get_xoxxoseconds)

    def get_weebleseconds(self):
        """Gets the number of weebleseconds of the xoxxosecond 0-999.

        A weeblesecond is one nonillionth of a second.

        return: (cardinal) - the weebleseconds of the xoxxoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    weebleseconds = property(fget=get_weebleseconds)

    def get_vatoseconds(self):
        """Gets the number of vatoseconds of the xoxxosecond 0-999.

        A vatosecond is one decillionth of a second.

        return: (cardinal) - the vatoseconds of the weeblesecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    vatoseconds = property(fget=get_vatoseconds)

    def get_undaseconds(self):
        """Gets the number of undaseconds of the vatosecond 0-999.

        An undasecond is one unadecillionth of a second.

        return: (cardinal) - the undaseconds of the vatosecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    undaseconds = property(fget=get_undaseconds)

    def get_planck_seconds(self):
        """Gets the number of Plancks of the vatoseconds.

        A Planck is 10 quattuordecillionths of a second.

        return: (cardinal) - the plancks of the undasecond
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    planck_seconds = property(fget=get_planck_seconds)

    def get_granularity(self):
        """Gets the granularity of this time.

        The granularity indicates the resolution of the clock. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        return: (osid.calendaring.DateTimeResolution) - granularity
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    granularity = property(fget=get_granularity)

    def get_granularity_multiplier(self):
        """If the granularity of the time equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        return: (cardinal) - granularity multiplier
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    granularity_multiplier = property(fget=get_granularity_multiplier)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this time.

        return: (boolean) - ``true`` if uncertainty is defined,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_uncertainty_units(self):
        """Gets the units of the uncertainty.

        return: (osid.calendaring.DateTimeResolution) - units of the
                uncertainty
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    uncertainty_units = property(fget=get_uncertainty_units)

    def get_uncertainty_minus(self):
        """Gets the uncertainty of this time in the negative direction.

        return: (cardinal) - the uncertainty under this value
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty of this time in the positive direction.

        return: (cardinal) - the uncertainty over this value
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    uncertainty_plus = property(fget=get_uncertainty_plus)

    def is_uncertainty_date_inclusive(self):
        """Tests if the uncertainty is inclusive of all dates.

        An inclusive uncertainty includes the entire range specified by
        the uncertainty units e.g. +/- 1 year includes all of the months
        and days within that interval. A non-inclusive uncertainty would
        mean the year is uncertain but the month and day is certain.

        return: (boolean) - ``true`` if the uncertainty includes all
                dates, ``false`` otherwise
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def is_uncertainty_time_inclusive(self):
        """Tests if the uncertainty is time inclusive.

        An inclusive uncertainty includes the entire range specified by
        the uncertainty units e.g. +/- 1 year includes all of the
        seconds within that interval. A non-inclusive uncertainty would
        mean the year is uncertain but the time is certain.

        return: (boolean) - ``true`` if the uncertainty includes all
                times, ``false`` otherwise
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()


class Duration(datetime.timedelta, abc_calendaring_primitives.Duration, OsidPrimitive):
    """The ``Duration`` a length of time."""

    def get_calendar_type(self):
        """Gets the calendar type.

        return: (osid.type.Type) - the calendar type
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    calendar_type = property(fget=get_calendar_type)

    def get_time_type(self):
        """Gets the time type.

        return: (osid.type.Type) - the time type
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    time_type = property(fget=get_time_type)

    def get_aeons(self):
        """Gets the number of aeons.

        An aeon is 1B years.

        return: (decimal) - the number of aeons
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    aeons = property(fget=get_aeons)

    def get_epochs(self):
        """Gets the number of epochs.

        An epoch is 1M years.

        return: (decimal) - the number of epochs
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    epochs = property(fget=get_epochs)

    def get_millennia(self):
        """Gets the number of millennia.

        A millennium is 1,000 years.

        return: (decimal) - the number of millennia
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    millennia = property(fget=get_millennia)

    def get_centuries(self):
        """Gets the number of centuries.

        return: (decimal) - the number of centuries
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    centuries = property(fget=get_centuries)

    def get_scores(self):
        """Gets the number of scores.

        return: (decimal) - the number of scores
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    scores = property(fget=get_scores)

    def get_bluemoons(self):
        """Gets the number of blue moons.

        return: (decimal) - the number of blue moons
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    bluemoons = property(fget=get_bluemoons)

    def get_years(self):
        """Gets the number of years.

        return: (decimal) - the number of years
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    years = property(fget=get_years)

    def get_months(self):
        """Gets the number of months.

        return: (decimal) - the number of months
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    months = property(fget=get_months)

    def get_weeks(self):
        """Gets the number of weeks.

        return: (decimal) - the number of weeks
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    weeks = property(fget=get_weeks)

    def get_days(self):
        """Gets the number of days.

        return: (decimal) - the number of days
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    days = property(fget=get_days)

    def get_hours(self):
        """Gets the number of hours.

        return: (decimal) - the number of hours
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    hours = property(fget=get_hours)

    def get_minutes(self):
        """Gets the number of minutes.

        return: (decimal) - the number of minutes
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    minutes = property(fget=get_minutes)

    def get_seconds(self):
        """Gets the number of seconds.

        return: (decimal) - the number of seconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    seconds = property(fget=get_seconds)

    def get_milliseconds(self):
        """Gets the number of milliseconds.

        A millisecond is one thousandth of a second.

        return: (decimal) - the number of milliseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    milliseconds = property(fget=get_milliseconds)

    def get_microseconds(self):
        """Gets the number of microseconds.

        A microsecond is one millionth of a second.

        return: (decimal) - the number of micrseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

#    microseconds = property(fget=get_microseconds)

    def get_nanoseconds(self):
        """Gets the number of nanoseconds.

        A nanosecond is one billionth of a second.

        return: (decimal) - the number of nanoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    nanoseconds = property(fget=get_nanoseconds)

    def get_picoseconds(self):
        """Gets the number of picoseconds.

        A picosecond is one trillionth of a second.

        return: (decimal) - the number of picoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    picoseconds = property(fget=get_picoseconds)

    def get_femtoseconds(self):
        """Gets the number of femtoseconds.

        A femtosecond is one quadrillionth of a second.

        return: (decimal) - the number of femtoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    femtoseconds = property(fget=get_femtoseconds)

    def get_attoseconds(self):
        """Gets the number of attoseconds.

        An attosecond is one quintillionth of a second.

        return: (decimal) - the number of attoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    attoseconds = property(fget=get_attoseconds)

    def get_zeptoseconds(self):
        """Gets the number of zeptoseconds.

        A zeptosecond is one sextillionth of a second.

        return: (decimal) - the number of zeptoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    zeptoseconds = property(fget=get_zeptoseconds)

    def get_yoctoseconds(self):
        """Gets the number of yoctoseconds.

        A yoctosecond is one septillionth of a second. This is getting
        quite small.

        return: (decimal) - the number of yoctoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    yoctoseconds = property(fget=get_yoctoseconds)

    def get_xoxxoseconds(self):
        """Gets the number of xoxxoseconds.

        A xoxxosecond is one octillionth of a second. We're going with
        Rudy Rucker here.

        return: (decimal) - the number of xoxxoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    xoxxoseconds = property(fget=get_xoxxoseconds)

    def get_weebleseconds(self):
        """Gets the number of weebleseconds.

        A weeblesecond is one nonillionth of a second.

        return: (decimal) - the number of weebleseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    weebleseconds = property(fget=get_weebleseconds)

    def get_vatoseconds(self):
        """Gets the number of vatoseconds.

        A vatosecond is one decillionth of a second.

        return: (decimal) - the number of vatoseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    vatoseconds = property(fget=get_vatoseconds)

    def get_undaseconds(self):
        """Gets the number of undaseconds.

        An undasecond is one unadecillionth of a second.

        return: (decimal) - the number of undaseconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    undaseconds = property(fget=get_undaseconds)

    def get_planck_seconds(self):
        """Gets the number of Planck sseconds.

        A Planck is 10 quattuordecillionths of a second.

        return: (decimal) - the number of planck seconds
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    planck_seconds = property(fget=get_planck_seconds)

    def get_granularity(self):
        """Gets the granularity of this duration.

        The granularity indicates the resolution of the clock. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        return: (osid.calendaring.DateTimeResolution) - the time units
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    granularity = property(fget=get_granularity)

    def get_granularity_multiplier(self):
        """If the granularity of the time equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        return: (cardinal) - granularity multiplier
        *compliance: mandatory -- This method must be implemented.*

        """
        return 1

    granularity_multiplier = property(fget=get_granularity_multiplier)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this time.

        return: (boolean) - ``true`` if uncertainty is defined,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_uncertainty_units(self):
        """Gets the units of the uncertainty.

        return: (osid.calendaring.DateTimeResolution) - units of the
                uncertainty
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    uncertainty_units = property(fget=get_uncertainty_units)

    def get_uncertainty_minus(self):
        """Gets the uncertainty of this time in the negative direction.

        return: (cardinal) - the uncertainty under this value
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty of this time in the positive direction.

        return: (cardinal) - the uncertainty over this value
        raise:  IllegalState - ``defines_uncertainty()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    uncertainty_plus = property(fget=get_uncertainty_plus)
