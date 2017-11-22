"""JSON implementations of authentication queries."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..osid import queries as osid_queries
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.authentication import queries as abc_authentication_queries
from dlkit.abstract_osid.osid import errors


class AgentQuery(abc_authentication_queries.AgentQuery, osid_queries.OsidObjectQuery):
    """This is the query for searching agents.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    The following example returns agents whose display name begins with
    "Tom" and whose "login name" is "tom" or "tjcoppet" in an agent
    record specified by ``companyAgentType``.
      Agent Query query = session.getAgentQuery();

      query.matchDisplayName("Tom*", wildcardStringMatchType, true);

      companyAgentQuery = query.getAgentQueryRecord(companyAgentType);
      companyAgentQuery.matchLoginName("tom");
      companyAgentQuery = query.getAgentQueryRecord(companyAgentType);
      companyAgentQuery.matchLoginName("tjcoppet");

      AgentList agentList = session.getAgentsByQuery(query);

    """
    _namespace = 'authentication.Agent'

    def __init__(self, **kwargs):
        osid_queries.OsidObjectQuery.__init__(self, **kwargs)
        self._catalog_name = 'Agency'

    @utilities.arguments_not_none
    def match_resource_id(self, agency_id, match):
        """Sets the resource ``Id`` for this query.

        arg:    agency_id (osid.id.Id): a resource ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``agency_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.match_avatar_id
        self._add_match('resourceId', str(agency_id), match)

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_avatar_id
        self._clear_terms('resourceId')

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    resource_query = property(fget=get_resource_query)

    @utilities.arguments_not_none
    def match_any_resource(self, match):
        """Matches agents with any resource.

        arg:    match (boolean): ``true`` if to match agents with a
                resource, ``false`` to match agents with no resource
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_resource_terms(self):
        """Clears the resource terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    resource_terms = property(fdel=clear_resource_terms)

    @utilities.arguments_not_none
    def match_agency_id(self, agency_id, match):
        """Sets the agency ``Id`` for this query.

        arg:    agency_id (osid.id.Id): an agency ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``agency_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.match_bin_id
        self._add_match('assignedAgencyIds', str(agency_id), match)

    def clear_agency_id_terms(self):
        """Clears the agency ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_bin_id_terms
        self._clear_terms('assignedAgencyIds')

    agency_id_terms = property(fdel=clear_agency_id_terms)

    def supports_agency_query(self):
        """Tests if an ``AgencyQuery`` is available.

        return: (boolean) - ``true`` if an agency query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_agency_query(self):
        """Gets the query for an agency.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.authentication.AgencyQuery) - the agency query
        raise:  Unimplemented - ``supports_agency_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agency_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    agency_query = property(fget=get_agency_query)

    def clear_agency_terms(self):
        """Clears the agency terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_group_terms
        self._clear_terms('agency')

    agency_terms = property(fdel=clear_agency_terms)

    @utilities.arguments_not_none
    def get_agent_query_record(self, agent_record_type):
        """Gets the agent query record corresponding to the given ``Agent`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    agent_record_type (osid.type.Type): an agent record type
        return: (osid.authentication.records.AgentQueryRecord) - the
                agent query record
        raise:  NullArgument - ``agent_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(agent_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
