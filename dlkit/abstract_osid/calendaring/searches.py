"""Implementations of calendaring abstract base class searches."""
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


class EventSearch:
    """``EventSearch`` defines the interface for specifying event search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_events(self, event_ids):
        """Execute this search among the given list of events.

        :param event_ids: list of events
        :type event_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``event_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_event_results(self, event_search_order):
        """Specify an ordering to the search results.

        :param event_search_order: event search order
        :type event_search_order: ``osid.calendaring.EventSearchOrder``
        :raise: ``NullArgument`` -- ``event_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``event_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_event_search_record(self, event_search_record_type):
        """Gets the event search record corresponding to the given event search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param event_search_record_type: an event search record type
        :type event_search_record_type: ``osid.type.Type``
        :return: the event search record
        :rtype: ``osid.calendaring.records.EventSearchRecord``
        :raise: ``NullArgument`` -- ``event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.EventSearchRecord


class EventSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_events(self):
        """Gets the event list resulting from the search.

        :return: the event list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventList

    events = property(fget=get_events)

    @abc.abstractmethod
    def get_event_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    event_query_inspector = property(fget=get_event_query_inspector)

    @abc.abstractmethod
    def get_event_search_results_record(self, event_search_record_type):
        """Gets the event search results record corresponding to the given event search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param event_search_record_type: an event search record type
        :type event_search_record_type: ``osid.type.Type``
        :return: the event search results record
        :rtype: ``osid.calendaring.records.EventSearchResultsRecord``
        :raise: ``NullArgument`` -- ``event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.EventSearchResultsRecord


class RecurringEventSearch:
    """``RecurringEventSearch`` defines the interface for specifying recurring event search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_recurring_events(self, recurring_event_ids):
        """Execute this search among the given list of recurring events.

        :param recurring_event_ids: list of recurring events
        :type recurring_event_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``recurring_event_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_recurring_event_results(self, recurring_event_search_order):
        """Specify an ordering to the search results.

        :param recurring_event_search_order: recurring event search order
        :type recurring_event_search_order: ``osid.calendaring.RecurringEventSearchOrder``
        :raise: ``NullArgument`` -- ``recurring_event_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``recurring_event_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_recurring_event_search_record(self, recurring_event_search_record_type):
        """Gets the recurring event record corresponding to the given recurring event search record ``Type``.

        :param recurring_event_search_record_type: a recurring event search record type
        :type recurring_event_search_record_type: ``osid.type.Type``
        :return: the recurring event search record
        :rtype: ``osid.calendaring.records.RecurringEventSearchRecord``
        :raise: ``NullArgument`` -- ``recurring_event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.RecurringEventSearchRecord


class RecurringEventSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_recurring_events(self):
        """Gets the recurring event list resulting from the search.

        :return: the recurring event list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.RecurringEventList

    recurring_events = property(fget=get_recurring_events)

    @abc.abstractmethod
    def get_recurring_event_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.RecurringEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.RecurringEventQueryInspector

    recurring_event_query_inspector = property(fget=get_recurring_event_query_inspector)

    @abc.abstractmethod
    def get_recurring_event_search_results_record(self, recurring_event_search_record_type):
        """Gets the recurring event search results record corresponding to the given recurring event search record
        ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param recurring_event_search_record_type: a recurring event search record type
        :type recurring_event_search_record_type: ``osid.type.Type``
        :return: the recurring event search results record
        :rtype: ``osid.calendaring.records.RecurringEventSearchResultsRecord``
        :raise: ``NullArgument`` -- ``recurring_event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.RecurringEventSearchResultsRecord


class SupersedingEventSearch:
    """``SupersedingEventSearch`` defines the interface for specifying superseding event search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_superseding_events(self, superseding_event_ids):
        """Execute this search among the given list of superseding events.

        :param superseding_event_ids: list of superseding events
        :type superseding_event_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``superseding_event_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_superseding_event_results(self, superseding_event_search_order):
        """Specify an ordering to the search results.

        :param superseding_event_search_order: superseding event search order
        :type superseding_event_search_order: ``osid.calendaring.SupersedingEventSearchOrder``
        :raise: ``NullArgument`` -- ``superseding_event_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``supereding_event_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_superseding_event_search_record(self, superseding_event_search_record_type):
        """Gets the superseding event search record corresponding to the given superseding event search record ``Type``.

        :param superseding_event_search_record_type: a superseding event search record type
        :type superseding_event_search_record_type: ``osid.type.Type``
        :return: the superseding event search record
        :rtype: ``osid.calendaring.records.SupersedingEventSearchRecord``
        :raise: ``NullArgument`` -- ``superseding_event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.SupersedingEventSearchRecord


class SupersedingEventSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_superseding_events(self):
        """Gets the superseding event list resulting from the search.

        :return: the superseding event list
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.SupersedingEventList

    superseding_events = property(fget=get_superseding_events)

    @abc.abstractmethod
    def get_superseding_event_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.SupersedingEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.SupersedingEventQueryInspector

    superseding_event_query_inspector = property(fget=get_superseding_event_query_inspector)

    @abc.abstractmethod
    def get_superseding_event_search_results_record(self, superseding_event_search_record_type):
        """Gets the superseding event search results record corresponding to the given superseding event search record
        ``Type``.

        :param superseding_event_search_record_type: a superseding event search record type
        :type superseding_event_search_record_type: ``osid.type.Type``
        :return: the superseding event search results record
        :rtype: ``osid.calendaring.records.SupersedingEventSearchResultsRecord``
        :raise: ``NullArgument`` -- ``superseding_event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.SupersedingEventSearchResultsRecord


class OffsetEventSearch:
    """``OffsetEventSearch`` defines the interface for specifying offset event search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_offset_events(self, offset_event_ids):
        """Execute this search among the given list of offset events.

        :param offset_event_ids: list of offset events
        :type offset_event_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``offset_event_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_offset_event_results(self, offset_event_search_order):
        """Specify an ordering to the search results.

        :param offset_event_search_order: offset event search order
        :type offset_event_search_order: ``osid.calendaring.OffsetEventSearchOrder``
        :raise: ``NullArgument`` -- ``offset_event_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``offset_event_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_offset_event_search_record(self, offset_event_search_record_type):
        """Gets the offset event search record corresponding to the given offset event search record ``Type``.

        :param offset_event_search_record_type: an offset event search record type
        :type offset_event_search_record_type: ``osid.type.Type``
        :return: the offset event search record
        :rtype: ``osid.calendaring.records.OffsetEventSearchRecord``
        :raise: ``NullArgument`` -- ``offset_event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.OffsetEventSearchRecord


class OffsetEventSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_offset_events(self):
        """Gets the offset event list resulting from the search.

        :return: the offset event list
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.OffsetEventList

    offset_events = property(fget=get_offset_events)

    @abc.abstractmethod
    def get_offset_event_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.OffsetEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.OffsetEventQueryInspector

    offset_event_query_inspector = property(fget=get_offset_event_query_inspector)

    @abc.abstractmethod
    def get_offset_event_search_results_record(self, offset_event_search_record_type):
        """Gets the offset event search results record corresponding to the given offset event search record ``Type``.

        :param offset_event_search_record_type: an offset event search record type
        :type offset_event_search_record_type: ``osid.type.Type``
        :return: the offset event search results record
        :rtype: ``osid.calendaring.records.OffsetEventSearchResultsRecord``
        :raise: ``NullArgument`` -- ``offset_event_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.OffsetEventSearchResultsRecord


class ScheduleSearch:
    """``ScheduleSearch`` defines the interface for specifying schedule search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_schedules(self, schedule_ids):
        """Execute this search among the given list of schedules.

        :param schedule_ids: list of schedules
        :type schedule_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``schedule_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_schedule_results(self, schedule_search_order):
        """Specify an ordering to the search results.

        :param schedule_search_order: schedule search order
        :type schedule_search_order: ``osid.calendaring.ScheduleSearchOrder``
        :raise: ``NullArgument`` -- ``schedule_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``schedule_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_schedule_search_record(self, schedule_search_record_type):
        """Gets the schedule search record corresponding to the given schedule search record ``Type``.

        :param schedule_search_record_type: a schedule search record type
        :type schedule_search_record_type: ``osid.type.Type``
        :return: the schedule search record
        :rtype: ``osid.calendaring.records.ScheduleSearchRecord``
        :raise: ``NullArgument`` -- ``schedule_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSearchRecord


class ScheduleSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_schedules(self):
        """Gets the schedule list resulting from the search.

        :return: the schedule list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleList

    schedules = property(fget=get_schedules)

    @abc.abstractmethod
    def get_schedule_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.ScheduleQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleQueryInspector

    schedule_query_inspector = property(fget=get_schedule_query_inspector)

    @abc.abstractmethod
    def get_schedule_search_results_record(self, schedule_search_record_type):
        """Gets the schedule search results record corresponding to the given schedule search record ``Type``.

        :param schedule_search_record_type: a schedule search record type
        :type schedule_search_record_type: ``osid.type.Type``
        :return: the schedule search results record
        :rtype: ``osid.calendaring.records.ScheduleSearchResultsRecord``
        :raise: ``NullArgument`` -- ``schedule_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSearchResultsRecord


class ScheduleSlotSearch:
    """``ScheduleSlotSearch`` defines the interface for specifying schedule slot search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_schedule_slots(self, schedule_slot_ids):
        """Execute this search among the given list of schedule slots.

        :param schedule_slot_ids: list of schedule slots
        :type schedule_slot_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``schedule_slot_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_schedule_slot_results(self, schedule_slot_search_order):
        """Specify an ordering to the search results.

        :param schedule_slot_search_order: schedule slot search order
        :type schedule_slot_search_order: ``osid.calendaring.ScheduleSlotSearchOrder``
        :raise: ``NullArgument`` -- ``schedule_slot_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``schedule_slot_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_schedule_slot_search_record(self, schedule_slot_search_record_type):
        """Gets the schedule slot search record corresponding to the given schedule slot search record ``Type``.

        :param schedule_slot_search_record_type: a schedule slot search record type
        :type schedule_slot_search_record_type: ``osid.type.Type``
        :return: the schedule slot search record
        :rtype: ``osid.calendaring.records.ScheduleSlotSearchRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSlotSearchRecord


class ScheduleSlotSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_schedule_slots(self):
        """Gets the schedule list resulting from the search.

        :return: the schedule slot list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleSlotList

    schedule_slots = property(fget=get_schedule_slots)

    @abc.abstractmethod
    def get_schedule_slot_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.ScheduleSlotQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleSlotQueryInspector

    schedule_slot_query_inspector = property(fget=get_schedule_slot_query_inspector)

    @abc.abstractmethod
    def get_schedule_slot_search_results_record(self, schedule_slot_search_record_type):
        """Gets the schedule slot record corresponding to the given schedule slot search record ``Type``.

        :param schedule_slot_search_record_type: a schedule slot search record type
        :type schedule_slot_search_record_type: ``osid.type.Type``
        :return: the schedule slot search results record
        :rtype: ``osid.calendaring.records.ScheduleSlotSearchResultsRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSlotSearchResultsRecord


class TimePeriodSearch:
    """``TimePeriodSearch`` defines the interface for specifying time period search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_time_periods(self, time_period_ids):
        """Execute this search among the given list of time periods.

        :param time_period_ids: list of time periods
        :type time_period_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``time_period_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_time_period_results(self, time_period_search_order):
        """Specify an ordering to the search results.

        :param time_period_search_order: time period search order
        :type time_period_search_order: ``osid.calendaring.TimePeriodSearchOrder``
        :raise: ``NullArgument`` -- ``time_period_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``time_period_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_time_period_search_record(self, time_period_search_record_type):
        """Gets the time period search record corresponding to the given time period search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param time_period_search_record_type: a time period search record type
        :type time_period_search_record_type: ``osid.type.Type``
        :return: the time period search record
        :rtype: ``osid.calendaring.records.TimePeriodSearchRecord``
        :raise: ``NullArgument`` -- ``time_period_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.TimePeriodSearchRecord


class TimePeriodSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_time_periods(self):
        """Gets the time period list resulting from the search.

        :return: the time period list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.TimePeriodList

    time_periods = property(fget=get_time_periods)

    @abc.abstractmethod
    def get_time_period_query_inspector(self):
        """Gets the inspector for the query to examine the time periods used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.TimePeriodQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.TimePeriodQueryInspector

    time_period_query_inspector = property(fget=get_time_period_query_inspector)

    @abc.abstractmethod
    def get_time_period_search_results_record(self, time_period_search_record_type):
        """Gets the time period search results record corresponding to the given time period search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param time_period_search_record_type: a time period search record type
        :type time_period_search_record_type: ``osid.type.Type``
        :return: the time period search results record
        :rtype: ``osid.calendaring.records.TimePeriodSearchResultsRecord``
        :raise: ``NullArgument`` -- ``time_period_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.TimePeriodSearchResultsRecord


class CommitmentSearch:
    """``CommitmentSearch`` defines the interface for specifying commitment search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_commitments(self, commitment_ids):
        """Execute this search among the given list of commitments.

        :param commitment_ids: list of commitments
        :type commitment_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``commitment_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_commitment_results(self, commitment_search_order):
        """Specify an ordering to the search results.

        :param commitment_search_order: commitment search order
        :type commitment_search_order: ``osid.calendaring.CommitmentSearchOrder``
        :raise: ``NullArgument`` -- ``commitment_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``commitment_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_commitment_search_record(self, commitment_search_record_type):
        """Gets the commitment seaqrch record corresponding to the given commitment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param commitment_search_record_type: a commitment search record type
        :type commitment_search_record_type: ``osid.type.Type``
        :return: the commitment search record
        :rtype: ``osid.calendaring.records.CommitmentSearchRecord``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CommitmentSearchRecord


class CommitmentSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_commitments(self):
        """Gets the commitment list resulting from the search.

        :return: the commitment list
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CommitmentList

    commitments = property(fget=get_commitments)

    @abc.abstractmethod
    def get_commitment_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.calendaring.CommitmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CommitmentQueryInspector

    commitment_query_inspector = property(fget=get_commitment_query_inspector)

    @abc.abstractmethod
    def get_commitment_search_results_record(self, commitment_search_record_type):
        """Gets the commitment search results record corresponding to the given commitment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param commitment_search_record_type: a commitment search record type
        :type commitment_search_record_type: ``osid.type.Type``
        :return: the commitment search results record
        :rtype: ``osid.calendaring.records.CommitmentSearchResultsRecord``
        :raise: ``NullArgument`` -- ``commitment_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CommitmentSearchResultsRecord


class CalendarSearch:
    """The interface for governing calendar searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_calendars(self, calendar_ids):
        """Execute this search among the given list of calendars.

        :param calendar_ids: list of calendars
        :type calendar_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_calendar_results(self, calendar_search_order):
        """Specify an ordering to the search results.

        :param calendar_search_order: calendar search order
        :type calendar_search_order: ``osid.calendaring.CalendarSearchOrder``
        :raise: ``NullArgument`` -- ``calendar_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``calendar_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_calendar_search_record(self, calendar_search_record_type):
        """Gets the calendar search record corresponding to the given calendar search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param calendar_search_record_type: a calendar search record type
        :type calendar_search_record_type: ``osid.type.Type``
        :return: the calendar search interface
        :rtype: ``osid.calendaring.records.CalendarSearchRecord``
        :raise: ``NullArgument`` -- ``calendar_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CalendarSearchRecord


class CalendarSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_calendars(self):
        """Gets the calendar list resulting from the search.

        :return: the calendar list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarList

    calendars = property(fget=get_calendars)

    @abc.abstractmethod
    def get_calendar_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the calendar query inspector
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_query_inspector = property(fget=get_calendar_query_inspector)

    @abc.abstractmethod
    def get_calendar_search_results_record(self, calendar_search_record_type):
        """Gets the calendar search results record corresponding to the given calendar search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param calendar_search_record_type: a calendar search record type
        :type calendar_search_record_type: ``osid.type.Type``
        :return: the calendar search results record
        :rtype: ``osid.calendaring.records.CalendarSearchResultsRecord``
        :raise: ``NullArgument`` -- ``calendar_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CalendarSearchResultsRecord
