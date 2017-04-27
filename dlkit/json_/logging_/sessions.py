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
COMPARATIVE = 0
PLENARY = 1
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')


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
        # Implemented from template for
        # osid.resource.BinLookupSession.can_lookup_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_lookup_catalogs()
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
            return self._catalog_session.can_create_catalogs_with_record_types(catalog_record_types=log_entry_record_types)
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
        if log_entry_id.get_identifier_namespace() != 'logging.LogEntry':
            if log_entry_id.get_authority() != self._authority:
                raise errors.InvalidArgument()
            else:
                log_entry_id = self._get_log_entry_id_with_enclosure(log_entry_id)
        result = collection.find_one({'_id': ObjectId(log_entry_id.get_identifier())})

        obj_form = objects.LogEntryForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    def _get_log_entry_id_with_enclosure(self, enclosure_id):
        """Create an LogEntry with an enclosed foreign object.

        return: (osid.id.Id) - the id of the new LogEntry

        """
        mgr = self._get_provider_manager('LOGGING')
        query_session = mgr.get_log_entry_query_session_for_log(self._catalog_id, proxy=self._proxy)
        query_form = query_session.get_log_entry_query()
        query_form.match_enclosed_object_id(enclosure_id)
        query_result = query_session.get_log_entries_by_query(query_form)
        if query_result.available() > 0:
            log_entry_id = query_result.next().get_id()
        else:
            create_form = self.get_log_entry_form_for_create([ENCLOSURE_RECORD_TYPE])
            create_form.set_enclosed_object(enclosure_id)
            log_entry_id = self.create_log_entry(create_form).get_id()
        return log_entry_id

    @utilities.arguments_not_none
    def duplicate_log_entry(self, log_entry_id):
        collection = JSONClientValidated('logging',
                                         collection='LogEntry',
                                         runtime=self._runtime)
        mgr = self._get_provider_manager('LOGGING')
        lookup_session = mgr.get_log_entry_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_log_view()
        try:
            lookup_session.use_unsequestered_log_entry_view()
        except AttributeError:
            pass
        log_entry_map = dict(lookup_session.get_log_entry(log_entry_id)._my_map)
        del log_entry_map['_id']
        if 'logId' in log_entry_map:
            log_entry_map['logId'] = str(self._catalog_id)
        if 'assignedLogIds' in log_entry_map:
            log_entry_map['assignedLogIds'] = [str(self._catalog_id)]
        insert_result = collection.insert_one(log_entry_map)
        result = objects.LogEntry(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)
        return result

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
            return self._catalog_session.can_create_catalogs_with_record_types(catalog_record_types=log_record_types)
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
            return self._catalog_session.alias_catalog(catalog_id=log_id, alias_id=osid.id.Id)
        self._alias_id(primary_id=log_id, equivalent_id=alias_id)
