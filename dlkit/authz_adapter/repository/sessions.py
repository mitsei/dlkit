"""AuthZ Adapter implementations of repository sessions."""
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
from dlkit.abstract_osid.repository import sessions as abc_repository_sessions


class AssetLookupSession(abc_repository_sessions.AssetLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AssetLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Asset'
        self.use_federated_repository_view()
        self.use_comparative_asset_view()
        self._auth_repository_ids = None
        self._unauth_repository_ids = None
    #     self._overriding_repository_ids = None
    #
    # def _get_overriding_repository_ids(self):
    #     if self._overriding_repository_ids is None:
    #         self._overriding_repository_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_repository_ids

    def _try_overriding_repositories(self, query):
        for catalog_id in self._get_overriding_catalog_ids('lookup'):
            query.match_repository_id(catalog_id, match=True)
        return self._query_session.get_assets_by_query(query), query

    def _get_unauth_repository_ids(self, repository_id):
        if self._can('lookup', repository_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(repository_id)]
        if self._hierarchy_session.has_child_repositories(repository_id):
            for child_repository_id in self._hierarchy_session.get_child_repository_ids(repository_id):
                unauth_list = unauth_list + self._get_unauth_repository_ids(child_repository_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_repositories(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_repository_ids is None:
            self._unauth_repository_ids = self._get_unauth_repository_ids(self._qualifier_id)
        for repository_id in self._unauth_repository_ids:
            query.match_repository_id(repository_id, match=False)
        return self._query_session.get_assets_by_query(query)

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_asset_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_asset_view()

    def use_plenary_asset_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_asset_view()

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    @raise_null_argument
    def get_asset(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_asset(asset_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_query()
        query.match_id(asset_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_assets_by_ids(self, asset_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_assets_by_ids(asset_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_query()
        for asset_id in (asset_ids):
            query.match_id(asset_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assets_by_genus_type(self, asset_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assets_by_genus_type(asset_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_query()
        query.match_genus_type(asset_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assets_by_parent_genus_type(self, asset_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assets_by_parent_genus_type(asset_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_query()
        query.match_parent_genus_type(asset_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assets_by_record_type(self, asset_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_assets_by_record_type(asset_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_query()
        query.match_record_type(asset_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assets_by_provider(self, resource_id):
        raise Unimplemented()

    def get_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_assets()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_query()
        query.match_any(match=True)
        return self._try_harder(query)

    assets = property(fget=get_assets)


# This still needs to be updated to work with authz overrides
class AssetContentLookupSession(abc_repository_sessions.AssetContentLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AssetContentLookupSession methods with authorization checks
    For now uses the "Asset" namespace authz -- assumes if you can lookup an asset, you can
     lookup the contents. That could change in the future.
    """

    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Asset'  # use Asset namespace for things like authz check
        self.use_federated_repository_view()
        self._auth_repository_ids = None
        self._unauth_repository_ids = None

    def _get_unauth_repository_ids(self, repository_id):
        if self._can('lookup', repository_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(repository_id)]
        if self._hierarchy_session.has_child_repositories(repository_id):
            for child_repository_id in self._hierarchy_session.get_child_repository_ids(repository_id):
                unauth_list = unauth_list + self._get_unauth_repository_ids(child_repository_id)
        return unauth_list

    def _try_harder(self, query):
        if self._hierarchy_session is None or self._query_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        if self._unauth_repository_ids is None:
            self._unauth_repository_ids = self._get_unauth_repository_ids(self._qualifier_id)
        for repository_id in self._unauth_repository_ids:
            query.match_repository_id(repository_id, match=False)
        return self._query_session.get_assets_by_query(query)

    def get_repository_id(self):
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_asset_contents(self):
        return self._can('lookup')

    def use_comparative_asset_content_view(self):
        self._use_comparative_object_view()
        self._provider_session.use_comparative_asset_content_view()

    def use_plenary_asset_content_view(self):
        self._use_plenary_object_view()
        self._provider_session.use_plenary_asset_content_view()

    def use_federated_repository_view(self):
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()

    def get_asset_content(self, asset_content_id):
        if self._can('lookup'):
            return self._provider_session.get_asset_content(asset_content_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_content_query()
        query.match_id(asset_content_id, match=True)
        results = self._try_harder(query)
        if results.available() > 0:
            return results.next()
        else:
            raise NotFound()

    def get_asset_contents_by_ids(self, asset_content_ids):
        if self._can('lookup'):
            return self._provider_session.get_asset_contents_by_ids(asset_content_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_content_query()
        for asset_content_id in (asset_content_ids):
            query.match_id(asset_content_id, match=True)
        return self._try_harder(query)

    def get_asset_contents_by_genus_type(self, asset_content_genus_type):
        if self._can('lookup'):
            return self._provider_session.get_asset_contents_by_genus_type(asset_content_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_content_query()
        query.match_genus_type(asset_content_genus_type, match=True)
        return self._try_harder(query)

    def get_asset_contents_by_parent_genus_type(self, asset_content_genus_type):
        if self._can('lookup'):
            return self._provider_session.get_asset_contents_by_parent_genus_type(asset_content_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_content_query()
        query.match_parent_genus_type(asset_content_genus_type, match=True)
        return self._try_harder(query)

    def get_asset_contents_by_record_type(self, asset_content_record_type):
        if self._can('lookup'):
            return self._provider_session.get_asset_contents_by_record_type(asset_content_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_asset_content_query()
        query.match_record_type(asset_content_record_type, match=True)
        return self._try_harder(query)

    def get_asset_contents_for_asset(self, asset_id):
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_asset_contents_for_asset(asset_id)

    def get_asset_contents_by_genus_type_for_asset(self, asset_content_genus_type, asset_id):
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_asset_contents_by_genus_type_for_asset(asset_content_genus_type,
                                                                                     asset_id)


class AssetQuerySession(abc_repository_sessions.AssetQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AssetQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Asset'
        self.use_federated_repository_view()
        self._unauth_repository_ids = None
        # self._overriding_repository_ids = None

    # def _get_overriding_repository_ids(self):
    #     if self._overriding_repository_ids is None:
    #         self._overriding_repository_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_repository_ids

    def _try_overriding_repositories(self, query):
        for repository_id in self._get_overriding_catalog_ids('search'):
            query._provider_query.match_repository_id(repository_id, match=True)
        return self._query_session.get_assets_by_query(query), query

    def _get_unauth_repository_ids(self, repository_id):
        if self._can('search', repository_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(repository_id)]
        if self._hierarchy_session.has_child_repositories(repository_id):
            for child_repository_id in self._hierarchy_session.get_child_repository_ids(repository_id):
                unauth_list = unauth_list + self._get_unauth_repository_ids(child_repository_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_repositories(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_repository_ids is None:
            self._unauth_repository_ids = self._get_unauth_repository_ids(self._qualifier_id)
        for repository_id in self._unauth_repository_ids:
            query._provider_query.match_repository_id(repository_id, match=False)
        return self._query_session.get_assets_by_query(query)

    class AssetQueryWrapper(QueryWrapper):
        """Wrapper for AssetQueries to override match_repository_id method"""

        def match_repository_id(self, repository_id, match=True):
            self._cat_id_args_list.append({'repository_id': repository_id, 'match': match})

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_search_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_repository_ids()))

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    def get_asset_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AssetQueryWrapper(self._provider_session.get_asset_query())

    asset_query = property(fget=get_asset_query)

    @raise_null_argument
    def get_assets_by_query(self, asset_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(asset_query, '_cat_id_args_list'):
            raise Unsupported('asset_query not from this session')
        for kwargs in asset_query._cat_id_args_list:
            if self._can('search', kwargs['repository_id']):
                asset_query._provider_query.match_repository_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_assets_by_query(asset_query)
        self._check_search_conditions()
        result = self._try_harder(asset_query)
        asset_query._provider_query.clear_repository_terms()
        return result

    def get_asset_content_query(self):
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self.AssetQueryWrapper(self._provider_session.get_asset_content_query())

    def get_asset_contents_by_query(self, asset_content_query):
        if not hasattr(asset_content_query, '_cat_id_args_list'):
            raise Unsupported('asset_content_query not from this session')
        for kwargs in asset_content_query._cat_id_args_list:
            if self._can('search', kwargs['repository_id']):
                asset_content_query._provider_query.match_repository_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_asset_contents_by_query(asset_content_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(asset_content_query)
            asset_content_query._provider_query.clear_repository_terms()
            return result


class AssetSearchSession(abc_repository_sessions.AssetSearchSession, AssetQuerySession):
    """Adapts underlying AssetSearchSession methodswith authorization checks."""

    def get_asset_search(self):
        """Pass through to provider AssetSearchSession.get_asset_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_asset_search()

    asset_search = property(fget=get_asset_search)

    def get_asset_search_order(self):
        raise Unimplemented()

    asset_search_order = property(fget=get_asset_search_order)

    @raise_null_argument
    def get_assets_by_search(self, asset_query, asset_search):
        """Pass through to provider AssetSearchSession.get_assets_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assets_by_search(asset_query, asset_search)

    @raise_null_argument
    def get_asset_query_from_inspector(self, asset_query_inspector):
        raise Unimplemented()


class AssetAdminSession(abc_repository_sessions.AssetAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AssetAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Asset'
        self._overriding_repository_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_asset_repository_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_asset_repository_session()
                self.get_repository_ids_by_asset = self._object_catalog_session.get_repository_ids_by_asset
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_repository_ids(self):
        if self._overriding_repository_ids is None:
            self._overriding_repository_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_repository_ids

    def _can_for_asset(self, func_name, asset_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, asset_id, 'get_repository_ids_for_asset')

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_create_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_asset_with_record_types(self, asset_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if asset_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_asset_form_for_create(self, asset_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_asset_form_for_create(asset_record_types)

    @raise_null_argument
    def create_asset(self, asset_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_asset(asset_form)

    def can_update_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_asset_form_for_update(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_asset('update', asset_id):
            raise PermissionDenied()
        return self._provider_session.get_asset_form_for_update(asset_id)

    def duplicate_asset(self, asset_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_asset(asset_id)

    @raise_null_argument
    def update_asset(self, asset_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_asset(asset_form)

    def can_delete_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_asset(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_asset('delete', asset_id):
            raise PermissionDenied()
        return self._provider_session.delete_asset(asset_id)

    def can_manage_asset_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_asset(self, asset_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_asset('alias', asset_id):
            raise PermissionDenied()
        return self._provider_session.alias_asset(asset_id, alias_id)

    def can_create_asset_content(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_asset_content_with_record_types(self, asset_content_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if asset_content_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_asset_content_form_for_create(self, asset_id, asset_content_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_asset_content_form_for_create(asset_id, asset_content_record_types)

    @raise_null_argument
    def create_asset_content(self, asset_content_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.create_asset_content_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_asset_content(asset_content_form)

    def can_update_asset_contents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_asset_content_form_for_update(self, asset_content_id):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_asset_content_form_for_update(asset_content_id)

    @raise_null_argument
    def update_asset_content(self, asset_content_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.update_asset_content_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_asset_content(asset_content_form)

    def can_delete_asset_contents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_asset_content(self, asset_content_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_asset_content_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_asset_content(asset_content_id)


class AssetNotificationSession(abc_repository_sessions.AssetNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AssetNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Asset'

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_register_for_asset_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    def register_for_new_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assets()

    @raise_null_argument
    def register_for_new_assets_by_genus_type(self, asset_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assets_by_genus_type()

    def register_for_changed_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assets()

    @raise_null_argument
    def register_for_changed_assets_by_genus_type(self, asset_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assets_by_genus_type(asset_genus_type)

    @raise_null_argument
    def register_for_changed_asset(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_asset(asset_id)

    def register_for_deleted_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assets()

    @raise_null_argument
    def register_for_deleted_assets_by_genus_type(self, asset_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assets_by_genus_type(asset_genus_type)

    @raise_null_argument
    def register_for_deleted_asset(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_asset(asset_id)

    def reliable_asset_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_asset_notifications()

    def unreliable_asset_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_asset_notifications()

    @raise_null_argument
    def acknowledge_asset_notification(self, notification_id):
        raise Unimplemented()


class AssetRepositorySession(abc_repository_sessions.AssetRepositorySession, osid_sessions.OsidSession):
    """Adapts underlying AssetRepositorySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'repository.AssetRepository'

    def can_lookup_asset_repository_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_repository_view()

    def use_plenary_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_repository_view()

    @raise_null_argument
    def get_asset_ids_by_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_asset_ids_by_repository(repository_id)

    @raise_null_argument
    def get_assets_by_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_asset_ids_by_repository(repository_id)

    @raise_null_argument
    def get_asset_ids_by_repositories(self, repository_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_asset_ids_by_repositories(repository_ids)

    @raise_null_argument
    def get_assets_by_repositories(self, repository_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assets_ids_by_repositories(repository_ids)

    @raise_null_argument
    def get_repository_ids_by_asset(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repository_ids_by_asset(asset_id)

    @raise_null_argument
    def get_repositories_by_asset(self, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repositories_by_asset(asset_id)


class AssetRepositoryAssignmentSession(abc_repository_sessions.AssetRepositoryAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssetRepositoryAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'repository.AssetRepository'

    def can_assign_assets(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_assets_to_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=repository_id)

    @raise_null_argument
    def get_assignable_repository_ids(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_repository_ids()

    @raise_null_argument
    def get_assignable_repository_ids_for_asset(self, repository_id, asset_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_repository_ids_for_asset(asset_id)

    @raise_null_argument
    def assign_asset_to_repository(self, asset_id, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_asset_to_repository(asset_id, repository_id)

    @raise_null_argument
    def unassign_asset_from_repository(self, asset_id, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_asset_from_repository(asset_id, repository_id)


class AssetSmartRepositorySession(abc_repository_sessions.AssetSmartRepositorySession, osid_sessions.OsidSession):
    """Adapts underlying AssetSmartRepositorySession methodswith authorization checks."""

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_manage_smart_repository(self):
        raise Unimplemented()

    def get_asset_query(self):
        raise Unimplemented()

    asset_query = property(fget=get_asset_query)

    def get_asset_search_order(self):
        raise Unimplemented()

    asset_search_order = property(fget=get_asset_search_order)

    @raise_null_argument
    def apply_asset_query(self, asset_query):
        raise Unimplemented()

    def inspect_asset_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_asset_sequencing(self, asset_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_query_from_inspector(self, asset_query_inspector):
        raise Unimplemented()


class AssetTemporalSession(abc_repository_sessions.AssetTemporalSession, osid_sessions.OsidSession):
    """Adapts underlying AssetTemporalSession methodswith authorization checks."""

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_temporal_coverage(self):
        raise Unimplemented()

    def use_comparative_asset_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_asset_view()

    def use_plenary_asset_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_asset_view()

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    @raise_null_argument
    def get_temporal_coverage(self, asset_id):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_ids_by_temporal_coverage(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_assets_by_temporal_coverage(self, from_, to):
        raise Unimplemented()


class AssetTemporalAssignmentSession(abc_repository_sessions.AssetTemporalAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssetTemporalAssignmentSession methodswith authorization checks."""

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_assign_temporal_coverage(self):
        raise Unimplemented()

    @raise_null_argument
    def add_temporal_coverage(self, asset_id, begin, end):
        raise Unimplemented()

    @raise_null_argument
    def remove_temporal_coverage(self, asset_id, begin, end):
        raise Unimplemented()


class AssetSpatialSession(abc_repository_sessions.AssetSpatialSession, osid_sessions.OsidSession):
    """Adapts underlying AssetSpatialSession methodswith authorization checks."""

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_spatial_coverage(self):
        raise Unimplemented()

    def use_comparative_asset_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_asset_view()

    def use_plenary_asset_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_asset_view()

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    @raise_null_argument
    def get_asset_location_ids(self, asset_id):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_locations(self, asset_id):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_spatial_coverage(self, asset_id):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_ids_by_location(self, location_id):
        raise Unimplemented()

    @raise_null_argument
    def get_assets_by_location(self, location_id):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_ids_by_spatial_coverage(self, spatial_unit):
        raise Unimplemented()

    @raise_null_argument
    def get_assets_by_spatial_coverage(self, spatial_unit):
        raise Unimplemented()


class AssetSpatialAssignmentSession(abc_repository_sessions.AssetSpatialAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssetSpatialAssignmentSession methodswith authorization checks."""

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_assign_spatial_coverage(self):
        raise Unimplemented()

    @raise_null_argument
    def add_asset_location(self, asset_id, location_id):
        raise Unimplemented()

    @raise_null_argument
    def add_asset_spatial_coverage(self, asset_id, spatial_unit):
        raise Unimplemented()

    @raise_null_argument
    def remove_asset_location(self, asset_id, location_id):
        raise Unimplemented()

    @raise_null_argument
    def remove_asset_spatial_coverage(self, asset_id, spatial_unit):
        raise Unimplemented()


class AssetCompositionSession(abc_repository_sessions.AssetCompositionSession, osid_sessions.OsidSession):
    """Adapts underlying AssetCompositionSession methodswith authorization checks."""
    def __init__(self, **kwargs):
        osid_sessions.OsidSession.__init__(self, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.AssetComposition'

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_access_asset_compositions(self):
        return self._can('access')

    def use_comparative_asset_composition_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_asset_composition_view()

    def use_plenary_asset_composition_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_asset_composition_view()

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    @raise_null_argument
    def get_composition_assets(self, composition_id):
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_composition_assets(composition_id)

    @raise_null_argument
    def get_compositions_by_asset(self, asset_id):
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_compositions_by_asset(asset_id)


class AssetCompositionDesignSession(abc_repository_sessions.AssetCompositionDesignSession, osid_sessions.OsidSession):
    """Adapts underlying AssetCompositionDesignSession methodswith authorization checks."""
    def __init__(self, **kwargs):
        osid_sessions.OsidSession.__init__(self, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.AssetComposition'

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_compose_assets(self):
        return self._can('compose')

    @raise_null_argument
    def add_asset(self, asset_id, composition_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.add_asset(asset_id, composition_id)

    @raise_null_argument
    def move_asset_ahead(self, asset_id, composition_id, reference_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.move_asset_ahead(asset_id, composition_id, reference_id)

    @raise_null_argument
    def move_asset_behind(self, asset_id, composition_id, reference_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.move_asset_behind(asset_id, composition_id, reference_id)

    @raise_null_argument
    def order_assets(self, asset_ids, composition_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.order_assets(asset_ids, composition_id)

    @raise_null_argument
    def remove_asset(self, asset_id, composition_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_asset(asset_id, composition_id)


class CompositionLookupSession(abc_repository_sessions.CompositionLookupSession, osid_sessions.OsidSession):
    """Adapts underlying CompositionLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Composition'
        self.use_federated_repository_view()
        self.use_comparative_composition_view()
        self._auth_repository_ids = None
        self._unauth_repository_ids = None
    #     self._overriding_repository_ids = None
    #
    # def _get_overriding_repository_ids(self):
    #     if self._overriding_repository_ids is None:
    #         self._overriding_repository_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_repository_ids

    def _try_overriding_repositories(self, query):
        for catalog_id in self._get_overriding_catalog_ids('lookup'):
            query.match_repository_id(catalog_id, match=True)
        return self._query_session.get_compositions_by_query(query), query

    def _get_unauth_repository_ids(self, repository_id):
        if self._can('lookup', repository_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(repository_id)]
        if self._hierarchy_session.has_child_repositories(repository_id):
            for child_repository_id in self._hierarchy_session.get_child_repository_ids(repository_id):
                unauth_list = unauth_list + self._get_unauth_repository_ids(child_repository_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_repositories(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_repository_ids is None:
            self._unauth_repository_ids = self._get_unauth_repository_ids(self._qualifier_id)
        for repository_id in self._unauth_repository_ids:
            query.match_repository_id(repository_id, match=False)
        return self._query_session.get_compositions_by_query(query)

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_lookup_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_composition_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_composition_view()

    def use_plenary_composition_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_composition_view()

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    def use_active_composition_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_active_composition_view
        return self._provider_session.use_active_composition_view()

    def use_any_status_composition_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_any_status_composition_view
        return self._provider_session.use_any_status_composition_view()

    def use_sequestered_composition_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_sequestered_composition_view_template
        return self._provider_session.use_sequestered_composition_view()

    def use_unsequestered_composition_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_unsequestered_composition_view_template
        return self._provider_session.use_unsequestered_composition_view()

    @raise_null_argument
    def get_composition(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_composition(composition_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_composition_query()
        query.match_id(composition_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_compositions_by_ids(self, composition_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_compositions_by_ids(composition_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_composition_query()
        for composition_id in (composition_ids):
            query.match_id(composition_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_compositions_by_genus_type(self, composition_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_compositions_by_genus_type(composition_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_composition_query()
        query.match_genus_type(composition_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_compositions_by_parent_genus_type(self, composition_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_compositions_by_parent_genus_type(composition_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_composition_query()
        query.match_parent_genus_type(composition_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_compositions_by_record_type(self, composition_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_compositions_by_record_type(composition_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_composition_query()
        query.match_record_type(composition_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_compositions_by_provider(self, resource_id):
        raise Unimplemented()

    def get_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_compositions()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_composition_query()
        query.match_any(match=True)
        return self._try_harder(query)

    compositions = property(fget=get_compositions)


class CompositionQuerySession(abc_repository_sessions.CompositionQuerySession, osid_sessions.OsidSession):
    """Adapts underlying CompositionQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Composition'
        self.use_federated_repository_view()
        self._unauth_repository_ids = None
        # self._overriding_repository_ids = None

    # def _get_overriding_repository_ids(self):
    #     if self._overriding_repository_ids is None:
    #         self._overriding_repository_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_repository_ids

    def _try_overriding_repositories(self, query):
        for repository_id in self._get_overriding_catalog_ids('search'):
            query._provider_query.match_repository_id(repository_id, match=True)
        return self._query_session.get_compositions_by_query(query), query

    def _get_unauth_repository_ids(self, repository_id):
        if self._can('search', repository_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(repository_id)]
        if self._hierarchy_session.has_child_repositories(repository_id):
            for child_repository_id in self._hierarchy_session.get_child_repository_ids(repository_id):
                unauth_list = unauth_list + self._get_unauth_repository_ids(child_repository_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_repositories(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_repository_ids is None:
            self._unauth_repository_ids = self._get_unauth_repository_ids(self._qualifier_id)
        for repository_id in self._unauth_repository_ids:
            query._provider_query.match_repository_id(repository_id, match=False)
        return self._query_session.get_compositions_by_query(query)

    class CompositionQueryWrapper(QueryWrapper):
        """Wrapper for CompositionQueries to override match_repository_id method"""

        def match_repository_id(self, repository_id, match=True):
            self._cat_id_args_list.append({'repository_id': repository_id, 'match': match})

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_search_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_repository_ids()))

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    def use_sequestered_composition_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_sequestered_composition_view_template
        return self._provider_session.use_sequestered_composition_view()

    def use_unsequestered_composition_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_unsequestered_composition_view_template
        return self._provider_session.use_unsequestered_composition_view()

    def get_composition_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.CompositionQueryWrapper(self._provider_session.get_composition_query())

    composition_query = property(fget=get_composition_query)

    @raise_null_argument
    def get_compositions_by_query(self, composition_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(composition_query, '_cat_id_args_list'):
            raise Unsupported('composition_query not from this session')
        for kwargs in composition_query._cat_id_args_list:
            if self._can('search', kwargs['repository_id']):
                composition_query._provider_query.match_repository_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_compositions_by_query(composition_query)
        self._check_search_conditions()
        result = self._try_harder(composition_query)
        composition_query._provider_query.clear_repository_terms()
        return result


class CompositionSearchSession(abc_repository_sessions.CompositionSearchSession, CompositionQuerySession):
    """Adapts underlying CompositionSearchSession methodswith authorization checks."""

    def get_composition_search(self):
        """Pass through to provider CompositionSearchSession.get_composition_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_composition_search()

    composition_search = property(fget=get_composition_search)

    def get_composition_search_order(self):
        raise Unimplemented()

    composition_search_order = property(fget=get_composition_search_order)

    @raise_null_argument
    def get_compositions_by_search(self, composition_query, composition_search):
        """Pass through to provider CompositionSearchSession.get_compositions_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_compositions_by_search(composition_query, composition_search)

    @raise_null_argument
    def get_composition_query_from_inspector(self, composition_query_inspector):
        raise Unimplemented()


class CompositionAdminSession(abc_repository_sessions.CompositionAdminSession, osid_sessions.OsidSession):
    """Adapts underlying CompositionAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Composition'
        self._overriding_repository_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_composition_repository_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_composition_repository_session()
                self.get_repository_ids_by_composition = self._object_catalog_session.get_repository_ids_by_composition
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_repository_ids(self):
        if self._overriding_repository_ids is None:
            self._overriding_repository_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_repository_ids

    def _can_for_composition(self, func_name, composition_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, composition_id, 'get_repository_ids_for_composition')

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_create_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_composition_with_record_types(self, composition_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if composition_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_composition_form_for_create(self, composition_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_composition_form_for_create(composition_record_types)

    @raise_null_argument
    def create_composition(self, composiiton_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_composition(composiiton_form)

    def can_update_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_composition_form_for_update(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_composition('update', composition_id):
            raise PermissionDenied()
        return self._provider_session.get_composition_form_for_update(composition_id)

    def duplicate_composition(self, composition_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_composition(composition_id)

    @raise_null_argument
    def update_composition(self, composiiton_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_composition(composiiton_form)

    def can_delete_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_composition(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_composition('delete', composition_id):
            raise PermissionDenied()
        return self._provider_session.delete_composition(composition_id)

    @raise_null_argument
    def delete_composition_node(self, composition_id):
        raise Unimplemented()

    @raise_null_argument
    def add_composition_child(self, composition_id, child_composition_id):
        raise Unimplemented()

    @raise_null_argument
    def remove_composition_child(self, composition_id, child_composition_id):
        raise Unimplemented()

    def can_manage_composition_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_composition(self, composition_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_composition('alias', composition_id):
            raise PermissionDenied()
        return self._provider_session.alias_composition(composition_id, alias_id)


class CompositionNotificationSession(abc_repository_sessions.CompositionNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying CompositionNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_repository_id()
        self._id_namespace = 'repository.Composition'

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_register_for_composition_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_repository_view()
        if self._query_session:
            self._query_session.use_federated_repository_view()

    def use_isolated_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_repository_view()
        if self._query_session:
            self._query_session.use_isolated_repository_view()

    def register_for_new_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_compositions()

    def register_for_changed_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_compositions()

    @raise_null_argument
    def register_for_changed_composition(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_composition(composition_id)

    def register_for_deleted_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_compositions()

    @raise_null_argument
    def register_for_deleted_composition(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_composition(composition_id)

    def reliable_composition_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_composition_notifications()

    def unreliable_composition_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_composition_notifications()

    @raise_null_argument
    def acknowledge_composition_notification(self, notification_id):
        raise Unimplemented()


class CompositionRepositorySession(abc_repository_sessions.CompositionRepositorySession, osid_sessions.OsidSession):
    """Adapts underlying CompositionRepositorySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'repository.CompositionRepository'

    def use_comparative_composition_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_composition_repository_view()

    def use_plenary_composition_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_composition_repository_view()

    def can_lookup_composition_repository_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    @raise_null_argument
    def get_composition_ids_by_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_composition_ids_by_repository(repository_id)

    @raise_null_argument
    def get_compositions_by_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_composition_ids_by_repository(repository_id)

    @raise_null_argument
    def get_composition_ids_by_repositories(self, repository_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_composition_ids_by_repositories(repository_ids)

    @raise_null_argument
    def get_compoitions_by_repositories(self, repository_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_compositions_ids_by_repositories(repository_ids)

    @raise_null_argument
    def get_repository_ids_by_composition(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repository_ids_by_composition(composition_id)

    @raise_null_argument
    def get_repositories_by_composition(self, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repositories_by_composition(composition_id)


class CompositionRepositoryAssignmentSession(abc_repository_sessions.CompositionRepositoryAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying CompositionRepositoryAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'repository.CompositionRepository'

    def can_assign_compositions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_compositions_to_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=repository_id)

    @raise_null_argument
    def get_assignable_repository_ids(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_repository_ids()

    @raise_null_argument
    def get_assignable_repository_ids_for_composition(self, repository_id, composition_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_repository_ids_for_composition(composition_id)

    @raise_null_argument
    def assign_composition_to_repository(self, composition_id, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_composition_to_repository(composition_id, repository_id)

    @raise_null_argument
    def unassign_composition_from_repository(self, composition_id, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_composition_from_repository(composition_id, repository_id)


class CompositionSmartRepositorySession(abc_repository_sessions.CompositionSmartRepositorySession, osid_sessions.OsidSession):
    """Adapts underlying CompositionSmartRepositorySession methodswith authorization checks."""

    def get_repository_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_repository()

    repository = property(fget=get_repository)

    def can_manage_smart_repository(self):
        raise Unimplemented()

    def get_composition_query(self):
        raise Unimplemented()

    composition_query = property(fget=get_composition_query)

    def get_composition_search_order(self):
        raise Unimplemented()

    composition_search_order = property(fget=get_composition_search_order)

    @raise_null_argument
    def apply_composition_query(self, composition_query):
        raise Unimplemented()

    def inspect_composition_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_composition_sequencing(self, composition_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_composition_query_from_inspector(self, composition_query_inspector):
        raise Unimplemented()


class RepositoryLookupSession(abc_repository_sessions.RepositoryLookupSession, osid_sessions.OsidSession):
    """Adapts underlying RepositoryLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'repository.Repository'

    def can_lookup_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_repository_view()

    def use_plenary_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_repository_view()

    @raise_null_argument
    def get_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repository(repository_id)

    @raise_null_argument
    def get_repositories_by_ids(self, repository_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repositories_by_ids(repository_ids)

    @raise_null_argument
    def get_repositories_by_genus_type(self, repository_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repositories_by_genus_type(repository_genus_type)

    @raise_null_argument
    def get_repositories_by_parent_genus_type(self, repository_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_repositories_by_record_type(self, repository_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_repositories_by_provider(self, resource_id):
        raise Unimplemented()

    def get_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_repositories()

    repositories = property(fget=get_repositories)


class RepositoryQuerySession(abc_repository_sessions.RepositoryQuerySession, osid_sessions.OsidSession):
    """Adapts underlying RepositoryQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'repository.Repository'

    def can_search_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_repository_ids()))

    def get_repository_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_repository_query()

    repository_query = property(fget=get_repository_query)

    @raise_null_argument
    def get_repositories_by_query(self, repository_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_repositories_by_query(repository_query)


class RepositorySearchSession(abc_repository_sessions.RepositorySearchSession, RepositoryQuerySession):
    """Adapts underlying RepositorySearchSession methodswith authorization checks."""

    def get_repository_search(self):
        raise Unimplemented()

    repository_search = property(fget=get_repository_search)

    def get_repository_search_order(self):
        raise Unimplemented()

    repository_search_order = property(fget=get_repository_search_order)

    @raise_null_argument
    def get_repositories_by_search(self, repository_query, repository_search):
        raise Unimplemented()

    @raise_null_argument
    def get_repository_query_from_inspector(self, repository_query_inspector):
        raise Unimplemented()


class RepositoryAdminSession(abc_repository_sessions.RepositoryAdminSession, osid_sessions.OsidSession):
    """Adapts underlying RepositoryAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'repository.Repository'

    def can_create_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_repository_with_record_types(self, repository_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if repository_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_repository_form_for_create(self, repository_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_repository_form_for_create(repository_record_types)

    @raise_null_argument
    def create_repository(self, repository_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_repository(repository_form)

    def can_update_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_repository_form_for_update(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_repository_form_for_update(repository_id)

    @raise_null_argument
    def update_repository(self, repository_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_repository(repository_form)

    def can_delete_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_repository(repository_id)

    def can_manage_repository_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_repository(self, repository_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_repository(repository_id, alias_id)


class RepositoryNotificationSession(abc_repository_sessions.RepositoryNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying RepositoryNotificationSession methodswith authorization checks."""

    def can_register_for_repository_notifications(self):
        raise Unimplemented()

    def register_for_new_repositories(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_new_repository_ancestors(self, repository_id):
        raise Unimplemented()

    @raise_null_argument
    def register_for_new_repository_descendants(self, repository_id):
        raise Unimplemented()

    def register_for_changed_repositories(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_repository(self, repository_id):
        raise Unimplemented()

    def register_for_deleted_repositories(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_repository(self, repository_id):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_repository_ancestors(self, repository_id):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_repository_descendants(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_repository_descendants(repository_id)

    def reliable_repository_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_repository_notifications()

    def unreliable_repository_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_repository_notifications()

    @raise_null_argument
    def acknowledge_repository_notification(self, notification_id):
        raise Unimplemented()


class RepositoryHierarchySession(abc_repository_sessions.RepositoryHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying RepositoryHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'repository.Repository'

    def get_repository_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_repository_hierarchy_id()

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_repository_hierarchy()

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_access_repository_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_repository_view()

    def use_plenary_repository_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_repository_view()

    def get_root_repository_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_repository_ids()

    root_repository_ids = property(fget=get_root_repository_ids)

    def get_root_repositories(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_repositories()

    root_repositories = property(fget=get_root_repositories)

    @raise_null_argument
    def has_parent_repositories(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_repositories(repository_id)

    @raise_null_argument
    def is_parent_of_repository(self, id_, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_repository(id_, repository_id)

    @raise_null_argument
    def get_parent_repository_ids(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_repository_ids(repository_id)

    @raise_null_argument
    def get_parent_repositories(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_repositories(repository_id)

    @raise_null_argument
    def is_ancestor_of_repository(self, id_, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_repository(id_, repository_id)

    @raise_null_argument
    def has_child_repositories(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_repositories(repository_id)

    @raise_null_argument
    def is_child_of_repository(self, id_, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_repository(id_, repository_id)

    @raise_null_argument
    def get_child_repository_ids(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_repository_ids(repository_id)

    @raise_null_argument
    def get_child_repositories(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_repositories(repository_id)

    @raise_null_argument
    def is_descendant_of_repository(self, id_, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_repository(id_, repository_id)

    @raise_null_argument
    def get_repository_node_ids(self, repository_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_repository_node_ids(
            repository_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_repository_nodes(self, repository_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_repository_nodes(
            repository_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class RepositoryHierarchyDesignSession(abc_repository_sessions.RepositoryHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying RepositoryHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('repository.Repository%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'repository.Repository'
        # should this be 'repository.RepositoryHierarchy' ?

    def get_repository_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_repository_hierarchy_id()

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_repository_hierarchy()

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_modify_repository_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_repository(repository_id)

    @raise_null_argument
    def remove_root_repository(self, repository_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_repository(repository_id)

    @raise_null_argument
    def add_child_repository(self, repository_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_repository(repository_id, child_id)

    @raise_null_argument
    def remove_child_repository(self, repository_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_repository(repository_id, child_id)

    @raise_null_argument
    def remove_child_repositories(self, repository_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_repositories(repository_id)
