"""Implementations of assessment abstract base class search_orders."""
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


class QuestionSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_question_search_order_record(self, question_record_type):
        """Gets the question search order record corresponding to the given question record ``Type``.

        Multiple retrievals return the same underlying object.

        :param question_record_type: a question record type
        :type question_record_type: ``osid.type.Type``
        :return: the question search order record
        :rtype: ``osid.assessment.records.QuestionSearchOrderRecord``
        :raise: ``NullArgument`` -- ``question_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(question_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.QuestionSearchOrderRecord


class AnswerSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_answer_search_order_record(self, answer_record_type):
        """Gets the answer search order record corresponding to the given answer record ``Type``.

        Multiple retrievals return the same underlying object.

        :param answer_record_type: an answer record type
        :type answer_record_type: ``osid.type.Type``
        :return: the answer search order record
        :rtype: ``osid.assessment.records.AnswerSearchOrderRecord``
        :raise: ``NullArgument`` -- ``answer_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(answer_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AnswerSearchOrderRecord


class ItemSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_question(self, style):
        """Specifies a preference for ordering the result set by the question.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_question_search_order(self):
        """Tests if a question search order is available.

        :return: ``true`` if a question search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_question_search_order(self):
        """Gets a question search order.

        :return: a question search order
        :rtype: ``osid.assessment.QuestionSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_question_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_question_search_order()`` is ``true``.*

        """
        return  # osid.assessment.QuestionSearchOrder

    question_search_order = property(fget=get_question_search_order)

    @abc.abstractmethod
    def get_item_search_order_record(self, item_record_type):
        """Gets the item search order record corresponding to the given item record ``Type``.

        Multiple retrievals return the same underlying object.

        :param item_record_type: an item record type
        :type item_record_type: ``osid.type.Type``
        :return: the item search order record
        :rtype: ``osid.assessment.records.ItemSearchOrderRecord``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemSearchOrderRecord


class AssessmentSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_level(self, style):
        """Specifies a preference for ordering the result set by the level of difficulty.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_level_search_order(self):
        """Tests if a grade search order is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_level_search_order(self):
        """Gets a grade search order.

        :return: a grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_level_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_level_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSearchOrder

    level_search_order = property(fget=get_level_search_order)

    @abc.abstractmethod
    def order_by_rubric(self, style):
        """Specifies a preference for ordering the result set by the rubric assessment.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_rubric_search_order(self):
        """Tests if an assessment search order is available.

        :return: ``true`` if an assessment search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_search_order(self):
        """Gets an assessment search order.

        :return: a rubric assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_rubric_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rubric_search_order()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSearchOrder

    rubric_search_order = property(fget=get_rubric_search_order)

    @abc.abstractmethod
    def get_assessment_search_order_record(self, assessment_record_type):
        """Gets the assessment search order record corresponding to the given assessment record ``Type``.

        Multiple retrievals return the same underlying object.

        :param assessment_record_type: an assessment record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the assessment search order record
        :rtype: ``osid.assessment.records.AssessmentSearchOrderRecord``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentSearchOrderRecord


class AssessmentOfferedSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_assessment(self, style):
        """Specifies a preference for ordering the result set by the assessment.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_assessment_search_order(self):
        """Tests if an assessment search order is available.

        :return: ``true`` if an assessment search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_search_order(self):
        """Gets an assessment search order.

        :return: an assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_assessment_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search_order()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentSearchOrder

    assessment_search_order = property(fget=get_assessment_search_order)

    @abc.abstractmethod
    def order_by_level(self, style):
        """Specifies a preference for ordering the result set by the level of difficulty.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_level_search_order(self):
        """Tests if a grade search order is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_level_search_order(self):
        """Gets a grade search order.

        :return: a grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_level_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_level_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSearchOrder

    level_search_order = property(fget=get_level_search_order)

    @abc.abstractmethod
    def order_by_items_sequential(self, style):
        """Specifies a preference for ordering the result set by the sequential flag.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_items_shuffled(self, style):
        """Specifies a preference for ordering the result set by the shuffle flag.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_start_time(self, style):
        """Specifies a preference for ordering the result set by the assessment start time.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_deadline(self, style):
        """Specifies a preference for ordering the result set by the assessment deadline.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_duration(self, style):
        """Specifies a preference for ordering the result set by the duration.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_score_system(self, style):
        """Specifies a preference for ordering the result set by the grade system for scores.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_score_system_search_order(self):
        """Tests if a grade system search order is available.

        :return: ``true`` if a grade system search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_score_system_search_order(self):
        """Gets a grade system search order.

        :return: a grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_score_system_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_score_system_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchOrder

    score_system_search_order = property(fget=get_score_system_search_order)

    @abc.abstractmethod
    def order_by_grade_system(self, style):
        """Specifies a preference for ordering the result set by the grade system for grades.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grade_system_search_order(self):
        """Tests if a grade system search order is available.

        :return: ``true`` if a grade system search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_search_order(self):
        """Gets a grade system search order.

        :return: a grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchOrder

    grade_system_search_order = property(fget=get_grade_system_search_order)

    @abc.abstractmethod
    def order_by_rubric(self, style):
        """Specifies a preference for ordering the result set by the rubric assessment offered.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_rubric_search_order(self):
        """Tests if an assessment offered search order is available.

        :return: ``true`` if an assessment offered search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_search_order(self):
        """Gets an assessment offered search order.

        :return: a rubric assessment offered search order
        :rtype: ``osid.assessment.AssessmentOfferedSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_rubric_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rubric_search_order()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSearchOrder

    rubric_search_order = property(fget=get_rubric_search_order)

    @abc.abstractmethod
    def get_assessment_offered_search_order_record(self, assessment_offered_record_type):
        """Gets the assessment offered search order record corresponding to the given assessment record ``Type``.

        Multiple retrievals return the same underlying object.

        :param assessment_offered_record_type: an assessment offered record type
        :type assessment_offered_record_type: ``osid.type.Type``
        :return: the assessment offered search order record
        :rtype: ``osid.assessment.records.AssessmentOfferedSearchOrderRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedSearchOrderRecord


class AssessmentTakenSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_assessment_offered(self, style):
        """Specifies a preference for ordering the result set by the assessment offered.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_assessment_offered_search_order(self):
        """Tests if an assessment search order is available.

        :return: ``true`` if an assessment offered search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_search_order(self):
        """Gets an assessment offered search order.

        :return: an assessment offered search order
        :rtype: ``osid.assessment.AssessmentOfferedSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_search_order()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedSearchOrder

    assessment_offered_search_order = property(fget=get_assessment_offered_search_order)

    @abc.abstractmethod
    def order_by_taker(self, style):
        """Specifies a preference for ordering the result set by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_taker_search_order(self):
        """Tests if a resource search order is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_taker_search_order(self):
        """Gets a resource search order.

        :return: a resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_taker_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_taker_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    taker_search_order = property(fget=get_taker_search_order)

    @abc.abstractmethod
    def order_by_taking_agent(self, style):
        """Specifies a preference for ordering the result set by the agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_taking_agent_search_order(self):
        """Tests if an agent search order is available.

        :return: ``true`` if an agent search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_taking_agent_search_order(self):
        """Gets an agent search order.

        :return: an agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_taking_agent_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_taking_agent_search_order()`` is ``true``.*

        """
        return  # osid.authentication.AgentSearchOrder

    taking_agent_search_order = property(fget=get_taking_agent_search_order)

    @abc.abstractmethod
    def order_by_actual_start_time(self, style):
        """Specifies a preference for ordering the result set by the assessment start time.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_completion_time(self, style):
        """Specifies a preference for ordering the result set by the assessment deadline.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_time_spent(self, style):
        """Specifies a preference for ordering the result set by the time spent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_score_system(self, style):
        """Specifies a preference for ordering the result set by the grade system.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_score_system_search_order(self):
        """Tests if a grade system search order is available.

        :return: ``true`` if a grade system search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_score_system_search_order(self):
        """Gets a grade system search order.

        :return: a grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_score_system_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_score_system_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchOrder

    score_system_search_order = property(fget=get_score_system_search_order)

    @abc.abstractmethod
    def order_by_score(self, style):
        """Specifies a preference for ordering the result set by the score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_grade(self, style):
        """Specifies a preference for ordering the result set by the grade.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grade_search_order(self):
        """Tests if a grade search order is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_search_order(self):
        """Gets a grade search order.

        :return: a grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grade_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSearchOrder

    grade_search_order = property(fget=get_grade_search_order)

    @abc.abstractmethod
    def order_by_feedback(self, style):
        """Specifies a preference for ordering the result set by the comments.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_rubric(self, style):
        """Specifies a preference for ordering the result set by the rubric assessment.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_rubric_search_order(self):
        """Tests if an assessment taken search order is available.

        :return: ``true`` if an assessment taken search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_search_order(self):
        """Gets an assessment taken search order.

        :return: a rubric assessment taken search order
        :rtype: ``osid.assessment.AssessmentTakenSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_rubric_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rubric_search_order()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenSearchOrder

    rubric_search_order = property(fget=get_rubric_search_order)

    @abc.abstractmethod
    def get_assessment_taken_search_order_record(self, assessment_taken_record_type):
        """Gets the assessment taken search order record corresponding to the given assessment record ``Type``.

        Multiple retrievals return the same underlying object.

        :param assessment_taken_record_type: an assessment record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the assessment taken search order record
        :rtype: ``osid.assessment.records.AssessmentTakenSearchOrderRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenSearchOrderRecord


class BankSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_search_order_record(self, bank_record_type):
        """Gets the bank search order record corresponding to the given bank record ``Type``.

        Multiple retrievals return the same underlying object.

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the bank search order record
        :rtype: ``osid.assessment.records.BankSearchOrderRecord``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankSearchOrderRecord
