"""Implementations of calendaring abstract base class search_orders."""
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


class EventSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_duration(self, style):
        """Specified a preference for ordering results by the duration.

        For recurring events, the duration is the duration of a single
        event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_recurring_event(self, style):
        """Specified a preference for ordering results by the recurring event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_recurring_event_search_order(self):
        """Tests if a ``RecurringEventSearchOrder`` is available for recurring events.

        :return: ``true`` if a recurring event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_recurring_event_search_order(self):
        """Gets the search order for a recurring event.

        :return: the recurring event search order
        :rtype: ``osid.calendaring.RecurringEventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventSearchOrder

    recurring_event_search_order = property(fget=get_recurring_event_search_order)

    @abc.abstractmethod
    def order_by_superseding_event(self, style):
        """Specified a preference for ordering results by the superseding event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_superseding_event_search_order(self):
        """Tests if a ``SupersedingEventSearchOrder`` is available for offset events.

        :return: ``true`` if a superseding event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_superseding_event_search_order(self):
        """Gets the search order for a superseding event.

        :return: the superseding event search order
        :rtype: ``osid.calendaring.SupersedingEventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSearchOrder

    superseding_event_search_order = property(fget=get_superseding_event_search_order)

    @abc.abstractmethod
    def order_by_offset_event(self, style):
        """Specified a preference for ordering results by the offset event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_offset_event_search_order(self):
        """Tests if an ``OffsetEventSearchOrder`` is available for offset events.

        :return: ``true`` if an offset event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_offset_event_search_order(self):
        """Gets the search order for an offset event.

        :return: the offset event search order
        :rtype: ``osid.calendaring.OffsetEventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_offset_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventSearchOrder

    offset_event_search_order = property(fget=get_offset_event_search_order)

    @abc.abstractmethod
    def order_by_location_description(self, style):
        """Specified a preference for ordering results by the location description.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_location(self, style):
        """Specified a preference for ordering results by the location.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_location_search_order(self):
        """Tests if a ``LocationSearchOrder`` is available.

        :return: ``true`` if a location search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_search_order(self):
        """Gets the search order for a location.

        :return: the location search order
        :rtype: ``osid.mapping.LocationSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_location_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search_order()`` is ``true``.*

        """
        return  # osid.mapping.LocationSearchOrder

    location_search_order = property(fget=get_location_search_order)

    @abc.abstractmethod
    def get_event_search_order_record(self, event_record_type):
        """Gets the event search order record corresponding to the given event record ``Type``.

        Multiple retrievals return the same underlying object.

        :param event_record_type: an event record type
        :type event_record_type: ``osid.type.Type``
        :return: the event search order record
        :rtype: ``osid.calendaring.records.EventSearchOrderRecord``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.EventSearchOrderRecord


class RecurringEventSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_recurring_event_search_order_record(self, recurring_event_record_type):
        """Gets the recurring event search order record corresponding to the given event record ``Type``.

        Multiple retrievals return the same underlying object.

        :param recurring_event_record_type: a recurring event record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: the recurring event search order record
        :rtype: ``osid.calendaring.records.RecurringEventSearchOrderRecord``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.RecurringEventSearchOrderRecord


class SupersedingEventSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_superseded_event(self, style):
        """Specified a preference for ordering results by the superseded event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_superseded_event_search_order(self):
        """Tests if an ``EventSearchOrder`` is available.

        :return: ``true`` if an event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_superseded_event_search_order(self):
        """Gets the search order for the superseded event.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_superseded_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseded_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchOrder

    superseded_event_search_order = property(fget=get_superseded_event_search_order)

    @abc.abstractmethod
    def order_by_superseding_event(self, style):
        """Specified a preference for ordering results by the superseding event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_superseding_event_search_order(self):
        """Tests if an ``EventSearchOrder`` is available.

        :return: ``true`` if an event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_superseding_event_search_order(self):
        """Gets the search order for the superseding event.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchOrder

    superseding_event_search_order = property(fget=get_superseding_event_search_order)

    @abc.abstractmethod
    def order_by_superseded_date(self, style):
        """Specified a preference for ordering results by the superseded date.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_superseded_event_position(self, style):
        """Specified a preference for ordering results by the superseded event position.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_superseding_event_search_order_record(self, superseding_event_record_type):
        """Gets the superseding event search order record corresponding to the given superseding event record ``Type``.

        Multiple retrievals return the same underlying object.

        :param superseding_event_record_type: a superseding event record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: the superseding event search order record
        :rtype: ``osid.calendaring.records.SupersedingEventSearchOrderRecord``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.SupersedingEventSearchOrderRecord


class OffsetEventSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_fixed_start_time(self, style):
        """Specified a preference for ordering results by the fixed start time.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_start_reference_event(self, style):
        """Specified a preference for ordering results by the starting reference event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_start_reference_event_search_order(self):
        """Tests if an ``EventSearchOrder`` is available.

        :return: ``true`` if an event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_start_reference_event_search_order(self):
        """Gets the search order for an event.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_start_reference_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_start_reference_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchOrder

    start_reference_event_search_order = property(fget=get_start_reference_event_search_order)

    @abc.abstractmethod
    def order_by_fixed_start_offset(self, style):
        """Specified a preference for ordering results by the fixed offset.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_relative_weekday_start_offset(self, style):
        """Specified a preference for ordering results by the relative weekday offset.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_relative_start_weekday(self, style):
        """Specified a preference for ordering results by the relative weekday.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_fixed_duration(self, style):
        """Specified a preference for ordering results by the fixed duration.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_end_reference_event(self, style):
        """Specified a preference for ordering results by the ending reference event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_end_reference_event_search_order(self):
        """Tests if an ``EventSearchOrder`` is available.

        :return: ``true`` if an event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_end_reference_event_search_order(self):
        """Gets the search order for an event.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_end_reference_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_end_reference_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchOrder

    end_reference_event_search_order = property(fget=get_end_reference_event_search_order)

    @abc.abstractmethod
    def order_by_fixed_end_offset(self, style):
        """Specified a preference for ordering results by the fixed offset.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_relative_weekday_end_offset(self, style):
        """Specified a preference for ordering results by the relative weekday offset.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_relative_end_weekday(self, style):
        """Specified a preference for ordering results by the relative weekday.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_location_description(self, style):
        """Specified a preference for ordering results by the location description.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_location(self, style):
        """Specified a preference for ordering results by the location.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_location_search_order(self):
        """Tests if a ``LocationSearchOrder`` is available.

        :return: ``true`` if a location search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_search_order(self):
        """Gets the search order for a location.

        :return: the location search order
        :rtype: ``osid.mapping.LocationSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_location_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search_order()`` is ``true``.*

        """
        return  # osid.mapping.LocationSearchOrder

    location_search_order = property(fget=get_location_search_order)

    @abc.abstractmethod
    def get_offset_event_search_order_record(self, offset_event_record_type):
        """Gets the offset event search order record corresponding to the given offset event record ``Type``.

        Multiple retrievals return the same underlying object.

        :param offset_event_record_type: an offset event record type
        :type offset_event_record_type: ``osid.type.Type``
        :return: the offset event search order record
        :rtype: ``osid.calendaring.records.OffsetEventSearchOrderRecord``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.OffsetEventSearchOrderRecord


class ScheduleSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_schedule_slot(self, style):
        """Specified a preference for ordering results by the schedule slot.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_schedule_slot_search_order(self):
        """Tests if a ``ScheduleSlotSearchOrder`` is available.

        :return: ``true`` if a schedule slot search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_schedule_slot_search_order(self):
        """Gets the search order for the schedule slot.

        :return: the schdeule slot search order
        :rtype: ``osid.calendaring.ScheduleSlotSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSearchOrder

    schedule_slot_search_order = property(fget=get_schedule_slot_search_order)

    @abc.abstractmethod
    def order_by_time_period(self, style):
        """Specified a preference for ordering results by the time period.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_time_period_search_order(self):
        """Tests if a ``TimePeriodSearchOrder`` is available.

        :return: ``true`` if a time period search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_time_period_search_order(self):
        """Gets the search order for the time period.

        :return: the time period search order
        :rtype: ``osid.calendaring.TimePeriodSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_time_period_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodSearchOrder

    time_period_search_order = property(fget=get_time_period_search_order)

    @abc.abstractmethod
    def order_by_schedule_start(self, style):
        """Specified a preference for ordering results by the schedule start.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_schedule_end(self, style):
        """Specified a preference for ordering results by the schedule end.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_total_duration(self, style):
        """Specified a preference for ordering results by the schedule duration.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_limit(self, style):
        """Specified a preference for ordering results by the occurrence limit.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_location_description(self, style):
        """Specified a preference for ordering results by the location description.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_location(self, style):
        """Specified a preference for ordering results by the location.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_location_search_order(self):
        """Tests if a ``LocationSearchOrder`` is available.

        :return: ``true`` if a location search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_search_order(self):
        """Gets the search order for a location.

        :return: the location search order
        :rtype: ``osid.mapping.LocationSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_location_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search_order()`` is ``true``.*

        """
        return  # osid.mapping.LocationSearchOrder

    location_search_order = property(fget=get_location_search_order)

    @abc.abstractmethod
    def get_schedule_search_order_record(self, schedule_record_type):
        """Gets the schedule search order record corresponding to the given schedule record ``Type``.

        Multiple retrievals return the same underlying object.

        :param schedule_record_type: a schedule record type
        :type schedule_record_type: ``osid.type.Type``
        :return: the schedule search order record
        :rtype: ``osid.calendaring.records.ScheduleSearchOrderRecord``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSearchOrderRecord


class ScheduleSlotSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_weekday_start(self, style):
        """Specified a preference for ordering results by the starting weekday.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_weekly_interval(self, style):
        """Specified a preference for ordering results by the weekly interval.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_week_of_month(self, style):
        """Specified a preference for ordering results by the week of the month.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_weekday_time(self, style):
        """Specified a preference for ordering results by the weekday time.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_fixed_interval(self, style):
        """Specified a preference for ordering results by the fixed interval.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_duration(self, style):
        """Specified a preference for ordering results by the duration.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_schedule_slot_search_order_record(self, schedule_slot_record_type):
        """Gets the schedule slot search order record corresponding to the given schedule record ``Type``.

        Multiple retrievals return the same underlying object.

        :param schedule_slot_record_type: a schedule slot record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: the schedule slot search order record
        :rtype: ``osid.calendaring.records.ScheduleSlotSearchOrderRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSlotSearchOrderRecord


class TimePeriodSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_start(self, style):
        """Specified a preference for ordering results by the start time.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_end(self, style):
        """Specified a preference for ordering results by the end time.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_duration(self, style):
        """Specified a preference for ordering results by the time period duration.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_time_period_search_order_record(self, time_period_record_type):
        """Gets the time period search order record corresponding to the given time period record ``Type``.

        Multiple retrievals return the same underlying object.

        :param time_period_record_type: a time period record type
        :type time_period_record_type: ``osid.type.Type``
        :return: the time period search order record
        :rtype: ``osid.calendaring.records.TimePeriodSearchOrderRecord``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.TimePeriodSearchOrderRecord


class CommitmentSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_event(self, style):
        """Specified a preference for ordering results by the event.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_event_search_order(self):
        """Tests if an ``EventSearchOrder`` is available.

        :return: ``true`` if an event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_event_search_order(self):
        """Gets the search order for an event.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_event_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search_order()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchOrder

    event_search_order = property(fget=get_event_search_order)

    @abc.abstractmethod
    def order_by_resource(self, style):
        """Specified a preference for ordering results by the resource.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_resource_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_search_order(self):
        """Gets the search order for a resource.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    @abc.abstractmethod
    def get_commitment_search_order_record(self, commitment_record_type):
        """Gets the commitment search order record corresponding to the given commitment record ``Type``.

        Multiple retrievals return the same underlying object.

        :param commitment_record_type: a commitment record type
        :type commitment_record_type: ``osid.type.Type``
        :return: the commitment search order record
        :rtype: ``osid.calendaring.records.CommitmentSearchOrderRecord``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CommitmentSearchOrderRecord


class CalendarSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_calendar_search_order_record(self, calendar_record_type):
        """Gets the calendar search order record corresponding to the given calendar record ``Type``.

        Multiple retrievals return the same underlying object.

        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the calendar search order record
        :rtype: ``osid.calendaring.records.CalendarSearchOrderRecord``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CalendarSearchOrderRecord
