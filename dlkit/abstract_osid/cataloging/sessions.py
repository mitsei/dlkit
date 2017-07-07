"""Implementations of cataloging abstract base class sessions."""
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


class CatalogSession:
    """This session provides methods to retrieve ``Id`` to ``Catalog`` mappings.

    An Id may appear in multiple ``Catalogs``. Each ``Catalog`` may have
    its own authorizations as to who is allowed to look at it.

    This lookup session defines several views:

      * federated view: entries are accessible from the specified
        ``Catalog`` and any descendant catalogs in the ``Catalog``
        hierarchy
      * isolated view: entries are accessible from the specified
        ``Catalog`` only
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there a particular element is
    inaccessible. For example, a hierarchy output can be plugged into a
    lookup method to retrieve all objects known to a hierarchy, but it
    may not be necessary to break execution if a node from the hierarchy
    no longer exists. However, some administrative applications may need
    to know whether it had retrieved an entire set of objects and may
    sacrifice some interoperability for the sake of precision.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_mappings(self):
        """Tests if this user can perform lookups of ``Id`` to ``Catalog`` mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_catalog_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_catalog_view(self):
        """A complete view of the ``Id`` and ``Catalog`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_catalog_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries from descendant catalogs
        in the catalog hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_catalog_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to the specified catalog
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_ids_by_catalog(self, catalog_id):
        """Gets the list of ``Ids`` map to a ``Catalog``.

        :param catalog_id: a catalog ``Id``
        :type catalog_id: ``osid.id.Id``
        :return: list of ``Ids`` mapped to the given ``catalog_id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_ids_by_catalogs(self, catalog_ids):
        """Gets the list of ``Ids`` map to a lst of ``Catalogs``.

        :param catalog_ids: an ``Id``
        :type catalog_ids: ``osid.id.IdList``
        :return: list of catalogs containing the given ``Id``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``catalog_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_catalog_ids_by_id(self, id_):
        """Gets the ``Catalog Ids`` mapped to an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: list of catalog ``Ids`` containing the given ``Id``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_catalogs_by_id(self, id_):
        """Gets the ``Catalogs`` mapped to an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: list of catalogs containing the given ``Id``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList


class CatalogAssignmentSession:
    """This session provides methods to assign OSID ``Ids`` to ``Catalogs``.

    An ``Id`` may appear in multiple ``Catalogs`` and removing the last
    reference to an ``Id`` is the equivalent of deleting it. Each
    catalog may have its own authorizations as to who is allowed to
    operate on it.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_catalogs(self):
        """Tests if this user can perform alter ``Id/Catalog`` mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def assign_id_to_catalog(self, id_, catalog_id):
        """Adds an ``Id`` to a ``Catalog``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param catalog_id: the ``Id`` of the ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``id`` is already mapped to ``catalog_id``
        :raise: ``NotFound`` -- ``id`` or ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_id_from_catalog(self, id_, catalog_id):
        """Removes an ``Id`` from a ``Catalog``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param catalog_id: the ``Id`` of the ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` or ``catalog_id`` not found or ``id`` is not mapped to ``catalog_id``
        :raise: ``NullArgument`` -- ``id`` or ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_id_to_catalog(self, id_, from_catalog_id, to_catalog_id):
        """Moves an ``Id`` from one ``Catalog`` to another.

        Mappings to other ``Catalogs`` are unaffected.

        :param id: the ``Id``
        :type id: ``osid.id.Id``
        :param from_catalog_id: the ``Id`` of the current ``Catalog``
        :type from_catalog_id: ``osid.id.Id``
        :param to_catalog_id: the ``Id`` of the destination ``Catalog``
        :type to_catalog_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id, from_catalog_id,`` or ``to_catalog_id`` not found or ``id`` not mapped to ``from_catalog_id``
        :raise: ``NullArgument`` -- ``id, from_catalog_id,`` or ``to_catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CatalogEntryNotificationSession:
    """This session defines methods to receive notifications on adds/changes to a catalog assignment.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to assignments of ``Ids``
    to this catalog. For notifications of changes to the ``Catalog``
    object use ``CatalogNotificationSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_id(self):
        """Gets the ``Catalog``  ``Id`` associated with this session.

        :return: the ``Catalog Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    catalog_id = property(fget=get_catalog_id)

    @abc.abstractmethod
    def get_catalog(self):
        """Gets the ``Catalog`` associated with this session.

        :return: the catalog
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.Catalog

    catalog = property(fget=get_catalog)

    @abc.abstractmethod
    def can_register_for_catalog_entry_notifications(self):
        """Tests if this user can register for ``Catalog`` entry notifications.

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
    def use_federated_catalog_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries from parent catalogs in
        the catalog hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_catalog_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for entries to this
        catalog only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_catalog_entry_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_catalog_entry_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_catalog_entry_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_catalog_entry_notification(self, notification_id):
        """Acknowledge a catalog entry notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_catalog_entries(self):
        """Register for notifications of new catalogs.

        ``CatalogEntryReceiver.newCatalogEntries()`` is invoked when a
        new ``Catalog`` entry is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_catalog_entries(self):
        """Registers for notification of deleted catalogs entries.

        ``CatalogEntryReceiver.deletedCatalogEntries()`` is invoked when
        a catalog entry is removed from this catalog.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_catalog_entry_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_catalog_entry_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_catalog_entry_notification(self, notification_id):
        """Acknowledge an catalog_entry notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CatalogLookupSession:
    """This session provides methods for retrieving ``Catalog`` objects.

    The ``Catalog`` represents a collection of OSID ``Ids``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Catalogs`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Catalogs``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_catalogs(self):
        """Tests if this user can perform ``Catalog`` lookups.

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
    def use_comparative_catalog_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_catalog_view(self):
        """A complete view of the ``Catalog`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_catalog(self, catalog_id):
        """Gets the ``Catalog`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Catalog`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Catalog`` and retained for
        compatibility.

        :param catalog_id: ``Id`` of the ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :return: the catalog
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.cataloging.Catalog

    @abc.abstractmethod
    def get_catalogs_by_ids(self, catalog_ids):
        """Gets a ``CatalogList`` corresponding to the given catalog ``IdList``.

        In plenary mode, the returned list contains all of the catalogs
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Catalogs`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param catalog_ids: the list of ``Ids`` to retrieve
        :type catalog_ids: ``osid.id.IdList``
        :return: the returned ``Catalog list``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``catalog_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def get_catalogs_by_genus_type(self, catalog_genus_type):
        """Gets a ``CatalogList`` corresponding to the given catalog genus ``Type`` which does not include catalogs of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known catalogs
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        :param catalog_genus_type: a catalog genus type
        :type catalog_genus_type: ``osid.type.Type``
        :return: the returned ``Catalog list``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NullArgument`` -- ``catalog_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def get_catalogs_by_parent_genus_type(self, catalog_genus_type):
        """Gets a ``CatalogList`` corresponding to the given catalog genus ``Type`` and include any additional catalogs with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known catalogs
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        :param catalog_genus_type: a catalog genus type
        :type catalog_genus_type: ``osid.type.Type``
        :return: the returned ``Catalog list``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NullArgument`` -- ``catalog_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def get_catalogs_by_record_type(self, catalog_record_type):
        """Gets a ``CatalogList`` containing the given subject record ``Type``.

        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        :param catalog_record_type: a catalog record type
        :type catalog_record_type: ``osid.type.Type``
        :return: the returned ``Catalog list``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def get_catalogs_by_provider(self, resource_id):
        """Gets a ``CatalogList`` from the given provider.

        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Catalog list``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def get_catalogs(self):
        """Gets all ``Catalogs``.

        In plenary mode, the returned list contains all known catalogs
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        :return: a list of ``Catalogs``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    catalogs = property(fget=get_catalogs)


class CatalogQuerySession:
    """This session provides methods for searching ``Catalog`` objects.

    The search query is constructed using the ``CatalogQuery``. The
    catalog record ``Type`` also specifies the record for the catalog
    query.

    Catalogs may have a query record indicated by their respective
    record types. The query record is accessed via the ``CatalogQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_catalogs(self):
        """Tests if this user can perform ``Catalog`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_catalog_query(self):
        """Gets a catalog query.

        The returned query will not have an extension query.

        :return: the catalog query
        :rtype: ``osid.cataloging.CatalogQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogQuery

    catalog_query = property(fget=get_catalog_query)

    @abc.abstractmethod
    def get_catalogs_by_query(self, catalog_query):
        """Gets a list of ``Catalogs`` matching the given catalog query.

        :param catalog_query: the catalog query
        :type catalog_query: ``osid.cataloging.CatalogQuery``
        :return: the returned ``CatalogList``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NullArgument`` -- ``catalog_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``catalog_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList


class CatalogSearchSession:
    """This session provides methods for searching ``Catalog`` objects.

    The search query is constructed using the ``CatalogQuery`` . The
    catalog record ``Type`` also specifies the record for the catalog
    query.

    ``get_catalogs_by_query()`` is the basic search method and returns a
    list of ``Catalog`` elements. A more advanced search may be
    performed with ``getCatalogsBySearch()``. It accepts a
    ``CatalogSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_catalogs_by_search()`` returns a
    ``CatalogSearchResults`` that can be used to access the resulting
    ``CatalogList`` or be used to perform a search within the result set
    through ``CatalogSearch``.

    Catalogs may have a query record indicated by their respective
    record types. The query record is accessed via the ``CatalogQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_search(self):
        """Gets a catalog search.

        :return: the catalog search
        :rtype: ``osid.cataloging.CatalogSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogSearch

    catalog_search = property(fget=get_catalog_search)

    @abc.abstractmethod
    def get_catalog_search_order(self):
        """Gets a subject search order.

        The ``CatalogSearchOrder`` is supplied to a ``CatalogSearch`` to
        specify the ordering of results.

        :return: the catalog search order
        :rtype: ``osid.cataloging.CatalogSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogSearchOrder

    catalog_search_order = property(fget=get_catalog_search_order)

    @abc.abstractmethod
    def get_catalogs_by_search(self, catalog_query, catalog_search):
        """Gets the search results matching the given search.

        :param catalog_query: the catalog query
        :type catalog_query: ``osid.cataloging.CatalogQuery``
        :param catalog_search: the catalog search
        :type catalog_search: ``osid.cataloging.CatalogSearch``
        :return: the search results
        :rtype: ``osid.cataloging.CatalogSearchResults``
        :raise: ``NullArgument`` -- ``catalog_query`` or ``catalog_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``catalog_query`` or ``catalog_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogSearchResults

    @abc.abstractmethod
    def get_catalog_query_from_inspector(self, catalog_query_inspector):
        """Gets a catalog query from an inspector.

        The inspector is available from an ``CatalogSearchResults``.

        :param catalog_query_inspector: a catalog query inspector
        :type catalog_query_inspector: ``osid.cataloging.CatalogQueryInspector``
        :return: the catalog query
        :rtype: ``osid.cataloging.CatalogQuery``
        :raise: ``NullArgument`` -- ``catalog_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``catalog_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogQuery


class CatalogAdminSession:
    """This session creates, updates, and deletes ``Catalogs``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Catalog,`` a ``CatalogForm`` is requested using
    ``get_catalog_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``CatalogForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``CatalogForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``CatalogForm``
    corresponds to an attempted transaction.

    For updates, ``CatalogForms`` are requested to the ``Catalog``
    ``Id`` that is to be updated using ``getCatalogFormForUpdate()``.
    Similarly, the ``CatalogForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``CatalogForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Catalogs``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_catalogs(self):
        """Tests if this user can create ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Catalog`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Catalog`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_catalog_with_record_types(self, catalog_record_types):
        """Tests if this user can create a single ``Catalog`` using the desired record types.

        While ``CatalogingManager.getCatalogRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Catalog``.
        Providing an empty array tests if a ``Catalog`` can be created
        with no records.

        :param catalog_record_types: array of catalog record types
        :type catalog_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Catalog`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``catalog_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_catalog_form_for_create(self, catalog_record_types):
        """Gets the catalog form for creating new catalogs.

        A new form should be requested for each create transaction.

        :param catalog_record_types: array of catalog record types
        :type catalog_record_types: ``osid.type.Type[]``
        :return: the catalog form
        :rtype: ``osid.cataloging.CatalogForm``
        :raise: ``NullArgument`` -- ``catalog_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogForm

    @abc.abstractmethod
    def create_catalog(self, catalog_form):
        """Creates a new ``Catalog``.

        :param catalog_form: the form for this ``Catalog``
        :type catalog_form: ``osid.cataloging.CatalogForm``
        :return: the new ``Catalog``
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``IllegalState`` -- ``catalog_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``catalog_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``catalog_form`` did not originate from ``get_catalog_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.Catalog

    @abc.abstractmethod
    def can_update_catalogs(self):
        """Tests if this user can update ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Catalog`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Catalog`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_catalog_form_for_update(self, catalog_id):
        """Gets the catalog form for updating an existing catalog.

        A new catalog form should be requested for each update
        transaction.

        :param catalog_id: the ``Id`` of the ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :return: the catalog form
        :rtype: ``osid.cataloging.CatalogForm``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogForm

    @abc.abstractmethod
    def update_catalog(self, catalog_form):
        """Updates an existing catalog.

        :param catalog_form: the form containing the elements to be updated
        :type catalog_form: ``osid.cataloging.CatalogForm``
        :raise: ``IllegalState`` -- ``catalog_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``catalog_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``catalog_form`` did not originate from ``get_catalog_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_catalogs(self):
        """Tests if this user can delete ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Catalog`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Catalog`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_catalog(self, catalog_id):
        """Deletes a ``Catalog``.

        :param catalog_id: the ``Id`` of the ``Catalog`` to remove
        :type catalog_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_catalog_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Catalog`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_catalog(self, catalog_id, alias_id):
        """Adds an ``Id`` to a ``Catalog`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Catalog`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another catalog, it is
        reassigned to the given catalog ``Id``.

        :param catalog_id: the ``Id`` of a ``Catalog``
        :type catalog_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CatalogNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Catalog`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to the ``Catalog`` object
    itself. Adding and removing ``Ids`` result in notifications
    available from the notification session for catalog entries.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_catalog_notifications(self):
        """Tests if this user can register for ``Catalog`` notifications.

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
    def reliable_catalog_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_catalog_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_catalog_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_catalog_notification(self, notification_id):
        """Acknowledge a catalog notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_catalogs(self):
        """Register for notifications of new catalogs.

        ``CatalogReceiver.newCatalogs()`` is invoked when a new
        ``Catalog`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_catalogs(self):
        """Registers for notification of updated catalogs.

        ``CatalogReceiver.changedCatalogs()`` is invoked when a catalog
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_catalog(self, catalog_id):
        """Registers for notification of an updated catalog.

        ``CatalogReceiver.changedCatalogs()`` is invoked when the
        specified catalog is changed.

        :param catalog_id: the ``Id`` of the ``Catalog`` to monitor
        :type catalog_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_catalogs(self):
        """Registers for notification of deleted catalogs.

        ``CatalogReceiver.deletedCatalogs()`` is invoked when a catalog
        is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_catalog(self, catalog_id):
        """Registers for notification of a deleted catalog.

        ``CatalogReceiver.deletedCatalogs()`` is invoked when the
        specified catalog is deleted.

        :param catalog_id: the ``Id`` of the ``Catalog`` to monitor
        :type catalog_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_catalog_hierarchy(self):
        """Registers for notification of an updated catalog hierarchy structure.

        ``CatalogReceiver.changedChildOfCatalogs()`` is invoked when a
        node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_catalog_hierarchy_for_ancestors(self, catalog_id):
        """Catalog ``Receiver.

        changedChildOfCatalogs()`` is invoked when the specified node or
        any of its ancestors experiences a change in its children.

        :param catalog_id: the ``Id`` of the ``Catalog`` node to monitor
        :type catalog_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_catalog_hierarchy_for_descendants(self, catalog_id):
        """Registers for notification of an updated catalog hierarchy structure.

        ``CatalogReceiver.changedChildOfCatalogs()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param catalog_id: the ``Id`` of the ``catalog`` node to monitor
        :type catalog_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_catalog_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_catalog_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_catalog_notification(self, notification_id):
        """Acknowledge an catalog notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CatalogHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Catalog`` objects.

    Each node in the hierarchy is a unique ``Catalog``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_catalogs()`` and ``getChildCatalogs()``. To relate
    these ``Ids`` to another OSID, ``get_catalog_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Catalog`` available in the Catalog OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_catalogs()`` or ``get_child_catalogs()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: catalog elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    @abc.abstractmethod
    def get_catalog_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    @abc.abstractmethod
    def can_access_catalog_hierarchy(self):
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
    def use_comparative_catalog_view(self):
        """The returns from the catalog methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_catalog_view(self):
        """A complete view of the ``Catalog`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_catalog_ids(self):
        """Gets the root catalog ``Ids`` in this hierarchy.

        :return: the root catalog ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_catalog_ids = property(fget=get_root_catalog_ids)

    @abc.abstractmethod
    def get_root_catalogs(self):
        """Gets the root catalogs in the catalog hierarchy.

        A node with no parents is an orphan. While all catalog ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root catalogs
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    root_catalogs = property(fget=get_root_catalogs)

    @abc.abstractmethod
    def has_parent_catalogs(self, catalog_id):
        """Tests if the ``Catalog`` has any parents.

        :param catalog_id: a catalog ``Id``
        :type catalog_id: ``osid.id.Id``
        :return: ``true`` if the catalog has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_catalog(self, id_, catalog_id):
        """Tests if an ``Id`` is a direct parent of a catalog.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``catalog_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_catalog_ids(self, catalog_id):
        """Gets the parent ``Ids`` of the given catalog.

        :param catalog_id: a catalog ``Id``
        :type catalog_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the catalog
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_catalogs(self, catalog_id):
        """Gets the parent catalogs of the given ``id``.

        :param catalog_id: the ``Id`` of the ``Catalog`` to query
        :type catalog_id: ``osid.id.Id``
        :return: the parent catalogs of the ``id``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NotFound`` -- a ``Catalog`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def is_ancestor_of_catalog(self, id_, catalog_id):
        """Tests if an ``Id`` is an ancestor of a catalog.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``catalogId``.  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_catalogs(self, catalog_id):
        """Tests if a catalog has any children.

        :param catalog_id: a ``catalog_id``
        :type catalog_id: ``osid.id.Id``
        :return: ``true`` if the ``catalog_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_catalog(self, id_, catalog_id):
        """Tests if a catalog is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``catalog_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_catalog_ids(self, catalog_id):
        """Gets the child ``Ids`` of the given catalog.

        :param catalog_id: the ``Id`` to query
        :type catalog_id: ``osid.id.Id``
        :return: the children of the catalog
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``catalog_id`` is not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_catalogs(self, catalog_id):
        """Gets the child catalogs of the given ``id``.

        :param catalog_id: the ``Id`` of the ``Catalog`` to query
        :type catalog_id: ``osid.id.Id``
        :return: the child catalogs of the ``id``
        :rtype: ``osid.cataloging.CatalogList``
        :raise: ``NotFound`` -- a ``Catalog`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogList

    @abc.abstractmethod
    def is_descendant_of_catalog(self, id_, catalog_id):
        """Tests if an ``Id`` is a descendant of a catalog.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``catalog_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_catalog_node_ids(self, catalog_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given catalog.

        :param catalog_id: the ``Id`` to query
        :type catalog_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- a ``Catalog`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_catalog_nodes(self, catalog_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given catalog.

        :param catalog_id: the ``Id`` to query
        :type catalog_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.cataloging.CatalogNode``
        :raise: ``NotFound`` -- a ``Catalog`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNode


class CatalogHierarchyDesignSession:
    """This session manages a hierarchy of catalogs.

    ``Catalogs`` may be organized into a hierarchy for organizing or
    federating. A parent ``Catalog`` includes all of the Ids of its
    children such that a single root node contains all of the ``Ids`` of
    the federation.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    @abc.abstractmethod
    def get_catalog_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    @abc.abstractmethod
    def can_modify_catalog_hierarchy(self):
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
    def add_root_catalog(self, catalog_id):
        """Adds a root catalog.

        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``catalog_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``catalog_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_catalog(self, catalog_id):
        """Removes a root catalog.

        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``catalog_id`` is not a root
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_catalog(self, catalog_id, child_id):
        """Adds a child to a catalog.

        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``catalog_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``catalog_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``catalog_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_catalog(self, catalog_id, child_id):
        """Removes a child from a catalog.

        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``catalog_id`` is not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``catalog_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_catalogs(self, catalog_id):
        """Removes all children from a catalog.

        :param catalog_id: the ``Id`` of a catalog
        :type catalog_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``catalog_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``catalog_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
