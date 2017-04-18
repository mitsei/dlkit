"""Implementations of logging abstract base class queries."""
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


class LogEntryQuery:
    """This is the query for searching log entries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_priority(self, priority_type, match):
        """Matches a priority ``Type`` for the log entry.

        :param priority_type: ``Type`` to match
        :type priority_type: ``osid.type.Type``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_priority(self, match):
        """Matches log entries with any priority.

        :param match: ``true`` to match log entries with any priority, ``false`` to match log entries with no priority
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_priority_terms(self):
        """Clears the priority terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    priority_terms = property(fdel=clear_priority_terms)

    @abc.abstractmethod
    def match_minimum_priority(self, priority_type, match):
        """Matches a log entries including and above the given priority type.

        :param priority_type: ``Type`` to match
        :type priority_type: ``osid.type.Type``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_priority_terms(self):
        """Clears the minimum priority terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_priority_terms = property(fdel=clear_minimum_priority_terms)

    @abc.abstractmethod
    def match_timestamp(self, start_time, end_time, match):
        """Matches the time of this log entry.

        :param start_time: start time
        :type start_time: ``osid.calendaring.DateTime``
        :param end_time: end time
        :type end_time: ``osid.calendaring.DateTime``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start_time`` is greater than ``end_time``
        :raise: ``NullArgument`` -- ``start_time`` or ``end_time`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_timestamp_terms(self):
        """Clears the timestamp terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    timestamp_terms = property(fdel=clear_timestamp_terms)

    @abc.abstractmethod
    def match_resource_id(self, resource_id, match):
        """Matches a resource in this log entry.

        :param resource_id: ``Id`` to match
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

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
        """Tests if a ``ResourceQuery`` is available for querying agents.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_query(self):
        """Gets the query for a resource.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    @abc.abstractmethod
    def clear_resource_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_terms = property(fdel=clear_resource_terms)

    @abc.abstractmethod
    def match_agent_id(self, agent_id, match):
        """Matches an agent in this log entry.

        :param agent_id: ``Id`` to match
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
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
        """Tests if an ``AgentQuery`` is available for querying agents.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_query(self):
        """Gets the query for an agent.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    @abc.abstractmethod
    def clear_agent_terms(self):
        """Clears the agent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_terms = property(fdel=clear_agent_terms)

    @abc.abstractmethod
    def match_log_id(self, log_id, match):
        """Matches a log.

        :param log_id: ``Id`` to match
        :type log_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_log_id_terms(self):
        """Clears the log ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    log_id_terms = property(fdel=clear_log_id_terms)

    @abc.abstractmethod
    def supports_log_query(self):
        """Tests if a ``LogQuery`` is available for querying logs.

        :return: ``true`` if a log query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_query(self):
        """Gets the query for a log.

        :return: the log query
        :rtype: ``osid.logging.LogQuery``
        :raise: ``Unimplemented`` -- ``supports_log_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_query()`` is ``true``.*

        """
        return  # osid.logging.LogQuery

    log_query = property(fget=get_log_query)

    @abc.abstractmethod
    def clear_log_terms(self):
        """Clears the log terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    log_terms = property(fdel=clear_log_terms)

    @abc.abstractmethod
    def get_log_entry_query_record(self, log_entry_record_type):
        """Gets the log entry query corresponding to the given ``LogEntry`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param log_entry_record_type: a log entry record type
        :type log_entry_record_type: ``osid.type.Type``
        :return: the log entry query record
        :rtype: ``osid.logging.records.LogEntryQueryRecord``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_eutry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.records.LogEntryQueryRecord


class LogQuery:
    """This is the query for searching for logs.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_log_entry_id(self, log_entry_id, match):
        """Sets a log entry ``Id``.

        :param log_entry_id: a log entry ``Id``
        :type log_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_log_entry_id_terms(self):
        """Clesrs the log entry ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    log_entry_id_terms = property(fdel=clear_log_entry_id_terms)

    @abc.abstractmethod
    def supports_log_entry_query(self):
        """Tests if a log entry query is available.

        :return: ``true`` if a log entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_entry_query(self):
        """Gets the query for a log entry.

        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` is ``true``.*

        """
        return  # osid.logging.LogEntryQuery

    log_entry_query = property(fget=get_log_entry_query)

    @abc.abstractmethod
    def match_any_log_entry(self, match):
        """Matches logs with any log entry.

        :param match: ``true`` to match logs with any entry, ``false`` to match logs with no log entries
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_log_entry_terms(self):
        """Clesrs the log entry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    log_entry_terms = property(fdel=clear_log_entry_terms)

    @abc.abstractmethod
    def match_ancestor_log_id(self, log_id, match):
        """Sets the log ``Id`` for this query to match logs that have the specified log as an ancestor.

        :param log_id: a log ``Id``
        :type log_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_log_id_terms(self):
        """Clesrs the ancestor log ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_log_id_terms = property(fdel=clear_ancestor_log_id_terms)

    @abc.abstractmethod
    def supports_ancestor_log_query(self):
        """Tests if a ``LogQuery`` is available.

        :return: ``true`` if a log query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_log_query(self):
        """Gets the query for a log.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the log query
        :rtype: ``osid.logging.LogQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_log_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_log_query()`` is ``true``.*

        """
        return  # osid.logging.LogQuery

    ancestor_log_query = property(fget=get_ancestor_log_query)

    @abc.abstractmethod
    def match_any_ancestor_log(self, match):
        """Matches logs with any ancestor.

        :param match: ``true`` to match logs with any ancestor, ``false`` to match root logs
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_log_terms(self):
        """Clesrs the ancestor log terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_log_terms = property(fdel=clear_ancestor_log_terms)

    @abc.abstractmethod
    def match_descendant_log_id(self, log_id, match):
        """Sets the log ``Id`` for this query to match logs that have the specified log as a descendant.

        :param log_id: a log ``Id``
        :type log_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_log_id_terms(self):
        """Clesrs the descendant log ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_log_id_terms = property(fdel=clear_descendant_log_id_terms)

    @abc.abstractmethod
    def supports_descendant_log_query(self):
        """Tests if a ``LogQuery`` is available.

        :return: ``true`` if a log query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_log_query(self):
        """Gets the query for a log.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the log query
        :rtype: ``osid.logging.LogQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_log_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_log_query()`` is ``true``.*

        """
        return  # osid.logging.LogQuery

    descendant_log_query = property(fget=get_descendant_log_query)

    @abc.abstractmethod
    def match_any_descendant_log(self, match):
        """Matches logs with any descendant.

        :param match: ``true`` to match logs with any descendant, ``false`` to match leaf logs
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_log_terms(self):
        """Clesrs the descendant log terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_log_terms = property(fdel=clear_descendant_log_terms)

    @abc.abstractmethod
    def get_log_query_record(self, log_record_type):
        """Gets the log query record corresponding to the given ``Log`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param log_record_type: a log record type
        :type log_record_type: ``osid.type.Type``
        :return: the log query record
        :rtype: ``osid.logging.records.LogQueryRecord``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.records.LogQueryRecord
