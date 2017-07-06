"""JSON implementations of authentication searches."""

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
from dlkit.abstract_osid.authentication import searches as abc_authentication_searches
from dlkit.abstract_osid.osid import errors


class AgentSearch(abc_authentication_searches.AgentSearch, osid_searches.OsidSearch):
    """``AgentSearch`` defines the interface for specifying agent search options.

    This example gets a limited set of squid-like agents. AgentSearch as
    = session.getAgentSearch(); as.limitResultSet(25, 50); AgentQuery
    queries[1]; queries[0] = session.getAgentQuery(); String kword =
    "squid"; queries[0].matchKeywords(kword, true); AgentSearchResults
    results = session.getAgentsBySearch(queries, as); AgentList list =
    results.getAgents();

    """
    def __init__(self, runtime):
        self._namespace = 'authentication.Agent'
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
    def search_among_agents(self, agent_ids):
        """Execute this search among the given list of agents.

        arg:    agent_ids (osid.id.IdList): list of agents
        raise:  NullArgument - ``agent_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = agent_ids

    @utilities.arguments_not_none
    def order_agent_results(self, agent_search_order):
        """Specify an ordering to the search results.

        arg:    agent_search_order
                (osid.authentication.AgentSearchOrder): agent search
                order
        raise:  NullArgument - ``agent_search_order`` is ``null``
        raise:  Unsupported - ``agent_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_agent_search_record(self, agent_search_record_type):
        """Gets the record corresponding to the given agent search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    agent_search_record_type (osid.type.Type): an agent
                search record type
        return: (osid.authentication.records.AgentSearchRecord) - the
                agent search record
        raise:  NullArgument - ``agent_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(agent_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class AgentSearchResults(abc_authentication_searches.AgentSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search.

    AgentSearch as = session.getAgentSearch(); as.limitResultSet(25,
    50); AgentQuery queries[1]; queries[0] = session.getAgentQuery();
    String kwords[1]; kwords[0] = "squid";
    queries[0].matchKeywords(kwords); AgentSearchResults results =
    session.getAgentsBySearch(queries, as); AgentList list =
    results.getAgents();

    """
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'authentication.Agent'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_agents(self):
        """Gets the agent list resulting from the search.

        return: (osid.authentication.AgentList) - the agent list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.AgentList(self._results, runtime=self._runtime)

    agents = property(fget=get_agents)

    def get_agent_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.authentication.AgentQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.AgentQueryInspector(self._query_terms, runtime=self._runtime)

    agent_query_inspector = property(fget=get_agent_query_inspector)

    @utilities.arguments_not_none
    def get_agent_search_results_record(self, agent_search_record_type):
        """Gets the record corresponding to the given agent search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    agent_search_record_type (osid.type.Type): an agent
                search record type
        return: (osid.authentication.records.AgentSearchResultsRecord) -
                the agent search results record
        raise:  NullArgument - ``agent_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(agent_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
