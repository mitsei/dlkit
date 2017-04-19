"""AuthZ Adapter implementations of grading managers."""
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
from dlkit.manager_impls.grading import managers as grading_managers


class GradingProfile(osid_managers.OsidProfile, grading_managers.GradingProfile):
    """Adapts underlying GradingProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_gradebook_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_gradebook_hierarchy_session()
        except Unimplemented:
            return None

    def supports_grade_system_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_system_lookup()

    def supports_grade_system_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_system_query()

    def supports_grade_system_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_system_admin()

    def supports_grade_entry_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_entry_lookup()

    def supports_grade_entry_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_entry_query()

    def supports_grade_entry_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_entry_admin()

    def supports_gradebook_column_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_column_lookup()

    def supports_gradebook_column_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_column_query()

    def supports_gradebook_column_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_column_admin()

    def supports_gradebook_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_lookup()

    def supports_gradebook_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_admin()

    def get_grade_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_record_types()

    grade_record_types = property(fget=get_grade_record_types)

    def get_grade_system_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_system_record_types()

    grade_system_record_types = property(fget=get_grade_system_record_types)

    def get_grade_system_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_system_search_record_types()

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    def get_grade_entry_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_entry_record_types()

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    def get_grade_entry_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_entry_search_record_types()

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    def get_gradebook_column_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_column_record_types()

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    def get_gradebook_column_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_column_search_record_types()

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    def get_gradebook_column_summary_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_column_summary_record_types()

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    def get_gradebook_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_record_types()

    gradebook_record_types = property(fget=get_gradebook_record_types)

    def get_gradebook_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_search_record_types()

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)


class GradingManager(osid_managers.OsidManager, GradingProfile, grading_managers.GradingManager):
    """Adapts underlying GradingManager methodswith authorization checks."""
    def __init__(self):
        GradingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:gradingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('GRADING', provider_impl)
        # need to add version argument

    def get_grade_system_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session()
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemLookupSession')(
                provider_session=self._provider_manager.get_grade_system_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    grade_system_lookup_session = property(fget=get_grade_system_lookup_session)

    @raise_null_argument
    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session_for_gradebook(gradebook_id)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemLookupSession')(
                provider_session=self._provider_manager.get_grade_system_lookup_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_grade_system_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session()
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemQuerySession')(
                provider_session=self._provider_manager.get_grade_system_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    grade_system_query_session = property(fget=get_grade_system_query_session)

    @raise_null_argument
    def get_grade_system_query_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session_for_gradebook(gradebook_id)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemQuerySession')(
                provider_session=self._provider_manager.get_grade_system_query_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_grade_system_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradeSystemAdminSession')(
                provider_session=self._provider_manager.get_grade_system_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    grade_system_admin_session = property(fget=get_grade_system_admin_session)

    @raise_null_argument
    def get_grade_system_admin_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradeSystemAdminSession')(
                provider_session=self._provider_manager.get_grade_system_admin_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_grade_entry_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session()
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryLookupSession')(
                provider_session=self._provider_manager.get_grade_entry_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    grade_entry_lookup_session = property(fget=get_grade_entry_lookup_session)

    @raise_null_argument
    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session_for_gradebook(gradebook_id)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryLookupSession')(
                provider_session=self._provider_manager.get_grade_entry_lookup_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_grade_entry_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session()
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryQuerySession')(
                provider_session=self._provider_manager.get_grade_entry_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    grade_entry_query_session = property(fget=get_grade_entry_query_session)

    @raise_null_argument
    def get_grade_entry_query_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session_for_gradebook(gradebook_id)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryQuerySession')(
                provider_session=self._provider_manager.get_grade_entry_query_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_grade_entry_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradeEntryAdminSession')(
                provider_session=self._provider_manager.get_grade_entry_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    grade_entry_admin_session = property(fget=get_grade_entry_admin_session)

    @raise_null_argument
    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradeEntryAdminSession')(
                provider_session=self._provider_manager.get_grade_entry_admin_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_gradebook_column_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookColumnLookupSession')(
                provider_session=self._provider_manager.get_gradebook_column_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    gradebook_column_lookup_session = property(fget=get_gradebook_column_lookup_session)

    @raise_null_argument
    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradebookColumnLookupSession')(
                provider_session=self._provider_manager.get_gradebook_column_lookup_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_gradebook_column_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookColumnQuerySession')(
                provider_session=self._provider_manager.get_gradebook_column_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    gradebook_column_query_session = property(fget=get_gradebook_column_query_session)

    @raise_null_argument
    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradebookColumnQuerySession')(
                provider_session=self._provider_manager.get_gradebook_column_query_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_gradebook_column_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookColumnAdminSession')(
                provider_session=self._provider_manager.get_gradebook_column_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    gradebook_column_admin_session = property(fget=get_gradebook_column_admin_session)

    @raise_null_argument
    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradebookColumnAdminSession')(
                provider_session=self._provider_manager.get_gradebook_column_admin_session_for_gradebook(gradebook_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_gradebook_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookLookupSession')(
                provider_session=self._provider_manager.get_gradebook_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)

    def get_gradebook_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookAdminSession')(
                provider_session=self._provider_manager.get_gradebook_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    gradebook_admin_session = property(fget=get_gradebook_admin_session)

    def get_grading_batch_manager(self):
        raise Unimplemented()

    grading_batch_manager = property(fget=get_grading_batch_manager)

    def get_grading_calculation_manager(self):
        raise Unimplemented()

    grading_calculation_manager = property(fget=get_grading_calculation_manager)

    def get_grading_transform_manager(self):
        raise Unimplemented()

    grading_transform_manager = property(fget=get_grading_transform_manager)


class GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile, grading_managers.GradingProxyManager):
    """Adapts underlying GradingProxyManager methodswith authorization checks."""
    def __init__(self):
        GradingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:gradingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('GRADING', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_grade_system_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session(proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemLookupSession')(
                provider_session=self._provider_manager.get_grade_system_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session_for_gradebook(gradebook_id, proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemLookupSession')(
                provider_session=self._provider_manager.get_grade_system_lookup_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_system_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session(proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemQuerySession')(
                provider_session=self._provider_manager.get_grade_system_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_system_query_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_system_query_session_for_gradebook(gradebook_id, proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeSystemQuerySession')(
                provider_session=self._provider_manager.get_grade_system_query_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_system_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradeSystemAdminSession')(
                provider_session=self._provider_manager.get_grade_system_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_system_admin_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradeSystemAdminSession')(
                provider_session=self._provider_manager.get_grade_system_admin_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_entry_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session(proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryLookupSession')(
                provider_session=self._provider_manager.get_grade_entry_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session_for_gradebook(gradebook_id, proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryLookupSession')(
                provider_session=self._provider_manager.get_grade_entry_lookup_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_entry_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session(proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryQuerySession')(
                provider_session=self._provider_manager.get_grade_entry_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_entry_query_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_grade_entry_query_session_for_gradebook(gradebook_id, proxy)
            query_session.use_federated_gradebook_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'GradeEntryQuerySession')(
                provider_session=self._provider_manager.get_grade_entry_query_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_entry_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradeEntryAdminSession')(
                provider_session=self._provider_manager.get_grade_entry_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradeEntryAdminSession')(
                provider_session=self._provider_manager.get_grade_entry_admin_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_column_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookColumnLookupSession')(
                provider_session=self._provider_manager.get_gradebook_column_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradebookColumnLookupSession')(
                provider_session=self._provider_manager.get_gradebook_column_lookup_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_column_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookColumnQuerySession')(
                provider_session=self._provider_manager.get_gradebook_column_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradebookColumnQuerySession')(
                provider_session=self._provider_manager.get_gradebook_column_query_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_column_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookColumnAdminSession')(
                provider_session=self._provider_manager.get_gradebook_column_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'GradebookColumnAdminSession')(
                provider_session=self._provider_manager.get_gradebook_column_admin_session_for_gradebook(gradebook_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookLookupSession')(
                provider_session=self._provider_manager.get_gradebook_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_gradebook_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'GradebookAdminSession')(
                provider_session=self._provider_manager.get_gradebook_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_grading_batch_proxy_manager(self):
        raise Unimplemented()

    grading_batch_proxy_manager = property(fget=get_grading_batch_proxy_manager)

    def get_grading_calculation_proxy_manager(self):
        raise Unimplemented()

    grading_calculation_proxy_manager = property(fget=get_grading_calculation_proxy_manager)

    def get_grading_transform_proxy_manager(self):
        raise Unimplemented()

    grading_transform_proxy_manager = property(fget=get_grading_transform_proxy_manager)
