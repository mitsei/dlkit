"""AuthZ Adapter implementations of commenting managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from ..osid.osid_errors import Unimplemented, OperationFailed
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.commenting import managers as commenting_managers


class CommentingProfile(osid_managers.OsidProfile, commenting_managers.CommentingProfile):
    """Adapts underlying CommentingProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_book_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_book_hierarchy_session()
        except Unimplemented:
            return None

    def supports_comment_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_comment_lookup()

    def supports_comment_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_comment_query()

    def supports_comment_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_comment_admin()

    def supports_book_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_book_lookup()

    def supports_book_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_book_admin()

    def supports_book_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_book_hierarchy()

    def supports_book_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_book_hierarchy_design()

    def get_comment_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_comment_record_types()

    comment_record_types = property(fget=get_comment_record_types)

    def get_comment_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_comment_search_record_types()

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def get_book_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_book_record_types()

    book_record_types = property(fget=get_book_record_types)

    def get_book_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_book_search_record_types()

    book_search_record_types = property(fget=get_book_search_record_types)


class CommentingManager(osid_managers.OsidManager, CommentingProfile, commenting_managers.CommentingManager):
    """Adapts underlying CommentingManager methodswith authorization checks."""
    def __init__(self):
        CommentingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:commentingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('COMMENTING', provider_impl)
        # need to add version argument

    def get_comment_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_comment_query_session()
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentLookupSession')(
                provider_session=self._provider_manager.get_comment_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    comment_lookup_session = property(fget=get_comment_lookup_session)

    @raise_null_argument
    def get_comment_lookup_session_for_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_comment_query_session_for_book(book_id)
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentLookupSession')(
                provider_session=self._provider_manager.get_comment_lookup_session_for_book(book_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_comment_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_comment_query_session()
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentQuerySession')(
                provider_session=self._provider_manager.get_comment_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    comment_query_session = property(fget=get_comment_query_session)

    @raise_null_argument
    def get_comment_query_session_for_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_comment_query_session_for_book(book_id)
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentQuerySession')(
                provider_session=self._provider_manager.get_comment_query_session_for_book(book_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_comment_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CommentAdminSession')(
                provider_session=self._provider_manager.get_comment_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    comment_admin_session = property(fget=get_comment_admin_session)

    @raise_null_argument
    def get_comment_admin_session_for_book(self, book_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'CommentAdminSession')(
                provider_session=self._provider_manager.get_comment_admin_session_for_book(book_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_book_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookLookupSession')(
                provider_session=self._provider_manager.get_book_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    book_lookup_session = property(fget=get_book_lookup_session)

    def get_book_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookAdminSession')(
                provider_session=self._provider_manager.get_book_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    book_admin_session = property(fget=get_book_admin_session)

    def get_book_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookHierarchySession')(
                provider_session=self._provider_manager.get_book_hierarchy_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    def get_book_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookHierarchyDesignSession')(
                provider_session=self._provider_manager.get_book_hierarchy_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    def get_commenting_batch_manager(self):
        raise Unimplemented()

    commenting_batch_manager = property(fget=get_commenting_batch_manager)


class CommentingProxyManager(osid_managers.OsidProxyManager, CommentingProfile, commenting_managers.CommentingProxyManager):
    """Adapts underlying CommentingProxyManager methodswith authorization checks."""
    def __init__(self):
        CommentingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:commentingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('COMMENTING', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_comment_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_comment_query_session(proxy)
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentLookupSession')(
                provider_session=self._provider_manager.get_comment_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_comment_lookup_session_for_book(self, book_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_comment_query_session_for_book(book_id, proxy)
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentLookupSession')(
                provider_session=self._provider_manager.get_comment_lookup_session_for_book(book_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_comment_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_comment_query_session(proxy)
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentQuerySession')(
                provider_session=self._provider_manager.get_comment_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_comment_query_session_for_book(self, book_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_comment_query_session_for_book(book_id, proxy)
            query_session.use_federated_book_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CommentQuerySession')(
                provider_session=self._provider_manager.get_comment_query_session_for_book(book_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_comment_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CommentAdminSession')(
                provider_session=self._provider_manager.get_comment_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_comment_admin_session_for_book(self, book_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'CommentAdminSession')(
                provider_session=self._provider_manager.get_comment_admin_session_for_book(book_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_book_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookLookupSession')(
                provider_session=self._provider_manager.get_book_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_book_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookAdminSession')(
                provider_session=self._provider_manager.get_book_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_book_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookHierarchySession')(
                provider_session=self._provider_manager.get_book_hierarchy_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_book_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BookHierarchyDesignSession')(
                provider_session=self._provider_manager.get_book_hierarchy_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_commenting_batch_proxy_manager(self):
        raise Unimplemented()

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)
