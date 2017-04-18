"""Implementations of assessment abstract base class query_inspectors."""
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


class QuestionQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_question_query_inspector_record(self, question_record_type):
        """Gets the record query inspector corresponding to the given ``Question`` record ``Type``.

        :param question_record_type: a question record type
        :type question_record_type: ``osid.type.Type``
        :return: the question query inspector record
        :rtype: ``osid.assessment.records.QuestionQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``question_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(question_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.QuestionQueryInspectorRecord


class AnswerQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_answer_query_inspector_record(self, question_record_type):
        """Gets the record query inspector corresponding to the given ``Question`` record ``Type``.

        :param question_record_type: a question record type
        :type question_record_type: ``osid.type.Type``
        :return: the answer query inspector record
        :rtype: ``osid.assessment.records.AnswerQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``question_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(question_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AnswerQueryInspectorRecord


class ItemQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_learning_objective_id_terms(self):
        """Gets the learning objective ``Id`` query terms.

        :return: the learning objective ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    learning_objective_id_terms = property(fget=get_learning_objective_id_terms)

    @abc.abstractmethod
    def get_learning_objective_terms(self):
        """Gets the learning objective query terms.

        :return: the learning objective terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    learning_objective_terms = property(fget=get_learning_objective_terms)

    @abc.abstractmethod
    def get_question_id_terms(self):
        """Gets the question ``Id`` query terms.

        :return: the question ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    question_id_terms = property(fget=get_question_id_terms)

    @abc.abstractmethod
    def get_question_terms(self):
        """Gets the question query terms.

        :return: the question terms
        :rtype: ``osid.assessment.QuestionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.QuestionQueryInspector

    question_terms = property(fget=get_question_terms)

    @abc.abstractmethod
    def get_answer_id_terms(self):
        """Gets the answer ``Id`` query terms.

        :return: the answer ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    answer_id_terms = property(fget=get_answer_id_terms)

    @abc.abstractmethod
    def get_answer_terms(self):
        """Gets the answer query terms.

        :return: the answer terms
        :rtype: ``osid.assessment.AnswerQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AnswerQueryInspector

    answer_terms = property(fget=get_answer_terms)

    @abc.abstractmethod
    def get_assessment_id_terms(self):
        """Gets the assessment ``Id`` query terms.

        :return: the assessment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_id_terms = property(fget=get_assessment_id_terms)

    @abc.abstractmethod
    def get_assessment_terms(self):
        """Gets the assessment query terms.

        :return: the assessment terms
        :rtype: ``osid.assessment.AssessmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    assessment_terms = property(fget=get_assessment_terms)

    @abc.abstractmethod
    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    @abc.abstractmethod
    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the bank terms
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    @abc.abstractmethod
    def get_item_query_inspector_record(self, item_record_type):
        """Gets the record query inspector corresponding to the given ``Item`` record ``Type``.

        :param item_record_type: an item record type
        :type item_record_type: ``osid.type.Type``
        :return: the item query inspector record
        :rtype: ``osid.assessment.records.ItemQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemQueryInspectorRecord


class AssessmentQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_level_id_terms(self):
        """Gets the level ``Id`` query terms.

        :return: the level ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    level_id_terms = property(fget=get_level_id_terms)

    @abc.abstractmethod
    def get_level_terms(self):
        """Gets the level query terms.

        :return: the level terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    level_terms = property(fget=get_level_terms)

    @abc.abstractmethod
    def get_rubric_id_terms(self):
        """Gets the assessment ``Id`` query terms.

        :return: the assessment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    rubric_id_terms = property(fget=get_rubric_id_terms)

    @abc.abstractmethod
    def get_rubric_terms(self):
        """Gets the assessment query terms.

        :return: the assessment terms
        :rtype: ``osid.assessment.AssessmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    rubric_terms = property(fget=get_rubric_terms)

    @abc.abstractmethod
    def get_item_id_terms(self):
        """Gets the item ``Id`` query terms.

        :return: the item ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    item_id_terms = property(fget=get_item_id_terms)

    @abc.abstractmethod
    def get_item_terms(self):
        """Gets the item query terms.

        :return: the item terms
        :rtype: ``osid.assessment.ItemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQueryInspector

    item_terms = property(fget=get_item_terms)

    @abc.abstractmethod
    def get_assessment_offered_id_terms(self):
        """Gets the assessment offered ``Id`` query terms.

        :return: the assessment offered ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_offered_id_terms = property(fget=get_assessment_offered_id_terms)

    @abc.abstractmethod
    def get_assessment_offered_terms(self):
        """Gets the assessment offered query terms.

        :return: the assessment offered terms
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQueryInspector

    assessment_offered_terms = property(fget=get_assessment_offered_terms)

    @abc.abstractmethod
    def get_assessment_taken_id_terms(self):
        """Gets the assessment taken ``Id`` query terms.

        :return: the assessment taken ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_taken_id_terms = property(fget=get_assessment_taken_id_terms)

    @abc.abstractmethod
    def get_assessment_taken_terms(self):
        """Gets the assessment taken query terms.

        :return: the assessment taken terms
        :rtype: ``osid.assessment.AssessmentTakenQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQueryInspector

    assessment_taken_terms = property(fget=get_assessment_taken_terms)

    @abc.abstractmethod
    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    @abc.abstractmethod
    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the bank terms
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    @abc.abstractmethod
    def get_assessment_query_inspector_record(self, assessment_record_type):
        """Gets the assessment query inspector record corresponding to the given ``Assessment`` record ``Type``.

        :param assessment_record_type: an assessment record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the assessment query inspector record
        :rtype: ``osid.assessment.records.AssessmentQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentQueryInspectorRecord


class AssessmentOfferedQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_id_terms(self):
        """Gets the assessment ``Id`` query terms.

        :return: the assessment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_id_terms = property(fget=get_assessment_id_terms)

    @abc.abstractmethod
    def get_assessment_terms(self):
        """Gets the assessment query terms.

        :return: the assessment terms
        :rtype: ``osid.assessment.AssessmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    assessment_terms = property(fget=get_assessment_terms)

    @abc.abstractmethod
    def get_level_id_terms(self):
        """Gets the level ``Id`` query terms.

        :return: the level ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    level_id_terms = property(fget=get_level_id_terms)

    @abc.abstractmethod
    def get_level_terms(self):
        """Gets the level query terms.

        :return: the level terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    level_terms = property(fget=get_level_terms)

    @abc.abstractmethod
    def get_items_sequential_terms(self):
        """Gets the items sequential query terms.

        :return: the boolean terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    items_sequential_terms = property(fget=get_items_sequential_terms)

    @abc.abstractmethod
    def get_items_shuffled_terms(self):
        """Gets the items shuffled query terms.

        :return: the boolean terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    items_shuffled_terms = property(fget=get_items_shuffled_terms)

    @abc.abstractmethod
    def get_start_time_terms(self):
        """Gets the start time query terms.

        :return: the start time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    start_time_terms = property(fget=get_start_time_terms)

    @abc.abstractmethod
    def get_deadline_terms(self):
        """Gets the deadline query terms.

        :return: the deadline terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    deadline_terms = property(fget=get_deadline_terms)

    @abc.abstractmethod
    def get_duration_terms(self):
        """Gets the deadline query terms.

        :return: the duration terms
        :rtype: ``osid.search.terms.DurationTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationTerm

    duration_terms = property(fget=get_duration_terms)

    @abc.abstractmethod
    def get_score_system_id_terms(self):
        """Gets the grade system ``Id`` query terms.

        :return: the grade system ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    score_system_id_terms = property(fget=get_score_system_id_terms)

    @abc.abstractmethod
    def get_score_system_terms(self):
        """Gets the grade system query terms.

        :return: the grade system terms
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    score_system_terms = property(fget=get_score_system_terms)

    @abc.abstractmethod
    def get_grade_system_id_terms(self):
        """Gets the grade system ``Id`` query terms.

        :return: the grade system ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_system_id_terms = property(fget=get_grade_system_id_terms)

    @abc.abstractmethod
    def get_grade_system_terms(self):
        """Gets the grade system query terms.

        :return: the grade system terms
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    grade_system_terms = property(fget=get_grade_system_terms)

    @abc.abstractmethod
    def get_rubric_id_terms(self):
        """Gets the assessment offered ``Id`` query terms.

        :return: the assessment offered ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    rubric_id_terms = property(fget=get_rubric_id_terms)

    @abc.abstractmethod
    def get_rubric_terms(self):
        """Gets the assessment query terms.

        :return: the assessment offered terms
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQueryInspector

    rubric_terms = property(fget=get_rubric_terms)

    @abc.abstractmethod
    def get_assessment_taken_id_terms(self):
        """Gets the assessment taken ``Id`` query terms.

        :return: the assessment taken ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_taken_id_terms = property(fget=get_assessment_taken_id_terms)

    @abc.abstractmethod
    def get_assessment_taken_terms(self):
        """Gets the assessment taken query terms.

        :return: the assessment taken terms
        :rtype: ``osid.assessment.AssessmentTakenQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQueryInspector

    assessment_taken_terms = property(fget=get_assessment_taken_terms)

    @abc.abstractmethod
    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    @abc.abstractmethod
    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the bank terms
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    @abc.abstractmethod
    def get_assessment_offered_query_inspector_record(self, assessment_offered_record_type):
        """Gets the assessment offered query inspector record corresponding to the given ``AssessmentOffered`` record ``Type``.

        :param assessment_offered_record_type: an assessment offered record type
        :type assessment_offered_record_type: ``osid.type.Type``
        :return: the assessment offered query inspector record
        :rtype: ``osid.assessment.records.AssessmentOfferedQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedQueryInspectorRecord


class AssessmentTakenQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_offered_id_terms(self):
        """Gets the assessment offered ``Id`` query terms.

        :return: the assessment offered ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_offered_id_terms = property(fget=get_assessment_offered_id_terms)

    @abc.abstractmethod
    def get_assessment_offered_terms(self):
        """Gets the assessment offered query terms.

        :return: the assessment offered terms
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQueryInspector

    assessment_offered_terms = property(fget=get_assessment_offered_terms)

    @abc.abstractmethod
    def get_taker_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    taker_id_terms = property(fget=get_taker_id_terms)

    @abc.abstractmethod
    def get_taker_terms(self):
        """Gets the resource query terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    taker_terms = property(fget=get_taker_terms)

    @abc.abstractmethod
    def get_taking_agent_id_terms(self):
        """Gets the agent ``Id`` query terms.

        :return: the agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    taking_agent_id_terms = property(fget=get_taking_agent_id_terms)

    @abc.abstractmethod
    def get_taking_agent_terms(self):
        """Gets the agent query terms.

        :return: the agent terms
        :rtype: ``osid.authentication.AgentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQueryInspector

    taking_agent_terms = property(fget=get_taking_agent_terms)

    @abc.abstractmethod
    def get_actual_start_time_terms(self):
        """Gets the start time query terms.

        :return: the start time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    actual_start_time_terms = property(fget=get_actual_start_time_terms)

    @abc.abstractmethod
    def get_completion_time_terms(self):
        """Gets the completion time query terms.

        :return: the completion time terms
        :rtype: ``osid.search.terms.DateTimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeTerm

    completion_time_terms = property(fget=get_completion_time_terms)

    @abc.abstractmethod
    def get_time_spent_terms(self):
        """Gets the time spent query terms.

        :return: the time spent terms
        :rtype: ``osid.search.terms.DurationTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationTerm

    time_spent_terms = property(fget=get_time_spent_terms)

    @abc.abstractmethod
    def get_score_system_id_terms(self):
        """Gets the grade system ``Id`` query terms.

        :return: the grade system ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    score_system_id_terms = property(fget=get_score_system_id_terms)

    @abc.abstractmethod
    def get_score_system_terms(self):
        """Gets the grade system query terms.

        :return: the grade system terms
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    score_system_terms = property(fget=get_score_system_terms)

    @abc.abstractmethod
    def get_score_terms(self):
        """Gets the score query terms.

        :return: the score terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    score_terms = property(fget=get_score_terms)

    @abc.abstractmethod
    def get_grade_id_terms(self):
        """Gets the grade ``Id`` query terms.

        :return: the grade ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    grade_id_terms = property(fget=get_grade_id_terms)

    @abc.abstractmethod
    def get_grade_terms(self):
        """Gets the grade query terms.

        :return: the grade terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    grade_terms = property(fget=get_grade_terms)

    @abc.abstractmethod
    def get_feedback_terms(self):
        """Gets the comment query terms.

        :return: the comment terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    feedback_terms = property(fget=get_feedback_terms)

    @abc.abstractmethod
    def get_rubric_id_terms(self):
        """Gets the assessment taken ``Id`` query terms.

        :return: the assessment taken ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    rubric_id_terms = property(fget=get_rubric_id_terms)

    @abc.abstractmethod
    def get_rubric_terms(self):
        """Gets the assessment taken query terms.

        :return: the assessment taken terms
        :rtype: ``osid.assessment.AssessmentTakenQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQueryInspector

    rubric_terms = property(fget=get_rubric_terms)

    @abc.abstractmethod
    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    @abc.abstractmethod
    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the bank terms
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    @abc.abstractmethod
    def get_assessment_taken_query_inspector_record(self, assessment_taken_record_type):
        """Gets the assessment taken query inspector record corresponding to the given ``AssessmentTaken`` record ``Type``.

        :param assessment_taken_record_type: an assessment taken record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the assessment taken query inspector record
        :rtype: ``osid.assessment.records.AssessmentTakenQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenQueryInspectorRecord


class BankQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_item_id_terms(self):
        """Gets the item ``Id`` query terms.

        :return: the item ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    item_id_terms = property(fget=get_item_id_terms)

    @abc.abstractmethod
    def get_item_terms(self):
        """Gets the item query terms.

        :return: the item query terms
        :rtype: ``osid.assessment.ItemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQueryInspector

    item_terms = property(fget=get_item_terms)

    @abc.abstractmethod
    def get_assessment_id_terms(self):
        """Gets the assessment ``Id`` query terms.

        :return: the assessment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_id_terms = property(fget=get_assessment_id_terms)

    @abc.abstractmethod
    def get_assessment_terms(self):
        """Gets the assessment query terms.

        :return: the assessment terms
        :rtype: ``osid.assessment.AssessmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    assessment_terms = property(fget=get_assessment_terms)

    @abc.abstractmethod
    def get_assessment_offered_id_terms(self):
        """Gets the assessment offered ``Id`` query terms.

        :return: the assessment offered ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_offered_id_terms = property(fget=get_assessment_offered_id_terms)

    @abc.abstractmethod
    def get_assessment_offered_terms(self):
        """Gets the assessment offered query terms.

        :return: the assessment offered terms
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQueryInspector

    assessment_offered_terms = property(fget=get_assessment_offered_terms)

    @abc.abstractmethod
    def get_ancestor_bank_id_terms(self):
        """Gets the ancestor bank ``Id`` query terms.

        :return: the ancestor bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_bank_id_terms = property(fget=get_ancestor_bank_id_terms)

    @abc.abstractmethod
    def get_ancestor_bank_terms(self):
        """Gets the ancestor bank query terms.

        :return: the ancestor bank terms
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    ancestor_bank_terms = property(fget=get_ancestor_bank_terms)

    @abc.abstractmethod
    def get_descendant_bank_id_terms(self):
        """Gets the descendant bank ``Id`` query terms.

        :return: the descendant bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_bank_id_terms = property(fget=get_descendant_bank_id_terms)

    @abc.abstractmethod
    def get_descendant_bank_terms(self):
        """Gets the descendant bank query terms.

        :return: the descendant bank terms
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    descendant_bank_terms = property(fget=get_descendant_bank_terms)

    @abc.abstractmethod
    def get_bank_query_inspector_record(self, bank_record_type):
        """Gets the bank query inspector record corresponding to the given ``Bank`` record ``Type``.

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the bank query inspector record
        :rtype: ``osid.assessment.records.BankQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankQueryInspectorRecord
