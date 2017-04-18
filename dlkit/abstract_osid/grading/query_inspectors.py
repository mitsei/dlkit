"""Implementations of grading abstract base class query_inspectors."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class GradeQueryInspector:
    """This is the query inspector for examining grade queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_id_terms(self):
        """Gets the grade system ``Id`` terms.

        :return: the grade system ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_system_id_terms = property(fget=get_grade_system_id_terms)

    @abc.abstractmethod
    def get_grade_system_terms(self):
        """Gets the grade system terms.

        :return: the grade system terms
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    grade_system_terms = property(fget=get_grade_system_terms)

    @abc.abstractmethod
    def get_input_score_start_range_terms(self):
        """Gets the input score start range terms.

        :return: the input score start range terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    input_score_start_range_terms = property(fget=get_input_score_start_range_terms)

    @abc.abstractmethod
    def get_input_score_end_range_terms(self):
        """Gets the input score end range terms.

        :return: the input score end range terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    input_score_end_range_terms = property(fget=get_input_score_end_range_terms)

    @abc.abstractmethod
    def get_input_score_terms(self):
        """Gets the input score terms.

        :return: the input score range terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    input_score_terms = property(fget=get_input_score_terms)

    @abc.abstractmethod
    def get_output_score_terms(self):
        """Gets the output score terms.

        :return: the output score terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    output_score_terms = property(fget=get_output_score_terms)

    @abc.abstractmethod
    def get_grade_entry_id_terms(self):
        """Gets the grade entry ``Id`` terms.

        :return: the grade entry ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_entry_id_terms = property(fget=get_grade_entry_id_terms)

    @abc.abstractmethod
    def get_grade_entry_terms(self):
        """Gets the grade entry terms.

        :return: the grade entry terms
        :rtype: ``osid.grading.GradeEntryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryQueryInspector

    grade_entry_terms = property(fget=get_grade_entry_terms)

    @abc.abstractmethod
    def get_gradebook_id_terms(self):
        """Gets the gradebook ``Id`` terms.

        :return: the gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_id_terms = property(fget=get_gradebook_id_terms)

    @abc.abstractmethod
    def get_gradebook_terms(self):
        """Gets the gradebook terms.

        :return: the gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    gradebook_terms = property(fget=get_gradebook_terms)

    @abc.abstractmethod
    def get_grade_query_inspector_record(self, grade_record_type):
        """Gets the grade query inspector record corresponding to the given ``Grade`` record ``Type``.

        :param grade_record_type: a grade record type
        :type grade_record_type: ``osid.type.Type``
        :return: the grade query inspector record
        :rtype: ``osid.grading.records.GradeQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeQueryInspectorRecord


class GradeSystemQueryInspector:
    """This is the query inspector for examining grade system queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_based_on_grades_terms(self):
        """Gets the grade-based systems terms.

        :return: the grade-based systems terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    based_on_grades_terms = property(fget=get_based_on_grades_terms)

    @abc.abstractmethod
    def get_grade_id_terms(self):
        """Gets the grade ``Id`` terms.

        :return: the grade ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_id_terms = property(fget=get_grade_id_terms)

    @abc.abstractmethod
    def get_grade_terms(self):
        """Gets the grade terms.

        :return: the grade terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    grade_terms = property(fget=get_grade_terms)

    @abc.abstractmethod
    def get_lowest_numeric_score_terms(self):
        """Gets the lowest numeric score terms.

        :return: the lowest numeric score terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    lowest_numeric_score_terms = property(fget=get_lowest_numeric_score_terms)

    @abc.abstractmethod
    def get_numeric_score_increment_terms(self):
        """Gets the numeric score increment terms.

        :return: the numeric score increment terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    numeric_score_increment_terms = property(fget=get_numeric_score_increment_terms)

    @abc.abstractmethod
    def get_highest_numeric_score_terms(self):
        """Gets the highest numeric score terms.

        :return: the highest numeric score terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    highest_numeric_score_terms = property(fget=get_highest_numeric_score_terms)

    @abc.abstractmethod
    def get_gradebook_column_id_terms(self):
        """Gets the gradebook column ``Id`` terms.

        :return: the gradebook column ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_column_id_terms = property(fget=get_gradebook_column_id_terms)

    @abc.abstractmethod
    def get_gradebook_column_terms(self):
        """Gets the gradebook column terms.

        :return: the gradebook column terms
        :rtype: ``osid.grading.GradebookColumnQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnQueryInspector

    gradebook_column_terms = property(fget=get_gradebook_column_terms)

    @abc.abstractmethod
    def get_gradebook_id_terms(self):
        """Gets the gradebook ``Id`` terms.

        :return: the gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_id_terms = property(fget=get_gradebook_id_terms)

    @abc.abstractmethod
    def get_gradebook_terms(self):
        """Gets the gradebook terms.

        :return: the gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    gradebook_terms = property(fget=get_gradebook_terms)

    @abc.abstractmethod
    def get_grade_system_query_inspector_record(self, grade_system_record_type):
        """Gets the grade system query inspector record corresponding to the given ``GradeSystem`` record ``Type``.

        :param grade_system_record_type: a grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system query inspector record
        :rtype: ``osid.grading.records.GradeSystemQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemQueryInspectorRecord


class GradeEntryQueryInspector:
    """This is the query inspector for examining grade entry queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_column_id_terms(self):
        """Gets the gradebook column ``Id`` terms.

        :return: the gradebook column ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_column_id_terms = property(fget=get_gradebook_column_id_terms)

    @abc.abstractmethod
    def get_gradebook_column_terms(self):
        """Gets the gradebook column terms.

        :return: the gradebook column terms
        :rtype: ``osid.grading.GradebookColumnQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnQueryInspector

    gradebook_column_terms = property(fget=get_gradebook_column_terms)

    @abc.abstractmethod
    def get_key_resource_id_terms(self):
        """Gets the key resource ``Id`` terms.

        :return: the key resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    key_resource_id_terms = property(fget=get_key_resource_id_terms)

    @abc.abstractmethod
    def get_key_resource_terms(self):
        """Gets the key resource terms.

        :return: the key resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    key_resource_terms = property(fget=get_key_resource_terms)

    @abc.abstractmethod
    def get_derived_terms(self):
        """Gets the derived terms.

        :return: the derived terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    derived_terms = property(fget=get_derived_terms)

    @abc.abstractmethod
    def get_overridden_grade_entry_id_terms(self):
        """Gets the overridden calculated grade entry ``Id`` terms.

        :return: the overridden grade entry ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    overridden_grade_entry_id_terms = property(fget=get_overridden_grade_entry_id_terms)

    @abc.abstractmethod
    def get_overridden_grade_entry_terms(self):
        """Gets the overriden derived grade terms.

        :return: the overridden grade entry terms
        :rtype: ``osid.grading.GradeEntryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryQueryInspector

    overridden_grade_entry_terms = property(fget=get_overridden_grade_entry_terms)

    @abc.abstractmethod
    def get_ignored_for_calculations_terms(self):
        """Gets the ignored for caluclation entries terms.

        :return: the ignored for calculation terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    ignored_for_calculations_terms = property(fget=get_ignored_for_calculations_terms)

    @abc.abstractmethod
    def get_grade_id_terms(self):
        """Gets the grade ``Id`` terms.

        :return: the grade ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_id_terms = property(fget=get_grade_id_terms)

    @abc.abstractmethod
    def get_grade_terms(self):
        """Gets the grade terms.

        :return: the grade terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    grade_terms = property(fget=get_grade_terms)

    @abc.abstractmethod
    def get_score_terms(self):
        """Gets the score terms.

        :return: the score terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    score_terms = property(fget=get_score_terms)

    @abc.abstractmethod
    def get_time_graded_terms(self):
        """Gets the time graded terms.

        :return: the time graded terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    time_graded_terms = property(fget=get_time_graded_terms)

    @abc.abstractmethod
    def get_grader_id_terms(self):
        """Gets the grader ``Id`` terms.

        :return: the grader ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grader_id_terms = property(fget=get_grader_id_terms)

    @abc.abstractmethod
    def get_grader_terms(self):
        """Gets the grader terms.

        :return: the grader terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    grader_terms = property(fget=get_grader_terms)

    @abc.abstractmethod
    def get_grading_agent_id_terms(self):
        """Gets the grading agent ``Id`` terms.

        :return: the grading agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grading_agent_id_terms = property(fget=get_grading_agent_id_terms)

    @abc.abstractmethod
    def get_grading_agent_terms(self):
        """Gets the grading agent terms.

        :return: the grading agent terms
        :rtype: ``osid.authentication.AgentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQueryInspector

    grading_agent_terms = property(fget=get_grading_agent_terms)

    @abc.abstractmethod
    def get_gradebook_id_terms(self):
        """Gets the gradebook ``Id`` terms.

        :return: the gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_id_terms = property(fget=get_gradebook_id_terms)

    @abc.abstractmethod
    def get_gradebook_terms(self):
        """Gets the gradebook terms.

        :return: the gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    gradebook_terms = property(fget=get_gradebook_terms)

    @abc.abstractmethod
    def get_grade_entry_query_inspector_record(self, grade_entry_record_type):
        """Gets the grade entry query inspector record corresponding to the given ``GradeEntry`` record ``Type``.

        :param grade_entry_record_type: a grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the grade entry query inspector record
        :rtype: ``osid.grading.records.GradeEntryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntryQueryInspectorRecord


class GradebookColumnQueryInspector:
    """This is the query inspector for examining gradebook column queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_id_terms(self):
        """Gets the grade system ``Id`` terms.

        :return: the grade system ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_system_id_terms = property(fget=get_grade_system_id_terms)

    @abc.abstractmethod
    def get_grade_system_terms(self):
        """Gets the grade system terms.

        :return: the grade system terms
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    grade_system_terms = property(fget=get_grade_system_terms)

    @abc.abstractmethod
    def get_grade_entry_id_terms(self):
        """Gets the grade entry ``Id`` terms.

        :return: the grade entry ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_entry_id_terms = property(fget=get_grade_entry_id_terms)

    @abc.abstractmethod
    def get_grade_entry_terms(self):
        """Gets the grade entry terms.

        :return: the grade entry terms
        :rtype: ``osid.grading.GradeEntryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryQueryInspector

    grade_entry_terms = property(fget=get_grade_entry_terms)

    @abc.abstractmethod
    def get_gradebook_column_summary_terms(self):
        """Gets the gradebook column summary terms.

        :return: the gradebook column summary terms
        :rtype: ``osid.grading.GradebookColumnSummaryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnSummaryQueryInspector

    gradebook_column_summary_terms = property(fget=get_gradebook_column_summary_terms)

    @abc.abstractmethod
    def get_gradebook_id_terms(self):
        """Gets the gradebook ``Id`` terms.

        :return: the gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_id_terms = property(fget=get_gradebook_id_terms)

    @abc.abstractmethod
    def get_gradebook_terms(self):
        """Gets the gradebook terms.

        :return: the gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    gradebook_terms = property(fget=get_gradebook_terms)

    @abc.abstractmethod
    def get_gradebook_column_query_inspector_record(self, gradebook_column_record_type):
        """Gets the gradebook column query inspector record corresponding to the given ``GradebookColumn`` record ``Type``.

        :param gradebook_column_record_type: a gradebook column record type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the gradebook column query inspector record
        :rtype: ``osid.grading.records.GradebookColumnQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnQueryInspectorRecord


class GradebookColumnSummaryQueryInspector:
    """This is the query inspector for examining gradebook column summary queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_column_id_terms(self):
        """Gets the gradebook column ``Id`` terms.

        :return: the gradebook column ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_column_id_terms = property(fget=get_gradebook_column_id_terms)

    @abc.abstractmethod
    def get_gradebook_column_terms(self):
        """Gets the gradebook column terms.

        :return: the gradebookc column terms
        :rtype: ``osid.grading.GradebookColumnQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnQueryInspector

    gradebook_column_terms = property(fget=get_gradebook_column_terms)

    @abc.abstractmethod
    def get_mean_terms(self):
        """Gets the mean terms.

        :return: the mean terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    mean_terms = property(fget=get_mean_terms)

    @abc.abstractmethod
    def get_minimum_mean_terms(self):
        """Gets the minimum mean terms.

        :return: the minimum mean terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_mean_terms = property(fget=get_minimum_mean_terms)

    @abc.abstractmethod
    def get_median_terms(self):
        """Gets the median terms.

        :return: the median terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    median_terms = property(fget=get_median_terms)

    @abc.abstractmethod
    def get_minimum_median_terms(self):
        """Gets the minimum median terms.

        :return: the minimum median terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_median_terms = property(fget=get_minimum_median_terms)

    @abc.abstractmethod
    def get_mode_terms(self):
        """Gets the mode terms.

        :return: the mode terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    mode_terms = property(fget=get_mode_terms)

    @abc.abstractmethod
    def get_minimum_mode_terms(self):
        """Gets the minimum mode terms.

        :return: the minimum mode terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_mode_terms = property(fget=get_minimum_mode_terms)

    @abc.abstractmethod
    def get_rms_terms(self):
        """Gets the rms terms.

        :return: the rms terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    rms_terms = property(fget=get_rms_terms)

    @abc.abstractmethod
    def get_minimum_rms_terms(self):
        """Gets the minimum rms terms.

        :return: the minimum rms terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_rms_terms = property(fget=get_minimum_rms_terms)

    @abc.abstractmethod
    def get_standard_deviation_terms(self):
        """Gets the standard deviation terms.

        :return: the standard deviation terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    standard_deviation_terms = property(fget=get_standard_deviation_terms)

    @abc.abstractmethod
    def get_minimum_standard_deviation_terms(self):
        """Gets the minimum standard deviation terms.

        :return: the minimum standard deviation terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_standard_deviation_terms = property(fget=get_minimum_standard_deviation_terms)

    @abc.abstractmethod
    def get_sum_terms(self):
        """Gets the sum terms.

        :return: the sum terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    sum_terms = property(fget=get_sum_terms)

    @abc.abstractmethod
    def get_minimum_sum_terms(self):
        """Gets the minimum sum terms.

        :return: the minimum sum terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_sum_terms = property(fget=get_minimum_sum_terms)

    @abc.abstractmethod
    def get_gradebook_id_terms(self):
        """Gets the gradebook ``Id`` terms.

        :return: the gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_id_terms = property(fget=get_gradebook_id_terms)

    @abc.abstractmethod
    def get_gradebook_terms(self):
        """Gets the gradebook terms.

        :return: the gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    gradebook_terms = property(fget=get_gradebook_terms)

    @abc.abstractmethod
    def get_gradebook_column_summary_query_inspector_record(self, gradebook_column_summary_record_type):
        """Gets the gradebook column summary query inspector record corresponding to the given ``GradebookColumnSummary`` record ``Type``.

        :param gradebook_column_summary_record_type: a gradebook column summry record type
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: the gradebook column summary query inspector record
        :rtype: ``osid.grading.records.GradebookColumnSummaryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_summary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_summary_record_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSummaryQueryInspectorRecord


class GradebookQueryInspector:
    """This is the query inspector for examining gradebook queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_id_terms(self):
        """Gets the grade system ``Id`` terms.

        :return: the grade system ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_system_id_terms = property(fget=get_grade_system_id_terms)

    @abc.abstractmethod
    def get_grade_system_terms(self):
        """Gets the grade system terms.

        :return: the grade system terms
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    grade_system_terms = property(fget=get_grade_system_terms)

    @abc.abstractmethod
    def get_grade_entry_id_terms(self):
        """Gets the grade entry ``Id`` terms.

        :return: the grade entry ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_entry_id_terms = property(fget=get_grade_entry_id_terms)

    @abc.abstractmethod
    def get_grade_entry_terms(self):
        """Gets the grade entry terms.

        :return: the grade entry terms
        :rtype: ``osid.grading.GradeEntryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryQueryInspector

    grade_entry_terms = property(fget=get_grade_entry_terms)

    @abc.abstractmethod
    def get_gradebook_column_id_terms(self):
        """Gets the gradebook column ``Id`` terms.

        :return: the gradebook column ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    gradebook_column_id_terms = property(fget=get_gradebook_column_id_terms)

    @abc.abstractmethod
    def get_gradebook_column_terms(self):
        """Gets the gradebook column terms.

        :return: the gradebook column terms
        :rtype: ``osid.grading.GradebookColumnQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnQueryInspector

    gradebook_column_terms = property(fget=get_gradebook_column_terms)

    @abc.abstractmethod
    def get_ancestor_gradebook_id_terms(self):
        """Gets the ancestor gradebook ``Id`` terms.

        :return: the ancestor gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_gradebook_id_terms = property(fget=get_ancestor_gradebook_id_terms)

    @abc.abstractmethod
    def get_ancestor_gradebook_terms(self):
        """Gets the ancestor gradebook terms.

        :return: the ancestor gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    ancestor_gradebook_terms = property(fget=get_ancestor_gradebook_terms)

    @abc.abstractmethod
    def get_descendant_gradebook_id_terms(self):
        """Gets the descendant gradebook ``Id`` terms.

        :return: the descendant gradebook ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_gradebook_id_terms = property(fget=get_descendant_gradebook_id_terms)

    @abc.abstractmethod
    def get_descendant_gradebook_terms(self):
        """Gets the descendant gradebook terms.

        :return: the descendant gradebook terms
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    descendant_gradebook_terms = property(fget=get_descendant_gradebook_terms)

    @abc.abstractmethod
    def get_gradebook_query_inspector_record(self, gradebook_record_type):
        """Gets the gradebook query inspector record corresponding to the given ``Gradebook`` record ``Type``.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook query inspector record
        :rtype: ``osid.grading.records.GradebookQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookQueryInspectorRecord
