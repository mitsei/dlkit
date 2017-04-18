"""Implementations of calendaring abstract base class records."""
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


class EventRecord:
    """A record for an ``Event``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class EventQueryRecord:
    """A record for an ``EventQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class EventQueryInspectorRecord:
    """A record for an ``EventQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class EventFormRecord:
    """A record for an ``EventForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class EventSearchOrderRecord:
    """A record for an ``EventSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class EventSearchRecord:
    """A record for an ``EventSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class EventSearchResultsRecord:
    """A record for an ``EventSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventRecord:
    """A record for a ``RecurringEvent``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventQueryRecord:
    """A record for a ``RecurringEventQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventQueryInspectorRecord:
    """A record for a ``RecurringEventQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventFormRecord:
    """A record for a ``RecurringEventForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventSearchOrderRecord:
    """A record for a ``RecurringEventSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventSearchRecord:
    """A record for a ``RecurringEventSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RecurringEventSearchResultsRecord:
    """A record for a ``RecurringEventSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventRecord:
    """A record for a ``SupersedingEvent``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventQueryRecord:
    """A record for a ``SupersedingEventQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventQueryInspectorRecord:
    """A record for a ``SupersedingEventQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventFormRecord:
    """A record for a ``SupersedingEventForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventSearchOrderRecord:
    """A record for a ``SupersedingEventSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventSearchRecord:
    """A record for a ``SupersedingEventSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SupersedingEventSearchResultsRecord:
    """A record for a ``SupersedingEventSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventRecord:
    """A record for an ``OffsetEvent``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventQueryRecord:
    """A record for an ``OffsetEventQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventQueryInspectorRecord:
    """A record for an ``OffsetEventQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventFormRecord:
    """A record for an ``OffsetEventForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventSearchOrderRecord:
    """A record for an ``OffsetEventSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventSearchRecord:
    """A record for an ``OffsetEventSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class OffsetEventSearchResultsRecord:
    """A record for an ``OffsetEventSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleRecord:
    """A record for a ``Schedule``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleQueryRecord:
    """A record for a ``ScheduleQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleQueryInspectorRecord:
    """A record for a ``ScheduleQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleFormRecord:
    """A record for a ``ScheduleForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSearchOrderRecord:
    """A record for a ``ScheduleSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSearchRecord:
    """A record for a ``ScheduleSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSearchResultsRecord:
    """A record for a ``ScheduleSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotRecord:
    """A record for a ``ScheduleSlot``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotQueryRecord:
    """A record for a ``ScheduleSlotQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotQueryInspectorRecord:
    """A record for a ``ScheduleSlotQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotFormRecord:
    """A record for a ``ScheduleSlotForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotSearchOrderRecord:
    """A record for a ``ScheduleSlotSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotSearchRecord:
    """A record for a ``ScheduleSlotSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ScheduleSlotSearchResultsRecord:
    """A record for a ``ScheduleSlotSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodRecord:
    """A record for a ``TimePeriod``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodQueryRecord:
    """A record for a ``TimePeriodQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodQueryInspectorRecord:
    """A record for a ``TimePeriodQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodFormRecord:
    """A record for a ``TimePeriodForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodSearchOrderRecord:
    """A record for a ``TimePeriodSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodSearchRecord:
    """A record for a ``TimePeriodSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class TimePeriodSearchResultsRecord:
    """A record for a ``TimePeriodSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentRecord:
    """A record for a ``Commitment``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentQueryRecord:
    """A record for a ``CommitmentQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentQueryInspectorRecord:
    """A record for a ``CommitmentQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentFormRecord:
    """A record for a ``CommitmentForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentSearchOrderRecord:
    """A record for a ``CommitmentSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentSearchRecord:
    """A record for a ``CommitmentSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CommitmentSearchResultsRecord:
    """A record for a ``CommitmentSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarRecord:
    """A record for a ``Calendar``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarQueryRecord:
    """A record for a ``CalendarQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarQueryInspectorRecord:
    """A record for a ``CalendarQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarFormRecord:
    """A record for a ``CalendarForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarSearchOrderRecord:
    """A record for a ``CalendarSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarSearchRecord:
    """A record for a ``CalendarSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class CalendarSearchResultsRecord:
    """A record for a ``CalendarSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
