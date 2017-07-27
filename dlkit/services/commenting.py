"""DLKit Services implementations of commenting service."""
# pylint: disable=no-init
#     osid specification includes some 'marker' interfaces.
# pylint: disable=too-many-ancestors
#     number of ancestors defined in spec.
# pylint: disable=too-few-public-methods,too-many-public-methods
#     number of methods defined in spec. Worse yet, these are aggregates.
# pylint: disable=invalid-name
#     method and class names defined in spec.
# pylint: disable=no-self-use,unused-argument
#     to catch unimplemented methods.
# pylint: disable=super-init-not-called
#     it just isn't.


from . import osid
from .osid_errors import Unimplemented, IllegalState, InvalidArgument
from dlkit.abstract_osid.commenting import objects as abc_commenting_objects
from dlkit.manager_impls.commenting import managers as commenting_managers


DEFAULT = 0
COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
ANY_STATUS = 0
ACTIVE = 1
UNSEQUESTERED = 0
SEQUESTERED = 1
AUTOMATIC = 0
MANDATORY = 1
DISABLED = -1


class CommentingProfile(osid.OsidProfile, commenting_managers.CommentingProfile):
    """CommentingProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_comment_lookup(self):
        """Pass through to provider supports_comment_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_comment_lookup()

    def supports_comment_query(self):
        """Pass through to provider supports_comment_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_comment_query()

    def supports_comment_admin(self):
        """Pass through to provider supports_comment_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_comment_admin()

    def supports_book_lookup(self):
        """Pass through to provider supports_book_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_book_lookup()

    def supports_book_admin(self):
        """Pass through to provider supports_book_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_book_admin()

    def supports_book_hierarchy(self):
        """Pass through to provider supports_book_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_book_hierarchy()

    def supports_book_hierarchy_design(self):
        """Pass through to provider supports_book_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_book_hierarchy_design()

    def get_comment_record_types(self):
        """Pass through to provider get_comment_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_comment_record_types()

    comment_record_types = property(fget=get_comment_record_types)

    def get_comment_search_record_types(self):
        """Pass through to provider get_comment_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_comment_search_record_types()

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def get_book_record_types(self):
        """Pass through to provider get_book_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_book_record_types()

    book_record_types = property(fget=get_book_record_types)

    def get_book_search_record_types(self):
        """Pass through to provider get_book_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_book_search_record_types()

    book_search_record_types = property(fget=get_book_search_record_types)


class CommentingManager(osid.OsidManager, osid.OsidSession, CommentingProfile, commenting_managers.CommentingManager):
    """CommentingManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._book_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_book_view(self, session):
        """Sets the underlying book view to match current view"""
        if self._book_view == COMPARATIVE:
            try:
                session.use_comparative_book_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_book_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_book_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:commentingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('COMMENTING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('COMMENTING', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

    def get_comment_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_comment_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_comment_lookup_session(*args, **kwargs)

    comment_lookup_session = property(fget=get_comment_lookup_session)

    def get_comment_lookup_session_for_book(self, *args, **kwargs):
        """Pass through to provider get_comment_lookup_session_for_book"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_comment_lookup_session_for_book(*args, **kwargs)

    def get_comment_query_session(self, *args, **kwargs):
        """Pass through to provider get_comment_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_comment_query_session(*args, **kwargs)

    comment_query_session = property(fget=get_comment_query_session)

    def get_comment_query_session_for_book(self, *args, **kwargs):
        """Pass through to provider get_comment_query_session_for_book"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_comment_query_session_for_book(*args, **kwargs)

    def get_comment_admin_session(self, *args, **kwargs):
        """Pass through to provider get_comment_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_comment_admin_session(*args, **kwargs)

    comment_admin_session = property(fget=get_comment_admin_session)

    def get_comment_admin_session_for_book(self, *args, **kwargs):
        """Pass through to provider get_comment_admin_session_for_book"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_comment_admin_session_for_book(*args, **kwargs)

    def get_book_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_book_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_book_lookup_session(*args, **kwargs)

    book_lookup_session = property(fget=get_book_lookup_session)

    def get_book_admin_session(self, *args, **kwargs):
        """Pass through to provider get_book_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_book_admin_session(*args, **kwargs)

    book_admin_session = property(fget=get_book_admin_session)

    def get_book_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_book_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_book_hierarchy_session(*args, **kwargs)

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    def get_book_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_book_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_book_hierarchy_design_session(*args, **kwargs)

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    def get_commenting_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    commenting_batch_manager = property(fget=get_commenting_batch_manager)
##
# The following methods are from osid.commenting.BookLookupSession

    def can_lookup_books(self):
        """Pass through to provider BookLookupSession.can_lookup_books"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('book_lookup_session').can_lookup_books()

    def use_comparative_book_view(self):
        """Pass through to provider BookLookupSession.use_comparative_book_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._book_view = COMPARATIVE
        # self._get_provider_session('book_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_book_view()
            except AttributeError:
                pass

    def use_plenary_book_view(self):
        """Pass through to provider BookLookupSession.use_plenary_book_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._book_view = PLENARY
        # self._get_provider_session('book_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_book_view()
            except AttributeError:
                pass

    def get_book(self, *args, **kwargs):
        """Pass through to provider BookLookupSession.get_book"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return Book(
            self._provider_manager,
            self._get_provider_session('book_lookup_session').get_book(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_books_by_ids(self, *args, **kwargs):
        """Pass through to provider BookLookupSession.get_books_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('book_lookup_session').get_books_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Book(self._provider_manager, cat, self._runtime, self._proxy))
        return BookList(cat_list)

    def get_books_by_genus_type(self, *args, **kwargs):
        """Pass through to provider BookLookupSession.get_books_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('book_lookup_session').get_books_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Book(self._provider_manager, cat, self._runtime, self._proxy))
        return BookList(cat_list)

    def get_books_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider BookLookupSession.get_books_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('book_lookup_session').get_books_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Book(self._provider_manager, cat, self._runtime, self._proxy))
        return BookList(cat_list)

    def get_books_by_record_type(self, *args, **kwargs):
        """Pass through to provider BookLookupSession.get_books_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('book_lookup_session').get_books_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Book(self._provider_manager, cat, self._runtime, self._proxy))
        return BookList(cat_list)

    def get_books_by_provider(self, *args, **kwargs):
        """Pass through to provider BookLookupSession.get_books_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('book_lookup_session').get_books_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Book(self._provider_manager, cat, self._runtime, self._proxy))
        return BookList(cat_list)

    def get_books(self):
        """Pass through to provider BookLookupSession.get_books"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
        catalogs = self._get_provider_session('book_lookup_session').get_books()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Book(self._provider_manager, cat, self._runtime, self._proxy))
        return BookList(cat_list)

    books = property(fget=get_books)
##
# The following methods are from osid.commenting.BookAdminSession

    def can_create_books(self):
        """Pass through to provider BookAdminSession.can_create_books"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('book_admin_session').can_create_books()

    def can_create_book_with_record_types(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.can_create_book_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('book_admin_session').can_create_book_with_record_types(*args, **kwargs)

    def get_book_form_for_create(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.get_book_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('book_admin_session').get_book_form_for_create(*args, **kwargs)

    def create_book(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.create_book"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return Book(
            self._provider_manager,
            self._get_provider_session('book_admin_session').create_book(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_books(self):
        """Pass through to provider BookAdminSession.can_update_books"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('book_admin_session').can_update_books()

    def get_book_form_for_update(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.get_book_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('book_admin_session').get_book_form_for_update(*args, **kwargs)

    def update_book(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.update_book"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return Book(
            self._provider_manager,
            self._get_provider_session('book_admin_session').update_book(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_books(self):
        """Pass through to provider BookAdminSession.can_delete_books"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('book_admin_session').can_delete_books()

    def delete_book(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.delete_book"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.delete_catalog
        self._get_provider_session('book_admin_session').delete_book(*args, **kwargs)

    def can_manage_book_aliases(self):
        """Pass through to provider BookAdminSession.can_manage_book_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('book_admin_session').can_manage_book_aliases()

    def alias_book(self, *args, **kwargs):
        """Pass through to provider BookAdminSession.alias_book"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('book_admin_session').alias_book(*args, **kwargs)
##
# The following methods are from osid.commenting.BookHierarchySession

    def get_book_hierarchy_id(self):
        """Pass through to provider BookHierarchySession.get_book_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('book_hierarchy_session').get_book_hierarchy_id()

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Pass through to provider BookHierarchySession.get_book_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('book_hierarchy_session').get_book_hierarchy()

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_access_book_hierarchy(self):
        """Pass through to provider BookHierarchySession.can_access_book_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('book_hierarchy_session').can_access_book_hierarchy()

    def get_root_book_ids(self):
        """Pass through to provider BookHierarchySession.get_root_book_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('book_hierarchy_session').get_root_book_ids()

    root_book_ids = property(fget=get_root_book_ids)

    def get_root_books(self):
        """Pass through to provider BookHierarchySession.get_root_books"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('book_hierarchy_session').get_root_books()

    root_books = property(fget=get_root_books)

    def has_parent_books(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.has_parent_books"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('book_hierarchy_session').has_parent_books(*args, **kwargs)

    def is_parent_of_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.is_parent_of_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('book_hierarchy_session').is_parent_of_book(*args, **kwargs)

    def get_parent_book_ids(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.get_parent_book_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('book_hierarchy_session').get_parent_book_ids(*args, **kwargs)

    def get_parent_books(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.get_parent_books"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('book_hierarchy_session').get_parent_books(*args, **kwargs)

    def is_ancestor_of_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.is_ancestor_of_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('book_hierarchy_session').is_ancestor_of_book(*args, **kwargs)

    def has_child_books(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.has_child_books"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('book_hierarchy_session').has_child_books(*args, **kwargs)

    def is_child_of_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.is_child_of_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('book_hierarchy_session').is_child_of_book(*args, **kwargs)

    def get_child_book_ids(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.get_child_book_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('book_hierarchy_session').get_child_book_ids(*args, **kwargs)

    def get_child_books(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.get_child_books"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('book_hierarchy_session').get_child_books(*args, **kwargs)

    def is_descendant_of_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.is_descendant_of_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('book_hierarchy_session').is_descendant_of_book(*args, **kwargs)

    def get_book_node_ids(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.get_book_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('book_hierarchy_session').get_book_node_ids(*args, **kwargs)

    def get_book_nodes(self, *args, **kwargs):
        """Pass through to provider BookHierarchySession.get_book_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('book_hierarchy_session').get_book_nodes(*args, **kwargs)
##
# The following methods are from osid.commenting.BookHierarchyDesignSession

    def can_modify_book_hierarchy(self):
        """Pass through to provider BookHierarchyDesignSession.can_modify_book_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('book_hierarchy_design_session').can_modify_book_hierarchy()

    def add_root_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchyDesignSession.add_root_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('book_hierarchy_design_session').add_root_book(*args, **kwargs)

    def remove_root_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchyDesignSession.remove_root_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('book_hierarchy_design_session').remove_root_book(*args, **kwargs)

    def add_child_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchyDesignSession.add_child_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('book_hierarchy_design_session').add_child_book(*args, **kwargs)

    def remove_child_book(self, *args, **kwargs):
        """Pass through to provider BookHierarchyDesignSession.remove_child_book"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('book_hierarchy_design_session').remove_child_book(*args, **kwargs)

    def remove_child_books(self, *args, **kwargs):
        """Pass through to provider BookHierarchyDesignSession.remove_child_books"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('book_hierarchy_design_session').remove_child_books(*args, **kwargs)


class CommentingProxyManager(osid.OsidProxyManager, CommentingProfile, CommentingManager, commenting_managers.CommentingProxyManager):
    """CommentingProxyManager convenience adapter including related Session methods."""
    pass


class Book(abc_commenting_objects.Book, osid.OsidSession, osid.OsidCatalog):
    """Book convenience adapter including related Session methods."""
    # Built from: templates/osid_catalog.GenericCatalog.init_template
    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, runtime, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        self._runtime = runtime
        osid.OsidObject.__init__(self, self._catalog)  # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy)  # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._book_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_book_view(self, session):
        """Sets the underlying book view to match current view"""
        if self._book_view == FEDERATED:
            try:
                session.use_federated_book_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_book_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_operable_view(self, session):
        """Sets the underlying operable views to match current view"""
        for obj_name in self._operable_views:
            if self._operable_views[obj_name] == ACTIVE:
                try:
                    getattr(session, 'use_active_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_any_status_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_containable_view(self, session):
        """Sets the underlying containable views to match current view"""
        for obj_name in self._containable_views:
            if self._containable_views[obj_name] == SEQUESTERED:
                try:
                    getattr(session, 'use_sequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_unsequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session.

        Instantiates a new one if the named session is not already known.

        """
        agent_key = self._get_agent_key()
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_book')
            if self._proxy is None:
                if 'notification_session' in session_name:
                    # Is there something else we should do about the receiver field?
                    session = session_class('fake receiver', self._catalog.get_id())
                else:
                    session = session_class(self._catalog.get_id())
            else:
                if 'notification_session' in session_name:
                    # Is there something else we should do about the receiver field?
                    session = session_class('fake receiver', self._catalog.get_id(), self._proxy)
                else:
                    session = session_class(self._catalog.get_id(), self._proxy)
            self._set_book_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_book_id(self):
        """Gets the Id of this book."""
        return self._catalog_id

    def get_book(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        else:
            raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

    def get_book_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.commenting.CommentLookupSession

    def get_book_id(self):
        """Pass through to provider CommentLookupSession.get_book_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('comment_lookup_session').get_book_id()

    book_id = property(fget=get_book_id)

    def get_book(self):
        """Pass through to provider CommentLookupSession.get_book"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return Book(
            self._provider_manager,
            self._get_provider_session('comment_lookup_session').get_book(*args, **kwargs),
            self._runtime,
            self._proxy)

    book = property(fget=get_book)

    def can_lookup_comments(self):
        """Pass through to provider CommentLookupSession.can_lookup_comments"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('comment_lookup_session').can_lookup_comments()

    def use_comparative_comment_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider CommentLookupSession.use_comparative_comment_view"""
        self._object_views['comment'] = COMPARATIVE
        # self._get_provider_session('comment_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_comment_view()
            except AttributeError:
                pass

    def use_plenary_comment_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider CommentLookupSession.use_plenary_comment_view"""
        self._object_views['comment'] = PLENARY
        # self._get_provider_session('comment_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_comment_view()
            except AttributeError:
                pass

    def use_federated_book_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_federated_catalog_view
        """Pass through to provider CommentLookupSession.use_federated_book_view"""
        self._book_view = FEDERATED
        # self._get_provider_session('comment_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_book_view()
            except AttributeError:
                pass

    def use_isolated_book_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_isolated_catalog_view
        """Pass through to provider CommentLookupSession.use_isolated_book_view"""
        self._book_view = ISOLATED
        # self._get_provider_session('comment_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_book_view()
            except AttributeError:
                pass

    def use_effective_comment_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_any_effective_comment_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_comment(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comment"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('comment_lookup_session').get_comment(*args, **kwargs)

    def get_comments_by_ids(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('comment_lookup_session').get_comments_by_ids(*args, **kwargs)

    def get_comments_by_genus_type(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('comment_lookup_session').get_comments_by_genus_type(*args, **kwargs)

    def get_comments_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('comment_lookup_session').get_comments_by_parent_genus_type(*args, **kwargs)

    def get_comments_by_record_type(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('comment_lookup_session').get_comments_by_record_type(*args, **kwargs)

    def get_comments_on_date(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_on_date
        return self._get_provider_session('comment_lookup_session').get_comments_on_date(*args, **kwargs)

    def get_comments_by_genus_type_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_comments_for_commentor(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_for_commentor"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination
        return self._get_provider_session('comment_lookup_session').get_comments_for_commentor(*args, **kwargs)

    def get_comments_for_commentor_on_date(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_for_commentor_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination_on_date
        return self._get_provider_session('comment_lookup_session').get_comments_for_commentor_on_date(*args, **kwargs)

    def get_comments_by_genus_type_for_commentor(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_genus_type_for_commentor"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_destination
        return self._get_provider_session('comment_lookup_session').get_comments_by_genus_type_for_commentor(*args, **kwargs)

    def get_comments_by_genus_type_for_commentor_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_comments_for_reference(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_for_reference"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source
        return self._get_provider_session('comment_lookup_session').get_comments_for_reference(*args, **kwargs)

    def get_comments_for_reference_on_date(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_for_reference_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source_on_date
        return self._get_provider_session('comment_lookup_session').get_comments_for_reference_on_date(*args, **kwargs)

    def get_comments_by_genus_type_for_reference(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_genus_type_for_reference"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_source
        return self._get_provider_session('comment_lookup_session').get_comments_by_genus_type_for_reference(*args, **kwargs)

    def get_comments_by_genus_type_for_reference_on_date(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_genus_type_for_reference_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date
        return self._get_provider_session('comment_lookup_session').get_comments_by_genus_type_for_reference_on_date(*args, **kwargs)

    def get_comments_for_commentor_and_reference(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_for_commentor_and_reference"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_peers
        return self._get_provider_session('comment_lookup_session').get_comments_for_commentor_and_reference(*args, **kwargs)

    def get_comments_for_commentor_and_reference_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_comments_by_genus_type_for_commentor_and_reference(self, *args, **kwargs):
        """Pass through to provider CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_peers
        return self._get_provider_session('comment_lookup_session').get_comments_by_genus_type_for_commentor_and_reference(*args, **kwargs)

    def get_comments_by_genus_type_for_commentor_and_reference_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_comments(self):
        """Pass through to provider CommentLookupSession.get_comments"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('comment_lookup_session').get_comments()

    comments = property(fget=get_comments)
##
# The following methods are from osid.commenting.CommentQuerySession

    def can_search_comments(self):
        """Pass through to provider CommentQuerySession.can_search_comments"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('comment_query_session').can_search_comments()

    def get_comment_query(self):
        """Pass through to provider CommentQuerySession.get_comment_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('comment_query_session').get_comment_query()

    comment_query = property(fget=get_comment_query)

    def get_comments_by_query(self, *args, **kwargs):
        """Pass through to provider CommentQuerySession.get_comments_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('comment_query_session').get_comments_by_query(*args, **kwargs)
##
# The following methods are from osid.commenting.CommentAdminSession

    def can_create_comments(self):
        """Pass through to provider CommentAdminSession.can_create_comments"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('comment_admin_session').can_create_comments()

    def can_create_comment_with_record_types(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.can_create_comment_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('comment_admin_session').can_create_comment_with_record_types(*args, **kwargs)

    def get_comment_form_for_create(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.get_comment_form_for_create"""
        # Built from: templates/osid_session.GenericRelationshipAdminSession.get_relationship_form_for_create_for_agent
        return self._get_provider_session('comment_admin_session').get_comment_form_for_create(*args, **kwargs)

    def create_comment(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.create_comment"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('comment_admin_session').create_comment(*args, **kwargs)

    def can_update_comments(self):
        """Pass through to provider CommentAdminSession.can_update_comments"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('comment_admin_session').can_update_comments()

    def get_comment_form_for_update(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.get_comment_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('comment_admin_session').get_comment_form_for_update(*args, **kwargs)

    def update_comment(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.update_comment"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('comment_admin_session').update_comment(*args, **kwargs)

    def can_delete_comments(self):
        """Pass through to provider CommentAdminSession.can_delete_comments"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('comment_admin_session').can_delete_comments()

    def delete_comment(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.delete_comment"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('comment_admin_session').delete_comment(*args, **kwargs)

    def can_manage_comment_aliases(self):
        """Pass through to provider CommentAdminSession.can_manage_comment_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('comment_admin_session').can_manage_comment_aliases()

    def alias_comment(self, *args, **kwargs):
        """Pass through to provider CommentAdminSession.alias_comment"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('comment_admin_session').alias_comment(*args, **kwargs)


class BookList(abc_commenting_objects.BookList, osid.OsidList):
    """BookList convenience adapter including related Session methods."""

    def get_next_book(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(Book)

    __next__ = next

    next_book = property(fget=get_next_book)

    def get_next_books(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(BookList, number=n)
