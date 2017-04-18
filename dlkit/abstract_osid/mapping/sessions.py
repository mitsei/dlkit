"""Implementations of mapping abstract base class sessions."""
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


class LocationLookupSession:
    """This session defines methods for retrieving locations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_lookup_locations(self):
        """Tests if this user can perform ``Location`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_location_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_location_view(self):
        """A complete view of the ``Location`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include locations in maps which are
        children of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location(self, location_id):
        """Gets the ``Location`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Location`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Location`` and retained for
        compatibility.

        :param location_id: the ``Id`` of the ``Location`` to retrieve
        :type location_id: ``osid.id.Id``
        :return: the returned ``Location``
        :rtype: ``osid.mapping.Location``
        :raise: ``NotFound`` -- no ``Location`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Location

    @abc.abstractmethod
    def get_locations_by_ids(self, location_ids):
        """Gets a ``LocationList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the locations
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Locations`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param location_ids: the list of ``Ids`` to retrieve
        :type location_ids: ``osid.id.IdList``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``location_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_locations_by_genus_type(self, location_genus_type):
        """Gets a ``LocationList`` corresponding to the given location genus ``Type`` which does not include locations of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :param location_genus_type: a location genus type
        :type location_genus_type: ``osid.type.Type``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_locations_by_parent_genus_type(self, location_genus_type):
        """Gets a ``LocationList`` corresponding to the given location genus ``Type`` and include any additional locations with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :param location_genus_type: a location genus type
        :type location_genus_type: ``osid.type.Type``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_locations_by_record_type(self, location_record_type):
        """Gets a ``LocationList`` containing the given location record ``Type``.

        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_locations(self):
        """Gets all ``Locations``.

        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :return: a list of ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    locations = abc.abstractproperty(fget=get_locations)


class LocationQuerySession:
    """This session provides methods for searching among ``Location`` objects.

    The search query is constructed using the ``LocationQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated map view: searches include locations in maps of which
        this map is an ancestor in the map hierarchy
      * isolated map view: searches are restricted to locations in this
        map


    Locations may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``LocationQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_search_locations(self):
        """Tests if this user can perform ``Location`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include locations in maps which are
        children of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location_query(self):
        """Gets a location query.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQuery

    location_query = abc.abstractproperty(fget=get_location_query)

    @abc.abstractmethod
    def get_locations_by_query(self, location_query):
        """Gets a list of ``Locations`` matching the given search.

        :param location_query: the location query
        :type location_query: ``osid.mapping.LocationQuery``
        :return: the returned ``LocationList``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList


class LocationSearchSession:
    """This session provides methods for searching among ``Location`` objects.

    The search query is constructed using the ``LocationQuery``.

    ``get_locations_by_query()`` is the basic search method and returns
    a list of ``Locations``. A more advanced search may be performed
    with ``getLocationsBySearch()``. It accepts a ``LocationSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_locations_by_search()`` returns a ``LocationSearchResults``
    that can be used to access the resulting ``LocationList`` or be used
    to perform a search within the result set through
    ``LocationSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated map view: searches include locations in maps of which
        this map is an ancestor in the map hierarchy
      * isolated map view: searches are restricted to locations in this
        map


    Locations may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``LocationQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_location_search(self):
        """Gets a location search.

        :return: the location search
        :rtype: ``osid.mapping.LocationSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationSearch

    location_search = abc.abstractproperty(fget=get_location_search)

    @abc.abstractmethod
    def get_location_search_order(self):
        """Gets a location search order.

        The ``LocationSearchOrder`` is supplied to a ``LocationSearch``
        to specify the ordering of results.

        :return: the location search order
        :rtype: ``osid.mapping.LocationSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationSearchOrder

    location_search_order = abc.abstractproperty(fget=get_location_search_order)

    @abc.abstractmethod
    def get_locations_by_search(self, location_query, location_search):
        """Gets the search results matching the given search query using the given search.

        :param location_query: the location query
        :type location_query: ``osid.mapping.LocationQuery``
        :param location_search: the location search
        :type location_search: ``osid.mapping.LocationSearch``
        :return: the returned search results
        :rtype: ``osid.mapping.LocationSearchResults``
        :raise: ``NullArgument`` -- ``location_query`` or ``location_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_query`` or ``location_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationSearchResults

    @abc.abstractmethod
    def get_location_query_from_inspector(self, location_query_inspector):
        """Gets a location query from an inspector.

        The inspector is available from a ``LocationSearchResults``.

        :param location_query_inspector: a location query inspector
        :type location_query_inspector: ``osid.mapping.LocationQueryInspector``
        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``NullArgument`` -- ``location_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``location_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQuery


class LocationAdminSession:
    """This session creates, updates, and deletes ``Locations``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Location,`` a ``LocationForm`` is requested using
    ``get_location_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LocationForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LocationForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LocationForm``
    corresponds to an attempted transaction.

    For updates, ``LocationForms`` are requested to the ``Location``
    ``Id`` that is to be updated using ``getLocationFormForUpdate()``.
    Similarly, the ``LocationForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``LocationForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Locations``. To unmap a ``Location``
    from the current ``Map,`` the ``LocationMapAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Location`` itself thus removing it from all known ``Map``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_create_locations(self):
        """Tests if this user can create ``Locations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Location`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Location`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_location_with_record_types(self, location_record_types):
        """Tests if this user can create a single ``Location`` using the desired record types.

        While ``MappingManager.getLocationRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Location``.
        Providing an empty array tests if a ``Location`` can be created
        with no records.

        :param location_record_types: array of location record types
        :type location_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Location`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``location_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_form_for_create(self, location_record_types):
        """Gets the location form for creating new locations.

        A new form should be requested for each create transaction.

        :param location_record_types: array of location record types
        :type location_record_types: ``osid.type.Type[]``
        :return: the location form
        :rtype: ``osid.mapping.LocationForm``
        :raise: ``NullArgument`` -- ``location_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get a form with given record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationForm

    @abc.abstractmethod
    def create_location(self, location_form):
        """Creates a new ``Location``.

        :param location_form: the form for this ``Location``
        :type location_form: ``osid.mapping.LocationForm``
        :return: the new ``Location``
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``location_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``location_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_form`` did not originate from ``get_location_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Location

    @abc.abstractmethod
    def can_update_locations(self):
        """Tests if this user can update ``Locations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Location`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Location`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_form_for_update(self, location_id):
        """Gets the location form for updating an existing location.

        A new location form should be requested for each update
        transaction.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :return: the location form
        :rtype: ``osid.mapping.LocationForm``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationForm

    @abc.abstractmethod
    def update_location(self, location_form):
        """Updates an existing location.

        :param location_form: the form containing the elements to be updated
        :type location_form: ``osid.mapping.LocationForm``
        :raise: ``IllegalState`` -- ``location_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``location_id`` or ``location_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_form`` did not originate from ``get_location_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_locations(self):
        """Tests if this user can delete ``Locations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Location`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Location`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_location(self, location_id):
        """Deletes a ``Location``.

        :param location_id: the ``Id`` of the ``Location`` to remove
        :type location_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_location_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Locations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Location`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_location(self, location_id, alias_id):
        """Adds an ``Id`` to a ``Location`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Location`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another location, it is
        reassigned to the given location ``Id``.

        :param location_id: the ``Id`` of a ``Location``
        :type location_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LocationNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Location`` objects in this ``Map``.

    This also includes existing locations that may appear or disappear
    due to changes in the ``Location`` hierarchy, This session is
    intended for consumers needing to synchronize their state with this
    service without the use of polling. Notifications are cancelled when
    this session is closed.

    The two views defined in this session correspond to the views in the
    ``LocationLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_register_for_location_notifications(self):
        """Tests if this user can register for ``Location`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include locations in maps which are
        children of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_location_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_location_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_location_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_location_notification(self, notification_id):
        """Acknowledge a location notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_locations(self):
        """Register for notifications of new locations.

        ``LocationReceiver.newLocations()`` is invoked when a new
        ``Location`` appears in this map.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_locations(self):
        """Registers for notification of updated locations.

        ``LocationReceiver.changedLocations()`` is invoked when a
        location in this map is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_location(self, location_id):
        """Registers for notification of an updated location.

        ``LocationReceiver.changedLocations()`` is invoked when the
        specified location in this map is changed.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_locations(self):
        """Registers for notification of deleted locations.

        ``LocationReceiver.deletedLocations()`` is invoked when a
        location is deleted or removed from this map.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_location(self, location_id):
        """Registers for notification of a deleted location.

        ``LocationReceiver.deletedLocations()`` is invoked when the
        specified location is deleted or removed from this map.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_location_hierarchy(self):
        """Registers for notification of an updated location hierarchy structure.

        ``LocationReceiver.changedChildOfLocations()`` is invoked when a
        node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_location_hierarchy_for_ancestors(self, location_id):
        """Registers for notification of an updated location hierarchy structure.

        ``LocationReceiver.changedChildOfLocations()`` is invoked when
        the specified node or any of its ancestors experiences a change
        in its children.

        :param location_id: the ``Id`` of the ``Location`` node to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_location_hierarchy_for_descendants(self, location_id):
        """Registers for notification of an updated location hierarchy structure.

        ``LocationReceiver.changedChildOfLocations()`` is invoked when
        the specified node or any of its descendants experiences a
        change in its children.

        :param location_id: the ``Id`` of the ``Location`` node to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LocationHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Location`` objects.

    Each node in the hierarchy is a unique ``Location``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_locations()`` and ``getChildLocations()``. To relate
    these ``Ids`` to another OSID, ``get_location_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Location`` available in the Mapping OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root location or a child of another location.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_m_locations()`` or ``get_child_locations()``
    in lieu of a ``PermissionDenied`` error that may disrupt the
    traversal through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative location view: location elements may be silently
        omitted or re-ordered
      * plenary location view: provides a complete set or is an error
        condition


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_location_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    location_hierarchy_id = abc.abstractproperty(fget=get_location_hierarchy_id)

    @abc.abstractmethod
    def get_location_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    location_hierarchy = abc.abstractproperty(fget=get_location_hierarchy)

    @abc.abstractmethod
    def can_access_location_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_location_view(self):
        """The returns from the location methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_location_view(self):
        """A complete view of the ``Locations`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_location_ids(self):
        """Gets the root location ``Ids`` in this hierarchy.

        :return: the root location ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_location_ids = abc.abstractproperty(fget=get_root_location_ids)

    @abc.abstractmethod
    def get_root_locations(self):
        """Gets the root location in the location hierarchy.

        A location with no parents is an orphan. While all location
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root location or
        child of another location.

        :return: the root locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.mapping.LocationList

    root_locations = abc.abstractproperty(fget=get_root_locations)

    @abc.abstractmethod
    def has_parent_locations(self, location_id):
        """Tests if the ``Location`` has any parents.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the location has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_location(self, id_, location_id):
        """Tests if an ``Id`` is a direct parent of location.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``location_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_location_ids(self, location_id):
        """Gets the parent ``Ids`` of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the location
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_locations(self, location_id):
        """Gets the parents of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the parents of the location
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def is_ancestor_of_location(self, id_, location_id):
        """Tests if an ``Id`` is an ancestor of a location.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``location_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_locations(self, location_id):
        """Tests if a location has any children.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the ``location_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_location(self, id_, location_id):
        """Tests if a location is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``location_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_location_ids(self, location_id):
        """Gets the child ``Ids`` of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the children of the location
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_locations(self, location_id):
        """Gets the children of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the children of the location
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def is_descendant_of_location(self, id_, location_id):
        """Tests if an ``Id`` is a descendant of a location.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``location_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_node_ids(self, location_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given location.

        :param location_id: the ``Id`` to query
        :type location_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a location node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_location_nodes(self, location_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given location.

        :param location_id: the ``Id`` to query
        :type location_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a location node
        :rtype: ``osid.mapping.LocationNode``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationNode


class LocationHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Location`` objects.

    Each node in the hierarchy is a unique ``Location``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_location_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    location_hierarchy_id = abc.abstractproperty(fget=get_location_hierarchy_id)

    @abc.abstractmethod
    def get_location_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    location_hierarchy = abc.abstractproperty(fget=get_location_hierarchy)

    @abc.abstractmethod
    def can_modify_location_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_location(self, location_id):
        """Adds a root location.

        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``location_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_location(self, location_id, child_id):
        """Adds a child to a location.

        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``map_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LocationMapSession:
    """This session provides methods to retrieve ``Location`` to ``Map`` locations.

    A ``Location`` may appear in multiple ``Map`` objects. Each map may
    have its own authorizations governing who is allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_location_map_locations(self):
        """Tests if this user can perform lookups of location/map locations.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up locations is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_location_map_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_location_map_view(self):
        """A complete view of the ``Location`` and ``Map`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location_ids_by_map(self, map_id):
        """Gets the list of ``Location Ids`` associated with a ``Map``.

        :param map_id: ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: list of related location ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_locations_by_map(self, map_id):
        """Gets the list of ``Locations`` associated with a ``Map``.

        :param map_id: ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: list of related locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_location_ids_by_maps(self, map_ids):
        """Gets the list of ``Location Ids`` corresponding to a list of ``Maps``.

        :param map_ids: list of map ``Ids``
        :type map_ids: ``osid.id.IdList``
        :return: list of location ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_locations_by_maps(self, map_ids):
        """Gets the list of ``Locations`` corresponding to a list of ``Maps``.

        :param map_ids: list of map ``Ids``
        :type map_ids: ``osid.id.IdList``
        :return: list of locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_map_ids_by_location(self, location_id):
        """Gets the ``Map``  ``Ids`` mapped to a ``Location``.

        :param location_id: ``Id`` of a ``Location``
        :type location_id: ``osid.id.Id``
        :return: list of maps
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_maps_by_location(self, location_id):
        """Gets the ``Maps`` mapped to a ``Location``.

        :param location_id: ``Id`` of a ``Location``
        :type location_id: ``osid.id.Id``
        :return: list of maps
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList


class LocationMapAssignmentSession:
    """This session provides methods to re-assign ``Locations`` to ``Map`` objects A ``Location`` may appear in multiple ``Map`` objects and removing the last reference to a ``Location`` is the equivalent of deleting it.

    Each ``Map`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Location`` to another ``Map`` is not a
    copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_locations(self):
        """Tests if this user can alter location/map mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if location is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_locations_to_map(self, map_id):
        """Tests if this user can alter location/map mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_map_ids(self, map_id):
        """Gets a list of maps including and under the given map node in which any location can be assigned.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: list of assignable map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_map_ids_for_location(self, map_id, location_id):
        """Gets a list of maps including and under the given map node in which a specific location can be assigned.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :return: list of assignable map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_location_to_map(self, location_id, map_id):
        """Adds an existing ``Location`` to a ``Map``.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``location_id`` is already assigned to ``map_id``
        :raise: ``NotFound`` -- ``location_id`` or ``map_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_location_from_map(self, location_id, map_id):
        """Removes a ``Location`` from a ``Map``.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``location_id`` or ``map_id`` not found or ``location_id`` not assigned to ``map_id``
        :raise: ``NullArgument`` -- ``location_id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_location_to_map(self, location_id, from_map_id, to_map_id):
        """Moves a ``Map`` from one ``Location`` to another.

        Mappings to other ``Locations`` are unaffected.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param from_map_id: the ``Id`` of the current ``Map``
        :type from_map_id: ``osid.id.Id``
        :param to_map_id: the ``Id`` of the destination ``Map``
        :type to_map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``location_id, from_map_id,`` or ``to_map_id`` not found or ``location_id`` not mapped to ``from_map_id``
        :raise: ``NullArgument`` -- ``location_id, from_map_id,`` or ``to_map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LocationSmartMapSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``LocationQuery`` can be retrieved from this session and mapped to
    this ``Map`` to create a virtual collection of ``Locations``. The
    locations may be sequenced using the ``LocationSearchOrder`` from
    this session.

    This ``Map`` has a default query that matches any location and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``LocationQueryInspector``. The query may be
    modified by converting the inspector back to a ``LocationQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_manage_smart_maps(self):
        """Tests if this user can manage smart maps.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart map management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_query(self):
        """Gets a location query.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQuery

    location_query = abc.abstractproperty(fget=get_location_query)

    @abc.abstractmethod
    def get_location_search_order(self):
        """Gets a location search order.

        :return: the location search order
        :rtype: ``osid.mapping.LocationSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationSearchOrder

    location_search_order = abc.abstractproperty(fget=get_location_search_order)

    @abc.abstractmethod
    def apply_location_query(self, location_query):
        """Applies a location query to this map.

        :param location_query: the location query
        :type location_query: ``osid.mapping.LocationQuery``
        :raise: ``NullArgument`` -- ``location_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``location_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspec_location_query(self):
        """Gets a location query inspector for this map.

        :return: the location query inspector
        :rtype: ``osid.mapping.LocationQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    @abc.abstractmethod
    def apply_location_sequencing(self, location_search_order):
        """Applies a location search order to this map.

        :param location_search_order: the location search order
        :type location_search_order: ``osid.mapping.LocationSearchOrder``
        :raise: ``NullArgument`` -- ``location_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``location_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location_query_from_inspector(self, location_query_inspector):
        """Gets a location query from an inspector.

        :param location_query_inspector: a location query inspector
        :type location_query_inspector: ``osid.mapping.LocationQueryInspector``
        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``NullArgument`` -- ``location_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``location_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQuery


class LocationAdjacencySession:
    """This session defines methods to traverse through a map."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_lookup_location_adjacencies(self):
        """Tests if this user can query adjacenies of locations A return of true does not guarantee successful authorization.

        A return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if location adjacency methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_location_view(self):
        """The returns from the traversal methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_location_view(self):
        """A complete view of the method returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include paths in maps which are children
        of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_adjacent_locations(self, location_id, hops):
        """Gets a list of adjacent locations for the given location.

        The adjacent locations reflect the locations at the same level
        of the location hierarchy.

        :param location_id: the given location ``Id``
        :type location_id: ``osid.id.Id``
        :param hops: the number of hops to include. 0 returns an empty list. 1 returns the immediate adjacent locations.
        :type hops: ``cardinal``
        :return: a list of locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def is_adjacent(self, location_id, another_location_id):
        """Tests if two locations of the same type are adjacent.

        A location is not adjacent if contained within another location.

        :param location_id: the given location ``Id``
        :type location_id: ``osid.id.Id``
        :param another_location_id: the given location ``Id``
        :type another_location_id: ``osid.id.Id``
        :return: ``true`` of the locations are adjacent, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` or ``another_location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` or ``another_location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class LocationSpatialSession:
    """This session defines methods for retrieving locations through spatial queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_lookup_locations(self):
        """Tests if this user can perform ``Location`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_location_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_location_view(self):
        """A complete view of the ``Location`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include locations in maps which are
        children of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location_by_coordinate(self, coordinate):
        """Gets the closest bounding location of the given coordinate.

        :param coordinate: a coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :return: the returned ``Location``
        :rtype: ``osid.mapping.Location``
        :raise: ``NullArgument`` -- ``coordinate`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- coordinate not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Location

    @abc.abstractmethod
    def get_locations_by_coordinates(self, coordinates):
        """Gets the closest bounding locations in the given coordinate list.

        In plenary mode, all locations are returned for each supplied
        coodrinate or an error results. In comparative mode, the
        returned list may omit inaccessible locations or reorder them.

        :param coordinates: a coordinate list
        :type coordinates: ``osid.mapping.CoordinateList``
        :return: the returned ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``coordinates`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a coordinate is not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_locations_in_spatial_unit(self, spatial_unit):
        """Gets the locations that are included inside the given spatial unit.

        In plenary mode, all locations are returned or an error results.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the returned ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    @abc.abstractmethod
    def get_locations_overlapping_spatial_unit(self, spatial_unit):
        """Gets the locations that are included inside or touch the given spatial unit.

        In plenary mode, all locations are returned or an error results.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the returned ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList


class ResourceLocationSession:
    """This session defines methods to look up resources on a map."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_access_resource_locations(self):
        """Tests if this user can access the locations of resources.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer location
        operations to unauthorized users.

        :return: ``false`` if location methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_resource_location_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_resource_location_view(self):
        """A complete view of the ``Location`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include paths in maps which are children
        of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_resource_location(self, resource_id):
        """Gets the current closest bounding location of the given resource.

        The returned ResourceLocation may not indicate a known location
        if no location is known.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the current location
        :rtype: ``osid.mapping.ResourceLocation``
        :raise: ``NotFound`` -- ``resource_id`` is not on map
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.ResourceLocation

    @abc.abstractmethod
    def get_resource_locations(self, resource_ids):
        """Gets the current closest bounding locations of the given resources.

        In plenary mode, the returned list contains all of the locations
        of the supplied resources or an error results. In comparative
        mode, inaccessible resources may be omitted or duplicates
        suppressed or reordered.

        :param resource_ids: a resource list
        :type resource_ids: ``osid.id.IdList``
        :return: the current locations
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NotFound`` -- a resource ``Id`` is not on map
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.ResourceLocationList

    @abc.abstractmethod
    def get_resources_at_location(self, location_id):
        """Gets the current resources at or within the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.ResourceLocationList

    @abc.abstractmethod
    def get_resources_at_location_by_genus_type(self, location_id, resource_genus_type):
        """Gets the current resources at or within the given location for a resource genus type.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` or ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.ResourceLocationList

    @abc.abstractmethod
    def get_resources_at_spatial_unit(self, spatial_unit):
        """Gets the current resource within the given spatial unit.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.ResourceLocationList

    @abc.abstractmethod
    def get_resources_at_spatial_unit_by_genus_type(self, spatial_unit, resource_genus_type):
        """Gets the current resource within the given spatial unit for a given resource genus type.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` or ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.ResourceLocationList


class ResourceLocationUpdateSession:
    """This session defines update positions of resources."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_update_resource_locations(self):
        """Tests if this user can set the locations of resources.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer location
        operations to unauthorized users.

        :return: ``false`` if location methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def update_resource_location(self, resource_id, location_id):
        """Updates the location of the resource.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id`` or ``location_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def update_resource_coordinate(self, resource_id, coordinate):
        """Updates the coordinate of the resource.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param coordinate: a coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``coordinate`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- coordinate not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourceLocationNotificationSession:
    """This session defines methods to receive notifications on adds/changes to resources locations in this ``Map``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_register_for_resource_location_notifications(self):
        """Tests if this user can register for notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer
        notification operations to unauthorized users.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include locations in maps which are
        children of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_resource_location_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_resource_location_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_resource_location_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_resource_location_notification(self, notification_id):
        """Acknowledge a resource location notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_locations(self):
        """Register for notifications of entered locations for a resource.

        ``ResourceLocationReceiver.enteredLocation()`` is invoked when a
        resource appears in a new location.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_location(self, location_id):
        """Register for notifications of an entered location.

        ``ResourceLocationReceiver.enteredLocation()`` is invoked when a
        resource appears in the specified location.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_locations_for_resource(self, resource_id):
        """Register for notifications of entered locations.

        ``ResourceLocationReceiver.enteredLocation()`` is invoked when
        the specified resource appears in a new location.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_locations_for_resources_by_genus_type(self, resource_genus_type):
        """Register for notifications of entered locations for the given resource genus type.

        ``ResourceLocationReceiver.enteredLocation()`` is invoked when a
        resource appears in a new location.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_locations(self):
        """Register for notifications of exited locations for a resource.

        ``ResourceLocationReceiver.exitedLocation()`` is invoked when a
        resource exits a location.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_location(self, location_id):
        """Register for notifications of an exited location.

        ``ResourceLocationReceiver.exitedLocation()`` is invoked when a
        resource exits the specified location.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_locations_for_resource(self, resource_id):
        """Register for notifications of exited locations.

        ``ResourceLocationReceiver.exitedLocation()`` is invoked when
        the specified resource exits a location.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_locations_for_resources_by_genus_type(self, resource_genus_type):
        """Register for notifications of exited locations for the given resource genus type.

        ``ResourceLocationReceiver.exitedLocation()`` is invoked when a
        resource exits a location.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourcePositionNotificationSession:
    """This session defines methods to receive notifications on adds/changes to resource positions in this ``Map``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_register_for_resource_path_notifications(self):
        """Tests if this user can register for notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer
        notification operations to unauthorized users.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_map_view(self):
        """Federates the view for methods in this session.

        A federated view will include positions in maps which are
        children of this map in the map hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this map only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_moved_resources(self):
        """Registers for notification of moved resources.

        ``ResourcePositionReceiver.movedResource()`` is invoked when a
        resource changes coordinates.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_moved_resource(self, resource_id):
        """Registers for notification of moved resources.

        ``ResourcePositionReceiver.movedResource()`` is invoked when the
        specified resource changes coordinates.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_moved_resources_by_genus_type(self, resource_genus_type):
        """Registers for notification of moved resources for the given resource genus type.

        ``ResourcePositionReceiver.movedResource()`` is invoked when a
        resource changes coordinates.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_spatial_unit(self, spatial_unit):
        """Register for notifications of an entered spatial unit.

        ``ResourcePositionReceiver.enteredSpatialUnit()`` is invoked
        when a resource appears in the specified spatial unit.

        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_spatial_unit_for_resource(self, resource_id, spatial_unit):
        """Register for notifications of an entered spatial unit.

        ``ResourcePositionReceiver.enteredSpatialUnit()`` is invoked
        when the specified resource appears in the specified spatial
        unit.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_id`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_entered_spatial_unit_for_resource_by_genus_type(self, resource_genus_type, spatial_unit):
        """Register for notifications of an entered spatial unit for resources of the given resource genus type.

        ``ResourcePositionReceiver.enteredSpatialUnit()`` is invoked
        when the specified resource appears in the specified spatial
        unit.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.id.Id``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_genus_type`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_spatial_unit(self, spatial_unit):
        """Register for notifications of an exited spatial unit.

        ``ResourcePositionReceiver.exitedSpatialUnit()`` is invoked when
        a resource exits the specified spatial unit.

        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_spatial_unit_for_resource(self, resource_id, spatial_unit):
        """Register for notifications of an exited spatial unit.

        ``ResourcePositionReceiver.exitedSpatialUnit()`` is invoked when
        the specified resource exits the specified spatial unit.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_id`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_exited_spatial_unit_for_resources_by_genus_type(self, resource_genus_type, spatial_unit):
        """Register for notifications of an exited spatial unit for the given resource genus type.

        ``ResourcePositionReceiver.exitedSpatialUnit()`` is invoked when
        a resource exits the specified spatial unit.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_genus_t_ype`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class MyLocationSession:
    """This session defines methods to route between locations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_id = abc.abstractproperty(fget=get_map_id)

    @abc.abstractmethod
    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    map = abc.abstractproperty(fget=get_map)

    @abc.abstractmethod
    def can_access_my_location(self):
        """Tests if this user can query own location.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer location
        operations to unauthorized users.

        :return: ``false`` if location methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def at_designated_location(self):
        """Tests if this agent is at a designated location.

        :return: ``true`` if the agent is at a designated location, ``false`` otherrwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_my_location(self):
        """Gets the current location of this agent.

        :return: the current location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``at_designated_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Location

    my_location = abc.abstractproperty(fget=get_my_location)

    @abc.abstractmethod
    def get_my_coordinate(self):
        """Gets the current coordinate of this agent.

        :return: the current coordinate
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    my_coordinate = abc.abstractproperty(fget=get_my_coordinate)

    @abc.abstractmethod
    def get_nearest_locations_to_me(self):
        """Gets the current nearest locations to this agent ordered by distance.

        :return: the nearest locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    nearest_locations_to_me = abc.abstractproperty(fget=get_nearest_locations_to_me)

    @abc.abstractmethod
    def get_nearest_location_to_me_by_genus_type(self, location_genus_type):
        """Gets the current nearest location of this agent of the specified location genus type ordered by distance.

        :param location_genus_type: a location genus type
        :type location_genus_type: ``osid.type.Type``
        :return: the nearest locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList


class MapLookupSession:
    """This session provides methods for retrieving ``Map`` objects.

    The ``Map`` represents a collection of locations.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Maps`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Maps`` referenced
    by it are available, and a test-taking application may sacrifice
    some interoperability for the sake of precision.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_maps(self):
        """Tests if this user can perform ``Map`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_map_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_map_view(self):
        """A complete view of the ``Map`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_map(self, map_id):
        """Gets the ``Map`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Map`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Map`` and retained for compatibility.

        :param map_id: ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.mapping.Map

    @abc.abstractmethod
    def get_maps_by_ids(self, map_ids):
        """Gets a ``MapList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the maps
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Maps`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param map_ids: the list of ``Ids`` to retrieve
        :type map_ids: ``osid.id.IdList``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def get_maps_by_genus_type(self, map_genus_type):
        """Gets a ``MapList`` corresponding to the given map genus ``Type`` which does not include maps of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param map_genus_type: a map genus type
        :type map_genus_type: ``osid.type.Type``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def get_maps_by_parent_genus_type(self, map_genus_type):
        """Gets a ``MapList`` corresponding to the given map genus ``Type`` and include any additional maps with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param map_genus_type: a map genus type
        :type map_genus_type: ``osid.type.Type``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def get_maps_by_record_type(self, map_record_type):
        """Gets a ``MapList`` containing the given map record ``Type``.

        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def get_maps_by_provider(self, resource_id):
        """Gets a ``MapList`` for the given provider.

        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def get_maps(self):
        """Gets all ``Maps``.

        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :return: a list of ``Maps``
        :rtype: ``osid.mapping.MapList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    maps = abc.abstractproperty(fget=get_maps)


class MapQuerySession:
    """This session provides methods for searching among ``Map`` objects.

    The search query is constructed using the ``MapQuery``.

    Maps may have a query record indicated by their respective record
    types. The query record is accessed via the ``MapQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_maps(self):
        """Tests if this user can perform ``Map`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_query(self):
        """Gets a map query.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapQuery

    map_query = abc.abstractproperty(fget=get_map_query)

    @abc.abstractmethod
    def get_maps_by_query(self, map_query):
        """Gets a list of ``Maps`` matching the given map query.

        :param map_query: the map query
        :type map_query: ``osid.mapping.MapQuery``
        :return: the returned ``MapList``
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList


class MapSearchSession:
    """This session provides methods for searching among ``Map`` objects.

    The search query is constructed using the ``MapQuery``.

    ``get_maps_by_query()`` is the basic search method and returns a
    list of ``Maps``. A more advanced search may be performed with
    ``getMapsBySearch()``. It accepts a ``MapSearch`` in addition to the
    query for the purpose of specifying additional options affecting the
    entire search, such as ordering. ``get_maps_by_search()`` returns a
    ``MapSearchResults`` that can be used to access the resulting
    ``MapList`` or be used to perform a search within the result set
    through ``MapSearch``.

    Maps may have a query record indicated by their respective record
    types. The query record is accessed via the ``MapQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_search(self):
        """Gets a map search.

        :return: the map search
        :rtype: ``osid.mapping.MapSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapSearch

    map_search = abc.abstractproperty(fget=get_map_search)

    @abc.abstractmethod
    def get_map_search_order(self):
        """Gets a map search order.

        The ``MapSearchOrder`` is supplied to a ``MapSearch`` to specify
        the ordering of results.

        :return: the map search order
        :rtype: ``osid.mapping.MapSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapSearchOrder

    map_search_order = abc.abstractproperty(fget=get_map_search_order)

    @abc.abstractmethod
    def get_maps_by_search(self, map_query, map_search):
        """Gets the search results matching the given search query using the given search.

        :param map_query: the map query
        :type map_query: ``osid.mapping.MapQuery``
        :param map_search: the map search
        :type map_search: ``osid.mapping.MapSearch``
        :return: the returned search results
        :rtype: ``osid.mapping.MapSearchResults``
        :raise: ``NullArgument`` -- ``map_query`` or ``map_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_query`` or ``map_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapSearchResults

    @abc.abstractmethod
    def get_map_query_from_inspector(self, map_query_inspector):
        """Gets a map query from an inspector.

        The inspector is available from a ``MapSearchResults``.

        :param map_query_inspector: a map query inspector
        :type map_query_inspector: ``osid.mapping.MapQueryInspector``
        :return: the map query
        :rtype: ``osid.mapping.MapQuery``
        :raise: ``NullArgument`` -- ``map_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``map_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapQuery


class MapAdminSession:
    """This session creates, updates, and deletes ``Maps``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Map,`` a ``MapForm`` is requested using
    ``get_map_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``MapForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``MapForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``MapForm`` corresponds
    to an attempted transaction.

    For updates, ``MapForms`` are requested to the ``Map``  ``Id`` that
    is to be updated using ``getMapFormForUpdate()``. Similarly, the
    ``MapForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``MapForm``
    can only be used once for a successful update and cannot be reused.

    The delete operations delete ``Maps``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_maps(self):
        """Tests if this user can create ``Maps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Map``.
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Map`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_map_with_record_types(self, map_record_types):
        """Tests if this user can create a single ``Map`` using the desired record types.

        While ``MappingManager.getMapRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Map``.
        Providing an empty array tests if a ``Map`` can be created with
        no records.

        :param map_record_types: array of map record types
        :type map_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Map`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_form_for_create(self, map_record_types):
        """Gets the map form for creating new maps.

        A new form should be requested for each create transaction.

        :param map_record_types: array of map record types
        :type map_record_types: ``osid.type.Type[]``
        :return: the map form
        :rtype: ``osid.mapping.MapForm``
        :raise: ``NullArgument`` -- ``map_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get a form with given record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapForm

    @abc.abstractmethod
    def create_map(self, map_form):
        """Creates a new ``Map``.

        :param map_form: the form for this ``Map``
        :type map_form: ``osid.mapping.MapForm``
        :return: the new ``Map``
        :rtype: ``osid.mapping.Map``
        :raise: ``IllegalState`` -- ``map_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``map_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_form`` did not originate from ``get_map_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Map

    @abc.abstractmethod
    def can_update_maps(self):
        """Tests if this user can update ``Maps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Map``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Map`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_form_for_update(self, map_id):
        """Gets the map form for updating an existing map.

        A new map form should be requested for each update transaction.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: the map form
        :rtype: ``osid.mapping.MapForm``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapForm

    @abc.abstractmethod
    def update_map(self, map_form):
        """Updates an existing map.

        :param map_form: the form containing the elements to be updated
        :type map_form: ``osid.mapping.MapForm``
        :raise: ``IllegalState`` -- ``map_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``map_id`` or ``map_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_form`` did not originate from ``get_map_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_maps(self):
        """Tests if this user can delete ``Maps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Map``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Map`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_map(self, map_id):
        """Deletes a ``Map``.

        :param map_id: the ``Id`` of the ``Map`` to remove
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_map_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Maps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Map`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_map(self, map_id, alias_id):
        """Adds an ``Id`` to a ``Map`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Map`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another map, it is reassigned to the
        given map ``Id``.

        :param map_id: the ``Id`` of a ``Map``
        :type map_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class MapNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Map`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_map_notifications(self):
        """Tests if this user can register for ``Map`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def reliable_map_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_map_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_map_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_map_notification(self, notification_id):
        """Acknowledge a map notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_maps(self):
        """Register for notifications of new maps.

        ``MapReceiver.newMaps()`` is invoked when a new ``Map`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_maps(self):
        """Registers for notification of updated maps.

        ``MapReceiver.changedMaps()`` is invoked when a map is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_map(self, map_id):
        """Registers for notification of an updated map.

        ``MapReceiver.changedMaps()`` is invoked when the specified map
        is changed.

        :param map_id: the Id of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``E``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_maps(self):
        """Registers for notification of deleted maps.

        ``MapReceiver.deletedMaps()`` is invoked when a map is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_map(self, map_id):
        """Registers for notification of a deleted map.

        ``MapReceiver.deletedMaps()`` is invoked when the specified map
        is deleted.

        :param map_id: the ``Id`` of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_map_hierarchy(self):
        """Registers for notification of an updated map hierarchy structure.

        ``MapReceiver.changedChildOfMaps()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_map_hierarchy_for_ancestors(self, map_id):
        """Registers for notification of an updated map hierarchy structure.

        ``MapReceiver.changedChildOfMaps()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param map_id: the ``Id`` of the ``Map`` node to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_map_hierarchy_for_descendants(self, map_id):
        """Registers for notification of an updated map hierarchy structure.

        ``MapReceiver.changedChildOfMaps()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param map_id: the ``Id`` of the ``Map`` node to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class MapHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Map`` objects.

    Each node in the hierarchy is a unique ``Map``. The hierarchy may be
    traversed recursively to establish the tree structure through
    ``get_parent_maps()`` and ``getChildMaps()``. To relate these
    ``Ids`` to another OSID, ``get_map_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Map`` available in the Mapping OSID is known to this hierarchy but
    does not appear in the hierarchy traversal until added as a root
    location or a child of another location.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_maps()`` or ``get_child_maps()`` in lieu of
    a ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative map view: map elements may be silently omitted or
        re-ordered
      * plenary map view: provides a complete set or is an error
        condition


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_hierarchy_id = abc.abstractproperty(fget=get_map_hierarchy_id)

    @abc.abstractmethod
    def get_map_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    map_hierarchy = abc.abstractproperty(fget=get_map_hierarchy)

    @abc.abstractmethod
    def can_access_map_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_map_view(self):
        """The returns from the map methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_map_view(self):
        """A complete view of the ``Maps`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_map_ids(self):
        """Gets the root map ``Ids`` in this hierarchy.

        :return: the root map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_map_ids = abc.abstractproperty(fget=get_root_map_ids)

    @abc.abstractmethod
    def get_root_maps(self):
        """Gets the root map in the map hierarchy.

        A location with no parents is an orphan. While all map ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root location or child of
        another location.

        :return: the root maps
        :rtype: ``osid.mapping.MapList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.mapping.MapList

    root_maps = abc.abstractproperty(fget=get_root_maps)

    @abc.abstractmethod
    def has_parent_maps(self, map_id):
        """Tests if the ``Map`` has any parents.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the map has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_map(self, id_, map_id):
        """Tests if an ``Id`` is a direct parent of map.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``map_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_map_ids(self, map_id):
        """Gets the parent ``Ids`` of the given map.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the map
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_maps(self, map_id):
        """Gets the parents of the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :return: the parents of the map
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def is_ancestor_of_map(self, id_, map_id):
        """Tests if an ``Id`` is an ancestor of a map.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``map_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_maps(self, map_id):
        """Tests if a map has any children.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the ``map_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_map(self, id_, map_id):
        """Tests if a map is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``map_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_map_ids(self, map_id):
        """Gets the child ``Ids`` of the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :return: the children of the map
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_maps(self, map_id):
        """Gets the children of the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :return: the children of the map
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    @abc.abstractmethod
    def is_descendant_of_map(self, id_, map_id):
        """Tests if an ``Id`` is a descendant of a map.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``map_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_node_ids(self, map_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a map node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_map_nodes(self, map_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a map node
        :rtype: ``osid.mapping.MapNode``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapNode


class MapHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Map`` objects.

    Each node in the hierarchy is a unique ``Map``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    map_hierarchy_id = abc.abstractproperty(fget=get_map_hierarchy_id)

    @abc.abstractmethod
    def get_map_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    map_hierarchy = abc.abstractproperty(fget=get_map_hierarchy)

    @abc.abstractmethod
    def can_modify_map_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_map(self, map_id):
        """Adds a root map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``map_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_map(self, map_id):
        """Removes a root map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not a root
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_map(self, map_id, child_id):
        """Adds a child to a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``map_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``map_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_map(self, map_id, child_id):
        """Removes a child from a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not parent of ``child_id``
        :raise: ``NullArgument`` -- ``map_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_maps(self, map_id):
        """Removes all children from a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
