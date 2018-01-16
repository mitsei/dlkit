"""JSON implementations of osid searches."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from collections import OrderedDict


from .. import utilities
from ..osid import rules as osid_rules
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid import searches as abc_osid_searches
from dlkit.primordium.id.primitives import Id


class OsidSearch(abc_osid_searches.OsidSearch, osid_rules.OsidCondition):
    """``OsidSearch`` specifies search options used to perform OSID searches.

    An ``OsidSearch`` is available from an ``OsidSession`` and defines
    methods to govern the overall search of terms supplied in one or
    more ``OsidQuery`` interfaces.

    This interface is available from a search session.Example using the
    search interface to retrieve the first 25 results:
      OsidSearch os = session.getObjectSearch();
      os.limitResultSet(1, 25);

      OsidQuery query;
      query = session.getObjectQuery();
      query.addDescriptionMatch("*food*", wildcardStringMatchType, true);

      ObjectSearchResults results = session.getObjectsBySearch(query, os);
      ObjectList list = results.getObjectList();

    """
    def __init__(self, runtime):
        self._records = OrderedDict()
        # _load_records is in OsidExtensibleQuery:
        # _all_supported_record_type_ids comes from inheriting query object
        # THIS SHOULD BE RE-DONE:
        self._load_records(self._all_supported_record_type_ids)
        self._runtime = runtime
        self._query_terms = {}
        self._keyword_terms = {}
        self._keyword_fields = ['displayName.text', 'description.text']
        try:
            # Try to get additional keyword fields from the runtime, if available:
            config = runtime.get_configuration()
            parameter_id = Id('parameter:keywordFields@json')
            additional_keyword_fields = config.get_value_by_parameter(parameter_id).get_object_value()
            self._keyword_fields += additional_keyword_fields[self._namespace]
        except (AttributeError, KeyError, errors.NotFound):
            pass
        self._limit_result_set_start = None
        self._limit_result_set_end = None

    @utilities.arguments_not_none
    def limit_result_set(self, start, end):
        """By default, searches return all matching results.

        This method restricts the number of results by setting the start
        and end of the result set, starting from 1. The starting and
        ending results can be used for paging results when a certain
        ordering is requested. The ending position must be greater than
        the starting position.

        arg:    start (cardinal): the start of the result set
        arg:    end (cardinal): the end of the result set
        raise:  InvalidArgument - ``end`` is less than or equal to
                ``start``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(start, int) or not isinstance(end, int):
            raise errors.InvalidArgument('start and end arguments must be integers.')
        if end <= start:
            raise errors.InvalidArgument('End must be greater than start.')

        # because Python is 0 indexed
        # Spec says that passing in (1, 25) should include 25 entries (1 - 25)
        # Python indices 0 - 24
        # Python [#:##] stops before the last index, but does not include it
        self._limit_result_set_start = start - 1
        self._limit_result_set_end = end

    @property
    def start(self):
        return self._limit_result_set_start

    @property
    def end(self):
        return self._limit_result_set_end


class OsidSearchResults(abc_osid_searches.OsidSearchResults, osid_rules.OsidResult):
    """This interface provides a means to capture results of a search.

    An example of searching withina result set: OsidSearch os =
    session.getObjectSearch(); OsidQuery query; query =
    session.getObjectQuery(); query.matchDescription("*food*",
    wildcardStringMatchType, true); ObjectSearchResults results =
    session.getObjectBySearch(query, os); // get information about
    search ObjectList objects = results.getObjects(); int size =
    results.getResultSize(); SearchPerformanceRecord record =
    (SearchPerformanceRecord)
    results.getObjectSearchResultsRecord(performanceRecodType); Duration
    duration = record.getTimeForSearch();

    """

    def get_result_size(self):
        """Returns the size of a result set from a search query.

        This number serves as an estimate to provide feedback for
        refining search queries and may not be the number of elements
        available through an ``OsidList``.

        return: (cardinal) - the result size
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._results.count(True)

    result_size = property(fget=get_result_size)
