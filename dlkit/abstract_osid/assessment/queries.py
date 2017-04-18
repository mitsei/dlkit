"""Implementations of assessment abstract base class queries."""
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


class QuestionQuery:
    """This is the query for searching questions.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_question_query_record(self, question_record_type):
        """Gets the question record query corresponding to the given ``Item`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param question_record_type: a question record type
        :type question_record_type: ``osid.type.Type``
        :return: the question query record
        :rtype: ``osid.assessment.records.QuestionQueryRecord``
        :raise: ``NullArgument`` -- ``question_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(question_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.QuestionQueryRecord


class AnswerQuery:
    """This is the query for searching answers.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_answer_query_record(self, answer_record_type):
        """Gets the answer record query corresponding to the given ``Answer`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param answer_record_type: an answer record type
        :type answer_record_type: ``osid.type.Type``
        :return: the answer query record
        :rtype: ``osid.assessment.records.AnswerQueryRecord``
        :raise: ``NullArgument`` -- ``answer_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(answer_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AnswerQueryRecord


class ItemQuery:
    """This is the query for searching items.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_learning_objective_id(self, objective_id, match):
        """Sets the learning objective ``Id`` for this query.

        :param objective_id: a learning objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_learning_objective_id_terms(self):
        """Clears all learning objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    learning_objective_id_terms = property(fdel=clear_learning_objective_id_terms)

    @abc.abstractmethod
    def supports_learning_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available.

        :return: ``true`` if a learning objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_learning_objective_query(self):
        """Gets the query for a learning objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the learning objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_learning_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    learning_objective_query = property(fget=get_learning_objective_query)

    @abc.abstractmethod
    def match_any_learning_objective(self, match):
        """Matches an item with any objective.

        :param match: ``true`` to match items with any learning objective, ``false`` to match items with no learning objectives
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_learning_objective_terms(self):
        """Clears all learning objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    learning_objective_terms = property(fdel=clear_learning_objective_terms)

    @abc.abstractmethod
    def match_question_id(self, question_id, match):
        """Sets the question ``Id`` for this query.

        :param question_id: a question ``Id``
        :type question_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``question_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_question_id_terms(self):
        """Clears all question ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    question_id_terms = property(fdel=clear_question_id_terms)

    @abc.abstractmethod
    def supports_question_query(self):
        """Tests if a ``QuestionQuery`` is available.

        :return: ``true`` if a question query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_question_query(self):
        """Gets the query for a question.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the question query
        :rtype: ``osid.assessment.QuestionQuery``
        :raise: ``Unimplemented`` -- ``supports_question_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_objective_query()`` is ``true``.*

        """
        return  # osid.assessment.QuestionQuery

    question_query = property(fget=get_question_query)

    @abc.abstractmethod
    def match_any_question(self, match):
        """Matches an item with any question.

        :param match: ``true`` to match items with any question, ``false`` to match items with no questions
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_question_terms(self):
        """Clears all question terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    question_terms = property(fdel=clear_question_terms)

    @abc.abstractmethod
    def match_answer_id(self, answer_id, match):
        """Sets the answer ``Id`` for this query.

        :param answer_id: an answer ``Id``
        :type answer_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_answer_id_terms(self):
        """Clears all answer ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    answer_id_terms = property(fdel=clear_answer_id_terms)

    @abc.abstractmethod
    def supports_answer_query(self):
        """Tests if an ``AnswerQuery`` is available.

        :return: ``true`` if an answer query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_answer_query(self):
        """Gets the query for an answer.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the answer query
        :rtype: ``osid.assessment.AnswerQuery``
        :raise: ``Unimplemented`` -- ``supports_answer_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_objective_query()`` is ``true``.*

        """
        return  # osid.assessment.AnswerQuery

    answer_query = property(fget=get_answer_query)

    @abc.abstractmethod
    def match_any_answer(self, match):
        """Matches an item with any answer.

        :param match: ``true`` to match items with any answer, ``false`` to match items with no answers
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_answer_terms(self):
        """Clears all answer terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    answer_terms = property(fdel=clear_answer_terms)

    @abc.abstractmethod
    def match_assessment_id(self, assessment_id, match):
        """Sets the assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_id_terms(self):
        """Clears all assessment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_id_terms = property(fdel=clear_assessment_id_terms)

    @abc.abstractmethod
    def supports_assessment_query(self):
        """Tests if an ``AssessmentQuery`` is available.

        :return: ``true`` if an assessment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets the query for an assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def match_any_assessment(self, match):
        """Matches an item with any assessment.

        :param match: ``true`` to match items with any assessment, ``false`` to match items with no assessments
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_terms(self):
        """Clears all assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_terms = property(fdel=clear_assessment_terms)

    @abc.abstractmethod
    def match_bank_id(self, bank_id, match):
        """Sets the bank ``Id`` for this query.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bank_id_terms(self):
        """Clears all bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    @abc.abstractmethod
    def supports_bank_query(self):
        """Tests if a ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_query()`` is ``true``.*

        """
        return  # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    @abc.abstractmethod
    def clear_bank_terms(self):
        """Clears all bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_terms = property(fdel=clear_bank_terms)

    @abc.abstractmethod
    def get_item_query_record(self, item_record_type):
        """Gets the item record query corresponding to the given ``Item`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param item_record_type: an item record type
        :type item_record_type: ``osid.type.Type``
        :return: the item query record
        :rtype: ``osid.assessment.records.ItemQueryRecord``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemQueryRecord


class AssessmentQuery:
    """This is the query for searching assessments.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_level_id(self, grade_id, match):
        """Sets the level grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level_id_terms(self):
        """Clears all level ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level_id_terms = property(fdel=clear_level_id_terms)

    @abc.abstractmethod
    def supports_level_query(self):
        """Tests if a ``GradeQuery`` is available.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_level_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_level_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_level_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    level_query = property(fget=get_level_query)

    @abc.abstractmethod
    def match_any_level(self, match):
        """Matches an assessment that has any level assigned.

        :param match: ``true`` to match assessments with any level, ``false`` to match assessments with no level
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level_terms(self):
        """Clears all level terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level_terms = property(fdel=clear_level_terms)

    @abc.abstractmethod
    def match_rubric_id(self, assessment_id, match):
        """Sets the rubric assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric_id_terms(self):
        """Clears all rubric assessment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric_id_terms = property(fdel=clear_rubric_id_terms)

    @abc.abstractmethod
    def supports_rubric_query(self):
        """Tests if an ``AssessmentQuery`` is available.

        :return: ``true`` if a rubric assessment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_query(self):
        """Gets the query for a rubric assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_rubric_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rubric_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuery

    rubric_query = property(fget=get_rubric_query)

    @abc.abstractmethod
    def match_any_rubric(self, match):
        """Matches an assessment that has any rubric assessment assigned.

        :param match: ``true`` to match assessments with any rubric, ``false`` to match assessments with no rubric
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric_terms(self):
        """Clears all rubric assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric_terms = property(fdel=clear_rubric_terms)

    @abc.abstractmethod
    def match_item_id(self, item_id, match):
        """Sets the item ``Id`` for this query.

        :param item_id: an item ``Id``
        :type item_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``item_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_item_id_terms(self):
        """Clears all item ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    item_id_terms = property(fdel=clear_item_id_terms)

    @abc.abstractmethod
    def supports_item_query(self):
        """Tests if an ``ItemQuery`` is available.

        :return: ``true`` if an item query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_query(self):
        """Gets the query for an item.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the item query
        :rtype: ``osid.assessment.ItemQuery``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_query()`` is ``true``.*

        """
        return  # osid.assessment.ItemQuery

    item_query = property(fget=get_item_query)

    @abc.abstractmethod
    def match_any_item(self, match):
        """Matches an assessment that has any item.

        :param match: ``true`` to match assessments with any item, ``false`` to match assessments with no items
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_item_terms(self):
        """Clears all item terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    item_terms = property(fdel=clear_item_terms)

    @abc.abstractmethod
    def match_assessment_offered_id(self, assessment_offered_id, match):
        """Sets the assessment offered ``Id`` for this query.

        :param assessment_offered_id: an assessment offered ``Id``
        :type assessment_offered_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_offered_id_terms(self):
        """Clears all assessment offered ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_offered_id_terms = property(fdel=clear_assessment_offered_id_terms)

    @abc.abstractmethod
    def supports_assessment_offered_query(self):
        """Tests if an ``AssessmentOfferedQuery`` is available.

        :return: ``true`` if an assessment offered query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_query(self):
        """Gets the query for an assessment offered.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuery

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @abc.abstractmethod
    def match_any_assessment_offered(self, match):
        """Matches an assessment that has any offering.

        :param match: ``true`` to match assessments with any offering, ``false`` to match assessments with no offerings
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_offered_terms(self):
        """Clears all assessment offered terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_offered_terms = property(fdel=clear_assessment_offered_terms)

    @abc.abstractmethod
    def match_assessment_taken_id(self, assessment_taken_id, match):
        """Sets the assessment taken ``Id`` for this query.

        :param assessment_taken_id: an assessment taken ``Id``
        :type assessment_taken_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_taken_id_terms(self):
        """Clears all assessment taken ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_taken_id_terms = property(fdel=clear_assessment_taken_id_terms)

    @abc.abstractmethod
    def supports_assessment_taken_query(self):
        """Tests if an ``AssessmentTakenQuery`` is available.

        :return: ``true`` if an assessment taken query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_query(self):
        """Gets the query for an assessment taken.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuery

    assessment_taken_query = property(fget=get_assessment_taken_query)

    @abc.abstractmethod
    def match_any_assessment_taken(self, match):
        """Matches an assessment that has any taken version.

        :param match: ``true`` to match assessments with any taken assessments, ``false`` to match assessments with no taken assessments
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_taken_terms(self):
        """Clears all assessment taken terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_taken_terms = property(fdel=clear_assessment_taken_terms)

    @abc.abstractmethod
    def match_bank_id(self, bank_id, match):
        """Sets the bank ``Id`` for this query.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bank_id_terms(self):
        """Clears all bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    @abc.abstractmethod
    def supports_bank_query(self):
        """Tests if a ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_query()`` is ``true``.*

        """
        return  # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    @abc.abstractmethod
    def clear_bank_terms(self):
        """Clears all bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_terms = property(fdel=clear_bank_terms)

    @abc.abstractmethod
    def get_assessment_query_record(self, assessment_record_type):
        """Gets the assessment query record corresponding to the given ``Assessment`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param assessment_record_type: an assessment record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the assessment query record
        :rtype: ``osid.assessment.records.AssessmentQueryRecord``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentQueryRecord


class AssessmentOfferedQuery:
    """This is the query for searching assessments.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_assessment_id(self, assessment_id, match):
        """Sets the assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_id_terms(self):
        """Clears all assessment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_id_terms = property(fdel=clear_assessment_id_terms)

    @abc.abstractmethod
    def supports_assessment_query(self):
        """Tests if an ``AssessmentQuery`` is available.

        :return: ``true`` if an assessment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets the query for an assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def clear_assessment_terms(self):
        """Clears all assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_terms = property(fdel=clear_assessment_terms)

    @abc.abstractmethod
    def match_level_id(self, grade_id, match):
        """Sets the level grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level_id_terms(self):
        """Clears all level ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level_id_terms = property(fdel=clear_level_id_terms)

    @abc.abstractmethod
    def supports_level_query(self):
        """Tests if a ``GradeQuery`` is available.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_level_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_level_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_level_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    level_query = property(fget=get_level_query)

    @abc.abstractmethod
    def match_any_level(self, match):
        """Matches an assessment offered that has any level assigned.

        :param match: ``true`` to match offerings with any level, ``false`` to match offerings with no levsls
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level_terms(self):
        """Clears all level terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level_terms = property(fdel=clear_level_terms)

    @abc.abstractmethod
    def match_items_sequential(self, match):
        """Match sequential assessments.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_items_sequential_terms(self):
        """Clears all sequential terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    items_sequential_terms = property(fdel=clear_items_sequential_terms)

    @abc.abstractmethod
    def match_items_shuffled(self, match):
        """Match shuffled item assessments.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_items_shuffled_terms(self):
        """Clears all shuffled terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    items_shuffled_terms = property(fdel=clear_items_shuffled_terms)

    @abc.abstractmethod
    def match_start_time(self, start, end, match):
        """Matches assessments whose start time falls between the specified range inclusive.

        :param start: start of range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_start_time(self, match):
        """Matches offerings that has any start time assigned.

        :param match: ``true`` to match offerings with any start time, ``false`` to match offerings with no start time
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_start_time_terms(self):
        """Clears all scheduled terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_time_terms = property(fdel=clear_start_time_terms)

    @abc.abstractmethod
    def match_deadline(self, start, end, match):
        """Matches assessments whose end time falls between the specified range inclusive.

        :param start: start of range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_deadline(self, match):
        """Matches offerings that have any deadline assigned.

        :param match: ``true`` to match offerings with any deadline, ``false`` to match offerings with no deadline
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_deadline_terms(self):
        """Clears all deadline terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    deadline_terms = property(fdel=clear_deadline_terms)

    @abc.abstractmethod
    def match_duration(self, low, high, match):
        """Matches assessments whose duration falls between the specified range inclusive.

        :param low: start range of duration
        :type low: ``osid.calendaring.Duration``
        :param high: end range of duration
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_duration(self, match):
        """Matches offerings that have any duration assigned.

        :param match: ``true`` to match offerings with any duration, ``false`` to match offerings with no duration
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_duration_terms(self):
        """Clears all duration terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    duration_terms = property(fdel=clear_duration_terms)

    @abc.abstractmethod
    def match_score_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true for a positive match, false for a negative match``
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_system_id_terms(self):
        """Clears all grade system ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_system_id_terms = property(fdel=clear_score_system_id_terms)

    @abc.abstractmethod
    def supports_score_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_score_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_score_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_score_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuery

    score_system_query = property(fget=get_score_system_query)

    @abc.abstractmethod
    def match_any_score_system(self, match):
        """Matches taken assessments that have any grade system assigned.

        :param match: ``true`` to match assessments with any grade system, ``false`` to match assessments with no grade system
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_system_terms(self):
        """Clears all grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_system_terms = property(fdel=clear_score_system_terms)

    @abc.abstractmethod
    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true for a positive match, false for a negative match``
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_id_terms(self):
        """Clears all grade system ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)

    @abc.abstractmethod
    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_score_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_score_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    @abc.abstractmethod
    def match_any_grade_system(self, match):
        """Matches taken assessments that have any grade system assigned.

        :param match: ``true`` to match assessments with any grade system, ``false`` to match assessments with no grade system
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_terms(self):
        """Clears all grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)

    @abc.abstractmethod
    def match_rubric_id(self, assessment_offered_id, match):
        """Sets the rubric assessment offered ``Id`` for this query.

        :param assessment_offered_id: an assessment offered ``Id``
        :type assessment_offered_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric_id_terms(self):
        """Clears all rubric assessment offered ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric_id_terms = property(fdel=clear_rubric_id_terms)

    @abc.abstractmethod
    def supports_rubric_query(self):
        """Tests if an ``AssessmentOfferedQuery`` is available.

        :return: ``true`` if a rubric assessment offered query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_query(self):
        """Gets the query for a rubric assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``Unimplemented`` -- ``supports_rubric_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rubric_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuery

    rubric_query = property(fget=get_rubric_query)

    @abc.abstractmethod
    def match_any_rubric(self, match):
        """Matches an assessment offered that has any rubric assessment assigned.

        :param match: ``true`` to match assessments offered with any rubric, ``false`` to match assessments offered with no rubric
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric_terms(self):
        """Clears all rubric assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric_terms = property(fdel=clear_rubric_terms)

    @abc.abstractmethod
    def match_assessment_taken_id(self, assessment_taken_id, match):
        """Sets the assessment taken ``Id`` for this query.

        :param assessment_taken_id: an assessment taken ``Id``
        :type assessment_taken_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_taken_id_terms(self):
        """Clears all assessment taken ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_taken_id_terms = property(fdel=clear_assessment_taken_id_terms)

    @abc.abstractmethod
    def supports_assessment_taken_query(self):
        """Tests if an ``AssessmentTakenQuery`` is available.

        :return: ``true`` if an assessment taken query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_query(self):
        """Gets the query for an assessment taken.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_taken_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuery

    assessment_taken_query = property(fget=get_assessment_taken_query)

    @abc.abstractmethod
    def match_any_assessment_taken(self, match):
        """Matches offerings that have any taken assessment version.

        :param match: ``true`` to match offerings with any taken assessment, ``false`` to match offerings with no assessmen taken
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_taken_terms(self):
        """Clears all assessment taken terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_taken_terms = property(fdel=clear_assessment_taken_terms)

    @abc.abstractmethod
    def match_bank_id(self, bank_id, match):
        """Sets the bank ``Id`` for this query.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bank_id_terms(self):
        """Clears all bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    @abc.abstractmethod
    def supports_bank_query(self):
        """Tests if a ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_query()`` is ``true``.*

        """
        return  # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    @abc.abstractmethod
    def clear_bank_terms(self):
        """Clears all bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_terms = property(fdel=clear_bank_terms)

    @abc.abstractmethod
    def get_assessment_offered_query_record(self, assessment_offered_record_type):
        """Gets the assessment offered query record corresponding to the given ``AssessmentOffered`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param assessment_offered_record_type: an assessment offered record type
        :type assessment_offered_record_type: ``osid.type.Type``
        :return: the assessment offered query record
        :rtype: ``osid.assessment.records.AssessmentOfferedQueryRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedQueryRecord


class AssessmentTakenQuery:
    """This is the query for searching assessments.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_assessment_offered_id(self, assessment_offered_id, match):
        """Sets the assessment offered ``Id`` for this query.

        :param assessment_offered_id: an assessment ``Id``
        :type assessment_offered_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_offered_id_terms(self):
        """Clears all assessment offered ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_offered_id_terms = property(fdel=clear_assessment_offered_id_terms)

    @abc.abstractmethod
    def supports_assessment_offered_query(self):
        """Tests if an ``AssessmentOfferedQuery`` is available.

        :return: ``true`` if an assessment offered query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_query(self):
        """Gets the query for an assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuery

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @abc.abstractmethod
    def clear_assessment_offered_terms(self):
        """Clears all assessment offered terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_offered_terms = property(fdel=clear_assessment_offered_terms)

    @abc.abstractmethod
    def match_taker_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_taker_id_terms(self):
        """Clears all resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    taker_id_terms = property(fdel=clear_taker_id_terms)

    @abc.abstractmethod
    def supports_taker_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_taker_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_taker_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_taker_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    taker_query = property(fget=get_taker_query)

    @abc.abstractmethod
    def clear_taker_terms(self):
        """Clears all resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    taker_terms = property(fdel=clear_taker_terms)

    @abc.abstractmethod
    def match_taking_agent_id(self, agent_id, match):
        """Sets the agent ``Id`` for this query.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_taking_agent_id_terms(self):
        """Clears all agent ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    taking_agent_id_terms = property(fdel=clear_taking_agent_id_terms)

    @abc.abstractmethod
    def supports_taking_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_taking_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_taking_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_taking_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    taking_agent_query = property(fget=get_taking_agent_query)

    @abc.abstractmethod
    def clear_taking_agent_terms(self):
        """Clears all taking agent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    taking_agent_terms = property(fdel=clear_taking_agent_terms)

    @abc.abstractmethod
    def match_actual_start_time(self, start, end, match):
        """Matches assessments whose start time falls between the specified range inclusive.

        :param start: start of range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_actual_start_time(self, match):
        """Matches taken assessments taken that have begun.

        :param match: ``true`` to match assessments taken started, ``false`` to match assessments taken that have not begun
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_actual_start_time_terms(self):
        """Clears all start time terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    actual_start_time_terms = property(fdel=clear_actual_start_time_terms)

    @abc.abstractmethod
    def match_completion_time(self, start, end, match):
        """Matches assessments whose completion time falls between the specified range inclusive.

        :param start: start of range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_completion_time(self, match):
        """Matches taken assessments taken that have completed.

        :param match: ``true`` to match assessments taken completed, ``false`` to match assessments taken that are incomplete
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_completion_time_terms(self):
        """Clears all in completion time terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    completion_time_terms = property(fdel=clear_completion_time_terms)

    @abc.abstractmethod
    def match_time_spent(self, low, high, match):
        """Matches assessments where the time spent falls between the specified range inclusive.

        :param low: start of duration range
        :type low: ``osid.calendaring.Duration``
        :param high: end of duration range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_time_spent_terms(self):
        """Clears all in time spent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_spent_terms = property(fdel=clear_time_spent_terms)

    @abc.abstractmethod
    def match_score_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true for a positive match, false for a negative match``
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_system_id_terms(self):
        """Clears all grade system ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_system_id_terms = property(fdel=clear_score_system_id_terms)

    @abc.abstractmethod
    def supports_score_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_score_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_score_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_score_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuery

    score_system_query = property(fget=get_score_system_query)

    @abc.abstractmethod
    def match_any_score_system(self, match):
        """Matches taken assessments that have any grade system assigned.

        :param match: ``true`` to match assessments with any grade system, ``false`` to match assessments with no grade system
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_system_terms(self):
        """Clears all grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_system_terms = property(fdel=clear_score_system_terms)

    @abc.abstractmethod
    def match_score(self, low, high, match):
        """Matches assessments whose score falls between the specified range inclusive.

        :param low: start of range
        :type low: ``decimal``
        :param high: end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_score(self, match):
        """Matches taken assessments that have any score assigned.

        :param match: ``true`` to match assessments with any score, ``false`` to match assessments with no score
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_terms(self):
        """Clears all score terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_terms = property(fdel=clear_score_terms)

    @abc.abstractmethod
    def match_grade_id(self, grade_id, match):
        """Sets the grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true for a positive match, false for a negative match``
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_id_terms(self):
        """Clears all grade ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_id_terms = property(fdel=clear_grade_id_terms)

    @abc.abstractmethod
    def supports_grade_query(self):
        """Tests if a ``GradeQuery`` is available.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    grade_query = property(fget=get_grade_query)

    @abc.abstractmethod
    def match_any_grade(self, match):
        """Matches taken assessments that have any grade assigned.

        :param match: ``true`` to match assessments with any grade, ``false`` to match assessments with no grade
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_terms(self):
        """Clears all grade terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_terms = property(fdel=clear_grade_terms)

    @abc.abstractmethod
    def match_feedback(self, comments, string_match_type, match):
        """Sets the comment string for this query.

        :param comments: comment string
        :type comments: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``comments is`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``comments`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_feedback(self, match):
        """Matches taken assessments that have any comments.

        :param match: ``true`` to match assessments with any comments, ``false`` to match assessments with no comments
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_feedback_terms(self):
        """Clears all comment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    feedback_terms = property(fdel=clear_feedback_terms)

    @abc.abstractmethod
    def match_rubric_id(self, assessment_taken_id, match):
        """Sets the rubric assessment taken ``Id`` for this query.

        :param assessment_taken_id: an assessment taken ``Id``
        :type assessment_taken_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric_id_terms(self):
        """Clears all rubric assessment taken ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric_id_terms = property(fdel=clear_rubric_id_terms)

    @abc.abstractmethod
    def supports_rubric_query(self):
        """Tests if an ``AssessmentTakenQuery`` is available.

        :return: ``true`` if a rubric assessment taken query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_query(self):
        """Gets the query for a rubric assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``Unimplemented`` -- ``supports_rubric_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rubric_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentTakenQuery

    rubric_query = property(fget=get_rubric_query)

    @abc.abstractmethod
    def match_any_rubric(self, match):
        """Matches an assessment taken that has any rubric assessment assigned.

        :param match: ``true`` to match assessments taken with any rubric, ``false`` to match assessments taken with no rubric
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric_terms(self):
        """Clears all rubric assessment taken terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric_terms = property(fdel=clear_rubric_terms)

    @abc.abstractmethod
    def match_bank_id(self, bank_id, match):
        """Sets the bank ``Id`` for this query.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bank_id_terms(self):
        """Clears all bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    @abc.abstractmethod
    def supports_bank_query(self):
        """Tests if a ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bank_query()`` is ``true``.*

        """
        return  # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    @abc.abstractmethod
    def clear_bank_terms(self):
        """Clears all bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bank_terms = property(fdel=clear_bank_terms)

    @abc.abstractmethod
    def get_assessment_taken_query_record(self, assessment_taken_record_type):
        """Gets the assessment taken query record corresponding to the given ``AssessmentTaken`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param assessment_taken_record_type: an assessment taken record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the assessment taken query record
        :rtype: ``osid.assessment.records.AssessmentTakenQueryRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenQueryRecord


class BankQuery:
    """This is the query for searching banks Each method specifies an ``AND`` term while multiple invocations of the same method produce a nested ``OR``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_item_id(self, item_id, match):
        """Sets the item ``Id`` for this query.

        :param item_id: an item ``Id``
        :type item_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``item_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_item_id_terms(self):
        """Clears all item ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    item_id_terms = property(fdel=clear_item_id_terms)

    @abc.abstractmethod
    def supports_item_query(self):
        """Tests if a ``ItemQuery`` is available.

        :return: ``true`` if an item query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_query(self):
        """Gets the query for an item.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the item query
        :rtype: ``osid.assessment.ItemQuery``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_item_query()`` is ``true``.*

        """
        return  # osid.assessment.ItemQuery

    item_query = property(fget=get_item_query)

    @abc.abstractmethod
    def match_any_item(self, match):
        """Matches assessment banks that have any item assigned.

        :param match: ``true`` to match banks with any item, ``false`` to match assessments with no item
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_item_terms(self):
        """Clears all item terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    item_terms = property(fdel=clear_item_terms)

    @abc.abstractmethod
    def match_assessment_id(self, assessment_id, match):
        """Sets the assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_id_terms(self):
        """Clears all assessment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_id_terms = property(fdel=clear_assessment_id_terms)

    @abc.abstractmethod
    def supports_assessment_query(self):
        """Tests if an ``AssessmentQuery`` is available.

        :return: ``true`` if an assessment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets the query for an assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def match_any_assessment(self, match):
        """Matches assessment banks that have any assessment assigned.

        :param match: ``true`` to match banks with any assessment, ``false`` to match banks with no assessment
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_terms(self):
        """Clears all assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_terms = property(fdel=clear_assessment_terms)

    @abc.abstractmethod
    def match_assessment_offered_id(self, assessment_offered_id, match):
        """Sets the assessment offered ``Id`` for this query.

        :param assessment_offered_id: an assessment ``Id``
        :type assessment_offered_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_offered_id_terms(self):
        """Clears all assessment offered ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_offered_id_terms = property(fdel=clear_assessment_offered_id_terms)

    @abc.abstractmethod
    def supports_assessment_offered_query(self):
        """Tests if an ``AssessmentOfferedQuery`` is available.

        :return: ``true`` if an assessment offered query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_query(self):
        """Gets the query for an assessment offered.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_offered_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentOfferedQuery

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @abc.abstractmethod
    def match_any_assessment_offered(self, match):
        """Matches assessment banks that have any assessment offering assigned.

        :param match: ``true`` to match banks with any assessment offering, ``false`` to match banks with no offering
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_offered_terms(self):
        """Clears all assessment offered terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_offered_terms = property(fdel=clear_assessment_offered_terms)

    @abc.abstractmethod
    def match_ancestor_bank_id(self, bank_id, match):
        """Sets the bank ``Id`` for to match banks in which the specified bank is an acestor.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_bank_id_terms(self):
        """Clears all ancestor bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_bank_id_terms = property(fdel=clear_ancestor_bank_id_terms)

    @abc.abstractmethod
    def supports_ancestor_bank_query(self):
        """Tests if a ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_bank_query(self):
        """Gets the query for an ancestor bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_bank_query()`` is ``true``.*

        """
        return  # osid.assessment.BankQuery

    ancestor_bank_query = property(fget=get_ancestor_bank_query)

    @abc.abstractmethod
    def match_any_ancestor_bank(self, match):
        """Matches a bank that has any ancestor.

        :param match: ``true`` to match banks with any ancestor banks, ``false`` to match root banks
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_bank_terms(self):
        """Clears all ancestor bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_bank_terms = property(fdel=clear_ancestor_bank_terms)

    @abc.abstractmethod
    def match_descendant_bank_id(self, bank_id, match):
        """Sets the bank ``Id`` for to match banks in which the specified bank is a descendant.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_bank_id_terms(self):
        """Clears all descendant bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_bank_id_terms = property(fdel=clear_descendant_bank_id_terms)

    @abc.abstractmethod
    def supports_descendant_bank_query(self):
        """Tests if a ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_bank_query(self):
        """Gets the query for a descendant bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_bank_query()`` is ``true``.*

        """
        return  # osid.assessment.BankQuery

    descendant_bank_query = property(fget=get_descendant_bank_query)

    @abc.abstractmethod
    def match_any_descendant_bank(self, match):
        """Matches a bank that has any descendant.

        :param match: ``true`` to match banks with any descendant banks, ``false`` to match leaf banks
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_bank_terms(self):
        """Clears all descendant bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_bank_terms = property(fdel=clear_descendant_bank_terms)

    @abc.abstractmethod
    def get_bank_query_record(self, bank_record_type):
        """Gets the bank query record corresponding to the given ``Bank`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the bank query record
        :rtype: ``osid.assessment.records.BankQueryRecord``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankQueryRecord
