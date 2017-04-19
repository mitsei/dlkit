"""AuthZ Adapter implementations of authentication.process sessions."""
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
from dlkit.abstract_osid.authentication_process import sessions as abc_authentication_process_sessions


class AuthenticationAcquisitionSession(abc_authentication_process_sessions.AuthenticationAcquisitionSession, osid_sessions.OsidSession):
    """Adapts underlying AuthenticationAcquisitionSession methodswith authorization checks."""

    def get_authentication(self):
        raise Unimplemented()

    authentication = property(fget=get_authentication)


class AuthenticationValidationSession(abc_authentication_process_sessions.AuthenticationValidationSession, osid_sessions.OsidSession):
    """Adapts underlying AuthenticationValidationSession methodswith authorization checks."""

    def get_authentication_input(self):
        raise Unimplemented()

    authentication_input = property(fget=get_authentication_input)

    @raise_null_argument
    def authenticate(self, input_):
        raise Unimplemented()

    @raise_null_argument
    def get_challenge_data(self, input_):
        raise Unimplemented()


class TrustLookupSession(abc_authentication_process_sessions.TrustLookupSession, osid_sessions.OsidSession):
    """Adapts underlying TrustLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_agency_id()
        self._id_namespace = 'authentication_process.Trust'
        self.use_federated_agency_view()
        self.use_comparative_trust_view()
        self._auth_agency_ids = None
        self._unauth_agency_ids = None
    #     self._overriding_agency_ids = None
    #
    # def _get_overriding_agency_ids(self):
    #     if self._overriding_agency_ids is None:
    #         self._overriding_agency_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_agency_ids

    def _try_overriding_agencies(self, query):
        for catalog_id in self._get_overriding_catalog_ids('lookup'):
            query.match_agency_id(catalog_id, match=True)
        return self._query_session.get_trusts_by_query(query), query

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
        return self._query_session.get_trusts_by_query(query)

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

    def can_lookup_trusts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_trust_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_trust_view()

    def use_plenary_trust_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_trust_view()

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
    def get_trust(self, trust_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_trust(trust_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_trust_query()
        query.match_id(trust_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_trusts_by_ids(self, trust_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_trusts_by_ids(trust_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_trust_query()
        for trust_id in (trust_ids):
            query.match_id(trust_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_trusts_by_genus_type(self, trust_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_trusts_by_genus_type(trust_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_trust_query()
        query.match_genus_type(trust_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_trusts_by_parent_genus_type(self, trust_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_trusts_by_parent_genus_type(trust_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_trust_query()
        query.match_parent_genus_type(trust_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_trusts_by_record_type(self, trust_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_trusts_by_record_type(trust_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_trust_query()
        query.match_record_type(trust_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_circle_of_trust(self, trust_id):
        raise Unimplemented()

    def get_trusts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_trusts()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_trust_query()
        query.match_any(match=True)
        return self._try_harder(query)

    trusts = property(fget=get_trusts)


class CircleOfTrustSession(abc_authentication_process_sessions.CircleOfTrustSession, osid_sessions.OsidSession):
    """Adapts underlying CircleOfTrustSession methodswith authorization checks."""

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

    def can_lookup_trust_circles(self):
        raise Unimplemented()

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
    def get_trust(self, agent_id):
        raise Unimplemented()

    @raise_null_argument
    def is_in_circle(self, agent_id):
        raise Unimplemented()
