"""JSON implementations of commenting searches."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import objects
from . import queries
from .. import utilities
from ..osid import searches as osid_searches
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.commenting import searches as abc_commenting_searches
from dlkit.abstract_osid.osid import errors


class CommentSearch(abc_commenting_searches.CommentSearch, osid_searches.OsidSearch):
    """The search interface for governing comment searches."""
    def __init__(self, runtime):
        self._namespace = 'commenting.Comment'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_comments(self, comment_ids):
        """Execute this search among the given list of comments.

        arg:    comment_ids (osid.id.IdList): list of comments
        raise:  NullArgument - ``comment_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = comment_ids

    @utilities.arguments_not_none
    def order_comment_results(self, comment_search_order):
        """Specify an ordering to the search results.

        arg:    comment_search_order
                (osid.commenting.CommentSearchOrder): comment search
                order
        raise:  NullArgument - ``comment_search_order`` is ``null``
        raise:  Unsupported - ``comment_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_comment_search_record(self, comment_search_record_type):
        """Gets the comment search record corresponding to the given comment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    comment_search_record_type (osid.type.Type): a comment
                search record type
        return: (osid.commenting.records.CommentSearchRecord) - the
                comment search record
        raise:  NullArgument - ``comment_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(comment_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class CommentSearchResults(abc_commenting_searches.CommentSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'commenting.Comment'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_comments(self):
        """Gets the comment list resulting from a search.

        return: (osid.commenting.CommentList) - the comment list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.CommentList(self._results, runtime=self._runtime)

    comments = property(fget=get_comments)

    def get_comment_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        return: (osid.commenting.CommentQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.CommentQueryInspector(self._query_terms, runtime=self._runtime)

    comment_query_inspector = property(fget=get_comment_query_inspector)

    @utilities.arguments_not_none
    def get_comment_search_results_record(self, comment_search_record_type):
        """Gets the comment search results record corresponding to the given comment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    comment_search_record_type (osid.type.Type): a comment
                search record type
        return: (osid.commenting.records.CommentSearchResultsRecord) -
                the comment search results record
        raise:  NullArgument - ``comment_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(comment_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BookSearch(abc_commenting_searches.BookSearch, osid_searches.OsidSearch):
    """The search interface for governing book searches."""
    def __init__(self, runtime):
        self._namespace = 'commenting.Book'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_books(self, book_ids):
        """Execute this search among the given list of books.

        arg:    book_ids (osid.id.IdList): list of books
        raise:  NullArgument - ``book_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = book_ids

    @utilities.arguments_not_none
    def order_book_results(self, book_search_order):
        """Specify an ordering to the search results.

        arg:    book_search_order (osid.commenting.BookSearchOrder):
                book search order
        raise:  NullArgument - ``book_search_order`` is ``null``
        raise:  Unsupported - ``book_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_book_search_record(self, book_search_record_type):
        """Gets the book search record corresponding to the given book search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    book_search_record_type (osid.type.Type): a book search
                record type
        return: (osid.commenting.records.BookSearchRecord) - the book
                search record
        raise:  NullArgument - ``book_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(book_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BookSearchResults(abc_commenting_searches.BookSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'commenting.Book'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_books(self):
        """Gets the book list resulting from a search.

        return: (osid.commenting.BookList) - the book list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.BookList(self._results, runtime=self._runtime)

    books = property(fget=get_books)

    def get_book_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        return: (osid.commenting.BookQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.BookQueryInspector(self._query_terms, runtime=self._runtime)

    book_query_inspector = property(fget=get_book_query_inspector)

    @utilities.arguments_not_none
    def get_book_search_results_record(self, book_search_record_type):
        """Gets the book search results record corresponding to the given book search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    book_search_record_type (osid.type.Type): a book search
                record type
        return: (osid.commenting.records.BookSearchResultsRecord) - the
                book search results record
        raise:  NullArgument - ``BookSearchRecordType`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(book_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
