"""AuthZ Adapter implementations of assessment sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import sessions as osid_sessions
from ..osid.osid_errors import NotFound
from ..osid.osid_errors import PermissionDenied
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from ..utilities import QueryWrapper
from ..utilities import raise_null_argument
from dlkit.abstract_osid.assessment import sessions as abc_assessment_sessions


class MyAssessmentTakenSession(abc_assessment_sessions.MyAssessmentTakenSession, osid_sessions.OsidSession):
    """Adapts underlying MyAssessmentTakenSession methodswith authorization checks."""
    def __init__(self, **kwargs):
        osid_sessions.OsidSession.__init__(self, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentTaken'

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

    def can_get_my_taken_assessments(self):
        return self._can('get_my')

    @raise_null_argument
    def get_assessments_started_during(self, start, end):
        if not self._can('get_my'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_started_during(start, end)

    def get_assessments_started(self):
        if not self._can('get_my'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_started_during()

    assessments_started = property(fget=get_assessments_started)

    @raise_null_argument
    def get_assessments_in_progress_during(self, start, end):
        if not self._can('get_my'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_in_progress_during(start, end)

    def get_assessments_in_progress(self):
        if not self._can('get_my'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_in_progress()

    assessments_in_progress = property(fget=get_assessments_in_progress)

    def get_assessments_completed(self):
        if not self._can('get_my'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_completed()

    assessments_completed = property(fget=get_assessments_completed)


class AssessmentSession(abc_assessment_sessions.AssessmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentSession methodswith authorization checks."""
    def __init__(self, **kwargs):
        osid_sessions.OsidSession.__init__(self, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Assessment'

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

    def can_take_assessments(self):
        return self._can('take')

    @raise_null_argument
    def has_assessment_begun(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_assessment_begun(assessment_taken_id)

    @raise_null_argument
    def is_assessment_over(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.is_assessment_over(assessment_taken_id)

    @raise_null_argument
    def requires_synchronous_sections(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.requires_synchronous_sections(assessment_taken_id)

    @raise_null_argument
    def get_first_assessment_section(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_first_assessment_section(assessment_taken_id)

    @raise_null_argument
    def has_next_assessment_section(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_next_assessment_section(assessment_section_id)

    @raise_null_argument
    def get_next_assessment_section(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_next_assessment_section(assessment_section_id)

    @raise_null_argument
    def has_previous_assessment_section(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_previous_assessment_section(assessment_section_id)

    @raise_null_argument
    def get_previous_assessment_section(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_previous_assessment_section(assessment_section_id)

    @raise_null_argument
    def get_assessment_section(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_section(assessment_section_id)

    @raise_null_argument
    def get_assessment_sections(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_sections(assessment_taken_id)

    @raise_null_argument
    def is_assessment_section_complete(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.is_assessment_section_complete(assessment_section_id)

    @raise_null_argument
    def get_incomplete_assessment_sections(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.is_assessment_section_complete(assessment_taken_id)

    @raise_null_argument
    def has_assessment_section_begun(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_assessment_section_begun(assessment_section_id)

    @raise_null_argument
    def is_assessment_section_over(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.is_assessment_section_over(assessment_section_id)

    @raise_null_argument
    def requires_synchronous_responses(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.requires_synchronous_responses(assessment_section_id)

    @raise_null_argument
    def get_first_question(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_first_question(assessment_section_id)

    @raise_null_argument
    def has_next_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_next_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_next_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_next_question(assessment_section_id, item_id)

    @raise_null_argument
    def has_previous_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_previous_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_previous_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_previous_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_questions(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_questions(assessment_section_id)

    @raise_null_argument
    def get_response_form(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_response_form(assessment_section_id, item_id)

    @raise_null_argument
    def submit_response(self, assessment_section_id, item_id, answer_form):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.submit_response(assessment_section_id, item_id, answer_form)

    @raise_null_argument
    def skip_item(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.skip_item(assessment_section_id, item_id)

    @raise_null_argument
    def is_question_answered(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.is_question_answered(assessment_section_id, item_id)

    @raise_null_argument
    def get_unanswered_questions(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_unanswered_questions(assessment_section_id)

    @raise_null_argument
    def has_unanswered_questions(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_unanswered_questions(assessment_section_id)

    @raise_null_argument
    def get_first_unanswered_question(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_first_unanswered_question(assessment_section_id)

    @raise_null_argument
    def has_next_unanswered_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_next_unanswered_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_next_unanswered_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_next_unanswered_question(assessment_section_id, item_id)

    @raise_null_argument
    def has_previous_unanswered_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.has_previous_unanswered_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_previous_unanswered_question(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_previous_unanswered_question(assessment_section_id, item_id)

    @raise_null_argument
    def get_response(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_response(assessment_section_id, item_id)

    @raise_null_argument
    def get_responses(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_responses(assessment_section_id)

    @raise_null_argument
    def clear_response(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.clear_response(assessment_section_id, item_id)

    @raise_null_argument
    def finish_assessment_section(self, assessment_section_id):
        if not self._can('take'):
            raise PermissionDenied()
        self._provider_session.finish_assessment_section(assessment_section_id)

    @raise_null_argument
    def is_answer_available(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.is_answer_available(assessment_section_id, item_id)

    @raise_null_argument
    def get_answers(self, assessment_section_id, item_id):
        if not self._can('take'):
            raise PermissionDenied()
        return self._provider_session.get_answers(assessment_section_id, item_id)

    @raise_null_argument
    def finish_assessment(self, assessment_taken_id):
        if not self._can('take'):
            raise PermissionDenied()
        self._provider_session.finish_assessment(assessment_taken_id)


class AssessmentResultsSession(abc_assessment_sessions.AssessmentResultsSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentResultsSession methodswith authorization checks."""
    def __init__(self, **kwargs):
        osid_sessions.OsidSession.__init__(self, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentResults'

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

    def can_access_assessment_results(self):
        return self._can('access')

    @raise_null_argument
    def get_items(self, assessment_taken_id):
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_items(assessment_taken_id)

    @raise_null_argument
    def get_responses(self, assessment_taken_id):
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_responses(assessment_taken_id)

    @raise_null_argument
    def are_results_available(self, assessment_taken_id):
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.are_results_available(assessment_taken_id)

    @raise_null_argument
    def get_grade_entries(self, assessment_taken_id):
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_grade_entries(assessment_taken_id)


class ItemLookupSession(abc_assessment_sessions.ItemLookupSession, osid_sessions.OsidSession):
    """Adapts underlying ItemLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Item'
        self.use_federated_bank_view()
        self.use_comparative_item_view()
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
        return self._query_session.get_items_by_query(query), query

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
        return self._query_session.get_items_by_query(query)

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

    def can_lookup_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_item_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_item_view()

    def use_plenary_item_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_item_view()

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
    def get_item(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_item(item_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_item_query()
        query.match_id(item_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_items_by_ids(self, item_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_items_by_ids(item_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_item_query()
        for item_id in (item_ids):
            query.match_id(item_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_items_by_genus_type(self, item_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_items_by_genus_type(item_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_item_query()
        query.match_genus_type(item_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_items_by_parent_genus_type(self, item_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_items_by_parent_genus_type(item_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_item_query()
        query.match_parent_genus_type(item_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_items_by_record_type(self, item_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_items_by_record_type(item_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_item_query()
        query.match_record_type(item_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_items_by_question(self, question_id):
        raise Unimplemented()

    @raise_null_argument
    def get_items_by_answer(self, answer_id):
        raise Unimplemented()

    @raise_null_argument
    def get_items_by_learning_objective(self, objective_id):
        raise Unimplemented()

    @raise_null_argument
    def get_items_by_learning_objectives(self, objective_ids):
        raise Unimplemented()

    def get_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_items()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_item_query()
        query.match_any(match=True)
        return self._try_harder(query)

    items = property(fget=get_items)


class ItemQuerySession(abc_assessment_sessions.ItemQuerySession, osid_sessions.OsidSession):
    """Adapts underlying ItemQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Item'
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
        return self._query_session.get_items_by_query(query), query

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
        return self._query_session.get_items_by_query(query)

    class ItemQueryWrapper(QueryWrapper):
        """Wrapper for ItemQueries to override match_bank_id method"""

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

    def can_search_items(self):
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

    def get_item_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.ItemQueryWrapper(self._provider_session.get_item_query())

    item_query = property(fget=get_item_query)

    @raise_null_argument
    def get_items_by_query(self, item_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(item_query, '_cat_id_args_list'):
            raise Unsupported('item_query not from this session')
        for kwargs in item_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                item_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_items_by_query(item_query)
        self._check_search_conditions()
        result = self._try_harder(item_query)
        item_query._provider_query.clear_bank_terms()
        return result


class ItemSearchSession(abc_assessment_sessions.ItemSearchSession, ItemQuerySession):
    """Adapts underlying ItemSearchSession methodswith authorization checks."""

    def get_item_search(self):
        """Pass through to provider ItemSearchSession.get_item_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_item_search()

    item_search = property(fget=get_item_search)

    def get_item_search_order(self):
        raise Unimplemented()

    item_search_order = property(fget=get_item_search_order)

    @raise_null_argument
    def get_items_by_search(self, item_query, item_search):
        """Pass through to provider ItemSearchSession.get_items_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_items_by_search(item_query, item_search)

    @raise_null_argument
    def get_item_query_from_inspector(self, item_query_inspector):
        raise Unimplemented()


class ItemAdminSession(abc_assessment_sessions.ItemAdminSession, osid_sessions.OsidSession):
    """Adapts underlying ItemAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Item'
        self._overriding_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_item_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_item_bank_session()
                self.get_bank_ids_by_item = self._object_catalog_session.get_bank_ids_by_item
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bank_ids(self):
        if self._overriding_bank_ids is None:
            self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bank_ids

    def _can_for_item(self, func_name, item_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, item_id, 'get_bank_ids_for_item')

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

    def can_create_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_item_with_record_types(self, item_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if item_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_item_form_for_create(self, item_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_item_form_for_create(item_record_types)

    @raise_null_argument
    def create_item(self, item_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_item(item_form)

    def can_update_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_item_form_for_update(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_item('update', item_id):
            raise PermissionDenied()
        return self._provider_session.get_item_form_for_update(item_id)

    def duplicate_item(self, item_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_item(item_id)

    @raise_null_argument
    def update_item(self, item_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_item(item_form)

    def can_delete_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_item(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_item('delete', item_id):
            raise PermissionDenied()
        return self._provider_session.delete_item(item_id)

    def can_manage_item_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_item(self, item_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_item('alias', item_id):
            raise PermissionDenied()
        return self._provider_session.alias_item(item_id, alias_id)

    def can_create_questions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_question_with_record_types(self, question_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if question_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_question_form_for_create(self, item_id, question_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_question_form_for_create(item_id, question_record_types)

    @raise_null_argument
    def create_question(self, question_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.create_asset_content_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_question(question_form)

    def can_update_questions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_question_form_for_update(self, question_id):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_question_form_for_update(question_id)

    @raise_null_argument
    def update_question(self, question_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.update_asset_content_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_question(question_form)

    def can_delete_questions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_question(self, question_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_asset_content_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_question(question_id)

    def can_create_answers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_answers_with_record_types(self, answer_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if answer_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_answer_form_for_create(self, item_id, answer_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_answer_form_for_create(item_id, answer_record_types)

    @raise_null_argument
    def create_answer(self, answer_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.create_asset_content_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_answer(answer_form)

    def can_update_answers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_answer_form_for_update(self, answer_id):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_answer_form_for_update(answer_id)

    @raise_null_argument
    def update_answer(self, answer_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.update_asset_content_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_answer(answer_form)

    def can_delete_answers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_answer(self, answer_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_asset_content_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_answer(answer_id)


class ItemNotificationSession(abc_assessment_sessions.ItemNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying ItemNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Item'

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

    def can_register_for_item_notifications(self):
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

    def reliable_item_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_item_notifications()

    def unreliable_item_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_item_notifications()

    @raise_null_argument
    def acknowledge_item_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_items()

    def register_for_changed_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_items()

    @raise_null_argument
    def register_for_changed_item(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_item(item_id)

    def register_for_deleted_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_items()

    @raise_null_argument
    def register_for_deleted_item(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_item(item_id)

    def reliable_item_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_item_notifications()

    def unreliable_item_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_item_notifications()

    @raise_null_argument
    def acknowledge_item_notification(self, notification_id):
        raise Unimplemented()


class ItemBankSession(abc_assessment_sessions.ItemBankSession, osid_sessions.OsidSession):
    """Adapts underlying ItemBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.ItemBank'

    def can_lookup_item_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bank_view()

    def use_plenary_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bank_view()

    @raise_null_argument
    def get_item_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_item_ids_by_bank(bank_id)

    @raise_null_argument
    def get_items_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_item_ids_by_bank(bank_id)

    @raise_null_argument
    def get_item_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_item_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_items_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_items_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_item(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_item(item_id)

    @raise_null_argument
    def get_banks_by_item(self, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_item(item_id)


class ItemBankAssignmentSession(abc_assessment_sessions.ItemBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying ItemBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.ItemBank'

    def can_assign_items(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_items_to_bank(self, bank_id):
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
    def get_assignable_bank_ids_for_item(self, bank_id, item_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_item(item_id)

    @raise_null_argument
    def assign_item_to_bank(self, item_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_item_to_bank(item_id, bank_id)

    @raise_null_argument
    def unassign_item_from_bank(self, item_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_item_from_bank(item_id, bank_id)

    @raise_null_argument
    def reassign_item_to_billing(self, item_id, from_bank_id, to_bank_id):
        raise Unimplemented()


class ItemSmartBankSession(abc_assessment_sessions.ItemSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying ItemSmartBankSession methodswith authorization checks."""

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

    def get_item_query(self):
        raise Unimplemented()

    item_query = property(fget=get_item_query)

    def get_item_search_order(self):
        raise Unimplemented()

    item_search_order = property(fget=get_item_search_order)

    @raise_null_argument
    def apply_item_query(self, item_query):
        raise Unimplemented()

    def inspect_item_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_item_sequencing(self, item_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_item_query_from_inspector(self, item_query_inspector):
        raise Unimplemented()


class AssessmentLookupSession(abc_assessment_sessions.AssessmentLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Assessment'
        self.use_federated_bank_view()
        self.use_comparative_assessment_view()
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
        return self._query_session.get_assessments_by_query(query), query

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
        return self._query_session.get_assessments_by_query(query)

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

    def can_lookup_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_assessment_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_assessment_view()

    def use_plenary_assessment_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_assessment_view()

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
    def get_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_assessment(assessment_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_query()
        query.match_id(assessment_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_assessments_by_ids(self, assessment_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_by_ids(assessment_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_query()
        for assessment_id in (assessment_ids):
            query.match_id(assessment_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_by_genus_type(self, assessment_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_by_genus_type(assessment_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_query()
        query.match_genus_type(assessment_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_by_parent_genus_type(self, assessment_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_by_parent_genus_type(assessment_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_query()
        query.match_parent_genus_type(assessment_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_by_record_type(self, assessment_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_by_record_type(assessment_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_query()
        query.match_record_type(assessment_record_type, match=True)
        return self._try_harder(query)

    def get_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_assessments()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_query()
        query.match_any(match=True)
        return self._try_harder(query)

    assessments = property(fget=get_assessments)


class AssessmentQuerySession(abc_assessment_sessions.AssessmentQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Assessment'
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
        return self._query_session.get_assessments_by_query(query), query

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
        return self._query_session.get_assessments_by_query(query)

    class AssessmentQueryWrapper(QueryWrapper):
        """Wrapper for AssessmentQueries to override match_bank_id method"""

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

    def can_search_assessments(self):
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

    def get_assessment_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AssessmentQueryWrapper(self._provider_session.get_assessment_query())

    assessment_query = property(fget=get_assessment_query)

    @raise_null_argument
    def get_assessments_by_query(self, assessment_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(assessment_query, '_cat_id_args_list'):
            raise Unsupported('assessment_query not from this session')
        for kwargs in assessment_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                assessment_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_assessments_by_query(assessment_query)
        self._check_search_conditions()
        result = self._try_harder(assessment_query)
        assessment_query._provider_query.clear_bank_terms()
        return result


class AssessmentSearchSession(abc_assessment_sessions.AssessmentSearchSession, AssessmentQuerySession):
    """Adapts underlying AssessmentSearchSession methodswith authorization checks."""

    def get_assessment_search(self):
        """Pass through to provider AssessmentSearchSession.get_assessment_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_search()

    assessment_search = property(fget=get_assessment_search)

    def get_assessment_search_order(self):
        raise Unimplemented()

    assessment_search_order = property(fget=get_assessment_search_order)

    @raise_null_argument
    def get_assessments_by_search(self, assessment_query, assessment_search):
        """Pass through to provider AssessmentSearchSession.get_assessments_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_by_search(assessment_query, assessment_search)

    @raise_null_argument
    def get_assessment_query_from_inspector(self, assessment_query_inspector):
        raise Unimplemented()


class AssessmentAdminSession(abc_assessment_sessions.AssessmentAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Assessment'
        self._overriding_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_assessment_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_assessment_bank_session()
                self.get_bank_ids_by_assessment = self._object_catalog_session.get_bank_ids_by_assessment
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bank_ids(self):
        if self._overriding_bank_ids is None:
            self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bank_ids

    def _can_for_assessment(self, func_name, assessment_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, assessment_id, 'get_bank_ids_for_assessment')

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

    def can_create_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_assessment_with_record_types(self, assessment_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if assessment_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_assessment_form_for_create(self, assessment_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_form_for_create(assessment_record_types)

    @raise_null_argument
    def create_assessment(self, assessment_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_assessment(assessment_form)

    def can_update_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_assessment_form_for_update(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_assessment('update', assessment_id):
            raise PermissionDenied()
        return self._provider_session.get_assessment_form_for_update(assessment_id)

    def duplicate_assessment(self, assessment_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_assessment(assessment_id)

    @raise_null_argument
    def update_assessment(self, assessment_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_assessment(assessment_form)

    def can_delete_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective_template
        if not self._can_for_assessment('delete', assessment_id):
            raise PermissionDenied()
        return self._provider_session.delete_assessment(assessment_id)

    def can_manage_assessment_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_assessment(self, assessment_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_assessment('alias', assessment_id):
            raise PermissionDenied()
        return self._provider_session.alias_assessment(assessment_id, alias_id)


class AssessmentNotificationSession(abc_assessment_sessions.AssessmentNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Assessment'

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

    def can_register_for_assessment_notifications(self):
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

    def reliable_assessment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_notifications()

    def unreliable_assessment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_notifications()

    @raise_null_argument
    def acknowledge_assessment_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments()

    def register_for_changed_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments()

    @raise_null_argument
    def register_for_changed_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessment(assessment_id)

    def register_for_deleted_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments()

    @raise_null_argument
    def register_for_deleted_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessment(assessment_id)

    def reliable_assessment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_notifications()

    def unreliable_assessment_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_notifications()

    @raise_null_argument
    def acknowledge_assessment_notification(self, notification_id):
        raise Unimplemented()


class AssessmentBankSession(abc_assessment_sessions.AssessmentBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.AssessmentBank'

    def can_lookup_assessment_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bank_view()

    def use_plenary_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bank_view()

    @raise_null_argument
    def get_assessment_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessments_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessment_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_assessments_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_assessment(assessment_id)

    @raise_null_argument
    def get_banks_by_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_assessment(assessment_id)


class AssessmentBankAssignmentSession(abc_assessment_sessions.AssessmentBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.AssessmentBank'

    def can_assign_assessments(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_assessments_to_bank(self, bank_id):
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
    def get_assignable_bank_ids_for_assessment(self, bank_id, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_assessment(assessment_id)

    @raise_null_argument
    def assign_assessment_to_bank(self, assessment_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_assessment_to_bank(assessment_id, bank_id)

    @raise_null_argument
    def unassign_assessment_from_bank(self, assessment_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_assessment_from_bank(assessment_id, bank_id)

    @raise_null_argument
    def reassign_assessment_to_billing(self, assessment_id, from_bank_id, to_bank_id):
        raise Unimplemented()


class AssessmentSmartBankSession(abc_assessment_sessions.AssessmentSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentSmartBankSession methodswith authorization checks."""

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

    def get_assessment_query(self):
        raise Unimplemented()

    assessment_query = property(fget=get_assessment_query)

    def get_assessment_search_order(self):
        raise Unimplemented()

    assessment_search_order = property(fget=get_assessment_search_order)

    @raise_null_argument
    def apply_assessment_query(self, assessment_query):
        raise Unimplemented()

    def inspect_assessment_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_assessment_sequencing(self, assessment_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_assessment_query_from_inspector(self, assessment_query_inspector):
        raise Unimplemented()


class AssessmentBasicAuthoringSession(abc_assessment_sessions.AssessmentBasicAuthoringSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentBasicAuthoringSession methodswith authorization checks."""
    def __init__(self, **kwargs):
        osid_sessions.OsidSession.__init__(self, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.Assessment'

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

    def can_author_assessments(self):
        return self._can('author')

    @raise_null_argument
    def get_items(self, assessment_id):
        # Implemented from azosid template for -
        # osid.assessment.AssessmentBasicAuthoringSession.get_items
        if not self._can('author'):
            raise PermissionDenied()
        return self._provider_session.get_items(assessment_id)

    @raise_null_argument
    def add_item(self, assessment_id, item_id):
        # Implemented from azosid template for -
        # osid.assessment.AssessmentBasicAuthoringSession.add_item
        if not self._can('author'):
            raise PermissionDenied()
        self._provider_session.add_item(assessment_id, item_id)

    @raise_null_argument
    def remove_item(self, assessment_id, item_id):
        # Implemented from azosid template for -
        # osid.assessment.AssessmentBasicAuthoringSession.remove_item
        if not self._can('author'):
            raise PermissionDenied()
        self._provider_session.remove_item(assessment_id, item_id)

    @raise_null_argument
    def move_item(self, assessment_id, item_id, preceeding_item_id):
        # Implemented from azosid template for -
        # osid.assessment.AssessmentBasicAuthoringSession.move_item
        if not self._can('author'):
            raise PermissionDenied()
        self._provider_session.move_item(assessment_id, item_id, preceeding_item_id)

    @raise_null_argument
    def order_items(self, item_ids, assessment_id):
        # Implemented from azosid template for -
        # osid.assessment.AssessmentBasicAuthoringSession.order_items
        if not self._can('author'):
            raise PermissionDenied()
        self._provider_session.order_items(item_ids, assessment_id)


class AssessmentOfferedLookupSession(abc_assessment_sessions.AssessmentOfferedLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentOffered'
        self.use_federated_bank_view()
        self.use_comparative_assessment_offered_view()
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
        return self._query_session.get_assessments_offered_by_query(query), query

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
        return self._query_session.get_assessments_offered_by_query(query)

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

    def can_lookup_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_assessment_offered_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_assessment_offered_view()

    def use_plenary_assessment_offered_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_assessment_offered_view()

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
    def get_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_offered(assessment_offered_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        query.match_id(assessment_offered_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_assessments_offered_by_ids(self, assessment_offered_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_offered_by_ids(assessment_offered_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        for assessment_offered_id in (assessment_offered_ids):
            query.match_id(assessment_offered_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_offered_by_genus_type(self, assessment_offered_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_offered_by_genus_type(assessment_offered_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        query.match_genus_type(assessment_offered_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_offered_by_parent_genus_type(self, assessment_offered_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_offered_by_parent_genus_type(assessment_offered_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        query.match_parent_genus_type(assessment_offered_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_offered_by_record_type(self, assessment_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_offered_by_record_type(assessment_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        query.match_record_type(assessment_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_offered_by_date(self, start, end):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_offered_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_offered_for_assessment(assessment_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        query.match_assessment_id(assessment_id, match=True)
        return self._try_harder(query)

    def get_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_offered()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_offered_query()
        query.match_any(match=True)
        return self._try_harder(query)

    assessments_offered = property(fget=get_assessments_offered)


class AssessmentOfferedQuerySession(abc_assessment_sessions.AssessmentOfferedQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentOffered'
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
        return self._query_session.get_assessments_offered_by_query(query), query

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
        return self._query_session.get_assessments_offered_by_query(query)

    class AssessmentOfferedQueryWrapper(QueryWrapper):
        """Wrapper for AssessmentOfferedQueries to override match_bank_id method"""

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

    def can_search_assessments_offered(self):
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

    def get_assessment_offered_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AssessmentOfferedQueryWrapper(self._provider_session.get_assessment_offered_query())

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @raise_null_argument
    def get_assessments_offered_by_query(self, assessment_offered_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(assessment_offered_query, '_cat_id_args_list'):
            raise Unsupported('assessment_offered_query not from this session')
        for kwargs in assessment_offered_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                assessment_offered_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_assessments_offered_by_query(assessment_offered_query)
        self._check_search_conditions()
        result = self._try_harder(assessment_offered_query)
        assessment_offered_query._provider_query.clear_bank_terms()
        return result


class AssessmentOfferedSearchSession(abc_assessment_sessions.AssessmentOfferedSearchSession, AssessmentOfferedQuerySession):
    """Adapts underlying AssessmentOfferedSearchSession methodswith authorization checks."""

    def get_assessment_offered_search(self):
        """Pass through to provider AssessmentOfferedSearchSession.get_assessment_offered_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_offered_search()

    assessment_offered_search = property(fget=get_assessment_offered_search)

    def get_assessment_offered_search_order(self):
        raise Unimplemented()

    assessment_offered_search_order = property(fget=get_assessment_offered_search_order)

    @raise_null_argument
    def get_assessments_offered_by_search(self, assessment_offered_query, assessment_offered_search):
        """Pass through to provider AssessmentOfferedSearchSession.get_assessments_offered_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_offered_by_search(assessment_offered_query, assessment_offered_search)

    @raise_null_argument
    def get_assessment_offered_query_from_inspector(self, assessment_offered_query_inspector):
        raise Unimplemented()


class AssessmentOfferedAdminSession(abc_assessment_sessions.AssessmentOfferedAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentOffered'
        self._overriding_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_assessment_offered_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_assessment_offered_bank_session()
                self.get_bank_ids_by_assessment_offered = self._object_catalog_session.get_bank_ids_by_assessment_offered
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bank_ids(self):
        if self._overriding_bank_ids is None:
            self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bank_ids

    def _can_for_assessment_offered(self, func_name, assessment_offered_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, assessment_offered_id, 'get_bank_ids_for_assessment_offered')

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

    def can_create_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_assessment_offered_with_record_types(self, assessment_offered_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if assessment_offered_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_assessment_offered_form_for_create(self, assessment_id, assessment_offered_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_offered_form_for_create(assessment_id, assessment_offered_record_types)

    @raise_null_argument
    def create_assessment_offered(self, assessment_offered_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_assessment_offered(assessment_offered_form)

    def can_update_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_assessment_offered_form_for_update(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_assessment_offered('update', assessment_offered_id):
            raise PermissionDenied()
        return self._provider_session.get_assessment_offered_form_for_update(assessment_offered_id)

    def duplicate_assessment_offered(self, assessment_offered_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_assessment_offered(assessment_offered_id)

    @raise_null_argument
    def update_assessment_offered(self, assessment_offered_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_assessment_offered(assessment_offered_form)

    def can_delete_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective_template
        if not self._can_for_assessment_offered('delete', assessment_offered_id):
            raise PermissionDenied()
        return self._provider_session.delete_assessment_offered(assessment_offered_id)

    def can_manage_assessment_offered_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_assessment_offered(self, assessment_offered_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_assessment_offered('alias', assessment_offered_id):
            raise PermissionDenied()
        return self._provider_session.alias_assessment_offered(assessment_offered_id, alias_id)


class AssessmentOfferedNotificationSession(abc_assessment_sessions.AssessmentOfferedNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentOffered'

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

    def can_register_for_assessment_offered_notifications(self):
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

    def reliable_assessment_offered_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_offered_notifications()

    def unreliable_assessment_offered_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_offered_notifications()

    @raise_null_argument
    def acknowledge_assessment_offered_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments_offered()

    @raise_null_argument
    def register_for_new_assessments_offered_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments_offered_for_assessment()

    def register_for_changed_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments_offered()

    @raise_null_argument
    def register_for_changed_assessments_offered_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments_offered_for_assessment(assessment_id)

    @raise_null_argument
    def register_for_changed_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessment_offered(assessment_offered_id)

    def register_for_deleted_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments_offered()

    @raise_null_argument
    def register_for_deleted_assessments_offered_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments_offered_for_assessment(assessment_id)

    @raise_null_argument
    def register_for_deleted_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessment_offered(assessment_offered_id)

    def reliable_assessment_offered_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_offered_notifications()

    def unreliable_assessment_offered_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_offered_notifications()

    @raise_null_argument
    def acknowledge_assessment_offered_notification(self, notification_id):
        raise Unimplemented()


class AssessmentOfferedBankSession(abc_assessment_sessions.AssessmentOfferedBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.AssessmentOfferedBank'

    def can_lookup_assessment_offered_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bank_view()

    def use_plenary_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bank_view()

    @raise_null_argument
    def get_assessment_offered_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_offered_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessments_offered_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_offered_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessment_offered_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_offered_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_assessments_offered_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_offered_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_assessment_offered(assessment_offered_id)

    @raise_null_argument
    def get_banks_by_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_assessment_offered(assessment_offered_id)


class AssessmentOfferedBankAssignmentSession(abc_assessment_sessions.AssessmentOfferedBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.AssessmentOfferedBank'

    def can_assign_assessments_offered(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_assessments_offered_to_bank(self, bank_id):
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
    def get_assignable_bank_ids_for_assessment_offered(self, bank_id, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_assessment_offered(assessment_offered_id)

    @raise_null_argument
    def assign_assessment_offered_to_bank(self, assessment_offered_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_assessment_offered_to_bank(assessment_offered_id, bank_id)

    @raise_null_argument
    def unassign_assessment_offered_from_bank(self, assessment_offered_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_assessment_offered_from_bank(assessment_offered_id, bank_id)

    @raise_null_argument
    def reassign_assessment_offered_to_billing(self, assessment_offered_id, from_bank_id, to_bank_id):
        raise Unimplemented()


class AssessmentOfferedSmartBankSession(abc_assessment_sessions.AssessmentOfferedSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentOfferedSmartBankSession methodswith authorization checks."""

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

    def get_assessment_offered_query(self):
        raise Unimplemented()

    assessment_offered_query = property(fget=get_assessment_offered_query)

    def get_assessment_offered_search_order(self):
        raise Unimplemented()

    assessment_offered_search_order = property(fget=get_assessment_offered_search_order)

    @raise_null_argument
    def apply_assessment_offered_query(self, assessment_offered_query):
        raise Unimplemented()

    def inspect_assessment_offered_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_assessment_offered_sequencing(self, assessment_offered_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_assessment_offered_query_from_inspector(self, assessment_offered_query_inspector):
        raise Unimplemented()


class AssessmentTakenLookupSession(abc_assessment_sessions.AssessmentTakenLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentTaken'
        self.use_federated_bank_view()
        self.use_comparative_assessment_taken_view()
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
        return self._query_session.get_assessments_taken_by_query(query), query

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
        return self._query_session.get_assessments_taken_by_query(query)

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

    def can_lookup_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return (self._can('lookup') or
                bool(self._get_overriding_catalog_ids('lookup')))

    def use_comparative_assessment_taken_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_assessment_taken_view()

    def use_plenary_assessment_taken_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_assessment_taken_view()

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
    def get_assessment_taken(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_assessment_taken(assessment_taken_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_id(assessment_taken_id, match=True)
        results = self._try_harder(query)
        if results.available():
            return results.next()
        raise NotFound()

    @raise_null_argument
    def get_assessments_taken_by_ids(self, assessment_taken_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_by_ids(assessment_taken_ids)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        for assessment_taken_id in (assessment_taken_ids):
            query.match_id(assessment_taken_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_genus_type(self, assessment_taken_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_by_genus_type(assessment_taken_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_genus_type(assessment_taken_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_parent_genus_type(self, assessment_taken_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_by_parent_genus_type(assessment_taken_genus_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_parent_genus_type(assessment_taken_genus_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_record_type(self, assessment_taken_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_by_record_type(assessment_taken_record_type)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_record_type(assessment_taken_record_type, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_date(self, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_for_taker(self, resource_id):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_by_date_for_taker(self, resource_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_for_assessment(assessment_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_assessment_id(assessment_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_date_for_assessment(self, assessment_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_for_taker_and_assessment(self, resource_id, assessment_id):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_by_date_for_taker_and_assessment(self, resource_id, assessment_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_for_assessment_offered(assessment_offered_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_assessment_offered_id(assessment_offered_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_date_for_assessment_offered(self, assessment_offered_id, from_, to):
        raise Unimplemented()

    @raise_null_argument
    def get_assessments_taken_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id):
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken_for_taker_and_assessment_offered(resource_id, assessment_offered_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_taking_agent_id(resource_id, match=True)
        query.match_assessment_offered_id(assessment_offered_id, match=True)
        return self._try_harder(query)

    @raise_null_argument
    def get_assessments_taken_by_date_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id, from_, to):
        raise Unimplemented()

    def get_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_assessments_taken()
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_taken_query()
        query.match_any(match=True)
        return self._try_harder(query)

    assessments_taken = property(fget=get_assessments_taken)


class AssessmentTakenQuerySession(abc_assessment_sessions.AssessmentTakenQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentTaken'
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
        return self._query_session.get_assessments_taken_by_query(query), query

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
        return self._query_session.get_assessments_taken_by_query(query)

    class AssessmentTakenQueryWrapper(QueryWrapper):
        """Wrapper for AssessmentTakenQueries to override match_bank_id method"""

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

    def can_search_assessments_taken(self):
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

    def get_assessment_taken_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AssessmentTakenQueryWrapper(self._provider_session.get_assessment_taken_query())

    assessment_taken_query = property(fget=get_assessment_taken_query)

    @raise_null_argument
    def get_assessments_taken_by_query(self, assessment_taken_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(assessment_taken_query, '_cat_id_args_list'):
            raise Unsupported('assessment_taken_query not from this session')
        for kwargs in assessment_taken_query._cat_id_args_list:
            if self._can('search', kwargs['bank_id']):
                assessment_taken_query._provider_query.match_bank_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_assessments_taken_by_query(assessment_taken_query)
        self._check_search_conditions()
        result = self._try_harder(assessment_taken_query)
        assessment_taken_query._provider_query.clear_bank_terms()
        return result


class AssessmentTakenSearchSession(abc_assessment_sessions.AssessmentTakenSearchSession, AssessmentTakenQuerySession):
    """Adapts underlying AssessmentTakenSearchSession methodswith authorization checks."""

    def get_assessment_taken_search(self):
        """Pass through to provider AssessmentTakenSearchSession.get_assessment_taken_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_taken_search()

    assessment_taken_search = property(fget=get_assessment_taken_search)

    def get_assessment_taken_search_order(self):
        raise Unimplemented()

    assessment_taken_search_order = property(fget=get_assessment_taken_search_order)

    @raise_null_argument
    def get_assessments_taken_by_search(self, assessment_taken_query, assessment_taken_search):
        """Pass through to provider AssessmentTakenSearchSession.get_assessments_taken_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_taken_by_search(assessment_taken_query, assessment_taken_search)

    @raise_null_argument
    def get_assessment_taken_query_from_inspector(self, assessment_taken_query_inspector):
        raise Unimplemented()


class AssessmentTakenAdminSession(abc_assessment_sessions.AssessmentTakenAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenAdminSession methodswith authorization checks."""
    def __init__(self, provider_manager, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentTaken'
        self._overriding_bank_ids = None
        if self._proxy is not None:
            try:
                self._object_catalog_session = provider_manager.get_assessment_taken_bank_session(self._proxy)
            except (Unimplemented, AttributeError):
                pass
        else:
            try:
                self._object_catalog_session = provider_manager.get_assessment_taken_bank_session()
                self.get_bank_ids_by_assessment_taken = self._object_catalog_session.get_bank_ids_by_assessment_taken
            except (Unimplemented, AttributeError):
                pass

    def _get_overriding_bank_ids(self):
        if self._overriding_bank_ids is None:
            self._overriding_bank_ids = self._get_overriding_catalog_ids('lookup')
        return self._overriding_bank_ids

    def _can_for_assessment_taken(self, func_name, assessment_taken_id):
        """Checks if agent can perform function for object"""
        return self._can_for_object(func_name, assessment_taken_id, 'get_bank_ids_for_assessment_taken')

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

    def can_create_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    @raise_null_argument
    def can_create_assessment_taken_with_record_types(self, assessment_taken_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if assessment_taken_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_assessment_taken_form_for_create(self, assessment_offered_id, assessment_taken_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_taken_form_for_create(assessment_offered_id, assessment_taken_record_types)

    @raise_null_argument
    def create_assessment_taken(self, assessment_taken_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_assessment_taken(assessment_taken_form)

    def can_update_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return (self._can('update') or
                bool(self._get_overriding_catalog_ids('update')))

    @raise_null_argument
    def get_assessment_taken_form_for_update(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can_for_assessment_taken('update', assessment_taken_id):
            raise PermissionDenied()
        return self._provider_session.get_assessment_taken_form_for_update(assessment_taken_id)

    def duplicate_assessment_taken(self, assessment_taken_id):
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.duplicate_assessment_taken(assessment_taken_id)

    @raise_null_argument
    def update_assessment_taken(self, assessment_taken_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_assessment_taken(assessment_taken_form)

    def can_delete_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return (self._can('delete') or
                bool(self._get_overriding_catalog_ids('delete')))

    @raise_null_argument
    def delete_assessment_taken(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can_for_assessment_taken('delete', assessment_taken_id):
            raise PermissionDenied()
        return self._provider_session.delete_assessment_taken(assessment_taken_id)

    def can_manage_assessment_taken_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_assessment_taken(self, assessment_taken_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can_for_assessment_taken('alias', assessment_taken_id):
            raise PermissionDenied()
        return self._provider_session.alias_assessment_taken(assessment_taken_id, alias_id)


class AssessmentTakenNotificationSession(abc_assessment_sessions.AssessmentTakenNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenNotificationSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = self._provider_session.get_bank_id()
        self._id_namespace = 'assessment.AssessmentTaken'

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

    def can_register_for_assessment_taken_notifications(self):
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

    def reliable_assessment_taken_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_taken_notifications()

    def unreliable_assessment_taken_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_taken_notifications()

    @raise_null_argument
    def acknowledge_assessment_taken_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments_taken()

    @raise_null_argument
    def register_for_new_assessments_taken_for_taker(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments_taken_for_taker()

    @raise_null_argument
    def register_for_new_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments_taken_for_assessment_offered()

    @raise_null_argument
    def register_for_new_assessments_taken_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_new_assessments_taken_for_assessment()

    def register_for_changed_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments_taken()

    @raise_null_argument
    def register_for_changed_assessments_taken_for_taker(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments_taken_for_taker(resource_id)

    @raise_null_argument
    def register_for_changed_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments_taken_for_assessment_offered(assessment_offered_id)

    @raise_null_argument
    def register_for_changed_assessments_taken_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessments_taken_for_assessment(assessment_id)

    @raise_null_argument
    def register_for_changed_assessment_taken(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_assessment_taken(assessment_taken_id)

    def register_for_deleted_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments_taken()

    @raise_null_argument
    def register_for_deleted_assessments_taken_for_taker(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments_taken_for_taker(resource_id)

    @raise_null_argument
    def register_for_deleted_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments_taken_for_assessment_offered(assessment_offered_id)

    @raise_null_argument
    def register_for_deleted_assessments_taken_for_assessment(self, assessment_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessments_taken_for_assessment(assessment_id)

    @raise_null_argument
    def register_for_deleted_assessment_taken(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_deleted_assessment_taken(assessment_taken_id)

    def reliable_assessment_taken_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_assessment_taken_notifications()

    def unreliable_assessment_taken_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_assessment_taken_notifications()

    @raise_null_argument
    def acknowledge_assessment_taken_notification(self, notification_id):
        raise Unimplemented()


class AssessmentTakenBankSession(abc_assessment_sessions.AssessmentTakenBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenBankSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.AssessmentTakenBank'

    def can_lookup_assessment_taken_bank_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bank_view()

    def use_plenary_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bank_view()

    @raise_null_argument
    def get_assessment_taken_ids_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_taken_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessments_taken_by_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_taken_ids_by_bank(bank_id)

    @raise_null_argument
    def get_assessment_taken_ids_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessment_taken_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_assessments_taken_by_banks(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_assessments_taken_ids_by_banks(bank_ids)

    @raise_null_argument
    def get_bank_ids_by_assessment_taken(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank_ids_by_assessment_taken(assessment_taken_id)

    @raise_null_argument
    def get_banks_by_assessment_taken(self, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_assessment_taken(assessment_taken_id)


class AssessmentTakenBankAssignmentSession(abc_assessment_sessions.AssessmentTakenBankAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenBankAssignmentSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')  # This could be better
        self._id_namespace = 'assessment.AssessmentTakenBank'

    def can_assign_assessments_taken(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    @raise_null_argument
    def can_assign_assessments_taken_to_bank(self, bank_id):
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
    def get_assignable_bank_ids_for_assessment_taken(self, bank_id, assessment_taken_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.get_assignable_bank_ids_for_assessment_taken(assessment_taken_id)

    @raise_null_argument
    def assign_assessment_taken_to_bank(self, assessment_taken_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.assign_assessment_taken_to_bank(assessment_taken_id, bank_id)

    @raise_null_argument
    def unassign_assessment_taken_from_bank(self, assessment_taken_id, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        return self._provider_session.unassign_assessment_taken_from_bank(assessment_taken_id, bank_id)

    @raise_null_argument
    def reassign_assessment_taken_to_billing(self, assessment_taken_id, from_bank_id, to_bank_id):
        raise Unimplemented()


class AssessmentTakenSmartBankSession(abc_assessment_sessions.AssessmentTakenSmartBankSession, osid_sessions.OsidSession):
    """Adapts underlying AssessmentTakenSmartBankSession methodswith authorization checks."""

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

    def get_assessment_taken_query(self):
        raise Unimplemented()

    assessment_taken_query = property(fget=get_assessment_taken_query)

    def get_assessment_taken_search_order(self):
        raise Unimplemented()

    assessment_taken_search_order = property(fget=get_assessment_taken_search_order)

    @raise_null_argument
    def apply_assessment_taken_query(self, assessment_taken_query):
        raise Unimplemented()

    def inspect_assessment_taken_query(self):
        raise Unimplemented()

    @raise_null_argument
    def apply_assessment_taken_sequencing(self, assessment_taken_search_order):
        raise Unimplemented()

    @raise_null_argument
    def get_assessment_taken_query_from_inspector(self, assessmen_taken_query_inspector):
        raise Unimplemented()


class BankLookupSession(abc_assessment_sessions.BankLookupSession, osid_sessions.OsidSession):
    """Adapts underlying BankLookupSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'assessment.Bank'

    def can_lookup_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._can('lookup')

    def use_comparative_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bank_view()

    def use_plenary_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bank_view()

    @raise_null_argument
    def get_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_bank(bank_id)

    @raise_null_argument
    def get_banks_by_ids(self, bank_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_ids(bank_ids)

    @raise_null_argument
    def get_banks_by_genus_type(self, bank_genus_type):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_genus_type(bank_genus_type)

    @raise_null_argument
    def get_banks_by_parent_genus_type(self, bank_genus_type):
        raise Unimplemented()

    @raise_null_argument
    def get_banks_by_record_type(self, bank_record_type):
        raise Unimplemented()

    @raise_null_argument
    def get_banks_by_provider(self, resource_id):
        raise Unimplemented()

    def get_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        return self._provider_session.get_banks()

    banks = property(fget=get_banks)


class BankQuerySession(abc_assessment_sessions.BankQuerySession, osid_sessions.OsidSession):
    """Adapts underlying BankQuerySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'assessment.Bank'

    def can_search_banks(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return (self._can('search') or
                bool(self._get_overriding_bank_ids()))

    def get_bank_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_bank_query()

    bank_query = property(fget=get_bank_query)

    @raise_null_argument
    def get_banks_by_query(self, bank_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        return self._provider_session.get_banks_by_query(bank_query)


class BankSearchSession(abc_assessment_sessions.BankSearchSession, BankQuerySession):
    """Adapts underlying BankSearchSession methodswith authorization checks."""

    def get_bank_search(self):
        raise Unimplemented()

    bank_search = property(fget=get_bank_search)

    def get_bank_search_order(self):
        raise Unimplemented()

    bank_search_order = property(fget=get_bank_search_order)

    @raise_null_argument
    def get_banks_by_search(self, bank_query, bank_search):
        raise Unimplemented()

    @raise_null_argument
    def get_bank_query_from_inspector(self, bank_query_inspector):
        raise Unimplemented()


class BankAdminSession(abc_assessment_sessions.BankAdminSession, osid_sessions.OsidSession):
    """Adapts underlying BankAdminSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'assessment.Bank'

    def can_create_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.can_create_bins_template
        return self._can('create')

    @raise_null_argument
    def can_create_bank_with_record_types(self, bank_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types_template
        # This would like to be a real implementation someday:
        if bank_record_types is None:
            raise NullArgument()  # Just 'cause the spec says to :)
        return self._can('create')

    @raise_null_argument
    def get_bank_form_for_create(self, bank_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.get_bank_form_for_create(bank_record_types)

    @raise_null_argument
    def create_bank(self, bank_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        return self._provider_session.create_bank(bank_form)

    def can_update_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._can('update')

    @raise_null_argument
    def get_bank_form_for_update(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.get_bank_form_for_update(bank_id)

    @raise_null_argument
    def update_bank(self, bank_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        return self._provider_session.update_bank(bank_form)

    def can_delete_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._can('delete')

    @raise_null_argument
    def delete_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        return self._provider_session.delete_bank(bank_id)

    def can_manage_bank_aliases(self):
        raise Unimplemented()

    @raise_null_argument
    def alias_bank(self, bank_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        return self._provider_session.alias_bank(bank_id, alias_id)


class BankNotificationSession(abc_assessment_sessions.BankNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying BankNotificationSession methodswith authorization checks."""

    def can_register_for_bank_notifications(self):
        raise Unimplemented()

    def reliable_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_bank_notifications()

    def unreliable_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_bank_notifications()

    @raise_null_argument
    def acknowledge_bank_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_banks(self):
        raise Unimplemented()

    def register_for_changed_banks(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_changed_bank(self, bank_id):
        raise Unimplemented()

    def register_for_deleted_banks(self):
        raise Unimplemented()

    @raise_null_argument
    def register_for_deleted_bank(self, bank_id):
        raise Unimplemented()

    def register_for_changed_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_bank_hierarchy()

    @raise_null_argument
    def register_for_changed_bank_hierarchy_for_ancestors(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_bank_hierarchy_for_ancestors(bank_id)

    @raise_null_argument
    def register_for_changed_bank_hierarchy_for_descendants(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        self._provider_session.register_for_changed_bank_hierarchy_for_descendants(bank_id)

    def reliable_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_bank_notifications()

    def unreliable_bank_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_bank_notifications()

    @raise_null_argument
    def acknowledge_bank_notification(self, notification_id):
        raise Unimplemented()


class BankHierarchySession(abc_assessment_sessions.BankHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying BankHierarchySession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'assessment.Bank'

    def get_bank_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_bank_hierarchy_id()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bank_hierarchy()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_access_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_bank_view()

    def use_plenary_bank_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_bank_view()

    def get_root_bank_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_bank_ids()

    root_bank_ids = property(fget=get_root_bank_ids)

    def get_root_banks(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_root_banks()

    root_banks = property(fget=get_root_banks)

    @raise_null_argument
    def has_parent_banks(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_parent_banks(bank_id)

    @raise_null_argument
    def is_parent_of_bank(self, id_, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_parent_of_bank(id_, bank_id)

    @raise_null_argument
    def get_parent_bank_ids(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_bank_ids(bank_id)

    @raise_null_argument
    def get_parent_banks(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_parent_banks(bank_id)

    @raise_null_argument
    def is_ancestor_of_bank(self, id_, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_ancestor_of_bank(id_, bank_id)

    @raise_null_argument
    def has_child_banks(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.has_child_banks(bank_id)

    @raise_null_argument
    def is_child_of_bank(self, id_, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_child_of_bank(id_, bank_id)

    @raise_null_argument
    def get_child_bank_ids(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_bank_ids(bank_id)

    @raise_null_argument
    def get_child_banks(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_child_banks(bank_id)

    @raise_null_argument
    def is_descendant_of_bank(self, id_, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.is_descendant_of_bank(id_, bank_id)

    @raise_null_argument
    def get_bank_node_ids(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bank_node_ids(
            bank_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)

    @raise_null_argument
    def get_bank_nodes(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bank_nodes(
            bank_id,
            ancestor_levels,
            descendant_levels,
            include_siblings)


class BankHierarchyDesignSession(abc_assessment_sessions.BankHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying BankHierarchyDesignSession methodswith authorization checks."""
    def __init__(self, *args, **kwargs):
        osid_sessions.OsidSession.__init__(self, *args, **kwargs)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'assessment.Bank'
        # should this be 'assessment.BankHierarchy' ?

    def get_bank_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_bank_hierarchy_id()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        return self._provider_session.get_bank_hierarchy()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_modify_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    @raise_null_argument
    def add_root_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_root_bank(bank_id)

    @raise_null_argument
    def remove_root_bank(self, bank_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_root_bank(bank_id)

    @raise_null_argument
    def add_child_bank(self, bank_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.add_child_bank(bank_id, child_id)

    @raise_null_argument
    def remove_child_bank(self, bank_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_bank(bank_id, child_id)

    @raise_null_argument
    def remove_child_banks(self, bank_id):
        if not self._can('modify'):
            raise PermissionDenied()
        return self._provider_session.remove_child_banks(bank_id)
