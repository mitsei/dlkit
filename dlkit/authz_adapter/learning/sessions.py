"""AuthZ Adapter implementations of learning sessions."""
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
from dlkit.abstract_osid.learning import sessions as abc_learning_sessions


class ObjectiveLookupSession(abc_learning_sessions.ObjectiveLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Objective'
        self.use_federated_objective_bank_view()
        self.use_comparative_objective_view()
        self._auth_objective_bank_ids = None
        self._unauth_objective_bank_ids = None
    #     self._overriding_objective_bank_ids = None
    #
    # def _get_overriding_objective_bank_ids(self):
    #     if self._overriding_objective_bank_ids is None:
    #         self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_objective_bank_ids

    def _try_overriding_objective_banks(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_objective_bank_id(catalog_id, match=True)
        return self._query_session.get_objectives_by_query(query), query

    def _get_unauth_objective_bank_ids(self, objective_bank_id):
        if self._can('lookup', objective_bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(objective_bank_id)]
        if self._hierarchy_session.has_child_objective_banks(objective_bank_id):
            for child_objective_bank_id in self._hierarchy_session.get_child_objective_bank_ids(objective_bank_id):
                unauth_list = unauth_list + self._get_unauth_objective_bank_ids(child_objective_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_objective_banks(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_objective_bank_ids is None:
            self._unauth_objective_bank_ids = self._get_unauth_objective_bank_ids(self._qualifier_id)
        for objective_bank_id in self._unauth_objective_bank_ids:
            query.match_objective_bank_id(objective_bank_id, match=False)
        return self._query_session.get_objectives_by_query(query)

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_objective_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_objective_view()

    def use_plenary_objective_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_objective_view()

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    @raise_null_argument
    def get_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_objective(objective_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_id(objective_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_objectives_by_ids(self, objective_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_objectives_by_ids(objective_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        for objective_id in (objective_ids):
            query.match_id(objective_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_objectives_by_genus_type(self, objective_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_objectives_by_genus_type(objective_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_genus_type(objective_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_objectives_by_parent_genus_type(self, objective_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_objectives_by_parent_genus_type(objective_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_parent_genus_type(objective_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_objectives_by_record_type(self, objective_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_objectives_by_record_type(objective_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_record_type(objective_record_type, match=True)
        return self._try_harder(query)

    def get_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_objectives()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_any(match=True)
        return self._try_harder(query)

    objectives = property(fget=get_objectives)


class ObjectiveQuerySession(abc_learning_sessions.ObjectiveQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Objective'
        self.use_federated_objective_bank_view()
        self._unauth_objective_bank_ids = None
        # self._overriding_objective_bank_ids = None

    # def _get_overriding_objective_bank_ids(self):
    #     if self._overriding_objective_bank_ids is None:
    #         self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_objective_bank_ids

    def _try_overriding_objective_banks(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for objective_bank_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_objective_bank_id(objective_bank_id, match=True)
        return self._query_session.get_objectives_by_query(query), query

    def _get_unauth_objective_bank_ids(self, objective_bank_id):
        if self._can('search', objective_bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(objective_bank_id)]
        if self._hierarchy_session.has_child_objective_banks(objective_bank_id):
            for child_objective_bank_id in self._hierarchy_session.get_child_objective_bank_ids(objective_bank_id):
                unauth_list = unauth_list + self._get_unauth_objective_bank_ids(child_objective_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_objective_banks(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_objective_bank_ids is None:
            self._unauth_objective_bank_ids = self._get_unauth_objective_bank_ids(self._qualifier_id)
        for objective_bank_id in self._unauth_objective_bank_ids:
            query._provider_query.match_objective_bank_id(objective_bank_id, match=False)
        return self._query_session.get_objectives_by_query(query)

    class ObjectiveQueryWrapper(QueryWrapper):
        """Wrapper for ObjectiveQueries to override match_objective_bank_id method"""

        def match_objective_bank_id(self, objective_bank_id, match=True):
            self._cat_id_args_list.append({'objective_bank_id': objective_bank_id, 'match': match})

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_search_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def get_objective_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.ObjectiveQueryWrapper(self._provider_session.get_objective_query())

    objective_query = property(fget=get_objective_query)

    @raise_null_argument
    def get_objectives_by_query(self, objective_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(objective_query, '_cat_id_args_list'):
            raise Unsupported('objective_query not from this session')
        for kwargs in objective_query._cat_id_args_list:
            if self._can('search', kwargs['objective_bank_id']):
                objective_query._provider_query.match_objective_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_objectives_by_query(objective_query)
        self._check_search_conditions()
        result = self._try_harder(objective_query)
        objective_query._provider_query.clear_objective_bank_terms()
        return result


class ObjectiveSearchSession(abc_learning_sessions.ObjectiveSearchSession, ObjectiveQuerySession):
    """Adapts underlying ObjectiveSearchSession methodswith authorization checks."""

    def get_objective_search(self):
        """Pass through to provider ObjectiveSearchSession.get_objective_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_objective_search()

    objective_search = property(fget=get_objective_search)

    def get_objective_search_order(self):
        raise Unimplemented()

    objective_search_order = property(fget=get_objective_search_order)

    @raise_null_argument
    def get_objectives_by_search(self, objective_query, objective_search):
        """Pass through to provider ObjectiveSearchSession.get_objectives_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_objectives_by_search(objective_query, objective_search)

    @raise_null_argument
    def get_objective_query_from_inspector(self, objective_query_inspector):
        raise Unimplemented()


class ObjectiveAdminSession(abc_learning_sessions.ObjectiveAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Objective'
        self._overriding_objective_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_objective_objective_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_objective_objective_bank_session()
                self.get_objective_bank_ids_by_objective = self._object_catalog_session.get_objective_bank_ids_by_objective
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_objective_bank_ids(self):
        if self._overriding_objective_bank_ids is None:
            self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_objective_bank_ids

    def _can_for_objective(self, func_name, objective_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, objective_id, 'get_objective_bank_ids_for_objective')

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_create_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_objective_with_record_types(self, objective_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if objective_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_objective_form_for_create(self, objective_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_objective_form_for_create(objective_record_types)

    @raise_null_argument
    def create_objective(self, objective_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_objective(objective_form)

    def can_update_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_objective_form_for_update(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_objective('update', objective_id):
            raise PermissionDenied()
        return self._provider_session.get_objective_form_for_update(objective_id)

    def duplicate_objective(self, objective_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_objective(objective_id)

    @raise_null_argument
    def update_objective(self, objective_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_objective(objective_form)

    def can_delete_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective_template
        if not self._can_for_objective('delete', objective_id):
            raise PermissionDenied()
        return self._provider_session.delete_objective(objective_id)

    def can_manage_objective_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_objective(self, objective_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_objective('alias', objective_id):
            raise PermissionDenied()
        return self._provider_session.alias_objective(objective_id, alias_id)


class ObjectiveNotificationSession(abc_learning_sessions.ObjectiveNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Objective'

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_register_for_objective_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def reliable_objective_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_objective_notifications()

    def unreliable_objective_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_objective_notifications()

    @raise_null_argument
    def acknowledge_objective_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_objectives()

    def register_for_changed_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objectives()

    @raise_null_argument
    def register_for_changed_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective(objective_id)

    def register_for_deleted_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_objectives()

    @raise_null_argument
    def register_for_deleted_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_objective(objective_id)

    def register_for_changed_objective_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective_hierarchy()

    @raise_null_argument
    def register_for_changed_objective_hierarchy_for_ancestors(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective_hierarchy_for_ancestors(objective_id)

    @raise_null_argument
    def register_for_changed_objective_hierarchy_for_descendants(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective_hierarchy_for_descendants(objective_id)

    def reliable_objective_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_objective_notifications()

    def unreliable_objective_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_objective_notifications()

    @raise_null_argument
    def acknowledge_objective_notification(self, notification_id):
        raise Unimplemented()


class ObjectiveHierarchySession(abc_learning_sessions.ObjectiveHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'

    def get_objective_hierarchy_id(self):
        raise Unimplemented()

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        raise Unimplemented()

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_access_objective_hierarchy(self):
        raise Unimplemented()

    def use_comparative_objective_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_objective_view()

    def use_plenary_objective_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_objective_view()

    def get_root_objective_ids(self):
        raise Unimplemented()

    root_objective_ids = property(fget=get_root_objective_ids)

    def get_root_objectives(self):
        # From azosid_templates/ontology.py::SubjectHierarchySession::get_root_subjects_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_root_objectives()

    root_objectives = property(fget=get_root_objectives)

    @raise_null_argument
    def has_parent_objectives(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def is_parent_of_objective(self, id_, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_parent_objective_ids(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_parent_objectives(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def is_ancestor_of_objective(self, id_, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def has_child_objectives(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def is_child_of_objective(self, id_, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_child_objective_ids(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_child_objectives(self, objective_id):
        # From azosid_templates/ontology.py::SubjectHierarchySession::get_child_subjects_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_child_objectives(objective_id)

    @raise_null_argument
    def is_descendant_of_objective(self, id_, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_objective_node_ids(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()

    @raise_null_argument
    def get_objective_nodes(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()


class ObjectiveHierarchyDesignSession(abc_learning_sessions.ObjectiveHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'
        # should this be 'learning.ObjectiveBankHierarchy' ?

    def get_objective_hierarchy_id(self):
        raise Unimplemented()

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        raise Unimplemented()

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_modify_objective_hierarchy(self):
        # From azosid_templates/ontology.py::SubjectHierarchyDesignSession::can_modify_subject_hierarchy_template
        return self._can('modify')

    @raise_null_argument
    def add_root_objective(self, objective_id):
        # From azosid_templates/ontology.py::SubjectHierarchyDesignSession::add_root_subject_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_objective(objective_id)

    @raise_null_argument
    def remove_root_objective(self, objective_id):
        # From azosid_templates/ontology.py::SubjectHierarchyDesignSession::remove_root_subject_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_objective(objective_id)

    @raise_null_argument
    def add_child_objective(self, objective_id, child_id):
        # From azosid_templates/ontology.py::SubjectHierarchyDesignSession::add_child_subject_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_objective(objective_id, child_id)

    @raise_null_argument
    def remove_child_objective(self, objective_id, child_id):
        # From azosid_templates/ontology.py::SubjectHierarchyDesignSession::remove_child_subject_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_objective(objective_id, child_id)

    @raise_null_argument
    def remove_child_objectives(self, objective_id):
        # From azosid_templates/ontology.py::SubjectHierarchyDesignSession::remove_child_subjects_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_objectives(objective_id)


class ObjectiveSequencingSession(abc_learning_sessions.ObjectiveSequencingSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveSequencingSession methodswith authorization checks."""

    def get_objective_hierarchy_id(self):
        raise Unimplemented()

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        raise Unimplemented()

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_sequence_objectives(self):
        raise Unimplemented()

    @raise_null_argument
    def move_objective_ahead(self, parent_objective_id, reference_objective_id, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def move_objective_behind(self, parent_objective_id, reference_objective_id, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def sequence_objectives(self, parent_objective_id, objective_ids):
        raise Unimplemented()


class ObjectiveObjectiveBankSession(abc_learning_sessions.ObjectiveObjectiveBankSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveObjectiveBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'learning.ObjectiveObjectiveBank'

    def can_lookup_objective_objective_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_objective_bank_view()

    def use_plenary_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_objective_bank_view()

    @raise_null_argument
    def get_objective_ids_by_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_ids_by_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_objectives_by_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objectives_by_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_objective_ids_by_objective_banks(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_ids_by_objective_banks(objective_bank_ids)

    @raise_null_argument
    def get_objectives_by_objective_banks(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objectives_by_objective_banks(objective_bank_ids)

    @raise_null_argument
    def get_objective_bank_ids_by_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_ids_by_objective(objective_id)

    @raise_null_argument
    def get_objective_banks_by_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks_by_objective(objective_id)


class ObjectiveObjectiveBankAssignmentSession(abc_learning_sessions.ObjectiveObjectiveBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveObjectiveBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'learning.ObjectiveObjectiveBank'

    def can_assign_objectives(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_objectives_to_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=objective_bank_id)

    @raise_null_argument
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_objective_bank_ids(objective_bank_id)

    @raise_null_argument
    def get_assignable_objective_bank_ids_for_objective(self, objective_bank_id, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_objective_bank_ids_for_objective(objective_bank_id, objective_id)

    @raise_null_argument
    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_objective_to_objective_bank(objective_id, objective_bank_id)

    @raise_null_argument
    def unassign_objective_from_objective_bank(self, objective_id, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_objective_from_objective_bank(objective_id, objective_bank_id)

    @raise_null_argument
    def reassign_proficiency_to_objective_bank(self, objective_id, from_objective_bank_id, to_objective_bank_id):
        raise Unimplemented()


class ObjectiveSmartObjectiveBankSession(abc_learning_sessions.ObjectiveSmartObjectiveBankSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveSmartObjectiveBankSession methodswith authorization checks."""

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_manage_smart_objective_banks(self):
        raise Unimplemented()

    def get_objective_query(self):
        raise Unimplemented()

    objective_query = property(fget=get_objective_query)

    def get_objective_search_order(self):
        raise Unimplemented()

    objective_search_order = property(fget=get_objective_search_order)

    @raise_null_argument
    def apply_objective_query(self, objective_query):
        raise Unimplemented()

    def inspect_objective_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_objective_sequencing(self, objective_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_objective_query_from_inspector(self, objective_query_inspector):
        raise Unimplemented()


class ObjectiveRequisiteSession(abc_learning_sessions.ObjectiveRequisiteSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveRequisiteSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Objective'
        self._auth_objective_bank_ids = None
        self._unauth_objective_bank_ids = None

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objective_prerequisites(self):
        raise Unimplemented()

    def use_comparative_objective_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_objective_view()

    def use_plenary_objective_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_objective_view()

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    @raise_null_argument
    def get_requisite_objectives(self, objective_id):
        if self._can('lookup'):
            return self._provider_session.get_requisite_objectives(objective_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_requisite_objective_id(objective_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_all_requisite_objectives(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_dependent_objectives(self, objective_id):
        if self._can('lookup'):
            return self._provider_session.get_dependent_objectives(objective_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_objective_query()
        query.match_dependent_objective_id(objective_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def is_objective_required(self, objective_id, required_objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_equivalent_objectives(self, objective_id):
        raise Unimplemented()


class ObjectiveRequisiteAssignmentSession(abc_learning_sessions.ObjectiveRequisiteAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveRequisiteAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Objective'
        self._auth_objective_bank_ids = None
        self._unauth_objective_bank_ids = None

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_assign_requisites(self):
        raise Unimplemented()

    @raise_null_argument
    def assign_objective_requisite(self, objective_id, requisite_objective_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.assign_objective_requisite(objective_id, requisite_objective_id)

    @raise_null_argument
    def unassign_objective_requisite(self, objective_id, requisite_objective_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.unassign_objective_requisite(objective_id, requisite_objective_id)

    @raise_null_argument
    def assign_equivalent_objective(self, objective_id, equivalent_objective_id):
        raise Unimplemented()

    @raise_null_argument
    def unassign_equivalent_objective(self, objective_id, equivalent_objective_id):
        raise Unimplemented()


class ActivityLookupSession(abc_learning_sessions.ActivityLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ActivityLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Activity'
        self.use_federated_objective_bank_view()
        self.use_comparative_activity_view()
        self._auth_objective_bank_ids = None
        self._unauth_objective_bank_ids = None
    #     self._overriding_objective_bank_ids = None
    #
    # def _get_overriding_objective_bank_ids(self):
    #     if self._overriding_objective_bank_ids is None:
    #         self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_objective_bank_ids

    def _try_overriding_objective_banks(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_objective_bank_id(catalog_id, match=True)
        return self._query_session.get_activities_by_query(query), query

    def _get_unauth_objective_bank_ids(self, objective_bank_id):
        if self._can('lookup', objective_bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(objective_bank_id)]
        if self._hierarchy_session.has_child_objective_banks(objective_bank_id):
            for child_objective_bank_id in self._hierarchy_session.get_child_objective_bank_ids(objective_bank_id):
                unauth_list = unauth_list + self._get_unauth_objective_bank_ids(child_objective_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_objective_banks(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_objective_bank_ids is None:
            self._unauth_objective_bank_ids = self._get_unauth_objective_bank_ids(self._qualifier_id)
        for objective_bank_id in self._unauth_objective_bank_ids:
            query.match_objective_bank_id(objective_bank_id, match=False)
        return self._query_session.get_activities_by_query(query)

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_activity_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_activity_view()

    def use_plenary_activity_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_activity_view()

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    @raise_null_argument
    def get_activity(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_activity(activity_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        query.match_id(activity_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_activities_by_ids(self, activity_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_activities_by_ids(activity_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        for activity_id in (activity_ids):
            query.match_id(activity_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_activities_by_genus_type(self, activity_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_activities_by_genus_type(activity_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        query.match_genus_type(activity_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_activities_by_parent_genus_type(self, activity_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_activities_by_parent_genus_type(activity_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        query.match_parent_genus_type(activity_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_activities_by_record_type(self, activity_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_activities_by_record_type(activity_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        query.match_record_type(activity_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_activities_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_activities_for_objective(objective_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        query.match_objective_id(objective_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_activities_for_objectives(self, objective_ids):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objectives_template
        if self._can('lookup'):
            return self._provider_session.get_activities_for_objectives(objective_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        for activity_id in (objective_ids):
            query.match_objective_id(activity_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_activities_by_asset(self, asset_id):
        raise Unimplemented()

    @raise_null_argument
    def get_activities_by_assets(self, asset_ids):
        raise Unimplemented()

    def get_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_activities()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_activity_query()
        query.match_any(match=True)
        return self._try_harder(query)

    activities = property(fget=get_activities)


class ActivityQuerySession(abc_learning_sessions.ActivityQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ActivityQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Activity'
        self.use_federated_objective_bank_view()
        self._unauth_objective_bank_ids = None
        # self._overriding_objective_bank_ids = None

    # def _get_overriding_objective_bank_ids(self):
    #     if self._overriding_objective_bank_ids is None:
    #         self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_objective_bank_ids

    def _try_overriding_objective_banks(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for objective_bank_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_objective_bank_id(objective_bank_id, match=True)
        return self._query_session.get_activities_by_query(query), query

    def _get_unauth_objective_bank_ids(self, objective_bank_id):
        if self._can('search', objective_bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(objective_bank_id)]
        if self._hierarchy_session.has_child_objective_banks(objective_bank_id):
            for child_objective_bank_id in self._hierarchy_session.get_child_objective_bank_ids(objective_bank_id):
                unauth_list = unauth_list + self._get_unauth_objective_bank_ids(child_objective_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_objective_banks(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_objective_bank_ids is None:
            self._unauth_objective_bank_ids = self._get_unauth_objective_bank_ids(self._qualifier_id)
        for objective_bank_id in self._unauth_objective_bank_ids:
            query._provider_query.match_objective_bank_id(objective_bank_id, match=False)
        return self._query_session.get_activities_by_query(query)

    class ActivityQueryWrapper(QueryWrapper):
        """Wrapper for ActivityQueries to override match_objective_bank_id method"""

        def match_objective_bank_id(self, objective_bank_id, match=True):
            self._cat_id_args_list.append({'objective_bank_id': objective_bank_id, 'match': match})

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_search_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def get_activity_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.ActivityQueryWrapper(self._provider_session.get_activity_query())

    activity_query = property(fget=get_activity_query)

    @raise_null_argument
    def get_activities_by_query(self, activity_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(activity_query, '_cat_id_args_list'):
            raise Unsupported('activity_query not from this session')
        for kwargs in activity_query._cat_id_args_list:
            if self._can('search', kwargs['objective_bank_id']):
                activity_query._provider_query.match_objective_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_activities_by_query(activity_query)
        self._check_search_conditions()
        result = self._try_harder(activity_query)
        activity_query._provider_query.clear_objective_bank_terms()
        return result


class ActivitySearchSession(abc_learning_sessions.ActivitySearchSession, ActivityQuerySession):
    """Adapts underlying ActivitySearchSession methodswith authorization checks."""

    def get_activity_search(self):
        """Pass through to provider ActivitySearchSession.get_activity_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_activity_search()

    activity_search = property(fget=get_activity_search)

    def get_activity_search_order(self):
        raise Unimplemented()

    activity_search_order = property(fget=get_activity_search_order)

    @raise_null_argument
    def get_activities_by_search(self, activity_query, activitiesearch):
        """Pass through to provider ActivitySearchSession.get_activities_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_activities_by_search(activity_query, activitiesearch)

    @raise_null_argument
    def get_activity_query_from_inspector(self, activity_query_inspector):
        raise Unimplemented()


class ActivityAdminSession(abc_learning_sessions.ActivityAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ActivityAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Activity'
        self._overriding_objective_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_activity_objective_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_activity_objective_bank_session()
                self.get_objective_bank_ids_by_activity = self._object_catalog_session.get_objective_bank_ids_by_activity
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_objective_bank_ids(self):
        if self._overriding_objective_bank_ids is None:
            self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_objective_bank_ids

    def _can_for_activity(self, func_name, activity_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, activity_id, 'get_objective_bank_ids_for_activity')

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_create_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_activity_with_record_types(self, activity_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if activity_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_activity_form_for_create(self, objective_id, activity_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_activity_form_for_create(objective_id, activity_record_types)

    @raise_null_argument
    def create_activity(self, activity_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_activity(activity_form)

    def can_update_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_activity_form_for_update(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_activity('update', activity_id):
            raise PermissionDenied()
        return self._provider_session.get_activity_form_for_update(activity_id)

    def duplicate_activity(self, activity_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_activity(activity_id)

    @raise_null_argument
    def update_activity(self, activity_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_activity(activity_form)

    def can_delete_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_activity(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_activity('delete', activity_id):
            raise PermissionDenied()
        return self._provider_session.delete_activity(activity_id)

    def can_manage_activity_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_activity(self, activity_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_activity('alias', activity_id):
            raise PermissionDenied()
        return self._provider_session.alias_activity(activity_id, alias_id)


class ActivityNotificationSession(abc_learning_sessions.ActivityNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ActivityNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Activity'

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_register_for_activity_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def reliable_activity_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_activity_notifications()

    def unreliable_activity_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_activity_notifications()

    @raise_null_argument
    def acknowledge_activity_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_activities()

    @raise_null_argument
    def register_for_new_activities_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_activities_for_objective()

    def register_for_changed_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_activities()

    @raise_null_argument
    def register_for_changed_activities_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_activities_for_objective(objective_id)

    @raise_null_argument
    def register_for_changed_activity(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_activity(activity_id)

    def register_for_deleted_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_activities()

    @raise_null_argument
    def register_for_deleted_activities_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_activities_for_objective(objective_id)

    @raise_null_argument
    def register_for_deleted_activity(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_activity(activity_id)

    def reliable_activity_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_activity_notifications()

    def unreliable_activity_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_activity_notifications()

    @raise_null_argument
    def acknowledge_activity_notification(self, notification_id):
        raise Unimplemented()


class ActivityObjectiveBankSession(abc_learning_sessions.ActivityObjectiveBankSession, osid_sessions.OsidSession):
    """Adapts underlying ActivityObjectiveBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'learning.ActivityObjectiveBank'

    def can_lookup_activity_objective_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_objective_bank_view()

    def use_plenary_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_objective_bank_view()

    @raise_null_argument
    def get_activity_ids_by_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_activity_ids_by_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_activities_by_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_activities_by_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_activity_ids_by_objective_banks(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_activity_ids_by_objective_banks(objective_bank_ids)

    @raise_null_argument
    def get_activities_by_objective_banks(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_activities_by_objective_banks(objective_bank_ids)

    @raise_null_argument
    def get_objective_bank_ids_by_activity(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_ids_by_activity(activity_id)

    @raise_null_argument
    def get_objective_banks_by_activity(self, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks_by_activity(activity_id)


class ActivityObjectiveBankAssignmentSession(abc_learning_sessions.ActivityObjectiveBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ActivityObjectiveBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'learning.ActivityObjectiveBank'

    def can_assign_activities(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_activities_to_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=objective_bank_id)

    @raise_null_argument
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_objective_bank_ids(objective_bank_id)

    @raise_null_argument
    def get_assignable_objective_bank_ids_for_activity(self, objective_bank_id, activity_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_objective_bank_ids_for_activity(objective_bank_id, activity_id)

    @raise_null_argument
    def assign_activity_to_objective_bank(self, activity_id, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_activity_to_objective_bank(activity_id, objective_bank_id)

    @raise_null_argument
    def unassign_activity_from_objective_bank(self, activity_id, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_activity_from_objective_bank(activity_id, objective_bank_id)

    @raise_null_argument
    def reassign_activity_to_objective_bank(self, activity_id, from_objective_bank_id, to_objective_bank_id):
        raise Unimplemented()


class ActivitySmartObjectiveBankSession(abc_learning_sessions.ActivitySmartObjectiveBankSession, osid_sessions.OsidSession):
    """Adapts underlying ActivitySmartObjectiveBankSession methodswith authorization checks."""

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_manage_smart_objective_banks(self):
        raise Unimplemented()

    def get_activity_query(self):
        raise Unimplemented()

    activity_query = property(fget=get_activity_query)

    def get_activity_search_order(self):
        raise Unimplemented()

    activity_search_order = property(fget=get_activity_search_order)

    @raise_null_argument
    def apply_activity_query(self, activity_query):
        raise Unimplemented()

    def inspect_activity_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_activity_sequencing(self, activity_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_activity_query_from_inspector(self, activity_query_inspector):
        raise Unimplemented()


class ProficiencyLookupSession(abc_learning_sessions.ProficiencyLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencyLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Proficiency'
        self.use_federated_objective_bank_view()
        self.use_comparative_proficiency_view()
        self._auth_objective_bank_ids = None
        self._unauth_objective_bank_ids = None
    #     self._overriding_objective_bank_ids = None
    #
    # def _get_overriding_objective_bank_ids(self):
    #     if self._overriding_objective_bank_ids is None:
    #         self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_objective_bank_ids

    def _try_overriding_objective_banks(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_objective_bank_id(catalog_id, match=True)
        return self._query_session.get_proficiencies_by_query(query), query

    def _get_unauth_objective_bank_ids(self, objective_bank_id):
        if self._can('lookup', objective_bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(objective_bank_id)]
        if self._hierarchy_session.has_child_objective_banks(objective_bank_id):
            for child_objective_bank_id in self._hierarchy_session.get_child_objective_bank_ids(objective_bank_id):
                unauth_list = unauth_list + self._get_unauth_objective_bank_ids(child_objective_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_objective_banks(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_objective_bank_ids is None:
            self._unauth_objective_bank_ids = self._get_unauth_objective_bank_ids(self._qualifier_id)
        for objective_bank_id in self._unauth_objective_bank_ids:
            query.match_objective_bank_id(objective_bank_id, match=False)
        return self._query_session.get_proficiencies_by_query(query)

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_proficiency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_proficiency_view()

    def use_plenary_proficiency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_proficiency_view()

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def use_effective_proficiency_view(self):
        raise Unimplemented()

    def use_any_effective_proficiency_view(self):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiency(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_proficiency(proficiency_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_id(proficiency_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_proficiencies_by_ids(self, proficiency_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_by_ids(proficiency_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        for proficiency_id in (proficiency_ids):
            query.match_id(proficiency_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_by_genus_type(self, proficiency_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_by_genus_type(proficiency_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_genus_type(proficiency_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_by_parent_genus_type(self, proficiency_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_by_parent_genus_type(proficiency_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_parent_genus_type(proficiency_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_by_record_type(self, proficiency_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_by_record_type(proficiency_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_record_type(proficiency_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_on_date(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_by_genus_type_on_date(self, proficiency_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_for_objective(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_for_objective_on_date(self, objective_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_by_genus_type_for_objective(self, objective_id, proficiency_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_by_genus_type_for_objective_on_date(self, objective_id, proficiency_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_for_objectives(self, objective_ids):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_for_resource(resource_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_source_id(resource_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_for_resource_on_date(self, resource_id, from_, to):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resource_on_date"""
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_for_resource_on_date(resource_id, from_, to)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_source_id(resource_id, match=True)
        query.match_date(from_, to, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_by_genus_type_for_resource(self, resource_id, proficiency_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_by_genus_type_for_resource_on_date(self, resource_id, proficiency_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_for_resources(self, resource_ids):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies_for_resources(resource_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_source_id(resource_ids, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_proficiencies_for_objective_and_resource(self, objective_id, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_for_objective_and_resource_on_date(self, objective_id, resource_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_by_genus_type_for_objective_and_resource(self, objective_id, resource_id, proficiency_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self, objective_id, resource_id, proficiency_genus_type, from_, to):
        raise Unimplemented()

    def get_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_proficiencies()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_proficiency_query()
        query.match_any(match=True)
        return self._try_harder(query)

    proficiencies = property(fget=get_proficiencies)


class ProficiencyQuerySession(abc_learning_sessions.ProficiencyQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencyQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Proficiency'
        self.use_federated_objective_bank_view()
        self._unauth_objective_bank_ids = None
        # self._overriding_objective_bank_ids = None

    # def _get_overriding_objective_bank_ids(self):
    #     if self._overriding_objective_bank_ids is None:
    #         self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_objective_bank_ids

    def _try_overriding_objective_banks(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for objective_bank_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_objective_bank_id(objective_bank_id, match=True)
        return self._query_session.get_proficiencies_by_query(query), query

    def _get_unauth_objective_bank_ids(self, objective_bank_id):
        if self._can('search', objective_bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(objective_bank_id)]
        if self._hierarchy_session.has_child_objective_banks(objective_bank_id):
            for child_objective_bank_id in self._hierarchy_session.get_child_objective_bank_ids(objective_bank_id):
                unauth_list = unauth_list + self._get_unauth_objective_bank_ids(child_objective_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_objective_banks(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_objective_bank_ids is None:
            self._unauth_objective_bank_ids = self._get_unauth_objective_bank_ids(self._qualifier_id)
        for objective_bank_id in self._unauth_objective_bank_ids:
            query._provider_query.match_objective_bank_id(objective_bank_id, match=False)
        return self._query_session.get_proficiencies_by_query(query)

    class ProficiencyQueryWrapper(QueryWrapper):
        """Wrapper for ProficiencyQueries to override match_objective_bank_id method"""

        def match_objective_bank_id(self, objective_bank_id, match=True):
            self._cat_id_args_list.append({'objective_bank_id': objective_bank_id, 'match': match})

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_search_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def get_proficiency_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.ProficiencyQueryWrapper(self._provider_session.get_proficiency_query())

    proficiency_query = property(fget=get_proficiency_query)

    @raise_null_argument
    def get_proficiencies_by_query(self, proficiency_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(proficiency_query, '_cat_id_args_list'):
            raise Unsupported('proficiency_query not from this session')
        for kwargs in proficiency_query._cat_id_args_list:
            if self._can('search', kwargs['objective_bank_id']):
                proficiency_query._provider_query.match_objective_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_proficiencies_by_query(proficiency_query)
        self._check_search_conditions()
        result = self._try_harder(proficiency_query)
        proficiency_query._provider_query.clear_objective_bank_terms()
        return result


class ProficiencySearchSession(abc_learning_sessions.ProficiencySearchSession, ProficiencyQuerySession):
    """Adapts underlying ProficiencySearchSession methodswith authorization checks."""

    def get_proficiency_search(self):
        """Pass through to provider ProficiencySearchSession.get_proficiency_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_proficiency_search()

    proficiency_search = property(fget=get_proficiency_search)

    def get_proficiency_search_order(self):
        raise Unimplemented()

    proficiency_search_order = property(fget=get_proficiency_search_order)

    @raise_null_argument
    def get_proficiencies_by_search(self, proficiency_query, proficiency_search):
        """Pass through to provider ProficiencySearchSession.get_proficiencies_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_proficiencies_by_search(proficiency_query, proficiency_search)

    @raise_null_argument
    def get_proficiency_query_from_inspector(self, proficiency_query_inspector):
        raise Unimplemented()


class ProficiencyAdminSession(abc_learning_sessions.ProficiencyAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencyAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_objective_bank_id()
        self._id_namespace = 'learning.Proficiency'
        self._overriding_objective_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_proficiency_objective_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_proficiency_objective_bank_session()
                self.get_objective_bank_ids_by_proficiency = self._object_catalog_session.get_objective_bank_ids_by_proficiency
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_objective_bank_ids(self):
        if self._overriding_objective_bank_ids is None:
            self._overriding_objective_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_objective_bank_ids

    def _can_for_proficiency(self, func_name, proficiency_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, proficiency_id, 'get_objective_bank_ids_for_proficiency')

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_create_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_proficiency_with_record_types(self, proficiency_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if proficiency_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_proficiency_form_for_create(self, objective_id, resource_id, proficiency_record_types):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_proficiency_form_for_create(objective_id, resource_id, proficiency_record_types)

    @raise_null_argument
    def create_proficiency(self, proficiency_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_proficiency(proficiency_form)

    def can_update_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_proficiency_form_for_update(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_proficiency('update', proficiency_id):
            raise PermissionDenied()
        return self._provider_session.get_proficiency_form_for_update(proficiency_id)

    def duplicate_proficiency(self, proficiency_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_proficiency(proficiency_id)

    @raise_null_argument
    def update_proficiency(self, proficiency_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_proficiency(proficiency_form)

    def can_delete_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_proficiency(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_proficiency('delete', proficiency_id):
            raise PermissionDenied()
        return self._provider_session.delete_proficiency(proficiency_id)

    def delete_proficiencies(self):
        raise Unimplemented()

    def can_manage_proficiency_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_proficiency(self, proficiency_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_proficiency('alias', proficiency_id):
            raise PermissionDenied()
        return self._provider_session.alias_proficiency(proficiency_id, alias_id)


class ProficiencyNotificationSession(abc_learning_sessions.ProficiencyNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencyNotificationSession methodswith authorization checks."""

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_register_for_proficiency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    def reliable_proficiency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_proficiency_notifications()

    def unreliable_proficiency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_proficiency_notifications()

    @raise_null_argument
    def acknowledge_proficiency_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_proficiencies()

    @raise_null_argument
    def register_for_new_proficiencies_by_genus_type(self, proficiency_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_proficiencies_by_genus_type(proficiency_genus_type)

    @raise_null_argument
    def register_for_new_proficiencies_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_proficiencies_for_objective()

    @raise_null_argument
    def register_for_new_proficiencies_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_proficiencies_for_resource()

    def register_for_changed_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_proficiencies()

    @raise_null_argument
    def register_for_changed_proficiencies_by_genus_type(self, proficiency_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_proficiencies_by_genus_type(proficiency_genus_type)

    @raise_null_argument
    def register_for_changed_proficiencies_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_proficiencies_for_objective(objective_id)

    @raise_null_argument
    def register_for_changed_proficiencies_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_proficiencies_for_resource(resource_id)

    @raise_null_argument
    def register_for_changed_proficiency(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_proficiency(proficiency_id)

    def register_for_deleted_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_proficiencies()

    @raise_null_argument
    def register_for_deleted_proficiencies_by_genus_type(self, proficiency_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_proficiencies_by_genus_type(proficiency_genus_type)

    @raise_null_argument
    def register_for_deleted_proficiencies_for_objective(self, objective_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_proficiencies_for_objective(objective_id)

    @raise_null_argument
    def register_for_deleted_proficiencies_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_proficiencies_for_resource(resource_id)

    @raise_null_argument
    def register_for_deleted_proficiency(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_proficiency(proficiency_id)

    def reliable_proficiency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_proficiency_notifications()

    def unreliable_proficiency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_proficiency_notifications()

    @raise_null_argument
    def acknowledge_proficiency_notification(self, notification_id):
        raise Unimplemented()


class ProficiencyObjectiveBankSession(abc_learning_sessions.ProficiencyObjectiveBankSession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencyObjectiveBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'learning.ProficiencyObjectiveBank'

    def can_lookup_proficiency_objective_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_proficiency_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_proficiency_objective_bank_view()

    def use_plenary_proficiency_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_proficiency_objective_bank_view()

    @raise_null_argument
    def get_proficiency_ids_by_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_proficiency_ids_by_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_proficiencies_by_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_proficiencies_by_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_proficiency_ids_by_objective_banks(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_proficiency_ids_by_objective_banks(objective_bank_ids)

    @raise_null_argument
    def get_proficiencies_by_objective_banks(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_proficiencies_by_objective_banks(objective_bank_ids)

    @raise_null_argument
    def get_objective_bank_ids_by_proficiency(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_ids_by_proficiency(proficiency_id)

    @raise_null_argument
    def get_objective_banks_by_proficiency(self, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks_by_proficiency(proficiency_id)


class ProficiencyObjectiveBankAssignmentSession(abc_learning_sessions.ProficiencyObjectiveBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencyObjectiveBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'learning.ProficiencyObjectiveBank'

    def can_assign_proficiencies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_proficiencies_to_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=objective_bank_id)

    @raise_null_argument
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_objective_bank_ids(objective_bank_id)

    @raise_null_argument
    def get_assignable_objective_bank_ids_for_proficiency(self, objective_bank_id, proficiency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_objective_bank_ids_for_proficiency(objective_bank_id, proficiency_id)

    @raise_null_argument
    def assign_proficiency_to_objective_bank(self, proficiency_id, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_proficiency_to_objective_bank(proficiency_id, objective_bank_id)

    @raise_null_argument
    def unassign_proficiency_from_objective_bank(self, proficiency_id, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_proficiency_from_objective_bank(proficiency_id, objective_bank_id)

    @raise_null_argument
    def reassign_proficiency_to_objective_bank(self, proficiency_id, from_objective_bank_id, to_objective_bank_id):
        raise Unimplemented()


class ProficiencySmartObjectiveBankSession(abc_learning_sessions.ProficiencySmartObjectiveBankSession, osid_sessions.OsidSession):
    """Adapts underlying ProficiencySmartObjectiveBankSession methodswith authorization checks."""

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_manage_smart_objective_banks(self):
        raise Unimplemented()

    def get_proficiency_query(self):
        raise Unimplemented()

    proficiency_query = property(fget=get_proficiency_query)

    def get_proficiency_search_order(self):
        raise Unimplemented()

    proficiency_search_order = property(fget=get_proficiency_search_order)

    @raise_null_argument
    def apply_proficiency_query(self, proficiency_query):
        raise Unimplemented()

    def inspect_proficiency_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_proficiency_sequencing(self, proficiency_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_proficiency_query_from_inspector(self, proficiency_query_inspector):
        raise Unimplemented()


class MyLearningPathSession(abc_learning_sessions.MyLearningPathSession, osid_sessions.OsidSession):
    """Adapts underlying MyLearningPathSession methodswith authorization checks."""

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_learning_paths(self):
        raise Unimplemented()

    def use_comparative_proficiency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_proficiency_view()

    def use_plenary_proficiency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_proficiency_view()

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    @raise_null_argument
    def find_path(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def find_path_at_proficiency(self, objective_id, grade_id):
        raise Unimplemented()

    @raise_null_argument
    def get_objectives_by_completion(self, objective_id, completion):
        raise Unimplemented()


class LearningPathSession(abc_learning_sessions.LearningPathSession, osid_sessions.OsidSession):
    """Adapts underlying LearningPathSession methodswith authorization checks."""

    def get_objective_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_objective_bank()

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_learning_paths(self):
        raise Unimplemented()

    def use_comparative_proficiency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_proficiency_view()

    def use_plenary_proficiency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_proficiency_view()

    def use_federated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_objective_bank_view()
        if self._query_session:
            self._query_session.use_federated_objective_bank_view()

    def use_isolated_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_objective_bank_view()
        if self._query_session:
            self._query_session.use_isolated_objective_bank_view()

    @raise_null_argument
    def find_path_for_resource(self, objective_id, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def find_path_for_resource_at_proficiency(self, objective_id, resource_id, grade_id):
        raise Unimplemented()

    @raise_null_argument
    def get_objectives_for_resource_by_completion(self, objective_id, resource_id, completion):
        raise Unimplemented()


class ObjectiveBankLookupSession(abc_learning_sessions.ObjectiveBankLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveBankLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'

    def can_lookup_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_objective_bank_view()

    def use_plenary_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_objective_bank_view()

    @raise_null_argument
    def get_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank(objective_bank_id)

    @raise_null_argument
    def get_objective_banks_by_ids(self, objective_bank_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks_by_ids(objective_bank_ids)

    @raise_null_argument
    def get_objective_banks_by_genus_type(self, objective_bank_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks_by_genus_type(objective_bank_genus_type)

    @raise_null_argument
    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_objective_banks_by_record_type(self, objective_bank_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_objective_banks_by_provider(self, resource_id):
        raise Unimplemented()

    def get_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks()

    objective_banks = property(fget=get_objective_banks)


class ObjectiveBankQuerySession(abc_learning_sessions.ObjectiveBankQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveBankQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'

    def can_search_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.can_search_bins_template
        return self._can('search')

    def get_objective_bank_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_query()

    objective_bank_query = property(fget=get_objective_bank_query)

    @raise_null_argument
    def get_objective_banks_by_query(self, objective_bank_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_objective_banks_by_query(objective_bank_query)


class ObjectiveBankSearchSession(abc_learning_sessions.ObjectiveBankSearchSession, ObjectiveBankQuerySession):
    """Adapts underlying ObjectiveBankSearchSession methodswith authorization checks."""

    def get_objective_bank_search(self):
        raise Unimplemented()

    objective_bank_search = property(fget=get_objective_bank_search)

    def get_objective_bank_search_order(self):
        raise Unimplemented()

    objective_bank_search_order = property(fget=get_objective_bank_search_order)

    @raise_null_argument
    def get_objective_banks_by_search(self, objective_bank_query, objective_bank_search):
        raise Unimplemented()

    @raise_null_argument
    def get_objective_bank_query_from_inspector(self, objective_bank_query_inspector):
        raise Unimplemented()


class ObjectiveBankAdminSession(abc_learning_sessions.ObjectiveBankAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveBankAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'

    def can_create_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_objective_bank_with_record_types(self, objective_bank_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if objective_bank_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_objective_bank_form_for_create(self, objective_bank_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_form_for_create(objective_bank_record_types)

    @raise_null_argument
    def create_objective_bank(self, objective_bank_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_objective_bank(objective_bank_form)

    def can_update_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_objective_bank_form_for_update(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_form_for_update(objective_bank_id)

    @raise_null_argument
    def update_objective_bank(self, objective_bank_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_objective_bank(objective_bank_form)

    def can_delete_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_objective_bank(objective_bank_id)

    def can_manage_objective_bank_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_objective_bank(self, objective_bank_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_objective_bank(objective_bank_id, alias_id)


class ObjectiveBankNotificationSession(abc_learning_sessions.ObjectiveBankNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveBankNotificationSession methodswith authorization checks."""

    def can_register_for_objective_bank_notifications(self):
        raise Unimplemented()

    def reliable_objective_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_objective_bank_notifications()

    def unreliable_objective_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_objective_bank_notifications()

    @raise_null_argument
    def acknowledge_objective_bank_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_objective_banks(self):
        raise Unimplemented()

    def register_for_changed_objective_banks(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_objective_bank(self, objective_bank_id):
        raise Unimplemented()

    def register_for_deleted_objective_banks(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_objective_bank(self, objective_bank_id):
        raise Unimplemented()

    def register_for_changed_objective_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective_bank_hierarchy()

    @raise_null_argument
    def register_for_changed_objective_bank_hierarchy_for_ancestors(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective_bank_hierarchy_for_ancestors(objective_bank_id)

    @raise_null_argument
    def register_for_changed_objective_bank_hierarchy_for_descendants(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_objective_bank_hierarchy_for_descendants(objective_bank_id)

    def reliable_objective_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_objective_bank_notifications()

    def unreliable_objective_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_objective_bank_notifications()

    @raise_null_argument
    def acknowledge_objective_bank_notification(self, notification_id):
        raise Unimplemented()


class ObjectiveBankHierarchySession(abc_learning_sessions.ObjectiveBankHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveBankHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'

    def get_objective_bank_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_objective_bank_hierarchy_id()

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_hierarchy()

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_objective_bank_view()

    def use_plenary_objective_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_objective_bank_view()

    def get_root_objective_bank_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_objective_bank_ids()

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_objective_banks()

    root_objective_banks = property(fget=get_root_objective_banks)

    @raise_null_argument
    def has_parent_objective_banks(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_objective_banks(objective_bank_id)

    @raise_null_argument
    def is_parent_of_objective_bank(self, id_, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_objective_bank(id_, objective_bank_id)

    @raise_null_argument
    def get_parent_objective_bank_ids(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_objective_bank_ids(objective_bank_id)

    @raise_null_argument
    def get_parent_objective_banks(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_objective_banks(objective_bank_id)

    @raise_null_argument
    def is_ancestor_of_objective_bank(self, id_, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_objective_bank(id_, objective_bank_id)

    @raise_null_argument
    def has_child_objective_banks(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_objective_banks(objective_bank_id)

    @raise_null_argument
    def is_child_of_objective_bank(self, id_, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_objective_bank(id_, objective_bank_id)

    @raise_null_argument
    def get_child_objective_bank_ids(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_objective_bank_ids(objective_bank_id)

    @raise_null_argument
    def get_child_objective_banks(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_objective_banks(objective_bank_id)

    @raise_null_argument
    def is_descendant_of_objective_bank(self, id_, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_objective_bank(id_, objective_bank_id)

    @raise_null_argument
    def get_objective_bank_node_ids(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_node_ids(
            objective_bank_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_objective_bank_nodes(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_nodes(
            objective_bank_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class ObjectiveBankHierarchyDesignSession(abc_learning_sessions.ObjectiveBankHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying ObjectiveBankHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'learning.ObjectiveBank'
        # should this be 'learning.ObjectiveBankHierarchy' ?

    def get_objective_bank_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_objective_bank_hierarchy_id()

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_objective_bank_hierarchy()

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_modify_objective_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_objective_bank(objective_bank_id)

    @raise_null_argument
    def remove_root_objective_bank(self, objective_bank_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_objective_bank(objective_bank_id)

    @raise_null_argument
    def add_child_objective_bank(self, objective_bank_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_objective_bank(objective_bank_id, child_id)

    @raise_null_argument
    def remove_child_objective_bank(self, objective_bank_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_objective_bank(objective_bank_id, child_id)

    @raise_null_argument
    def remove_child_objective_banks(self, objective_bank_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_objective_banks(objective_bank_id)
