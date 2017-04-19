"""AuthZ Adapter implementations of osid sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid.osid_errors import IllegalState, Unimplemented
from ..osid.osid_errors import PermissionDenied
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.abstract_osid.osid import sessions as abc_osid_sessions


COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1


class OsidSession(abc_osid_sessions.OsidSession):
    """Adapts underlying OsidSession methodswith authorization checks."""
    def __init__(self, provider_session, authz_session, override_lookup_session=None, proxy=None, **kwargs):
        self._provider_session = provider_session
        self._authz_session = authz_session
        self._override_lookup_session = override_lookup_session
        self._proxy = proxy
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None
        self._object_catalog_session = None
        self._id_namespace = None
        self._qualifier_id = None
        self._authz_cache = dict()  # Does this want to be a real cache???
        self._overriding_catalog_ids = None
        self._object_view = COMPARATIVE
        self._catalog_view = FEDERATED

    def _get_function_id(self, func_name):
        return Id(
            identifier=func_name,
            namespace=self._id_namespace,
            authority='ODL.MIT.EDU')

    def _can(self, func_name, qualifier_id=None):
        """Tests if the named function is authorized with agent and qualifier.

        Also, caches authz's in a dict.  It is expected that this will not grow to big, as
        there are typically only a small number of qualifier + function combinations to
        store for the agent.  However, if this becomes an issue, we can switch to something
        like cachetools.

        """
        function_id = self._get_function_id(func_name)
        if qualifier_id is None:
            qualifier_id = self._qualifier_id
        agent_id = self.get_effective_agent_id()
        try:
            return self._authz_cache[str(agent_id) + str(function_id) + str(qualifier_id)]
        except KeyError:
            authz = self._authz_session.is_authorized(agent_id=agent_id,
                                                      function_id=function_id,
                                                      qualifier_id=qualifier_id)
            self._authz_cache[str(agent_id) + str(function_id) + str(qualifier_id)] = authz
            return authz

    def _can_for_object(self, func_name, object_id, method_name):
        """Checks if agent can perform function for object"""
        can_for_session = self._can(func_name)
        if (can_for_session or
                self._object_catalog_session is None or
                self._override_lookup_session is None):
            return can_for_session

        override_auths = self._override_lookup_session.get_authorizations_for_agent_and_function(
            self.get_effective_agent_id(),
            self._get_function_id(func_name))
        if not override_auths.available():
            return False

        if self._object_catalog_session is not None:
            catalog_ids = list(getattr(self._object_catalog_session, method_name)(object_id))
            for auth in override_auths:
                if auth.get_qualifier_id() in catalog_ids:
                    return True
        return False

    def _get_overriding_catalog_ids(self, func_name):
        cat_id_list = []
        if self._overriding_catalog_ids is None and self._override_lookup_session is not None:
            function_id = Id(
                identifier=func_name,
                namespace=self._id_namespace,
                authority='ODL.MIT.EDU')
            auths = self._override_lookup_session.get_authorizations_for_agent_and_function(
                self.get_effective_agent_id(),
                function_id)
            for auth in auths:
                cat_id_list.append(auth.get_qualifier_id())
        self._overriding_catalog_ids = cat_id_list
        return self._overriding_catalog_ids

    def _check_lookup_conditions(self):
        if ((self._is_plenary_object_view() or self._is_isolated_catalog_view() or self._query_session is None) and
                not self._get_overriding_catalog_ids('lookup')):
            raise PermissionDenied()

    def _check_search_conditions(self):
        if (self._is_federated_catalog_view() and
                self._get_overriding_catalog_ids('search')):
            return
        raise PermissionDenied()

    def _use_comparative_object_view(self):
        self._object_view = COMPARATIVE

    def _use_plenary_object_view(self):
        self._object_view = PLENARY

    def _is_comparative_object_view(self):
        return not bool(self._object_view)

    def _is_plenary_object_view(self):
        return bool(self._object_view)

    def _use_federated_catalog_view(self):
        self._catalog_view = FEDERATED

    def _use_isolated_catalog_view(self):
        self._catalog_view = ISOLATED

    def _is_federated_catalog_view(self):
        return not bool(self._catalog_view)

    def _is_isolated_catalog_view(self):
        return bool(self._catalog_view)

    def get_locale(self):
        pass

    locale = property(fget=get_locale)

    def is_authenticated(self):
        if self._proxy is None:
            return False
        elif self._proxy.has_authentication():
            return self._proxy.get_authentication().is_valid()
        else:
            return False

    def get_authenticated_agent_id(self):
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent_id()
        else:
            raise IllegalState()

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent()
        else:
            raise IllegalState()

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        if self.is_authenticated():
            if self._proxy.has_effective_agent():
                return self._proxy.get_effective_agent_id()
            else:
                return self._proxy.get_authentication().get_agent_id()
        else:
            return Id(
                identifier='MC3GUE$T@MIT.EDU',
                namespace='agent.Agent',
                authority='MIT-OEIT')

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        # effective_agent_id = self.get_effective_agent_id()
        # This may want to be extended to get the Agent directly from the Authentication
        # if available and if not effective agent is available in the proxy
        # return Agent(
        #    identifier=effective_agent_id.get_identifier(),
        #    namespace=effective_agent_id.get_namespace(),
        #    authority=effective_agent_id.get_authority())
        raise Unimplemented()

    effective_agent = property(fget=get_effective_agent)

    def get_date(self):
        raise Unimplemented()

    date = property(fget=get_date)

    def get_clock_rate(self):
        raise Unimplemented()

    clock_rate = property(fget=get_clock_rate)

    def get_format_type(self):
        raise Unimplemented()

    format_type = property(fget=get_format_type)

    def supports_transactions(self):
        raise Unimplemented()

    def start_transaction(self):
        raise Unimplemented()
