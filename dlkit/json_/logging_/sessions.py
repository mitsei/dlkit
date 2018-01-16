"""JSON implementations of logging sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from bson.objectid import ObjectId


from . import objects
from . import queries
from .. import utilities
from ..id.objects import IdList
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import *
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.logging_ import sessions as abc_logging_sessions
from dlkit.abstract_osid.logging_.objects import LogEntryForm as ABCLogEntryForm
from dlkit.abstract_osid.logging_.objects import LogForm as ABCLogForm
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.primitives import Type as ABCType


DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')
COMPARATIVE = 0
PLENARY = 1


class LoggingSession(abc_logging_sessions.LoggingSession, osid_sessions.OsidSession):
    """This session is used to log entries to a log."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        OsidSession.__init__(self)
        self._catalog_class = objects.Log
        self._catalog_name = 'Log'
        OsidSession._init_object(self, catalog_id, proxy, runtime, db_name='logging', cat_name='Log', cat_class=objects.Log)
        self._forms = dict()
        lm = self._get_provider_manager('LOGGING')
        self._leas = lm.get_log_entry_admin_session_for_log(self._catalog_id, proxy=self._proxy)
        self._lels = lm.get_log_entry_lookup_session_for_log(self._catalog_id, proxy=self._proxy)
        self._content_types = lm.get_content_types()

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Log Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        return: (osid.logging.Log) - the log
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    log = property(fget=get_log)

    def can_log(self):
        """Tests if this user can log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer logging
        operations.

        return: (boolean) - ``false`` if logging methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def log(self, content, content_type):
        """Logs an item.

        This method is a shortcut to ``createLogEntry()``.

        arg:    content (object): the entry to log
        arg:    content_type (osid.type.Type): the type of this entry
                which must be one of the types returned by
                ``LoggingManager.getContentTypes()``
        raise:  InvalidArgument - ``content`` is not of ``content_type``
        raise:  NullArgument - ``content`` or ``content_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported -
                ``LoggingManager.supportsContentType(contentType)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        if content_type not in self._content_types:
            raise errors.Unsupported()
        lefc = self._leas.get_content_form_for_create([])
        lefc.set_timestamp(DateTime.utcnow())

    @utilities.arguments_not_none
    def log_at_priority(self, priority_type, content, content_type):
        """Logs an item.

        arg:    priority_type (osid.type.Type): the entry priority
        arg:    content (object): the entry to log
        arg:    content_type (osid.type.Type): the type of this entry
                which must be one of the types returned by
                ``LoggingManager.getContentTypes()``
        raise:  InvalidArgument - ``content`` is not of ``content_type``
        raise:  NullArgument - ``content`` , ``content_type`` or
                ``priority_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported -
                ``LoggingManager.supportsContentType(contentType)`` is
                ``false`` or
                ``LoggingManager.supportsPriorityType(priorityType)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_log_entry_form(self):
        """Gets a log entry form for creating a log entry.

        return: (osid.logging.LogEntryForm) - the log entry form
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    log_entry_form = property(fget=get_log_entry_form)

    @utilities.arguments_not_none
    def create_log_entry(self, log_entry_form):
        """Logs an entry through the log entry form.

        arg:    log_entry_form (osid.logging.LogEntryForm): the log
                entry form
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``log_entry_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``log_entry_form`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogEntryLookupSession(abc_logging_sessions.LogEntryLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``log entries``."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Log
        self._catalog_name = 'Log'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='logging',
            cat_name='Log',
            cat_class=objects.Log)
        self._kwargs = kwargs

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Log Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        return: (osid.logging.Log) - the log
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    log = property(fget=get_log)

    def can_read_log(self):
        """Tests if this user can read the log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer reading
        operations.

        return: (boolean) - ``false`` if reading methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        """Tests if this user can read the log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer reading
        operations.

        return: (boolean) - ``false`` if reading methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.can_lookup_log_entries()

    def can_lookup_log_entries(self):
        """Tests if a user can read logs :)"""
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_log_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_log_entry_view(self):
        """A complete view of the ``LogEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in logs which are children
        of this log in the log hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this log only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_log_entry(self, log_entry_id):
        """Gets the ``LogEntry`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``LogEntry`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``LogEntry`` and retained for
        compatibility.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``LogEntry`` to retrieve
        return: (osid.logging.LogEntry) - the returned ``LogEntry``
        raise:  NotFound - no ``LogEntry`` found with the given ``Id``
        raise:  NullArgument - ``log_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(log_entry_id, 'logging').get_identifier())},
                 **self._view_filter()))
        return objects.LogEntry(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_log_entries_by_ids(self, log_entry_ids):
        """Gets a ``LogEntryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the entries
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible logentries may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    log_entry_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.logging.LogEntryList) - the returned ``LogEntry
                list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``log_entry_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        object_id_list = []
        for i in log_entry_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'logging').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.LogEntryList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_log_entries_by_genus_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` corresponding to the given log entry genus ``Type`` which doe snot include entries of genus types derived form the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session

        arg:    log_entry_genus_type (osid.type.Type): a log entry genus
                type
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  NullArgument - ``log_entry_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(log_entry_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.LogEntryList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_log_entries_by_parent_genus_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` corresponding to the given log entry genus ``Type`` and include any additional entries with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    log_entry_genus_type (osid.type.Type): a log entry genus
                type
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  NullArgument - ``log_entry_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.LogEntryList([])

    @utilities.arguments_not_none
    def get_log_entries_by_record_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` containing the given log entry record ``Type``.

        In plenary mode, the returned list contains all known log
        entries or an error results. Otherwise, the returned list may
        contain only those log entries that are accessible through this
        session.

        arg:    log_entry_genus_type (osid.type.Type): a log entry genus
                type
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  NullArgument - ``log_entry_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.LogEntryList([])

    @utilities.arguments_not_none
    def get_log_entries_by_priority_type(self, priority_type):
        """Gets a ``LogEntryList`` filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    priority_type (osid.type.Type): a log entry priority
                type
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  NullArgument - ``priority_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_entries_by_date(self, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    start (osid.calendaring.DateTime): a starting time
        arg:    end (osid.calendaring.DateTime): a starting time
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  InvalidArgument - ``start`` is greater than ``end``
        raise:  NullArgument - ``start`` or ``end`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_entries_by_priority_type_and_date(self, priority_type, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    priority_type (osid.type.Type): a log entry priority
                type
        arg:    start (osid.calendaring.DateTime): a starting time
        arg:    end (osid.calendaring.DateTime): a starting time
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  InvalidArgument - ``start`` is greater than ``end``
        raise:  NullArgument - ``priority_type, start`` or ``end`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_entries_for_resource(self, resource_id):
        """Gets a ``LogEntryList`` for an agent associated with the given resource.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_entries_by_date_for_resource(self, resource_id, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive for an agent associated with the given resource.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    start (osid.calendaring.DateTime): a starting time
        arg:    end (osid.calendaring.DateTime): a starting time
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  InvalidArgument - ``start`` is greater than ``end``
        raise:  NullArgument - ``resource_id, start`` or ``end`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_log_entries_by_priority_type_and_date_for_resource(self, resource_id, priority_type, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive for an agent associated with the given resource filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    priority_type (osid.type.Type): a log entry priority
                type
        arg:    start (osid.calendaring.DateTime): a starting time
        arg:    end (osid.calendaring.DateTime): a starting time
        return: (osid.logging.LogEntryList) - the returned ``LogEntry``
                list
        raise:  InvalidArgument - ``start`` is greater than ``end``
        raise:  NullArgument - ``resource_id, priority_type, start`` or
                ``end`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_log_entries(self):
        """Gets all log entries.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        return: (osid.logging.LogEntryList) - a list of log entries
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.LogEntryList(result, runtime=self._runtime, proxy=self._proxy)

    log_entries = property(fget=get_log_entries)


class LogEntryQuerySession(abc_logging_sessions.LogEntryQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among log entries.

    The search query is constructed using the ``LogEntryQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated log view: searches include entries in logs of which
        this log is an ancestor in the log hierarchy
      * isolated log view: searches are restricted to entries in this
        log only

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Log
        self._catalog_name = 'Log'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='logging',
            cat_name='Log',
            cat_class=objects.Log)
        self._kwargs = kwargs

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Log Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        return: (osid.logging.Log) - the ``Log`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    log = property(fget=get_log)

    def can_search_log_entries(self):
        """Tests if this user can perform ``LogEntry`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in logs which are children
        of this log in the log hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this log only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_log_entry_query(self):
        """Gets a log entry query.

        return: (osid.logging.LogEntryQuery) - the log entry query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.LogEntryQuery(runtime=self._runtime)

    log_entry_query = property(fget=get_log_entry_query)

    @utilities.arguments_not_none
    def get_log_entries_by_query(self, log_entry_query):
        """Gets a list of log entries matching the given log entry query.

        arg:    log_entry_query (osid.logging.LogEntryQuery): the log
                entry query
        return: (osid.logging.LogEntryList) - the returned
                ``LogEntryList``
        raise:  NullArgument - ``log_entry_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``log_entry_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in log_entry_query._query_terms:
            if '$in' in log_entry_query._query_terms[term] and '$nin' in log_entry_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': log_entry_query._query_terms[term]['$in']}},
                             {term: {'$nin': log_entry_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: log_entry_query._query_terms[term]})
        for term in log_entry_query._keyword_terms:
            or_list.append({term: log_entry_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('logging',
                                             collection='LogEntry',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.LogEntryList(result, runtime=self._runtime, proxy=self._proxy)


class LogEntryAdminSession(abc_logging_sessions.LogEntryAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``LogEntries``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``LogEntry,`` a ``LogEntryForm`` is requested using
    ``get_log_entry_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LogEntryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LogEntryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LogEntryForm``
    corresponds to an attempted transaction.

    For updates, ``LogEntryForms`` are requested to the ``LogEntry``
    ``Id`` that is to be updated using ``getLogEntryFormForUpdate()``.
    Similarly, the ``LogEntryForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``LogEntryForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``LogEntries``. To unmap a ``LogEntry``
    from the current ``Log,`` the ``LogEntryLogAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``LogEntry`` itself thus removing it from all known ``Log``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Log
        self._catalog_name = 'Log'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='logging',
            cat_name='Log',
            cat_class=objects.Log)
        self._forms = dict()
        self._kwargs = kwargs

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Log Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        return: (osid.logging.Log) - the ``Log`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    log = property(fget=get_log)

    def can_create_log_entries(self):
        """Tests if this user can create log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``LogEntry`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs()
        return True

    @utilities.arguments_not_none
    def can_create_log_entry_with_record_types(self, log_entry_record_types):
        """Tests if this user can create a single ``LogEntry`` using the desired record types.

        While ``LoggingManager.getLogEntryRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``LogEntry``.
        Providing an empty array tests if a ``LogEntry`` can be created
        with no records.

        arg:    log_entry_record_types (osid.type.Type[]): array of log
                entry record types
        return: (boolean) - ``true`` if ``LogEntry`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``log_entry_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=log_entry_record_types)
        return True

    @utilities.arguments_not_none
    def get_log_entry_form_for_create(self, log_entry_record_types):
        """Gets the log entry form for creating new log entries.

        A new form should be requested for each create transaction.

        arg:    log_entry_record_types (osid.type.Type[]): array of log
                entry record types
        return: (osid.logging.LogEntryForm) - the log entry form
        raise:  NullArgument - ``log_entry_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in log_entry_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if log_entry_record_types == []:
            obj_form = objects.LogEntryForm(
                log_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.LogEntryForm(
                log_id=self._catalog_id,
                record_types=log_entry_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_log_entry(self, log_entry_form):
        """Creates a new ``LogEntry``.

        arg:    log_entry_form (osid.logging.LogEntryForm): the form for
                this ``LogEntry``
        return: (osid.logging.LogEntry) - the new ``LogEntry``
        raise:  IllegalState - ``log_entry_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``log_entry_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``log_entry_form`` did not originate from
                ``get_log_entry_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        if not isinstance(log_entry_form, ABCLogEntryForm):
            raise errors.InvalidArgument('argument type is not an LogEntryForm')
        if log_entry_form.is_for_update():
            raise errors.InvalidArgument('the LogEntryForm is for update only, not create')
        try:
            if self._forms[log_entry_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('log_entry_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('log_entry_form did not originate from this session')
        if not log_entry_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')

        if 'timestamp' not in log_entry_form._my_map or log_entry_form._my_map['timestamp'] is None:
            log_entry_form._my_map['timestamp'] = DateTime.utcnow()
        log_entry_form._my_map['agentId'] = str(self.get_effective_agent_id())

        insert_result = collection.insert_one(log_entry_form._my_map)

        self._forms[log_entry_form.get_id().get_identifier()] = CREATED
        result = objects.LogEntry(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_log_entries(self):
        """Tests if this user can update log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``LogEntry`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_update_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_update_catalogs()
        return True

    @utilities.arguments_not_none
    def get_log_entry_form_for_update(self, log_entry_id):
        """Gets the log entry form for updating an existing log.

        A new log entry form should be requested for each update
        transaction.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``LogEntry``
        return: (osid.logging.LogEntryForm) - the log entry form
        raise:  NotFound - ``log_entry_id`` is not found
        raise:  NullArgument - ``log_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        if not isinstance(log_entry_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (log_entry_id.get_identifier_namespace() != 'logging.LogEntry' or
                log_entry_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(log_entry_id.get_identifier())})

        obj_form = objects.LogEntryForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_log_entry(self, log_entry_form):
        """Updates an existing log entry.

        arg:    log_entry_form (osid.logging.LogEntryForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``log_entry_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``log_entry_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``log_entry_form`` did not originate from
                ``get_log_entry_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        if not isinstance(log_entry_form, ABCLogEntryForm):
            raise errors.InvalidArgument('argument type is not an LogEntryForm')
        if not log_entry_form.is_for_update():
            raise errors.InvalidArgument('the LogEntryForm is for update only, not create')
        try:
            if self._forms[log_entry_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('log_entry_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('log_entry_form did not originate from this session')
        if not log_entry_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(log_entry_form._my_map)

        self._forms[log_entry_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.LogEntry(
            osid_object_map=log_entry_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_log_entries(self):
        """Tests if this user can delete log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``LogEntry`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_delete_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_delete_catalogs()
        return True

    @utilities.arguments_not_none
    def delete_log_entry(self, log_entry_id):
        """Deletes a ``LogEntry``.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``log_entry_id`` to remove
        raise:  NotFound - ``log_entry_id`` not found
        raise:  NullArgument - ``log_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        if not isinstance(log_entry_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        log_entry_map = collection.find_one(
            dict({'_id': ObjectId(log_entry_id.get_identifier())},
                 **self._view_filter()))

        objects.LogEntry(osid_object_map=log_entry_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(log_entry_id.get_identifier())})

    def can_manage_log_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``LogEntry`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_log_entry(self, log_entry_id, alias_id):
        """Adds an ``Id`` to a ``LogEntry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``LogEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another log entry, it is
        reassigned to the given log entry ``Id``.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of a ``LogEntry``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``log_entry_id`` not found
        raise:  NullArgument - ``log_entry_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=log_entry_id, equivalent_id=alias_id)


class LogEntryLogSession(abc_logging_sessions.LogEntryLogSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``LogEntry`` to ``Log`` mappings.

    An entry may appear in multiple ``Logs``. Each ``Log`` may have its
    own authorizations governing who is allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'logging.LogEntryLogSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_log_view(self):
        """A complete view of the ``LogEntry`` and ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    def can_lookup_log_entry_log_mappings(self):
        """Tests if this user can perform lookups of logEntry/log mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_log_entry_ids_by_log(self, log_id):
        """Gets the list of ``LogEntry``  ``Ids`` associated with a ``Log``.

        arg:    log_id (osid.id.Id): ``Id`` of a ``Log``
        return: (osid.id.IdList) - list of related logEntry ``Ids``
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for log_entry in self.get_log_entries_by_log(log_ids):
            id_list.append(log_entry.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_log_entries_by_log(self, log_id):
        """Gets the list of log entries associated with a ``Log``.

        arg:    log_id (osid.id.Id): ``Id`` of a ``Log``
        return: (osid.logging.LogEntryList) - list of related logEntry
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('LOGGING', local=True)
        lookup_session = mgr.get_log_entry_lookup_session_for_log(log_id, proxy=self._proxy)
        lookup_session.use_isolated_log_view()
        return lookup_session.get_log_entries()

    @utilities.arguments_not_none
    def get_log_entry_ids_by_log(self, log_ids):
        """Gets the list of ``LogEntry Ids`` corresponding to a list of ``Log`` objects.

        arg:    log_ids (osid.id.IdList): list of log ``Ids``
        return: (osid.id.IdList) - list of logEntry ``Ids``
        raise:  NullArgument - ``log_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for log_entry in self.get_log_entries_by_log(log_ids):
            id_list.append(log_entry.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_log_entrie_by_log(self, log_ids):
        """Gets the list of log entries corresponding to a list of ``Log``.

        arg:    log_ids (osid.id.IdList): list of log ``Ids``
        return: (osid.logging.LogEntryList) - list of log entries
        raise:  NullArgument - ``log_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('LOGGING', local=True)
        lookup_session = mgr.get_log_entry_lookup_session_for_log(log_ids, proxy=self._proxy)
        lookup_session.use_isolated_log_view()
        return lookup_session.get_log_entries()

    @utilities.arguments_not_none
    def get_log_ids_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log``  ``Ids`` mapped to a ``LogEntry``.

        arg:    log_entry_id (osid.id.Id): ``Id`` of a ``LogEntry``
        return: (osid.id.IdList) - list of log ``Ids``
        raise:  NotFound - ``log_entry_id`` is not found
        raise:  NullArgument - ``log_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('LOGGING', local=True)
        lookup_session = mgr.get_log_entry_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_log_view()
        log_entry = lookup_session.get_log_entry(log_entry_id)
        id_list = []
        for idstr in log_entry._my_map['assignedLogIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_log_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log`` objects mapped to a ``LogEntry``.

        arg:    log_entry_id (osid.id.Id): ``Id`` of a ``LogEntry``
        return: (osid.logging.LogList) - list of log
        raise:  NotFound - ``log_entry_id`` is not found
        raise:  NullArgument - ``log_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class LogEntryLogAssignmentSession(abc_logging_sessions.LogEntryLogAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign log entries to ``Logs``.

    A ``LogEntry`` may map to multiple ``Log`` objects and removing the
    last reference to a ``LogEntry`` is the equivalent of deleting it.
    Each ``Log`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of a ``LogEntry`` to another ``Log`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'logging.LogEntryLogAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Log'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_log_entries(self):
        """Tests if this user can alter log entry/log mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_assign_log_entries_to_log(self, log_id):
        """Tests if this user can alter log entry/log mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``log_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if log_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_log_ids(self, log_id):
        """Gets a list of log including and under the given log node in which any log entry can be assigned.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.id.IdList) - list of assignable log ``Ids``
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('LOGGING', local=True)
        lookup_session = mgr.get_log_lookup_session(proxy=self._proxy)
        logs = lookup_session.get_logs()
        id_list = []
        for log in logs:
            id_list.append(log.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_log_ids_for_log_entry(self, log_id, log_entry_id):
        """Gets a list of log including and under the given log node in which a specific log entry can be assigned.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``LogEntry``
        return: (osid.id.IdList) - list of assignable log ``Ids``
        raise:  NullArgument - ``log_id`` or ``log_entry_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_log_ids(log_id)

    @utilities.arguments_not_none
    def assign_log_entry_to_log(self, log_entry_id, log_id):
        """Adds an existing ``LogEntry`` to a ``Log``.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``LogEntry``
        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        raise:  AlreadyExists - ``log_entry_id`` is already assigned to
                ``log_id``
        raise:  NotFound - ``log_entry_id`` or ``log_id`` not found
        raise:  NullArgument - ``log_entry_id`` or ``log_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('LOGGING', local=True)
        lookup_session = mgr.get_log_lookup_session(proxy=self._proxy)
        lookup_session.get_log(log_id)  # to raise NotFound
        self._assign_object_to_catalog(log_entry_id, log_id)

    @utilities.arguments_not_none
    def unassign_log_entry_from_log(self, log_entry_id, log_id):
        """Removes a ``LogEntry`` from a ``Log``.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``LogEntry``
        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        raise:  NotFound - ``log_entry_id`` or ``log_id`` not found or
                ``log_entry_id`` not assigned to ``log_id``
        raise:  NullArgument - ``log_entry_id`` or ``log_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('LOGGING', local=True)
        lookup_session = mgr.get_log_lookup_session(proxy=self._proxy)
        lookup_session.get_log(log_id)  # to raise NotFound
        self._unassign_object_from_catalog(log_entry_id, log_id)

    @utilities.arguments_not_none
    def reassign_log_entry_to_log(self, log_entry_id, from_log_id, to_log_id):
        """Moves a ``LogEntry`` from one ``Log`` to another.

        Mappings to other ``Logs`` are unaffected.

        arg:    log_entry_id (osid.id.Id): the ``Id`` of the
                ``LogEntry``
        arg:    from_log_id (osid.id.Id): the ``Id`` of the current
                ``Log``
        arg:    to_log_id (osid.id.Id): the ``Id`` of the destination
                ``Log``
        raise:  NotFound - ``log_entry_id, from_log_id,`` or
                ``to_log_id`` not found or ``log_entry_id`` not mapped
                to ``from_log_id``
        raise:  NullArgument - ``log_entry_id, from_log_id,`` or
                ``to_log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.reassign_resource_to_bin
        self.assign_log_entry_to_log(log_entry_id, to_log_id)
        try:
            self.unassign_log_entry_from_log(log_entry_id, from_log_id)
        except:  # something went wrong, roll back assignment to to_log_id
            self.unassign_log_entry_from_log(log_entry_id, to_log_id)
            raise


class LogLookupSession(abc_logging_sessions.LogLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Log`` objects.

    The ``Log`` represents a collection of log entries.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Logs`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Logs`` referenced
    by it are available, and a test-taking applicationmay sacrifice some
    interoperability for the sake of precision.

    """
    _session_namespace = 'logging.LogLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_logs(self):
        """Tests if this user can perform ``Log`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.can_lookup_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_lookup_catalogs()
        return True

    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_log_view(self):
        """A complete view of the ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_log(self, log_id):
        """Gets the ``Log`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Log`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Log`` and retained for compatibility.

        arg:    log_id (osid.id.Id): ``Id`` of the ``Log``
        return: (osid.logging.Log) - the log
        raise:  NotFound - ``log_id`` not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=log_id)
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if log_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.Log, cat_name='Log')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(log_id, 'logging').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Log.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(log_id, 'logging', 'Log')

        return objects.Log(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_logs_by_ids(self, log_ids):
        """Gets a ``LogList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the logs
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Logs`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    log_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.logging.LogList) - the returned ``Log list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``log_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Log() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=log_ids)
        catalog_id_list = []
        for i in log_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.LogList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_logs_by_genus_type(self, log_genus_type):
        """Gets a ``LogList`` corresponding to the given log genus ``Type`` which does not include logs of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        arg:    log_genus_type (osid.type.Type): a log genus type
        return: (osid.logging.LogList) - the returned ``Log list``
        raise:  NullArgument - ``log_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=log_genus_type)
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(log_genus_type)}).sort('_id', DESCENDING)

        return objects.LogList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_logs_by_parent_genus_type(self, log_genus_type):
        """Gets a ``LogList`` corresponding to the given log genus ``Type`` and include any additional logs with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        arg:    log_genus_type (osid.type.Type): a log genus type
        return: (osid.logging.LogList) - the returned ``Log list``
        raise:  NullArgument - ``log_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_logs_by_record_type(self, log_record_type):
        """Gets a ``LogList`` containing the given log record ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        arg:    log_record_type (osid.type.Type): a log record type
        return: (osid.logging.LogList) - the returned ``Log list``
        raise:  NullArgument - ``log_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_logs_by_provider(self, resource_id):
        """Gets a ``LogList`` for a given provider.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.logging.LogList) - the returned ``Log list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_logs(self):
        """Gets all ``Logs``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        return: (osid.logging.LogList) - a list of ``Logs``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.LogList(result, runtime=self._runtime, proxy=self._proxy)

    logs = property(fget=get_logs)


class LogAdminSession(abc_logging_sessions.LogAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Logs``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Log,`` a ``LogForm`` is requested using
    ``get_log_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LogForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LogForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LogForm`` corresponds
    to an attempted transaction.

    For updates, ``LogForms`` are requested to the ``Log``  ``Id`` that
    is to be updated using ``getLogFormForUpdate()``. Similarly, the
    ``LogForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``LogForm``
    can only be used once for a successful update and cannot be reused.

    The delete operations delete ``Logs``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    _session_namespace = 'logging.LogAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_logs(self):
        """Tests if this user can create ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Log`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs()
        return True

    @utilities.arguments_not_none
    def can_create_log_with_record_types(self, log_record_types):
        """Tests if this user can create a single ``Log`` using the desired record types.

        While ``LoggingManager.getLogRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Log``.
        Providing an empty array tests if a ``Log`` can be created with
        no records.

        arg:    log_record_types (osid.type.Type[]): array of log record
                types
        return: (boolean) - ``true`` if ``Log`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``log_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=log_record_types)
        return True

    @utilities.arguments_not_none
    def get_log_form_for_create(self, log_record_types):
        """Gets the log form for creating new logs.

        A new form should be requested for each create transaction.

        arg:    log_record_types (osid.type.Type[]): array of log record
                types
        return: (osid.logging.LogForm) - the log form
        raise:  NullArgument - ``log_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=log_record_types)
        for arg in log_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if log_record_types == []:
            result = objects.LogForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.LogForm(
                record_types=log_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_log(self, log_form):
        """Creates a new ``Log``.

        arg:    log_form (osid.logging.LogForm): the form for this
                ``Log``
        return: (osid.logging.Log) - the new ``Log``
        raise:  IllegalState - ``log_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``log_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``log_form`` did not originate from
                ``get_log_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=log_form)
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        if not isinstance(log_form, ABCLogForm):
            raise errors.InvalidArgument('argument type is not an LogForm')
        if log_form.is_for_update():
            raise errors.InvalidArgument('the LogForm is for update only, not create')
        try:
            if self._forms[log_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('log_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('log_form did not originate from this session')
        if not log_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(log_form._my_map)

        self._forms[log_form.get_id().get_identifier()] = CREATED
        result = objects.Log(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_logs(self):
        """Tests if this user can update ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Log`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_update_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_update_catalogs()
        return True

    @utilities.arguments_not_none
    def get_log_form_for_update(self, log_id):
        """Gets the log form for updating an existing log.

        A new log form should be requested for each update transaction.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LogForm) - the log form
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=log_id)
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        if not isinstance(log_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(log_id.get_identifier())})

        cat_form = objects.LogForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_log(self, log_form):
        """Updates an existing log.

        arg:    log_form (osid.logging.LogForm): the form containing the
                elements to be updated
        raise:  IllegalState - ``log_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``log_id`` or ``log_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``log_form`` did not originate from
                ``get_log_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=log_form)
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        if not isinstance(log_form, ABCLogForm):
            raise errors.InvalidArgument('argument type is not an LogForm')
        if not log_form.is_for_update():
            raise errors.InvalidArgument('the LogForm is for update only, not create')
        try:
            if self._forms[log_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('log_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('log_form did not originate from this session')
        if not log_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(log_form._my_map)  # save is deprecated - change to replace_one

        self._forms[log_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Log(osid_object_map=log_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_logs(self):
        """Tests if this user can delete ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Log`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_delete_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_delete_catalogs()
        return True

    @utilities.arguments_not_none
    def delete_log(self, log_id):
        """Deletes a ``Log``.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log`` to remove
        raise:  NotFound - ``log_id`` not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=log_id)
        collection = JSONClientValidated('logging',
                                         collection='Log',
                                         runtime=self._runtime)
        if not isinstance(log_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['LogEntry', 'Log']:
            obj_collection = JSONClientValidated('logging',
                                                 collection=object_catalog,
                                                 runtime=self._runtime)
            if obj_collection.find({'assignedLogIds': {'$in': [str(log_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(log_id.get_identifier())})

    def can_manage_log_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Log`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_log(self, log_id, alias_id):
        """Adds an ``Id`` to a ``Log`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Log`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another log, it is reassigned to the
        given log ``Id``.

        arg:    log_id (osid.id.Id): the ``Id`` of a ``Log``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``log_id`` not found
        raise:  NullArgument - ``log_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=log_id, alias_id=alias_id)
        self._alias_id(primary_id=log_id, equivalent_id=alias_id)


class LogHierarchySession(abc_logging_sessions.LogHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Log`` objects.

    Each node in the hierarchy is a unique ``Log``. The hierarchy may be
    traversed recursively to establish the tree structure through
    ``get_parent_logs()`` and ``getChildLogs()``. To relate these
    ``Ids`` to another OSID, ``get_log_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Log`` available in the Log OSID is known to this hierarchy but
    does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_logs()`` or ``get_child_logs()`` in lieu of
    a ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: log elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    _session_namespace = 'logging.LogHierarchySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchySession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_traversal_session_for_hierarchy(
                Id(authority='LOGGING',
                   namespace='CATALOG',
                   identifier='LOG'),
                proxy=self._proxy)

    def get_log_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_access_log_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_access_catalog_hierarchy()
        return True

    def use_comparative_log_view(self):
        """The returns from the log methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_log_view(self):
        """A complete view of the ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    def get_root_log_ids(self):
        """Gets the root log ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root log ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalog_ids()
        return self._hierarchy_session.get_roots()

    root_log_ids = property(fget=get_root_log_ids)

    def get_root_logs(self):
        """Gets the root logs in the log hierarchy.

        A node with no parents is an orphan. While all log ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        return: (osid.logging.LogList) - the root logs
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalogs()
        return LogLookupSession(
            self._proxy,
            self._runtime).get_logs_by_ids(list(self.get_root_log_ids()))

    root_logs = property(fget=get_root_logs)

    @utilities.arguments_not_none
    def has_parent_logs(self, log_id):
        """Tests if the ``Log`` has any parents.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (boolean) - ``true`` if the log has parents, ``false``
                otherwise
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_parent_catalogs(catalog_id=log_id)
        return self._hierarchy_session.has_parents(id_=log_id)

    @utilities.arguments_not_none
    def is_parent_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct parent of a log.

        arg:    id (osid.id.Id): an ``Id``
        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``log_id,``  ``false`` otherwise
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``id`` or ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_parent_of_catalog(id_=id_, catalog_id=log_id)
        return self._hierarchy_session.is_parent(id_=log_id, parent_id=id_)

    @utilities.arguments_not_none
    def get_parent_log_ids(self, log_id):
        """Gets the parent ``Ids`` of the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (osid.id.IdList) - the parent ``Ids`` of the log
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalog_ids(catalog_id=log_id)
        return self._hierarchy_session.get_parents(id_=log_id)

    @utilities.arguments_not_none
    def get_parent_logs(self, log_id):
        """Gets the parent logs of the given ``id``.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log`` to query
        return: (osid.logging.LogList) - the parent logs of the ``id``
        raise:  NotFound - a ``Log`` identified by ``Id is`` not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalogs(catalog_id=log_id)
        return LogLookupSession(
            self._proxy,
            self._runtime).get_logs_by_ids(
                list(self.get_parent_log_ids(log_id)))

    @utilities.arguments_not_none
    def is_ancestor_of_log(self, id_, log_id):
        """Tests if an ``Id`` is an ancestor of a log.

        arg:    id (osid.id.Id): an ``Id``
        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (boolean) - ``true`` if the ``id`` is an ancestor of the
                ``log_id,``  ``false`` otherwise
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``id`` or ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_ancestor_of_catalog(id_=id_, catalog_id=log_id)
        return self._hierarchy_session.is_ancestor(id_=id_, ancestor_id=log_id)

    @utilities.arguments_not_none
    def has_child_logs(self, log_id):
        """Tests if a log has any children.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (boolean) - ``true`` if the ``log_id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_child_catalogs(catalog_id=log_id)
        return self._hierarchy_session.has_children(id_=log_id)

    @utilities.arguments_not_none
    def is_child_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct child of a log.

        arg:    id (osid.id.Id): an ``Id``
        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (boolean) - ``true`` if this ``id`` is a child of
                ``log_id,``  ``false`` otherwise
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``id`` or ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_child_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_child_of_catalog(id_=id_, catalog_id=log_id)
        return self._hierarchy_session.is_child(id_=log_id, child_id=id_)

    @utilities.arguments_not_none
    def get_child_log_ids(self, log_id):
        """Gets the child ``Ids`` of the given log.

        arg:    log_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the depot
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalog_ids(catalog_id=log_id)
        return self._hierarchy_session.get_children(id_=log_id)

    @utilities.arguments_not_none
    def get_child_logs(self, log_id):
        """Gets the child logs of the given ``id``.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log`` to query
        return: (osid.logging.LogList) - the child logs of the ``id``
        raise:  NotFound - a ``Log`` identified by ``Id is`` not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalogs(catalog_id=log_id)
        return LogLookupSession(
            self._proxy,
            self._runtime).get_logs_by_ids(
                list(self.get_child_log_ids(log_id)))

    @utilities.arguments_not_none
    def is_descendant_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a descendant of a log.

        arg:    id (osid.id.Id): an ``Id``
        arg:    log_id (osid.id.Id): the ``Id`` of a log
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``log_id,``  ``false`` otherwise
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``id`` or ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_descendant_of_catalog(id_=id_, catalog_id=log_id)
        return self._hierarchy_session.is_descendant(id_=id_, descendant_id=log_id)

    @utilities.arguments_not_none
    def get_log_node_ids(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a log node
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_node_ids(
                catalog_id=log_id,
                ancestor_levels=ancestor_levels,
                descendant_levels=descendant_levels,
                include_siblings=include_siblings)
        return self._hierarchy_session.get_nodes(
            id_=log_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)

    @utilities.arguments_not_none
    def get_log_nodes(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.logging.LogNode) - a log node
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_nodes
        return objects.LogNode(self.get_log_node_ids(
            log_id=log_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)._my_map, runtime=self._runtime, proxy=self._proxy)


class LogHierarchyDesignSession(abc_logging_sessions.LogHierarchyDesignSession, osid_sessions.OsidSession):
    """This session manages a hierarchy of logs.

    Logs may be organized into a hierarchy for organizing or federating.
    A parent ``Log`` includes all of the Ids of its children such that a
    single root node contains all of the ``Ids`` of the federation.

    """
    _session_namespace = 'logging.LogHierarchyDesignSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_design_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_design_session_for_hierarchy(
                Id(authority='LOGGING',
                   namespace='CATALOG',
                   identifier='LOG'),
                proxy=self._proxy)

    def get_log_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_modify_log_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_modify_catalog_hierarchy()
        return True

    @utilities.arguments_not_none
    def add_root_log(self, log_id):
        """Adds a root log.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        raise:  AlreadyExists - ``log_id`` is already in hierarchy
        raise:  NotFound - ``log_id`` is not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_root_catalog(catalog_id=log_id)
        return self._hierarchy_session.add_root(id_=log_id)

    @utilities.arguments_not_none
    def remove_root_log(self, log_id):
        """Removes a root log.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        raise:  NotFound - ``log_id`` is not a root
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_root_catalog(catalog_id=log_id)
        return self._hierarchy_session.remove_root(id_=log_id)

    @utilities.arguments_not_none
    def add_child_log(self, log_id, child_id):
        """Adds a child to a log.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``log_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``log_id`` or ``child_id`` not found
        raise:  NullArgument - ``log_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_child_catalog(catalog_id=log_id, child_id=child_id)
        return self._hierarchy_session.add_child(id_=log_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_log(self, log_id, child_id):
        """Removes a child from a log.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``log_id`` not a parent of ``child_id``
        raise:  NullArgument - ``log_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalog(catalog_id=log_id, child_id=child_id)
        return self._hierarchy_session.remove_child(id_=log_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_logs(self, log_id):
        """Removes all children from a log.

        arg:    log_id (osid.id.Id): the ``Id`` of a log
        raise:  NotFound - ``log_id`` not in hierarchy
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalogs(catalog_id=log_id)
        return self._hierarchy_session.remove_children(id_=log_id)
