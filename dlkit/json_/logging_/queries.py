"""JSON implementations of logging queries."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..id.objects import IdList
from ..osid import queries as osid_queries
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.logging_ import queries as abc_logging_queries
from dlkit.abstract_osid.osid import errors


class LogEntryQuery(abc_logging_queries.LogEntryQuery, osid_queries.OsidObjectQuery):
    """This is the query for searching log entries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def __init__(self, runtime):
        self._namespace = 'logging.LogEntry'
        self._runtime = runtime
        record_type_data_sets = get_registry('LOG_ENTRY_RECORD_TYPES', runtime)
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_queries.OsidObjectQuery.__init__(self, runtime)

    @utilities.arguments_not_none
    def match_priority(self, priority_type, match):
        """Matches a priority ``Type`` for the log entry.

        arg:    priority_type (osid.type.Type): ``Type`` to match
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``priority_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def match_any_priority(self, match):
        """Matches log entries with any priority.

        arg:    match (boolean): ``true`` to match log entries with any
                priority, ``false`` to match log entries with no
                priority
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_priority_terms(self):
        """Clears the priority terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_group_terms
        self._clear_terms('priority')

    priority_terms = property(fdel=clear_priority_terms)

    @utilities.arguments_not_none
    def match_minimum_priority(self, priority_type, match):
        """Matches a log entries including and above the given priority type.

        arg:    priority_type (osid.type.Type): ``Type`` to match
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``priority_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_minimum_priority_terms(self):
        """Clears the minimum priority terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    minimum_priority_terms = property(fdel=clear_minimum_priority_terms)

    @utilities.arguments_not_none
    def match_timestamp(self, start_time, end_time, match):
        """Matches the time of this log entry.

        arg:    start_time (osid.calendaring.DateTime): start time
        arg:    end_time (osid.calendaring.DateTime): end time
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``start_time`` is greater than
                ``end_time``
        raise:  NullArgument - ``start_time`` or ``end_time`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._match_minimum_date_time('timestamp', start_time, match)
        self._match_maximum_date_time('timestamp', end_time, match)

    def clear_timestamp_terms(self):
        """Clears the timestamp terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_group_terms
        self._clear_terms('timestamp')

    timestamp_terms = property(fdel=clear_timestamp_terms)

    @utilities.arguments_not_none
    def match_resource_id(self, resource_id, match):
        """Matches a resource in this log entry.

        arg:    resource_id (osid.id.Id): ``Id`` to match
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.match_avatar_id
        self._add_match('resourceId', str(resource_id), match)

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_avatar_id
        self._clear_terms('resourceId')

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available for querying agents.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_resource_query(self):
        """Gets the query for a resource.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    resource_query = property(fget=get_resource_query)

    def clear_resource_terms(self):
        """Clears the resource terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    resource_terms = property(fdel=clear_resource_terms)

    @utilities.arguments_not_none
    def match_agent_id(self, agent_id, match):
        """Matches an agent in this log entry.

        arg:    agent_id (osid.id.Id): ``Id`` to match
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``agent_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._add_match("agentId", str(agent_id), match)

    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_avatar_id
        self._clear_terms('agentId')

    agent_id_terms = property(fdel=clear_agent_id_terms)

    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available for querying agents.

        return: (boolean) - ``true`` if an agent query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_agent_query(self):
        """Gets the query for an agent.

        return: (osid.authentication.AgentQuery) - the agent query
        raise:  Unimplemented - ``supports_agent_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    agent_query = property(fget=get_agent_query)

    def clear_agent_terms(self):
        """Clears the agent terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_group_terms
        self._clear_terms('agent')

    agent_terms = property(fdel=clear_agent_terms)

    @utilities.arguments_not_none
    def match_log_id(self, log_id, match):
        """Matches a log.

        arg:    log_id (osid.id.Id): ``Id`` to match
        arg:    match (boolean): ``true`` if for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``log_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.match_bin_id
        self._add_match('assignedLogIds', str(log_id), match)

    def clear_log_id_terms(self):
        """Clears the log ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_bin_id_terms
        self._clear_terms('assignedLogIds')

    log_id_terms = property(fdel=clear_log_id_terms)

    def supports_log_query(self):
        """Tests if a ``LogQuery`` is available for querying logs.

        return: (boolean) - ``true`` if a log query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_log_query(self):
        """Gets the query for a log.

        return: (osid.logging.LogQuery) - the log query
        raise:  Unimplemented - ``supports_log_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    log_query = property(fget=get_log_query)

    def clear_log_terms(self):
        """Clears the log terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceQuery.clear_group_terms
        self._clear_terms('log')

    log_terms = property(fdel=clear_log_terms)

    @utilities.arguments_not_none
    def get_log_entry_query_record(self, log_entry_record_type):
        """Gets the log entry query corresponding to the given ``LogEntry`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        arg:    log_entry_record_type (osid.type.Type): a log entry
                record type
        return: (osid.logging.records.LogEntryQueryRecord) - the log
                entry query record
        raise:  NullArgument - ``log_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(log_eutry_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogQuery(abc_logging_queries.LogQuery, osid_queries.OsidCatalogQuery):
    """This is the query for searching for logs.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def __init__(self, runtime):
        self._runtime = runtime
        record_type_data_sets = get_registry('LOG_RECORD_TYPES', runtime)
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_queries.OsidCatalogQuery.__init__(self, runtime)

    def _get_descendant_catalog_ids(self, catalog_id):
        hm = self._get_provider_manager('HIERARCHY')
        hts = hm.get_hierarchy_traversal_session_for_hierarchy(
            Id(authority='LOGGING',
               namespace='CATALOG',
               identifier='LOG')
        )  # What about the Proxy?
        descendants = []
        if hts.has_children(catalog_id):
            for child_id in hts.get_children(catalog_id):
                descendants += list(self._get_descendant_catalog_ids(child_id))
                descendants.append(child_id)
        return IdList(descendants)

    @utilities.arguments_not_none
    def match_log_entry_id(self, log_entry_id, match):
        """Sets a log entry ``Id``.

        arg:    log_entry_id (osid.id.Id): a log entry ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``log_entry_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_log_entry_id_terms(self):
        """Clesrs the log entry ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('logEntryId')

    log_entry_id_terms = property(fdel=clear_log_entry_id_terms)

    def supports_log_entry_query(self):
        """Tests if a log entry query is available.

        return: (boolean) - ``true`` if a log entry query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_log_entry_query(self):
        """Gets the query for a log entry.

        return: (osid.logging.LogEntryQuery) - the log entry query
        raise:  Unimplemented - ``supports_log_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    log_entry_query = property(fget=get_log_entry_query)

    @utilities.arguments_not_none
    def match_any_log_entry(self, match):
        """Matches logs with any log entry.

        arg:    match (boolean): ``true`` to match logs with any entry,
                ``false`` to match logs with no log entries
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_log_entry_terms(self):
        """Clesrs the log entry terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('logEntry')

    log_entry_terms = property(fdel=clear_log_entry_terms)

    @utilities.arguments_not_none
    def match_ancestor_log_id(self, log_id, match):
        """Sets the log ``Id`` for this query to match logs that have the specified log as an ancestor.

        arg:    log_id (osid.id.Id): a log ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``log_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_ancestor_log_id_terms(self):
        """Clesrs the ancestor log ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('ancestorLogId')

    ancestor_log_id_terms = property(fdel=clear_ancestor_log_id_terms)

    def supports_ancestor_log_query(self):
        """Tests if a ``LogQuery`` is available.

        return: (boolean) - ``true`` if a log query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_ancestor_log_query(self):
        """Gets the query for a log.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.logging.LogQuery) - the log query
        raise:  Unimplemented - ``supports_ancestor_log_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_log_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    ancestor_log_query = property(fget=get_ancestor_log_query)

    @utilities.arguments_not_none
    def match_any_ancestor_log(self, match):
        """Matches logs with any ancestor.

        arg:    match (boolean): ``true`` to match logs with any
                ancestor, ``false`` to match root logs
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_ancestor_log_terms(self):
        """Clesrs the ancestor log terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('ancestorLog')

    ancestor_log_terms = property(fdel=clear_ancestor_log_terms)

    @utilities.arguments_not_none
    def match_descendant_log_id(self, log_id, match):
        """Sets the log ``Id`` for this query to match logs that have the specified log as a descendant.

        arg:    log_id (osid.id.Id): a log ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``log_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_descendant_log_id_terms(self):
        """Clesrs the descendant log ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('descendantLogId')

    descendant_log_id_terms = property(fdel=clear_descendant_log_id_terms)

    def supports_descendant_log_query(self):
        """Tests if a ``LogQuery`` is available.

        return: (boolean) - ``true`` if a log query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_descendant_log_query(self):
        """Gets the query for a log.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.logging.LogQuery) - the log query
        raise:  Unimplemented - ``supports_descendant_log_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_log_query()`` is ``true``.*

        """
        raise errors.Unimplemented()

    descendant_log_query = property(fget=get_descendant_log_query)

    @utilities.arguments_not_none
    def match_any_descendant_log(self, match):
        """Matches logs with any descendant.

        arg:    match (boolean): ``true`` to match logs with any
                descendant, ``false`` to match leaf logs
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_descendant_log_terms(self):
        """Clesrs the descendant log terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        self._clear_terms('descendantLog')

    descendant_log_terms = property(fdel=clear_descendant_log_terms)

    @utilities.arguments_not_none
    def get_log_query_record(self, log_record_type):
        """Gets the log query record corresponding to the given ``Log`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        arg:    log_record_type (osid.type.Type): a log record type
        return: (osid.logging.records.LogQueryRecord) - the log query
                record
        raise:  NullArgument - ``log_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(log_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
