"""JSON implementations of logging searches."""

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
from dlkit.abstract_osid.logging_ import searches as abc_logging_searches
from dlkit.abstract_osid.osid import errors


class LogEntrySearch(abc_logging_searches.LogEntrySearch, osid_searches.OsidSearch):
    """The search interface for governing log entry searches."""
    def __init__(self, runtime):
        self._namespace = 'logging.LogEntry'
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
    def search_among_log_entries(self, log_entry_ids):
        """Execute this search among the given list of log entries.

        arg:    log_entry_ids (osid.id.IdList): list of log entries
        raise:  NullArgument - ``log_entry_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = log_entry_ids

    @utilities.arguments_not_none
    def order_log_entry_results(self, log_entry_search_order):
        """Specify an ordering to the search results.

        arg:    log_entry_search_order
                (osid.logging.LogEntrySearchOrder): log entry search
                order
        raise:  NullArgument - ``log_entry_search_order`` is ``null``
        raise:  Unsupported - ``log_entry_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_entry_search_record(self, log_entry_search_record_type):
        """Gets the log search record corresponding to the given log entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    log_entry_search_record_type (osid.type.Type): a log
                entry search record type
        return: (osid.logging.records.LogEntrySearchRecord) - the log
                entry search record
        raise:  NullArgument - ``log_entry_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(log_entry_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogEntrySearchResults(abc_logging_searches.LogEntrySearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'logging.LogEntry'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_log_entries(self):
        """Gets the log entry list resulting from a search.

        return: (osid.logging.LogEntryList) - the log entry list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.LogEntryList(self._results, runtime=self._runtime)

    log_entries = property(fget=get_log_entries)

    def get_log_entry_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.logging.LogEntryQueryInspector) - the log entry
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.LogEntryQueryInspector(self._query_terms, runtime=self._runtime)

    log_entry_query_inspector = property(fget=get_log_entry_query_inspector)

    @utilities.arguments_not_none
    def get_log_entry_search_results_record(self, log_entry_search_record_type):
        """Gets the log entry search results record corresponding to the given log entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    log_entry_search_record_type (osid.type.Type): a log
                entry search record type
        return: (osid.logging.records.LogEntrySearchResultsRecord) - the
                log entry search results record
        raise:  NullArgument - ``log_entry_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(log_entry_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogSearch(abc_logging_searches.LogSearch, osid_searches.OsidSearch):
    """The search interface for governing log searches."""
    def __init__(self, runtime):
        self._namespace = 'logging.Log'
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
    def search_among_logs(self, log_ids):
        """Execute this search among the given list of logs.

        arg:    log_ids (osid.id.IdList): list of logs
        raise:  NullArgument - ``log_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = log_ids

    @utilities.arguments_not_none
    def order_log_results(self, log_search_order):
        """Specify an ordering to the search results.

        arg:    log_search_order (osid.logging.LogSearchOrder): log
                search order
        raise:  NullArgument - ``log_search_order`` is ``null``
        raise:  Unsupported - ``log_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_search_record(self, log_search_record_type):
        """Gets the log search record corresponding to the given log search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    log_search_record_type (osid.type.Type): a log search
                record type
        return: (osid.logging.records.LogSearchRecord) - the log search
                record
        raise:  NullArgument - ``log_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(log_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogSearchResults(abc_logging_searches.LogSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'logging.Log'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_logs(self):
        """Gets the log list resulting from a search.

        return: (osid.logging.LogList) - the log list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.LogList(self._results, runtime=self._runtime)

    logs = property(fget=get_logs)

    def get_log_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.logging.LogQueryInspector) - the log query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.LogQueryInspector(self._query_terms, runtime=self._runtime)

    log_query_inspector = property(fget=get_log_query_inspector)

    @utilities.arguments_not_none
    def get_log_search_results_record(self, log_search_record_type):
        """Gets the log search results record corresponding to the given log search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    log_search_record_type (osid.type.Type): a log search
                record type
        return: (osid.logging.records.LogSearchResultsRecord) - the log
                search results record
        raise:  NullArgument - ``log_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(log_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
