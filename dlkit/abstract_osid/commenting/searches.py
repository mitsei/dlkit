"""Implementations of commenting abstract base class searches."""
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


class CommentSearch:
    """The search interface for governing comment searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_comments(self, comment_ids):
        """Execute this search among the given list of comments.

        :param comment_ids: list of comments
        :type comment_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``comment_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_comment_results(self, comment_search_order):
        """Specify an ordering to the search results.

        :param comment_search_order: comment search order
        :type comment_search_order: ``osid.commenting.CommentSearchOrder``
        :raise: ``NullArgument`` -- ``comment_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``comment_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_comment_search_record(self, comment_search_record_type):
        """Gets the comment search record corresponding to the given comment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param comment_search_record_type: a comment search record type
        :type comment_search_record_type: ``osid.type.Type``
        :return: the comment search record
        :rtype: ``osid.commenting.records.CommentSearchRecord``
        :raise: ``NullArgument`` -- ``comment_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.CommentSearchRecord


class CommentSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_comments(self):
        """Gets the comment list resulting from a search.

        :return: the comment list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    comments = property(fget=get_comments)

    @abc.abstractmethod
    def get_comment_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        :return: the query inspector
        :rtype: ``osid.commenting.CommentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentQueryInspector

    comment_query_inspector = property(fget=get_comment_query_inspector)

    @abc.abstractmethod
    def get_comment_search_results_record(self, comment_search_record_type):
        """Gets the comment search results record corresponding to the given comment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param comment_search_record_type: a comment search record type
        :type comment_search_record_type: ``osid.type.Type``
        :return: the comment search results record
        :rtype: ``osid.commenting.records.CommentSearchResultsRecord``
        :raise: ``NullArgument`` -- ``comment_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.CommentSearchResultsRecord


class BookSearch:
    """The search interface for governing book searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_books(self, book_ids):
        """Execute this search among the given list of books.

        :param book_ids: list of books
        :type book_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_book_results(self, book_search_order):
        """Specify an ordering to the search results.

        :param book_search_order: book search order
        :type book_search_order: ``osid.commenting.BookSearchOrder``
        :raise: ``NullArgument`` -- ``book_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``book_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_book_search_record(self, book_search_record_type):
        """Gets the book search record corresponding to the given book search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param book_search_record_type: a book search record type
        :type book_search_record_type: ``osid.type.Type``
        :return: the book search record
        :rtype: ``osid.commenting.records.BookSearchRecord``
        :raise: ``NullArgument`` -- ``book_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.BookSearchRecord


class BookSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_books(self):
        """Gets the book list resulting from a search.

        :return: the book list
        :rtype: ``osid.commenting.BookList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    books = property(fget=get_books)

    @abc.abstractmethod
    def get_book_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        :return: the query inspector
        :rtype: ``osid.commenting.BookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookQueryInspector

    book_query_inspector = property(fget=get_book_query_inspector)

    @abc.abstractmethod
    def get_book_search_results_record(self, book_search_record_type):
        """Gets the book search results record corresponding to the given book search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param book_search_record_type: a book search record type
        :type book_search_record_type: ``osid.type.Type``
        :return: the book search results record
        :rtype: ``osid.commenting.records.BookSearchResultsRecord``
        :raise: ``NullArgument`` -- ``BookSearchRecordType`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.BookSearchResultsRecord
