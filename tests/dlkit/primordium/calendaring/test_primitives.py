import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.calendaring.primitives import DateTime, Duration


@pytest.fixture(scope="function")
def date_time_test_wrapper(request):
    utcnow = DateTime.utcnow()
    request.cls.date_time = DateTime(
        year=utcnow.year,
        month=utcnow.month,
        day=utcnow.day,
        hour=utcnow.hour,
        minute=utcnow.minute,
        second=utcnow.second,
        microsecond=utcnow.microsecond
    )


@pytest.mark.usefixtures("date_time_test_wrapper")
class TestDateTime(object):
    def test_get_calendar_type(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_calendar_type()

    def test_get_aeon(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_aeon()

    def test_get_epoch(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_epoch()

    def test_get_millennium(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_millennium()

    def test_get_century(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_century()

    def test_get_year(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_year()

    def test_get_month(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_month()

    def test_get_day(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_day()

    def test_get_time_type(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_time_type()

    def test_get_hour(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_hour()

    def test_get_minute(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_minute()

    def test_get_second(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_second()

    def test_get_milliseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_milliseconds()

    def test_get_microseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_microseconds()

    def test_get_nanoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_nanoseconds()

    def test_get_picoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_picoseconds()

    def test_get_femtoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_femtoseconds()

    def test_get_attoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_attoseconds()

    def test_get_zeptoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_zeptoseconds()

    def test_get_yoctoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_yoctoseconds()

    def test_get_xoxxoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_xoxxoseconds()

    def test_get_weebleseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_weebleseconds()

    def test_get_vatoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_vatoseconds()

    def test_get_undaseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_undaseconds()

    def test_get_planck_seconds(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_planck_seconds()

    def test_get_granularity(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_granularity()

    def test_get_granularity_multiplier(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_granularity_multiplier()

    def test_defines_uncertainty(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.defines_uncertainty()

    def test_get_uncertainty_units(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_uncertainty_units()

    def test_get_uncertainty_minus(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_uncertainty_minus()

    def test_get_uncertainty_plus(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.get_uncertainty_plus()

    def test_is_uncertainty_date_inclusive(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.is_uncertainty_date_inclusive()

    def test_is_uncertainty_time_inclusive(self):
        with pytest.raises(errors.Unimplemented):
            self.date_time.is_uncertainty_time_inclusive()


@pytest.fixture(scope="function")
def duration_test_wrapper(request):
    request.cls.duration = Duration(hours=5)


@pytest.mark.usefixtures("duration_test_wrapper")
class TestDuration(object):
    def test_get_calendar_type(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_calendar_type()

    def test_get_aeons(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_aeons()

    def test_get_epochs(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_epochs()

    def test_get_millennia(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_millennia()

    def test_get_centuries(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_centuries()

    def test_get_scores(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_scores()

    def test_get_bluemoons(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_bluemoons()

    def test_get_years(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_years()

    def test_get_months(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_months()

    def test_get_weeks(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_weeks()

    def test_get_days(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_days()

    def test_get_time_type(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_time_type()

    def test_get_hours(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_hours()

    def test_get_minutes(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_minutes()

    def test_get_seconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_seconds()

    def test_get_milliseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_milliseconds()

    def test_get_microseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_microseconds()

    def test_get_nanoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_nanoseconds()

    def test_get_picoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_picoseconds()

    def test_get_femtoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_femtoseconds()

    def test_get_attoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_attoseconds()

    def test_get_zeptoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_zeptoseconds()

    def test_get_yoctoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_yoctoseconds()

    def test_get_xoxxoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_xoxxoseconds()

    def test_get_weebleseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_weebleseconds()

    def test_get_vatoseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_vatoseconds()

    def test_get_undaseconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_undaseconds()

    def test_get_planck_seconds(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_planck_seconds()

    def test_get_granularity(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_granularity()

    def test_get_granularity_multiplier(self):
        assert self.duration.get_granularity_multiplier() == 1

    def test_defines_uncertainty(self):
        assert not self.duration.defines_uncertainty()

    def test_get_uncertainty_units(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_uncertainty_units()

    def test_get_uncertainty_minus(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_uncertainty_minus()

    def test_get_uncertainty_plus(self):
        with pytest.raises(errors.Unimplemented):
            self.duration.get_uncertainty_plus()
