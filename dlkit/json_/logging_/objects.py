"""JSON implementations of logging objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import datetime
import importlib


from . import default_mdata
from .. import utilities
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..osid.osid_errors import *
from ..primitives import *
from ..primitives import Id
from ..utilities import get_provider_manager
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.logging_ import objects as abc_logging_objects
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id


class LogEntry(abc_logging_objects.LogEntry, osid_objects.OsidObject):
    """A log entry consists of a time, an agent, and a priority type."""
    _namespace = 'logging.LogEntry'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='LOG_ENTRY', **kwargs)
        self._catalog_name = 'Log'

    def get_priority(self):
        """Gets the priority level of this entry.

        return: (osid.type.Type) - the priority level
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.logging.LogEntry.get_priority
        if not self._my_map['priority']:
            raise errors.IllegalState('this LogEntry has no priority')
        else:
            return Id(self._my_map['priority'])

    priority = property(fget=get_priority)

    def get_timestamp(self):
        """Gets the time this entry was logged.

        return: (osid.calendaring.DateTime) - the time stamp of this
                entry
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    timestamp = property(fget=get_timestamp)

    def get_resource_id(self):
        """Gets the resource ``Id`` who created this entry.

        return: (osid.id.Id) - the resource ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the ``Resource`` who created this entry.

        return: (osid.resource.Resource) - the ``Resource``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    resource = property(fget=get_resource)

    def get_agent_id(self):
        """Gets the agent ``Id`` who created this entry.

        return: (osid.id.Id) - the agent ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['agentId']):
            raise errors.IllegalState('this LogEntry has no agent')
        else:
            return Id(self._my_map['agentId'])

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the ``Agent`` who created this entry.

        return: (osid.authentication.Agent) - the ``Agent``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['agentId']):
            raise errors.IllegalState('this LogEntry has no agent')
        mgr = self._get_provider_manager('AUTHENTICATION')
        if not mgr.supports_agent_lookup():
            raise errors.OperationFailed('Authentication does not support Agent lookup')
        lookup_session = mgr.get_agent_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_agency_view()
        osid_object = lookup_session.get_agent(self.get_agent_id())
        return osid_object

    agent = property(fget=get_agent)

    @utilities.arguments_not_none
    def get_log_entry_record(self, log_entry_record_type):
        """Gets the log entry record corresponding to the given ``LogEntry`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``log_entry_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(log_entry_record_type)`` is ``true`` .

        arg:    log_entry_record_type (osid.type.Type): the type of log
                entry record to retrieve
        return: (osid.logging.records.LogEntryRecord) - the log entry
                record
        raise:  NullArgument - ``log_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(log_entry_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(log_entry_record_type)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['timestamp'] is not None:
            timestamp = obj_map['timestamp']
            obj_map['timestamp'] = dict()
            obj_map['timestamp']['year'] = timestamp.year
            obj_map['timestamp']['month'] = timestamp.month
            obj_map['timestamp']['day'] = timestamp.day
            obj_map['timestamp']['hour'] = timestamp.hour
            obj_map['timestamp']['minute'] = timestamp.minute
            obj_map['timestamp']['second'] = timestamp.second
            obj_map['timestamp']['microsecond'] = timestamp.microsecond

        obj_map = osid_objects.OsidObject.get_object_map(self, obj_map)

        return obj_map

    object_map = property(fget=get_object_map)


class LogEntryForm(abc_logging_objects.LogEntryForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating log entries.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``LogEntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='LOG_ENTRY', **kwargs)
        self._mdata = default_mdata.get_log_entry_mdata()
        self._init_metadata(**kwargs)

        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._priority_default = self._mdata['priority']['default_type_values'][0]
        self._timestamp_default = datetime.datetime.utcnow()
        self._agent_default = self._mdata['agent']['default_id_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['priorityId'] = self._priority_default
        self._my_map['timestamp'] = self._timestamp_default
        self._my_map['assignedLogIds'] = [str(kwargs['log_id'])]
        self._my_map['agentId'] = self._agent_default

    def get_priority_metadata(self):
        """Gets the metadata for a priority type.

        return: (osid.Metadata) - metadata for the priority
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.logging.LogEntryForm.get_priority_metadata
        metadata = dict(self._mdata['priority'])
        metadata.update({'existing_type_values': self._my_map['priorityId']})
        return Metadata(**metadata)

    priority_metadata = property(fget=get_priority_metadata)

    @utilities.arguments_not_none
    def set_priority(self, priority):
        """Sets the priority.

        arg:    priority (osid.type.Type): the new priority
        raise:  InvalidArgument - ``priority`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``priority`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.logging.LogEntryForm.set_priority
        if self.get_priority_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_type(priority):
            raise errors.InvalidArgument()
        self._my_map['priority'] = str(priority)

    def clear_priority(self):
        """Removes the priority.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.logging.LogEntryForm.clear_priority_template
        if (self.get_priority_metadata().is_read_only() or
                self.get_priority_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['priority'] = self._priority_default

    priority = property(fset=set_priority, fdel=clear_priority)

    def get_timestamp_metadata(self):
        """Gets the metadata for a timestamp.

        return: (osid.Metadata) - metadata for the timestamp
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['timestamp'])
        metadata.update({'existing_date_time_values': self._my_map['timestamp']})
        return Metadata(**metadata)

    timestamp_metadata = property(fget=get_timestamp_metadata)

    @utilities.arguments_not_none
    def set_timestamp(self, timestamp):
        """Sets the timestamp.

        arg:    timestamp (osid.calendaring.DateTime): the new timestamp
        raise:  InvalidArgument - ``timestamp`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``timestamp`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.set_start_time_template
        if self.get_timestamp_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_date_time(
                timestamp,
                self.get_timestamp_metadata()):
            raise errors.InvalidArgument()
        self._my_map['timestamp'] = timestamp

    timestamp = property(fset=set_timestamp)

    def get_agent_metadata(self):
        """Gets the metadata for the agent.

        return: (osid.Metadata) - metadata for the agent
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['agent'])
        metadata.update({'existing_id_values': self._my_map['agentId']})
        return Metadata(**metadata)

    agent_metadata = property(fget=get_agent_metadata)

    @utilities.arguments_not_none
    def set_agent(self, agent_id):
        """Sets the agent.

        arg:    agent_id (osid.id.Id): the new agent
        raise:  InvalidArgument - ``agent_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``agent_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_agent_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(agent_id):
            raise errors.InvalidArgument()
        self._my_map['agentId'] = str(agent_id)

    agent = property(fset=set_agent)

    @utilities.arguments_not_none
    def get_log_entry_form_record(self, log_entry_record_type):
        """Gets the ``LogEntryFormRecord`` corresponding to the given log entry record ``Type``.

        arg:    log_entry_record_type (osid.type.Type): the log entry
                record type
        return: (osid.logging.records.LogEntryFormRecord) - the log
                entry form record
        raise:  NullArgument - ``log_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(log_entry_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(log_entry_record_type)


class LogEntryList(abc_logging_objects.LogEntryList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LogList`` provides a means for accessing ``LogEntry`` elements sequentially either one at a time or many at a time.

    Examples: while (lel.hasNext()) { LogEntry entry =
    lel.getNextLogEntry(); }

    or
      while (lel.hasNext()) {
           LogEntry[] entries = lel.getNextLogEntries(lel.available());
      }

    """

    def get_next_log_entry(self):
        """Gets the next ``LogEntry`` in this list.

        return: (osid.logging.LogEntry) - the next ``LogEntry`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``LogEntry`` is available before calling
                this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(LogEntry)

    __next__ = next

    next_log_entry = property(fget=get_next_log_entry)

    @utilities.arguments_not_none
    def get_next_log_entries(self, n):
        """Gets the next set of ``LogEntry elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``LogEntry`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.logging.LogEntry) - an array of ``LogEntry``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(LogEntryList, number=n)


class Log(abc_logging_objects.Log, osid_objects.OsidCatalog):
    """A ``Log`` represents a collection of entries.

    Like all ``OsidObjects,`` a ``Log`` is identified by its Id and any
    persisted references should use the ``Id``.

    """
    _namespace = 'logging.Log'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='LOG', **kwargs)

    @utilities.arguments_not_none
    def get_log_record(self, log_record_type):
        """Gets the record corresponding to the given ``Log`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``log_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(log_record_type)`` is
        ``true`` .

        arg:    log_record_type (osid.type.Type): the type of log record
                to retrieve
        return: (osid.logging.records.LogRecord) - the log record
        raise:  NullArgument - ``log_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(log_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogForm(abc_logging_objects.LogForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Logs``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``LogAdminSession``.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    _namespace = 'logging.Log'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='LOG', **kwargs)
        self._mdata = default_mdata.get_log_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidCatalogForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm._init_map(self, record_types, **kwargs)

    @utilities.arguments_not_none
    def get_log_form_record(self, log_record_type):
        """Gets the ``LogFormRecord`` corresponding to the given log record ``Type``.

        arg:    log_record_type (osid.type.Type): the log record type
        return: (osid.logging.records.LogFormRecord) - the log form
                record
        raise:  NullArgument - ``log_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(log_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogList(abc_logging_objects.LogList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LogList`` provides a means for accessing ``Log`` elements sequentially either one at a time or many at a time.

    Examples: while (ll.hasNext()) { Log log = ll.getNextLog(); }

    or
      while (ll.hasNext()) {
           Log[] logs = ll.getNextLogs(ll.available());
      }

    """

    def get_next_log(self):
        """Gets the next ``Log`` in this list.

        return: (osid.logging.Log) - the next ``Log`` in this list. The
                ``has_next()`` method should be used to test that a next
                ``Log`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Log)

    __next__ = next

    next_log = property(fget=get_next_log)

    @utilities.arguments_not_none
    def get_next_logs(self, n):
        """Gets the next set of ``Log`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Log`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.logging.Log) - an array of ``Log`` elements.The
                length of the array is less than or equal to the number
                specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(LogList, number=n)


class LogNode(abc_logging_objects.LogNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``LogHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_log().get_object_map())
        node_map['type'] = 'LogNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for log_node in self.get_parent_log_nodes():
            node_map['parentNodes'].append(log_node.get_object_node_map())
        for log_node in self.get_child_log_nodes():
            node_map['childNodes'].append(log_node.get_object_node_map())
        return node_map

    def get_log(self):
        """Gets the ``Log`` at this node.

        return: (osid.logging.Log) - the log represented by this node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('LOGGING', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_log_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_log(Id(self._my_map['id']))

    log = property(fget=get_log)

    def get_parent_log_nodes(self):
        """Gets the parents of this log.

        return: (osid.logging.LogNodeList) - the parents of this log
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_log_nodes = []
        for node in self._my_map['parentNodes']:
            parent_log_nodes.append(LogNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return LogNodeList(parent_log_nodes)

    parent_log_nodes = property(fget=get_parent_log_nodes)

    def get_child_log_nodes(self):
        """Gets the children of this log.

        return: (osid.logging.LogNodeList) - the children of this log
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_log_nodes = []
        for node in self._my_map['childNodes']:
            parent_log_nodes.append(LogNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return LogNodeList(parent_log_nodes)

    child_log_nodes = property(fget=get_child_log_nodes)


class LogNodeList(abc_logging_objects.LogNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LogNodeList`` provides a means for accessing ``LogNode`` elements sequentially either one at a time or many at a time.

    Examples: while (lnl.hasNext()) { LogNode node =
    lnl.getNextLogNode(); }

    or
      while (lnl.hasNext()) {
           LogNode[] nodes = lnl.getNextLogNodes(lnl.available());
      }

    """

    def get_next_log_node(self):
        """Gets the next ``LogNode`` in this list.

        return: (osid.logging.LogNode) - the next ``LogNode`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``LogNode`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(LogNode)

    __next__ = next

    next_log_node = property(fget=get_next_log_node)

    @utilities.arguments_not_none
    def get_next_log_nodes(self, n):
        """Gets the next set of ``LogNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``LogNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.logging.LogNode) - an array of ``LogNode``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(LogNodeList, number=n)
