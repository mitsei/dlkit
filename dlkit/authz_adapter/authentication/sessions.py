"""AuthZ Adapter implementations of authentication sessions."""
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
from dlkit.abstract_osid.authentication import sessions as abc_authentication_sessions


class AgentLookupSession(abc_authentication_sessions.AgentLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AgentLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_agency_id()
        self._id_namespace = 'authentication.Agent'
        self.use_federated_agency_view()
        self.use_comparative_agent_view()
        self._auth_agency_ids = None
        self._unauth_agency_ids = None
    #     self._overriding_agency_ids = None
    #
    # def _get_overriding_agency_ids(self):
    #     if self._overriding_agency_ids is None:
    #         self._overriding_agency_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_agency_ids

    def _try_overriding_agencies(self, query):
        if self._get_overriding_catalog_ids('lookup') is not None:
            for catalog_id in self._get_overriding_catalog_ids('lookup'):
                query.match_agency_id(catalog_id, match=True)
        return self._query_session.get_agents_by_query(query), query

    def _get_unauth_agency_ids(self, agency_id):
        if self._can('lookup', agency_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(agency_id)]
        if self._hierarchy_session.has_child_agencies(agency_id):
            for child_agency_id in self._hierarchy_session.get_child_agency_ids(agency_id):
                unauth_list = unauth_list + self._get_unauth_agency_ids(child_agency_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_agencies(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_agency_ids is None:
            self._unauth_agency_ids = self._get_unauth_agency_ids(self._qualifier_id)
        for agency_id in self._unauth_agency_ids:
            query.match_agency_id(agency_id, match=False)
        return self._query_session.get_agents_by_query(query)

    def get_agency_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_agency_id()

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_agency()

    agency = property(fget=get_agency)

    def can_lookup_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

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

    def use_federated_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_agency_view()
        if self._query_session:
            self._query_session.use_federated_agency_view()

    def use_isolated_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_agency_view()
        if self._query_session:
            self._query_session.use_isolated_agency_view()

    @raise_null_argument
    def get_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_agent(agent_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_agent_query()
        query.match_id(agent_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_agents_by_ids(self, agent_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_agents_by_ids(agent_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_agent_query()
        for agent_id in (agent_ids):
            query.match_id(agent_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_agents_by_genus_type(self, agent_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_agents_by_genus_type(agent_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_agent_query()
        query.match_genus_type(agent_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_agents_by_parent_genus_type(self, agent_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_agents_by_parent_genus_type(agent_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_agent_query()
        query.match_parent_genus_type(agent_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_agents_by_record_type(self, agent_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_agents_by_record_type(agent_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_agent_query()
        query.match_record_type(agent_record_type, match=True)
        return self._try_harder(query)

    def get_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_agents()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_agent_query()
        query.match_any(match=True)
        return self._try_harder(query)

    agents = property(fget=get_agents)


class AgentQuerySession(abc_authentication_sessions.AgentQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AgentQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_agency_id()
        self._id_namespace = 'authentication.Agent'
        self.use_federated_agency_view()
        self._unauth_agency_ids = None
        # self._overriding_agency_ids = None

    # def _get_overriding_agency_ids(self):
    #     if self._overriding_agency_ids is None:
    #         self._overriding_agency_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_agency_ids

    def _try_overriding_agencies(self, query):
        if self._get_overriding_catalog_ids('search') is not None:
            for agency_id in self._get_overriding_catalog_ids('search'):
                query._provider_query.match_agency_id(agency_id, match=True)
        return self._query_session.get_agents_by_query(query), query

    def _get_unauth_agency_ids(self, agency_id):
        if self._can('search', agency_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(agency_id)]
        if self._hierarchy_session.has_child_agencies(agency_id):
            for child_agency_id in self._hierarchy_session.get_child_agency_ids(agency_id):
                unauth_list = unauth_list + self._get_unauth_agency_ids(child_agency_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_agencies(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_agency_ids is None:
            self._unauth_agency_ids = self._get_unauth_agency_ids(self._qualifier_id)
        for agency_id in self._unauth_agency_ids:
            query._provider_query.match_agency_id(agency_id, match=False)
        return self._query_session.get_agents_by_query(query)

    class AgentQueryWrapper(QueryWrapper):
        """Wrapper for AgentQueries to override match_agency_id method"""

        def match_agency_id(self, agency_id, match=True):
            self._cat_id_args_list.append({'agency_id': agency_id, 'match': match})

    def get_agency_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_agency_id()

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_agency()

    agency = property(fget=get_agency)

    def can_search_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_catalog_ids('search')))

    def use_federated_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_agency_view()
        if self._query_session:
            self._query_session.use_federated_agency_view()

    def use_isolated_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_agency_view()
        if self._query_session:
            self._query_session.use_isolated_agency_view()

    def get_agent_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AgentQueryWrapper(self._provider_session.get_agent_query())

    agent_query = property(fget=get_agent_query)

    @raise_null_argument
    def get_agents_by_query(self, agent_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(agent_query, '_cat_id_args_list'):
            raise Unsupported('agent_query not from this session')
        for kwargs in agent_query._cat_id_args_list:
            if self._can('search', kwargs['agency_id']):
                agent_query._provider_query.match_agency_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_agents_by_query(agent_query)
        self._check_search_conditions()
        result = self._try_harder(agent_query)
        agent_query._provider_query.clear_agency_terms()
        return result


class AgentSearchSession(abc_authentication_sessions.AgentSearchSession, AgentQuerySession):
    """Adapts underlying AgentSearchSession methodswith authorization checks."""

    def get_agent_search(self):
        """Pass through to provider AgentSearchSession.get_agent_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_agent_search()

    agent_search = property(fget=get_agent_search)

    def get_agent_search_order(self):
        raise Unimplemented()

    agent_search_order = property(fget=get_agent_search_order)

    @raise_null_argument
    def get_agents_by_search(self, agent_query, agent_search):
        """Pass through to provider AgentSearchSession.get_agents_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_agents_by_search(agent_query, agent_search)

    @raise_null_argument
    def get_agent_query_from_inspector(self, agent_query_inspector):
        raise Unimplemented()


class AgentAdminSession(abc_authentication_sessions.AgentAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AgentAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_agency_id()
        self._id_namespace = 'authentication.Agent'
        self._overriding_agency_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_agent_agency_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_agent_agency_session()
                self.get_agency_ids_by_agent = self._object_catalog_session.get_agency_ids_by_agent
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_agency_ids(self):
        if self._overriding_agency_ids is None:
            self._overriding_agency_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_agency_ids

    def _can_for_agent(self, func_name, agent_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, agent_id, 'get_agency_ids_for_agent')

    def get_agency_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_agency_id()

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_agency()

    agency = property(fget=get_agency)

    def can_create_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_agent_with_record_types(self, agent_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if agent_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_agent_form_for_create(self, agent_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_agent_form_for_create(agent_record_types)

    @raise_null_argument
    def create_agent(self, agent_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_agent(agent_form)

    def can_update_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def can_update_agent(self, agent_id):
        raise Unimplemented()

    @raise_null_argument
    def get_agent_form_for_update(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_agent('update', agent_id):
            raise PermissionDenied()
        return self._provider_session.get_agent_form_for_update(agent_id)

    def duplicate_agent(self, agent_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_agent(agent_id)

    @raise_null_argument
    def update_agent(self, agent_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_agent(agent_form)

    def can_delete_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def can_delete_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_agent('delete', agent_id):
            raise PermissionDenied()
        return self._provider_session.delete_agent(agent_id)

    def can_manage_agent_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_agent(self, agent_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_agent('alias', agent_id):
            raise PermissionDenied()
        return self._provider_session.alias_agent(agent_id, alias_id)


class AgentNotificationSession(abc_authentication_sessions.AgentNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AgentNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_agency_id()
        self._id_namespace = 'authentication.Agent'

    def get_agency_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_agency_id()

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_agency()

    agency = property(fget=get_agency)

    def can_register_for_agent_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_agency_view()
        if self._query_session:
            self._query_session.use_federated_agency_view()

    def use_isolated_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_agency_view()
        if self._query_session:
            self._query_session.use_isolated_agency_view()

    def reliable_agent_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_agent_notifications()

    def unreliable_agent_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_agent_notifications()

    @raise_null_argument
    def acknowledge_agent_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_agents()

    def register_for_changed_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_agents()

    @raise_null_argument
    def register_for_changed_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_agent(agent_id)

    def register_for_deleted_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_agents()

    @raise_null_argument
    def register_for_deleted_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_agent(agent_id)

    def reliable_agent_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_agent_notifications()

    def unreliable_agent_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_agent_notifications()

    @raise_null_argument
    def acknowledge_agent_notification(self, notification_id):
        raise Unimplemented()


class AgentAgencySession(abc_authentication_sessions.AgentAgencySession, osid_sessions.OsidSession):
    """Adapts underlying AgentAgencySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'authentication.AgentAgency'

    def can_lookup_agent_agency_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_agency_view()

    def use_plenary_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_agency_view()

    @raise_null_argument
    def get_agent_ids_by_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agent_ids_by_agency(agency_id)

    @raise_null_argument
    def get_agents_by_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agents_by_agency(agency_id)

    @raise_null_argument
    def get_agent_ids_by_agencies(self, agency_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agent_ids_by_agencies(agency_ids)

    @raise_null_argument
    def get_agents_by_agencies(self, agency_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agents_by_agencies(agency_ids)

    @raise_null_argument
    def get_agency_ids_by_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agency_ids_by_agent(agent_id)

    @raise_null_argument
    def get_agencies_by_agent(self, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agencies_by_agent(agent_id)


class AgentAgencyAssignmentSession(abc_authentication_sessions.AgentAgencyAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AgentAgencyAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'authentication.AgentAgency'

    def can_assign_agents(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_agents_to_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=agency_id)

    @raise_null_argument
    def get_assignable_agency_ids(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_agency_ids(agency_id)

    @raise_null_argument
    def get_assignable_agency_ids_for_agent(self, agency_id, agent_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_agency_ids_for_agent(agency_id, agent_id)

    @raise_null_argument
    def assign_agent_to_agency(self, agent_id, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_agent_to_agency(agent_id, agency_id)

    @raise_null_argument
    def unassign_agent_from_agency(self, agent_id, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_agent_from_agency(agent_id, agency_id)

    @raise_null_argument
    def reassign_agent_to_agency(self, agent_id, from_agency_id, to_agency_id):
        raise Unimplemented()


class AgentSmartAgencySession(abc_authentication_sessions.AgentSmartAgencySession, osid_sessions.OsidSession):
    """Adapts underlying AgentSmartAgencySession methodswith authorization checks."""

    def get_agency_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_agency_id()

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_agency()

    agency = property(fget=get_agency)

    def can_manage_smart_agencies(self):
        raise Unimplemented()

    def get_agent_query(self):
        raise Unimplemented()

    agent_query = property(fget=get_agent_query)

    def get_agent_search_order(self):
        raise Unimplemented()

    agent_search_order = property(fget=get_agent_search_order)

    @raise_null_argument
    def apply_agent_query(self, agent_query):
        raise Unimplemented()

    def inspect_agent_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_agent_sequencing(self, agent_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_agent_query_from_inspector(self, agent_query_inspector):
        raise Unimplemented()


class AgencyLookupSession(abc_authentication_sessions.AgencyLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AgencyLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authentication.Agency'

    def can_lookup_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_agency_view()

    def use_plenary_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_agency_view()

    @raise_null_argument
    def get_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agency(agency_id)

    @raise_null_argument
    def get_agencies_by_ids(self, agency_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agencies_by_ids(agency_ids)

    @raise_null_argument
    def get_agencies_by_genus_type(self, agency_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agencies_by_genus_type(agency_genus_type)

    @raise_null_argument
    def get_agencies_by_parent_genus_type(self, agency_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_agencies_by_record_type(self, agency_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_agencies_by_provider(self, resource_id):
        raise Unimplemented()

    def get_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_agencies()

    agencies = property(fget=get_agencies)


class AgencyQuerySession(abc_authentication_sessions.AgencyQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AgencyQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authentication.Agency'

    def can_search_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.can_search_bins_template
        return self._can('search')

    def get_agency_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_agency_query()

    agency_query = property(fget=get_agency_query)

    @raise_null_argument
    def get_agencies_by_query(self, agency_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_agencies_by_query(agency_query)


class AgencySearchSession(abc_authentication_sessions.AgencySearchSession, AgencyQuerySession):
    """Adapts underlying AgencySearchSession methodswith authorization checks."""

    def get_agency_search(self):
        raise Unimplemented()

    agency_search = property(fget=get_agency_search)

    def get_agency_search_order(self):
        raise Unimplemented()

    agency_search_order = property(fget=get_agency_search_order)

    @raise_null_argument
    def get_agencies_by_search(self, agency_query, agency_search):
        raise Unimplemented()

    @raise_null_argument
    def get_agency_query_from_inspector(self, agency_query_inspector):
        raise Unimplemented()


class AgencyAdminSession(abc_authentication_sessions.AgencyAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AgencyAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authentication.Agency'

    def can_create_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_agency_with_record_types(self, agency_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if agency_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_agency_form_for_create(self, agency_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_agency_form_for_create(agency_record_types)

    @raise_null_argument
    def create_agency(self, agency_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_agency(agency_form)

    def can_update_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_agency_form_for_update(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_agency_form_for_update(agency_id)

    @raise_null_argument
    def update_agency(self, agency_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_agency(agency_form)

    def can_delete_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_agency(agency_id)

    def can_manage_agency_aliases(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases
        return (self._can('manage') or
                bool(self._get_overriding_catalog_ids('manage')))

    @raise_null_argument
    def alias_agency(self, agency_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_agency(agency_id, alias_id)


class AgencyNotificationSession(abc_authentication_sessions.AgencyNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AgencyNotificationSession methodswith authorization checks."""

    def can_register_for_agency_notifications(self):
        raise Unimplemented()

    def reliable_agency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_agency_notifications()

    def unreliable_agency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_agency_notifications()

    @raise_null_argument
    def acknowledge_agency_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_agencies(self):
        raise Unimplemented()

    def register_for_changed_agencies(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_agency(self, agency_id):
        raise Unimplemented()

    def register_for_deleted_agencies(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_agency(self, agency_id):
        raise Unimplemented()

    def register_for_changed_agency_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_agency_hierarchy()

    @raise_null_argument
    def register_for_changed_agency_hierarchy_for_ancestors(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_agency_hierarchy_for_ancestors(agency_id)

    @raise_null_argument
    def register_for_changed_agency_hierarchy_for_descendants(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_agency_hierarchy_for_descendants(agency_id)

    def reliable_agency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_agency_notifications()

    def unreliable_agency_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_agency_notifications()

    @raise_null_argument
    def acknowledge_agency_notification(self, notification_id):
        raise Unimplemented()


class AgencyHierarchySession(abc_authentication_sessions.AgencyHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying AgencyHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authentication.Agency'

    def get_agency_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_agency_hierarchy_id()

    agency_hierarchy_id = property(fget=get_agency_hierarchy_id)

    def get_agency_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_agency_hierarchy()

    agency_hierarchy = property(fget=get_agency_hierarchy)

    def can_access_agency_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_agency_view()

    def use_plenary_agency_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_agency_view()

    def get_root_agency_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_agency_ids()

    root_agency_ids = property(fget=get_root_agency_ids)

    def get_root_agencies(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_agencies()

    root_agencies = property(fget=get_root_agencies)

    @raise_null_argument
    def has_parent_agencies(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_agencies(agency_id)

    @raise_null_argument
    def is_parent_of_agency(self, id_, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_agency(id_, agency_id)

    @raise_null_argument
    def get_parent_agency_ids(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_agency_ids(agency_id)

    @raise_null_argument
    def get_parent_agencies(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_agencies(agency_id)

    @raise_null_argument
    def is_ancestor_of_agency(self, id_, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_agency(id_, agency_id)

    @raise_null_argument
    def has_child_agencies(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_agencies(agency_id)

    @raise_null_argument
    def is_child_of_agency(self, id_, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_agency(id_, agency_id)

    @raise_null_argument
    def get_child_agency_ids(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_agency_ids(agency_id)

    @raise_null_argument
    def get_child_agencies(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_agencies(agency_id)

    @raise_null_argument
    def is_descendant_of_agency(self, id_, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_agency(id_, agency_id)

    @raise_null_argument
    def get_agency_node_ids(self, agency_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_agency_node_ids(
            agency_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_agency_nodes(self, agency_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_agency_nodes(
            agency_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class AgencyHierarchyDesignSession(abc_authentication_sessions.AgencyHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying AgencyHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authentication.Agency%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authentication.Agency'
        # should this be 'authentication.AgencyHierarchy' ?

    def get_agency_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_agency_hierarchy_id()

    agency_hierarchy_id = property(fget=get_agency_hierarchy_id)

    def get_agency_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_agency_hierarchy()

    agency_hierarchy = property(fget=get_agency_hierarchy)

    def can_modify_agency_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_agency(agency_id)

    @raise_null_argument
    def remove_root_agency(self, agency_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_agency(agency_id)

    @raise_null_argument
    def add_child_agency(self, agency_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_agency(agency_id, child_id)

    @raise_null_argument
    def remove_child_agency(self, agency_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_agency(agency_id, child_id)

    @raise_null_argument
    def remove_child_agencies(self, agency_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_agencies(agency_id)
