"""Implementations of commenting abstract base class managers."""
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


class CommentingProfile:
    """The commenting profile describes the interoperability among commenting services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if any book federation is exposed.

        Federation is exposed when a specific book may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of books appears as a
        single book.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_lookup(self):
        """Tests for the availability of a comment lookup service.

        :return: ``true`` if comment lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_rating_lookup(self):
        """Tests for the availability of a rating lookup service.

        :return: ``true`` if rating lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_query(self):
        """Tests if querying comments is available.

        :return: ``true`` if comment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_search(self):
        """Tests if searching for comments is available.

        :return: ``true`` if comment search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_admin(self):
        """Tests if managing comments is available.

        :return: ``true`` if comment admin is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_notification(self):
        """Tests if comment notification is available.

        :return: ``true`` if comment notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_book(self):
        """Tests if a comment to book lookup session is available.

        :return: ``true`` if comment book lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_book_assignment(self):
        """Tests if a comment to book assignment session is available.

        :return: ``true`` if comment book assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_comment_smart_book(self):
        """Tests if a comment smart booking session is available.

        :return: ``true`` if comment smart booking is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_lookup(self):
        """Tests for the availability of an book lookup service.

        :return: ``true`` if book lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_query(self):
        """Tests if querying books is available.

        :return: ``true`` if book query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_search(self):
        """Tests if searching for books is available.

        :return: ``true`` if book search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_admin(self):
        """Tests for the availability of a book administrative service for creating and deleting books.

        :return: ``true`` if book administration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_notification(self):
        """Tests for the availability of a book notification service.

        :return: ``true`` if book notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_hierarchy(self):
        """Tests for the availability of a book hierarchy traversal service.

        :return: ``true`` if book hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_book_hierarchy_design(self):
        """Tests for the availability of a book hierarchy design service.

        :return: ``true`` if book hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_commenting_batch(self):
        """Tests for the availability of a commenting batch service.

        :return: ``true`` if commenting batch service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_record_types(self):
        """Gets the supported ``Comment`` record types.

        :return: a list containing the supported comment record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    comment_record_types = property(fget=get_comment_record_types)

    @abc.abstractmethod
    def supports_comment_record_type(self, comment_record_type):
        """Tests if the given ``Comment`` record type is supported.

        :param comment_record_type: a ``Type`` indicating a ``Comment`` record type
        :type comment_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_search_record_types(self):
        """Gets the supported comment search record types.

        :return: a list containing the supported comment search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    comment_search_record_types = property(fget=get_comment_search_record_types)

    @abc.abstractmethod
    def supports_comment_search_record_type(self, comment_search_record_type):
        """Tests if the given comment search record type is supported.

        :param comment_search_record_type: a ``Type`` indicating a comment record type
        :type comment_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``comment_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_record_types(self):
        """Gets the supported ``Book`` record types.

        :return: a list containing the supported book record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    book_record_types = property(fget=get_book_record_types)

    @abc.abstractmethod
    def supports_book_record_type(self, book_record_type):
        """Tests if the given ``Book`` record type is supported.

        :param book_record_type: a ``Type`` indicating a ``Book`` record type
        :type book_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_search_record_types(self):
        """Gets the supported book search record types.

        :return: a list containing the supported book search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    book_search_record_types = property(fget=get_book_search_record_types)

    @abc.abstractmethod
    def supports_book_search_record_type(self, book_search_record_type):
        """Tests if the given book search record type is supported.

        :param book_search_record_type: a ``Type`` indicating a book record type
        :type book_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class CommentingManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_comment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` is ``true``.*

        """
        return  # osid.commenting.CommentLookupSession

    comment_lookup_session = property(fget=get_comment_lookup_session)

    @abc.abstractmethod
    def get_comment_lookup_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentLookupSession

    @abc.abstractmethod
    def get_rating_lookup_session(self):
        """Gets the ``OsidSession`` associated with the rating lookup service.

        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` is ``true``.*

        """
        return  # osid.commenting.RatingLookupSession

    rating_lookup_session = property(fget=get_rating_lookup_session)

    @abc.abstractmethod
    def get_rating_lookup_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the rating lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.RatingLookupSession

    @abc.abstractmethod
    def get_comment_query_session(self):
        """Gets the ``OsidSession`` associated with the comment query service.

        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        return  # osid.commenting.CommentQuerySession

    comment_query_session = property(fget=get_comment_query_session)

    @abc.abstractmethod
    def get_comment_query_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentQuerySession

    @abc.abstractmethod
    def get_comment_search_session(self):
        """Gets the ``OsidSession`` associated with the comment search service.

        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` is ``true``.*

        """
        return  # osid.commenting.CommentSearchSession

    comment_search_session = property(fget=get_comment_search_session)

    @abc.abstractmethod
    def get_comment_search_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment search service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentSearchSession

    @abc.abstractmethod
    def get_comment_admin_session(self):
        """Gets the ``OsidSession`` associated with the comment administration service.

        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` is ``true``.*

        """
        return  # osid.commenting.CommentAdminSession

    comment_admin_session = property(fget=get_comment_admin_session)

    @abc.abstractmethod
    def get_comment_admin_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentAdminSession

    @abc.abstractmethod
    def get_comment_notification_session(self, comment_receiver):
        """Gets the ``OsidSession`` associated with the comment notification service.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NullArgument`` -- ``comment_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` is ``true``.*

        """
        return  # osid.commenting.CommentNotificationSession

    @abc.abstractmethod
    def get_comment_notification_session_for_book(self, comment_receiver, book_id):
        """Gets the ``OsidSession`` associated with the comment notification service for the given book.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_receiver`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentNotificationSession

    @abc.abstractmethod
    def get_comment_book_session(self):
        """Gets the session for retrieving comment to book mappings.

        :return: a ``CommentBookSession``
        :rtype: ``osid.commenting.CommentBookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_book()`` is ``true``.*

        """
        return  # osid.commenting.CommentBookSession

    comment_book_session = property(fget=get_comment_book_session)

    @abc.abstractmethod
    def get_comment_book_assignment_session(self):
        """Gets the session for assigning comment to book mappings.

        :return: a ``CommentBookAssignmentSession``
        :rtype: ``osid.commenting.CommentBookAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_book_assignment()`` is ``true``.*

        """
        return  # osid.commenting.CommentBookAssignmentSession

    comment_book_assignment_session = property(fget=get_comment_book_assignment_session)

    @abc.abstractmethod
    def get_comment_smart_book_session(self, book_id):
        """Gets the session associated with the comment smart book for the given book.

        :param book_id: the ``Id`` of the book
        :type book_id: ``osid.id.Id``
        :return: a ``CommentSmartBookSession``
        :rtype: ``osid.commenting.CommentSmartBookSession``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_smart_book()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_smart_book()`` is ``true``.*

        """
        return  # osid.commenting.CommentSmartBookSession

    @abc.abstractmethod
    def get_book_lookup_session(self):
        """Gets the ``OsidSession`` associated with the book lookup service.

        :return: a ``BookLookupSession``
        :rtype: ``osid.commenting.BookLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        return  # osid.commenting.BookLookupSession

    book_lookup_session = property(fget=get_book_lookup_session)

    @abc.abstractmethod
    def get_book_query_session(self):
        """Gets the ``OsidSession`` associated with the book query service.

        :return: a ``BookQuerySession``
        :rtype: ``osid.commenting.BookQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_query()`` is ``true``.*

        """
        return  # osid.commenting.BookQuerySession

    book_query_session = property(fget=get_book_query_session)

    @abc.abstractmethod
    def get_book_search_session(self):
        """Gets the ``OsidSession`` associated with the book search service.

        :return: a ``BookSearchSession``
        :rtype: ``osid.commenting.BookSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_search()`` is ``true``.*

        """
        return  # osid.commenting.BookSearchSession

    book_search_session = property(fget=get_book_search_session)

    @abc.abstractmethod
    def get_book_admin_session(self):
        """Gets the ``OsidSession`` associated with the book administrative service.

        :return: a ``BookAdminSession``
        :rtype: ``osid.commenting.BookAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_admin()`` is ``true``.*

        """
        return  # osid.commenting.BookAdminSession

    book_admin_session = property(fget=get_book_admin_session)

    @abc.abstractmethod
    def get_book_notification_session(self, book_receiver):
        """Gets the ``OsidSession`` associated with the book notification service.

        :param book_receiver: the receiver
        :type book_receiver: ``osid.commenting.BookReceiver``
        :return: a ``BookNotificationSession``
        :rtype: ``osid.commenting.BookNotificationSession``
        :raise: ``NullArgument`` -- ``book_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_notification()`` is ``true``.*

        """
        return  # osid.commenting.BookNotificationSession

    @abc.abstractmethod
    def get_book_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        :return: a ``BookHierarchySession``
        :rtype: ``osid.commenting.BookHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy()`` is ``true``.*

        """
        return  # osid.commenting.BookHierarchySession

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    @abc.abstractmethod
    def get_book_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        :return: a ``BookHierarchyDesignSession``
        :rtype: ``osid.commenting.BookHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy_design()`` is ``true``.*

        """
        return  # osid.commenting.BookHierarchyDesignSession

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    @abc.abstractmethod
    def get_commenting_batch_manager(self):
        """Gets a ``CommentingBatchManager``.

        :return: a ``CommentingBatchManager``
        :rtype: ``osid.commenting.batch.CommentingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        return  # osid.commenting.batch.CommentingBatchManager

    commenting_batch_manager = property(fget=get_commenting_batch_manager)


class CommentingProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_comment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` is ``true``.*

        """
        return  # osid.commenting.CommentLookupSession

    @abc.abstractmethod
    def get_comment_lookup_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentLookupSession

    @abc.abstractmethod
    def get_rating_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rating lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` is ``true``.*

        """
        return  # osid.commenting.RatingLookupSession

    @abc.abstractmethod
    def get_rating_lookup_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the rating lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rating_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.RatingLookupSession

    @abc.abstractmethod
    def get_comment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        return  # osid.commenting.CommentQuerySession

    @abc.abstractmethod
    def get_comment_query_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentQuerySession

    @abc.abstractmethod
    def get_comment_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` is ``true``.*

        """
        return  # osid.commenting.CommentSearchSession

    @abc.abstractmethod
    def get_comment_search_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment search service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentSearchSession

    @abc.abstractmethod
    def get_comment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` is ``true``.*

        """
        return  # osid.commenting.CommentAdminSession

    @abc.abstractmethod
    def get_comment_admin_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentAdminSession

    @abc.abstractmethod
    def get_comment_notification_session(self, comment_receiver, proxy):
        """Gets the ``OsidSession`` associated with the comment notification service.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NullArgument`` -- ``comment_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` is ``true``.*

        """
        return  # osid.commenting.CommentNotificationSession

    @abc.abstractmethod
    def get_comment_notification_session_for_book(self, comment_receiver, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment notification service for the given book.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_receiver, book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.commenting.CommentNotificationSession

    @abc.abstractmethod
    def get_comment_book_session(self, proxy):
        """Gets the session for retrieving comment to book mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentBookSession``
        :rtype: ``osid.commenting.CommentBookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_book()`` is ``true``.*

        """
        return  # osid.commenting.CommentBookSession

    @abc.abstractmethod
    def get_comment_book_assignment_session(self, proxy):
        """Gets the session for assigning comment to book mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentBookAssignmentSession``
        :rtype: ``osid.commenting.CommentBookAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_book_assignment()`` is ``true``.*

        """
        return  # osid.commenting.CommentBookAssignmentSession

    @abc.abstractmethod
    def get_comment_smart_book_session(self, book_id, proxy):
        """Gets the session for managing dynamic comment books for the given book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``book_id`` not found
        :rtype: ``osid.commenting.CommentSmartBookSession``
        :raise: ``NotFound`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_smart_book()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_smart_book()`` is ``true``.*

        """
        return  # osid.commenting.CommentSmartBookSession

    @abc.abstractmethod
    def get_book_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookLookupSession``
        :rtype: ``osid.commenting.BookLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        return  # osid.commenting.BookLookupSession

    @abc.abstractmethod
    def get_book_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookQuerySession``
        :rtype: ``osid.commenting.BookQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_queryh()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_query()`` is ``true``.*

        """
        return  # osid.commenting.BookQuerySession

    @abc.abstractmethod
    def get_book_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookSearchSession``
        :rtype: ``osid.commenting.BookSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_search()`` is ``true``.*

        """
        return  # osid.commenting.BookSearchSession

    @abc.abstractmethod
    def get_book_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookAdminSession``
        :rtype: ``osid.commenting.BookAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_admin()`` is ``true``.*

        """
        return  # osid.commenting.BookAdminSession

    @abc.abstractmethod
    def get_book_notification_session(self, book_receiver, proxy):
        """Gets the ``OsidSession`` associated with the book notification service.

        :param book_receiver: the receiver
        :type book_receiver: ``osid.commenting.BookReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookNotificationSession``
        :rtype: ``osid.commenting.BookNotificationSession``
        :raise: ``NullArgument`` -- ``book_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_notification()`` is ``true``.*

        """
        return  # osid.commenting.BookNotificationSession

    @abc.abstractmethod
    def get_book_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookHierarchySession``
        :rtype: ``osid.commenting.BookHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy()`` is ``true``.*

        """
        return  # osid.commenting.BookHierarchySession

    @abc.abstractmethod
    def get_book_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookHierarchyDesignSession``
        :rtype: ``osid.commenting.BookHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy_design()`` is ``true``.*

        """
        return  # osid.commenting.BookHierarchyDesignSession

    @abc.abstractmethod
    def get_commenting_batch_proxy_manager(self):
        """Gets a ``CommentingBatchProxyManager``.

        :return: a ``CommentingBatchProxyManager``
        :rtype: ``osid.commenting.batch.CommentingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        return  # osid.commenting.batch.CommentingBatchProxyManager

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)
