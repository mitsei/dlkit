"""Implementations of authentication abstract base class queries."""
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


class AgentQuery:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_resource_id(self, agency_id, match):
        """Sets the resource ``Id`` for this query.

        :param agency_id: a resource ``Id``
        :type agency_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    @abc.abstractmethod
    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    @abc.abstractmethod
    def match_any_resource(self, match):
        """Matches agents with any resource.

        :param match: ``true`` if to match agents with a resource, ``false`` to match agents with no resource
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_terms = property(fdel=clear_resource_terms)

    @abc.abstractmethod
    def match_agency_id(self, agency_id, match):
        """Sets the agency ``Id`` for this query.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_agency_id_terms(self):
        """Clears the agency ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agency_id_terms = property(fdel=clear_agency_id_terms)

    @abc.abstractmethod
    def supports_agency_query(self):
        """Tests if an ``AgencyQuery`` is available.

        :return: ``true`` if an agency query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agency_query(self):
        """Gets the query for an agency.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agency query
        :rtype: ``osid.authentication.AgencyQuery``
        :raise: ``Unimplemented`` -- ``supports_agency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agency_query()`` is ``true``.*

        """
        return  # osid.authentication.AgencyQuery

    agency_query = property(fget=get_agency_query)

    @abc.abstractmethod
    def clear_agency_terms(self):
        """Clears the agency terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agency_terms = property(fdel=clear_agency_terms)

    @abc.abstractmethod
    def get_agent_query_record(self, agent_record_type):
        """Gets the agent query record corresponding to the given ``Agent`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent query record
        :rtype: ``osid.authentication.records.AgentQueryRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgentQueryRecord


class AgencyQuery:
    """This is the query for searching agencies.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_agent_id(self, agent_id, match):
        """Sets the agent ``Id`` for this query.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_id_terms = property(fdel=clear_agent_id_terms)

    @abc.abstractmethod
    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    @abc.abstractmethod
    def match_any_agent(self, match):
        """Matches agencies with any agent.

        :param match: ``true`` to match agencies with any agent. ``false`` to match agencies with no agents
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_agent_terms(self):
        """Clears the agent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_terms = property(fdel=clear_agent_terms)

    @abc.abstractmethod
    def match_ancestor_agency_id(self, agency_id, match):
        """Sets the agency ``Id`` for this query to match agencies that have the specified agency as an ancestor.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_agency_id_terms(self):
        """Clears the ancestor agency ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_agency_id_terms = property(fdel=clear_ancestor_agency_id_terms)

    @abc.abstractmethod
    def supports_ancestor_agency_query(self):
        """Tests if an ``AgencyQuery`` is available.

        :return: ``true`` if an agency query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_agency_query(self):
        """Gets the query for an agency.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agency query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_agency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_agency_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    ancestor_agency_query = property(fget=get_ancestor_agency_query)

    @abc.abstractmethod
    def match_any_ancestor_agency(self, match):
        """Matches agencies with any ancestor.

        :param match: ``true`` to match agencies with any ancestor, ``false`` to match root agencies
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_agency_terms(self):
        """Clears the ancestor agency terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_agency_terms = property(fdel=clear_ancestor_agency_terms)

    @abc.abstractmethod
    def match_descendant_agency_id(self, agency_id, match):
        """Sets the agency ``Id`` for this query to match agencies that have the specified agency as an descendant.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_agency_id_terms(self):
        """Clears the descendant agency ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_agency_id_terms = property(fdel=clear_descendant_agency_id_terms)

    @abc.abstractmethod
    def supports_descendant_agency_query(self):
        """Tests if an ``AgencyQuery`` is available.

        :return: ``true`` if an agency query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_agency_query(self):
        """Gets the query for an agency.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agency query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_agency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_agency_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    descendant_agency_query = property(fget=get_descendant_agency_query)

    @abc.abstractmethod
    def match_any_descendant_agency(self, match):
        """Matches agencies with any descendant.

        :param match: ``true`` to match agencies with any descendant, ``false`` to match leaf agencies
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_agency_terms(self):
        """Clears the descendant agency terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_agency_terms = property(fdel=clear_descendant_agency_terms)

    @abc.abstractmethod
    def get_agency_query_record(self, agency_record_type):
        """Gets the agency query record corresponding to the given ``Agency`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency query record
        :rtype: ``osid.authentication.records.AgencyQueryRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgencyQueryRecord
