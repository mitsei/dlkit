"""AuthZ Adapter implementations of commenting sessions."""
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
from dlkit.abstract_osid.commenting import sessions as abc_commenting_sessions


class CommentLookupSession(abc_commenting_sessions.CommentLookupSession, osid_sessions.OsidSession):
    """Adapts underlying CommentLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_book_id()
        self._id_namespace = 'commenting.Comment'
        self.use_federated_book_view()
        self.use_comparative_comment_view()
        self._auth_book_ids = None
        self._unauth_book_ids = None
    #     self._overriding_book_ids = None
    #
    # def _get_overriding_book_ids(self):
    #     if self._overriding_book_ids is None:
    #         self._overriding_book_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_book_ids

    def _try_overriding_books(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_book_id(catalog_id, match=True)
        return self._query_session.get_comments_by_query(query), query

    def _get_unauth_book_ids(self, book_id):
        if self._can('lookup', book_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(book_id)]
        if self._hierarchy_session.has_child_books(book_id):
            for child_book_id in self._hierarchy_session.get_child_book_ids(book_id):
                unauth_list = unauth_list + self._get_unauth_book_ids(child_book_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_books(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_book_ids is None:
            self._unauth_book_ids = self._get_unauth_book_ids(self._qualifier_id)
        for book_id in self._unauth_book_ids:
            query.match_book_id(book_id, match=False)
        return self._query_session.get_comments_by_query(query)

    def get_book_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_book()

    book = property(fget=get_book)

    def can_lookup_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_comment_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_comment_view()

    def use_plenary_comment_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_comment_view()

    def use_federated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_book_view()
        if self._query_session:
            self._query_session.use_federated_book_view()

    def use_isolated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_book_view()
        if self._query_session:
            self._query_session.use_isolated_book_view()

    def use_effective_comment_view(self):
        raise Unimplemented()

    def use_any_effective_comment_view(self):
        raise Unimplemented()

    @raise_null_argument
    def get_comment(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_comment(comment_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_id(comment_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_comments_by_ids(self, comment_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_comments_by_ids(comment_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        for comment_id in (comment_ids):
            query.match_id(comment_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_comments_by_genus_type(self, comment_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_comments_by_genus_type(comment_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_genus_type(comment_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_comments_by_parent_genus_type(self, comment_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_comments_by_parent_genus_type(comment_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_parent_genus_type(comment_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_comments_by_record_type(self, comment_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_comments_by_record_type(comment_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_record_type(comment_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_comments_on_date(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_by_genus_type_on_date(self, comment_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_for_commentor(self, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_for_commentor_on_date(self, resource_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_by_genus_type_for_commentor(self, resource_id, comment_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_by_genus_type_for_commentor_on_date(self, resource_id, comment_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_for_reference(self, reference_id):
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        if self._can('lookup'):
            return self._provider_session.get_comments_for_reference(reference_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_source_id(reference_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_comments_for_reference_on_date(self, reference_id, from_, to):
        """Pass through to provider CommentLookupSession.get_comments_for_reference_on_date"""
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        if self._can('lookup'):
            return self._provider_session.get_comments_for_reference_on_date(reference_id, from_, to)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_source_id(reference_id, match=True)
        query.match_date(from_, to, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_comments_by_genus_type_for_reference(self, reference_id, comment_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_by_genus_type_for_reference_on_date(self, reference_id, comment_genus_type, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_for_commentor_and_reference(self, resource_id, reference_id):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_for_commentor_and_reference_on_date(self, resource_id, reference_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_by_genus_type_for_commentor_and_reference(self, resource_id, reference_id, comment_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_comments_by_genus_type_for_commentor_and_reference_on_date(self, resource_id, reference_id, comment_genus_type, from_, to):
        raise Unimplemented()

    def get_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_comments()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_comment_query()
        query.match_any(match=True)
        return self._try_harder(query)

    comments = property(fget=get_comments)


class RatingLookupSession(abc_commenting_sessions.RatingLookupSession, osid_sessions.OsidSession):
    """Adapts underlying RatingLookupSession methodswith authorization checks."""

    def get_book_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_book()

    book = property(fget=get_book)

    def can_lookup_ratings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_comment_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_comment_view()

    def use_plenary_comment_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_comment_view()

    def use_federated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_book_view()
        if self._query_session:
            self._query_session.use_federated_book_view()

    def use_isolated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_book_view()
        if self._query_session:
            self._query_session.use_isolated_book_view()

    def get_cumulative_rating(self):
        raise Unimplemented()

    cumulative_rating = property(fget=get_cumulative_rating)

    @raise_null_argument
    def get_cumulative_rating_for_reference(self, reference_id):
        raise Unimplemented()

    @raise_null_argument
    def get_cumulative_rating_for_commentor(self, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_top_references(self, max_):
        raise Unimplemented()

    @raise_null_argument
    def get_references(self, grade_id):
        raise Unimplemented()


class CommentQuerySession(abc_commenting_sessions.CommentQuerySession, osid_sessions.OsidSession):
    """Adapts underlying CommentQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_book_id()
        self._id_namespace = 'commenting.Comment'
        self.use_federated_book_view()
        self._unauth_book_ids = None
        # self._overriding_book_ids = None

    # def _get_overriding_book_ids(self):
    #     if self._overriding_book_ids is None:
    #         self._overriding_book_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_book_ids

    def _try_overriding_books(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for book_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_book_id(book_id, match=True)
        return self._query_session.get_comments_by_query(query), query

    def _get_unauth_book_ids(self, book_id):
        if self._can('search', book_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(book_id)]
        if self._hierarchy_session.has_child_books(book_id):
            for child_book_id in self._hierarchy_session.get_child_book_ids(book_id):
                unauth_list = unauth_list + self._get_unauth_book_ids(child_book_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_books(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_book_ids is None:
            self._unauth_book_ids = self._get_unauth_book_ids(self._qualifier_id)
        for book_id in self._unauth_book_ids:
            query._provider_query.match_book_id(book_id, match=False)
        return self._query_session.get_comments_by_query(query)

    class CommentQueryWrapper(QueryWrapper):
        """Wrapper for CommentQueries to override match_book_id method"""

        def match_book_id(self, book_id, match=True):
            self._cat_id_args_list.append({'book_id': book_id, 'match': match})

    def get_book_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_book()

    book = property(fget=get_book)

    def can_search_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_book_view()
        if self._query_session:
            self._query_session.use_federated_book_view()

    def use_isolated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_book_view()
        if self._query_session:
            self._query_session.use_isolated_book_view()

    def get_comment_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.CommentQueryWrapper(self._provider_session.get_comment_query())

    comment_query = property(fget=get_comment_query)

    @raise_null_argument
    def get_comments_by_query(self, comment_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(comment_query, '_cat_id_args_list'):
            raise Unsupported('comment_query not from this session')
        for kwargs in comment_query._cat_id_args_list:
            if self._can('search', kwargs['book_id']):
                comment_query._provider_query.match_book_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_comments_by_query(comment_query)
        self._check_search_conditions()
        result = self._try_harder(comment_query)
        comment_query._provider_query.clear_book_terms()
        return result


class CommentSearchSession(abc_commenting_sessions.CommentSearchSession, CommentQuerySession):
    """Adapts underlying CommentSearchSession methodswith authorization checks."""

    def get_comment_search(self):
        """Pass through to provider CommentSearchSession.get_comment_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_comment_search()

    comment_search = property(fget=get_comment_search)

    def get_comment_search_order(self):
        raise Unimplemented()

    comment_search_order = property(fget=get_comment_search_order)

    @raise_null_argument
    def get_comments_by_search(self, comment_query, comment_search):
        """Pass through to provider CommentSearchSession.get_comments_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_comments_by_search(comment_query, comment_search)

    @raise_null_argument
    def get_comment_query_from_inspector(self, comment_query_inspector):
        raise Unimplemented()


class CommentAdminSession(abc_commenting_sessions.CommentAdminSession, osid_sessions.OsidSession):
    """Adapts underlying CommentAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_book_id()
        self._id_namespace = 'commenting.Comment'
        self._overriding_book_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_comment_book_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_comment_book_session()
                self.get_book_ids_by_comment = self._object_catalog_session.get_book_ids_by_comment
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_book_ids(self):
        if self._overriding_book_ids is None:
            self._overriding_book_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_book_ids

    def _can_for_comment(self, func_name, comment_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, comment_id, 'get_book_ids_for_comment')

    def get_book_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_book()

    book = property(fget=get_book)

    def can_create_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_comment_with_record_types(self, comment_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if comment_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_comment_form_for_create(self, reference_id, comment_record_types):
        # Implemented from azosid template for -
        # osid.repository.CommentAdminSession.get_comment_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_comment_form_for_create(reference_id, comment_record_types)

    @raise_null_argument
    def create_comment(self, comment_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_comment(comment_form)

    def can_update_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_comment_form_for_update(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_comment('update', comment_id):
            raise PermissionDenied()
        return self._provider_session.get_comment_form_for_update(comment_id)

    def duplicate_comment(self, comment_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_comment(comment_id)

    @raise_null_argument
    def update_comment(self, comment_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_comment(comment_form)

    def can_delete_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_comment(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_comment('delete', comment_id):
            raise PermissionDenied()
        return self._provider_session.delete_comment(comment_id)

    def can_manage_comment_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_comment(self, comment_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_comment('alias', comment_id):
            raise PermissionDenied()
        return self._provider_session.alias_comment(comment_id, alias_id)


class CommentNotificationSession(abc_commenting_sessions.CommentNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying CommentNotificationSession methodswith authorization checks."""

    def get_book_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_book()

    book = property(fget=get_book)

    def can_register_for_comment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_book_view()
        if self._query_session:
            self._query_session.use_federated_book_view()

    def use_isolated_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_book_view()
        if self._query_session:
            self._query_session.use_isolated_book_view()

    def reliable_comment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_comment_notifications()

    def unreliable_comment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_comment_notifications()

    @raise_null_argument
    def acknowledge_comment_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_comments()

    @raise_null_argument
    def register_for_new_comments_for_commentor(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_comments_for_commentor()

    @raise_null_argument
    def register_for_new_comments_for_reference(self, reference_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_comments_for_reference()

    def register_for_changed_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_comments()

    @raise_null_argument
    def register_for_changed_comments_for_commentor(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_comments_for_commentor(resource_id)

    @raise_null_argument
    def register_for_changed_comments_for_reference(self, reference_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_comments_for_reference(reference_id)

    @raise_null_argument
    def register_for_changed_comment(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_comment(comment_id)

    def register_for_deleted_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_comments()

    @raise_null_argument
    def register_for_deleted_comments_for_commentor(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_comments_for_commentor(resource_id)

    @raise_null_argument
    def register_for_deleted_comments_for_reference(self, reference_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_comments_for_reference(reference_id)

    @raise_null_argument
    def register_for_deleted_comment(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_comment(comment_id)

    def reliable_comment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_comment_notifications()

    def unreliable_comment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_comment_notifications()

    @raise_null_argument
    def acknowledge_comment_notification(self, notification_id):
        raise Unimplemented()


class CommentBookSession(abc_commenting_sessions.CommentBookSession, osid_sessions.OsidSession):
    """Adapts underlying CommentBookSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'commenting.CommentBook'

    def can_lookup_comment_book_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_book_view()

    def use_plenary_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_book_view()

    @raise_null_argument
    def get_comment_ids_by_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_comment_ids_by_book(book_id)

    @raise_null_argument
    def get_comments_by_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_comments_by_book(book_id)

    @raise_null_argument
    def get_comment_ids_by_books(self, book_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_comment_ids_by_books(book_ids)

    @raise_null_argument
    def get_comments_by_books(self, book_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_comments_by_books(book_ids)

    @raise_null_argument
    def get_book_ids_by_comment(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_book_ids_by_comment(comment_id)

    @raise_null_argument
    def get_books_by_comment(self, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_books_by_comment(comment_id)


class CommentBookAssignmentSession(abc_commenting_sessions.CommentBookAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying CommentBookAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'commenting.CommentBook'

    def can_assign_comments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_comments_to_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=book_id)

    @raise_null_argument
    def get_assignable_book_ids(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_book_ids(book_id)

    @raise_null_argument
    def get_assignable_book_ids_for_comment(self, book_id, comment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_book_ids_for_comment(book_id, comment_id)

    @raise_null_argument
    def assign_comment_to_book(self, comment_id, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_comment_to_book(comment_id, book_id)

    @raise_null_argument
    def unassign_comment_from_book(self, comment_id, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_comment_from_book(comment_id, book_id)

    @raise_null_argument
    def reassign_comment_to_book(self, comment_id, from_book_id, to_book_id):
        raise Unimplemented()


class CommentSmartBookSession(abc_commenting_sessions.CommentSmartBookSession, osid_sessions.OsidSession):
    """Adapts underlying CommentSmartBookSession methodswith authorization checks."""

    def get_book_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_book()

    book = property(fget=get_book)

    def can_manage_smart_books(self):
        raise Unimplemented()

    def get_comment_query(self):
        raise Unimplemented()

    comment_query = property(fget=get_comment_query)

    def get_comment_search_order(self):
        raise Unimplemented()

    comment_search_order = property(fget=get_comment_search_order)

    @raise_null_argument
    def apply_comment_query(self, comment_query):
        raise Unimplemented()

    def inspect_comment_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_comment_sequencing(self, comment_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_comment_query_from_inspector(self, comment_query_inspector):
        raise Unimplemented()


class BookLookupSession(abc_commenting_sessions.BookLookupSession, osid_sessions.OsidSession):
    """Adapts underlying BookLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'commenting.Book'

    def can_lookup_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_book_view()

    def use_plenary_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_book_view()

    @raise_null_argument
    def get_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_book(book_id)

    @raise_null_argument
    def get_books_by_ids(self, book_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_books_by_ids(book_ids)

    @raise_null_argument
    def get_books_by_genus_type(self, book_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_books_by_genus_type(book_genus_type)

    @raise_null_argument
    def get_books_by_parent_genus_type(self, book_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_books_by_record_type(self, book_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_books_by_provider(self, resource_id):
        raise Unimplemented()

    def get_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_books()

    books = property(fget=get_books)


class BookQuerySession(abc_commenting_sessions.BookQuerySession, osid_sessions.OsidSession):
    """Adapts underlying BookQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'commenting.Book'

    def can_search_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.can_search_bins_template
        return self._can('search')

    def get_book_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_book_query()

    book_query = property(fget=get_book_query)

    @raise_null_argument
    def get_books_by_query(self, book_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_books_by_query(book_query)


class BookSearchSession(abc_commenting_sessions.BookSearchSession, BookQuerySession):
    """Adapts underlying BookSearchSession methodswith authorization checks."""

    def get_book_search(self):
        raise Unimplemented()

    book_search = property(fget=get_book_search)

    def get_book_search_order(self):
        raise Unimplemented()

    book_search_order = property(fget=get_book_search_order)

    @raise_null_argument
    def get_books_by_search(self, book_query, book_search):
        raise Unimplemented()

    @raise_null_argument
    def get_book_query_from_inspector(self, book_query_inspector):
        raise Unimplemented()


class BookAdminSession(abc_commenting_sessions.BookAdminSession, osid_sessions.OsidSession):
    """Adapts underlying BookAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'commenting.Book'

    def can_create_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_book_with_record_types(self, book_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if book_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_book_form_for_create(self, book_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_book_form_for_create(book_record_types)

    @raise_null_argument
    def create_book(self, book_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_book(book_form)

    def can_update_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_book_form_for_update(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_book_form_for_update(book_id)

    @raise_null_argument
    def update_book(self, book_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_book(book_form)

    def can_delete_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_book(book_id)

    def can_manage_book_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_book(self, book_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_book(book_id, alias_id)


class BookNotificationSession(abc_commenting_sessions.BookNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying BookNotificationSession methodswith authorization checks."""

    def can_register_for_book_notifications(self):
        raise Unimplemented()

    def reliable_book_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_book_notifications()

    def unreliable_book_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_book_notifications()

    @raise_null_argument
    def acknowledge_book_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_books(self):
        raise Unimplemented()

    def register_for_changed_books(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_book(self, book_id):
        raise Unimplemented()

    def register_for_deleted_books(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_book(self, book_id):
        raise Unimplemented()

    def register_for_changed_book_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_book_hierarchy()

    @raise_null_argument
    def register_for_changed_book_hierarchy_for_ancestors(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_book_hierarchy_for_ancestors(book_id)

    @raise_null_argument
    def register_for_changed_book_hierarchy_for_descendants(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_book_hierarchy_for_descendants(book_id)

    def reliable_book_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_book_notifications()

    def unreliable_book_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_book_notifications()

    @raise_null_argument
    def acknowledge_book_notification(self, notification_id):
        raise Unimplemented()


class BookHierarchySession(abc_commenting_sessions.BookHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying BookHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'commenting.Book'

    def get_book_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_book_hierarchy_id()

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_book_hierarchy()

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_access_book_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_book_view()

    def use_plenary_book_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_book_view()

    def get_root_book_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_book_ids()

    root_book_ids = property(fget=get_root_book_ids)

    def get_root_books(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_books()

    root_books = property(fget=get_root_books)

    @raise_null_argument
    def has_parent_books(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_books(book_id)

    @raise_null_argument
    def is_parent_of_book(self, id_, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_book(id_, book_id)

    @raise_null_argument
    def get_parent_book_ids(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_book_ids(book_id)

    @raise_null_argument
    def get_parent_books(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_books(book_id)

    @raise_null_argument
    def is_ancestor_of_book(self, id_, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_book(id_, book_id)

    @raise_null_argument
    def has_child_books(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_books(book_id)

    @raise_null_argument
    def is_child_of_book(self, id_, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_book(id_, book_id)

    @raise_null_argument
    def get_child_book_ids(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_book_ids(book_id)

    @raise_null_argument
    def get_child_books(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_books(book_id)

    @raise_null_argument
    def is_descendant_of_book(self, id_, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_book(id_, book_id)

    @raise_null_argument
    def get_book_node_ids(self, book_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_book_node_ids(
            book_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_book_nodes(self, book_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_book_nodes(
            book_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class BookHierarchyDesignSession(abc_commenting_sessions.BookHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying BookHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'commenting.Book'
        # should this be 'commenting.BookHierarchy' ?

    def get_book_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_book_hierarchy_id()

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_book_hierarchy()

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_modify_book_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_book(book_id)

    @raise_null_argument
    def remove_root_book(self, book_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_book(book_id)

    @raise_null_argument
    def add_child_book(self, book_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_book(book_id, child_id)

    @raise_null_argument
    def remove_child_book(self, book_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_book(book_id, child_id)

    @raise_null_argument
    def remove_child_books(self, book_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_books(book_id)
