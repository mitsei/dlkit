"""DLKit Services implementations of learning service."""
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
from dlkit.abstract_osid.learning import objects as abc_learning_objects
from dlkit.manager_impls.learning import managers as learning_managers


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


class LearningProfile(osid.OsidProfile, learning_managers.LearningProfile):
    """LearningProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_objective_lookup(self):
        """Pass through to provider supports_objective_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_lookup()

    def supports_objective_query(self):
        """Pass through to provider supports_objective_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_query()

    def supports_objective_admin(self):
        """Pass through to provider supports_objective_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_admin()

    def supports_objective_hierarchy(self):
        """Pass through to provider supports_objective_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_hierarchy()

    def supports_objective_hierarchy_design(self):
        """Pass through to provider supports_objective_hierarchy_design"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_hierarchy_design()

    def supports_objective_sequencing(self):
        """Pass through to provider supports_objective_sequencing"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_sequencing()

    def supports_objective_objective_bank(self):
        """Pass through to provider supports_objective_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_objective_bank()

    def supports_objective_objective_bank_assignment(self):
        """Pass through to provider supports_objective_objective_bank_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_objective_bank_assignment()

    def supports_objective_requisite(self):
        """Pass through to provider supports_objective_requisite"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_requisite()

    def supports_objective_requisite_assignment(self):
        """Pass through to provider supports_objective_requisite_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_requisite_assignment()

    def supports_activity_lookup(self):
        """Pass through to provider supports_activity_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_lookup()

    def supports_activity_admin(self):
        """Pass through to provider supports_activity_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_admin()

    def supports_activity_objective_bank(self):
        """Pass through to provider supports_activity_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_objective_bank()

    def supports_activity_objective_bank_assignment(self):
        """Pass through to provider supports_activity_objective_bank_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_activity_objective_bank_assignment()

    def supports_proficiency_lookup(self):
        """Pass through to provider supports_proficiency_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_proficiency_lookup()

    def supports_proficiency_query(self):
        """Pass through to provider supports_proficiency_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_proficiency_query()

    def supports_proficiency_admin(self):
        """Pass through to provider supports_proficiency_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_proficiency_admin()

    def supports_objective_bank_lookup(self):
        """Pass through to provider supports_objective_bank_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_lookup()

    def supports_objective_bank_admin(self):
        """Pass through to provider supports_objective_bank_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_admin()

    def supports_objective_bank_hierarchy(self):
        """Pass through to provider supports_objective_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_hierarchy()

    def supports_objective_bank_hierarchy_design(self):
        """Pass through to provider supports_objective_bank_hierarchy_design"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_objective_bank_hierarchy_design()

    def get_objective_record_types(self):
        """Pass through to provider get_objective_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_record_types()

    objective_record_types = property(fget=get_objective_record_types)

    def get_objective_search_record_types(self):
        """Pass through to provider get_objective_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_search_record_types()

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def get_activity_record_types(self):
        """Pass through to provider get_activity_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_activity_record_types()

    activity_record_types = property(fget=get_activity_record_types)

    def get_activity_search_record_types(self):
        """Pass through to provider get_activity_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_activity_search_record_types()

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def get_proficiency_record_types(self):
        """Pass through to provider get_proficiency_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_proficiency_record_types()

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def get_proficiency_search_record_types(self):
        """Pass through to provider get_proficiency_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_proficiency_search_record_types()

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def get_objective_bank_record_types(self):
        """Pass through to provider get_objective_bank_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_bank_record_types()

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def get_objective_bank_search_record_types(self):
        """Pass through to provider get_objective_bank_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_objective_bank_search_record_types()

    objective_bank_search_record_types = property(fget=get_objective_bank_search_record_types)


class LearningManager(osid.OsidManager, osid.OsidSession, LearningProfile, learning_managers.LearningManager):
    """LearningManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._objective_bank_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_objective_bank_view(self, session):
        """Sets the underlying objective_bank view to match current view"""
        if self._objective_bank_view == COMPARATIVE:
            try:
                session.use_comparative_objective_bank_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_objective_bank_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_objective_bank_view(session)
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
        parameter_id = Id('parameter:learningProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('LEARNING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('LEARNING', provider_impl)

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

    def get_objective_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_objective_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_lookup_session(*args, **kwargs)

    objective_lookup_session = property(fget=get_objective_lookup_session)

    def get_objective_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_lookup_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_lookup_session_for_objective_bank(*args, **kwargs)

    def get_objective_query_session(self, *args, **kwargs):
        """Pass through to provider get_objective_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_query_session(*args, **kwargs)

    objective_query_session = property(fget=get_objective_query_session)

    def get_objective_query_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_query_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_query_session_for_objective_bank(*args, **kwargs)

    def get_objective_admin_session(self, *args, **kwargs):
        """Pass through to provider get_objective_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_admin_session(*args, **kwargs)

    objective_admin_session = property(fget=get_objective_admin_session)

    def get_objective_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_admin_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_admin_session_for_objective_bank(*args, **kwargs)

    def get_objective_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_hierarchy_session(*args, **kwargs)

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    def get_objective_hierarchy_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_hierarchy_session_for_objective_bank(*args, **kwargs)

    def get_objective_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_design_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_hierarchy_design_session(*args, **kwargs)

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    def get_objective_hierarchy_design_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_design_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_hierarchy_design_session_for_objective_bank(*args, **kwargs)

    def get_objective_sequencing_session(self, *args, **kwargs):
        """Pass through to provider get_objective_sequencing_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_sequencing_session(*args, **kwargs)

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    def get_objective_sequencing_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_sequencing_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_sequencing_session_for_objective_bank(*args, **kwargs)

    def get_objective_objective_bank_session(self, *args, **kwargs):
        """Pass through to provider get_objective_objective_bank_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_objective_objective_bank_session(*args, **kwargs)

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    def get_objective_objective_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_objective_objective_bank_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_objective_objective_bank_assignment_session(*args, **kwargs)

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    def get_objective_requisite_session(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_requisite_session(*args, **kwargs)

    objective_requisite_session = property(fget=get_objective_requisite_session)

    def get_objective_requisite_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_requisite_session_for_objective_bank(*args, **kwargs)

    def get_objective_requisite_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_objective_requisite_assignment_session(*args, **kwargs)

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    def get_objective_requisite_assignment_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_assignment_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_objective_requisite_assignment_session_for_objective_bank(*args, **kwargs)

    def get_activity_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_activity_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_activity_lookup_session(*args, **kwargs)

    activity_lookup_session = property(fget=get_activity_lookup_session)

    def get_activity_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_activity_lookup_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_activity_lookup_session_for_objective_bank(*args, **kwargs)

    def get_activity_admin_session(self, *args, **kwargs):
        """Pass through to provider get_activity_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_activity_admin_session(*args, **kwargs)

    activity_admin_session = property(fget=get_activity_admin_session)

    def get_activity_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_activity_admin_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_activity_admin_session_for_objective_bank(*args, **kwargs)

    def get_activity_objective_bank_session(self, *args, **kwargs):
        """Pass through to provider get_activity_objective_bank_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_activity_objective_bank_session(*args, **kwargs)

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    def get_activity_objective_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_activity_objective_bank_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_activity_objective_bank_assignment_session(*args, **kwargs)

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    def get_proficiency_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_proficiency_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_proficiency_lookup_session(*args, **kwargs)

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    def get_proficiency_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_proficiency_lookup_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_proficiency_lookup_session_for_objective_bank(*args, **kwargs)

    def get_proficiency_query_session(self, *args, **kwargs):
        """Pass through to provider get_proficiency_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_proficiency_query_session(*args, **kwargs)

    proficiency_query_session = property(fget=get_proficiency_query_session)

    def get_proficiency_query_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_proficiency_query_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_proficiency_query_session_for_objective_bank(*args, **kwargs)

    def get_proficiency_admin_session(self, *args, **kwargs):
        """Pass through to provider get_proficiency_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_proficiency_admin_session(*args, **kwargs)

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    def get_proficiency_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_proficiency_admin_session_for_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_proficiency_admin_session_for_objective_bank(*args, **kwargs)

    def get_objective_bank_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_objective_bank_lookup_session(*args, **kwargs)

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    def get_objective_bank_admin_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_objective_bank_admin_session(*args, **kwargs)

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    def get_objective_bank_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_hierarchy_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_objective_bank_hierarchy_session(*args, **kwargs)

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    def get_objective_bank_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_hierarchy_design_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_objective_bank_hierarchy_design_session(*args, **kwargs)

    objective_bank_hierarchy_design_session = property(fget=get_objective_bank_hierarchy_design_session)

    def get_learning_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    learning_batch_manager = property(fget=get_learning_batch_manager)
##
# The following methods are from osid.learning.ObjectiveObjectiveBankSession

    def can_lookup_objective_objective_bank_mappings(self):
        """Pass through to provider ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('objective_objective_bank_session').can_lookup_objective_objective_bank_mappings()

    def use_comparative_objective_bank_view(self):
        """Pass through to provider ObjectiveObjectiveBankSession.use_comparative_objective_bank_view"""
        self._objective_bank_view = COMPARATIVE
        # self._get_provider_session('objective_objective_bank_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_objective_bank_view()
            except AttributeError:
                pass

    def use_plenary_objective_bank_view(self):
        """Pass through to provider ObjectiveObjectiveBankSession.use_plenary_objective_bank_view"""
        self._objective_bank_view = PLENARY
        # self._get_provider_session('objective_objective_bank_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_objective_bank_view()
            except AttributeError:
                pass

    def get_objective_ids_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('objective_objective_bank_session').get_objective_ids_by_objective_bank(*args, **kwargs)

    def get_objectives_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objectives_by_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('objective_objective_bank_session').get_objectives_by_objective_bank(*args, **kwargs)

    def get_objective_ids_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('objective_objective_bank_session').get_objective_ids_by_objective_banks(*args, **kwargs)

    def get_objectives_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objectives_by_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('objective_objective_bank_session').get_objectives_by_objective_banks(*args, **kwargs)

    def get_objective_bank_ids_by_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('objective_objective_bank_session').get_objective_bank_ids_by_objective(*args, **kwargs)

    def get_objective_banks_by_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_banks_by_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        catalogs = self._get_provider_session('objective_objective_bank_session').get_objective_banks_by_objective(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)
##
# The following methods are from osid.learning.ObjectiveObjectiveBankAssignmentSession

    def can_assign_objectives(self):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.can_assign_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('objective_objective_bank_assignment_session').can_assign_objectives()

    def can_assign_objectives_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('objective_objective_bank_assignment_session').can_assign_objectives_to_objective_bank(*args, **kwargs)

    def get_assignable_objective_bank_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        return self._get_provider_session('objective_objective_bank_assignment_session').get_assignable_objective_bank_ids(*args, **kwargs)

    def get_assignable_objective_bank_ids_for_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('objective_objective_bank_assignment_session').get_assignable_objective_bank_ids_for_objective(*args, **kwargs)

    def assign_objective_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('objective_objective_bank_assignment_session').assign_objective_to_objective_bank(*args, **kwargs)

    def unassign_objective_from_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('objective_objective_bank_assignment_session').unassign_objective_from_objective_bank(*args, **kwargs)

    def reassign_proficiency_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ActivityObjectiveBankSession

    def can_lookup_activity_objective_bank_mappings(self):
        """Pass through to provider ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('activity_objective_bank_session').can_lookup_activity_objective_bank_mappings()

    def get_activity_ids_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activity_ids_by_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('activity_objective_bank_session').get_activity_ids_by_objective_bank(*args, **kwargs)

    def get_activities_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activities_by_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('activity_objective_bank_session').get_activities_by_objective_bank(*args, **kwargs)

    def get_activity_ids_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activity_ids_by_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('activity_objective_bank_session').get_activity_ids_by_objective_banks(*args, **kwargs)

    def get_activities_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activities_by_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('activity_objective_bank_session').get_activities_by_objective_banks(*args, **kwargs)

    def get_objective_bank_ids_by_activity(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_objective_bank_ids_by_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('activity_objective_bank_session').get_objective_bank_ids_by_activity(*args, **kwargs)

    def get_objective_banks_by_activity(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_objective_banks_by_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        catalogs = self._get_provider_session('activity_objective_bank_session').get_objective_banks_by_activity(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)
##
# The following methods are from osid.learning.ActivityObjectiveBankAssignmentSession

    def can_assign_activities(self):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.can_assign_activities"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('activity_objective_bank_assignment_session').can_assign_activities()

    def can_assign_activities_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('activity_objective_bank_assignment_session').can_assign_activities_to_objective_bank(*args, **kwargs)

    def get_assignable_objective_bank_ids_for_activity(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('activity_objective_bank_assignment_session').get_assignable_objective_bank_ids_for_activity(*args, **kwargs)

    def assign_activity_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('activity_objective_bank_assignment_session').assign_activity_to_objective_bank(*args, **kwargs)

    def unassign_activity_from_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('activity_objective_bank_assignment_session').unassign_activity_from_objective_bank(*args, **kwargs)

    def reassign_activity_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ObjectiveBankLookupSession

    def can_lookup_objective_banks(self):
        """Pass through to provider ObjectiveBankLookupSession.can_lookup_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('objective_bank_lookup_session').can_lookup_objective_banks()

    def get_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_bank_lookup_session').get_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_objective_banks_by_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_record_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_provider(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks(self):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks()
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    objective_banks = property(fget=get_objective_banks)
##
# The following methods are from osid.learning.ObjectiveBankAdminSession

    def can_create_objective_banks(self):
        """Pass through to provider ObjectiveBankAdminSession.can_create_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('objective_bank_admin_session').can_create_objective_banks()

    def can_create_objective_bank_with_record_types(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.can_create_objective_bank_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('objective_bank_admin_session').can_create_objective_bank_with_record_types(*args, **kwargs)

    def get_objective_bank_form_for_create(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.get_objective_bank_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('objective_bank_admin_session').get_objective_bank_form_for_create(*args, **kwargs)

    def create_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.create_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_bank_admin_session').create_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_objective_banks(self):
        """Pass through to provider ObjectiveBankAdminSession.can_update_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('objective_bank_admin_session').can_update_objective_banks()

    def get_objective_bank_form_for_update(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.get_objective_bank_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('objective_bank_admin_session').get_objective_bank_form_for_update(*args, **kwargs)

    def get_objective_bank_form(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.get_objective_bank_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'objective_bank_record_types' in kwargs:
            return self.get_objective_bank_form_for_create(*args, **kwargs)
        else:
            return self.get_objective_bank_form_for_update(*args, **kwargs)

    def update_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.update_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_bank_admin_session').update_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    def save_objective_bank(self, objective_bank_form, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.update_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if objective_bank_form.is_for_update():
            return self.update_objective_bank(objective_bank_form, *args, **kwargs)
        else:
            return self.create_objective_bank(objective_bank_form, *args, **kwargs)

    def can_delete_objective_banks(self):
        """Pass through to provider ObjectiveBankAdminSession.can_delete_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('objective_bank_admin_session').can_delete_objective_banks()

    def delete_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.delete_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('objective_bank_admin_session').delete_objective_bank(*args, **kwargs)

    def can_manage_objective_bank_aliases(self):
        """Pass through to provider ObjectiveBankAdminSession.can_manage_objective_bank_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('objective_bank_admin_session').can_manage_objective_bank_aliases()

    def alias_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.alias_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.alias_bin
        self._get_provider_session('objective_bank_admin_session').alias_objective_bank(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_id(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_hierarchy_id"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_hierarchy_id()

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_hierarchy()

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
        """Pass through to provider ObjectiveBankHierarchySession.can_access_objective_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._get_provider_session('objective_bank_hierarchy_session').can_access_objective_bank_hierarchy()

    def get_root_objective_bank_ids(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_root_objective_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_root_objective_bank_ids()

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_root_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        return self._get_provider_session('objective_bank_hierarchy_session').get_root_objective_banks()

    root_objective_banks = property(fget=get_root_objective_banks)

    def has_parent_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.has_parent_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        return self._get_provider_session('objective_bank_hierarchy_session').has_parent_objective_banks(*args, **kwargs)

    def is_parent_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_parent_of_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        return self._get_provider_session('objective_bank_hierarchy_session').is_parent_of_objective_bank(*args, **kwargs)

    def get_parent_objective_bank_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_parent_objective_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_parent_objective_bank_ids(*args, **kwargs)

    def get_parent_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_parent_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        return self._get_provider_session('objective_bank_hierarchy_session').get_parent_objective_banks(*args, **kwargs)

    def is_ancestor_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_ancestor_of_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        return self._get_provider_session('objective_bank_hierarchy_session').is_ancestor_of_objective_bank(*args, **kwargs)

    def has_child_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.has_child_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        return self._get_provider_session('objective_bank_hierarchy_session').has_child_objective_banks(*args, **kwargs)

    def is_child_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_child_of_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        return self._get_provider_session('objective_bank_hierarchy_session').is_child_of_objective_bank(*args, **kwargs)

    def get_child_objective_bank_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_child_objective_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_child_objective_bank_ids(*args, **kwargs)

    def get_child_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_child_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bins
        return self._get_provider_session('objective_bank_hierarchy_session').get_child_objective_banks(*args, **kwargs)

    def is_descendant_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_descendant_of_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        return self._get_provider_session('objective_bank_hierarchy_session').is_descendant_of_objective_bank(*args, **kwargs)

    def get_objective_bank_node_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_node_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_node_ids(*args, **kwargs)

    def get_objective_bank_nodes(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_nodes"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_nodes(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveBankHierarchyDesignSession

    def can_modify_objective_bank_hierarchy(self):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._get_provider_session('objective_bank_hierarchy_design_session').can_modify_objective_bank_hierarchy()

    def create_objective_bank_hierarchy(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('objective_bank_hierarchy_design_session').create_objective_bank_hierarchy(*args, **kwargs)

    def delete_objective_bank_hierarchy(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('objective_bank_hierarchy_design_session').delete_objective_bank_hierarchy(*args, **kwargs)

    def add_root_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.add_root_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin
        self._get_provider_session('objective_bank_hierarchy_design_session').add_root_objective_bank(*args, **kwargs)

    def remove_root_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.remove_root_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_root_bin
        self._get_provider_session('objective_bank_hierarchy_design_session').remove_root_objective_bank(*args, **kwargs)

    def add_child_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.add_child_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_child_bin
        self._get_provider_session('objective_bank_hierarchy_design_session').add_child_objective_bank(*args, **kwargs)

    def remove_child_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.remove_child_objective_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bin
        self._get_provider_session('objective_bank_hierarchy_design_session').remove_child_objective_bank(*args, **kwargs)

    def remove_child_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.remove_child_objective_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bins
        self._get_provider_session('objective_bank_hierarchy_design_session').remove_child_objective_banks(*args, **kwargs)


class LearningProxyManager(osid.OsidProxyManager, LearningProfile, learning_managers.LearningProxyManager):
    """LearningProxyManager convenience adapter including related Session methods."""

    def get_objective_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return LearningManager.get_objective_lookup_session(*args, **kwargs)

    def get_objective_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return LearningManager.get_objective_lookup_session_for_objective_bank(*args, **kwargs)

    def get_objective_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return LearningManager.get_objective_query_session(*args, **kwargs)

    def get_objective_query_session_for_objective_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return LearningManager.get_objective_query_session_for_objective_bank(*args, **kwargs)

    def get_objective_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_hierarchy_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_hierarchy_design_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_sequencing_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_sequencing_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_objective_bank_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_objective_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_requisite_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_requisite_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_requisite_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_requisite_assignment_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activity_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return LearningManager.get_activity_lookup_session(*args, **kwargs)

    def get_activity_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return LearningManager.get_activity_lookup_session_for_objective_bank(*args, **kwargs)

    def get_activity_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activity_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activity_objective_bank_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activity_objective_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiency_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return LearningManager.get_proficiency_lookup_session(*args, **kwargs)

    def get_proficiency_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return LearningManager.get_proficiency_lookup_session_for_objective_bank(*args, **kwargs)

    def get_proficiency_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return LearningManager.get_proficiency_query_session(*args, **kwargs)

    def get_proficiency_query_session_for_objective_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return LearningManager.get_proficiency_query_session_for_objective_bank(*args, **kwargs)

    def get_proficiency_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiency_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_bank_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_bank_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_bank_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_bank_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_learning_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    learning_batch_proxy_manager = property(fget=get_learning_batch_proxy_manager)


class ObjectiveBank(abc_learning_objects.ObjectiveBank, osid.OsidSession, osid.OsidCatalog):
    """ObjectiveBank convenience adapter including related Session methods."""
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
        self._objective_bank_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_objective_bank_view(self, session):
        """Sets the underlying objective_bank view to match current view"""
        if self._objective_bank_view == FEDERATED:
            try:
                session.use_federated_objective_bank_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_objective_bank_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_objective_bank')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_objective_bank_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_objective_bank_id(self):
        """Gets the Id of this objective_bank."""
        return self._catalog_id

    def get_objective_bank(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
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

    def get_objective_bank_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ObjectiveLookupSession

    def can_lookup_objectives(self):
        """Pass through to provider ObjectiveLookupSession.can_lookup_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('objective_lookup_session').can_lookup_objectives()

    def use_comparative_objective_view(self):
        """Pass through to provider ObjectiveLookupSession.use_comparative_objective_view"""
        self._object_views['objective'] = COMPARATIVE
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_objective_view()
            except AttributeError:
                pass

    def use_plenary_objective_view(self):
        """Pass through to provider ObjectiveLookupSession.use_plenary_objective_view"""
        self._object_views['objective'] = PLENARY
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_objective_view()
            except AttributeError:
                pass

    def use_federated_objective_bank_view(self):
        """Pass through to provider ObjectiveLookupSession.use_federated_objective_bank_view"""
        self._objective_bank_view = FEDERATED
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_objective_bank_view()
            except AttributeError:
                pass

    def use_isolated_objective_bank_view(self):
        """Pass through to provider ObjectiveLookupSession.use_isolated_objective_bank_view"""
        self._objective_bank_view = ISOLATED
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_objective_bank_view()
            except AttributeError:
                pass

    def get_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('objective_lookup_session').get_objective(*args, **kwargs)

    def get_objectives_by_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('objective_lookup_session').get_objectives_by_ids(*args, **kwargs)

    def get_objectives_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('objective_lookup_session').get_objectives_by_genus_type(*args, **kwargs)

    def get_objectives_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('objective_lookup_session').get_objectives_by_parent_genus_type(*args, **kwargs)

    def get_objectives_by_record_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('objective_lookup_session').get_objectives_by_record_type(*args, **kwargs)

    def get_objectives(self):
        """Pass through to provider ObjectiveLookupSession.get_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('objective_lookup_session').get_objectives()

    objectives = property(fget=get_objectives)
##
# The following methods are from osid.learning.ObjectiveQuerySession

    def can_search_objectives(self):
        """Pass through to provider ObjectiveQuerySession.can_search_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('objective_query_session').can_search_objectives()

    def get_objective_query(self):
        """Pass through to provider ObjectiveQuerySession.get_objective_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('objective_query_session').get_objective_query()

    objective_query = property(fget=get_objective_query)

    def get_objectives_by_query(self, *args, **kwargs):
        """Pass through to provider ObjectiveQuerySession.get_objectives_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('objective_query_session').get_objectives_by_query(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveAdminSession

    def can_create_objectives(self):
        """Pass through to provider ObjectiveAdminSession.can_create_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('objective_admin_session').can_create_objectives()

    def can_create_objective_with_record_types(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.can_create_objective_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('objective_admin_session').can_create_objective_with_record_types(*args, **kwargs)

    def get_objective_form_for_create(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.get_objective_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('objective_admin_session').get_objective_form_for_create(*args, **kwargs)

    def create_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.create_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('objective_admin_session').create_objective(*args, **kwargs)

    def can_update_objectives(self):
        """Pass through to provider ObjectiveAdminSession.can_update_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('objective_admin_session').can_update_objectives()

    def get_objective_form_for_update(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.get_objective_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('objective_admin_session').get_objective_form_for_update(*args, **kwargs)

    def get_objective_form(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.get_objective_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'objective_record_types' in kwargs:
            return self.get_objective_form_for_create(*args, **kwargs)
        else:
            return self.get_objective_form_for_update(*args, **kwargs)

    def duplicate_objective(self, objective_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('objective_admin_session').duplicate_objective(objective_id)

    def update_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.update_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('objective_admin_session').update_objective(*args, **kwargs)

    def save_objective(self, objective_form, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.update_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if objective_form.is_for_update():
            return self.update_objective(objective_form, *args, **kwargs)
        else:
            return self.create_objective(objective_form, *args, **kwargs)

    def can_delete_objectives(self):
        """Pass through to provider ObjectiveAdminSession.can_delete_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('objective_admin_session').can_delete_objectives()

    def delete_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.delete_objective"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective
        self._get_provider_session('objective_admin_session').delete_objective(*args, **kwargs)

    def can_manage_objective_aliases(self):
        """Pass through to provider ObjectiveAdminSession.can_manage_objective_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('objective_admin_session').can_manage_objective_aliases()

    def alias_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.alias_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('objective_admin_session').alias_objective(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveHierarchySession

    def can_access_objective_hierarchy(self):
        """Pass through to provider ObjectiveHierarchySession.can_access_objective_hierarchy"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.can_access_subject_hierarchy_template
        return self._get_provider_session('objective_hierarchy_session').can_access_objective_hierarchy()

    def get_root_objective_ids(self):
        """Pass through to provider ObjectiveHierarchySession.get_root_objective_ids"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_root_subject_ids_template
        return self._get_provider_session('objective_hierarchy_session').get_root_objective_ids()

    root_objective_ids = property(fget=get_root_objective_ids)

    def get_root_objectives(self):
        """Pass through to provider ObjectiveHierarchySession.get_root_objectives"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_root_subjects_template
        return self._get_provider_session('objective_hierarchy_session').get_root_objectives()

    root_objectives = property(fget=get_root_objectives)

    def has_parent_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.has_parent_objectives"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.has_parent_subjects_template
        return self._get_provider_session('objective_hierarchy_session').has_parent_objectives(*args, **kwargs)

    def is_parent_of_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.is_parent_of_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.is_parent_of_subject_template
        return self._get_provider_session('objective_hierarchy_session').is_parent_of_objective(*args, **kwargs)

    def get_parent_objective_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_parent_objective_ids"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_parent_subject_ids_template
        return self._get_provider_session('objective_hierarchy_session').get_parent_objective_ids(*args, **kwargs)

    def get_parent_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_parent_objectives"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_parent_subjects_template
        return self._get_provider_session('objective_hierarchy_session').get_parent_objectives(*args, **kwargs)

    def is_ancestor_of_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.is_ancestor_of_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.is_ancestor_of_subject_template
        return self._get_provider_session('objective_hierarchy_session').is_ancestor_of_objective(*args, **kwargs)

    def has_child_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.has_child_objectives"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.has_child_subjects_template
        return self._get_provider_session('objective_hierarchy_session').has_child_objectives(*args, **kwargs)

    def is_child_of_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.is_child_of_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.is_child_of_subject_template
        return self._get_provider_session('objective_hierarchy_session').is_child_of_objective(*args, **kwargs)

    def get_child_objective_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_child_objective_ids"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_child_subject_ids_template
        return self._get_provider_session('objective_hierarchy_session').get_child_objective_ids(*args, **kwargs)

    def get_child_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_child_objectives"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_child_subjects_template
        return self._get_provider_session('objective_hierarchy_session').get_child_objectives(*args, **kwargs)

    def is_descendant_of_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.is_descendant_of_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.is_descendant_of_subject_template
        return self._get_provider_session('objective_hierarchy_session').is_descendant_of_objective(*args, **kwargs)

    def get_objective_node_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_objective_node_ids"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_subject_node_ids_template
        return self._get_provider_session('objective_hierarchy_session').get_objective_node_ids(*args, **kwargs)

    def get_objective_nodes(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_objective_nodes"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchySession.get_subject_nodes_template
        return self._get_provider_session('objective_hierarchy_session').get_objective_nodes(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveHierarchyDesignSession

    def can_modify_objective_hierarchy(self):
        """Pass through to provider ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchyDesignSession.can_modify_subject_hierarchy
        return self._get_provider_session('objective_hierarchy_design_session').can_modify_objective_hierarchy()

    def add_root_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.add_root_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchyDesignSession.add_root_subject
        self._get_provider_session('objective_hierarchy_design_session').add_root_objective(*args, **kwargs)

    def remove_root_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.remove_root_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchyDesignSession.remove_root_subject
        self._get_provider_session('objective_hierarchy_design_session').remove_root_objective(*args, **kwargs)

    def add_child_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.add_child_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchyDesignSession.add_child_subject
        self._get_provider_session('objective_hierarchy_design_session').add_child_objective(*args, **kwargs)

    def remove_child_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.remove_child_objective"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchyDesignSession.remove_child_subject
        self._get_provider_session('objective_hierarchy_design_session').remove_child_objective(*args, **kwargs)

    def remove_child_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.remove_child_objectives"""
        # Implemented from kitosid template for -
        # osid.ontology.SubjectHierarchyDesignSession.remove_child_subjects_template
        self._get_provider_session('objective_hierarchy_design_session').remove_child_objectives(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveSequencingSession

    def can_sequence_objectives(self):
        """Pass through to provider method"""
        return self._get_provider_session('objective_sequencing_session').can_sequence_objectives()

    def move_objective_ahead(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('objective_sequencing_session').move_objective_ahead(*args, **kwargs)

    def move_objective_behind(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('objective_sequencing_session').move_objective_behind(*args, **kwargs)

    def sequence_objectives(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('objective_sequencing_session').sequence_objectives(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveRequisiteSession

    def can_lookup_objective_prerequisites(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_requisite_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.get_requisite_objectives"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteSession.get_requisite_objectives
        return self._get_provider_session('objective_requisite_session').get_requisite_objectives(*args, **kwargs)

    def get_all_requisite_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.get_all_requisite_objectives"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteSession.get_all_requisite_objectives
        return self._get_provider_session('objective_requisite_session').get_all_requisite_objectives(*args, **kwargs)

    def get_dependent_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.get_dependent_objectives"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteSession.get_dependent_objectives
        return self._get_provider_session('objective_requisite_session').get_dependent_objectives(*args, **kwargs)

    def is_objective_required(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.is_objective_required"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteSession.is_objective_required
        return self._get_provider_session('objective_requisite_session').is_objective_required(*args, **kwargs)

    def get_equivalent_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.get_equivalent_objectives"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteSession.get_equivalent_objectives
        return self._get_provider_session('objective_requisite_session').get_equivalent_objectives(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveRequisiteAssignmentSession

    def can_assign_requisites(self):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.can_assign_requisites"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteAssignmentSession.can_assign_requisites
        return self._get_provider_session('objective_requisite_assignment_session').can_assign_requisites()

    def assign_objective_requisite(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.assign_objective_requisite"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteAssignmentSession.assign_objective_requisite
        return self._get_provider_session('objective_requisite_assignment_session').assign_objective_requisite(*args, **kwargs)

    def unassign_objective_requisite(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.unassign_objective_requisite"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteAssignmentSession.unassign_objective_requisite
        return self._get_provider_session('objective_requisite_assignment_session').unassign_objective_requisite(*args, **kwargs)

    def assign_equivalent_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.assign_equivalent_objective"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteAssignmentSession.assign_equivalent_objective
        return self._get_provider_session('objective_requisite_assignment_session').assign_equivalent_objective(*args, **kwargs)

    def unassign_equivalent_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective
        return self._get_provider_session('objective_requisite_assignment_session').unassign_equivalent_objective(*args, **kwargs)
##
# The following methods are from osid.learning.ActivityLookupSession

    def can_lookup_activities(self):
        """Pass through to provider ActivityLookupSession.can_lookup_activities"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('activity_lookup_session').can_lookup_activities()

    def use_comparative_activity_view(self):
        """Pass through to provider ActivityLookupSession.use_comparative_activity_view"""
        self._object_views['activity'] = COMPARATIVE
        # self._get_provider_session('activity_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_activity_view()
            except AttributeError:
                pass

    def use_plenary_activity_view(self):
        """Pass through to provider ActivityLookupSession.use_plenary_activity_view"""
        self._object_views['activity'] = PLENARY
        # self._get_provider_session('activity_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_activity_view()
            except AttributeError:
                pass

    def get_activity(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('activity_lookup_session').get_activity(*args, **kwargs)

    def get_activities_by_ids(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('activity_lookup_session').get_activities_by_ids(*args, **kwargs)

    def get_activities_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('activity_lookup_session').get_activities_by_genus_type(*args, **kwargs)

    def get_activities_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('activity_lookup_session').get_activities_by_parent_genus_type(*args, **kwargs)

    def get_activities_by_record_type(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('activity_lookup_session').get_activities_by_record_type(*args, **kwargs)

    def get_activities_for_objective(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_for_objective"""
        # Implemented from kitosid template for -
        # osid.resource.ActivityLookupSession.get_activities_for_objective
        return self._get_provider_session('activity_lookup_session').get_activities_for_objective(*args, **kwargs)

    def get_activities_for_objectives(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_for_objectives"""
        # Implemented from kitosid template for -
        # osid.resource.ActivityLookupSession.get_activities_for_objectives
        return self._get_provider_session('activity_lookup_session').get_activities_for_objectives(*args, **kwargs)

    def get_activities_by_asset(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activities_by_assets(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activities(self):
        """Pass through to provider ActivityLookupSession.get_activities"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('activity_lookup_session').get_activities()

    activities = property(fget=get_activities)
##
# The following methods are from osid.learning.ActivityAdminSession

    def can_create_activities(self):
        """Pass through to provider ActivityAdminSession.can_create_activities"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('activity_admin_session').can_create_activities()

    def can_create_activity_with_record_types(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.can_create_activity_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('activity_admin_session').can_create_activity_with_record_types(*args, **kwargs)

    def get_activity_form_for_create(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.get_activity_form_for_create"""
        # Implemented from -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        return self._get_provider_session('activity_admin_session').get_activity_form_for_create(*args, **kwargs)

    def create_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.create_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('activity_admin_session').create_activity(*args, **kwargs)

    def can_update_activities(self):
        """Pass through to provider ActivityAdminSession.can_update_activities"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('activity_admin_session').can_update_activities()

    def get_activity_form_for_update(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.get_activity_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('activity_admin_session').get_activity_form_for_update(*args, **kwargs)

    def get_activity_form(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.get_activity_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'activity_record_types' in kwargs:
            return self.get_activity_form_for_create(*args, **kwargs)
        else:
            return self.get_activity_form_for_update(*args, **kwargs)

    def duplicate_activity(self, activity_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('activity_admin_session').duplicate_activity(activity_id)

    def update_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.update_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('activity_admin_session').update_activity(*args, **kwargs)

    def save_activity(self, activity_form, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.update_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if activity_form.is_for_update():
            return self.update_activity(activity_form, *args, **kwargs)
        else:
            return self.create_activity(activity_form, *args, **kwargs)

    def can_delete_activities(self):
        """Pass through to provider ActivityAdminSession.can_delete_activities"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('activity_admin_session').can_delete_activities()

    def delete_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.delete_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('activity_admin_session').delete_activity(*args, **kwargs)

    def can_manage_activity_aliases(self):
        """Pass through to provider ActivityAdminSession.can_manage_activity_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('activity_admin_session').can_manage_activity_aliases()

    def alias_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.alias_activity"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('activity_admin_session').alias_activity(*args, **kwargs)
##
# The following methods are from osid.learning.ProficiencyLookupSession

    def can_lookup_proficiencies(self):
        """Pass through to provider ProficiencyLookupSession.can_lookup_proficiencies"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('proficiency_lookup_session').can_lookup_proficiencies()

    def use_comparative_proficiency_view(self):
        """Pass through to provider ProficiencyLookupSession.use_comparative_proficiency_view"""
        self._object_views['proficiency'] = COMPARATIVE
        # self._get_provider_session('proficiency_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_proficiency_view()
            except AttributeError:
                pass

    def use_plenary_proficiency_view(self):
        """Pass through to provider ProficiencyLookupSession.use_plenary_proficiency_view"""
        self._object_views['proficiency'] = PLENARY
        # self._get_provider_session('proficiency_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_proficiency_view()
            except AttributeError:
                pass

    def use_effective_proficiency_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_any_effective_proficiency_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiency"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiency(*args, **kwargs)

    def get_proficiencies_by_ids(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_ids(*args, **kwargs)

    def get_proficiencies_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_genus_type(*args, **kwargs)

    def get_proficiencies_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_parent_genus_type(*args, **kwargs)

    def get_proficiencies_by_record_type(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_record_type(*args, **kwargs)

    def get_proficiencies_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_objective_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_for_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_for_objective_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_resource(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resource"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_resource(*args, **kwargs)

    def get_proficiencies_for_resource_on_date(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resource_on_date"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_resource_on_date(*args, **kwargs)

    def get_proficiencies_by_genus_type_for_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_for_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_resources(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resources"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_resources(*args, **kwargs)

    def get_proficiencies_for_objective_and_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_objective_and_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_for_objective_and_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies(self):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies()

    proficiencies = property(fget=get_proficiencies)
##
# The following methods are from osid.learning.ProficiencyQuerySession

    def can_search_proficiencies(self):
        """Pass through to provider ProficiencyQuerySession.can_search_proficiencies"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('proficiency_query_session').can_search_proficiencies()

    def get_proficiency_query(self):
        """Pass through to provider ProficiencyQuerySession.get_proficiency_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('proficiency_query_session').get_proficiency_query()

    proficiency_query = property(fget=get_proficiency_query)

    def get_proficiencies_by_query(self, *args, **kwargs):
        """Pass through to provider ProficiencyQuerySession.get_proficiencies_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('proficiency_query_session').get_proficiencies_by_query(*args, **kwargs)
##
# The following methods are from osid.learning.ProficiencyAdminSession

    def can_create_proficiencies(self):
        """Pass through to provider ProficiencyAdminSession.can_create_proficiencies"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('proficiency_admin_session').can_create_proficiencies()

    def can_create_proficiency_with_record_types(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.can_create_proficiency_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('proficiency_admin_session').can_create_proficiency_with_record_types(*args, **kwargs)

    def get_proficiency_form_for_create(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.get_proficiency_form_for_create"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create_template
        return self._get_provider_session('proficiency_admin_session').get_proficiency_form_for_create(*args, **kwargs)

    def create_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.create_proficiency"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('proficiency_admin_session').create_proficiency(*args, **kwargs)

    def can_update_proficiencies(self):
        """Pass through to provider ProficiencyAdminSession.can_update_proficiencies"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('proficiency_admin_session').can_update_proficiencies()

    def get_proficiency_form_for_update(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.get_proficiency_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('proficiency_admin_session').get_proficiency_form_for_update(*args, **kwargs)

    def get_proficiency_form(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.get_proficiency_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'proficiency_record_types' in kwargs:
            return self.get_proficiency_form_for_create(*args, **kwargs)
        else:
            return self.get_proficiency_form_for_update(*args, **kwargs)

    def duplicate_proficiency(self, proficiency_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('proficiency_admin_session').duplicate_proficiency(proficiency_id)

    def update_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.update_proficiency"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('proficiency_admin_session').update_proficiency(*args, **kwargs)

    def save_proficiency(self, proficiency_form, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.update_proficiency"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if proficiency_form.is_for_update():
            return self.update_proficiency(proficiency_form, *args, **kwargs)
        else:
            return self.create_proficiency(proficiency_form, *args, **kwargs)

    def can_delete_proficiencies(self):
        """Pass through to provider ProficiencyAdminSession.can_delete_proficiencies"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('proficiency_admin_session').can_delete_proficiencies()

    def delete_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.delete_proficiency"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('proficiency_admin_session').delete_proficiency(*args, **kwargs)

    def delete_proficiencies(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def can_manage_proficiency_aliases(self):
        """Pass through to provider ProficiencyAdminSession.can_manage_proficiency_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('proficiency_admin_session').can_manage_proficiency_aliases()

    def alias_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.alias_proficiency"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('proficiency_admin_session').alias_proficiency(*args, **kwargs)


class ObjectiveBankList(abc_learning_objects.ObjectiveBankList, osid.OsidList):
    """ObjectiveBankList convenience adapter including related Session methods."""

    def get_next_objective_bank(self):
        """Gets next object"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        try:
            next_item = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        else:
            return next_item

    def next(self):
        """next method for enumerator"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        next_item = osid.OsidList.next(self)
        return next_item

    __next__ = next

    next_objective_bank = property(fget=get_next_objective_bank)

    def get_next_objective_banks(self, n):
        """gets next n objects from list"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            i = 0
            while i < n:
                try:
                    next_list.append(next(self))
                except StopIteration:
                    break
                i += 1
            return next_list
