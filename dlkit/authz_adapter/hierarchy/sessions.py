"""AuthZ Adapter implementations of hierarchy sessions."""
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
from dlkit.abstract_osid.hierarchy import sessions as abc_hierarchy_sessions


class HierarchyTraversalSession(abc_hierarchy_sessions.HierarchyTraversalSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyTraversalSession methodswith authorization checks."""

    def get_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_hierarchy_id()

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_hierarchy()

    hierarchy = property(fget=get_hierarchy)

    def can_access_hierarchy(self):
        raise Unimplemented()

    def get_roots(self):
        raise Unimplemented()

    roots = property(fget=get_roots)

    @raise_null_argument
    def has_parents(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def is_parent(self, id_, parent_id):
        raise Unimplemented()

    @raise_null_argument
    def get_parents(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def is_ancestor(self, id_, ancestor_id):
        raise Unimplemented()

    @raise_null_argument
    def has_children(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def is_child(self, id_, child_id):
        raise Unimplemented()

    @raise_null_argument
    def get_children(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def is_descendant(self, id_, descendant_id):
        raise Unimplemented()

    @raise_null_argument
    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()


class HierarchyDesignSession(abc_hierarchy_sessions.HierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyDesignSession methodswith authorization checks."""

    def get_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_hierarchy_id()

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_hierarchy()

    hierarchy = property(fget=get_hierarchy)

    def can_modify_hierarchy(self):
        raise Unimplemented()

    @raise_null_argument
    def add_root(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def add_child(self, id_, child_id):
        raise Unimplemented()

    @raise_null_argument
    def remove_root(self, id_):
        raise Unimplemented()

    @raise_null_argument
    def remove_child(self, id_, child_id):
        raise Unimplemented()

    @raise_null_argument
    def remove_children(self, id_):
        raise Unimplemented()


class HierarchySequencingSession(abc_hierarchy_sessions.HierarchySequencingSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchySequencingSession methodswith authorization checks."""

    def get_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_hierarchy_id()

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_hierarchy()

    hierarchy = property(fget=get_hierarchy)

    def can_sequence_hierarchy(self):
        raise Unimplemented()

    @raise_null_argument
    def move_node_ahead(self, parent_id, reference_id, id_):
        raise Unimplemented()

    @raise_null_argument
    def move_node_behind(self, parent_id, reference_id, id_):
        raise Unimplemented()

    @raise_null_argument
    def sequence_nodes(self, parent_id, ids):
        raise Unimplemented()


class HierarchyStructureNotificationSession(abc_hierarchy_sessions.HierarchyStructureNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyStructureNotificationSession methodswith authorization checks."""

    def get_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_hierarchy_id()

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_hierarchy()

    hierarchy = property(fget=get_hierarchy)

    def can_register_for_hierarchy_structure_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def reliable_hierarchy_structure_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_hierarchy_structure_notifications()

    def unreliable_hierarchy_structure_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_hierarchy_structure_notifications()

    @raise_null_argument
    def acknowledge_hierarchy_structure_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_hierarchy_nodes(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_hierarchy_nodes()

    def register_for_deleted_hierarchy_nodes(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_hierarchy_nodes()

    @raise_null_argument
    def register_for_deleted_hierarchy_node(self, node_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_hierarchy_node(node_id)

    def register_for_changed_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_hierarchy()

    @raise_null_argument
    def register_for_changed_hierarchy_for_ancestors(self, billing_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_hierarchy_for_ancestors(billing_id)

    @raise_null_argument
    def register_for_changed_hierarchy_for_descendants(self, node_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_hierarchy_for_descendants(node_id)

    def reliable_hierarchy_structure_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_hierarchy_structure_notifications()

    def unreliable_hierarchy_structure_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_hierarchy_structure_notifications()

    @raise_null_argument
    def acknowledge_hierarchy_structure_notification(self, notification_id):
        raise Unimplemented()


class HierarchyLookupSession(abc_hierarchy_sessions.HierarchyLookupSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('hierarchy.Hierarchy%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'hierarchy.Hierarchy'

    def can_lookup_hierarchies(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_hierarchy_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_hierarchy_view()

    def use_plenary_hierarchy_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_hierarchy_view()

    @raise_null_argument
    def get_hierarchy(self, hierarchy_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchy(hierarchy_id)

    @raise_null_argument
    def get_hierarchies_by_ids(self, hierarchy_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchies_by_ids(hierarchy_ids)

    @raise_null_argument
    def get_hierarchies_by_genus_type(self, hierarchy_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchies_by_genus_type(hierarchy_genus_type)

    @raise_null_argument
    def get_hierarchies_by_parent_genus_type(self, hierarchy_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_hierarchies_by_record_type(self, hierarchy_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_hierarchies_by_provider(self, resource_id):
        raise Unimplemented()

    def get_hierarchies(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchies()

    hierarchies = property(fget=get_hierarchies)


class HierarchyQuerySession(abc_hierarchy_sessions.HierarchyQuerySession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('hierarchy.Hierarchy%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'hierarchy.Hierarchy'

    def can_search_hierarchies(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_hierarchy_ids()))

    def get_hierarchy_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchy_query()

    hierarchy_query = property(fget=get_hierarchy_query)

    @raise_null_argument
    def get_hierarchies_by_query(self, hierarchy_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchies_by_query(hierarchy_query)


class HierarchySearchSession(abc_hierarchy_sessions.HierarchySearchSession, HierarchyQuerySession):
    """Adapts underlying HierarchySearchSession methodswith authorization checks."""

    def get_hierarchy_search(self):
        raise Unimplemented()

    hierarchy_search = property(fget=get_hierarchy_search)

    def get_hierarchy_search_order(self):
        raise Unimplemented()

    hierarchy_search_order = property(fget=get_hierarchy_search_order)

    @raise_null_argument
    def get_hierarchies_by_search(self, hierarchy_query, hierarchy_search):
        raise Unimplemented()

    @raise_null_argument
    def get_hierarchy_query_from_inspector(self, hierarchy_query_inspector):
        raise Unimplemented()


class HierarchyAdminSession(abc_hierarchy_sessions.HierarchyAdminSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('hierarchy.Hierarchy%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'hierarchy.Hierarchy'

    def can_create_hierarchies(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_hierarchy_with_record_types(self, hierarchy_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if hierarchy_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchy_form_for_create(hierarchy_record_types)

    @raise_null_argument
    def create_hierarchy(self, hierarchy_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_hierarchy(hierarchy_form)

    def can_update_hierarchies(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_hierarchy_form_for_update(self, hierarchy_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_hierarchy_form_for_update(hierarchy_id)

    @raise_null_argument
    def update_hierarchy(self, hierarchy_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_hierarchy(hierarchy_form)

    def can_delete_hierarchies(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_hierarchy(self, hierarchy_id):
        raise Unimplemented()

    def can_manage_hierarchy_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_hierarchy(self, hierarchy_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_hierarchy(hierarchy_id, alias_id)


class HierarchyNotificationSession(abc_hierarchy_sessions.HierarchyNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying HierarchyNotificationSession methodswith authorization checks."""

    def can_register_for_hierarchy_notifications(self):
        raise Unimplemented()

    def reliable_hierarchy_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_hierarchy_notifications()

    def unreliable_hierarchy_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_hierarchy_notifications()

    @raise_null_argument
    def acknowledge_hierarchy_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_hierarchies(self):
        raise Unimplemented()

    def register_for_changed_hierarchies(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_hierarchy(self, hierarchy_id):
        raise Unimplemented()

    def register_for_deleted_hierarchies(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_hierarchy(self, hierarchy_id):
        raise Unimplemented()

    def reliable_hierarchy_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_hierarchy_notifications()

    def unreliable_hierarchy_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_hierarchy_notifications()

    @raise_null_argument
    def acknowledge_hierarchy_notification(self, notification_id):
        raise Unimplemented()
