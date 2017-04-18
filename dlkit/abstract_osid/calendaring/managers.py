"""Implementations of calendaring abstract base class managers."""
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


class CalendaringProfile:
    """The ``CalendaringProfile`` describes the interoperability among calendaring services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_lookup(self):
        """Tests if an event lookup service is supported.

        An event lookup service defines methods to access events.

        :return: true if event lookup is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_query(self):
        """Tests if an event query service is supported.

        :return: ``true`` if event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_search(self):
        """Tests if an event search service is supported.

        :return: ``true`` if event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_admin(self):
        """Tests if an event administrative service is supported.

        :return: ``true`` if event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_notification(self):
        """Tests if event notification is supported.

        Messages may be sent when events are created, modified, or
        deleted.

        :return: ``true`` if event notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_calendar(self):
        """Tests if an event to calendar lookup session is available.

        :return: ``true`` if event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_calendar_assignment(self):
        """Tests if an event to calendar assignment session is available.

        :return: ``true`` if event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_event_smart_calendar(self):
        """Tests if event smart calendaring is available.

        :return: ``true`` if event smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_lookup(self):
        """Tests if a recurring event lookup service is supported.

        :return: true if recurring event lookup is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_unravelling(self):
        """Tests if a recurring event unravelling service is supported.

        :return: true if recurring event unravelling is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_query(self):
        """Tests if a recurring event query service is supported.

        :return: ``true`` if recurring event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_search(self):
        """Tests if a recurring event search service is supported.

        :return: ``true`` if recurring event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_admin(self):
        """Tests if a recurring event administrative service is supported.

        :return: ``true`` if recurring event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_notification(self):
        """Tests if recurring event notification is supported.

        Messages may be sent when recurring events are created,
        modified, or deleted.

        :return: ``true`` if recurring event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_calendar(self):
        """Tests if a recurring event to calendar lookup session is available.

        :return: ``true`` if recurring event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_calendar_assignment(self):
        """Tests if a recurring event to calendar assignment session is available.

        :return: ``true`` if recurring event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_recurring_event_smart_calendar(self):
        """Tests if recurring event smart calendaring is available.

        :return: ``true`` if recurring event smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_lookup(self):
        """Tests if a superseding event lookup service is supported.

        A superseding event lookup service defines methods to access
        superseding events.

        :return: true if superseding event lookup is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_query(self):
        """Tests if a superseding event query service is supported.

        :return: ``true`` if superseding event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_search(self):
        """Tests if a superseding event search service is supported.

        :return: ``true`` if superseding event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_admin(self):
        """Tests if a superseding event administrative service is supported.

        :return: ``true`` if superseding event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_notification(self):
        """Tests if superseding event notification is supported.

        Messages may be sent when supsreding events are created,
        modified, or deleted.

        :return: ``true`` if superseding event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_calendar(self):
        """Tests if superseding event to calendar lookup session is available.

        :return: ``true`` if superseding event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_calendar_assignment(self):
        """Tests if a superseding event to calendar assignment session is available.

        :return: ``true`` if superseding event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_superseding_event_smart_calendar(self):
        """Tests if supsreding event smart calendaring is available.

        :return: ``true`` if superseding smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_lookup(self):
        """Tests if an offset event lookup service is supported.

        An offset event lookup service defines methods to access events.

        :return: true if offset event lookup is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_query(self):
        """Tests if an offset event query service is supported.

        :return: ``true`` if offset event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_search(self):
        """Tests if an offset event search service is supported.

        :return: ``true`` if offset event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_admin(self):
        """Tests if an offset event administrative service is supported.

        :return: ``true`` if offset event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_notification(self):
        """Tests if offset event notification is supported.

        Messages may be sent when events are created, modified, or
        deleted.

        :return: ``true`` if offset event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_calendar(self):
        """Tests if an offset event to calendar lookup session is available.

        :return: ``true`` if event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_calendar_assignment(self):
        """Tests if an offset event to calendar assignment session is available.

        :return: ``true`` if offset event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_offset_event_smart_calendar(self):
        """Tests if offset event smart calendaring is available.

        :return: ``true`` if offset event smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_lookup(self):
        """Tests if a schedule lookup service is supported.

        A schedule lookup service defines methods to access schedules.

        :return: true if schedule lookup is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_query(self):
        """Tests if a schedule query service is supported.

        :return: ``true`` if schedule query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_search(self):
        """Tests if a schedule search service is supported.

        :return: ``true`` if schedule search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_admin(self):
        """Tests if a schedule administrative service is supported.

        :return: ``true`` if schedule admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_notification(self):
        """Tests if schedule notification is supported.

        Messages may be sent when schedules are created, modified, or
        deleted.

        :return: ``true`` if schedule notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_calendar(self):
        """Tests if a schedule to calendar lookup session is available.

        :return: ``true`` if schedule calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_calendar_assignment(self):
        """Tests if a schedule to calendar assignment session is available.

        :return: ``true`` if schedule calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_smart_calendar(self):
        """Tests if schedule smart calendaring is available.

        :return: ``true`` if schedule smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_lookup(self):
        """Tests if a schedule slot lookup service is supported.

        A schedule sot lookup service defines methods to access schedule
        slots.

        :return: true if schedule slot lookup is supported, false otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_query(self):
        """Tests if a schedule slot query service is supported.

        :return: ``true`` if schedule slot query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_search(self):
        """Tests if a schedule slot search service is supported.

        :return: ``true`` if schedule slots search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_admin(self):
        """Tests if a schedule slot administrative service is supported.

        :return: ``true`` if schedule slot admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_notification(self):
        """Tests if schedule slot notification is supported.

        Messages may be sent when schedule slots are created, modified,
        or deleted.

        :return: ``true`` if schedule slot notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_calendar(self):
        """Tests if a schedule slot to calendar lookup session is available.

        :return: ``true`` if schedule slot calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_calendar_assignment(self):
        """Tests if a schedule slot to calendar assignment session is available.

        :return: ``true`` if schedule slot calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_schedule_slot_smart_calendar(self):
        """Tests if schedule slot smart calendaring is available.

        :return: ``true`` if schedule slot smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_lookup(self):
        """Tests if an event commitment lookup service is supported.

        :return: ``true`` if commitment lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_query(self):
        """Tests if a commitment query service is supported.

        :return: ``true`` if commitment query is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_search(self):
        """Tests if a commitment search service is supported.

        :return: ``true`` if commitment search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_admin(self):
        """Tests if a commitment administrative service is supported.

        :return: ``true`` if commitment admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_notification(self):
        """Tests if commitment notification is supported.

        Messages may be sent when commitments are created, modified, or
        deleted.

        :return: ``true`` if commitment notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_calendar(self):
        """Tests if a commitment to calendar lookup session is available.

        :return: ``true`` if commitment calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_calendar_assignment(self):
        """Tests if a commitment to calendar assignment session is available.

        :return: ``true`` if commitment calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commitment_smart_calendar(self):
        """Tests if commitment smart calendaring is available.

        :return: ``true`` if commitment smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_lookup(self):
        """Tests if a time period lookup service is supported.

        :return: ``true`` if time period lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_search(self):
        """Tests if a time period search service is supported.

        :return: ``true`` if time period search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_admin(self):
        """Tests if a time period administrative service is supported.

        :return: ``true`` if time period admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_notification(self):
        """Tests if time period notification is supported.

        Messages may be sent when time periods are created, modified, or
        deleted.

        :return: ``true`` if time period notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_calendar(self):
        """Tests if a time period to calendar lookup session is available.

        :return: ``true`` if time period calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_calendar_assignment(self):
        """Tests if a time period to calendar assignment session is available.

        :return: ``true`` if time period calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_time_period_smart_calendar(self):
        """Tests if time period smart calendaring is available.

        :return: ``true`` if time period smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendar_lookup(self):
        """Tests if a calendar lookup service is supported.

        :return: ``true`` if calendar lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendar_search(self):
        """Tests if a calendar search service is supported.

        :return: ``true`` if calendar search is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendar_admin(self):
        """Tests if a calendar administrative service is supported.

        :return: ``true`` if calendar admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendar_notification(self):
        """Tests if calendar notification is supported.

        Messages may be sent when calendars are created, modified, or
        deleted.

        :return: ``true`` if calendar notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendar_hierarchy(self):
        """Tests if a calendar hierarchy traversal is supported.

        :return: ``true`` if a calendar hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendar_hierarchy_design(self):
        """Tests if calendar hierarchy design is supported.

        :return: ``true`` if a calendar hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendaring_batch(self):
        """Tests if a calendaring batch subpackage is supported.

        :return: ``true`` if a calendar batch package is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendaring_cycle(self):
        """Tests if a calendaring cycle subpackage is supported.

        :return: ``true`` if a calendar cycle package is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_calendaring_rules(self):
        """Tests if a calendaring rules subpackage is supported.

        :return: ``true`` if a calendar rules package is supported, ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_event_record_types(self):
        """Gets the supported ``Event`` record types.

        :return: a list containing the supported ``Event`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    event_record_types = property(fget=get_event_record_types)

    @abc.abstractmethod
    def supports_event_record_type(self, event_record_type):
        """Tests if the given ``Event`` record type is supported.

        :param event_record_type: a ``Type`` indicating an ``Event`` record type
        :type event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_event_search_record_types(self):
        """Gets the supported ``Event`` search record types.

        :return: a list containing the supported ``Event`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    event_search_record_types = property(fget=get_event_search_record_types)

    @abc.abstractmethod
    def supports_event_search_record_type(self, event_search_record_type):
        """Tests if the given ``Event`` search record type is supported.

        :param event_search_record_type: a ``Type`` indicating an ``Event`` search record type
        :type event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``event_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_recurring_event_record_types(self):
        """Gets the supported ``RecurringEvent`` record types.

        :return: a list containing the supported ``RecurringEvent`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    recurring_event_record_types = property(fget=get_recurring_event_record_types)

    @abc.abstractmethod
    def supports_recurring_event_record_type(self, recurring_event_record_type):
        """Tests if the given ``RecurringEvent`` record type is supported.

        :param recurring_event_record_type: a ``Type`` indicating a ``RecurringEvent`` record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_recurring_event_search_record_types(self):
        """Gets the supported ``RecurringEvent`` search record types.

        :return: a list containing the supported ``RecurringEvent`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    recurring_event_search_record_types = property(fget=get_recurring_event_search_record_types)

    @abc.abstractmethod
    def supports_recurring_event_search_record_type(self, recurring_event_search_record_type):
        """Tests if the given ``RecurringEvent`` search record type is supported.

        :param recurring_event_search_record_type: a ``Type`` indicating a ``RecurringEvent`` search record type
        :type recurring_event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``recurring_event_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_superseding_event_record_types(self):
        """Gets the supported ``Superseding`` record types.

        :return: a list containing the supported ``SupersedingEvent`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    superseding_event_record_types = property(fget=get_superseding_event_record_types)

    @abc.abstractmethod
    def supports_superseding_event_record_type(self, superseding_event_record_type):
        """Tests if the given ``SupersedingEvent`` record type is supported.

        :param superseding_event_record_type: a ``Type`` indicating a ``SupersedingEvent`` record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_superseding_event_search_record_types(self):
        """Gets the supported ``SupersedingEvent`` search record types.

        :return: a list containing the supported ``SupersedingEvent`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    superseding_event_search_record_types = property(fget=get_superseding_event_search_record_types)

    @abc.abstractmethod
    def supports_superseding_event_search_record_type(self, superseding_event_search_record_type):
        """Tests if the given ``SupersedingEvent`` search record type is supported.

        :param superseding_event_search_record_type: a ``Type`` indicating a ``SupersedingEvent`` search record type
        :type superseding_event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_offset_event_record_types(self):
        """Gets the supported ``OffsetEvent`` record types.

        :return: a list containing the supported ``OffsetEvent`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    offset_event_record_types = property(fget=get_offset_event_record_types)

    @abc.abstractmethod
    def supports_offset_event_record_type(self, offset_event_record_type):
        """Tests if the given ``OffsetEvent`` record type is supported.

        :param offset_event_record_type: a ``Type`` indicating a ``OffsetEvent`` record type
        :type offset_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_offset_event_search_record_types(self):
        """Gets the supported ``OffsetEvent`` search record types.

        :return: a list containing the supported ``OffsetEvent`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    offset_event_search_record_types = property(fget=get_offset_event_search_record_types)

    @abc.abstractmethod
    def supports_offset_event_search_record_type(self, offset_event_search_record_type):
        """Tests if the given ``OffsetEvent`` search record type is supported.

        :param offset_event_search_record_type: a ``Type`` indicating a ``OffsetEvent`` search record type
        :type offset_event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``offset_event_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_schedule_record_types(self):
        """Gets the supported ``Schedule`` record types.

        :return: a list containing the supported ``Schedule`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    schedule_record_types = property(fget=get_schedule_record_types)

    @abc.abstractmethod
    def supports_schedule_record_type(self, schedule_record_type):
        """Tests if the given ``Schedule`` record type is supported.

        :param schedule_record_type: a ``Type`` indicating a ``Schedule`` record type
        :type schedule_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_schedule_search_record_types(self):
        """Gets the supported ``Schedule`` search record types.

        :return: a list containing the supported ``Schedule`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    schedule_search_record_types = property(fget=get_schedule_search_record_types)

    @abc.abstractmethod
    def supports_schedule_search_record_type(self, schedule_search_record_type):
        """Tests if the given ``Schedule`` search record type is supported.

        :param schedule_search_record_type: a ``Type`` indicating a ``Schedule`` search record type
        :type schedule_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_schedule_slot_record_types(self):
        """Gets the supported ``ScheduleSlot`` record types.

        :return: a list containing the supported ``ScheduleSlot`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    schedule_slot_record_types = property(fget=get_schedule_slot_record_types)

    @abc.abstractmethod
    def supports_schedule_slot_record_type(self, schedule_slot_record_type):
        """Tests if the given ``ScheduleSlot`` record type is supported.

        :param schedule_slot_record_type: a ``Type`` indicating a ``ScheduleSlot`` record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_schedule_slot_search_record_types(self):
        """Gets the supported ``ScheduleSlot`` search record types.

        :return: a list containing the supported ``ScheduleSlot`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    schedule_slot_search_record_types = property(fget=get_schedule_slot_search_record_types)

    @abc.abstractmethod
    def supports_schedule_slot_search_record_type(self, schedule_slot_search_record_type):
        """Tests if the given ``ScheduleSlot`` search record type is supported.

        :param schedule_slot_search_record_type: a ``Type`` indicating a ``ScheduleSlot`` search record type
        :type schedule_slot_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_time_period_record_types(self):
        """Gets the supported ``TimePeriod`` record types.

        :return: a list containing the supported ``TimePeriod`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    time_period_record_types = property(fget=get_time_period_record_types)

    @abc.abstractmethod
    def supports_time_period_record_type(self, time_period_record_type):
        """Tests if the given ``TimePeriod`` record type is supported.

        :param time_period_record_type: a ``Type`` indicating a ``TimePeriod`` record type
        :type time_period_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_time_period_search_record_types(self):
        """Gets the supported ``TimePeriod`` search record types.

        :return: a list containing the supported ``TimePeriod`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    time_period_search_record_types = property(fget=get_time_period_search_record_types)

    @abc.abstractmethod
    def supports_time_period_search_record_type(self, time_period_search_record_type):
        """Tests if the given ``TimePeriod`` search record type is supported.

        :param time_period_search_record_type: a ``Type`` indicating a ``TimePeriod`` search record type
        :type time_period_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_commitment_record_types(self):
        """Gets the supported ``Commitment`` record types.

        :return: a list containing the supported ``Commitment`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    commitment_record_types = property(fget=get_commitment_record_types)

    @abc.abstractmethod
    def supports_commitment_record_type(self, commitment_record_type):
        """Tests if the given ``Commitment`` record type is supported.

        :param commitment_record_type: a ``Type`` indicating a ``Commitment`` type
        :type commitment_record_type: ``osid.type.Type``
        :return: ``true`` if the given commitment record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_commitment_search_record_types(self):
        """Gets the supported commitment search record types.

        :return: a list containing the supported ``Commitment`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    commitment_search_record_types = property(fget=get_commitment_search_record_types)

    @abc.abstractmethod
    def supports_commitment_search_record_type(self, commitment_search_record_type):
        """Tests if the given commitment search record type is supported.

        :param commitment_search_record_type: a ``Type`` indicating a ``Commitment`` search record type
        :type commitment_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_calendar_record_types(self):
        """Gets the supported ``Calendar`` record types.

        :return: a list containing the supported ``Calendar`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    calendar_record_types = property(fget=get_calendar_record_types)

    @abc.abstractmethod
    def supports_calendar_record_type(self, calendar_record_type):
        """Tests if the given ``Calendar`` record type is supported.

        :param calendar_record_type: a ``Type`` indicating a ``Calendar`` type
        :type calendar_record_type: ``osid.type.Type``
        :return: ``true`` if the given calendar record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_calendar_search_record_types(self):
        """Gets the supported calendar search record types.

        :return: a list containing the supported ``Calendar`` search record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    calendar_search_record_types = property(fget=get_calendar_search_record_types)

    @abc.abstractmethod
    def supports_calendar_search_record_type(self, calendar_search_record_type):
        """Tests if the given calendar search record type is supported.

        :param calendar_search_record_type: a ``Type`` indicating a ``Calendar`` search record type
        :type calendar_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_spatial_unit_record_types(self):
        """Gets all the spatial unit record types supported.

        :return: the list of supported spatial unit record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    @abc.abstractmethod
    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if a given spatial unit record type is supported.

        :param spatial_unit_record_type: the spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the spatial unit record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_coordinate_record_types(self):
        """Gets all the coordinate record types supported.

        :return: the list of supported coordinate record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    coordinate_record_types = property(fget=get_coordinate_record_types)

    @abc.abstractmethod
    def supports_coordinate_record_type(self, coordinate_record_type):
        """Tests if a given coordinate record type is supported.

        :param coordinate_record_type: the coordinate domain type
        :type coordinate_record_type: ``osid.type.Type``
        :return: ``true`` if the coordinate record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class CalendaringManager:
    """The calendaring manager provides access to calendaring sessions and provides interoperability tests for various aspects
        of this service.

    The sessions included in this manager are:

      * ``EventLookupSession:`` a session to look up events
      * ``EventQuerySession:`` a session to query events ``None``
      * ``EventSearchSession:`` a session to search events
      * ``EventAdminSession:`` a session to manage events ``None``
      * ``EventNotificationSession: a`` session to receive messages
        pertaining to event ```` changes
      * ``EventCalendarSession:`` a session for retriieving event and
        calendar mappings
      * ``EventCalendarAssignmentSession:`` a session for managing event
        and calendar mappings
      * ``EventSmartCalendarSession:`` a session to manage dynamic event
        catalogs
      * ``RecurringEventLookupSession:`` a session to look up recurring
        events
      * ``RecurringEventQuerySession:`` a session to query recurring
        events
      * ``RecurringEventSearchSession:`` a session to search recurring
        events
      * ``RecurringEventAdminSession:`` a session to create, modify and
        delete recurring event
      * ``RecurringEventNotificationSession:`` a session to receive
        messages pertaining to recurring event changes
      * ``RecurringEventCalendarSession:`` a session for retriieving
        recurring event and calendar mappings
      * ``RecurringEventCalendarAssignmentSession:`` a session for
        managing recurring event and calendar mappings
      * ``RecurringEventSmartCalendarSession:`` a session to manage
        dynamic recurring event catalogs

      * ``SupersedingEventLookupSession:`` a session to look up
        superseding events
      * ``SupersedingEventQuerySession:`` a session to query superseding
        events ``None``
      * ``SupersedingEventSearchSession:`` a session to search
        superseding events
      * ``SupersedingEventAdminSession:`` a session to create, modify
        and delete superseding events ``None``
      * ``SupersedingEventNotificationSession: a`` session to receive
        messages pertaining to superseding event ```` changes
      * ``SupersedingEventCalendarSession:`` a session for retriieving
        superseding event and calendar mappings
      * ``SupersedingEventCalendarAssignmentSession:`` a session for
        managing superseding event and calendar mappings
      * ``SupersedingEventSmartCalendarSession:`` a session to manage
        dynamic superseding event catalogs
      * ``OffsetEventLookupSession:`` a session to look up offset events
      * ``OffsetEventQuerySession:`` a session to query offset events
      * ``OffsetEventSearchSession:`` a session to search offset events
      * ``OffsetEventAdminSession:`` a session to create, modify and
        delete offset events
      * ``OffsetEventNotificationSession:`` a session to receive
        messages pertaining to offset event changes
      * ``OffsetEventCalendarSession:`` a session for retriieving offset
        event and calendar mappings
      * ``OffsetEventCalendarAssignmentSession:`` a session for managing
        offset event and calendar mappings
      * ``OffsetEventSmartCalendarSession:`` a session to manage dynamic
        offset event catalogs

      * ``ScheduleLookupSession:`` a session to look up schedules
      * ``ScheduleQuerySession:`` a session to query schedules ``None``
      * ``ScheduleSearchSession:`` a session to search schedules
      * ``ScheduleAdminSession:`` a session to create, modify and delete
        schedules ``None``
      * ``ScheduleNotificationSession: a`` session to receive messages
        pertaining to schedule ```` changes
      * ``ScheduleCalendarSession:`` a session for retriieving schedule
        and calendar mappings
      * ``ScheduleCalendarAssignmentSession:`` a session for managing
        schedule and calendar mappings
      * ``ScheduleSmartCalendarSession:`` a session to manage dynamic
        schedule catalogs
      * ``ScheduleSlotLookupSession:`` a session to look up schedule
        slots
      * ``ScheduleSlotQuerySession:`` a session to query schedule slots
      * ``ScheduleSlotSearchSession:`` a session to search scheduls
        slots
      * ``ScheduleSlotAdminSession:`` a session to create, modify and
        delete schedule slots
      * ``ScheduleSlotNotificationSession:`` a session to receive
        messages pertaining to schedule slot changes
      * ``ScheduleSlotCalendarSession:`` a session for retriieving
        schedule slot and calendar mappings
      * ``ScheduleSlotCalendarAssignmentSession:`` a session for
        managing schedule slot and calendar mappings
      * ``ScheduleSlotSmartCalendarSession:`` a session to manage
        dynamic schedule slot catalogs

      * ``CommitmentLookupSession:`` a session to look up commitments
      * ``CommitmentQuerySession:`` a session to query commitments
        ``None``
      * ``CommitmentSearchSession:`` a session to search commitments
      * ``CommitmentAdminSession:`` a session to create, modify and
        delete commitments ``None``
      * ``CommitmentNotificationSession: a`` session to receive messages
        pertaining to commitment changes
      * ``CommitmentCalendarSession:`` a session for retriieving
        commitment and calendar mappings
      * ``CommitmentCalendarAssignmentSession:`` a session for managing
        commitment and calendar mappings
      * ``CommitmentSmartCalendarSession:`` a session to manage dynamic
        commitment catalogs

      * ``TimePeriodLookupSession:`` a session to look up time periods
      * ``TimePeriodQuerySession:`` a session to query time periods
        ``None``
      * ``TimePeriodSearchSession:`` a session to search time periods
      * ``TimePeriodAdminSession:`` a session to create, modify and
        delete time periods ``None``
      * ``TimePeriodNotificationSession: a`` session to receive messages
        pertaining to time period ```` changes
      * ``TimePeriodCalendarSession:`` a session for retriieving time
        period and calendar mappings
      * ``TimePeriodCalendarAssignmentSession:`` a session for managing
        time period and calendar mappings
      * ``TimePeriodSmartCalendarSession:`` a session to manage dynamic
        time period catalogs

      * ``CalendarLookupSession:`` a session to lookup calendars
      * ``CalendarSearchSession`` : a session to search calendars
      * ``CalendarAdminSession`` : a session to create, modify and
        delete calendars
      * ``CalendarNotificationSession`` : a session to receive messages
        pertaining to calendar changes
      * ``CalendarHierarchySession:`` a session to traverse the calendar
        hierarchy
      * ``CalendarHierarchyDesignSession:`` a session to manage the
        calendar hierarchy

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the event lookup service.

        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.EventLookupSession

    event_lookup_session = property(fget=get_event_lookup_session)

    @abc.abstractmethod
    def get_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.EventLookupSession

    @abc.abstractmethod
    def get_event_query_session(self):
        """Gets the ``OsidSession`` associated with the event query service.

        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.EventQuerySession

    event_query_session = property(fget=get_event_query_session)

    @abc.abstractmethod
    def get_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.calendaring.EventQuerySession

    @abc.abstractmethod
    def get_event_search_session(self):
        """Gets the ``OsidSession`` associated with the event search service.

        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchSession

    event_search_session = property(fget=get_event_search_session)

    @abc.abstractmethod
    def get_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.EventSearchSession

    @abc.abstractmethod
    def get_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the event administration service.

        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.EventAdminSession

    event_admin_session = property(fget=get_event_admin_session)

    @abc.abstractmethod
    def get_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.calendaring.EventAdminSession

    @abc.abstractmethod
    def get_event_notification_session(self, event_receiver):
        """Gets the notification session for notifications pertaining to event changes.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :return: an ``EventNotificationSession``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NullArgument`` -- ``event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.EventNotificationSession

    @abc.abstractmethod
    def get_event_notification_session_for_calendar(self, event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the event notification service for the given calendar.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventNotificationSession``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.EventNotificationSession

    @abc.abstractmethod
    def get_event_calendar_session(self):
        """Gets the session for retrieving event to calendar mappings.

        :return: an ``EventCalendarSession``
        :rtype: ``osid.calendaring.EventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.EventCalendarSession

    event_calendar_session = property(fget=get_event_calendar_session)

    @abc.abstractmethod
    def get_event_calendar_assignment_session(self):
        """Gets the session for assigning event to calendar mappings.

        :return: an ``EventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.EventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.EventCalendarAssignmentSession

    event_calendar_assignment_session = property(fget=get_event_calendar_assignment_session)

    @abc.abstractmethod
    def get_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventSmartCalendarSession``
        :rtype: ``osid.calendaring.EventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.EventSmartCalendarSession

    @abc.abstractmethod
    def get_recurring_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the recurring event lookup service.

        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventLookupSession

    recurring_event_lookup_session = property(fget=get_recurring_event_lookup_session)

    @abc.abstractmethod
    def get_recurring_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventLookupSession

    @abc.abstractmethod
    def get_recurring_event_query_session(self):
        """Gets the ``OsidSession`` associated with the recurring event query service.

        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventQuerySession

    recurring_event_query_session = property(fget=get_recurring_event_query_session)

    @abc.abstractmethod
    def get_recurring_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventQuerySession

    @abc.abstractmethod
    def get_recurring_event_search_session(self):
        """Gets the ``OsidSession`` associated with the recurring event search service.

        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventSearchSession

    recurring_event_search_session = property(fget=get_recurring_event_search_session)

    @abc.abstractmethod
    def get_recurring_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventSearchSession

    @abc.abstractmethod
    def get_recurring_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the recurring event administration service.

        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventAdminSession

    recurring_event_admin_session = property(fget=get_recurring_event_admin_session)

    @abc.abstractmethod
    def get_recurring_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventAdminSession

    @abc.abstractmethod
    def get_recurring_event_notification_session(self, recurring_event_receiver):
        """Gets the notification session for notifications pertaining to recurring event changes.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NullArgument`` -- ``recurring_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventNotificationSession

    @abc.abstractmethod
    def get_recurring_event_notification_session_for_calendar(self, recurring_event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event notification service for the given calendar.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventNotificationSession

    @abc.abstractmethod
    def get_recurring_event_calendar_session(self):
        """Gets the session for retrieving recurring event to calendar mappings.

        :return: A ``RecurringEventCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventCalendarSession

    recurring_event_calendar_session = property(fget=get_recurring_event_calendar_session)

    @abc.abstractmethod
    def get_recurring_event_calendar_assignment_session(self):
        """Gets the session for assigning recurring event to calendar mappings.

        :return: a ``RecurringEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventCalendarAssignmentSession

    recurring_event_calendar_assignment_session = property(fget=get_recurring_event_calendar_assignment_session)

    @abc.abstractmethod
    def get_recurring_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the recurring event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventSmartCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventSmartCalendarSession

    @abc.abstractmethod
    def get_superseding_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the superseding event lookup service.

        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventLookupSession

    superseding_event_lookup_session = property(fget=get_superseding_event_lookup_session)

    @abc.abstractmethod
    def get_superseding_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventLookupSession

    @abc.abstractmethod
    def get_superseding_event_query_session(self):
        """Gets the ``OsidSession`` associated with the superseding event query service.

        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventQuerySession

    superseding_event_query_session = property(fget=get_superseding_event_query_session)

    @abc.abstractmethod
    def get_superseding_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventQuerySession

    @abc.abstractmethod
    def get_superseding_event_search_session(self):
        """Gets the ``OsidSession`` associated with the superseding event search service.

        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSearchSession

    superseding_event_search_session = property(fget=get_superseding_event_search_session)

    @abc.abstractmethod
    def get_superseding_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSearchSession

    @abc.abstractmethod
    def get_superseding_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the superseding event administration service.

        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventAdminSession

    superseding_event_admin_session = property(fget=get_superseding_event_admin_session)

    @abc.abstractmethod
    def get_superseding_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventAdminSession

    @abc.abstractmethod
    def get_superseding_event_notification_session(self, superseding_event_receiver):
        """Gets the notification session for notifications pertaining to superseding event changes.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NullArgument`` -- ``superseding_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventNotificationSession

    @abc.abstractmethod
    def get_superseding_event_notification_session_for_calendar(self, superseding_event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event notification service for the given calendar.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` or ``supports_visible_federation()``
        is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventNotificationSession

    @abc.abstractmethod
    def get_superseding_event_calendar_session(self):
        """Gets the session for retrieving superseding event to calendar mappings.

        :return: a ``SupersedingEventCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventCalendarSession

    superseding_event_calendar_session = property(fget=get_superseding_event_calendar_session)

    @abc.abstractmethod
    def get_superseding_event_calendar_assignment_session(self):
        """Gets the session for assigning superseding event to calendar mappings.

        :return: a ``SupersedingEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_calendar_assignment()`` is
        ``true``.*

        """
        return  # osid.calendaring.SupersedingEventCalendarAssignmentSession

    superseding_event_calendar_assignment_session = property(fget=get_superseding_event_calendar_assignment_session)

    @abc.abstractmethod
    def get_superseding_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the superseding event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventSmartCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSmartCalendarSession

    @abc.abstractmethod
    def get_offset_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the offset event lookup service.

        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventLookupSession

    offset_event_lookup_session = property(fget=get_offset_event_lookup_session)

    @abc.abstractmethod
    def get_offset_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventLookupSession

    @abc.abstractmethod
    def get_offset_event_query_session(self):
        """Gets the ``OsidSession`` associated with the offset event query service.

        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventQuerySession

    offset_event_query_session = property(fget=get_offset_event_query_session)

    @abc.abstractmethod
    def get_offset_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventQuerySession

    @abc.abstractmethod
    def get_offset_event_search_session(self):
        """Gets the ``OsidSession`` associated with the offset event search service.

        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventSearchSession

    offset_event_search_session = property(fget=get_offset_event_search_session)

    @abc.abstractmethod
    def get_offset_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventSearchSession

    @abc.abstractmethod
    def get_offset_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the offset event administration service.

        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventAdminSession

    offset_event_admin_session = property(fget=get_offset_event_admin_session)

    @abc.abstractmethod
    def get_offset_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventAdminSession

    @abc.abstractmethod
    def get_offset_event_notification_session(self, offset_event_receiver):
        """Gets the notification session for notifications pertaining to offset event changes.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NullArgument`` -- ``offset_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventNotificationSession

    @abc.abstractmethod
    def get_offset_event_notification_session_for_calendar(self, offset_event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event notification service for the given calendar.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventNotificationSession

    @abc.abstractmethod
    def get_offset_event_calendar_session(self):
        """Gets the session for retrieving offset event to calendar mappings.

        :return: an ``OffsetEventCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventCalendarSession

    offset_event_calendar_session = property(fget=get_offset_event_calendar_session)

    @abc.abstractmethod
    def get_offset_event_calendar_assignment_session(self):
        """Gets the session for assigning offset event to calendar mappings.

        :return: an ``OffsetEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventCalendarAssignmentSession

    offset_event_calendar_assignment_session = property(fget=get_offset_event_calendar_assignment_session)

    @abc.abstractmethod
    def get_offset_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the offset event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventSmartCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventSmartCalendarSession

    @abc.abstractmethod
    def get_schedule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the schedule lookup service.

        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleLookupSession

    schedule_lookup_session = property(fget=get_schedule_lookup_session)

    @abc.abstractmethod
    def get_schedule_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleLookupSession

    @abc.abstractmethod
    def get_schedule_query_session(self):
        """Gets the ``OsidSession`` associated with the schedule query service.

        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_query()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleQuerySession

    schedule_query_session = property(fget=get_schedule_query_session)

    @abc.abstractmethod
    def get_schedule_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleQuerySession

    @abc.abstractmethod
    def get_schedule_search_session(self):
        """Gets the ``OsidSession`` associated with the schedule search service.

        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_search()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSearchSession

    schedule_search_session = property(fget=get_schedule_search_session)

    @abc.abstractmethod
    def get_schedule_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSearchSession

    @abc.abstractmethod
    def get_schedule_admin_session(self):
        """Gets the ``OsidSession`` associated with the schedule administration service.

        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_admin()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleAdminSession

    schedule_admin_session = property(fget=get_schedule_admin_session)

    @abc.abstractmethod
    def get_schedule_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleAdminSession

    @abc.abstractmethod
    def get_schedule_notification_session(self, schedule_receiver):
        """Gets the notification session for notifications pertaining to schedule changes.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_notification()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleNotificationSession

    @abc.abstractmethod
    def get_schedule_notification_session_for_calendar(self, schedule_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule notification service for the given calendar.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleNotificationSession

    @abc.abstractmethod
    def get_schedule_calendar_session(self):
        """Gets the session for retrieving schedule to calendar mappings.

        :return: a ``ScheduleCalendarSession``
        :rtype: ``osid.calendaring.ScheduleCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleCalendarSession

    schedule_calendar_session = property(fget=get_schedule_calendar_session)

    @abc.abstractmethod
    def get_schedule_calendar_assignment_session(self):
        """Gets the session for assigning schedule to calendar mappings.

        :return: a ``ScheduleCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleCalendarAssignmentSession

    schedule_calendar_assignment_session = property(fget=get_schedule_calendar_assignment_session)

    @abc.abstractmethod
    def get_schedule_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the schedule smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSmartCalendarSession

    @abc.abstractmethod
    def get_schedule_slot_lookup_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service.

        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotLookupSession

    schedule_slot_lookup_session = property(fget=get_schedule_slot_lookup_session)

    @abc.abstractmethod
    def get_schedule_slot_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotLookupSession

    @abc.abstractmethod
    def get_schedule_slot_query_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot query service.

        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_query()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotQuerySession

    schedule_slot_query_session = property(fget=get_schedule_slot_query_session)

    @abc.abstractmethod
    def get_schedule_slot_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotQuerySession

    @abc.abstractmethod
    def get_schedule_slot_search_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot search service.

        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_search()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSearchSession

    schedule_slot_search_session = property(fget=get_schedule_slot_search_session)

    @abc.abstractmethod
    def get_schedule_slot_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSearchSession

    @abc.abstractmethod
    def get_schedule_slot_admin_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot administration service.

        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_admin()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotAdminSession

    schedule_slot_admin_session = property(fget=get_schedule_slot_admin_session)

    @abc.abstractmethod
    def get_schedule_slot_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotAdminSession

    @abc.abstractmethod
    def get_schedule_slot_notification_session(self, schedule_slot_receiver):
        """Gets the notification session for notifications pertaining to schedule slot changes.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_slot_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_notification()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotNotificationSession

    @abc.abstractmethod
    def get_schedule_slot_notification_session_for_calendar(self, schedule_slot_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot notification service for the given calendar.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotNotificationSession

    @abc.abstractmethod
    def get_schedule_slot_calendar_session(self):
        """Gets the session for retrieving schedule slot to calendar mappings.

        :return: a ``ScheduleSlotCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotCalendarSession

    schedule_slot_calendar_session = property(fget=get_schedule_slot_calendar_session)

    @abc.abstractmethod
    def get_schedule_slot_calendar_assignment_session(self):
        """Gets the session for assigning schedule slot to calendar mappings.

        :return: a ``ScheduleSlotCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotCalendarAssignmentSession

    schedule_slot_calendar_assignment_session = property(fget=get_schedule_slot_calendar_assignment_session)

    @abc.abstractmethod
    def get_schedule_slot_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the schedule slot smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSmartCalendarSession

    @abc.abstractmethod
    def get_commitment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the commitment lookup service.

        :return: a ``CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentLookupSession

    commitment_lookup_session = property(fget=get_commitment_lookup_session)

    @abc.abstractmethod
    def get_commitment_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentLookupSession

    @abc.abstractmethod
    def get_commitment_query_session(self):
        """Gets the ``OsidSession`` associated with the commitment query service.

        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentQuerySession

    commitment_query_session = property(fget=get_commitment_query_session)

    @abc.abstractmethod
    def get_commitment_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentQuerySession

    @abc.abstractmethod
    def get_commitment_search_session(self):
        """Gets the ``OsidSession`` associated with the commitment search service.

        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_search()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentSearchSession

    commitment_search_session = property(fget=get_commitment_search_session)

    @abc.abstractmethod
    def get_commitment_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentSearchSession

    @abc.abstractmethod
    def get_commitment_admin_session(self):
        """Gets the ``OsidSession`` associated with the commitment administration service.

        :return: a ``CommitmentAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_admin()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentAdminSession

    commitment_admin_session = property(fget=get_commitment_admin_session)

    @abc.abstractmethod
    def get_commitment_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmenttAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentAdminSession

    @abc.abstractmethod
    def get_commitment_notification_session(self, commitment_receiver):
        """Gets the notification session for notifications pertaining to commitment changes.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NullArgument`` -- ``commitment_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_notification()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentNotificationSession

    @abc.abstractmethod
    def get_commitment_notification_session_for_calendar(self, commitment_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment notification service for the given calendar.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``commitment_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentNotificationSession

    @abc.abstractmethod
    def get_commitment_calendar_session(self):
        """Gets the session for retrieving commitment to calendar mappings.

        :return: a ``CommitmentCalendarSession``
        :rtype: ``osid.calendaring.CommitmentCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentCalendarSession

    commitment_calendar_session = property(fget=get_commitment_calendar_session)

    @abc.abstractmethod
    def get_commitment_calendar_assignment_session(self):
        """Gets the session for assigning commitment to calendar mappings.

        :return: a ``CommitmentCalendarAssignmentSession``
        :rtype: ``osid.calendaring.CommitmentCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentCalendarAssignmentSession

    commitment_calendar_assignment_session = property(fget=get_commitment_calendar_assignment_session)

    @abc.abstractmethod
    def get_commitment_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the commitment smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentSmartCalendarSession``
        :rtype: ``osid.calendaring.CommitmentSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentSmartCalendarSession

    @abc.abstractmethod
    def get_time_period_lookup_session(self):
        """Gets the ``OsidSession`` associated with the time period lookup service.

        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodLookupSession

    time_period_lookup_session = property(fget=get_time_period_lookup_session)

    @abc.abstractmethod
    def get_time_period_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodLookupSession

    @abc.abstractmethod
    def get_time_period_query_session(self):
        """Gets the ``OsidSession`` associated with the time period query service.

        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_query()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodQuerySession

    time_period_query_session = property(fget=get_time_period_query_session)

    @abc.abstractmethod
    def get_time_period_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodQuerySession

    @abc.abstractmethod
    def get_time_period_search_session(self):
        """Gets the ``OsidSession`` associated with the time period search service.

        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_search()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodSearchSession

    time_period_search_session = property(fget=get_time_period_search_session)

    @abc.abstractmethod
    def get_time_period_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodSearchSession

    @abc.abstractmethod
    def get_time_period_admin_session(self):
        """Gets the ``OsidSession`` associated with the time period administration service.

        :return: a ``TimePeriodAdminSession``
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_admin()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodAdminSession

    time_period_admin_session = property(fget=get_time_period_admin_session)

    @abc.abstractmethod
    def get_time_period_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodAdminSession``
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodAdminSession

    @abc.abstractmethod
    def get_time_period_notification_session(self, time_period_receiver):
        """Gets the notification session for notifications pertaining to time period changes.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :return: a ``TimePeriodNotificationSession``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NullArgument`` -- ``time_period_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_notification()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodNotificationSession

    @abc.abstractmethod
    def get_time_period_notification_session_for_calendar(self, time_period_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the time period notification service for the given calendar.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``a _time_period_notification_session``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``time_period_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodNotificationSession

    @abc.abstractmethod
    def get_time_period_calendar_session(self):
        """Gets the session for retrieving time period to calendar mappings.

        :return: a ``TimePeriodCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodCalendarSession

    time_period_calendar_session = property(fget=get_time_period_calendar_session)

    @abc.abstractmethod
    def get_time_period_calendar_assignment_session(self):
        """Gets the session for assigning time period to calendar mappings.

        :return: a ``TimePeriodCalendarAssignmentSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodCalendarAssignmentSession

    time_period_calendar_assignment_session = property(fget=get_time_period_calendar_assignment_session)

    @abc.abstractmethod
    def get_time_period_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the time period smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodSmartCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodSmartCalendarSession

    @abc.abstractmethod
    def get_calendar_lookup_session(self):
        """Gets the OsidSession associated with the calendar lookup service.

        :return: a ``CalendarLookupSession``
        :rtype: ``osid.calendaring.CalendarLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_lookup()`` is true.*

        """
        return  # osid.calendaring.CalendarLookupSession

    calendar_lookup_session = property(fget=get_calendar_lookup_session)

    @abc.abstractmethod
    def get_calendar_search_session(self):
        """Gets the OsidSession associated with the calendar search service.

        :return: a ``CalendarSearchSession``
        :rtype: ``osid.calendaring.CalendarSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_search()`` is true.*

        """
        return  # osid.calendaring.CalendarSearchSession

    calendar_search_session = property(fget=get_calendar_search_session)

    @abc.abstractmethod
    def get_calendar_admin_session(self):
        """Gets the OsidSession associated with the calendar administration service.

        :return: a ``CalendarAdminSession``
        :rtype: ``osid.calendaring.CalendarAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_admin()`` is true.*

        """
        return  # osid.calendaring.CalendarAdminSession

    calendar_admin_session = property(fget=get_calendar_admin_session)

    @abc.abstractmethod
    def get_calendar_notification_session(self, calendar_receiver):
        """Gets the notification session for notifications pertaining to calendar service changes.

        :param calendar_receiver: the calendar receiver
        :type calendar_receiver: ``osid.calendaring.CalendarReceiver``
        :return: a ``CalendarNotificationSession``
        :rtype: ``osid.calendaring.CalendarNotificationSession``
        :raise: ``NullArgument`` -- ``calendar_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_notification()`` is true.*

        """
        return  # osid.calendaring.CalendarNotificationSession

    @abc.abstractmethod
    def get_calendar_hierarchy_session(self):
        """Gets the session traversing calendar hierarchies.

        :return: a ``CalendarHierarchySession``
        :rtype: ``osid.calendaring.CalendarHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_hierarchy()`` is true.*

        """
        return  # osid.calendaring.CalendarHierarchySession

    calendar_hierarchy_session = property(fget=get_calendar_hierarchy_session)

    @abc.abstractmethod
    def get_calendar_hierarchy_design_session(self):
        """Gets the session designing calendar hierarchies.

        :return: a ``CalendarHierarchyDesignSession``
        :rtype: ``osid.calendaring.CalendarHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_hierarchy_design()`` is true.*

        """
        return  # osid.calendaring.CalendarHierarchyDesignSession

    calendar_hierarchy_design_session = property(fget=get_calendar_hierarchy_design_session)

    @abc.abstractmethod
    def get_calandaring_batch_manager(self):
        """Gets the calendaring batch manager.

        :return: a ``CalendaringBatchManager``
        :rtype: ``osid.calendaring.batch.CalendaringBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendaring_batch()`` is ``true``.*

        """
        return  # osid.calendaring.batch.CalendaringBatchManager

    calandaring_batch_manager = property(fget=get_calandaring_batch_manager)

    @abc.abstractmethod
    def get_calandaring_cycle_manager(self):
        """Gets the calendaring cycle manager.

        :return: a ``CalendaringCycleManager``
        :rtype: ``osid.calendaring.cycle.CalendaringCycleManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_cycle()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendaring_cycle()`` is ``true``.*

        """
        return  # osid.calendaring.cycle.CalendaringCycleManager

    calandaring_cycle_manager = property(fget=get_calandaring_cycle_manager)

    @abc.abstractmethod
    def get_calandaring_rules_manager(self):
        """Gets the calendaring rules manager.

        :return: a ``CalendaringRulesManager``
        :rtype: ``osid.calendaring.rules.CalendaringRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendaring_rules()`` is ``true``.*

        """
        return  # osid.calendaring.rules.CalendaringRulesManager

    calandaring_rules_manager = property(fget=get_calandaring_rules_manager)


class CalendaringProxyManager:
    """The calendaring manager provides access to calendaring sessions and provides interoperability tests for various aspects
        of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``EventLookupSession:`` a session to look up events
      * ``EventQuerySession:`` a session to query events ``None``
      * ``EventSearchSession:`` a session to search events
      * ``EventAdminSession:`` a session to create, modify and delete
        events ``None``
      * ``EventNotificationSession: a`` session to receive messages
        pertaining to event ```` changes
      * ``EventCalendarSession:`` a session for retriieving event and
        calendar mappings
      * ``EventCalendarAssignmentSession:`` a session for managing event
        and calendar mappings
      * ``EventSmartCalendarSession:`` a session to manage dynamic event
        catalogs
      * ``RecurringEventLookupSession:`` a session to look up recurring
        events
      * ``RecurringEventQuerySession:`` a session to query recurring
        events
      * ``RecurringEventSearchSession:`` a session to search recurring
        events
      * ``RecurringEventAdminSession:`` a session to create, modify and
        delete recurring events
      * ``RecurringEventNotificationSession:`` a session to receive
        messages pertaining to recurring event changes
      * ``RecurringEventCalendarSession:`` a session for retriieving
        recurring event and calendar mappings
      * ``RecurringEventCalendarAssignmentSession:`` a session for
        managing recurring event and calendar mappings
      * ``RecurringEventSmartCalendarSession:`` a session to manage
        dynamic recurring event catalogs

      * ``SupersedingEventLookupSession:`` a session to look up
        superseding events
      * ``SupersedingEventQuerySession:`` a session to query superseding
        events ``None``
      * ``SupersedingEventSearchSession:`` a session to search
        superseding events
      * ``SupersedingEventAdminSession:`` a session to create, modify
        and delete superseding events ``None``
      * ``SupersedingEventNotificationSession: a`` session to receive
        messages pertaining to superseding event ```` changes
      * ``SupersedingEventCalendarSession:`` a session for retriieving
        superseding event and calendar mappings
      * ``SupersedingEventCalendarAssignmentSession:`` a session for
        managing superseding event and calendar mappings
      * ``SupersedingEventSmartCalendarSession:`` a session to manage
        dynamic superseding event catalogs
      * ``OffsetEventLookupSession:`` a session to look up offset events
      * ``OffsetEventQuerySession:`` a session to query offset events
      * ``OffsetEventSearchSession:`` a session to search offset events
      * ``OffsetEventAdminSession:`` a session to create, modify and
        delete offset events
      * ``OffsetEventNotificationSession:`` a session to receive
        messages pertaining to offset event changes
      * ``OffsetEventCalendarSession:`` a session for retriieving offset
        event and calendar mappings
      * ``OffsetEventCalendarAssignmentSession:`` a session for managing
        offset event and calendar mappings
      * ``OffsetEventSmartCalendarSession:`` a session to manage dynamic
        offset event catalogs

      * ``ScheduleLookupSession:`` a session to look up schedules
      * ``ScheduleQuerySession:`` a session to query schedules ``None``
      * ``ScheduleSearchSession:`` a session to search schedules
      * ``ScheduleAdminSession:`` a session to create, modify and delete
        schedules ``None``
      * ``ScheduleNotificationSession: a`` session to receive messages
        pertaining to schedule ```` changes
      * ``ScheduleCalendarSession:`` a session for retriieving schedule
        and calendar mappings
      * ``ScheduleCalendarAssignmentSession:`` a session for managing
        schedule and calendar mappings
      * ``ScheduleSmartCalendarSession:`` a session to manage dynamic
        schedule catalogs
      * ``ScheduleSlotLookupSession:`` a session to look up schedule
        slots
      * ``ScheduleSlotQuerySession:`` a session to query schedule slots
      * ``ScheduleSlotSearchSession:`` a session to search scheduls
        slots
      * ``ScheduleSlotAdminSession:`` a session to create, modify and
        delete schedule slots
      * ``ScheduleSlotNotificationSession:`` a session to receive
        messages pertaining to schedule slot changes
      * ``ScheduleSlotCalendarSession:`` a session for retriieving
        schedule slot and calendar mappings
      * ``ScheduleSlotCalendarAssignmentSession:`` a session for
        managing schedule slot and calendar mappings
      * ``ScheduleSlotSmartCalendarSession:`` a session to manage
        dynamic schedule slot catalogs

      * ``CommitmentLookupSession:`` a session to look up commitments
      * ``CommitmentQuerySession:`` a session to query commitments
        ``None``
      * ``CommitmentSearchSession:`` a session to search commitments
      * ``CommitmentAdminSession:`` a session to create, modify and
        delete commitments ``None``
      * ``CommitmentNotificationSession: a`` session to receive messages
        pertaining to commitment changes
      * ``CommitmentCalendarSession:`` a session for retriieving
        commitment and calendar mappings
      * ``CommitmentCalendarAssignmentSession:`` a session for managing
        commitment and calendar mappings
      * ``CommitmentSmartCalendarSession:`` a session to manage dynamic
        commitment catalogs

      * ``TimePeriodLookupSession:`` a session to look up time periods
      * ``TimePeriodQuerySession:`` a session to query time periods
        ``None``
      * ``TimePeriodSearchSession:`` a session to search time periods
      * ``TimePeriodAdminSession:`` a session to create, modify and
        delete time periods ``None``
      * ``TimePeriodNotificationSession: a`` session to receive messages
        pertaining to time period ```` changes
      * ``TimePeriodCalendarSession:`` a session for retriieving time
        period and calendar mappings
      * ``TimePeriodCalendarAssignmentSession:`` a session for managing
        time period and calendar mappings
      * ``TimePeriodSmartCalendarSession:`` a session to manage dynamic
        time period catalogs

      * ``CalendarLookupSession:`` a session to lookup calendars
      * ``CalendarSearchSession`` : a session to search calendars
      * ``CalendarAdminSession`` : a session to create, modify and
        delete calendars
      * ``CalendarNotificationSession`` : a session to receive messages
        pertaining to calendar changes
      * ``CalendarHierarchySession:`` a session to traverse the calendar
        hierarchy
      * ``CalendarHierarchyDesignSession:`` a session to manage the
        calendar hierarchy

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.EventLookupSession

    @abc.abstractmethod
    def get_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.EventLookupSession

    @abc.abstractmethod
    def get_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.EventQuerySession

    @abc.abstractmethod
    def get_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.calendaring.EventQuerySession

    @abc.abstractmethod
    def get_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.EventSearchSession

    @abc.abstractmethod
    def get_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.EventSearchSession

    @abc.abstractmethod
    def get_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.EventAdminSession

    @abc.abstractmethod
    def get_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return  # osid.calendaring.EventAdminSession

    @abc.abstractmethod
    def get_event_notification_session(self, event_receiver, proxy):
        """Gets the notification session for notifications pertaining to event changes.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventNotificationSession``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NullArgument`` -- ``event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.EventNotificationSession

    @abc.abstractmethod
    def get_event_notification_session_for_calendar(self, event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event notification service for the given calendar.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _event_notification_session``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``event_receiver,`` None ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.EventNotificationSession

    @abc.abstractmethod
    def get_event_calendar_session(self, proxy):
        """Gets the session for retrieving event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventCalendarSession``
        :rtype: ``osid.calendaring.EventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.EventCalendarSession

    @abc.abstractmethod
    def get_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.EventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.EventCalendarAssignmentSession

    @abc.abstractmethod
    def get_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventSmartCalendarSession``
        :rtype: ``osid.calendaring.EventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.EventSmartCalendarSession

    @abc.abstractmethod
    def get_recurring_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventLookupSession

    @abc.abstractmethod
    def get_recurring_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventLookupSession

    @abc.abstractmethod
    def get_recurring_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventQuerySession

    @abc.abstractmethod
    def get_recurring_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventQuerySession

    @abc.abstractmethod
    def get_recurring_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventSearchSession

    @abc.abstractmethod
    def get_recurring_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventSearchSession

    @abc.abstractmethod
    def get_recurring_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventAdminSession

    @abc.abstractmethod
    def get_recurring_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventAdminSession

    @abc.abstractmethod
    def get_recurring_event_notification_session(self, recurring_event_receiver, proxy):
        """Gets the notification session for notifications pertaining to recurring event changes.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NullArgument`` -- ``recurring_event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventNotificationSession

    @abc.abstractmethod
    def get_recurring_event_notification_session_for_calendar(self, recurring_event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event notification service for the given calendar.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_receiver,``  ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.RecurringEventNotificationSession

    @abc.abstractmethod
    def get_recurring_event_calendar_session(self, proxy):
        """Gets the session for retrieving recurring event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventCalendarSession

    @abc.abstractmethod
    def get_recurring_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning recurring event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventCalendarAssignmentSession

    @abc.abstractmethod
    def get_recurring_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the recurring event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventSmartCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_recurring_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.RecurringEventSmartCalendarSession

    @abc.abstractmethod
    def get_superseding_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventLookupSession

    @abc.abstractmethod
    def get_superseding_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventLookupSession

    @abc.abstractmethod
    def get_superseding_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventQuerySession

    @abc.abstractmethod
    def get_superseding_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventQuerySession

    @abc.abstractmethod
    def get_superseding_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSearchSession

    @abc.abstractmethod
    def get_superseding_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSearchSession

    @abc.abstractmethod
    def get_superseding_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventAdminSession

    @abc.abstractmethod
    def get_superseding_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventAdminSession

    @abc.abstractmethod
    def get_superseding_event_notification_session(self, superseding_event_receiver, proxy):
        """Gets the notification session for notifications pertaining to superseding event changes.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NullArgument`` -- ``superseding_event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventNotificationSession

    @abc.abstractmethod
    def get_superseding_event_notification_session_for_calendar(self, superseding_event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event notification service for the given calendar.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` or ``supports_visible_federation()``
        is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.SupersedingEventNotificationSession

    @abc.abstractmethod
    def get_superseding_event_calendar_session(self, proxy):
        """Gets the session for retrieving superseding event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventCalendarSession

    @abc.abstractmethod
    def get_superseding_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning superseding event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_calendar_assignment()`` is
        ``true``.*

        """
        return  # osid.calendaring.SupersedingEventCalendarAssignmentSession

    @abc.abstractmethod
    def get_superseding_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the superseding event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventSmartCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_superseding_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.SupersedingEventSmartCalendarSession

    @abc.abstractmethod
    def get_offset_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventLookupSession

    @abc.abstractmethod
    def get_offset_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventLookupSession

    @abc.abstractmethod
    def get_offset_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_query()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventQuerySession

    @abc.abstractmethod
    def get_offset_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventQuerySession

    @abc.abstractmethod
    def get_offset_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_search()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventSearchSession

    @abc.abstractmethod
    def get_offset_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventSearchSession

    @abc.abstractmethod
    def get_offset_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_admin()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventAdminSession

    @abc.abstractmethod
    def get_offset_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventAdminSession

    @abc.abstractmethod
    def get_offset_event_notification_session(self, offset_event_receiver, proxy):
        """Gets the notification session for notifications pertaining to offset event changes.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NullArgument`` -- ``offset_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_notification()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventNotificationSession

    @abc.abstractmethod
    def get_offset_event_notification_session_for_calendar(self, offset_event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event notification service for the given calendar.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.OffsetEventNotificationSession

    @abc.abstractmethod
    def get_offset_event_calendar_session(self, proxy):
        """Gets the session for retrieving offset event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventCalendarSession

    @abc.abstractmethod
    def get_offset_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning offset event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventCalendarAssignmentSession

    @abc.abstractmethod
    def get_offset_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the offset event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventSmartCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_offset_event_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.OffsetEventSmartCalendarSession

    @abc.abstractmethod
    def get_schedule_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleLookupSession

    @abc.abstractmethod
    def get_schedule_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleLookupSession

    @abc.abstractmethod
    def get_schedule_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_query()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleQuerySession

    @abc.abstractmethod
    def get_schedule_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleQuerySession

    @abc.abstractmethod
    def get_schedule_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_search()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSearchSession

    @abc.abstractmethod
    def get_schedule_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSearchSession

    @abc.abstractmethod
    def get_schedule_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_admin()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleAdminSession

    @abc.abstractmethod
    def get_schedule_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleAdminSession

    @abc.abstractmethod
    def get_schedule_notification_session(self, schedule_receiver, proxy):
        """Gets the notification session for notifications pertaining to schedule changes.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_notification()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleNotificationSession

    @abc.abstractmethod
    def get_schedule_notification_session_for_calendar(self, schedule_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule notification service for the given calendar.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleNotificationSession

    @abc.abstractmethod
    def get_schedule_calendar_session(self, proxy):
        """Gets the session for retrieving schedule to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleCalendarSession``
        :rtype: ``osid.calendaring.ScheduleCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleCalendarSession

    @abc.abstractmethod
    def get_schedule_calendar_assignment_session(self, proxy):
        """Gets the session for assigning schedule to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleCalendarAssignmentSession

    @abc.abstractmethod
    def get_schedule_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the schedule smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSmartCalendarSession

    @abc.abstractmethod
    def get_schedule_slot_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotLookupSession

    @abc.abstractmethod
    def get_schedule_slot_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotLookupSession

    @abc.abstractmethod
    def get_schedule_slot_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_query()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotQuerySession

    @abc.abstractmethod
    def get_schedule_slot_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotQuerySession

    @abc.abstractmethod
    def get_schedule_slot_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_search()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSearchSession

    @abc.abstractmethod
    def get_schedule_slot_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSearchSession

    @abc.abstractmethod
    def get_schedule_slot_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_admin()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotAdminSession

    @abc.abstractmethod
    def get_schedule_slot_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotAdminSession

    @abc.abstractmethod
    def get_schedule_slot_notification_session(self, schedule_slot_receiver, proxy):
        """Gets the notification session for notifications pertaining to schedule slot changes.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_slot_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_notification()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotNotificationSession

    @abc.abstractmethod
    def get_schedule_slot_notification_session_for_calendar(self, schedule_slot_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot notification service for the given calendar.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotNotificationSession

    @abc.abstractmethod
    def get_schedule_slot_calendar_session(self, proxy):
        """Gets the session for retrieving schedule slot to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotCalendarSession

    @abc.abstractmethod
    def get_schedule_slot_calendar_assignment_session(self, proxy):
        """Gets the session for assigning schedule slot to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotCalendarAssignmentSession

    @abc.abstractmethod
    def get_schedule_slot_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the schedule slot smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_slot_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.ScheduleSlotSmartCalendarSession

    @abc.abstractmethod
    def get_commitment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentLookupSession

    @abc.abstractmethod
    def get_commitment_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentLookupSession

    @abc.abstractmethod
    def get_commitment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentQuerySession

    @abc.abstractmethod
    def get_commitment_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentQuerySession

    @abc.abstractmethod
    def get_commitment_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_search()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentSearchSession

    @abc.abstractmethod
    def get_commitment_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentSearchSession

    @abc.abstractmethod
    def get_commitment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_admin()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentAdminSession

    @abc.abstractmethod
    def get_commitment_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmenttAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentAdminSession

    @abc.abstractmethod
    def get_commitment_notification_session(self, commitment_receiver, proxy):
        """Gets the notification session for notifications pertaining to commitment changes.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NullArgument`` -- ``commitment_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_notification()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentNotificationSession

    @abc.abstractmethod
    def get_commitment_notification_session_for_calendar(self, commitment_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment notification service for the given calendar.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``commitment_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.CommitmentNotificationSession

    @abc.abstractmethod
    def get_commitment_calendar_session(self, proxy):
        """Gets the session for retrieving commitment to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentCalendarSession``
        :rtype: ``osid.calendaring.CommitmentCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentCalendarSession

    @abc.abstractmethod
    def get_commitment_calendar_assignment_session(self, proxy):
        """Gets the session for assigning commitment to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentCalendarAssignmentSession``
        :rtype: ``osid.calendaring.CommitmentCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentCalendarAssignmentSession

    @abc.abstractmethod
    def get_commitment_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the commitment smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentSmartCalendarSession``
        :rtype: ``osid.calendaring.CommitmentSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commitment_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.CommitmentSmartCalendarSession

    @abc.abstractmethod
    def get_time_period_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_lookup()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodLookupSession

    @abc.abstractmethod
    def get_time_period_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodLookupSession

    @abc.abstractmethod
    def get_time_period_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_query()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodQuerySession

    @abc.abstractmethod
    def get_time_period_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodQuerySession

    @abc.abstractmethod
    def get_time_period_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_search()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodSearchSession

    @abc.abstractmethod
    def get_time_period_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodSearchSession

    @abc.abstractmethod
    def get_time_period_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodAdminSession``
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_admin()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodAdminSession

    @abc.abstractmethod
    def get_time_period_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``calendar_id`` not found
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``NotFound`` -- a ``TimePeriodAdminSession``
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodAdminSession

    @abc.abstractmethod
    def get_time_period_notification_session(self, time_period_receiver, proxy):
        """Gets the notification session for notifications pertaining to time period changes.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodNotificationSession``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NullArgument`` -- ``time_period_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_notification()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodNotificationSession

    @abc.abstractmethod
    def get_time_period_notification_session_for_calendar(self, time_period_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period notification service for the given calendar.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _time_period_notification_session``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``time_period_receiver`` or ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.calendaring.TimePeriodNotificationSession

    @abc.abstractmethod
    def get_time_period_calendar_session(self, proxy):
        """Gets the session for retrieving time period to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodCalendarSession

    @abc.abstractmethod
    def get_time_period_calendar_assignment_session(self, proxy):
        """Gets the session for assigning time period to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodCalendarAssignmentSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_calendar_assignment()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodCalendarAssignmentSession

    @abc.abstractmethod
    def get_time_period_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the time period smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodSmartCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_smart_calendar()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_time_period_smart_calendar()`` is ``true``.*

        """
        return  # osid.calendaring.TimePeriodSmartCalendarSession

    @abc.abstractmethod
    def get_calendar_lookup_session(self, proxy):
        """Gets the OsidSession associated with the calendar lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarLookupSession``
        :rtype: ``osid.calendaring.CalendarLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_lookup()`` is true.*

        """
        return  # osid.calendaring.CalendarLookupSession

    @abc.abstractmethod
    def get_calendar_search_session(self, proxy):
        """Gets the OsidSession associated with the calendar search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarSearchSession``
        :rtype: ``osid.calendaring.CalendarSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_search()`` is true.*

        """
        return  # osid.calendaring.CalendarSearchSession

    @abc.abstractmethod
    def get_calendar_admin_session(self, proxy):
        """Gets the OsidSession associated with the calendar administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarAdminSession``
        :rtype: ``osid.calendaring.CalendarAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_admin()`` is true.*

        """
        return  # osid.calendaring.CalendarAdminSession

    @abc.abstractmethod
    def get_calendar_notification_session(self, calendar_receiver, proxy):
        """Gets the notification session for notifications pertaining to calendar service changes.

        :param calendar_receiver: the calendar receiver
        :type calendar_receiver: ``osid.calendaring.CalendarReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarNotificationSession``
        :rtype: ``osid.calendaring.CalendarNotificationSession``
        :raise: ``NullArgument`` -- ``calendar_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_notification()`` is true.*

        """
        return  # osid.calendaring.CalendarNotificationSession

    @abc.abstractmethod
    def get_calendar_hierarchy_session(self, proxy):
        """Gets the session traversing calendar hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarHierarchySession``
        :rtype: ``osid.calendaring.CalendarHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_hierarchy()`` is true.*

        """
        return  # osid.calendaring.CalendarHierarchySession

    @abc.abstractmethod
    def get_calendar_hierarchy_design_session(self, proxy):
        """Gets the session designing calendar hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarHierarchyDesignSession``
        :rtype: ``osid.calendaring.CalendarHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendar_hierarchy_design()`` is true.*

        """
        return  # osid.calendaring.CalendarHierarchyDesignSession

    @abc.abstractmethod
    def get_calandaring_batch_proxy_manager(self):
        """Gets the calendaring batch proxy manager.

        :return: a ``CalendaringBatchProxyManager``
        :rtype: ``osid.calendaring.batch.CalendaringBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendaring_batch()`` is ``true``.*

        """
        return  # osid.calendaring.batch.CalendaringBatchProxyManager

    calandaring_batch_proxy_manager = property(fget=get_calandaring_batch_proxy_manager)

    @abc.abstractmethod
    def get_calandaring_cycle_proxy_manager(self):
        """Gets the calendaring cycle proxy manager.

        :return: a ``CalendaringCycleProxyManager``
        :rtype: ``osid.calendaring.cycle.CalendaringCycleProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_cycle()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendaring_cycle()`` is ``true``.*

        """
        return  # osid.calendaring.cycle.CalendaringCycleProxyManager

    calandaring_cycle_proxy_manager = property(fget=get_calandaring_cycle_proxy_manager)

    @abc.abstractmethod
    def get_calandaring_rules_proxy_manager(self):
        """Gets the calendaring rules proxy manager.

        :return: a ``CalendaringRulesProxyManager``
        :rtype: ``osid.calendaring.rules.CalendaringRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_calendaring_rules()`` is ``true``.*

        """
        return  # osid.calendaring.rules.CalendaringRulesProxyManager

    calandaring_rules_proxy_manager = property(fget=get_calandaring_rules_proxy_manager)
