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
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_lookup()

    def supports_objective_query(self):
        """Pass through to provider supports_objective_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_query()

    def supports_objective_admin(self):
        """Pass through to provider supports_objective_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_admin()

    def supports_objective_hierarchy(self):
        """Pass through to provider supports_objective_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_hierarchy()

    def supports_objective_hierarchy_design(self):
        """Pass through to provider supports_objective_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_hierarchy_design()

    def supports_objective_sequencing(self):
        """Pass through to provider supports_objective_sequencing"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_sequencing()

    def supports_objective_objective_bank(self):
        """Pass through to provider supports_objective_objective_bank"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_objective_bank()

    def supports_objective_objective_bank_assignment(self):
        """Pass through to provider supports_objective_objective_bank_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_objective_bank_assignment()

    def supports_objective_requisite(self):
        """Pass through to provider supports_objective_requisite"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_requisite()

    def supports_objective_requisite_assignment(self):
        """Pass through to provider supports_objective_requisite_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_requisite_assignment()

    def supports_activity_lookup(self):
        """Pass through to provider supports_activity_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_activity_lookup()

    def supports_activity_admin(self):
        """Pass through to provider supports_activity_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_activity_admin()

    def supports_activity_objective_bank(self):
        """Pass through to provider supports_activity_objective_bank"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_activity_objective_bank()

    def supports_activity_objective_bank_assignment(self):
        """Pass through to provider supports_activity_objective_bank_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_activity_objective_bank_assignment()

    def supports_proficiency_lookup(self):
        """Pass through to provider supports_proficiency_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_proficiency_lookup()

    def supports_proficiency_query(self):
        """Pass through to provider supports_proficiency_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_proficiency_query()

    def supports_proficiency_admin(self):
        """Pass through to provider supports_proficiency_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_proficiency_admin()

    def supports_objective_bank_lookup(self):
        """Pass through to provider supports_objective_bank_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_bank_lookup()

    def supports_objective_bank_admin(self):
        """Pass through to provider supports_objective_bank_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_bank_admin()

    def supports_objective_bank_hierarchy(self):
        """Pass through to provider supports_objective_bank_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_bank_hierarchy()

    def supports_objective_bank_hierarchy_design(self):
        """Pass through to provider supports_objective_bank_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_objective_bank_hierarchy_design()

    def get_objective_record_types(self):
        """Pass through to provider get_objective_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_objective_record_types()

    objective_record_types = property(fget=get_objective_record_types)

    def get_objective_search_record_types(self):
        """Pass through to provider get_objective_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_objective_search_record_types()

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def get_activity_record_types(self):
        """Pass through to provider get_activity_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_activity_record_types()

    activity_record_types = property(fget=get_activity_record_types)

    def get_activity_search_record_types(self):
        """Pass through to provider get_activity_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_activity_search_record_types()

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def get_proficiency_record_types(self):
        """Pass through to provider get_proficiency_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_proficiency_record_types()

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def get_proficiency_search_record_types(self):
        """Pass through to provider get_proficiency_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_proficiency_search_record_types()

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def get_objective_bank_record_types(self):
        """Pass through to provider get_objective_bank_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_objective_bank_record_types()

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def get_objective_bank_search_record_types(self):
        """Pass through to provider get_objective_bank_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
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
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_objective_lookup_session(*args, **kwargs)

    objective_lookup_session = property(fget=get_objective_lookup_session)

    def get_objective_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_lookup_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_objective_lookup_session_for_objective_bank(*args, **kwargs)

    def get_objective_query_session(self, *args, **kwargs):
        """Pass through to provider get_objective_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_objective_query_session(*args, **kwargs)

    objective_query_session = property(fget=get_objective_query_session)

    def get_objective_query_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_query_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_objective_query_session_for_objective_bank(*args, **kwargs)

    def get_objective_admin_session(self, *args, **kwargs):
        """Pass through to provider get_objective_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_admin_session(*args, **kwargs)

    objective_admin_session = property(fget=get_objective_admin_session)

    def get_objective_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_admin_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_objective_admin_session_for_objective_bank(*args, **kwargs)

    def get_objective_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_hierarchy_session(*args, **kwargs)

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    def get_objective_hierarchy_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_objective_hierarchy_session_for_objective_bank(*args, **kwargs)

    def get_objective_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_hierarchy_design_session(*args, **kwargs)

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    def get_objective_hierarchy_design_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_hierarchy_design_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_objective_hierarchy_design_session_for_objective_bank(*args, **kwargs)

    def get_objective_sequencing_session(self, *args, **kwargs):
        """Pass through to provider get_objective_sequencing_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_sequencing_session(*args, **kwargs)

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    def get_objective_sequencing_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_sequencing_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_objective_sequencing_session_for_objective_bank(*args, **kwargs)

    def get_objective_objective_bank_session(self, *args, **kwargs):
        """Pass through to provider get_objective_objective_bank_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_objective_bank_session(*args, **kwargs)

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    def get_objective_objective_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_objective_objective_bank_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_objective_bank_assignment_session(*args, **kwargs)

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    def get_objective_requisite_session(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_requisite_session(*args, **kwargs)

    objective_requisite_session = property(fget=get_objective_requisite_session)

    def get_objective_requisite_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_objective_requisite_session_for_objective_bank(*args, **kwargs)

    def get_objective_requisite_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_requisite_assignment_session(*args, **kwargs)

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    def get_objective_requisite_assignment_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_objective_requisite_assignment_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_objective_requisite_assignment_session_for_objective_bank(*args, **kwargs)

    def get_activity_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_activity_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_activity_lookup_session(*args, **kwargs)

    activity_lookup_session = property(fget=get_activity_lookup_session)

    def get_activity_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_activity_lookup_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_activity_lookup_session_for_objective_bank(*args, **kwargs)

    def get_activity_admin_session(self, *args, **kwargs):
        """Pass through to provider get_activity_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_activity_admin_session(*args, **kwargs)

    activity_admin_session = property(fget=get_activity_admin_session)

    def get_activity_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_activity_admin_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_activity_admin_session_for_objective_bank(*args, **kwargs)

    def get_activity_objective_bank_session(self, *args, **kwargs):
        """Pass through to provider get_activity_objective_bank_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_activity_objective_bank_session(*args, **kwargs)

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    def get_activity_objective_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_activity_objective_bank_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_activity_objective_bank_assignment_session(*args, **kwargs)

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    def get_proficiency_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_proficiency_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_proficiency_lookup_session(*args, **kwargs)

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    def get_proficiency_lookup_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_proficiency_lookup_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_proficiency_lookup_session_for_objective_bank(*args, **kwargs)

    def get_proficiency_query_session(self, *args, **kwargs):
        """Pass through to provider get_proficiency_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_proficiency_query_session(*args, **kwargs)

    proficiency_query_session = property(fget=get_proficiency_query_session)

    def get_proficiency_query_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_proficiency_query_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_proficiency_query_session_for_objective_bank(*args, **kwargs)

    def get_proficiency_admin_session(self, *args, **kwargs):
        """Pass through to provider get_proficiency_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_proficiency_admin_session(*args, **kwargs)

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    def get_proficiency_admin_session_for_objective_bank(self, *args, **kwargs):
        """Pass through to provider get_proficiency_admin_session_for_objective_bank"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_proficiency_admin_session_for_objective_bank(*args, **kwargs)

    def get_objective_bank_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_bank_lookup_session(*args, **kwargs)

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    def get_objective_bank_admin_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_bank_admin_session(*args, **kwargs)

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    def get_objective_bank_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_objective_bank_hierarchy_session(*args, **kwargs)

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    def get_objective_bank_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_objective_bank_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
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
        # Built from: templates/osid_session.GenericObjectCatalogSession.can_lookup_object_catalog_mappings
        return self._get_provider_session('objective_objective_bank_session').can_lookup_objective_objective_bank_mappings()

    def use_comparative_objective_bank_view(self):
        """Pass through to provider ObjectiveObjectiveBankSession.use_comparative_objective_bank_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._objective_bank_view = COMPARATIVE
        # self._get_provider_session('objective_objective_bank_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_objective_bank_view()
            except AttributeError:
                pass

    def use_plenary_objective_bank_view(self):
        """Pass through to provider ObjectiveObjectiveBankSession.use_plenary_objective_bank_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._objective_bank_view = PLENARY
        # self._get_provider_session('objective_objective_bank_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_objective_bank_view()
            except AttributeError:
                pass

    def get_objective_ids_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalog
        return self._get_provider_session('objective_objective_bank_session').get_objective_ids_by_objective_bank(*args, **kwargs)

    def get_objectives_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objectives_by_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalog
        return self._get_provider_session('objective_objective_bank_session').get_objectives_by_objective_bank(*args, **kwargs)

    def get_objective_ids_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalogs
        return self._get_provider_session('objective_objective_bank_session').get_objective_ids_by_objective_banks(*args, **kwargs)

    def get_objectives_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objectives_by_objective_banks"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalogs
        return self._get_provider_session('objective_objective_bank_session').get_objectives_by_objective_banks(*args, **kwargs)

    def get_objective_bank_ids_by_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalog_ids_by_object
        return self._get_provider_session('objective_objective_bank_session').get_objective_bank_ids_by_objective(*args, **kwargs)

    def get_objective_banks_by_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankSession.get_objective_banks_by_objective"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalogs_by_object
        catalogs = self._get_provider_session('objective_objective_bank_session').get_objective_banks_by_objective(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)
##
# The following methods are from osid.learning.ObjectiveObjectiveBankAssignmentSession

    def can_assign_objectives(self):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.can_assign_objectives"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects
        return self._get_provider_session('objective_objective_bank_assignment_session').can_assign_objectives()

    def can_assign_objectives_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects_to_catalog
        return self._get_provider_session('objective_objective_bank_assignment_session').can_assign_objectives_to_objective_bank(*args, **kwargs)

    def get_assignable_objective_bank_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids
        return self._get_provider_session('objective_objective_bank_assignment_session').get_assignable_objective_bank_ids(*args, **kwargs)

    def get_assignable_objective_bank_ids_for_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids_for_object
        return self._get_provider_session('objective_objective_bank_assignment_session').get_assignable_objective_bank_ids_for_objective(*args, **kwargs)

    def assign_objective_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.assign_object_to_catalog
        self._get_provider_session('objective_objective_bank_assignment_session').assign_objective_to_objective_bank(*args, **kwargs)

    def unassign_objective_from_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.unassign_object_from_catalog
        self._get_provider_session('objective_objective_bank_assignment_session').unassign_objective_from_objective_bank(*args, **kwargs)

    def reassign_proficiency_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.reassign_object_to_catalog
        self._get_provider_session('objective_objective_bank_assignment_session').reassign_proficiency_to_objective_bank(*args, **kwargs)
##
# The following methods are from osid.learning.ActivityObjectiveBankSession

    def can_lookup_activity_objective_bank_mappings(self):
        """Pass through to provider ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.can_lookup_object_catalog_mappings
        return self._get_provider_session('activity_objective_bank_session').can_lookup_activity_objective_bank_mappings()

    def get_activity_ids_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activity_ids_by_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalog
        return self._get_provider_session('activity_objective_bank_session').get_activity_ids_by_objective_bank(*args, **kwargs)

    def get_activities_by_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activities_by_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalog
        return self._get_provider_session('activity_objective_bank_session').get_activities_by_objective_bank(*args, **kwargs)

    def get_activity_ids_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activity_ids_by_objective_banks"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalogs
        return self._get_provider_session('activity_objective_bank_session').get_activity_ids_by_objective_banks(*args, **kwargs)

    def get_activities_by_objective_banks(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_activities_by_objective_banks"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalogs
        return self._get_provider_session('activity_objective_bank_session').get_activities_by_objective_banks(*args, **kwargs)

    def get_objective_bank_ids_by_activity(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_objective_bank_ids_by_activity"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalog_ids_by_object
        return self._get_provider_session('activity_objective_bank_session').get_objective_bank_ids_by_activity(*args, **kwargs)

    def get_objective_banks_by_activity(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankSession.get_objective_banks_by_activity"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalogs_by_object
        catalogs = self._get_provider_session('activity_objective_bank_session').get_objective_banks_by_activity(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)
##
# The following methods are from osid.learning.ActivityObjectiveBankAssignmentSession

    def can_assign_activities(self):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.can_assign_activities"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects
        return self._get_provider_session('activity_objective_bank_assignment_session').can_assign_activities()

    def can_assign_activities_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects_to_catalog
        return self._get_provider_session('activity_objective_bank_assignment_session').can_assign_activities_to_objective_bank(*args, **kwargs)

    def get_assignable_objective_bank_ids_for_activity(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids_for_object
        return self._get_provider_session('activity_objective_bank_assignment_session').get_assignable_objective_bank_ids_for_activity(*args, **kwargs)

    def assign_activity_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.assign_object_to_catalog
        self._get_provider_session('activity_objective_bank_assignment_session').assign_activity_to_objective_bank(*args, **kwargs)

    def unassign_activity_from_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.unassign_object_from_catalog
        self._get_provider_session('activity_objective_bank_assignment_session').unassign_activity_from_objective_bank(*args, **kwargs)

    def reassign_activity_to_objective_bank(self, *args, **kwargs):
        """Pass through to provider ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.reassign_object_to_catalog
        self._get_provider_session('activity_objective_bank_assignment_session').reassign_activity_to_objective_bank(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveBankLookupSession

    def can_lookup_objective_banks(self):
        """Pass through to provider ObjectiveBankLookupSession.can_lookup_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('objective_bank_lookup_session').can_lookup_objective_banks()

    def get_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_bank_lookup_session').get_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_objective_banks_by_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_record_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks_by_provider(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('objective_bank_lookup_session').get_objective_banks_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(ObjectiveBank(self._provider_manager, cat, self._runtime, self._proxy))
        return ObjectiveBankList(cat_list)

    def get_objective_banks(self):
        """Pass through to provider ObjectiveBankLookupSession.get_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
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
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('objective_bank_admin_session').can_create_objective_banks()

    def can_create_objective_bank_with_record_types(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.can_create_objective_bank_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('objective_bank_admin_session').can_create_objective_bank_with_record_types(*args, **kwargs)

    def get_objective_bank_form_for_create(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.get_objective_bank_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('objective_bank_admin_session').get_objective_bank_form_for_create(*args, **kwargs)

    def create_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.create_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_bank_admin_session').create_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_objective_banks(self):
        """Pass through to provider ObjectiveBankAdminSession.can_update_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('objective_bank_admin_session').can_update_objective_banks()

    def get_objective_bank_form_for_update(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.get_objective_bank_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('objective_bank_admin_session').get_objective_bank_form_for_update(*args, **kwargs)

    def update_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.update_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_bank_admin_session').update_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_objective_banks(self):
        """Pass through to provider ObjectiveBankAdminSession.can_delete_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('objective_bank_admin_session').can_delete_objective_banks()

    def delete_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.delete_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.delete_catalog
        self._get_provider_session('objective_bank_admin_session').delete_objective_bank(*args, **kwargs)

    def can_manage_objective_bank_aliases(self):
        """Pass through to provider ObjectiveBankAdminSession.can_manage_objective_bank_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('objective_bank_admin_session').can_manage_objective_bank_aliases()

    def alias_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankAdminSession.alias_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('objective_bank_admin_session').alias_objective_bank(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_id(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_hierarchy_id()

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_hierarchy()

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
        """Pass through to provider ObjectiveBankHierarchySession.can_access_objective_bank_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('objective_bank_hierarchy_session').can_access_objective_bank_hierarchy()

    def get_root_objective_bank_ids(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_root_objective_bank_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_root_objective_bank_ids()

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        """Pass through to provider ObjectiveBankHierarchySession.get_root_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('objective_bank_hierarchy_session').get_root_objective_banks()

    root_objective_banks = property(fget=get_root_objective_banks)

    def has_parent_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.has_parent_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('objective_bank_hierarchy_session').has_parent_objective_banks(*args, **kwargs)

    def is_parent_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_parent_of_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('objective_bank_hierarchy_session').is_parent_of_objective_bank(*args, **kwargs)

    def get_parent_objective_bank_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_parent_objective_bank_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_parent_objective_bank_ids(*args, **kwargs)

    def get_parent_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_parent_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('objective_bank_hierarchy_session').get_parent_objective_banks(*args, **kwargs)

    def is_ancestor_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_ancestor_of_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('objective_bank_hierarchy_session').is_ancestor_of_objective_bank(*args, **kwargs)

    def has_child_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.has_child_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('objective_bank_hierarchy_session').has_child_objective_banks(*args, **kwargs)

    def is_child_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_child_of_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('objective_bank_hierarchy_session').is_child_of_objective_bank(*args, **kwargs)

    def get_child_objective_bank_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_child_objective_bank_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_child_objective_bank_ids(*args, **kwargs)

    def get_child_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_child_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('objective_bank_hierarchy_session').get_child_objective_banks(*args, **kwargs)

    def is_descendant_of_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.is_descendant_of_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('objective_bank_hierarchy_session').is_descendant_of_objective_bank(*args, **kwargs)

    def get_objective_bank_node_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_node_ids(*args, **kwargs)

    def get_objective_bank_nodes(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchySession.get_objective_bank_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('objective_bank_hierarchy_session').get_objective_bank_nodes(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveBankHierarchyDesignSession

    def can_modify_objective_bank_hierarchy(self):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('objective_bank_hierarchy_design_session').can_modify_objective_bank_hierarchy()

    def add_root_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.add_root_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('objective_bank_hierarchy_design_session').add_root_objective_bank(*args, **kwargs)

    def remove_root_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.remove_root_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('objective_bank_hierarchy_design_session').remove_root_objective_bank(*args, **kwargs)

    def add_child_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.add_child_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('objective_bank_hierarchy_design_session').add_child_objective_bank(*args, **kwargs)

    def remove_child_objective_bank(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.remove_child_objective_bank"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('objective_bank_hierarchy_design_session').remove_child_objective_bank(*args, **kwargs)

    def remove_child_objective_banks(self, *args, **kwargs):
        """Pass through to provider ObjectiveBankHierarchyDesignSession.remove_child_objective_banks"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('objective_bank_hierarchy_design_session').remove_child_objective_banks(*args, **kwargs)


class LearningProxyManager(osid.OsidProxyManager, LearningProfile, LearningManager, learning_managers.LearningProxyManager):
    """LearningProxyManager convenience adapter including related Session methods."""
    pass


class ObjectiveBank(abc_learning_objects.ObjectiveBank, osid.OsidSession, osid.OsidCatalog):
    """ObjectiveBank convenience adapter including related Session methods."""
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

    def get_objective_bank_id(self):
        """Pass through to provider ObjectiveLookupSession.get_objective_bank_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('objective_lookup_session').get_objective_bank_id()

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Pass through to provider ObjectiveLookupSession.get_objective_bank"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return ObjectiveBank(
            self._provider_manager,
            self._get_provider_session('objective_lookup_session').get_objective_bank(*args, **kwargs),
            self._runtime,
            self._proxy)

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objectives(self):
        """Pass through to provider ObjectiveLookupSession.can_lookup_objectives"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('objective_lookup_session').can_lookup_objectives()

    def use_comparative_objective_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider ObjectiveLookupSession.use_comparative_objective_view"""
        self._object_views['objective'] = COMPARATIVE
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_objective_view()
            except AttributeError:
                pass

    def use_plenary_objective_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider ObjectiveLookupSession.use_plenary_objective_view"""
        self._object_views['objective'] = PLENARY
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_objective_view()
            except AttributeError:
                pass

    def use_federated_objective_bank_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_federated_catalog_view
        """Pass through to provider ObjectiveLookupSession.use_federated_objective_bank_view"""
        self._objective_bank_view = FEDERATED
        # self._get_provider_session('objective_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_objective_bank_view()
            except AttributeError:
                pass

    def use_isolated_objective_bank_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_isolated_catalog_view
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('objective_lookup_session').get_objective(*args, **kwargs)

    def get_objectives_by_ids(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('objective_lookup_session').get_objectives_by_ids(*args, **kwargs)

    def get_objectives_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('objective_lookup_session').get_objectives_by_genus_type(*args, **kwargs)

    def get_objectives_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('objective_lookup_session').get_objectives_by_parent_genus_type(*args, **kwargs)

    def get_objectives_by_record_type(self, *args, **kwargs):
        """Pass through to provider ObjectiveLookupSession.get_objectives_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('objective_lookup_session').get_objectives_by_record_type(*args, **kwargs)

    def get_objectives(self):
        """Pass through to provider ObjectiveLookupSession.get_objectives"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('objective_lookup_session').get_objectives()

    objectives = property(fget=get_objectives)
##
# The following methods are from osid.learning.ObjectiveQuerySession

    def can_search_objectives(self):
        """Pass through to provider ObjectiveQuerySession.can_search_objectives"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('objective_query_session').can_search_objectives()

    def get_objective_query(self):
        """Pass through to provider ObjectiveQuerySession.get_objective_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('objective_query_session').get_objective_query()

    objective_query = property(fget=get_objective_query)

    def get_objectives_by_query(self, *args, **kwargs):
        """Pass through to provider ObjectiveQuerySession.get_objectives_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('objective_query_session').get_objectives_by_query(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveAdminSession

    def can_create_objectives(self):
        """Pass through to provider ObjectiveAdminSession.can_create_objectives"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('objective_admin_session').can_create_objectives()

    def can_create_objective_with_record_types(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.can_create_objective_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('objective_admin_session').can_create_objective_with_record_types(*args, **kwargs)

    def get_objective_form_for_create(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.get_objective_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_create
        return self._get_provider_session('objective_admin_session').get_objective_form_for_create(*args, **kwargs)

    def create_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.create_objective"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('objective_admin_session').create_objective(*args, **kwargs)

    def can_update_objectives(self):
        """Pass through to provider ObjectiveAdminSession.can_update_objectives"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('objective_admin_session').can_update_objectives()

    def get_objective_form_for_update(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.get_objective_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('objective_admin_session').get_objective_form_for_update(*args, **kwargs)

    def update_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.update_objective"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('objective_admin_session').update_objective(*args, **kwargs)

    def can_delete_objectives(self):
        """Pass through to provider ObjectiveAdminSession.can_delete_objectives"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('objective_admin_session').can_delete_objectives()

    def delete_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.delete_objective"""
        # Built from: templates/osid_session.GenericRequisiteObjectAdminSession.delete_requisite_object
        self._get_provider_session('objective_admin_session').delete_objective(*args, **kwargs)

    def can_manage_objective_aliases(self):
        """Pass through to provider ObjectiveAdminSession.can_manage_objective_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('objective_admin_session').can_manage_objective_aliases()

    def alias_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveAdminSession.alias_objective"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('objective_admin_session').alias_objective(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_id(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_access_objective_hierarchy(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_root_objective_ids(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    root_objective_ids = property(fget=get_root_objective_ids)

    def get_root_objectives(self):
        """Pass through to provider ObjectiveHierarchySession.get_root_objectives"""
        # Built from: templates/osid_session.GenericObjectHierarchySession.get_root_objects
        return self._get_provider_session('objective_hierarchy_session').get_root_objectives()

    root_objectives = property(fget=get_root_objectives)

    def has_parent_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def is_parent_of_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_parent_objective_ids(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_parent_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def is_ancestor_of_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def has_child_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def is_child_of_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_child_objective_ids(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_child_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchySession.get_child_objectives"""
        # Built from: templates/osid_session.GenericObjectHierarchySession.get_child_objects
        return self._get_provider_session('objective_hierarchy_session').get_child_objectives(*args, **kwargs)

    def is_descendant_of_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_node_ids(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_objective_nodes(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ObjectiveHierarchyDesignSession

    def can_modify_objective_hierarchy(self):
        """Pass through to provider ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy"""
        # Built from: templates/osid_session.GenericObjectHierarchyDesignSession.can_modify_object_hierarchy
        return self._get_provider_session('objective_hierarchy_design_session').can_modify_objective_hierarchy()

    def add_root_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.add_root_objective"""
        # Built from: templates/osid_session.GenericObjectHierarchyDesignSession.add_root_object
        return self._get_provider_session('objective_hierarchy_design_session').add_root_objective(*args, **kwargs)

    def remove_root_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.remove_root_objective"""
        # Built from: templates/osid_session.GenericObjectHierarchyDesignSession.remove_root_object
        return self._get_provider_session('objective_hierarchy_design_session').remove_root_objective(*args, **kwargs)

    def add_child_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.add_child_objective"""
        # Built from: templates/osid_session.GenericObjectHierarchyDesignSession.add_child_object
        return self._get_provider_session('objective_hierarchy_design_session').add_child_objective(*args, **kwargs)

    def remove_child_objective(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.remove_child_objective"""
        # Built from: templates/osid_session.GenericObjectHierarchyDesignSession.remove_child_object
        return self._get_provider_session('objective_hierarchy_design_session').remove_child_objective(*args, **kwargs)

    def remove_child_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveHierarchyDesignSession.remove_child_objectives"""
        # Built from: templates/osid_session.GenericObjectHierarchyDesignSession.remove_child_objects
        return self._get_provider_session('objective_hierarchy_design_session').remove_child_objectives(*args, **kwargs)
##
# The following methods are from osid.learning.ObjectiveSequencingSession

    def can_sequence_objectives(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def move_objective_ahead(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def move_objective_behind(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def sequence_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ObjectiveRequisiteSession

    def can_lookup_objective_prerequisites(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_requisite_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.get_requisite_objectives"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_requisite_objects
        return self._get_provider_session('objective_requisite_session').get_requisite_objectives(*args, **kwargs)

    def get_all_requisite_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_dependent_objectives(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteSession.get_dependent_objectives"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_dependent_objects
        return self._get_provider_session('objective_requisite_session').get_dependent_objectives(*args, **kwargs)

    def is_objective_required(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_equivalent_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ObjectiveRequisiteAssignmentSession

    def can_assign_requisites(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def assign_objective_requisite(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.assign_objective_requisite"""
        # Built from: templates/osid_session.GenericRelationshipAdminSession.assign_object_requisite
        return self._get_provider_session('objective_requisite_assignment_session').assign_objective_requisite(*args, **kwargs)

    def unassign_objective_requisite(self, *args, **kwargs):
        """Pass through to provider ObjectiveRequisiteAssignmentSession.unassign_objective_requisite"""
        # Built from: templates/osid_session.GenericRelationshipAdminSession.unassign_object_requisite
        return self._get_provider_session('objective_requisite_assignment_session').unassign_objective_requisite(*args, **kwargs)

    def assign_equivalent_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def unassign_equivalent_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.learning.ActivityLookupSession

    def can_lookup_activities(self):
        """Pass through to provider ActivityLookupSession.can_lookup_activities"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('activity_lookup_session').can_lookup_activities()

    def use_comparative_activity_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider ActivityLookupSession.use_comparative_activity_view"""
        self._object_views['activity'] = COMPARATIVE
        # self._get_provider_session('activity_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_activity_view()
            except AttributeError:
                pass

    def use_plenary_activity_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('activity_lookup_session').get_activity(*args, **kwargs)

    def get_activities_by_ids(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('activity_lookup_session').get_activities_by_ids(*args, **kwargs)

    def get_activities_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('activity_lookup_session').get_activities_by_genus_type(*args, **kwargs)

    def get_activities_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('activity_lookup_session').get_activities_by_parent_genus_type(*args, **kwargs)

    def get_activities_by_record_type(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('activity_lookup_session').get_activities_by_record_type(*args, **kwargs)

    def get_activities_for_objective(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_for_objective"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_subjugated_objects_for_object
        return self._get_provider_session('activity_lookup_session').get_activities_for_objective(*args, **kwargs)

    def get_activities_for_objectives(self, *args, **kwargs):
        """Pass through to provider ActivityLookupSession.get_activities_for_objectives"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_subjugated_objects_for_objects
        return self._get_provider_session('activity_lookup_session').get_activities_for_objectives(*args, **kwargs)

    def get_activities_by_asset(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activities_by_assets(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_activities(self):
        """Pass through to provider ActivityLookupSession.get_activities"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('activity_lookup_session').get_activities()

    activities = property(fget=get_activities)
##
# The following methods are from osid.learning.ActivityAdminSession

    def can_create_activities(self):
        """Pass through to provider ActivityAdminSession.can_create_activities"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('activity_admin_session').can_create_activities()

    def can_create_activity_with_record_types(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.can_create_activity_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('activity_admin_session').can_create_activity_with_record_types(*args, **kwargs)

    def get_activity_form_for_create(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.get_activity_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_subjugated_object_form_for_create
        return self._get_provider_session('activity_admin_session').get_activity_form_for_create(*args, **kwargs)

    def create_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.create_activity"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('activity_admin_session').create_activity(*args, **kwargs)

    def can_update_activities(self):
        """Pass through to provider ActivityAdminSession.can_update_activities"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('activity_admin_session').can_update_activities()

    def get_activity_form_for_update(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.get_activity_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('activity_admin_session').get_activity_form_for_update(*args, **kwargs)

    def update_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.update_activity"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('activity_admin_session').update_activity(*args, **kwargs)

    def can_delete_activities(self):
        """Pass through to provider ActivityAdminSession.can_delete_activities"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('activity_admin_session').can_delete_activities()

    def delete_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.delete_activity"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('activity_admin_session').delete_activity(*args, **kwargs)

    def can_manage_activity_aliases(self):
        """Pass through to provider ActivityAdminSession.can_manage_activity_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('activity_admin_session').can_manage_activity_aliases()

    def alias_activity(self, *args, **kwargs):
        """Pass through to provider ActivityAdminSession.alias_activity"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('activity_admin_session').alias_activity(*args, **kwargs)
##
# The following methods are from osid.learning.ProficiencyLookupSession

    def can_lookup_proficiencies(self):
        """Pass through to provider ProficiencyLookupSession.can_lookup_proficiencies"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('proficiency_lookup_session').can_lookup_proficiencies()

    def use_comparative_proficiency_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider ProficiencyLookupSession.use_comparative_proficiency_view"""
        self._object_views['proficiency'] = COMPARATIVE
        # self._get_provider_session('proficiency_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_proficiency_view()
            except AttributeError:
                pass

    def use_plenary_proficiency_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('proficiency_lookup_session').get_proficiency(*args, **kwargs)

    def get_proficiencies_by_ids(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_ids(*args, **kwargs)

    def get_proficiencies_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_genus_type(*args, **kwargs)

    def get_proficiencies_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_parent_genus_type(*args, **kwargs)

    def get_proficiencies_by_record_type(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_record_type(*args, **kwargs)

    def get_proficiencies_on_date(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_on_date
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_on_date(*args, **kwargs)

    def get_proficiencies_by_genus_type_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_objective(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_objective"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_objective(*args, **kwargs)

    def get_proficiencies_for_objective_on_date(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_objective_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination_on_date
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_objective_on_date(*args, **kwargs)

    def get_proficiencies_by_genus_type_for_objective(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_genus_type_for_objective"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_destination
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_genus_type_for_objective(*args, **kwargs)

    def get_proficiencies_by_genus_type_for_objective_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_for_objectives(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_objectives"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_objectives(*args, **kwargs)

    def get_proficiencies_for_resource(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resource"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_resource(*args, **kwargs)

    def get_proficiencies_for_resource_on_date(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resource_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source_on_date
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_resource_on_date(*args, **kwargs)

    def get_proficiencies_by_genus_type_for_resource(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_genus_type_for_resource"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_source
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_genus_type_for_resource(*args, **kwargs)

    def get_proficiencies_by_genus_type_for_resource_on_date(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_genus_type_for_resource_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_genus_type_for_resource_on_date(*args, **kwargs)

    def get_proficiencies_for_resources(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_resources"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_resources(*args, **kwargs)

    def get_proficiencies_for_objective_and_resource(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_for_objective_and_resource"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_peers
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_for_objective_and_resource(*args, **kwargs)

    def get_proficiencies_for_objective_and_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies_by_genus_type_for_objective_and_resource(self, *args, **kwargs):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies_by_genus_type_for_objective_and_resource"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_peers
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies_by_genus_type_for_objective_and_resource(*args, **kwargs)

    def get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_proficiencies(self):
        """Pass through to provider ProficiencyLookupSession.get_proficiencies"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('proficiency_lookup_session').get_proficiencies()

    proficiencies = property(fget=get_proficiencies)
##
# The following methods are from osid.learning.ProficiencyQuerySession

    def can_search_proficiencies(self):
        """Pass through to provider ProficiencyQuerySession.can_search_proficiencies"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('proficiency_query_session').can_search_proficiencies()

    def get_proficiency_query(self):
        """Pass through to provider ProficiencyQuerySession.get_proficiency_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('proficiency_query_session').get_proficiency_query()

    proficiency_query = property(fget=get_proficiency_query)

    def get_proficiencies_by_query(self, *args, **kwargs):
        """Pass through to provider ProficiencyQuerySession.get_proficiencies_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('proficiency_query_session').get_proficiencies_by_query(*args, **kwargs)
##
# The following methods are from osid.learning.ProficiencyAdminSession

    def can_create_proficiencies(self):
        """Pass through to provider ProficiencyAdminSession.can_create_proficiencies"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('proficiency_admin_session').can_create_proficiencies()

    def can_create_proficiency_with_record_types(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.can_create_proficiency_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('proficiency_admin_session').can_create_proficiency_with_record_types(*args, **kwargs)

    def get_proficiency_form_for_create(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.get_proficiency_form_for_create"""
        # Built from: templates/osid_session.GenericRelationshipAdminSession.get_relationship_form_for_create
        return self._get_provider_session('proficiency_admin_session').get_proficiency_form_for_create(*args, **kwargs)

    def create_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.create_proficiency"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('proficiency_admin_session').create_proficiency(*args, **kwargs)

    def can_update_proficiencies(self):
        """Pass through to provider ProficiencyAdminSession.can_update_proficiencies"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('proficiency_admin_session').can_update_proficiencies()

    def get_proficiency_form_for_update(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.get_proficiency_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('proficiency_admin_session').get_proficiency_form_for_update(*args, **kwargs)

    def update_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.update_proficiency"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('proficiency_admin_session').update_proficiency(*args, **kwargs)

    def can_delete_proficiencies(self):
        """Pass through to provider ProficiencyAdminSession.can_delete_proficiencies"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('proficiency_admin_session').can_delete_proficiencies()

    def delete_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.delete_proficiency"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('proficiency_admin_session').delete_proficiency(*args, **kwargs)

    def delete_proficiencies(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def can_manage_proficiency_aliases(self):
        """Pass through to provider ProficiencyAdminSession.can_manage_proficiency_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('proficiency_admin_session').can_manage_proficiency_aliases()

    def alias_proficiency(self, *args, **kwargs):
        """Pass through to provider ProficiencyAdminSession.alias_proficiency"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('proficiency_admin_session').alias_proficiency(*args, **kwargs)


class ObjectiveBankList(abc_learning_objects.ObjectiveBankList, osid.OsidList):
    """ObjectiveBankList convenience adapter including related Session methods."""

    def get_next_objective_bank(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(ObjectiveBank)

    __next__ = next

    next_objective_bank = property(fget=get_next_objective_bank)

    def get_next_objective_banks(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(ObjectiveBankList, number=n)
