"""AuthZ Adapter implementations of resource sessions."""
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
from dlkit.abstract_osid.resource import sessions as abc_resource_sessions


class ResourceLookupSession(abc_resource_sessions.ResourceLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.Resource'
        self.use_federated_bin_view()
        self.use_comparative_resource_view()
        self._auth_bin_ids = None
        self._unauth_bin_ids = None
    #     self._overriding_bin_ids = None
    #
    # def _get_overriding_bin_ids(self):
    #     if self._overriding_bin_ids is None:
    #         self._overriding_bin_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_bin_ids

    def _try_overriding_bins(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_bin_id(catalog_id, match=True)
        return self._query_session.get_resources_by_query(query), query

    def _get_unauth_bin_ids(self, bin_id):
        if self._can('lookup', bin_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bin_id)]
        if self._hierarchy_session.has_child_bins(bin_id):
            for child_bin_id in self._hierarchy_session.get_child_bin_ids(bin_id):
                unauth_list = unauth_list + self._get_unauth_bin_ids(child_bin_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_bins(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bin_ids is None:
            self._unauth_bin_ids = self._get_unauth_bin_ids(self._qualifier_id)
        for bin_id in self._unauth_bin_ids:
            query.match_bin_id(bin_id, match=False)
        return self._query_session.get_resources_by_query(query)

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_lookup_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_resource_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_resource_view()

    def use_plenary_resource_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_resource_view()

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    @raise_null_argument
    def get_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_resource(resource_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_query()
        query.match_id(resource_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_resources_by_ids(self, resource_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_resources_by_ids(resource_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_query()
        for resource_id in (resource_ids):
            query.match_id(resource_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resources_by_genus_type(self, resource_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_resources_by_genus_type(resource_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_query()
        query.match_genus_type(resource_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resources_by_parent_genus_type(self, resource_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_resources_by_parent_genus_type(resource_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_query()
        query.match_parent_genus_type(resource_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resources_by_record_type(self, resource_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_resources_by_record_type(resource_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_query()
        query.match_record_type(resource_record_type, match=True)
        return self._try_harder(query)

    def get_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_resources()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_query()
        query.match_any(match=True)
        return self._try_harder(query)

    resources = property(fget=get_resources)


class ResourceQuerySession(abc_resource_sessions.ResourceQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ResourceQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.Resource'
        self.use_federated_bin_view()
        self._unauth_bin_ids = None
        # self._overriding_bin_ids = None

    # def _get_overriding_bin_ids(self):
    #     if self._overriding_bin_ids is None:
    #         self._overriding_bin_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_bin_ids

    def _try_overriding_bins(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for bin_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_bin_id(bin_id, match=True)
        return self._query_session.get_resources_by_query(query), query

    def _get_unauth_bin_ids(self, bin_id):
        if self._can('search', bin_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bin_id)]
        if self._hierarchy_session.has_child_bins(bin_id):
            for child_bin_id in self._hierarchy_session.get_child_bin_ids(bin_id):
                unauth_list = unauth_list + self._get_unauth_bin_ids(child_bin_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_bins(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bin_ids is None:
            self._unauth_bin_ids = self._get_unauth_bin_ids(self._qualifier_id)
        for bin_id in self._unauth_bin_ids:
            query._provider_query.match_bin_id(bin_id, match=False)
        return self._query_session.get_resources_by_query(query)

    class ResourceQueryWrapper(QueryWrapper):
        """Wrapper for ResourceQueries to override match_bin_id method"""

        def match_bin_id(self, bin_id, match=True):
            self._cat_id_args_list.append({'bin_id': bin_id, 'match': match})

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_search_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    def get_resource_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.ResourceQueryWrapper(self._provider_session.get_resource_query())

    resource_query = property(fget=get_resource_query)

    @raise_null_argument
    def get_resources_by_query(self, resource_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(resource_query, '_cat_id_args_list'):
            raise Unsupported('resource_query not from this session')
        for kwargs in resource_query._cat_id_args_list:
            if self._can('search', kwargs['bin_id']):
                resource_query._provider_query.match_bin_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_resources_by_query(resource_query)
        self._check_search_conditions()
        result = self._try_harder(resource_query)
        resource_query._provider_query.clear_bin_terms()
        return result


class ResourceSearchSession(abc_resource_sessions.ResourceSearchSession, ResourceQuerySession):
    """Adapts underlying ResourceSearchSession methodswith authorization checks."""

    def get_resource_search(self):
        """Pass through to provider ResourceSearchSession.get_resource_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_resource_search()

    resource_search = property(fget=get_resource_search)

    def get_resource_search_order(self):
        raise Unimplemented()

    resource_search_order = property(fget=get_resource_search_order)

    @raise_null_argument
    def get_resources_by_search(self, resource_query, resource_search):
        """Pass through to provider ResourceSearchSession.get_resources_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_resources_by_search(resource_query, resource_search)

    @raise_null_argument
    def get_resource_query_from_inspector(self, resource_query_inspector):
        raise Unimplemented()


class ResourceAdminSession(abc_resource_sessions.ResourceAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.Resource'
        self._overriding_bin_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_resource_bin_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_resource_bin_session()
                self.get_bin_ids_by_resource = self._object_catalog_session.get_bin_ids_by_resource
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bin_ids(self):
        if self._overriding_bin_ids is None:
            self._overriding_bin_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bin_ids

    def _can_for_resource(self, func_name, resource_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, resource_id, 'get_bin_ids_for_resource')

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_create_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_resource_with_record_types(self, resource_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if resource_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_resource_form_for_create(self, resource_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_resource_form_for_create(resource_record_types)

    @raise_null_argument
    def create_resource(self, resource_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_resource(resource_form)

    def can_update_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_resource_form_for_update(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_resource('update', resource_id):
            raise PermissionDenied()
        return self._provider_session.get_resource_form_for_update(resource_id)

    def duplicate_resource(self, resource_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_resource(resource_id)

    @raise_null_argument
    def update_resource(self, resource_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_resource(resource_form)

    def can_delete_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_resource('delete', resource_id):
            raise PermissionDenied()
        return self._provider_session.delete_resource(resource_id)

    def can_manage_resource_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_resource(self, resource_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_resource('alias', resource_id):
            raise PermissionDenied()
        return self._provider_session.alias_resource(resource_id, alias_id)


class ResourceNotificationSession(abc_resource_sessions.ResourceNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.Resource'

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_register_for_resource_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    def register_for_new_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_resources()

    def register_for_changed_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resources()

    @raise_null_argument
    def register_for_changed_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resource(resource_id)

    def register_for_deleted_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resources()

    @raise_null_argument
    def register_for_deleted_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resource(resource_id)

    def reliable_resource_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_resource_notifications()

    def unreliable_resource_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_resource_notifications()

    @raise_null_argument
    def acknowledge_resource_notification(self, notification_id):
        raise Unimplemented()


class ResourceBinSession(abc_resource_sessions.ResourceBinSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceBinSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'resource.ResourceBin'

    def use_comparative_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bin_view()

    def use_plenary_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bin_view()

    def can_lookup_resource_bin_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    @raise_null_argument
    def get_resource_ids_by_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_ids_by_bin(bin_id)

    @raise_null_argument
    def get_resources_by_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resources_by_bin(bin_id)

    @raise_null_argument
    def get_resource_ids_by_bins(self, bin_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_ids_by_bins(bin_ids)

    @raise_null_argument
    def get_resources_by_bins(self, bin_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resources_by_bins(bin_ids)

    @raise_null_argument
    def get_bin_ids_by_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bin_ids_by_resource(resource_id)

    @raise_null_argument
    def get_bins_by_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bins_by_resource(resource_id)


class ResourceBinAssignmentSession(abc_resource_sessions.ResourceBinAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceBinAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'resource.ResourceBin'

    def can_assign_resources(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_resources_to_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    @raise_null_argument
    def get_assignable_bin_ids(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bin_ids(bin_id)

    @raise_null_argument
    def get_assignable_bin_ids_for_resource(self, bin_id, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bin_ids_for_resource(bin_id, resource_id)

    @raise_null_argument
    def assign_resource_to_bin(self, resource_id, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_resource_to_bin(resource_id, bin_id)

    @raise_null_argument
    def unassign_resource_from_bin(self, resource_id, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_resource_from_bin(resource_id, bin_id)


class ResourceSmartBinSession(abc_resource_sessions.ResourceSmartBinSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceSmartBinSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_manage_smart_bins(self):
        raise Unimplemented()

    def get_resource_query(self):
        raise Unimplemented()

    resource_query = property(fget=get_resource_query)

    def get_resource_search_order(self):
        raise Unimplemented()

    resource_search_order = property(fget=get_resource_search_order)

    @raise_null_argument
    def apply_resource_query(self, resource_query):
        raise Unimplemented()

    def inspect_resource_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_resource_sequencing(self, resource_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_query_from_inspector(self, resource_query_inspector):
        raise Unimplemented()


class MembershipSession(abc_resource_sessions.MembershipSession, osid_sessions.OsidSession):
    """Adapts underlying MembershipSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_query_membership(self):
        raise Unimplemented()

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    @raise_null_argument
    def is_member(self, member_resource_id, resource_id):
        raise Unimplemented()


class GroupSession(abc_resource_sessions.GroupSession, osid_sessions.OsidSession):
    """Adapts underlying GroupSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_lookup_resource_members(self):
        raise Unimplemented()

    def use_comparative_resource_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_resource_view()

    def use_plenary_resource_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_resource_view()

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    def use_federated_group_view(self):
        raise Unimplemented()

    def use_isolated_group_view(self):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_ids_by_group(self, group_resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_resources_by_group(self, group_resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_ids_by_groups(self, group_resource_ids):
        raise Unimplemented()

    @raise_null_argument
    def get_resources_by_groups(self, group_resource_ids):
        raise Unimplemented()

    @raise_null_argument
    def get_group_ids_by_resource(self, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_groups_by_resource(self, resource_id):
        raise Unimplemented()


class GroupAssignmentSession(abc_resource_sessions.GroupAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying GroupAssignmentSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_assign_resources(self):
        raise Unimplemented()

    @raise_null_argument
    def can_assign_resources_to_group(self, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def assign_resource_to_group(self, resource_id, resource_group_id):
        raise Unimplemented()

    @raise_null_argument
    def unassign_resource_from_group(self, resource_id, resource_group_id):
        raise Unimplemented()


class GroupNotificationSession(abc_resource_sessions.GroupNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying GroupNotificationSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_register_for_group_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    @raise_null_argument
    def register_for_new_members(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_members()

    @raise_null_argument
    def register_for_deleted_members(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_members(resource_id)

    def reliable_group_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_group_notifications()

    def unreliable_group_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_group_notifications()

    @raise_null_argument
    def acknowledge_group_notification(self, notification_id):
        raise Unimplemented()


class GroupHierarchySession(abc_resource_sessions.GroupHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying GroupHierarchySession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_access_group_hierarchy(self):
        raise Unimplemented()

    def use_comparative_resource_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_resource_view()

    def use_plenary_resource_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_resource_view()

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    @raise_null_argument
    def is_member_of_group(self, group_id, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_node_ids(self, resource_id, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_nodes(self, resource_id, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()


class ResourceAgentSession(abc_resource_sessions.ResourceAgentSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceAgentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.ResourceAgent'

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_lookup_resource_agent_mappings(self):
        return self._can('lookup')

    def use_comparative_agent_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_agent_view()

    def use_plenary_agent_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_agent_view()

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    @raise_null_argument
    def get_resource_id_by_agent(self, agent_id):
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_id_by_agent(agent_id)

    @raise_null_argument
    def get_resource_by_agent(self, agent_id):
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_by_agent(agent_id)

    @raise_null_argument
    def get_agent_ids_by_resource(self, resource_id):
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agent_ids_by_resource(resource_id)

    @raise_null_argument
    def get_agents_by_resource(self, resource_id):
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agents_by_resource(resource_id)


class ResourceAgentAssignmentSession(abc_resource_sessions.ResourceAgentAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceAgentAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.ResourceAgent'

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_assign_agents(self):
        return self._can('assign')

    @raise_null_argument
    def can_assign_agents_to_resource(self, resource_id):
        return False  # don't have enough information yet

    @raise_null_argument
    def assign_agent_to_resource(self, agent_id, resource_id):
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_agent_to_resource(agent_id, resource_id)

    @raise_null_argument
    def unassign_agent_from_resource(self, agent_id, resource_id):
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_agent_from_resource(agent_id, resource_id)


class ResourceRelationshipLookupSession(abc_resource_sessions.ResourceRelationshipLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.ResourceRelationship'
        self.use_federated_bin_view()
        self.use_comparative_resource_relationship_view()
        self._auth_bin_ids = None
        self._unauth_bin_ids = None
    #     self._overriding_bin_ids = None
    #
    # def _get_overriding_bin_ids(self):
    #     if self._overriding_bin_ids is None:
    #         self._overriding_bin_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_bin_ids

    def _try_overriding_bins(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_bin_id(catalog_id, match=True)
        return self._query_session.get_resource_relationships_by_query(query), query

    def _get_unauth_bin_ids(self, bin_id):
        if self._can('lookup', bin_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bin_id)]
        if self._hierarchy_session.has_child_bins(bin_id):
            for child_bin_id in self._hierarchy_session.get_child_bin_ids(bin_id):
                unauth_list = unauth_list + self._get_unauth_bin_ids(child_bin_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_bins(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bin_ids is None:
            self._unauth_bin_ids = self._get_unauth_bin_ids(self._qualifier_id)
        for bin_id in self._unauth_bin_ids:
            query.match_bin_id(bin_id, match=False)
        return self._query_session.get_resource_relationships_by_query(query)

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_lookup_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_resource_relationship_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_resource_relationship_view()

    def use_plenary_resource_relationship_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_resource_relationship_view()

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    def use_effective_resource_relationship_view(self):
        raise Unimplemented()

    def use_any_effective_resource_relationship_view(self):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationship(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationship(resource_relationship_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_id(resource_relationship_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_resource_relationships_by_ids(self, resource_relationship_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships_by_ids(resource_relationship_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        for resource_relationship_id in (resource_relationship_ids):
            query.match_id(resource_relationship_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resource_relationships_by_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships_by_genus_type(relationship_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_genus_type(relationship_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resource_relationships_by_parent_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships_by_parent_genus_type(relationship_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_parent_genus_type(relationship_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resource_relationships_by_record_type(self, relationship_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships_by_record_type(relationship_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_record_type(relationship_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resource_relationships_on_date(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_for_source_resource(self, source_resource_id):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships_for_source_resource(source_resource_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_source_id(source_resource_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resource_relationships_for_source_resource_on_date(self, source_resource_id, from_, to):
        """Pass through to provider ResourceRelationshipLookupSession.get_resource_relationships_for_source_resource_on_date"""
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships_for_source_resource_on_date(source_resource_id, from_, to)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_source_id(source_resource_id, match=True)
        query.match_date(from_, to, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_resource_relationships_by_genus_type_for_source_resource(self, source_resource_id, relationship_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_by_genus_type_for_source_resource_on_date(self, source_resource_id, relationship_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_for_destination_resource(self, destination_resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_for_destination_resource_on_date(self, source_resource_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_by_genus_type_for_destination_resource(self, destination_resource_id, relationship_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_by_genus_type_for_destination_resource_on_date(self, destination_resource_id, relationship_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_for_resources(self, source_resource_id, destination_resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_for_resources_on_date(self, source_resource_id, destination_resource_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_by_genus_type_for_resources(self, source_resource_id, destination_resource_id, relationship_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationships_by_genus_type_for_resources_on_date(self, source_resource_id, destination_resource_id, relationship_genus_type, from_, to):
        raise Unimplemented()

    def get_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_resource_relationships()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_resource_relationship_query()
        query.match_any(match=True)
        return self._try_harder(query)

    resource_relationships = property(fget=get_resource_relationships)


class ResourceRelationshipQuerySession(abc_resource_sessions.ResourceRelationshipQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.ResourceRelationship'
        self.use_federated_bin_view()
        self._unauth_bin_ids = None
        # self._overriding_bin_ids = None

    # def _get_overriding_bin_ids(self):
    #     if self._overriding_bin_ids is None:
    #         self._overriding_bin_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_bin_ids

    def _try_overriding_bins(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for bin_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_bin_id(bin_id, match=True)
        return self._query_session.get_resource_relationships_by_query(query), query

    def _get_unauth_bin_ids(self, bin_id):
        if self._can('search', bin_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bin_id)]
        if self._hierarchy_session.has_child_bins(bin_id):
            for child_bin_id in self._hierarchy_session.get_child_bin_ids(bin_id):
                unauth_list = unauth_list + self._get_unauth_bin_ids(child_bin_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_bins(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bin_ids is None:
            self._unauth_bin_ids = self._get_unauth_bin_ids(self._qualifier_id)
        for bin_id in self._unauth_bin_ids:
            query._provider_query.match_bin_id(bin_id, match=False)
        return self._query_session.get_resource_relationships_by_query(query)

    class ResourceRelationshipQueryWrapper(QueryWrapper):
        """Wrapper for ResourceRelationshipQueries to override match_bin_id method"""

        def match_bin_id(self, bin_id, match=True):
            self._cat_id_args_list.append({'bin_id': bin_id, 'match': match})

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_search_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    def get_resource_relationship_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.ResourceRelationshipQueryWrapper(self._provider_session.get_resource_relationship_query())

    resource_relationship_query = property(fget=get_resource_relationship_query)

    @raise_null_argument
    def get_resource_relationships_by_query(self, resource_relationship_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(resource_relationship_query, '_cat_id_args_list'):
            raise Unsupported('resource_relationship_query not from this session')
        for kwargs in resource_relationship_query._cat_id_args_list:
            if self._can('search', kwargs['bin_id']):
                resource_relationship_query._provider_query.match_bin_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_resource_relationships_by_query(resource_relationship_query)
        self._check_search_conditions()
        result = self._try_harder(resource_relationship_query)
        resource_relationship_query._provider_query.clear_bin_terms()
        return result


class ResourceRelationshipSearchSession(abc_resource_sessions.ResourceRelationshipSearchSession, ResourceRelationshipQuerySession):
    """Adapts underlying ResourceRelationshipSearchSession methodswith authorization checks."""

    def get_resource_relationship_search(self):
        """Pass through to provider ResourceRelationshipSearchSession.get_resource_relationship_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationship_search()

    resource_relationship_search = property(fget=get_resource_relationship_search)

    def get_resource_relationship_search_order(self):
        raise Unimplemented()

    resource_relationship_search_order = property(fget=get_resource_relationship_search_order)

    @raise_null_argument
    def get_resource_relationships_by_search(self, resource_relationship_query, resource_relationship_search):
        """Pass through to provider ResourceRelationshipSearchSession.get_resource_relationships_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationships_by_search(resource_relationship_query, resource_relationship_search)

    @raise_null_argument
    def get_resource_relationship_query_from_inspector(self, resource_relationship_query_inspector):
        raise Unimplemented()


class ResourceRelationshipAdminSession(abc_resource_sessions.ResourceRelationshipAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bin_id()
        self._id_namespace = 'resource.ResourceRelationship'
        self._overriding_bin_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_resource_relationship_bin_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_resource_relationship_bin_session()
                self.get_bin_ids_by_resource_relationship = self._object_catalog_session.get_bin_ids_by_resource_relationship
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bin_ids(self):
        if self._overriding_bin_ids is None:
            self._overriding_bin_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bin_ids

    def _can_for_resource_relationship(self, func_name, resource_relationship_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, resource_relationship_id, 'get_bin_ids_for_resource_relationship')

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_create_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_resource_relationship_with_record_types(self, resource_relationship_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if resource_relationship_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_resource_relationship_form_for_create(self, source_resource_id, destination_resource_id, resource_relationship_record_types):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationship_form_for_create(source_resource_id, destination_resource_id, resource_relationship_record_types)

    @raise_null_argument
    def create_resource_relationship(self, resource_relationship_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_resource_relationship(resource_relationship_form)

    def can_update_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_resource_relationship_form_for_update(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_resource_relationship('update', resource_relationship_id):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationship_form_for_update(resource_relationship_id)

    def duplicate_resource_relationship(self, resource_relationship_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_resource_relationship(resource_relationship_id)

    @raise_null_argument
    def update_resource_relationship(self, resource_relationship_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_resource_relationship(resource_relationship_form)

    def can_delete_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_resource_relationship(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_resource_relationship('delete', resource_relationship_id):
            raise PermissionDenied()
        return self._provider_session.delete_resource_relationship(resource_relationship_id)

    def can_manage_resource_relationship_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_resource_relationship(self, resource_relationship_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_resource_relationship('alias', resource_relationship_id):
            raise PermissionDenied()
        return self._provider_session.alias_resource_relationship(resource_relationship_id, alias_id)


class ResourceRelationshipNotificationSession(abc_resource_sessions.ResourceRelationshipNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipNotificationSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_register_for_resource_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bin_view()
        if self._query_session:
            self._query_session.use_federated_bin_view()

    def use_isolated_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bin_view()
        if self._query_session:
            self._query_session.use_isolated_bin_view()

    def register_for_new_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_resource_relationships()

    @raise_null_argument
    def register_for_new_resource_relationships_by_genus_type(self, resource_relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_resource_relationships_by_genus_type(resource_relationship_genus_type)

    @raise_null_argument
    def register_for_new_resource_relationships_for_source_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_resource_relationships_for_source_resource()

    @raise_null_argument
    def register_for_new_resource_relationships_for_destination_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_resource_relationships_for_destination_resource()

    def register_for_changed_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resource_relationships()

    @raise_null_argument
    def register_for_changed_resource_relationships_by_genus_type(self, resource_relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resource_relationships_by_genus_type(resource_relationship_genus_type)

    @raise_null_argument
    def register_for_changed_resource_relationships_for_source_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resource_relationships_for_source_resource(resource_id)

    @raise_null_argument
    def register_for_changed_resource_relationships_for_destination_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resource_relationships_for_destination_resource(resource_id)

    @raise_null_argument
    def register_for_changed_resource_relationship(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_resource_relationship(resource_relationship_id)

    def register_for_deleted_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resource_relationships()

    @raise_null_argument
    def register_for_deleted_resource_relationships_by_genus_type(self, resource_relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resource_relationships_by_genus_type(resource_relationship_genus_type)

    @raise_null_argument
    def register_for_deleted_resource_relationships_for_source_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resource_relationships_for_source_resource(resource_id)

    @raise_null_argument
    def register_for_deleted_resource_relationships_for_destination_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resource_relationships_for_destination_resource(resource_id)

    @raise_null_argument
    def register_for_deleted_resource_relationship(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_resource_relationship(resource_relationship_id)

    def reliable_resource_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_resource_relationship_notifications()

    def unreliable_resource_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_resource_relationship_notifications()

    @raise_null_argument
    def acknowledge_resource_relationship_notification(self, notification_id):
        raise Unimplemented()


class ResourceRelationshipBinSession(abc_resource_sessions.ResourceRelationshipBinSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipBinSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'resource.ResourceRelationshipBin'

    def use_comparative_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bin_view()

    def use_plenary_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bin_view()

    def can_lookup_resource_relationship_bin_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    @raise_null_argument
    def get_resource_relationship_ids_by_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationship_ids_by_bin(bin_id)

    @raise_null_argument
    def get_resource_relationships_by_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationships_by_bin(bin_id)

    @raise_null_argument
    def get_resource_relationships_ids_by_bins(self, bin_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationships_ids_by_bins(bin_ids)

    @raise_null_argument
    def get_resource_relationships_by_bins(self, bin_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_resource_relationships_by_bins(bin_ids)

    @raise_null_argument
    def get_bin_ids_by_resource_relationship(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bin_ids_by_resource_relationship(resource_relationship_id)

    @raise_null_argument
    def get_bins_by_resource_relationship(self, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bins_by_resource_relationship(resource_relationship_id)


class ResourceRelationshipBinAssignmentSession(abc_resource_sessions.ResourceRelationshipBinAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipBinAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'resource.ResourceRelationshipBin'

    def can_assign_resource_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_resource_relationships_to_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    @raise_null_argument
    def get_assignable_bin_ids(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bin_ids(bin_id)

    @raise_null_argument
    def get_assignable_bin_ids_for_resource_relationship(self, bin_id, resource_relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bin_ids_for_resource_relationship(bin_id, resource_relationship_id)

    @raise_null_argument
    def assign_resource_relationship_to_bin(self, resource_relationship_id, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_resource_relationship_to_bin(resource_relationship_id, bin_id)

    @raise_null_argument
    def unassign_resource_relationship_from_bin(self, resource_relationship_id, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_resource_relationship_from_bin(resource_relationship_id, bin_id)


class ResourceRelationshipSmartBinSession(abc_resource_sessions.ResourceRelationshipSmartBinSession, osid_sessions.OsidSession):
    """Adapts underlying ResourceRelationshipSmartBinSession methodswith authorization checks."""

    def get_bin_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bin()

    bin = property(fget=get_bin)

    def can_manage_smart_bins(self):
        raise Unimplemented()

    def get_resource_relationship_query(self):
        raise Unimplemented()

    resource_relationship_query = property(fget=get_resource_relationship_query)

    def get_resource_relationship_search_order(self):
        raise Unimplemented()

    resource_relationship_search_order = property(fget=get_resource_relationship_search_order)

    @raise_null_argument
    def apply_resource_relationship_query(self, resource_query):
        raise Unimplemented()

    def inspect_resource_relationship_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_resource_relationship_sequencing(self, resource_relationship_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_resource_relationship_query_from_inspector(self, resource_relationship_query_inspector):
        raise Unimplemented()


class BinLookupSession(abc_resource_sessions.BinLookupSession, osid_sessions.OsidSession):
    """Adapts underlying BinLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'resource.Bin'

    def can_lookup_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bin_view()

    def use_plenary_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bin_view()

    @raise_null_argument
    def get_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bin(bin_id)

    @raise_null_argument
    def get_bins_by_ids(self, bin_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bins_by_ids(bin_ids)

    @raise_null_argument
    def get_bins_by_genus_type(self, bin_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bins_by_genus_type(bin_genus_type)

    @raise_null_argument
    def get_bins_by_parent_genus_type(self, bin_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_bins_by_record_type(self, bin_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_bins_by_provider(self, resource_id):
        raise Unimplemented()

    def get_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bins()

    bins = property(fget=get_bins)


class BinQuerySession(abc_resource_sessions.BinQuerySession, osid_sessions.OsidSession):
    """Adapts underlying BinQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'resource.Bin'

    def can_search_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.can_search_bins_template
        return self._can('search')

    def get_bin_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_bin_query()

    bin_query = property(fget=get_bin_query)

    @raise_null_argument
    def get_bins_by_query(self, bin_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_bins_by_query(bin_query)


class BinSearchSession(abc_resource_sessions.BinSearchSession, BinQuerySession):
    """Adapts underlying BinSearchSession methodswith authorization checks."""

    def get_bin_search(self):
        raise Unimplemented()

    bin_search = property(fget=get_bin_search)

    def get_bin_search_order(self):
        raise Unimplemented()

    bin_search_order = property(fget=get_bin_search_order)

    @raise_null_argument
    def get_bins_by_search(self, bin_query, bin_search):
        raise Unimplemented()

    @raise_null_argument
    def get_bin_query_from_inspector(self, bin_query_inspector):
        raise Unimplemented()


class BinAdminSession(abc_resource_sessions.BinAdminSession, osid_sessions.OsidSession):
    """Adapts underlying BinAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'resource.Bin'

    def can_create_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_bin_with_record_types(self, bin_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if bin_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_bin_form_for_create(self, bin_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_bin_form_for_create(bin_record_types)

    @raise_null_argument
    def create_bin(self, bin_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_bin(bin_form)

    def can_update_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_bin_form_for_update(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_bin_form_for_update(bin_id)

    @raise_null_argument
    def update_bin(self, bin_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_bin(bin_form)

    def can_delete_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_bin(bin_id)

    def can_manage_bin_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_bin(self, bin_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_bin(bin_id, alias_id)


class BinNotificationSession(abc_resource_sessions.BinNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying BinNotificationSession methodswith authorization checks."""

    def can_register_for_bin_notifications(self):
        raise Unimplemented()

    def register_for_new_bins(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_new_bin_ancestors(self, bin_id):
        raise Unimplemented()

    @raise_null_argument
    def register_for_new_bin_descendants(self, bin_id):
        raise Unimplemented()

    def register_for_changed_bins(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_bin(self, bin_id):
        raise Unimplemented()

    def register_for_deleted_bins(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_bin(self, bin_id):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_bin_ancestors(self, bin_id):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_bin_descendants(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_bin_descendants(bin_id)

    def reliable_bin_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_bin_notifications()

    def unreliable_bin_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_bin_notifications()

    @raise_null_argument
    def acknowledge_bin_notification(self, notification_id):
        raise Unimplemented()


class BinHierarchySession(abc_resource_sessions.BinHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying BinHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'resource.Bin'

    def get_bin_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_bin_hierarchy_id()

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bin_hierarchy()

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bin_view()

    def use_plenary_bin_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bin_view()

    def get_root_bin_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_bin_ids()

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_bins()

    root_bins = property(fget=get_root_bins)

    @raise_null_argument
    def has_parent_bins(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_bins(bin_id)

    @raise_null_argument
    def is_parent_of_bin(self, id_, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_bin(id_, bin_id)

    @raise_null_argument
    def get_parent_bin_ids(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_bin_ids(bin_id)

    @raise_null_argument
    def get_parent_bins(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_bins(bin_id)

    @raise_null_argument
    def is_ancestor_of_bin(self, id_, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_bin(id_, bin_id)

    @raise_null_argument
    def has_child_bins(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_bins(bin_id)

    @raise_null_argument
    def is_child_of_bin(self, id_, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_bin(id_, bin_id)

    @raise_null_argument
    def get_child_bin_ids(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_bin_ids(bin_id)

    @raise_null_argument
    def get_child_bins(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_bins(bin_id)

    @raise_null_argument
    def is_descendant_of_bin(self, id_, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_bin(id_, bin_id)

    @raise_null_argument
    def get_bin_node_ids(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bin_node_ids(
            bin_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_bin_nodes(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bin_nodes(
            bin_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class BinHierarchyDesignSession(abc_resource_sessions.BinHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying BinHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'resource.Bin'
        # should this be 'resource.BinHierarchy' ?

    def get_bin_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_bin_hierarchy_id()

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bin_hierarchy()

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_modify_bin_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_bin(bin_id)

    @raise_null_argument
    def remove_root_bin(self, bin_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_bin(bin_id)

    @raise_null_argument
    def add_child_bin(self, bin_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_bin(bin_id, child_id)

    @raise_null_argument
    def remove_child_bin(self, bin_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_bin(bin_id, child_id)

    @raise_null_argument
    def remove_child_bins(self, bin_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_bins(bin_id)
