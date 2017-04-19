"""AuthZ Adapter implementations of assessment.authoring sessions."""
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
from dlkit.abstract_osid.assessment_authoring import sessions as abc_assessment_authoring_sessions


class AssessmentPartLookupSession(abc_assessment_authoring_sessions.AssessmentPartLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.AssessmentPart'
        self.use_federated_bank_view()
        self.use_comparative_assessment_part_view()
        self._auth_bank_ids = None
        self._unauth_bank_ids = None
    #     self._overriding_bank_ids = None
    #
    # def _get_overriding_bank_ids(self):
    #     if self._overriding_bank_ids is None:
    #         self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_bank_ids

    def _try_overriding_banks(self, query):
        for catalog_id in self._get_overriding_catalog_ids('lookup'):
            query.match_bank_id(catalog_id, match=True)
        return self._query_session.get_assessment_parts_by_query(query), query

    def _get_unauth_bank_ids(self, bank_id):
        if self._can('lookup', bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bank_id)]
        if self._hierarchy_session.has_child_banks(bank_id):
            for child_bank_id in self._hierarchy_session.get_child_bank_ids(bank_id):
                unauth_list = unauth_list + self._get_unauth_bank_ids(child_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_banks(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bank_ids is None:
            self._unauth_bank_ids = self._get_unauth_bank_ids(self._qualifier_id)
        for bank_id in self._unauth_bank_ids:
            query.match_bank_id(bank_id, match=False)
        return self._query_session.get_assessment_parts_by_query(query)

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_lookup_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_assessment_part_view()

    def use_plenary_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_assessment_part_view()

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def use_active_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_active_composition_view
        return self._provider_session.use_active_assessment_part_view()

    def use_any_status_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_any_status_composition_view
        return self._provider_session.use_any_status_assessment_part_view()

    def use_sequestered_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_sequestered_composition_view_template
        return self._provider_session.use_sequestered_assessment_part_view()

    def use_unsequestered_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_unsequestered_composition_view_template
        return self._provider_session.use_unsequestered_assessment_part_view()

    @raise_null_argument
    def get_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_part(assessment_part_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_id(assessment_part_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_assessment_parts_by_ids(self, assessment_part_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_by_ids(assessment_part_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        for assessment_part_id in (assessment_part_ids):
            query.match_id(assessment_part_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessment_parts_by_genus_type(self, assessment_part_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_by_genus_type(assessment_part_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_genus_type(assessment_part_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessment_parts_by_parent_genus_type(self, assessment_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_by_parent_genus_type(assessment_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_parent_genus_type(assessment_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessment_parts_by_record_type(self, assessment_part_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_by_record_type(assessment_part_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_record_type(assessment_part_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessment_parts_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_for_assessment(assessment_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_assessment_id(assessment_id, match=True)
        return self._try_harder(query)

    def get_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_any(match=True)
        return self._try_harder(query)

    assessment_parts = property(fget=get_assessment_parts)

    def get_assessment_parts_for_assessment_part(self, assessment_part_id):
        # NOT CURRENTLY IN SPEC - Implemented from
        # osid.assessment_authoring.AssessmentPartLookupSession.additional_methods
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_for_assessment_part(assessment_part_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_assessment_part_id(assessment_part_id, match=True)
        return self._try_harder(query)


class AssessmentPartQuerySession(abc_assessment_authoring_sessions.AssessmentPartQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.AssessmentPart'
        self.use_federated_bank_view()
        self._unauth_bank_ids = None
        # self._overriding_bank_ids = None

    # def _get_overriding_bank_ids(self):
    #     if self._overriding_bank_ids is None:
    #         self._overriding_bank_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_bank_ids

    def _try_overriding_banks(self, query):
        for bank_id in self._get_overriding_catalog_ids('search'):
            query._provider_query.match_bank_id(bank_id, match=True)
        return self._query_session.get_assessment_parts_by_query(query), query

    def _get_unauth_bank_ids(self, bank_id):
        if self._can('search', bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bank_id)]
        if self._hierarchy_session.has_child_banks(bank_id):
            for child_bank_id in self._hierarchy_session.get_child_bank_ids(bank_id):
                unauth_list = unauth_list + self._get_unauth_bank_ids(child_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_banks(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bank_ids is None:
            self._unauth_bank_ids = self._get_unauth_bank_ids(self._qualifier_id)
        for bank_id in self._unauth_bank_ids:
            query._provider_query.match_bank_id(bank_id, match=False)
        return self._query_session.get_assessment_parts_by_query(query)

    class AssessmentPartQueryWrapper(QueryWrapper):
        """Wrapper for AssessmentPartQueries to override match_bank_id method"""

        def match_bank_id(self, bank_id, match=True):
            self._cat_id_args_list.append({'bank_id': bank_id, 'match': match})

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_search_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_bank_ids()))

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def use_sequestered_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_sequestered_composition_view_template
        return self._provider_session.use_sequestered_assessment_part_view()

    def use_unsequestered_assessment_part_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_unsequestered_composition_view_template
        return self._provider_session.use_unsequestered_assessment_part_view()

    def get_assessment_part_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AssessmentPartQueryWrapper(self._provider_session.get_assessment_part_query())

    assessment_part_query = property(fget=get_assessment_part_query)

    @raise_null_argument
    def get_assessment_parts_by_query(self, assessment_part_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(assessment_part_query, '_cat_id_args_list'):
            raise Unsupported('assessment_part_query not from this session')
        for kwargs in assessment_part_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                assessment_part_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_assessment_parts_by_query(assessment_part_query)
        self._check_search_conditions()
        result = self._try_harder(assessment_part_query)
        assessment_part_query._provider_query.clear_bank_terms()
        return result


class AssessmentPartSearchSession(abc_assessment_authoring_sessions.AssessmentPartSearchSession, AssessmentPartQuerySession):
    """Adapts underlying AssessmentPartSearchSession methodswith authorization checks."""

    def get_assessment_part_search(self):
        """Pass through to provider AssessmentPartSearchSession.get_assessment_part_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_search()

    assessment_part_search = property(fget=get_assessment_part_search)

    def get_assessment_part_search_order(self):
        raise Unimplemented()

    assessment_part_search_order = property(fget=get_assessment_part_search_order)

    @raise_null_argument
    def get_assessment_parts_by_search(self, assessment_part_query, assessment_part_search):
        """Pass through to provider AssessmentPartSearchSession.get_assessment_parts_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_parts_by_search(assessment_part_query, assessment_part_search)

    @raise_null_argument
    def get_assessment_part_query_from_inspector(self, assessment_part_query_inspector):
        raise Unimplemented()


class AssessmentPartAdminSession(abc_assessment_authoring_sessions.AssessmentPartAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.AssessmentPart'
        self._overriding_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_assessment_part_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_assessment_part_bank_session()
                self.get_bank_ids_by_assessment_part = self._object_catalog_session.get_bank_ids_by_assessment_part
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bank_ids(self):
        if self._overriding_bank_ids is None:
            self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bank_ids

    def _can_for_assessment_part(self, func_name, assessment_part_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, assessment_part_id, 'get_bank_ids_for_assessment_part')

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_create_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_assessment_part_with_record_types(self, assessment_part_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if assessment_part_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_assessment_part_form_for_create_for_assessment(self, assessment_id, assessment_part_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_form_for_create_for_assessment(assessment_id, assessment_part_record_types)

    @raise_null_argument
    def create_assessment_part_for_assessment(self, assessment_part_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_assessment_part_for_assessment(assessment_part_form)

    @raise_null_argument
    def get_assessment_part_form_for_create_for_assessment_part(self, assessment_part_id, assessment_part_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_form_for_create_for_assessment_part(assessment_part_id, assessment_part_record_types)

    @raise_null_argument
    def create_assessment_part_for_assessment_part(self, assessment_part_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_assessment_part_for_assessment_part(assessment_part_form)

    def can_update_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_assessment_part_form_for_update(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_assessment_part('update', assessment_part_id):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_form_for_update(assessment_part_id)

    def duplicate_assessment_part(self, assessment_part_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_assessment_part(assessment_part_id)

    @raise_null_argument
    def update_assessment_part(self, assessment_part_id, assessment_part_form):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_assessment_part(assessment_part_id, assessment_part_form)

    def can_delete_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective_template
        if not self._can_for_assessment_part('delete', assessment_part_id):
            raise PermissionDenied()
        return self._provider_session.delete_assessment_part(assessment_part_id)

    def can_manage_assessment_part_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_assessment_part(self, assessment_part_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_assessment_part('alias', assessment_part_id):
            raise PermissionDenied()
        return self._provider_session.alias_assessment_part(assessment_part_id, alias_id)


class AssessmentPartNotificationSession(abc_assessment_authoring_sessions.AssessmentPartNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.AssessmentPart'

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_register_for_assessment_part_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def reliable_assessment_part_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_part_notifications()

    def unreliable_assessment_part_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_part_notifications()

    @raise_null_argument
    def acknowledge_assessment_part_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessment_parts()

    def register_for_changed_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessment_parts()

    @raise_null_argument
    def register_for_changed_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessment_part(assessment_part_id)

    def register_for_deleted_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessment_parts()

    @raise_null_argument
    def register_for_deleted_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessment_part(assessment_part_id)

    def reliable_assessment_part_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_part_notifications()

    def unreliable_assessment_part_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_part_notifications()

    @raise_null_argument
    def acknowledge_assessment_part_notification(self, notification_id):
        raise Unimplemented()


class AssessmentPartBankSession(abc_assessment_authoring_sessions.AssessmentPartBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment_authoring.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment_authoring.AssessmentPartBank'

    def can_lookup_assessment_part_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_assessment_part_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_assessment_part_bank_view()

    def use_plenary_assessment_part_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_assessment_part_bank_view()

    @raise_null_argument
    def get_assessment_part_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessment_parts_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessment_part_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_part_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_assessment_parts_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_parts_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_assessment_part(assessment_part_id)

    @raise_null_argument
    def get_banks_by_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_assessment_part(assessment_part_id)


class AssessmentPartBankAssignmentSession(abc_assessment_authoring_sessions.AssessmentPartBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment_authoring.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment_authoring.AssessmentPartBank'

    def can_assign_assessment_parts(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_assessment_parts_to_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bank_id)

    @raise_null_argument
    def get_assignable_bank_ids(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids()

    @raise_null_argument
    def get_assignable_bank_ids_for_assessment_part(self, bank_id, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_assessment_part(assessment_part_id)

    @raise_null_argument
    def assign_assessment_part_to_bank(self, assessment_part_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_assessment_part_to_bank(assessment_part_id, bank_id)

    @raise_null_argument
    def unassign_assessment_part_from_bank(self, assessment_part_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_assessment_part_from_bank(assessment_part_id, bank_id)

    @raise_null_argument
    def reassign_assessment_part_to_bank(self, assessment_part_id, from_biank_id, to_bank_id):
        raise Unimplemented()


class AssessmentPartSmartBankSession(abc_assessment_authoring_sessions.AssessmentPartSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartSmartBankSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_manage_smart_banks(self):
        raise Unimplemented()

    def get_assessment_part_query(self):
        raise Unimplemented()

    assessment_part_query = property(fget=get_assessment_part_query)

    def get_assessment_part_search_order(self):
        raise Unimplemented()

    assessment_part_search_order = property(fget=get_assessment_part_search_order)

    @raise_null_argument
    def apply_assessment_part_query(self, assessment_part_query):
        raise Unimplemented()

    def inspect_assessment_part_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_assessment_part_sequencing(self, assessment_part_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_assessment_part_query_from_inspector(self, assessment_part_query_inspector):
        raise Unimplemented()


class AssessmentPartItemSession(abc_assessment_authoring_sessions.AssessmentPartItemSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartItemSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_access_assessment_part_items(self):
        raise Unimplemented()

    def use_comparative_asseessment_part_item_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_asseessment_part_item_view()

    def use_plenary_assessment_part_item_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_assessment_part_item_view()

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    @raise_null_argument
    def get_assessment_part_items(self, assessment_part_id):
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assessment_part_items(assessment_part_id)

    @raise_null_argument
    def get_assessment_parts_by_item(self, item_id):
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assessment_parts_by_item(item_id)


class AssessmentPartItemDesignSession(abc_assessment_authoring_sessions.AssessmentPartItemDesignSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentPartItemDesignSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_design_assessment_parts(self):
        raise Unimplemented()

    @raise_null_argument
    def add_item(self, item_id, assessment_part_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.add_item(item_id, assessment_part_id)

    @raise_null_argument
    def move_item_ahead(self, item_id, assessment_part_id, reference_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.move_item_ahead(item_id, assessment_part_id, reference_id)

    @raise_null_argument
    def move_item_behind(self, item_id, assessment_part_id, reference_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.move_item_behind(item_id, assessment_part_id, reference_id)

    @raise_null_argument
    def order_items(self, item_ids, assessment_part_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.order_items(item_ids, assessment_part_id)

    @raise_null_argument
    def remove_item(self, item_id, assessment_part_id):
        if not self._can('compose'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_item(item_id, assessment_part_id)


class SequenceRuleLookupSession(abc_assessment_authoring_sessions.SequenceRuleLookupSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.SequenceRule'
        self.use_federated_bank_view()
        self.use_comparative_sequence_rule_view()
        self._auth_bank_ids = None
        self._unauth_bank_ids = None
    #     self._overriding_bank_ids = None
    #
    # def _get_overriding_bank_ids(self):
    #     if self._overriding_bank_ids is None:
    #         self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
    #     return self._overriding_bank_ids

    def _try_overriding_banks(self, query):
        for catalog_id in self._get_overriding_catalog_ids('lookup'):
            query.match_bank_id(catalog_id, match=True)
        return self._query_session.get_sequence_rules_by_query(query), query

    def _get_unauth_bank_ids(self, bank_id):
        if self._can('lookup', bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bank_id)]
        if self._hierarchy_session.has_child_banks(bank_id):
            for child_bank_id in self._hierarchy_session.get_child_bank_ids(bank_id):
                unauth_list = unauth_list + self._get_unauth_bank_ids(child_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_banks(query)
        if self._is_isolated_catalog_view():
            if results.available() or self._is_comparative_object_view():
                return results
        if self._is_plenary_object_view():
            return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bank_ids is None:
            self._unauth_bank_ids = self._get_unauth_bank_ids(self._qualifier_id)
        for bank_id in self._unauth_bank_ids:
            query.match_bank_id(bank_id, match=False)
        return self._query_session.get_sequence_rules_by_query(query)

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_lookup_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_sequence_rule_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_sequence_rule_view()

    def use_plenary_sequence_rule_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_sequence_rule_view()

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def use_active_sequence_rule_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_active_composition_view
        return self._provider_session.use_active_sequence_rule_view()

    def use_any_status_sequence_rule_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_any_status_composition_view
        return self._provider_session.use_any_status_sequence_rule_view()

    @raise_null_argument
    def get_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule(sequence_rule_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_id(sequence_rule_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_sequence_rules_by_ids(self, sequence_rule_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_by_ids(sequence_rule_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        for sequence_rule_id in (sequence_rule_ids):
            query.match_id(sequence_rule_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rules_by_genus_type(self, sequence_rule_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_by_genus_type(sequence_rule_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_genus_type(sequence_rule_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rules_by_parent_genus_type(self, sequence_rule_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_by_parent_genus_type(sequence_rule_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_parent_genus_type(sequence_rule_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rules_by_record_type(self, sequence_rule_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_by_record_type(sequence_rule_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_record_type(sequence_rule_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rules_for_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_for_assessment_part(assessment_part_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_assessment_part_id(assessment_part_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rules_for_next_assessment_part(self, next_assessment_part_id):
        raise Unimplemented()

    @raise_null_argument
    def get_sequence_rules_for_assessment_parts(self, assessment_part_id, next_assessment_part_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objectives_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_for_assessment_parts(assessment_part_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        for sequence_rule_id in (assessment_part_id):
            query.match_assessment_part_id(sequence_rule_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rules_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_for_assessment(assessment_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_assessment_id(assessment_id, match=True)
        return self._try_harder(query)

    def get_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        query.match_any(match=True)
        return self._try_harder(query)

    sequence_rules = property(fget=get_sequence_rules)


class SequenceRuleQuerySession(abc_assessment_authoring_sessions.SequenceRuleQuerySession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.SequenceRule'
        self.use_federated_bank_view()
        self._unauth_bank_ids = None
        # self._overriding_bank_ids = None

    # def _get_overriding_bank_ids(self):
    #     if self._overriding_bank_ids is None:
    #         self._overriding_bank_ids = self._get_overriding_catalog_ids('search')
    #     return self._overriding_bank_ids

    def _try_overriding_banks(self, query):
        for bank_id in self._get_overriding_catalog_ids('search'):
            query._provider_query.match_bank_id(bank_id, match=True)
        return self._query_session.get_sequence_rules_by_query(query), query

    def _get_unauth_bank_ids(self, bank_id):
        if self._can('search', bank_id):
            return []  # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(bank_id)]
        if self._hierarchy_session.has_child_banks(bank_id):
            for child_bank_id in self._hierarchy_session.get_child_bank_ids(bank_id):
                unauth_list = unauth_list + self._get_unauth_bank_ids(child_bank_id)
        return unauth_list

    def _try_harder(self, query):
        results, query = self._try_overriding_banks(query)
        if self._is_isolated_catalog_view():
            if results.available():
                return results
        if self._hierarchy_session is None or self._query_session is None:
            return results
        if self._unauth_bank_ids is None:
            self._unauth_bank_ids = self._get_unauth_bank_ids(self._qualifier_id)
        for bank_id in self._unauth_bank_ids:
            query._provider_query.match_bank_id(bank_id, match=False)
        return self._query_session.get_sequence_rules_by_query(query)

    class SequenceRuleQueryWrapper(QueryWrapper):
        """Wrapper for SequenceRuleQueries to override match_bank_id method"""

        def match_bank_id(self, bank_id, match=True):
            self._cat_id_args_list.append({'bank_id': bank_id, 'match': match})

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_search_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_bank_ids()))

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def get_sequence_rule_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.SequenceRuleQueryWrapper(self._provider_session.get_sequence_rule_query())

    sequence_rule_query = property(fget=get_sequence_rule_query)

    @raise_null_argument
    def get_sequence_rules_by_query(self, sequence_rule_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(sequence_rule_query, '_cat_id_args_list'):
            raise Unsupported('sequence_rule_query not from this session')
        for kwargs in sequence_rule_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                sequence_rule_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_sequence_rules_by_query(sequence_rule_query)
        self._check_search_conditions()
        result = self._try_harder(sequence_rule_query)
        sequence_rule_query._provider_query.clear_bank_terms()
        return result


class SequenceRuleSearchSession(abc_assessment_authoring_sessions.SequenceRuleSearchSession, SequenceRuleQuerySession):
    """Adapts underlying SequenceRuleSearchSession methodswith authorization checks."""

    def get_sequence_rule_search(self):
        """Pass through to provider SequenceRuleSearchSession.get_sequence_rule_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_search()

    sequence_rule_search = property(fget=get_sequence_rule_search)

    def get_sequence_rule_search_order(self):
        raise Unimplemented()

    sequence_rule_search_order = property(fget=get_sequence_rule_search_order)

    @raise_null_argument
    def get_sequence_rules_by_search(self, sequence_rule_query, sequence_rule_search):
        """Pass through to provider SequenceRuleSearchSession.get_sequence_rules_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rules_by_search(sequence_rule_query, sequence_rule_search)

    @raise_null_argument
    def get_sequence_rule_query_from_inspector(self, sequence_rule_query_inspector):
        raise Unimplemented()


class SequenceRuleAdminSession(abc_assessment_authoring_sessions.SequenceRuleAdminSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.SequenceRule'
        self._overriding_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_sequence_rule_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_sequence_rule_bank_session()
                self.get_bank_ids_by_sequence_rule = self._object_catalog_session.get_bank_ids_by_sequence_rule
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bank_ids(self):
        if self._overriding_bank_ids is None:
            self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bank_ids

    def _can_for_sequence_rule(self, func_name, sequence_rule_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, sequence_rule_id, 'get_bank_ids_for_sequence_rule')

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_create_sequence_rule(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_sequence_rule_with_record_types(self, sequence_rule_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if sequence_rule_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_sequence_rule_form_for_create(self, assessment_part_id, next_assessment_part_id, sequence_rule_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_form_for_create(assessment_part_id)

    @raise_null_argument
    def create_sequence_rule(self, sequence_rule_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_sequence_rule(sequence_rule_form)

    def can_update_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_sequence_rule_form_for_update(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_sequence_rule('update', sequence_rule_id):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_form_for_update(sequence_rule_id)

    def duplicate_sequence_rule(self, sequence_rule_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_sequence_rule(sequence_rule_id)

    @raise_null_argument
    def update_sequence_rule(self, sequence_rule_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_sequence_rule(sequence_rule_form)

    def can_delete_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_sequence_rule('delete', sequence_rule_id):
            raise PermissionDenied()
        return self._provider_session.delete_sequence_rule(sequence_rule_id)

    def can_manage_sequence_rule_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_sequence_rule(self, sequence_rule_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_sequence_rule('alias', sequence_rule_id):
            raise PermissionDenied()
        return self._provider_session.alias_sequence_rule(sequence_rule_id, alias_id)

    def can_sequence_sequence_rules(self):
        raise Unimplemented()

    @raise_null_argument
    def move_sequence_rule_ahead(self, sequence_rule_id, assessment_part_id, reference_id):
        raise Unimplemented()

    @raise_null_argument
    def move_sequence_rule_behind(self, sequence_rule_id, assessment_part_id, reference_id):
        raise Unimplemented()

    @raise_null_argument
    def order_sequence_rules(self, sequence_rule_ids, assessment_part_id):
        raise Unimplemented()


class SequenceRuleNotificationSession(abc_assessment_authoring_sessions.SequenceRuleNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment_authoring.SequenceRule'

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_register_for_sequence_rule_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def reliable_sequence_rule_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_sequence_rule_notifications()

    def unreliable_sequence_rule_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_sequence_rule_notifications()

    @raise_null_argument
    def acknowledge_sequence_rule_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_sequence_rules()

    @raise_null_argument
    def register_for_new_sequence_rules_for_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_sequence_rules_for_assessment_part()

    @raise_null_argument
    def register_for_new_sequence_rules_for_next_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_sequence_rules_for_next_assessment_part()

    def register_for_changed_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_sequence_rules()

    @raise_null_argument
    def register_for_changed_sequence_rules_for_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_sequence_rules_for_assessment_part(assessment_part_id)

    @raise_null_argument
    def register_for_changed_sequence_rules_for_next_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_sequence_rules_for_next_assessment_part(assessment_part_id)

    @raise_null_argument
    def register_for_changed_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_sequence_rule(sequence_rule_id)

    def register_for_deleted_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_sequence_rules()

    @raise_null_argument
    def register_for_deleted_sequence_rules_for_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_sequence_rules_for_assessment_part(assessment_part_id)

    @raise_null_argument
    def register_for_deleted_sequence_rules_for_next_assessment_part(self, assessment_part_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_sequence_rules_for_next_assessment_part(assessment_part_id)

    @raise_null_argument
    def register_for_deleted_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_sequence_rule(sequence_rule_id)

    def reliable_sequence_rule_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_sequence_rule_notifications()

    def unreliable_sequence_rule_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_sequence_rule_notifications()

    @raise_null_argument
    def acknowledge_sequence_rule_notification(self, notification_id):
        raise Unimplemented()


class SequenceRuleBankSession(abc_assessment_authoring_sessions.SequenceRuleBankSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment_authoring.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment_authoring.SequenceRuleBank'

    def can_lookup_sequence_rule_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_sequence_rule_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_sequence_rule_bank_view()

    def use_plenary_sequence_rule_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_sequence_rule_bank_view()

    @raise_null_argument
    def get_sequence_rule_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_ids_by_bank(bank_id)

    @raise_null_argument
    def get_sequence_rules_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_ids_by_bank(bank_id)

    @raise_null_argument
    def get_sequence_rule_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_sequence_rules_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rules_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_sequence_rule(sequence_rule_id)

    @raise_null_argument
    def get_banks_by_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_sequence_rule(sequence_rule_id)


class SequenceRuleBankAssignmentSession(abc_assessment_authoring_sessions.SequenceRuleBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment_authoring.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment_authoring.SequenceRuleBank'

    def can_assign_sequence_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_sequence_rules_to_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bank_id)

    @raise_null_argument
    def get_assignable_bank_ids(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids()

    @raise_null_argument
    def get_assignable_bank_ids_for_sequence_rule(self, bank_id, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_sequence_rule(sequence_rule_id)

    @raise_null_argument
    def assign_sequence_rule_to_bank(self, sequence_rule_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_sequence_rule_to_bank(sequence_rule_id, bank_id)

    @raise_null_argument
    def unassign_sequence_rule_from_bank(self, sequence_rule_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_sequence_rule_from_bank(sequence_rule_id, bank_id)

    @raise_null_argument
    def reassign_sequence_rule_to_bank(self, sequence_rule_id, from_bank_id, to_bank_id):
        raise Unimplemented()


class SequenceRuleSmartBankSession(abc_assessment_authoring_sessions.SequenceRuleSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleSmartBankSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_manage_smart_banks(self):
        raise Unimplemented()

    def get_sequence_rule_query(self):
        raise Unimplemented()

    sequence_rule_query = property(fget=get_sequence_rule_query)

    def get_sequence_rule_search_order(self):
        raise Unimplemented()

    sequence_rule_search_order = property(fget=get_sequence_rule_search_order)

    @raise_null_argument
    def apply_sequence_rule_query(self, sequence_rule_query):
        raise Unimplemented()

    def inspect_sequence_rule_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_sequence_rule_sequencing(self, sequence_rule_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_sequence_rule_query_from_inspector(self, sequence_rule_query_inspector):
        raise Unimplemented()


class SequenceRuleEnablerLookupSession(abc_assessment_authoring_sessions.SequenceRuleEnablerLookupSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerLookupSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_lookup_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_sequence_rule_enabler_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_sequence_rule_enabler_view()

    def use_plenary_sequence_rule_enabler_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_sequence_rule_enabler_view()

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def use_active_sequence_rule_enabler_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_active_composition_view
        return self._provider_session.use_active_sequence_rule_enabler_view()

    def use_any_status_sequence_rule_enabler_view(self):
        # Implemented from azosid template for -
        # osid.composition.CompositionLookupSession.use_any_status_composition_view
        return self._provider_session.use_any_status_sequence_rule_enabler_view()

    @raise_null_argument
    def get_sequence_rule_enabler(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enabler(sequence_rule_enabler_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_query()
        query.match_id(sequence_rule_enabler_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_sequence_rule_enablers_by_ids(self, sequence_rule_enabler_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enablers_by_ids(sequence_rule_enabler_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_query()
        for sequence_rule_enabler_id in (sequence_rule_enabler_ids):
            query.match_id(sequence_rule_enabler_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rule_enablers_by_genus_type(self, sequence_rule_enabler_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enablers_by_genus_type(sequence_rule_enabler_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_query()
        query.match_genus_type(sequence_rule_enabler_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rule_enablers_by_parent_genus_type(self, sequence_rule_enabler_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enablers_by_parent_genus_type(sequence_rule_enabler_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_query()
        query.match_parent_genus_type(sequence_rule_enabler_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rule_enablers_by_record_type(self, sequence_rule_enabler_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enablers_by_record_type(sequence_rule_enabler_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_query()
        query.match_record_type(sequence_rule_enabler_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rule_enablers_on_date(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_sequence_rule_enablers_on_date_with_agent(self, agent_id, from_, to):
        raise Unimplemented()

    def get_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enablers()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_query()
        query.match_any(match=True)
        return self._try_harder(query)

    sequence_rule_enablers = property(fget=get_sequence_rule_enablers)


class SequenceRuleEnablerQuerySession(abc_assessment_authoring_sessions.SequenceRuleEnablerQuerySession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerQuerySession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_search_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_bank_ids()))

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def get_sequence_rule_enabler_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.SequenceRuleEnablerQueryWrapper(self._provider_session.get_sequence_rule_enabler_query())

    sequence_rule_enabler_query = property(fget=get_sequence_rule_enabler_query)

    @raise_null_argument
    def get_sequence_rule_enablers_by_query(self, sequence_rule_enabler_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(sequence_rule_enabler_query, '_cat_id_args_list'):
            raise Unsupported('sequence_rule_enabler_query not from this session')
        for kwargs in sequence_rule_enabler_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                sequence_rule_enabler_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_sequence_rule_enablers_by_query(sequence_rule_enabler_query)
        self._check_search_conditions()
        result = self._try_harder(sequence_rule_enabler_query)
        sequence_rule_enabler_query._provider_query.clear_bank_terms()
        return result


class SequenceRuleEnablerSearchSession(abc_assessment_authoring_sessions.SequenceRuleEnablerSearchSession, SequenceRuleEnablerQuerySession):
    """Adapts underlying SequenceRuleEnablerSearchSession methodswith authorization checks."""

    def get_sequence_rule_enabler_search(self):
        """Pass through to provider SequenceRuleEnablerSearchSession.get_sequence_rule_enabler_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enabler_search()

    sequence_rule_enabler_search = property(fget=get_sequence_rule_enabler_search)

    def get_sequence_rule_enabler_search_order(self):
        raise Unimplemented()

    sequence_rule_enabler_search_order = property(fget=get_sequence_rule_enabler_search_order)

    @raise_null_argument
    def get_sequence_rule_enablers_by_search(self, sequence_rule_enabler_query, sequence_rule_enabler_search):
        """Pass through to provider SequenceRuleEnablerSearchSession.get_sequence_rule_enablers_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enablers_by_search(sequence_rule_enabler_query, sequence_rule_enabler_search)

    @raise_null_argument
    def get_sequence_rule_enabler_query_from_inspector(self, sequence_rule_enabler_query_inspector):
        raise Unimplemented()


class SequenceRuleEnablerAdminSession(abc_assessment_authoring_sessions.SequenceRuleEnablerAdminSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerAdminSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_create_sequence_rule_enabler(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_sequence_rule_enabler_with_record_types(self, sequence_rule_enabler_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if sequence_rule_enabler_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_sequence_rule_enabler_form_for_create(self, sequence_rule_enabler_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enabler_form_for_create(sequence_rule_enabler_record_types)

    @raise_null_argument
    def create_sequence_rule_enabler(self, sequence_rule_enabler_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_sequence_rule_enabler(sequence_rule_enabler_form)

    def can_update_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_sequence_rule_enabler_form_for_update(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_sequence_rule_enabler('update', sequence_rule_enabler_id):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enabler_form_for_update(sequence_rule_enabler_id)

    def duplicate_sequence_rule_enabler(self, sequence_rule_enabler_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_sequence_rule_enabler(sequence_rule_enabler_id)

    @raise_null_argument
    def update_sequence_rule_enabler(self, sequence_rule_enabler_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_sequence_rule_enabler(sequence_rule_enabler_form)

    def can_delete_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_sequence_rule_enabler(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_sequence_rule_enabler('delete', sequence_rule_enabler_id):
            raise PermissionDenied()
        return self._provider_session.delete_sequence_rule_enabler(sequence_rule_enabler_id)

    def can_manage_sequence_rule_enabler_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_sequence_rule_enabler(self, sequence_rule_enabler_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_sequence_rule_enabler('alias', sequence_rule_enabler_id):
            raise PermissionDenied()
        return self._provider_session.alias_sequence_rule_enabler(sequence_rule_enabler_id, alias_id)


class SequenceRuleEnablerNotificationSession(abc_assessment_authoring_sessions.SequenceRuleEnablerNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerNotificationSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_register_for_sequence_rule_enabler_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    def reliable_sequence_rule_enabler_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_sequence_rule_enabler_notifications()

    def unreliable_sequence_rule_enabler_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_sequence_rule_enabler_notifications()

    @raise_null_argument
    def acknowledge_sequence_rule_enabler_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_sequence_rule_enablers()

    def register_for_changed_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_sequence_rule_enablers()

    @raise_null_argument
    def register_for_changed_sequence_rule_enabler(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_sequence_rule_enabler(sequence_rule_enabler_id)

    def register_for_deleted_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_sequence_rule_enablers()

    @raise_null_argument
    def register_for_deleted_sequence_rule_enabler(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_sequence_rule_enabler(sequence_rule_enabler_id)

    def reliable_sequence_rule_enabler_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_sequence_rule_enabler_notifications()

    def unreliable_sequence_rule_enabler_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_sequence_rule_enabler_notifications()

    @raise_null_argument
    def acknowledge_sequence_rule_enabler_notification(self, notification_id):
        raise Unimplemented()


class SequenceRuleEnablerBankSession(abc_assessment_authoring_sessions.SequenceRuleEnablerBankSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerBankSession methodswith authorization checks."""

    def can_lookup_sequence_rule_enabler_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_sequence_rule_enabler_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_sequence_rule_enabler_bank_view()

    def use_plenary_sequence_rule_enabler_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_sequence_rule_enabler_bank_view()

    @raise_null_argument
    def get_sequence_rule_enabler_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enabler_ids_by_bank(bank_id)

    @raise_null_argument
    def get_sequence_rule_enablers_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enabler_ids_by_bank(bank_id)

    @raise_null_argument
    def get_sequence_rule_enabler_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enabler_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_sequence_rule_enablers_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_sequence_rule_enablers_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_sequence_rule_enabler(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_sequence_rule_enabler(sequence_rule_enabler_id)

    @raise_null_argument
    def get_banks_by_sequence_rule_enabler(self, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_sequence_rule_enabler(sequence_rule_enabler_id)


class SequenceRuleEnablerBankAssignmentSession(abc_assessment_authoring_sessions.SequenceRuleEnablerBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerBankAssignmentSession methodswith authorization checks."""

    def can_assign_sequence_rule_enablers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_sequence_rule_enablers_to_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bank_id)

    @raise_null_argument
    def get_assignable_bank_ids(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids()

    @raise_null_argument
    def get_assignable_bank_ids_for_sequence_rule_enabler(self, bank_id, sequence_rule_enabler_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_sequence_rule_enabler(sequence_rule_enabler_id)

    @raise_null_argument
    def assign_sequence_rule_enabler_to_bank(self, sequence_rule_enabler_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_sequence_rule_enabler_to_bank(sequence_rule_enabler_id, bank_id)

    @raise_null_argument
    def unassign_sequence_rule_enabler_from_bank(self, sequence_rule_enabler_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_sequence_rule_enabler_from_bank(sequence_rule_enabler_id, bank_id)


class SequenceRuleEnablerSmartBankSession(abc_assessment_authoring_sessions.SequenceRuleEnablerSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerSmartBankSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_manage_smart_banks(self):
        raise Unimplemented()

    def get_sequence_rule_enabler_query(self):
        raise Unimplemented()

    sequence_rule_enabler_query = property(fget=get_sequence_rule_enabler_query)

    def get_sequence_rule_enabler_search_order(self):
        raise Unimplemented()

    sequence_rule_enabler_search_order = property(fget=get_sequence_rule_enabler_search_order)

    @raise_null_argument
    def apply_sequence_rule_enabler_query(self, sequence_rule_enabler_query):
        raise Unimplemented()

    def inspect_sequence_rule_enabler_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_sequence_rule_enabler_sequencing(self, sequence_rule_enabler_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_sequence_rule_enabler_query_from_inspector(self, sequence_rule_enabler_query_inspector):
        raise Unimplemented()


class SequenceRuleEnablerRuleLookupSession(abc_assessment_authoring_sessions.SequenceRuleEnablerRuleLookupSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerRuleLookupSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_lookup_sequence_rule_enabler_rules(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_sequence_rule_enabler_rule_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_sequence_rule_enabler_rule_view()

    def use_plenary_sequence_rule_enabler_rule_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_sequence_rule_enabler_rule_view()

    def use_federated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_bank_view()
        if self._query_session:
            self._query_session.use_federated_bank_view()

    def use_isolated_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_bank_view()
        if self._query_session:
            self._query_session.use_isolated_bank_view()

    @raise_null_argument
    def get_sequence_rule_enabler_ids_for_sequence_rule(self, sequence_rule_id):
        raise Unimplemented()

    @raise_null_argument
    def get_sequence_rule_enablers_for_sequence_rule(self, sequence_rule_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_sequence_rule_enablers_for_sequence_rule(sequence_rule_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_enabler_rule_query()
        query.match_sequence_rule_id(sequence_rule_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_sequence_rule_ids_for_sequence_rule_enabler(self, sequence_rule_enabler_id):
        raise Unimplemented()

    @raise_null_argument
    def get_sequence_rules_for_sequence_rule_enabler(self, sequence_rule_enabler_id):
        raise Unimplemented()


class SequenceRuleEnablerRuleApplicationSession(abc_assessment_authoring_sessions.SequenceRuleEnablerRuleApplicationSession, osid_sessions.OsidSession):
    """Adapts underlying SequenceRuleEnablerRuleApplicationSession methodswith authorization checks."""

    def get_bank_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_bank_id()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_bank()

    bank = property(fget=get_bank)

    def can_assign_sequence_rule_enablers(self):
        raise Unimplemented()

    @raise_null_argument
    def assign_sequence_rule_enabler_to_sequence_rule(self, sequence_rule_enabler_id, sequence_rule_id):
        raise Unimplemented()

    @raise_null_argument
    def unassign_sequence_rule_enabler_from_sequence_rule(self, sequence_rule_enabler_id, sequence_rule_id):
        raise Unimplemented()

    def can_sequence_sequence_rule_enablers(self):
        raise Unimplemented()

    @raise_null_argument
    def move_sequence_rule_enabler_ahead(self, sequence_rule_enabler_id, sequence_rule_id, reference_id):
        raise Unimplemented()

    @raise_null_argument
    def move_sequence_rule_enabler_behind(self, sequence_rule_enabler_id, sequence_rule_id, reference_id):
        raise Unimplemented()

    @raise_null_argument
    def order_sequence_rule_enablers(self, sequence_rule_enabler_ids, sequence_rule_id):
        raise Unimplemented()
