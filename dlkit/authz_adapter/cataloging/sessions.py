"""AuthZ Adapter implementations of cataloging sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import sessions as osid_sessions
from ..osid.osid_errors import NotFound
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.abstract_osid.cataloging import sessions as abc_cataloging_sessions


class CatalogSession(abc_cataloging_sessions.CatalogSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'

    def can_lookup_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_catalog_view()

    def use_plenary_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_catalog_view()

    def use_federated_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_catalog_view()
        if self._query_session:
            self._query_session.use_federated_catalog_view()

    def use_isolated_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_catalog_view()
        if self._query_session:
            self._query_session.use_isolated_catalog_view()

    @raise_null_argument
    def get_ids_by_catalog(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_ids_by_catalog(catalog_id)

    @raise_null_argument
    def get_ids_by_catalogs(self, catalog_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_ids_by_catalogs(catalog_ids)

    @raise_null_argument
    def get_catalog_ids_by_id(self, id_):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_ids_by_id(id_)

    @raise_null_argument
    def get_catalogs_by_id(self, id_):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_catalogs_by_id(id_)


class CatalogAssignmentSession(abc_cataloging_sessions.CatalogAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'

    def can_assign_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def assign_id_to_catalog(self, id_, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_id_to_catalog(id_, catalog_id)

    @raise_null_argument
    def unassign_id_from_catalog(self, id_, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_id_from_catalog(id_, catalog_id)

    @raise_null_argument
    def reassign_id_to_catalog(self, id_, from_catalog_id, to_catalog_id):
        raise Unimplemented()


class CatalogEntryNotificationSession(abc_cataloging_sessions.CatalogEntryNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogEntryNotificationSession methodswith authorization checks."""

    def get_catalog_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_catalog_id()

    catalog_id = property(fget=get_catalog_id)

    def get_catalog(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_catalog()

    catalog = property(fget=get_catalog)

    def can_register_for_catalog_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_catalog_view()
        if self._query_session:
            self._query_session.use_federated_catalog_view()

    def use_isolated_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_catalog_view()
        if self._query_session:
            self._query_session.use_isolated_catalog_view()

    def reliable_catalog_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_catalog_entry_notifications()

    def unreliable_catalog_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_catalog_entry_notifications()

    @raise_null_argument
    def acknowledge_catalog_entry_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_catalog_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_catalog_entries()

    def register_for_deleted_catalog_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_catalog_entries()

    def reliable_catalog_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_catalog_entry_notifications()

    def unreliable_catalog_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_catalog_entry_notifications()

    @raise_null_argument
    def acknowledge_catalog_entry_notification(self, notification_id):
        raise Unimplemented()


class CatalogLookupSession(abc_cataloging_sessions.CatalogLookupSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'

    def can_lookup_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_catalog_view()

    def use_plenary_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_catalog_view()

    @raise_null_argument
    def get_catalog(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_catalog(catalog_id)

    @raise_null_argument
    def get_catalogs_by_ids(self, catalog_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_catalogs_by_ids(catalog_ids)

    @raise_null_argument
    def get_catalogs_by_genus_type(self, catalog_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_catalogs_by_genus_type(catalog_genus_type)

    @raise_null_argument
    def get_catalogs_by_parent_genus_type(self, catalog_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_catalogs_by_record_type(self, catalog_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_catalogs_by_provider(self, resource_id):
        raise Unimplemented()

    def get_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_catalogs()

    catalogs = property(fget=get_catalogs)


class CatalogQuerySession(abc_cataloging_sessions.CatalogQuerySession, osid_sessions.OsidSession):
    """Adapts underlying CatalogQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'

    def can_search_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.can_search_bins_template
        return self._can('search')

    def get_catalog_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_query()

    catalog_query = property(fget=get_catalog_query)

    @raise_null_argument
    def get_catalogs_by_query(self, catalog_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_catalogs_by_query(catalog_query)


class CatalogSearchSession(abc_cataloging_sessions.CatalogSearchSession, CatalogQuerySession):
    """Adapts underlying CatalogSearchSession methodswith authorization checks."""

    def get_catalog_search(self):
        raise Unimplemented()

    catalog_search = property(fget=get_catalog_search)

    def get_catalog_search_order(self):
        raise Unimplemented()

    catalog_search_order = property(fget=get_catalog_search_order)

    @raise_null_argument
    def get_catalogs_by_search(self, catalog_query, catalog_search):
        raise Unimplemented()

    @raise_null_argument
    def get_catalog_query_from_inspector(self, catalog_query_inspector):
        raise Unimplemented()


class CatalogAdminSession(abc_cataloging_sessions.CatalogAdminSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'

    def can_create_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_catalog_with_record_types(self, catalog_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if catalog_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_catalog_form_for_create(self, catalog_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_form_for_create(catalog_record_types)

    @raise_null_argument
    def create_catalog(self, catalog_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_catalog(catalog_form)

    def can_update_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_catalog_form_for_update(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_form_for_update(catalog_id)

    @raise_null_argument
    def update_catalog(self, catalog_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_catalog(catalog_form)

    def can_delete_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_catalog(self, catalog_id):
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_catalog(catalog_id)

    def can_manage_catalog_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_catalog(self, catalog_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_catalog(catalog_id, alias_id)


class CatalogNotificationSession(abc_cataloging_sessions.CatalogNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogNotificationSession methodswith authorization checks."""

    def can_register_for_catalog_notifications(self):
        raise Unimplemented()

    def reliable_catalog_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_catalog_notifications()

    def unreliable_catalog_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_catalog_notifications()

    @raise_null_argument
    def acknowledge_catalog_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_catalogs(self):
        raise Unimplemented()

    def register_for_changed_catalogs(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_catalog(self, catalog_id):
        raise Unimplemented()

    def register_for_deleted_catalogs(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_catalog(self, catalog_id):
        raise Unimplemented()

    def register_for_changed_catalog_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_catalog_hierarchy()

    @raise_null_argument
    def register_for_changed_catalog_hierarchy_for_ancestors(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_catalog_hierarchy_for_ancestors(catalog_id)

    @raise_null_argument
    def register_for_changed_catalog_hierarchy_for_descendants(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_catalog_hierarchy_for_descendants(catalog_id)

    def reliable_catalog_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_catalog_notifications()

    def unreliable_catalog_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_catalog_notifications()

    @raise_null_argument
    def acknowledge_catalog_notification(self, notification_id):
        raise Unimplemented()


class CatalogHierarchySession(abc_cataloging_sessions.CatalogHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying CatalogHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'

    def get_catalog_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_catalog_hierarchy_id()

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    def get_catalog_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_hierarchy()

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    def can_access_catalog_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_catalog_view()

    def use_plenary_catalog_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_catalog_view()

    def get_root_catalog_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_catalog_ids()

    root_catalog_ids = property(fget=get_root_catalog_ids)

    def get_root_catalogs(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_catalogs()

    root_catalogs = property(fget=get_root_catalogs)

    @raise_null_argument
    def has_parent_catalogs(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_catalogs(catalog_id)

    @raise_null_argument
    def is_parent_of_catalog(self, id_, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_catalog(id_, catalog_id)

    @raise_null_argument
    def get_parent_catalog_ids(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_catalog_ids(catalog_id)

    @raise_null_argument
    def get_parent_catalogs(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_catalogs(catalog_id)

    @raise_null_argument
    def is_ancestor_of_catalog(self, id_, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_catalog(id_, catalog_id)

    @raise_null_argument
    def has_child_catalogs(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_catalogs(catalog_id)

    @raise_null_argument
    def is_child_of_catalog(self, id_, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_catalog(id_, catalog_id)

    @raise_null_argument
    def get_child_catalog_ids(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_catalog_ids(catalog_id)

    @raise_null_argument
    def get_child_catalogs(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_catalogs(catalog_id)

    @raise_null_argument
    def is_descendant_of_catalog(self, id_, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_catalog(id_, catalog_id)

    @raise_null_argument
    def get_catalog_node_ids(self, catalog_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_node_ids(
            catalog_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_catalog_nodes(self, catalog_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_nodes(
            catalog_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class CatalogHierarchyDesignSession(abc_cataloging_sessions.CatalogHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying CatalogHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('cataloging.Catalog%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'cataloging.Catalog'
        # should this be 'cataloging.CatalogHierarchy' ?

    def get_catalog_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_catalog_hierarchy_id()

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    def get_catalog_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_catalog_hierarchy()

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    def can_modify_catalog_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_catalog(self, catalog_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_catalog(catalog_id)

    @raise_null_argument
    def remove_root_catalog(self, catalog_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_catalog(catalog_id)

    @raise_null_argument
    def add_child_catalog(self, catalog_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_catalog(catalog_id, child_id)

    @raise_null_argument
    def remove_child_catalog(self, catalog_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_catalog(catalog_id, child_id)

    @raise_null_argument
    def remove_child_catalogs(self, catalog_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_catalogs(catalog_id)
