"""JSON implementations of assessment.authoring searches."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import objects
from . import queries
from .. import utilities
from ..osid import searches as osid_searches
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.assessment_authoring import searches as abc_assessment_authoring_searches
from dlkit.abstract_osid.osid import errors


class AssessmentPartSearch(abc_assessment_authoring_searches.AssessmentPartSearch, osid_searches.OsidSearch):
    """The search interface for governing assessment part searches."""
    def __init__(self, runtime):
        self._namespace = 'assessment.authoring.AssessmentPart'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_assessment_parts(self, bank_ids):
        """Execute this search among the given list of assessment parts.

        arg:    bank_ids (osid.id.IdList): list of assessment parts
        raise:  NullArgument - ``bank_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = bank_ids

    @utilities.arguments_not_none
    def order_assessment_part_results(self, assessment_part_search_order):
        """Specify an ordering to the search results.

        arg:    assessment_part_search_order
                (osid.assessment.authoring.AssessmentPartSearchOrder):
                assessment part search order
        raise:  NullArgument - ``assessment_part_search_order`` is
                ``null``
        raise:  Unsupported - ``assessment_part_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessment_part_search_record(self, assessment_part_search_record_type):
        """Gets the assessment part search record corresponding to the given assessment part search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_part_search_record_type (osid.type.Type): an
                assessment part search record type
        return:
                (osid.assessment.authoring.records.AssessmentPartSearchR
                ecord) - the assessment part search record
        raise:  NullArgument - ``assessment_part_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_part_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class AssessmentPartSearchResults(abc_assessment_authoring_searches.AssessmentPartSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'assessment.authoring.AssessmentPart'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_assessment_parts(self):
        """Gets the ``AssessmentPartList`` resulting from a search.

        return: (osid.assessment.authoring.AssessmentPartList) - the
                assessment part list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.AssessmentPartList(self._results, runtime=self._runtime)

    assessment_parts = property(fget=get_assessment_parts)

    def get_assessment_part_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.authoring.AssessmentPartQueryInspector)
                - the assessment part query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.AssessmentPartQueryInspector(self._query_terms, runtime=self._runtime)

    assessment_part_query_inspector = property(fget=get_assessment_part_query_inspector)

    @utilities.arguments_not_none
    def get_assessment_part_search_results_record(self, assessment_part_search_record_type):
        """Gets the assessment part search results record corresponding to the given assessment part search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record.

        arg:    assessment_part_search_record_type (osid.type.Type): an
                assessment part search record type
        return: (osid.assessment.authoring.records.AssessmentPartSearchR
                esultsRecord) - the assessment part search results
                record
        raise:  NullArgument - ``assessment_part_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(assessment_part_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class SequenceRuleSearch(abc_assessment_authoring_searches.SequenceRuleSearch, osid_searches.OsidSearch):
    """The search interface for governing sequence rule searches."""
    def __init__(self, runtime):
        self._namespace = 'assessment.authoring.SequenceRule'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_sequence_rules(self, bank_ids):
        """Execute this search among the given list of sequence rules.

        arg:    bank_ids (osid.id.IdList): list of sequence rules
        raise:  NullArgument - ``bank_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = bank_ids

    @utilities.arguments_not_none
    def order_sequence_rule_results(self, sequence_rule_search_order):
        """Specify an ordering to the search results.

        arg:    sequence_rule_search_order
                (osid.assessment.authoring.SequenceRuleSearchOrder):
                sequence rule search order
        raise:  NullArgument - ``sequence_rule_search_order`` is
                ``null``
        raise:  Unsupported - ``sequence_rule_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_sequence_rule_search_record(self, sequence_rule_search_record_type):
        """Gets the sequence rule search record corresponding to the given sequence rule search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    sequence_rule_search_record_type (osid.type.Type): a
                sequence rule search record type
        return:
                (osid.assessment.authoring.records.SequenceRuleSearchRec
                ord) - the sequence rule search record
        raise:  NullArgument - ``sequence_rule_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(sequence_rule_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class SequenceRuleSearchResults(abc_assessment_authoring_searches.SequenceRuleSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'assessment.authoring.SequenceRule'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_sequence_rules(self):
        """Gets the ``SequenceRuleList`` resulting from a search.

        return: (osid.assessment.authoring.SequenceRuleList) - the
                sequence rule list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.SequenceRuleList(self._results, runtime=self._runtime)

    sequence_rules = property(fget=get_sequence_rules)

    def get_sequence_rule_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.authoring.SequenceRuleQueryInspector) -
                the sequence rule query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.SequenceRuleQueryInspector(self._query_terms, runtime=self._runtime)

    sequence_rule_query_inspector = property(fget=get_sequence_rule_query_inspector)

    @utilities.arguments_not_none
    def get_sequence_rule_search_results_record(self, sequence_rule_search_record_type):
        """Gets the sequence rule search results record corresponding to the given sequence rule search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record.

        arg:    sequence_rule_search_record_type (osid.type.Type): a
                sequence rule search record type
        return: (osid.assessment.authoring.records.SequenceRuleSearchRes
                ultsRecord) - the sequence rule search results record
        raise:  NullArgument - ``sequence_rule_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(sequence_rule_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
