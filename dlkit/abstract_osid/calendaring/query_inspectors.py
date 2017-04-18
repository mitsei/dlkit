"""Implementations of calendaring abstract base class query_inspectors."""
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


class EventQueryInspector:
    """This is the query inspector for examining event queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_implicit_terms(self):
        """Gets the implicit terms.

        :return: the implicit terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    implicit_terms = property(fget=get_implicit_terms)

    @abc.abstractmethod
    def get_duration_terms(self):
        """Gets the duration terms.

        :return: the duration terms
        :rtype: ``osid.search.terms.DurationTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationTerm

    duration_terms = property(fget=get_duration_terms)

    @abc.abstractmethod
    def get_recurring_event_id_terms(self):
        """Gets the recurring event ``Id`` terms.

        :return: the recurring event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    recurring_event_id_terms = property(fget=get_recurring_event_id_terms)

    @abc.abstractmethod
    def get_recurring_event_terms(self):
        """Gets the recurring event terms.

        :return: the recurring event terms
        :rtype: ``osid.calendaring.RecurringEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.RecurringEventQueryInspector

    recurring_event_terms = property(fget=get_recurring_event_terms)

    @abc.abstractmethod
    def get_superseding_event_id_terms(self):
        """Gets the superseding event ``Id`` terms.

        :return: the superseding event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    superseding_event_id_terms = property(fget=get_superseding_event_id_terms)

    @abc.abstractmethod
    def get_superseding_event_terms(self):
        """Gets the superseding event terms.

        :return: the superseding event terms
        :rtype: ``osid.calendaring.SupersedingEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.SupersedingEventQueryInspector

    superseding_event_terms = property(fget=get_superseding_event_terms)

    @abc.abstractmethod
    def get_offset_event_id_terms(self):
        """Gets the offset event ``Id`` terms.

        :return: the offset event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    offset_event_id_terms = property(fget=get_offset_event_id_terms)

    @abc.abstractmethod
    def get_offset_event_terms(self):
        """Gets the offset event terms.

        :return: the offset event terms
        :rtype: ``osid.calendaring.OffsetEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.OffsetEventQueryInspector

    offset_event_terms = property(fget=get_offset_event_terms)

    @abc.abstractmethod
    def get_location_description_terms(self):
        """Gets the location description terms.

        :return: the location description terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    location_description_terms = property(fget=get_location_description_terms)

    @abc.abstractmethod
    def get_location_id_terms(self):
        """Gets the location ``Id`` terms.

        :return: the location ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    location_id_terms = property(fget=get_location_id_terms)

    @abc.abstractmethod
    def get_location_terms(self):
        """Gets the location terms.

        :return: the location terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    location_terms = property(fget=get_location_terms)

    @abc.abstractmethod
    def get_sponsor_id_terms(self):
        """Gets the sponsor ``Id`` terms.

        :return: the sponsor ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    sponsor_id_terms = property(fget=get_sponsor_id_terms)

    @abc.abstractmethod
    def get_sponsor_terms(self):
        """Gets the sponsor terms.

        :return: the sponsor terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    sponsor_terms = property(fget=get_sponsor_terms)

    @abc.abstractmethod
    def get_coordinate_terms(self):
        """Gets the coordinate terms.

        :return: the coordinate terms
        :rtype: ``osid.search.terms.CoordinateTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CoordinateTerm

    coordinate_terms = property(fget=get_coordinate_terms)

    @abc.abstractmethod
    def get_spatial_unit_terms(self):
        """Gets the spatial unit terms.

        :return: the spatial unit terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    spatial_unit_terms = property(fget=get_spatial_unit_terms)

    @abc.abstractmethod
    def get_commitment_id_terms(self):
        """Gets the commitment ``Id`` terms.

        :return: the commitment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    commitment_id_terms = property(fget=get_commitment_id_terms)

    @abc.abstractmethod
    def get_commitment_terms(self):
        """Gets the commitment terms.

        :return: the commitment terms
        :rtype: ``osid.calendaring.CommitmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CommitmentQueryInspector

    commitment_terms = property(fget=get_commitment_terms)

    @abc.abstractmethod
    def get_containing_event_id_terms(self):
        """Gets the containing event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    containing_event_id_terms = property(fget=get_containing_event_id_terms)

    @abc.abstractmethod
    def get_containing_event_terms(self):
        """Gets the containing event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    containing_event_terms = property(fget=get_containing_event_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_event_query_inspector_record(self, event_record_type):
        """Gets the event query inspector record corresponding to the given ``Event`` record ``Type``.

        :param event_record_type: an event query record type
        :type event_record_type: ``osid.type.Type``
        :return: the event query inspector record
        :rtype: ``osid.calendaring.records.EventQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.EventQueryInspectorRecord


class RecurringEventQueryInspector:
    """This is the query inspector for examining recurring event queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_schedule_id_terms(self):
        """Gets the schedule ``Id`` terms.

        :return: the schedule ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    schedule_id_terms = property(fget=get_schedule_id_terms)

    @abc.abstractmethod
    def get_schedule_terms(self):
        """Gets the schedule terms.

        :return: the schedule terms
        :rtype: ``osid.calendaring.ScheduleQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleQueryInspector

    schedule_terms = property(fget=get_schedule_terms)

    @abc.abstractmethod
    def get_superseding_event_id_terms(self):
        """Gets the superseding event ``Id`` terms.

        :return: the superseding event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    superseding_event_id_terms = property(fget=get_superseding_event_id_terms)

    @abc.abstractmethod
    def get_superseding_event_terms(self):
        """Gets the superseding event terms.

        :return: the superseding event terms
        :rtype: ``osid.calendaring.SupersedingEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.SupersedingEventQueryInspector

    superseding_event_terms = property(fget=get_superseding_event_terms)

    @abc.abstractmethod
    def get_event_id_terms(self):
        """Gets the event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    event_id_terms = property(fget=get_event_id_terms)

    @abc.abstractmethod
    def get_event_terms(self):
        """Gets the event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    event_terms = property(fget=get_event_terms)

    @abc.abstractmethod
    def get_blackout_terms(self):
        """Gets the blackout terms.

        :return: the time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    blackout_terms = property(fget=get_blackout_terms)

    @abc.abstractmethod
    def get_blackout_inclusive_terms(self):
        """Gets the inclusive blackout terms.

        :return: the time range terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    blackout_inclusive_terms = property(fget=get_blackout_inclusive_terms)

    @abc.abstractmethod
    def get_sponsor_id_terms(self):
        """Gets the sponsor ``Id`` terms.

        :return: the sponsor ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    sponsor_id_terms = property(fget=get_sponsor_id_terms)

    @abc.abstractmethod
    def get_sponsor_terms(self):
        """Gets the sponsor terms.

        :return: the sponsor terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    sponsor_terms = property(fget=get_sponsor_terms)

    @abc.abstractmethod
    def get_specific_meeting_time_terms(self):
        """Gets the date terms.

        :return: the time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    specific_meeting_time_terms = property(fget=get_specific_meeting_time_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_recurring_event_query_inspector_record(self, recurring_event_record_type):
        """Gets the recurring event query inspector record corresponding to the given ``RecurringEvent`` record
        ``Type``.

        :param recurring_event_record_type: a recurring event query record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: the recurring event query inspector record
        :rtype: ``osid.calendaring.records.RecurringEventQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.RecurringEventQueryInspectorRecord


class SupersedingEventQueryInspector:
    """This is the query inspector for examining superseding event queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_superseded_event_id_terms(self):
        """Gets the superseded event ``Id`` terms.

        :return: the superseded event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    superseded_event_id_terms = property(fget=get_superseded_event_id_terms)

    @abc.abstractmethod
    def get_superseded_event_terms(self):
        """Gets the superseded event terms.

        :return: the superseded event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    superseded_event_terms = property(fget=get_superseded_event_terms)

    @abc.abstractmethod
    def get_superseding_event_id_terms(self):
        """Gets the superseding event ``Id`` terms.

        :return: the superseding event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    superseding_event_id_terms = property(fget=get_superseding_event_id_terms)

    @abc.abstractmethod
    def get_superseding_event_terms(self):
        """Gets the superseding event terms.

        :return: the superseding event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    superseding_event_terms = property(fget=get_superseding_event_terms)

    @abc.abstractmethod
    def get_superseded_date_terms(self):
        """Gets the superseded date range terms.

        :return: the superseded date range terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    superseded_date_terms = property(fget=get_superseded_date_terms)

    @abc.abstractmethod
    def get_superseded_event_position_terms(self):
        """Gets the superseded event position terms.

        :return: the superseded event position terms
        :rtype: ``osid.search.terms.IntegerRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerRangeTerm

    superseded_event_position_terms = property(fget=get_superseded_event_position_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_superseding_event_query_inspector_record(self, superseding_event_record_type):
        """Gets the superseding event query inspector record corresponding to the given ``SupersedingEvent`` record
        ``Type``.

        :param superseding_event_record_type: a superseding event query record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: the superseding event query inspector record
        :rtype: ``osid.calendaring.records.SupersedingEventQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.SupersedingEventQueryInspectorRecord


class OffsetEventQueryInspector:
    """This is the query inspector for examining offset event queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_fixed_start_time_terms(self):
        """Gets the fixed start time terms.

        :return: the fixed start time terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    fixed_start_time_terms = property(fget=get_fixed_start_time_terms)

    @abc.abstractmethod
    def get_start_reference_event_id_terms(self):
        """Gets the event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    start_reference_event_id_terms = property(fget=get_start_reference_event_id_terms)

    @abc.abstractmethod
    def get_start_reference_event_terms(self):
        """Gets the event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    start_reference_event_terms = property(fget=get_start_reference_event_terms)

    @abc.abstractmethod
    def get_fixed_start_offset_terms(self):
        """Gets the fixed offset terms.

        :return: the fixed offset terms
        :rtype: ``osid.search.terms.IntegerRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerRangeTerm

    fixed_start_offset_terms = property(fget=get_fixed_start_offset_terms)

    @abc.abstractmethod
    def get_relative_weekday_start_offset_terms(self):
        """Gets the relative weekday offset terms.

        :return: the relative weekday offset terms
        :rtype: ``osid.search.terms.IntegerRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerRangeTerm

    relative_weekday_start_offset_terms = property(fget=get_relative_weekday_start_offset_terms)

    @abc.abstractmethod
    def get_relative_start_weekday_terms(self):
        """Gets the relative weekday terms.

        :return: the relative weekday terms
        :rtype: ``osid.search.terms.CardinalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalTerm

    relative_start_weekday_terms = property(fget=get_relative_start_weekday_terms)

    @abc.abstractmethod
    def get_fixed_duration_terms(self):
        """Gets the fixed duration terms.

        :return: the fixed duration terms
        :rtype: ``osid.search.terms.DurationRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationRangeTerm

    fixed_duration_terms = property(fget=get_fixed_duration_terms)

    @abc.abstractmethod
    def get_end_reference_event_id_terms(self):
        """Gets the event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    end_reference_event_id_terms = property(fget=get_end_reference_event_id_terms)

    @abc.abstractmethod
    def get_end_reference_event_terms(self):
        """Gets the event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    end_reference_event_terms = property(fget=get_end_reference_event_terms)

    @abc.abstractmethod
    def get_fixed_end_offset_terms(self):
        """Gets the fixed offset terms.

        :return: the fixed offset terms
        :rtype: ``osid.search.terms.IntegerRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerRangeTerm

    fixed_end_offset_terms = property(fget=get_fixed_end_offset_terms)

    @abc.abstractmethod
    def get_relative_weekday_end_offset_terms(self):
        """Gets the relative weekday offset terms.

        :return: the relative weekday offset terms
        :rtype: ``osid.search.terms.IntegerRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerRangeTerm

    relative_weekday_end_offset_terms = property(fget=get_relative_weekday_end_offset_terms)

    @abc.abstractmethod
    def get_relative_end_weekday_terms(self):
        """Gets the relative weekday terms.

        :return: the relative weekday terms
        :rtype: ``osid.search.terms.CardinalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalTerm

    relative_end_weekday_terms = property(fget=get_relative_end_weekday_terms)

    @abc.abstractmethod
    def get_location_description_terms(self):
        """Gets the location description terms.

        :return: the location description terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    location_description_terms = property(fget=get_location_description_terms)

    @abc.abstractmethod
    def get_location_id_terms(self):
        """Gets the location ``Id`` terms.

        :return: the location ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    location_id_terms = property(fget=get_location_id_terms)

    @abc.abstractmethod
    def get_location_terms(self):
        """Gets the location terms.

        :return: the location terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    location_terms = property(fget=get_location_terms)

    @abc.abstractmethod
    def get_sponsor_id_terms(self):
        """Gets the sponsor ``Id`` terms.

        :return: the sponsor ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    sponsor_id_terms = property(fget=get_sponsor_id_terms)

    @abc.abstractmethod
    def get_sponsor_terms(self):
        """Gets the sponsor terms.

        :return: the sponsor terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    sponsor_terms = property(fget=get_sponsor_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_offset_event_query_inspector_record(self, offset_event_record_type):
        """Gets the offset event query inspector record corresponding to the given ``OffsetEvent`` record ``Type``.

        :param offset_event_record_type: an offset event query record type
        :type offset_event_record_type: ``osid.type.Type``
        :return: the offset event query inspector record
        :rtype: ``osid.calendaring.records.OffsetEventQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.OffsetEventQueryInspectorRecord


class ScheduleQueryInspector:
    """This is the query inspector for examining schedule queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_schedule_slot_id_terms(self):
        """Gets the schedule slot ``Id`` terms.

        :return: the schedule slot ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    schedule_slot_id_terms = property(fget=get_schedule_slot_id_terms)

    @abc.abstractmethod
    def get_schedule_slot_terms(self):
        """Gets the schedule slot terms.

        :return: the schedule slot terms
        :rtype: ``osid.calendaring.ScheduleSlotQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleSlotQueryInspector

    schedule_slot_terms = property(fget=get_schedule_slot_terms)

    @abc.abstractmethod
    def get_time_period_id_terms(self):
        """Gets the time period ``Id`` terms.

        :return: the time period ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    time_period_id_terms = property(fget=get_time_period_id_terms)

    @abc.abstractmethod
    def get_time_period_terms(self):
        """Gets the time period terms.

        :return: the time period terms
        :rtype: ``osid.calendaring.TimePeriodQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.TimePeriodQueryInspector

    time_period_terms = property(fget=get_time_period_terms)

    @abc.abstractmethod
    def get_schedule_start_terms(self):
        """Gets the schedule start terms.

        :return: the schedule start terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    schedule_start_terms = property(fget=get_schedule_start_terms)

    @abc.abstractmethod
    def get_schedule_end_terms(self):
        """Gets the schedule end terms.

        :return: the schedule end terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    schedule_end_terms = property(fget=get_schedule_end_terms)

    @abc.abstractmethod
    def get_schedule_time_terms(self):
        """Gets the schedule time terms.

        :return: the schedule time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    schedule_time_terms = property(fget=get_schedule_time_terms)

    @abc.abstractmethod
    def get_schedule_time_inclusive_terms(self):
        """Gets the schedule inclusive time terms.

        :return: the schedule time range terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    schedule_time_inclusive_terms = property(fget=get_schedule_time_inclusive_terms)

    @abc.abstractmethod
    def get_limit_terms(self):
        """Gets the limit terms.

        :return: the limit terms
        :rtype: ``osid.search.terms.CardinalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalTerm

    limit_terms = property(fget=get_limit_terms)

    @abc.abstractmethod
    def get_location_description_terms(self):
        """Gets the location description terms.

        :return: the location description terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    location_description_terms = property(fget=get_location_description_terms)

    @abc.abstractmethod
    def get_location_id_terms(self):
        """Gets the location ``Id`` terms.

        :return: the location ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    location_id_terms = property(fget=get_location_id_terms)

    @abc.abstractmethod
    def get_location_terms(self):
        """Gets the location terms.

        :return: the location terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    location_terms = property(fget=get_location_terms)

    @abc.abstractmethod
    def get_total_duration_terms(self):
        """Gets the total duration terms.

        :return: the duration terms
        :rtype: ``osid.search.terms.DurationRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationRangeTerm

    total_duration_terms = property(fget=get_total_duration_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_schedule_query_inspector_record(self, schedule_record_type):
        """Gets the schedule query inspector record corresponding to the given ``Schedule`` record ``Type``.

        :param schedule_record_type: a schedule query record type
        :type schedule_record_type: ``osid.type.Type``
        :return: the schedule query inspector record
        :rtype: ``osid.calendaring.records.ScheduleQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleQueryInspectorRecord


class ScheduleSlotQueryInspector:
    """This is the query inspector for examining schedule queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_schedule_slot_id_terms(self):
        """Gets the schedule slot ``Id`` terms.

        :return: the schedule ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    schedule_slot_id_terms = property(fget=get_schedule_slot_id_terms)

    @abc.abstractmethod
    def get_schedule_slot_terms(self):
        """Gets the schedule slot terms.

        :return: the schedule slot terms
        :rtype: ``osid.calendaring.ScheduleSlotQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.ScheduleSlotQueryInspector

    schedule_slot_terms = property(fget=get_schedule_slot_terms)

    @abc.abstractmethod
    def get_weekday_terms(self):
        """Gets the weekday terms.

        :return: the weekday terms
        :rtype: ``osid.search.terms.CardinalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalTerm

    weekday_terms = property(fget=get_weekday_terms)

    @abc.abstractmethod
    def get_weekly_interval_terms(self):
        """Gets the weekly interval terms.

        :return: the weekly interval terms
        :rtype: ``osid.search.terms.IntegerTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerTerm

    weekly_interval_terms = property(fget=get_weekly_interval_terms)

    @abc.abstractmethod
    def get_week_of_month_terms(self):
        """Gets the week of month terms.

        :return: the week of month terms
        :rtype: ``osid.search.terms.IntegerTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerTerm

    week_of_month_terms = property(fget=get_week_of_month_terms)

    @abc.abstractmethod
    def get_weekday_time_terms(self):
        """Gets the weekday time terms.

        :return: the fixed interval terms
        :rtype: ``osid.search.terms.TimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TimeRangeTerm

    weekday_time_terms = property(fget=get_weekday_time_terms)

    @abc.abstractmethod
    def get_fixed_interval_terms(self):
        """Gets the fixed interval terms.

        :return: the fixed interval terms
        :rtype: ``osid.search.terms.DurationRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationRangeTerm

    fixed_interval_terms = property(fget=get_fixed_interval_terms)

    @abc.abstractmethod
    def get_duration_terms(self):
        """Gets the duration terms.

        :return: the duration terms
        :rtype: ``osid.search.terms.DurationTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationTerm

    duration_terms = property(fget=get_duration_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_schedule_slot_query_inspector_record(self, schedule_slot_record_type):
        """Gets the schedule slot query inspector record corresponding to the given ``ScheduleSlot`` record ``Type``.

        :param schedule_slot_record_type: a schedule slot query record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: the schedule slot query inspector record
        :rtype: ``osid.calendaring.records.ScheduleSlotQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.ScheduleSlotQueryInspectorRecord


class TimePeriodQueryInspector:
    """This is the query inspector for examining time period queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_start_terms(self):
        """Gets the start terms.

        :return: the start terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    start_terms = property(fget=get_start_terms)

    @abc.abstractmethod
    def get_end_terms(self):
        """Gets the end terms.

        :return: the end terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    end_terms = property(fget=get_end_terms)

    @abc.abstractmethod
    def get_time_terms(self):
        """Gets the time terms.

        :return: the time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    time_terms = property(fget=get_time_terms)

    @abc.abstractmethod
    def get_time_inclusive_terms(self):
        """Gets the inclusive time terms.

        :return: the time range terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    time_inclusive_terms = property(fget=get_time_inclusive_terms)

    @abc.abstractmethod
    def get_duration_terms(self):
        """Gets the duration terms.

        :return: the duration terms
        :rtype: ``osid.search.terms.DurationTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationTerm

    duration_terms = property(fget=get_duration_terms)

    @abc.abstractmethod
    def get_exception_id_terms(self):
        """Gets the exception event ``Id`` terms.

        :return: the exception event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    exception_id_terms = property(fget=get_exception_id_terms)

    @abc.abstractmethod
    def get_exception_terms(self):
        """Gets the exception event terms.

        :return: the exception event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    exception_terms = property(fget=get_exception_terms)

    @abc.abstractmethod
    def get_event_id_terms(self):
        """Gets the event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    event_id_terms = property(fget=get_event_id_terms)

    @abc.abstractmethod
    def get_event_terms(self):
        """Gets the event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    event_terms = property(fget=get_event_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_time_period_query_inspector_record(self, time_period_record_type):
        """Gets the time period query record interface corresponding to the given ``TimePeriod`` record ``Type``.

        :param time_period_record_type: a time period query record type
        :type time_period_record_type: ``osid.type.Type``
        :return: the time period query inspector record
        :rtype: ``osid.calendaring.records.TimePeriodQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.TimePeriodQueryInspectorRecord


class CommitmentQueryInspector:
    """This is the query inspector for examining commitment queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_event_id_terms(self):
        """Gets the event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    event_id_terms = property(fget=get_event_id_terms)

    @abc.abstractmethod
    def get_event_terms(self):
        """Gets the event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    event_terms = property(fget=get_event_terms)

    @abc.abstractmethod
    def get_resource_id_terms(self):
        """Gets the resource ``Id`` terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    @abc.abstractmethod
    def get_resource_terms(self):
        """Gets the resource terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    @abc.abstractmethod
    def get_calendar_id_terms(self):
        """Gets the calendar ``Id`` terms.

        :return: the calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    calendar_id_terms = property(fget=get_calendar_id_terms)

    @abc.abstractmethod
    def get_calendar_terms(self):
        """Gets the calendar terms.

        :return: the calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    calendar_terms = property(fget=get_calendar_terms)

    @abc.abstractmethod
    def get_commitment_query_inspector_record(self, commitment_record_type):
        """Gets the commitment query inspector record corresponding to the given ``Commitment`` record ``Type``.

        :param commitment_record_type: a commitment query record type
        :type commitment_record_type: ``osid.type.Type``
        :return: the commitment query inspector record
        :rtype: ``osid.calendaring.records.CommitmentQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CommitmentQueryInspectorRecord


class CalendarQueryInspector:
    """This is the query inspector for examining calendar queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_event_id_terms(self):
        """Gets the event ``Id`` terms.

        :return: the event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    event_id_terms = property(fget=get_event_id_terms)

    @abc.abstractmethod
    def get_event_terms(self):
        """Gets the event terms.

        :return: the event terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.EventQueryInspector

    event_terms = property(fget=get_event_terms)

    @abc.abstractmethod
    def get_time_period_id_terms(self):
        """Gets the time period ``Id`` terms.

        :return: the time period ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    time_period_id_terms = property(fget=get_time_period_id_terms)

    @abc.abstractmethod
    def get_time_period_terms(self):
        """Gets the time period terms.

        :return: the time period terms
        :rtype: ``osid.calendaring.TimePeriodQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.TimePeriodQueryInspector

    time_period_terms = property(fget=get_time_period_terms)

    @abc.abstractmethod
    def get_commitment_id_terms(self):
        """Gets the commitment ``Id`` terms.

        :return: the commitment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    commitment_id_terms = property(fget=get_commitment_id_terms)

    @abc.abstractmethod
    def get_commitment_terms(self):
        """Gets the commitment terms.

        :return: the commitment terms
        :rtype: ``osid.calendaring.CommitmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CommitmentQueryInspector

    commitment_terms = property(fget=get_commitment_terms)

    @abc.abstractmethod
    def get_ancestor_calendar_id_terms(self):
        """Gets the ancestor calendar ``Id`` terms.

        :return: the ancestor calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_calendar_id_terms = property(fget=get_ancestor_calendar_id_terms)

    @abc.abstractmethod
    def get_ancestor_calendar_terms(self):
        """Gets the ancestor calendar terms.

        :return: the ancestor calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    ancestor_calendar_terms = property(fget=get_ancestor_calendar_terms)

    @abc.abstractmethod
    def get_descendant_calendar_id_terms(self):
        """Gets the descendant calendar ``Id`` terms.

        :return: the descendant calendar ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_calendar_id_terms = property(fget=get_descendant_calendar_id_terms)

    @abc.abstractmethod
    def get_descendant_calendar_terms(self):
        """Gets the descendant calendar terms.

        :return: the descendant calendar terms
        :rtype: ``osid.calendaring.CalendarQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.CalendarQueryInspector

    descendant_calendar_terms = property(fget=get_descendant_calendar_terms)

    @abc.abstractmethod
    def get_calendar_query_inspector_record(self, calendar_record_type):
        """Gets the calendar query inspector record corresponding to the given ``Calendar`` record ``Type``.

        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the calendar query inspector record
        :rtype: ``osid.calendaring.records.CalendarQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.records.CalendarQueryInspectorRecord
