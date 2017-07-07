"""AuthZ Adapter implementations of relationship sessions."""
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
from dlkit.abstract_osid.relationship import sessions as abc_relationship_sessions


class RelationshipLookupSession(abc_relationship_sessions.RelationshipLookupSession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_family_id()
        self._id_namespace = 'relationship.Relationship'
        self.use_federated_family_view()
        self.use_comparative_relationship_view()
        self._auth_family_ids = None
        self._unauth_family_ids = None
    #     self._overriding_family_ids = None
    #
    # def _get_overriding_family_ids(self):
    #     if self._overriding_family_ids is None:
    #         self._overriding_family_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_family_ids

    def _try_overriding_families(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_family_id(catalog_id, match=True)
        return self._query_session.get_relationships_by_query(query), query

    def _get_unauth_family_ids(self, family_id):
        if self._can('lookup', family_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(family_id)]
        if self._hierarchy_session.has_child_families(family_id):
            for child_family_id in self._hierarchy_session.get_child_family_ids(family_id):
                unauth_list = unauth_list + self._get_unauth_family_ids(child_family_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_families(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_family_ids is None:
            self._unauth_family_ids = self._get_unauth_family_ids(self._qualifier_id)
        for family_id in self._unauth_family_ids:
            query.match_family_id(family_id, match=False)
        return self._query_session.get_relationships_by_query(query)

    def get_family_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_family_id()

    family_id = property(fget=get_family_id)

    def get_family(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_family()

    family = property(fget=get_family)

    def can_lookup_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_relationship_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_relationship_view()

    def use_plenary_relationship_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_relationship_view()

    def use_federated_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_family_view()
        if self._query_session:
            self._query_session.use_federated_family_view()

    def use_isolated_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_family_view()
        if self._query_session:
            self._query_session.use_isolated_family_view()

    def use_effective_relationship_view(self):
        raise Unimplemented()

    def use_any_effective_relationship_view(self):
        raise Unimplemented()

    @raise_null_argument
    def get_relationship(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_relationship(relationship_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_id(relationship_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_relationships_by_ids(self, relationship_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_relationships_by_ids(relationship_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        for relationship_id in (relationship_ids):
            query.match_id(relationship_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_relationships_by_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_relationships_by_genus_type(relationship_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_genus_type(relationship_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_relationships_by_parent_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_relationships_by_parent_genus_type(relationship_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_parent_genus_type(relationship_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_relationships_by_record_type(self, relationship_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_relationships_by_record_type(relationship_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_record_type(relationship_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_relationships_on_date(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_for_source(self, source_id):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        if self._can('lookup'):
            return self._provider_session.get_relationships_for_source(source_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_source_id(source_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_relationships_for_source_on_date(self, source_id, from_, to):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_source_on_date"""
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        if self._can('lookup'):
            return self._provider_session.get_relationships_for_source_on_date(source_id, from_, to)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_source_id(source_id, match=True)
        query.match_date(from_, to, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_relationships_by_genus_type_for_source(self, source_id, relationship_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_by_genus_type_for_source_on_date(self, source_id, relationship_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_for_destination(self, destination_id):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_for_destination_on_date(self, destination_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_by_genus_type_for_destination(self, destination_id, relationship_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_by_genus_type_for_destination_on_date(self, destination_id, relationship_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_for_peers(self, source_id, destination_id):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_for_peers_on_date(self, source_id, destination_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_by_genus_type_for_peers(self, source_id, destination_id, relationship_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_relationships_by_genus_type_for_peers_on_date(self, source_id, destination_id, relationship_genus_type, from_, to):
        raise Unimplemented()

    def get_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_relationships()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_relationship_query()
        query.match_any(match=True)
        return self._try_harder(query)

    relationships = property(fget=get_relationships)


class RelationshipQuerySession(abc_relationship_sessions.RelationshipQuerySession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_family_id()
        self._id_namespace = 'relationship.Relationship'
        self.use_federated_family_view()
        self._unauth_family_ids = None
        # self._overriding_family_ids = None

    # def _get_overriding_family_ids(self):
    #     if self._overriding_family_ids is None:
    #         self._overriding_family_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_family_ids

    def _try_overriding_families(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for family_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_family_id(family_id, match=True)
        return self._query_session.get_relationships_by_query(query), query

    def _get_unauth_family_ids(self, family_id):
        if self._can('search', family_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(family_id)]
        if self._hierarchy_session.has_child_families(family_id):
            for child_family_id in self._hierarchy_session.get_child_family_ids(family_id):
                unauth_list = unauth_list + self._get_unauth_family_ids(child_family_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_families(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_family_ids is None:
            self._unauth_family_ids = self._get_unauth_family_ids(self._qualifier_id)
        for family_id in self._unauth_family_ids:
            query._provider_query.match_family_id(family_id, match=False)
        return self._query_session.get_relationships_by_query(query)

    class RelationshipQueryWrapper(QueryWrapper):
        """Wrapper for RelationshipQueries to override match_family_id method"""

        def match_family_id(self, family_id, match=True):
            self._cat_id_args_list.append({'family_id': family_id, 'match': match})

    def get_family_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_family_id()

    family_id = property(fget=get_family_id)

    def get_family(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_family()

    family = property(fget=get_family)

    def use_federated_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_family_view()
        if self._query_session:
            self._query_session.use_federated_family_view()

    def use_isolated_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_family_view()
        if self._query_session:
            self._query_session.use_isolated_family_view()

    def can_search_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def get_relationship_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.RelationshipQueryWrapper(self._provider_session.get_relationship_query())

    relationship_query = property(fget=get_relationship_query)

    @raise_null_argument
    def get_relationships_by_query(self, relationship_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(relationship_query, '_cat_id_args_list'):
            raise Unsupported('relationship_query not from this session')
        for kwargs in relationship_query._cat_id_args_list:
            if self._can('search', kwargs['family_id']):
                relationship_query._provider_query.match_family_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_relationships_by_query(relationship_query)
        self._check_search_conditions()
        result = self._try_harder(relationship_query)
        relationship_query._provider_query.clear_family_terms()
        return result


class RelationshipSearchSession(abc_relationship_sessions.RelationshipSearchSession, RelationshipQuerySession):
    """Adapts underlying RelationshipSearchSession methodswith authorization checks."""

    def get_relationship_search(self):
        """Pass through to provider RelationshipSearchSession.get_relationship_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_relationship_search()

    relationship_search = property(fget=get_relationship_search)

    def get_relationship_search_order(self):
        raise Unimplemented()

    relationship_search_order = property(fget=get_relationship_search_order)

    @raise_null_argument
    def get_relationships_by_search(self, relationship_query, relationship_search):
        """Pass through to provider RelationshipSearchSession.get_relationships_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_relationships_by_search(relationship_query, relationship_search)

    @raise_null_argument
    def get_relationship_query_from_inspector(self, relationship_query_inspector):
        raise Unimplemented()


class RelationshipAdminSession(abc_relationship_sessions.RelationshipAdminSession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_family_id()
        self._id_namespace = 'relationship.Relationship'
        self._overriding_family_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_relationship_family_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_relationship_family_session()
                self.get_family_ids_by_relationship = self._object_catalog_session.get_family_ids_by_relationship
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_family_ids(self):
        if self._overriding_family_ids is None:
            self._overriding_family_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_family_ids

    def _can_for_relationship(self, func_name, relationship_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, relationship_id, 'get_family_ids_for_relationship')

    def get_family_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_family_id()

    family_id = property(fget=get_family_id)

    def get_family(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_family()

    family = property(fget=get_family)

    def can_create_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_relationship_with_record_types(self, relationship_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if relationship_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_relationship_form_for_create(self, source_id, destination_id, relationship_record_types):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_relationship_form_for_create(source_id, destination_id, relationship_record_types)

    @raise_null_argument
    def create_relationship(self, relationship_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_relationship(relationship_form)

    def can_update_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_relationship_form_for_update(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_relationship('update', relationship_id):
            raise PermissionDenied()
        return self._provider_session.get_relationship_form_for_update(relationship_id)

    def duplicate_relationship(self, relationship_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_relationship(relationship_id)

    @raise_null_argument
    def update_relationship(self, relationship_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_relationship(relationship_form)

    def can_delete_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_relationship(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_relationship('delete', relationship_id):
            raise PermissionDenied()
        return self._provider_session.delete_relationship(relationship_id)

    def can_manage_relationship_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_relationship(self, relationship_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_relationship('alias', relationship_id):
            raise PermissionDenied()
        return self._provider_session.alias_relationship(relationship_id, alias_id)


class RelationshipNotificationSession(abc_relationship_sessions.RelationshipNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipNotificationSession methodswith authorization checks."""

    def get_family_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_family_id()

    family_id = property(fget=get_family_id)

    def get_family(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_family()

    family = property(fget=get_family)

    def can_register_for_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_family_view()
        if self._query_session:
            self._query_session.use_federated_family_view()

    def use_isolated_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_family_view()
        if self._query_session:
            self._query_session.use_isolated_family_view()

    def reliable_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_relationship_notifications()

    def unreliable_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_relationship_notifications()

    @raise_null_argument
    def acknowledge_relationship_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_relationships()

    @raise_null_argument
    def register_for_new_relationships_for_source(self, source_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_relationships_for_source()

    @raise_null_argument
    def register_for_new_relationships_for_destination(self, destination_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_relationships_for_destination()

    @raise_null_argument
    def register_for_new_relationships_by_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_relationships_by_genus_type(relationship_genus_type)

    def register_for_changed_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_relationships()

    @raise_null_argument
    def register_for_changed_relationships_for_source(self, source_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_relationships_for_source(source_id)

    @raise_null_argument
    def register_for_changed_relationships_for_destination(self, destination_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_relationships_for_destination(destination_id)

    @raise_null_argument
    def register_for_changed_relationships_by_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_relationships_by_genus_type(relationship_genus_type)

    @raise_null_argument
    def register_for_changed_relationship(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_relationship(relationship_id)

    def register_for_deleted_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_relationships()

    @raise_null_argument
    def register_for_deleted_relationships_for_source(self, source_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_relationships_for_source(source_id)

    @raise_null_argument
    def register_for_deleted_relationships_for_destination(self, destination_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_relationships_for_destination(destination_id)

    @raise_null_argument
    def register_for_deleted_relationships_by_genus_type(self, relationship_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_relationships_by_genus_type(relationship_genus_type)

    @raise_null_argument
    def register_for_deleted_relationship(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_relationship(relationship_id)

    def reliable_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_relationship_notifications()

    def unreliable_relationship_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_relationship_notifications()

    @raise_null_argument
    def acknowledge_relationship_notification(self, notification_id):
        raise Unimplemented()


class RelationshipFamilySession(abc_relationship_sessions.RelationshipFamilySession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipFamilySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'relationship.RelationshipFamily'

    def can_lookup_relationship_family_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_family_view()

    def use_plenary_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_family_view()

    @raise_null_argument
    def get_relationship_ids_by_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_relationship_ids_by_family(family_id)

    @raise_null_argument
    def get_relationships_by_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_relationships_by_family(family_id)

    @raise_null_argument
    def get_relationship_ids_by_families(self, family_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_relationship_ids_by_families(family_ids)

    @raise_null_argument
    def get_relationships_by_families(self, family_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_relationships_by_families(family_ids)

    @raise_null_argument
    def get_family_ids_by_relationship(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_family_ids_by_relationship(relationship_id)

    @raise_null_argument
    def get_families_by_relationship(self, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_families_by_relationship(relationship_id)


class RelationshipFamilyAssignmentSession(abc_relationship_sessions.RelationshipFamilyAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipFamilyAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'relationship.RelationshipFamily'

    def can_assign_relationships(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_relationships_to_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=family_id)

    @raise_null_argument
    def get_assignable_family_ids(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_family_ids(family_id)

    @raise_null_argument
    def get_assignable_family_ids_for_relationship(self, family_id, relationship_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_family_ids_for_relationship(family_id, relationship_id)

    @raise_null_argument
    def assign_relationship_to_family(self, relationship_id, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_relationship_to_family(relationship_id, family_id)

    @raise_null_argument
    def unassign_relationship_from_family(self, relationship_id, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_relationship_from_family(relationship_id, family_id)

    @raise_null_argument
    def reassign_relationship_to_family(self, relationship_id, from_family_id, to_family_id):
        raise Unimplemented()


class RelationshipSmartFamilySession(abc_relationship_sessions.RelationshipSmartFamilySession, osid_sessions.OsidSession):
    """Adapts underlying RelationshipSmartFamilySession methodswith authorization checks."""

    def get_family_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_family_id()

    family_id = property(fget=get_family_id)

    def get_family(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_family()

    family = property(fget=get_family)

    def can_manage_smart_families(self):
        raise Unimplemented()

    def get_relationship_query(self):
        raise Unimplemented()

    relationship_query = property(fget=get_relationship_query)

    def get_relationship_search_order(self):
        raise Unimplemented()

    relationship_search_order = property(fget=get_relationship_search_order)

    @raise_null_argument
    def apply_relationship_query(self, relationship_query):
        raise Unimplemented()

    def inspect_relationship_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_relationship_sequencing(self, relationship_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_relationship_query_from_inspector(self, relationship_query_inspector):
        raise Unimplemented()


class FamilyLookupSession(abc_relationship_sessions.FamilyLookupSession, osid_sessions.OsidSession):
    """Adapts underlying FamilyLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'relationship.Family'

    def can_lookup_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_family_view()

    def use_plenary_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_family_view()

    @raise_null_argument
    def get_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_family(family_id)

    @raise_null_argument
    def get_families_by_ids(self, family_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_families_by_ids(family_ids)

    @raise_null_argument
    def get_families_by_genus_type(self, family_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_families_by_genus_type(family_genus_type)

    @raise_null_argument
    def get_families_by_parent_genus_type(self, family_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_families_by_record_type(self, family_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_families_by_provider(self, resource_id):
        raise Unimplemented()

    def get_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_families()

    families = property(fget=get_families)


class FamilyQuerySession(abc_relationship_sessions.FamilyQuerySession, osid_sessions.OsidSession):
    """Adapts underlying FamilyQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'relationship.Family'

    def can_search_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.can_search_bins_template
        return self._can('search')

    def get_family_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_family_query()

    family_query = property(fget=get_family_query)

    @raise_null_argument
    def get_families_by_query(self, family_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_families_by_query(family_query)


class FamilySearchSession(abc_relationship_sessions.FamilySearchSession, FamilyQuerySession):
    """Adapts underlying FamilySearchSession methodswith authorization checks."""

    def get_family_search(self):
        raise Unimplemented()

    family_search = property(fget=get_family_search)

    def get_family_search_order(self):
        raise Unimplemented()

    family_search_order = property(fget=get_family_search_order)

    @raise_null_argument
    def get_families_by_search(self, family_query, family_search):
        raise Unimplemented()

    @raise_null_argument
    def get_family_query_from_inspector(self, family_query_inspector):
        raise Unimplemented()


class FamilyAdminSession(abc_relationship_sessions.FamilyAdminSession, osid_sessions.OsidSession):
    """Adapts underlying FamilyAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'relationship.Family'

    def can_create_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_family_with_record_types(self, family_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if family_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_family_form_for_create(self, family_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_family_form_for_create(family_record_types)

    @raise_null_argument
    def create_family(self, family_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_family(family_form)

    def can_update_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_family_form_for_update(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_family_form_for_update(family_id)

    @raise_null_argument
    def update_family(self, family_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_family(family_form)

    def can_delete_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_family(family_id)

    def can_manage_family_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_family(self, family_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_family(family_id, alias_id)


class FamilyNotificationSession(abc_relationship_sessions.FamilyNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying FamilyNotificationSession methodswith authorization checks."""

    def can_register_for_family_notifications(self):
        raise Unimplemented()

    def reliable_family_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_family_notifications()

    def unreliable_family_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_family_notifications()

    @raise_null_argument
    def acknowledge_family_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_families(self):
        raise Unimplemented()

    def register_for_changed_families(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_family(self, family_id):
        raise Unimplemented()

    def register_for_deleted_families(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_family(self, family_id):
        raise Unimplemented()

    def register_for_changed_family_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_family_hierarchy()

    @raise_null_argument
    def register_for_changed_family_hierarchy_for_ancestors(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_family_hierarchy_for_ancestors(family_id)

    @raise_null_argument
    def register_for_changed_family_hierarchy_for_descendants(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_family_hierarchy_for_descendants(family_id)

    def reliable_family_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_family_notifications()

    def unreliable_family_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_family_notifications()

    @raise_null_argument
    def acknowledge_family_notification(self, notification_id):
        raise Unimplemented()


class FamilyHierarchySession(abc_relationship_sessions.FamilyHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying FamilyHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'relationship.Family'

    def get_family_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_family_hierarchy_id()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_family_hierarchy()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_access_family_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_family_view()

    def use_plenary_family_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_family_view()

    def get_root_family_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_family_ids()

    root_family_ids = property(fget=get_root_family_ids)

    def get_root_families(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_families()

    root_families = property(fget=get_root_families)

    @raise_null_argument
    def has_parent_families(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_families(family_id)

    @raise_null_argument
    def is_parent_of_family(self, id_, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_family(id_, family_id)

    @raise_null_argument
    def get_parent_family_ids(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_family_ids(family_id)

    @raise_null_argument
    def get_parent_families(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_families(family_id)

    @raise_null_argument
    def is_ancestor_of_family(self, id_, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_family(id_, family_id)

    @raise_null_argument
    def has_child_families(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_families(family_id)

    @raise_null_argument
    def is_child_of_family(self, id_, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_family(id_, family_id)

    @raise_null_argument
    def get_child_family_ids(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_family_ids(family_id)

    @raise_null_argument
    def get_child_families(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_families(family_id)

    @raise_null_argument
    def is_descendant_of_family(self, id_, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_family(id_, family_id)

    @raise_null_argument
    def get_family_node_ids(self, family_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_family_node_ids(
            family_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_family_nodes(self, family_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_family_nodes(
            family_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class FamilyHierarchyDesignSession(abc_relationship_sessions.FamilyHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying FamilyHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('relationship.Family%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'relationship.Family'
        # should this be 'relationship.FamilyHierarchy' ?

    def get_family_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_family_hierarchy_id()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_family_hierarchy()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_modify_family_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_family(family_id)

    @raise_null_argument
    def remove_root_family(self, family_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_family(family_id)

    @raise_null_argument
    def add_child_family(self, family_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_family(family_id, child_id)

    @raise_null_argument
    def remove_child_family(self, family_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_family(family_id, child_id)

    @raise_null_argument
    def remove_child_families(self, family_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_families(family_id)
