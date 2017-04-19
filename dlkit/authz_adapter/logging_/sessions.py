"""AuthZ Adapter implementations of logging sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import sessions as osid_sessions
from ..osid.osid_errors import NotFound
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from ..utilities import QueryWrapper
from ..utilities import raise_null_argument
from dlkit.abstract_osid.logging_ import sessions as abc_logging_sessions


class LoggingSession(abc_logging_sessions.LoggingSession, osid_sessions.OsidSession):
    """Adapts underlying LoggingSession methodswith authorization checks."""

    def get_log_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_log()

    log = property(fget=get_log)

    def can_log(self):
        raise Unimplemented()

    @raise_null_argument
    def log(self, content, content_type):
        raise Unimplemented()

    @raise_null_argument
    def log_at_priority(self, priority_type, content, content_type):
        raise Unimplemented()

    def get_log_entry_form(self):
        raise Unimplemented()

    log_entry_form = property(fget=get_log_entry_form)

    @raise_null_argument
    def create_log_entry(self, log_entry_form):
        raise Unimplemented()


class LogEntryLookupSession(abc_logging_sessions.LogEntryLookupSession, osid_sessions.OsidSession):
    """Adapts underlying LogEntryLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_log_id()
        self._id_namespace = 'logging.LogEntry'
        self.use_federated_log_view()
        self.use_comparative_log_entry_view()
        self._auth_log_ids = None
        self._unauth_log_ids = None
    #     self._overriding_log_ids = None
    #
    # def _get_overriding_log_ids(self):
    #     if self._overriding_log_ids is None:
    #         self._overriding_log_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_log_ids

    def _try_overriding_logs(self, query):
        for catalog_id in self._get_overriding_catalog_ids('lookup'):
            query.match_log_id(catalog_id, match=True)
        return self._query_session.get_log_entries_by_query(query), query

    def _get_unauth_log_ids(self, log_id):
        if self._can('lookup', log_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(log_id)]
        if self._hierarchy_session.has_child_logs(log_id):
            for child_log_id in self._hierarchy_session.get_child_log_ids(log_id):
                unauth_list = unauth_list + self._get_unauth_log_ids(child_log_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_logs(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_log_ids is None:
            self._unauth_log_ids = self._get_unauth_log_ids(self._qualifier_id)
        for log_id in self._unauth_log_ids:
            query.match_log_id(log_id, match=False)
        return self._query_session.get_log_entries_by_query(query)

    def get_log_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_log()

    log = property(fget=get_log)

    def can_read_log(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('read')

    def use_comparative_log_entry_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_log_entry_view()

    def use_plenary_log_entry_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_log_entry_view()

    def use_federated_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_log_view()
        if self._query_session:
            self._query_session.use_federated_log_view()

    def use_isolated_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_log_view()
        if self._query_session:
            self._query_session.use_isolated_log_view()

    @raise_null_argument
    def get_log_entry(self, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_log_entry(log_entry_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_log_entry_query()
        query.match_id(log_entry_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_log_entries_by_ids(self, log_entry_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_log_entries_by_ids(log_entry_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_log_entry_query()
        for log_entry_id in (log_entry_ids):
            query.match_id(log_entry_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_log_entries_by_genus_type(self, log_entry_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_log_entries_by_genus_type(log_entry_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_log_entry_query()
        query.match_genus_type(log_entry_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_log_entries_by_parent_genus_type(self, log_entry_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_log_entries_by_parent_genus_type(log_entry_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_log_entry_query()
        query.match_parent_genus_type(log_entry_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_log_entries_by_record_type(self, log_entry_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_log_entries_by_record_type(log_entry_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_log_entry_query()
        query.match_record_type(log_entry_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_log_entries_by_priority_type(self, priority_type):
        raise Unimplemented()

    @raise_null_argument
    def get_log_entries_by_date(self, start, end):
        raise Unimplemented()

    @raise_null_argument
    def get_log_entries_by_priority_type_and_date(self, priority_type, start, end):
        raise Unimplemented()

    @raise_null_argument
    def get_log_entries_for_resource(self, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_log_entries_by_date_for_resource(self, resource_id, start, end):
        raise Unimplemented()

    @raise_null_argument
    def get_log_entries_by_priority_type_and_date_for_resource(self, resource_id, priority_type, start, end):
        raise Unimplemented()

    def get_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_log_entries()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_log_entry_query()
        query.match_any(match=True)
        return self._try_harder(query)

    log_entries = property(fget=get_log_entries)


class LogEntryQuerySession(abc_logging_sessions.LogEntryQuerySession, osid_sessions.OsidSession):
    """Adapts underlying LogEntryQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_log_id()
        self._id_namespace = 'logging.LogEntry'
        self.use_federated_log_view()
        self._unauth_log_ids = None
        # self._overriding_log_ids = None

    # def _get_overriding_log_ids(self):
    #     if self._overriding_log_ids is None:
    #         self._overriding_log_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_log_ids

    def _try_overriding_logs(self, query):
        for log_id in self._get_overriding_catalog_ids('search'):
            query._provider_query.match_log_id(log_id, match=True)
        return self._query_session.get_log_entries_by_query(query), query

    def _get_unauth_log_ids(self, log_id):
        if self._can('search', log_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(log_id)]
        if self._hierarchy_session.has_child_logs(log_id):
            for child_log_id in self._hierarchy_session.get_child_log_ids(log_id):
                unauth_list = unauth_list + self._get_unauth_log_ids(child_log_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_logs(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_log_ids is None:
            self._unauth_log_ids = self._get_unauth_log_ids(self._qualifier_id)
        for log_id in self._unauth_log_ids:
            query._provider_query.match_log_id(log_id, match=False)
        return self._query_session.get_log_entries_by_query(query)

    class LogEntryQueryWrapper(QueryWrapper):
        """Wrapper for LogEntryQueries to override match_log_id method"""

        def match_log_id(self, log_id, match=True):
            self._cat_id_args_list.append({'log_id': log_id, 'match': match})

    def get_log_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_log()

    log = property(fget=get_log)

    def can_search_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_log_ids()))

    def use_federated_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_log_view()
        if self._query_session:
            self._query_session.use_federated_log_view()

    def use_isolated_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_log_view()
        if self._query_session:
            self._query_session.use_isolated_log_view()

    def get_log_entry_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.LogEntryQueryWrapper(self._provider_session.get_log_entry_query())

    log_entry_query = property(fget=get_log_entry_query)

    @raise_null_argument
    def get_log_entries_by_query(self, log_entry_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(log_entry_query, '_cat_id_args_list'):
            raise Unsupported('log_entry_query not from this session')
        for kwargs in log_entry_query._cat_id_args_list:
            if self._can('search', kwargs['log_id']):
                log_entry_query._provider_query.match_log_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_log_entries_by_query(log_entry_query)
        self._check_search_conditions()
        result = self._try_harder(log_entry_query)
        log_entry_query._provider_query.clear_log_terms()
        return result


class LogEntrySearchSession(abc_logging_sessions.LogEntrySearchSession, LogEntryQuerySession):
    """Adapts underlying LogEntrySearchSession methodswith authorization checks."""

    def get_log_entry_search(self):
        """Pass through to provider LogEntrySearchSession.get_log_entry_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_search()

    log_entry_search = property(fget=get_log_entry_search)

    def get_log_entry_search_order(self):
        raise Unimplemented()

    log_entry_search_order = property(fget=get_log_entry_search_order)

    @raise_null_argument
    def get_log_entries_by_search(self, log_entry_query, log_entry_search):
        """Pass through to provider LogEntrySearchSession.get_log_entries_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_log_entries_by_search(log_entry_query, log_entry_search)

    @raise_null_argument
    def get_log_entry_query_from_inspector(self, log_entry_query_inspector):
        raise Unimplemented()


class LogEntryAdminSession(abc_logging_sessions.LogEntryAdminSession, osid_sessions.OsidSession):
    """Adapts underlying LogEntryAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_log_id()
        self._id_namespace = 'logging.LogEntry'
        self._overriding_log_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_log_entry_log_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_log_entry_log_session()
                self.get_log_ids_by_log_entry = self._object_catalog_session.get_log_ids_by_log_entry
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_log_ids(self):
        if self._overriding_log_ids is None:
            self._overriding_log_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_log_ids

    def _can_for_log_entry(self, func_name, log_entry_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, log_entry_id, 'get_log_ids_for_log_entry')

    def get_log_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_log()

    log = property(fget=get_log)

    def can_create_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_log_entry_with_record_types(self, log_entry_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if log_entry_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_log_entry_form_for_create(self, log_entry_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_form_for_create(log_entry_record_types)

    @raise_null_argument
    def create_log_entry(self, log_entry_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_log_entry(log_entry_form)

    def can_update_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_log_entry_form_for_update(self, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_log_entry('update', log_entry_id):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_form_for_update(log_entry_id)

    def duplicate_log_entry(self, log_entry_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_log_entry(log_entry_id)

    @raise_null_argument
    def update_log_entry(self, log_entry_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_log_entry(log_entry_form)

    def can_delete_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_log_entry(self, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_log_entry('delete', log_entry_id):
            raise PermissionDenied()
        return self._provider_session.delete_log_entry(log_entry_id)

    def can_manage_log_entry_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_log_entry(self, log_entry_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_log_entry('alias', log_entry_id):
            raise PermissionDenied()
        return self._provider_session.alias_log_entry(log_entry_id, alias_id)


class LogEntryNotificationSession(abc_logging_sessions.LogEntryNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying LogEntryNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_log_id()
        self._id_namespace = 'logging.LogEntry'

    def get_log_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_log()

    log = property(fget=get_log)

    def can_register_for_log_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_log_view()
        if self._query_session:
            self._query_session.use_federated_log_view()

    def use_isolated_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_log_view()
        if self._query_session:
            self._query_session.use_isolated_log_view()

    def reliable_log_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_log_entry_notifications()

    def unreliable_log_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_log_entry_notifications()

    @raise_null_argument
    def acknowledge_log_entry_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_log_entries()

    @raise_null_argument
    def register_for_new_log_entries_at_priority(self, priority_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_log_entries_at_priority()

    @raise_null_argument
    def register_for_new_log_entries_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_log_entries_for_resource()

    def register_for_changed_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_log_entries()

    @raise_null_argument
    def register_for_changed_entries_at_priority(self, priority_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_entries_at_priority(priority_type)

    @raise_null_argument
    def register_for_changed_entries_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_entries_for_resource(resource_id)

    @raise_null_argument
    def register_for_changed_log_entry(self, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_log_entry(log_entry_id)

    def register_for_deleted_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_log_entries()

    @raise_null_argument
    def register_for_deleted_log_entries_at_priority(self, priority_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_log_entries_at_priority(priority_type)

    @raise_null_argument
    def register_for_deleted_log_entries_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_log_entries_for_resource(resource_id)

    @raise_null_argument
    def register_for_deleted_log_entry(self, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_log_entry(log_entry_id)

    def reliable_log_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_log_entry_notifications()

    def unreliable_log_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_log_entry_notifications()

    @raise_null_argument
    def acknowledge_log_entry_notification(self, notification_id):
        raise Unimplemented()


class LogEntryLogSession(abc_logging_sessions.LogEntryLogSession, osid_sessions.OsidSession):
    """Adapts underlying LogEntryLogSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'logging.LogEntryLog'

    def use_comparative_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_log_view()

    def use_plenary_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_log_view()

    def can_lookup_log_entry_log_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    @raise_null_argument
    def get_log_entry_ids_by_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_ids_by_log(log_id)

    @raise_null_argument
    def get_log_entries_by_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_ids_by_log(log_id)

    @raise_null_argument
    def get_log_entry_ids_by_log(self, log_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_ids_by_log(log_id)

    @raise_null_argument
    def get_log_entrie_by_log(self, log_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_log_entry_ids_by_log(log_id)

    @raise_null_argument
    def get_log_ids_by_log_entry(self, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_log_ids_by_log_entry(log_entry_id)

    @raise_null_argument
    def get_log_by_log_entry(self, log_entry_id):
        raise Unimplemented()


class LogEntryLogAssignmentSession(abc_logging_sessions.LogEntryLogAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying LogEntryLogAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'logging.LogEntryLog'

    def can_assign_log_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_log_entries_to_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=log_id)

    @raise_null_argument
    def get_assignable_log_ids(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_log_ids()

    @raise_null_argument
    def get_assignable_log_ids_for_log_entry(self, log_id, log_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_log_ids_for_log_entry(log_entry_id)

    @raise_null_argument
    def assign_log_entry_to_log(self, log_entry_id, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_log_entry_to_log(log_entry_id, log_id)

    @raise_null_argument
    def unassign_log_entry_from_log(self, log_entry_id, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_log_entry_from_log(log_entry_id, log_id)

    @raise_null_argument
    def reassign_log_entry_to_log(self, log_entry_id, from_log_id, to_log_id):
        raise Unimplemented()


class LogEntrySmartLogSession(abc_logging_sessions.LogEntrySmartLogSession, osid_sessions.OsidSession):
    """Adapts underlying LogEntrySmartLogSession methodswith authorization checks."""

    def get_log_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_log()

    log = property(fget=get_log)

    def can_manage_smart_log(self):
        raise Unimplemented()

    def get_log_entry_query(self):
        raise Unimplemented()

    log_entry_query = property(fget=get_log_entry_query)

    def get_log_entry_search_order(self):
        raise Unimplemented()

    log_entry_search_order = property(fget=get_log_entry_search_order)

    @raise_null_argument
    def apply_log_entry_query(self, log_entry_query):
        raise Unimplemented()

    def inspect_log_entry_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_log_entry_sequencing(self, log_entry_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_log_entry_query_from_inspector(self, log_entry_query_inspector):
        raise Unimplemented()


class LogLookupSession(abc_logging_sessions.LogLookupSession, osid_sessions.OsidSession):
    """Adapts underlying LogLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'logging.Log'

    def can_lookup_logs(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_log_view()

    def use_plenary_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_log_view()

    @raise_null_argument
    def get_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_log(log_id)

    @raise_null_argument
    def get_logs_by_ids(self, log_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_logs_by_ids(log_ids)

    @raise_null_argument
    def get_logs_by_genus_type(self, log_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_logs_by_genus_type(log_genus_type)

    @raise_null_argument
    def get_logs_by_parent_genus_type(self, log_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_logs_by_record_type(self, log_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_logs_by_provider(self, resource_id):
        raise Unimplemented()

    def get_logs(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_logs()

    logs = property(fget=get_logs)


class LogQuerySession(abc_logging_sessions.LogQuerySession, osid_sessions.OsidSession):
    """Adapts underlying LogQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'logging.Log'

    def can_search_logs(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_log_ids()))

    def get_log_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_log_query()

    log_query = property(fget=get_log_query)

    @raise_null_argument
    def get_logs_by_query(self, log_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_logs_by_query(log_query)


class LogSearchSession(abc_logging_sessions.LogSearchSession, LogQuerySession):
    """Adapts underlying LogSearchSession methodswith authorization checks."""

    def get_log_search(self):
        raise Unimplemented()

    log_search = property(fget=get_log_search)

    def get_log_search_order(self):
        raise Unimplemented()

    log_search_order = property(fget=get_log_search_order)

    @raise_null_argument
    def get_logs_by_search(self, log_query, log_search):
        raise Unimplemented()

    @raise_null_argument
    def get_log_query_from_inspector(self, log_query_inspector):
        raise Unimplemented()


class LogAdminSession(abc_logging_sessions.LogAdminSession, osid_sessions.OsidSession):
    """Adapts underlying LogAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'logging.Log'

    def can_create_logs(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_log_with_record_types(self, log_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if log_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_log_form_for_create(self, log_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_log_form_for_create(log_record_types)

    @raise_null_argument
    def create_log(self, log_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_log(log_form)

    def can_update_logs(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_log_form_for_update(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_log_form_for_update(log_id)

    @raise_null_argument
    def update_log(self, log_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_log(log_form)

    def can_delete_logs(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_log(log_id)

    def can_manage_log_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_log(self, log_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_log(log_id, alias_id)


class LogNotificationSession(abc_logging_sessions.LogNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying LogNotificationSession methodswith authorization checks."""

    def can_register_for_log_notifications(self):
        raise Unimplemented()

    def reliable_log_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_log_notifications()

    def unreliable_log_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_log_notifications()

    @raise_null_argument
    def acknowledge_log_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_logs(self):
        raise Unimplemented()

    def register_for_changed_logs(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_log(self, log_id):
        raise Unimplemented()

    def register_for_deleted_logs(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_log(self, log_id):
        raise Unimplemented()

    def register_for_changed_log_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_log_hierarchy()

    @raise_null_argument
    def register_for_changed_log_hierarchy_for_ancestors(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_log_hierarchy_for_ancestors(log_id)

    @raise_null_argument
    def register_for_changed_log_hierarchy_for_descendants(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_log_hierarchy_for_descendants(log_id)

    def reliable_log_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_log_notifications()

    def unreliable_log_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_log_notifications()

    @raise_null_argument
    def acknowledge_log_notification(self, notification_id):
        raise Unimplemented()


class LogHierarchySession(abc_logging_sessions.LogHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying LogHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'logging.Log'

    def get_log_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_log_hierarchy_id()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_log_hierarchy()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_access_log_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_log_view()

    def use_plenary_log_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_log_view()

    def get_root_log_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_log_ids()

    root_log_ids = property(fget=get_root_log_ids)

    def get_root_logs(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_logs()

    root_logs = property(fget=get_root_logs)

    @raise_null_argument
    def has_parent_logs(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_logs(log_id)

    @raise_null_argument
    def is_parent_of_log(self, id_, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_log(id_, log_id)

    @raise_null_argument
    def get_parent_log_ids(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_log_ids(log_id)

    @raise_null_argument
    def get_parent_logs(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_logs(log_id)

    @raise_null_argument
    def is_ancestor_of_log(self, id_, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_log(id_, log_id)

    @raise_null_argument
    def has_child_logs(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_logs(log_id)

    @raise_null_argument
    def is_child_of_log(self, id_, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_log(id_, log_id)

    @raise_null_argument
    def get_child_log_ids(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_log_ids(log_id)

    @raise_null_argument
    def get_child_logs(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_logs(log_id)

    @raise_null_argument
    def is_descendant_of_log(self, id_, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_log(id_, log_id)

    @raise_null_argument
    def get_log_node_ids(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_log_node_ids(
            log_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_log_nodes(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_log_nodes(
            log_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class LogHierarchyDesignSession(abc_logging_sessions.LogHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying LogHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('logging.Log%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'logging.Log'
        # should this be 'logging.LogHierarchy' ?

    def get_log_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_log_hierarchy_id()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_log_hierarchy()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_modify_log_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_log(log_id)

    @raise_null_argument
    def remove_root_log(self, log_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_log(log_id)

    @raise_null_argument
    def add_child_log(self, log_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_log(log_id, child_id)

    @raise_null_argument
    def remove_child_log(self, log_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_log(log_id, child_id)

    @raise_null_argument
    def remove_child_logs(self, log_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_logs(log_id)
