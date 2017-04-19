"""AuthZ Adapter implementations of learning managers."""
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
from dlkit.manager_impls.learning import managers as learning_managers


class LearningProfile(osid_managers.OsidProfile, learning_managers.LearningProfile):
    """Adapts underlying LearningProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_objective_bank_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_objective_bank_hierarchy_session()
        except Unimplemented:
            return None

    def supports_objective_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_lookup()

    def supports_objective_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_query()

    def supports_objective_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_admin()

    def supports_objective_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_hierarchy()

    def supports_objective_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_hierarchy_design()

    def supports_objective_sequencing(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_sequencing()

    def supports_objective_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_objective_bank()

    def supports_objective_objective_bank_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_objective_bank_assignment()

    def supports_objective_requisite(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_requisite()

    def supports_objective_requisite_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_requisite_assignment()

    def supports_activity_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_lookup()

    def supports_activity_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_admin()

    def supports_activity_objective_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_objective_bank()

    def supports_activity_objective_bank_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_objective_bank_assignment()

    def supports_proficiency_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_proficiency_lookup()

    def supports_proficiency_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_proficiency_query()

    def supports_proficiency_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_proficiency_admin()

    def supports_objective_bank_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_lookup()

    def supports_objective_bank_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_admin()

    def supports_objective_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_hierarchy()

    def supports_objective_bank_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_hierarchy_design()

    def get_objective_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_record_types()

    objective_record_types = property(fget=get_objective_record_types)

    def get_objective_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_search_record_types()

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def get_activity_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_activity_record_types()

    activity_record_types = property(fget=get_activity_record_types)

    def get_activity_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_activity_search_record_types()

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def get_proficiency_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_proficiency_record_types()

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def get_proficiency_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_proficiency_search_record_types()

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def get_objective_bank_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_bank_record_types()

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def get_objective_bank_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_bank_search_record_types()

    objective_bank_search_record_types = property(fget=get_objective_bank_search_record_types)


class LearningManager(osid_managers.OsidManager, LearningProfile, learning_managers.LearningManager):
    """Adapts underlying LearningManager methodswith authorization checks."""
    def __init__(self):
        LearningProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:learningProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('LEARNING', provider_impl)
        # need to add version argument

    def get_objective_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_objective_query_session()
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveLookupSession')(
                provider_session=self._provider_manager.get_objective_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    objective_lookup_session = property(fget=get_objective_lookup_session)

    @raise_null_argument
    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_objective_query_session_for_objective_bank(objective_bank_id)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveLookupSession')(
                provider_session=self._provider_manager.get_objective_lookup_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_objective_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_objective_query_session()
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveQuerySession')(
                provider_session=self._provider_manager.get_objective_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    objective_query_session = property(fget=get_objective_query_session)

    @raise_null_argument
    def get_objective_query_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_objective_query_session_for_objective_bank(objective_bank_id)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveQuerySession')(
                provider_session=self._provider_manager.get_objective_query_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_objective_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveAdminSession')(
                provider_session=self._provider_manager.get_objective_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_admin_session = property(fget=get_objective_admin_session)

    @raise_null_argument
    def get_objective_admin_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveAdminSession')(
                provider_session=self._provider_manager.get_objective_admin_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_objective_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveHierarchySession')(
                provider_session=self._provider_manager.get_objective_hierarchy_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    @raise_null_argument
    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveHierarchySession')(
                provider_session=self._provider_manager.get_objective_hierarchy_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_objective_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveHierarchyDesignSession')(
                provider_session=self._provider_manager.get_objective_hierarchy_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    @raise_null_argument
    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveHierarchyDesignSession')(
                provider_session=self._provider_manager.get_objective_hierarchy_design_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_objective_sequencing_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveSequencingSession')(
                provider_session=self._provider_manager.get_objective_sequencing_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    @raise_null_argument
    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveSequencingSession')(
                provider_session=self._provider_manager.get_objective_sequencing_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_objective_objective_bank_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveObjectiveBankSession')(
                provider_session=self._provider_manager.get_objective_objective_bank_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    def get_objective_objective_bank_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveObjectiveBankAssignmentSession')(
                provider_session=self._provider_manager.get_objective_objective_bank_assignment_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    def get_objective_requisite_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteSession')(
                provider_session=self._provider_manager.get_objective_requisite_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_requisite_session = property(fget=get_objective_requisite_session)

    @raise_null_argument
    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteSession')(
                provider_session=self._provider_manager.get_objective_requisite_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_objective_requisite_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteAssignmentSession')(
                provider_session=self._provider_manager.get_objective_requisite_assignment_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    @raise_null_argument
    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteAssignmentSession')(
                provider_session=self._provider_manager.get_objective_requisite_assignment_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_activity_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_activity_query_session()
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ActivityLookupSession')(
                provider_session=self._provider_manager.get_activity_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    activity_lookup_session = property(fget=get_activity_lookup_session)

    @raise_null_argument
    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_activity_query_session_for_objective_bank(objective_bank_id)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ActivityLookupSession')(
                provider_session=self._provider_manager.get_activity_lookup_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_activity_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ActivityAdminSession')(
                provider_session=self._provider_manager.get_activity_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    activity_admin_session = property(fget=get_activity_admin_session)

    @raise_null_argument
    def get_activity_admin_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ActivityAdminSession')(
                provider_session=self._provider_manager.get_activity_admin_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_activity_objective_bank_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ActivityObjectiveBankSession')(
                provider_session=self._provider_manager.get_activity_objective_bank_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    def get_activity_objective_bank_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ActivityObjectiveBankAssignmentSession')(
                provider_session=self._provider_manager.get_activity_objective_bank_assignment_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    def get_proficiency_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session()
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyLookupSession')(
                provider_session=self._provider_manager.get_proficiency_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    @raise_null_argument
    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session_for_objective_bank(objective_bank_id)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyLookupSession')(
                provider_session=self._provider_manager.get_proficiency_lookup_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_proficiency_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session()
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyQuerySession')(
                provider_session=self._provider_manager.get_proficiency_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    proficiency_query_session = property(fget=get_proficiency_query_session)

    @raise_null_argument
    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session_for_objective_bank(objective_bank_id)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyQuerySession')(
                provider_session=self._provider_manager.get_proficiency_query_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_proficiency_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ProficiencyAdminSession')(
                provider_session=self._provider_manager.get_proficiency_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    @raise_null_argument
    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ProficiencyAdminSession')(
                provider_session=self._provider_manager.get_proficiency_admin_session_for_objective_bank(objective_bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_objective_bank_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankLookupSession')(
                provider_session=self._provider_manager.get_objective_bank_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    def get_objective_bank_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankAdminSession')(
                provider_session=self._provider_manager.get_objective_bank_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    def get_objective_bank_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankHierarchySession')(
                provider_session=self._provider_manager.get_objective_bank_hierarchy_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    def get_objective_bank_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankHierarchyDesignSession')(
                provider_session=self._provider_manager.get_objective_bank_hierarchy_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    objective_bank_hierarchy_design_session = property(fget=get_objective_bank_hierarchy_design_session)

    def get_learning_batch_manager(self):
        raise Unimplemented()

    learning_batch_manager = property(fget=get_learning_batch_manager)


class LearningProxyManager(osid_managers.OsidProxyManager, LearningProfile, learning_managers.LearningProxyManager):
    """Adapts underlying LearningProxyManager methodswith authorization checks."""
    def __init__(self):
        LearningProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:learningProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('LEARNING', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_objective_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_objective_query_session(proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveLookupSession')(
                provider_session=self._provider_manager.get_objective_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_objective_query_session_for_objective_bank(objective_bank_id, proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveLookupSession')(
                provider_session=self._provider_manager.get_objective_lookup_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_objective_query_session(proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveQuerySession')(
                provider_session=self._provider_manager.get_objective_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_query_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_objective_query_session_for_objective_bank(objective_bank_id, proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ObjectiveQuerySession')(
                provider_session=self._provider_manager.get_objective_query_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveAdminSession')(
                provider_session=self._provider_manager.get_objective_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveAdminSession')(
                provider_session=self._provider_manager.get_objective_admin_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveHierarchySession')(
                provider_session=self._provider_manager.get_objective_hierarchy_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveHierarchySession')(
                provider_session=self._provider_manager.get_objective_hierarchy_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveHierarchyDesignSession')(
                provider_session=self._provider_manager.get_objective_hierarchy_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveHierarchyDesignSession')(
                provider_session=self._provider_manager.get_objective_hierarchy_design_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_sequencing_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveSequencingSession')(
                provider_session=self._provider_manager.get_objective_sequencing_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveSequencingSession')(
                provider_session=self._provider_manager.get_objective_sequencing_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_objective_bank_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveObjectiveBankSession')(
                provider_session=self._provider_manager.get_objective_objective_bank_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_objective_bank_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveObjectiveBankAssignmentSession')(
                provider_session=self._provider_manager.get_objective_objective_bank_assignment_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_requisite_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteSession')(
                provider_session=self._provider_manager.get_objective_requisite_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteSession')(
                provider_session=self._provider_manager.get_objective_requisite_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_requisite_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteAssignmentSession')(
                provider_session=self._provider_manager.get_objective_requisite_assignment_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ObjectiveRequisiteAssignmentSession')(
                provider_session=self._provider_manager.get_objective_requisite_assignment_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_activity_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_activity_query_session(proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ActivityLookupSession')(
                provider_session=self._provider_manager.get_activity_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_activity_query_session_for_objective_bank(objective_bank_id, proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ActivityLookupSession')(
                provider_session=self._provider_manager.get_activity_lookup_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_activity_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ActivityAdminSession')(
                provider_session=self._provider_manager.get_activity_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_activity_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ActivityAdminSession')(
                provider_session=self._provider_manager.get_activity_admin_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_activity_objective_bank_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ActivityObjectiveBankSession')(
                provider_session=self._provider_manager.get_activity_objective_bank_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_activity_objective_bank_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ActivityObjectiveBankAssignmentSession')(
                provider_session=self._provider_manager.get_activity_objective_bank_assignment_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_proficiency_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session(proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyLookupSession')(
                provider_session=self._provider_manager.get_proficiency_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session_for_objective_bank(objective_bank_id, proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyLookupSession')(
                provider_session=self._provider_manager.get_proficiency_lookup_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_proficiency_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session(proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyQuerySession')(
                provider_session=self._provider_manager.get_proficiency_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_proficiency_query_session_for_objective_bank(objective_bank_id, proxy)
            query_session.use_federated_objective_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'ProficiencyQuerySession')(
                provider_session=self._provider_manager.get_proficiency_query_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_proficiency_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ProficiencyAdminSession')(
                provider_session=self._provider_manager.get_proficiency_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ProficiencyAdminSession')(
                provider_session=self._provider_manager.get_proficiency_admin_session_for_objective_bank(objective_bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_bank_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankLookupSession')(
                provider_session=self._provider_manager.get_objective_bank_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_bank_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankAdminSession')(
                provider_session=self._provider_manager.get_objective_bank_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_bank_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankHierarchySession')(
                provider_session=self._provider_manager.get_objective_bank_hierarchy_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_objective_bank_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ObjectiveBankHierarchyDesignSession')(
                provider_session=self._provider_manager.get_objective_bank_hierarchy_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_learning_batch_proxy_manager(self):
        raise Unimplemented()

    learning_batch_proxy_manager = property(fget=get_learning_batch_proxy_manager)
