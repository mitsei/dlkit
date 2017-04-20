"""Manager utility implementations of commenting managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import NullArgument
from ..osid.osid_errors import Unimplemented
from ..type.objects import TypeList
from dlkit.abstract_osid.commenting import managers as abc_commenting_managers


class CommentingProfile(abc_commenting_managers.CommentingProfile, osid_managers.OsidProfile):
    """The commenting profile describes the interoperability among commenting services."""

    def supports_visible_federation(self):
        """Tests if any book federation is exposed.

        Federation is exposed when a specific book may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of books appears as a
        single book.

        return: (boolean) - ``true`` if visible federation is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_lookup(self):
        """Tests for the availability of a comment lookup service.

        return: (boolean) - ``true`` if comment lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_rating_lookup(self):
        """Tests for the availability of a rating lookup service.

        return: (boolean) - ``true`` if rating lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_query(self):
        """Tests if querying comments is available.

        return: (boolean) - ``true`` if comment query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_search(self):
        """Tests if searching for comments is available.

        return: (boolean) - ``true`` if comment search is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_admin(self):
        """Tests if managing comments is available.

        return: (boolean) - ``true`` if comment admin is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_notification(self):
        """Tests if comment notification is available.

        return: (boolean) - ``true`` if comment notification is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_book(self):
        """Tests if a comment to book lookup session is available.

        return: (boolean) - ``true`` if comment book lookup session is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_book_assignment(self):
        """Tests if a comment to book assignment session is available.

        return: (boolean) - ``true`` if comment book assignment is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_comment_smart_book(self):
        """Tests if a comment smart booking session is available.

        return: (boolean) - ``true`` if comment smart booking is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_book_lookup(self):
        """Tests for the availability of an book lookup service.

        return: (boolean) - ``true`` if book lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_book_query(self):
        """Tests if querying books is available.

        return: (boolean) - ``true`` if book query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_book_search(self):
        """Tests if searching for books is available.

        return: (boolean) - ``true`` if book search is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_book_admin(self):
        """Tests for the availability of a book administrative service for creating and deleting books.

        return: (boolean) - ``true`` if book administration is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_book_notification(self):
        """Tests for the availability of a book notification service.

        return: (boolean) - ``true`` if book notification is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def supports_book_hierarchy(self):
        """Tests for the availability of a book hierarchy traversal service.

        return: (boolean) - ``true`` if book hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_book_hierarchy_design(self):
        """Tests for the availability of a book hierarchy design service.

        return: (boolean) - ``true`` if book hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def supports_commenting_batch(self):
        """Tests for the availability of a commenting batch service.

        return: (boolean) - ``true`` if commenting batch service is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def get_comment_record_types(self):
        """Gets the supported ``Comment`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                comment record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    comment_record_types = property(fget=get_comment_record_types)

    def supports_comment_record_type(self, comment_record_type=None):
        """Tests if the given ``Comment`` record type is supported.

        arg:    comment_record_type (osid.type.Type): a ``Type``
                indicating a ``Comment`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``comment_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if comment_record_type is None:
            raise NullArgument()
        return False

    def get_comment_search_record_types(self):
        """Gets the supported comment search record types.

        return: (osid.type.TypeList) - a list containing the supported
                comment search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def supports_comment_search_record_type(self, comment_search_record_type=None):
        """Tests if the given comment search record type is supported.

        arg:    comment_search_record_type (osid.type.Type): a ``Type``
                indicating a comment record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``comment_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if comment_search_record_type is None:
            raise NullArgument()
        return False

    def get_book_record_types(self):
        """Gets the supported ``Book`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                book record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    book_record_types = property(fget=get_book_record_types)

    def supports_book_record_type(self, book_record_type=None):
        """Tests if the given ``Book`` record type is supported.

        arg:    book_record_type (osid.type.Type): a ``Type`` indicating
                a ``Book`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``book_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if book_record_type is None:
            raise NullArgument()
        return False

    def get_book_search_record_types(self):
        """Gets the supported book search record types.

        return: (osid.type.TypeList) - a list containing the supported
                book search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    book_search_record_types = property(fget=get_book_search_record_types)

    def supports_book_search_record_type(self, book_search_record_type=None):
        """Tests if the given book search record type is supported.

        arg:    book_search_record_type (osid.type.Type): a ``Type``
                indicating a book record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``book_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if book_search_record_type is None:
            raise NullArgument()
        return False


class CommentingManager(abc_commenting_managers.CommentingManager, osid_managers.OsidManager, CommentingProfile):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``CommentLookupSession:`` a session to lookup comments
      * ``RatingLookupSession:`` a session to lookup comments
      * ``CommentQuerySession:`` a session to query comments
      * ``CommentSearchSession:`` a session to search comments
      * ``CommentAdminSession:`` a session to manage comments
      * ``CommentNotificationSession:`` a session to subscribe to
        notifications of comment changes
      * ``CommentBookSession:`` a session for looking up comment and
        book mappings
      * ``CommentBookAssignmentSession:`` a session for managing comment
        and book mappings
      * ``CommentSmartBookSession:`` a session to manage dynamic comment
        books
      * ``BookLookupSession:`` a session to retrieve books
      * ``BookQuerySession:`` a session to query books
      * ``BookSearchSession:`` a session to search for books
      * ``BookAdminSession:`` a session to create, update and delete
        books
      * ``BookNotificationSession:`` a session to receive notifications
        for changes in books
      * ``BookHierarchyTraversalSession:`` a session to traverse
        hierarchies of books
      * ``BookHierarchyDesignSession:`` a session to manage hierarchies
        of books


    The commenting manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def get_comment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    comment_lookup_session = property(fget=get_comment_lookup_session)

    def get_comment_lookup_session_for_book(self, book_id=None):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_rating_lookup_session(self):
        """Gets the ``OsidSession`` associated with the rating lookup service.

        return: (osid.commenting.RatingLookupSession) - a
                ``RatingLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_rating_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    rating_lookup_session = property(fget=get_rating_lookup_session)

    def get_rating_lookup_session_for_book(self, book_id=None):
        """Gets the ``OsidSession`` associated with the rating lookup service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.RatingLookupSession) - a
                ``RatingLookupSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_rating_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_query_session(self):
        """Gets the ``OsidSession`` associated with the comment query service.

        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        raise Unimplemented()

    comment_query_session = property(fget=get_comment_query_session)

    def get_comment_query_session_for_book(self, book_id=None):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_search_session(self):
        """Gets the ``OsidSession`` associated with the comment search service.

        return: (osid.commenting.CommentSearchSession) - a
                ``CommentSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` is ``true``.*

        """
        raise Unimplemented()

    comment_search_session = property(fget=get_comment_search_session)

    def get_comment_search_session_for_book(self, book_id=None):
        """Gets the ``OsidSession`` associated with the comment search service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentSearchSession) - a
                ``CommentSearchSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_admin_session(self):
        """Gets the ``OsidSession`` associated with the comment administration service.

        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` is ``true``.*

        """
        raise Unimplemented()

    comment_admin_session = property(fget=get_comment_admin_session)

    def get_comment_admin_session_for_book(self, book_id=None):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_notification_session(self, comment_receiver=None):
        """Gets the ``OsidSession`` associated with the comment notification service.

        arg:    comment_receiver (osid.commenting.CommentReceiver): the
                receiver
        return: (osid.commenting.CommentNotificationSession) - a
                ``CommentNotificationSession``
        raise:  NullArgument - ``comment_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_comment_notification_session_for_book(self, comment_receiver=None, book_id=None):
        """Gets the ``OsidSession`` associated with the comment notification service for the given book.

        arg:    comment_receiver (osid.commenting.CommentReceiver): the
                receiver
        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentNotificationSession) - a
                ``CommentNotificationSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``comment_receiver`` or ``book_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if comment_receiver is None:
            raise NullArgument
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_book_session(self):
        """Gets the session for retrieving comment to book mappings.

        return: (osid.commenting.CommentBookSession) - a
                ``CommentBookSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_book()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_book()`` is ``true``.*

        """
        raise Unimplemented()

    comment_book_session = property(fget=get_comment_book_session)

    def get_comment_book_assignment_session(self):
        """Gets the session for assigning comment to book mappings.

        return: (osid.commenting.CommentBookAssignmentSession) - a
                ``CommentBookAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_book_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_book_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    comment_book_assignment_session = property(fget=get_comment_book_assignment_session)

    def get_comment_smart_book_session(self, book_id=None):
        """Gets the session associated with the comment smart book for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the book
        return: (osid.commenting.CommentSmartBookSession) - a
                ``CommentSmartBookSession``
        raise:  NotFound - ``book_id`` not found
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_smart_book()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_smart_book()`` is ``true``.*

        """
        if book_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_book_lookup_session(self):
        """Gets the ``OsidSession`` associated with the book lookup service.

        return: (osid.commenting.BookLookupSession) - a
                ``BookLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    book_lookup_session = property(fget=get_book_lookup_session)

    def get_book_query_session(self):
        """Gets the ``OsidSession`` associated with the book query service.

        return: (osid.commenting.BookQuerySession) - a
                ``BookQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_query()`` is ``true``.*

        """
        raise Unimplemented()

    book_query_session = property(fget=get_book_query_session)

    def get_book_search_session(self):
        """Gets the ``OsidSession`` associated with the book search service.

        return: (osid.commenting.BookSearchSession) - a
                ``BookSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_search()`` is ``true``.*

        """
        raise Unimplemented()

    book_search_session = property(fget=get_book_search_session)

    def get_book_admin_session(self):
        """Gets the ``OsidSession`` associated with the book administrative service.

        return: (osid.commenting.BookAdminSession) - a
                ``BookAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_admin()`` is ``true``.*

        """
        raise Unimplemented()

    book_admin_session = property(fget=get_book_admin_session)

    def get_book_notification_session(self, book_receiver=None):
        """Gets the ``OsidSession`` associated with the book notification service.

        arg:    book_receiver (osid.commenting.BookReceiver): the
                receiver
        return: (osid.commenting.BookNotificationSession) - a
                ``BookNotificationSession``
        raise:  NullArgument - ``book_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_book_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        return: (osid.commenting.BookHierarchySession) - a
                ``BookHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy()`` is ``true``.*

        """
        raise Unimplemented()

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    def get_book_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        return: (osid.commenting.BookHierarchyDesignSession) - a
                ``BookHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy_design()`` is ``true``.*

        """
        raise Unimplemented()

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    def get_commenting_batch_manager(self):
        """Gets a ``CommentingBatchManager``.

        return: (osid.commenting.batch.CommentingBatchManager) - a
                ``CommentingBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_commenting_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        raise Unimplemented()

    commenting_batch_manager = property(fget=get_commenting_batch_manager)


class CommentingProxyManager(abc_commenting_managers.CommentingProxyManager, osid_managers.OsidProxyManager, CommentingProfile):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from a server environment. The sessions included in this manager
    are:

      * ``CommentLookupSession:`` a session to lookup comments
      * ``RatingLookupSession:`` a session to lookup comments
      * ``CommentQuerySession:`` a session to query comments
      * ``CommentSearchSession:`` a session to search comments
      * ``CommentAdminSession:`` a session to manage comments
      * ``CommentNotificationSession:`` a session to subscribe to
        notifications of comment changes
      * ``CommentBookSession:`` a session for looking up comment and
        book mappings
      * ``CommentBookAssignmentSession:`` a session for managing comment
        and book mappings
      * ``CommentSmartBookSession:`` a session to manage dynamic comment
        books
      * ``BookLookupSession:`` a session to retrieve books
      * ``BookQuerySession:`` a session to query books
      * ``BookSearchSession:`` a session to search for books
      * ``BookAdminSession:`` a session to create, update and delete
        books
      * ``BookNotificationSession:`` a session to receive notifications
        for changes in books
      * ``BookHierarchyTraversalSession:`` a session to traverse
        hierarchies of books
      * ``BookHierarchyDesignSession:`` a session to manage hierarchies
        of books


    The commenting manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def get_comment_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_lookup_session_for_book(self, book_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_rating_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the rating lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.RatingLookupSession) - a
                ``RatingLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_rating_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_rating_lookup_session_for_book(self, book_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the rating lookup service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.RatingLookupSession) - a
                ``RatingLookupSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_rating_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the comment query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_query_session_for_book(self, book_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  NotFound - no ``Comment`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the comment search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentSearchSession) - a
                ``CommentSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_search_session_for_book(self, book_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the comment search service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentSearchSession) - a
                ``CommentSearchSession``
        raise:  NotFound - no ``Comment`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the comment administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_admin_session_for_book(self, book_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  NotFound - no ``Comment`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if book_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_notification_session(self, comment_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the comment notification service.

        arg:    comment_receiver (osid.commenting.CommentReceiver): the
                receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentNotificationSession) - a
                ``CommentNotificationSession``
        raise:  NullArgument - ``comment_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_notification_session_for_book(self, comment_receiver=None, book_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the comment notification service for the given book.

        arg:    comment_receiver (osid.commenting.CommentReceiver): the
                receiver
        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentNotificationSession) - a
                ``CommentNotificationSession``
        raise:  NotFound - no ``Comment`` found by the given ``Id``
        raise:  NullArgument - ``comment_receiver, book_id`` or
                ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if comment_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_comment_book_session(self, proxy=None):
        """Gets the session for retrieving comment to book mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentBookSession) - a
                ``CommentBookSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_book()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_book()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_book_assignment_session(self, proxy=None):
        """Gets the session for assigning comment to book mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentBookAssignmentSession) - a
                ``CommentBookAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_book_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_book_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_comment_smart_book_session(self, book_id=None, proxy=None):
        """Gets the session for managing dynamic comment books for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of a book
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentSmartBookSession) - ``book_id``
                not found
        raise:  NotFound - ``book_id`` or ``proxy`` is ``null``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_smart_book()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_smart_book()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the book lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookLookupSession) - a
                ``BookLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the book query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookQuerySession) - a
                ``BookQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_queryh()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the book search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookSearchSession) - a
                ``BookSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the book administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookAdminSession) - a
                ``BookAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_notification_session(self, book_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the book notification service.

        arg:    book_receiver (osid.commenting.BookReceiver): the
                receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookNotificationSession) - a
                ``BookNotificationSession``
        raise:  NullArgument - ``book_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_hierarchy_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookHierarchySession) - a
                ``BookHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_book_hierarchy_design_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookHierarchyDesignSession) - a
                ``BookHierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy_design()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_commenting_batch_proxy_manager(self):
        """Gets a ``CommentingBatchProxyManager``.

        return: (osid.commenting.batch.CommentingBatchProxyManager) - a
                ``CommentingBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_commenting_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)
