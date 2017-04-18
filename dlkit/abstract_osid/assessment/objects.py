"""Implementations of assessment abstract base class objects."""
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


class Question:
    """A ``Question`` represents the question portion of an assessment item.

    Like all OSID objects, a ``Question`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_question_record(self, question_record_type):
        """Gets the item record corresponding to the given ``Question`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``question_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(question_record_type)`` is ``true`` .

        :param question_record_type: the type of the record to retrieve
        :type question_record_type: ``osid.type.Type``
        :return: the question record
        :rtype: ``osid.assessment.records.QuestionRecord``
        :raise: ``NullArgument`` -- ``question_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(question_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.QuestionRecord


class QuestionForm:
    """This is the form for creating and updating ``Questions``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_question_form_record(self, question_record_type):
        """Gets the ``QuestionFormRecord`` corresponding to the given question record ``Type``.

        :param question_record_type: the question record type
        :type question_record_type: ``osid.type.Type``
        :return: the question record
        :rtype: ``osid.assessment.records.QuestionFormRecord``
        :raise: ``NullArgument`` -- ``question_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(question_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.QuestionFormRecord


class QuestionList:
    """Like all ``OsidLists,``  ``QuestionList`` provides a means for accessing ``Question`` elements sequentially either one at a time or many at a time.

    Examples: while (ql.hasNext()) { Question question =
    ql.getNextQuestion(); }

    or
      while (ql.hasNext()) {
           Question[] question = al.getNextQuestions(ql.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_question(self):
        """Gets the next ``Question`` in this list.

        :return: the next ``Question`` in this list. The ``has_next()`` method should be used to test that a next ``Question`` is available before calling this method.
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    next_question = property(fget=get_next_question)

    @abc.abstractmethod
    def get_next_questions(self, n):
        """Gets the next set of ``Question`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Question`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Question`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question


class Answer:
    """An ``Answer`` represents the question portion of an assessment item.

    Like all OSID objects, an ``Answer`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_answer_record(self, answer_record_type):
        """Gets the answer record corresponding to the given ``Answer`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested records. The ``answer_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(answer_record_type)`` is ``true`` .

        :param answer_record_type: the type of the record to retrieve
        :type answer_record_type: ``osid.type.Type``
        :return: the answer record
        :rtype: ``osid.assessment.records.AnswerRecord``
        :raise: ``NullArgument`` -- ``answer_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(answer_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AnswerRecord


class AnswerForm:
    """This is the form for creating and updating ``Answers``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_answer_form_record(self, answer_record_type):
        """Gets the ``AnswerFormRecord`` corresponding to the given answer record ``Type``.

        :param answer_record_type: the answer record type
        :type answer_record_type: ``osid.type.Type``
        :return: the answer record
        :rtype: ``osid.assessment.records.AnswerFormRecord``
        :raise: ``NullArgument`` -- ``answer_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(answer_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AnswerFormRecord


class AnswerList:
    """Like all ``OsidLists,``  ``AnswerList`` provides a means for accessing ``Answer`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Answer answer = al.getNextAnswer();
    }

    or
      while (al.hasNext()) {
           Answer[] answer = al.getNextAnswers(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_answer(self):
        """Gets the next ``Answer`` in this list.

        :return: the next ``Answer`` in this list. The ``has_next()`` method should be used to test that a next ``Answer`` is available before calling this method.
        :rtype: ``osid.assessment.Answer``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Answer

    next_answer = property(fget=get_next_answer)

    @abc.abstractmethod
    def get_next_answers(self, n):
        """Gets the next set of ``Answer`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Answer`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Answer`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Answer``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Answer


class Item:
    """An ``Item`` represents an individual assessment item such as a question.

    Like all OSID objects, a ``Item`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    An ``Item`` is composed of a ``Question`` and an ``Answer``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_learning_objective_ids(self):
        """Gets the ``Ids`` of any ``Objectives`` corresponding to this item.

        :return: the learning objective ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    learning_objective_ids = property(fget=get_learning_objective_ids)

    @abc.abstractmethod
    def get_learning_objectives(self):
        """Gets the any ``Objectives`` corresponding to this item.

        :return: the learning objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    learning_objectives = property(fget=get_learning_objectives)

    @abc.abstractmethod
    def get_question_id(self):
        """Gets the ``Id`` of the ``Question``.

        :return: the question ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    question_id = property(fget=get_question_id)

    @abc.abstractmethod
    def get_question(self):
        """Gets the question.

        :return: the question
        :rtype: ``osid.assessment.Question``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    question = property(fget=get_question)

    @abc.abstractmethod
    def get_answer_ids(self):
        """Gets the ``Ids`` of the answers.

        Questions may have more than one acceptable answer.

        :return: the answer ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    answer_ids = property(fget=get_answer_ids)

    @abc.abstractmethod
    def get_answers(self):
        """Gets the answers.

        :return: the answers
        :rtype: ``osid.assessment.AnswerList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AnswerList

    answers = property(fget=get_answers)

    @abc.abstractmethod
    def get_item_record(self, item_record_type):
        """Gets the item record corresponding to the given ``Item`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested records. The ``item_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(item_record_type)``
        is ``true`` .

        :param item_record_type: the type of the record to retrieve
        :type item_record_type: ``osid.type.Type``
        :return: the item record
        :rtype: ``osid.assessment.records.ItemRecord``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemRecord


class ItemForm:
    """This is the form for creating and updating ``Items``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ItemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_learning_objectives_metadata(self):
        """Gets the metadata for learning objectives.

        :return: metadata for the learning objectives
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    learning_objectives_metadata = property(fget=get_learning_objectives_metadata)

    @abc.abstractmethod
    def set_learning_objectives(self, objective_ids):
        """Sets the learning objectives.

        :param objective_ids: the learning objective ``Ids``
        :type objective_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``objective_ids`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_learning_objectives(self):
        """Clears the learning objectives.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    learning_objectives = property(fset=set_learning_objectives, fdel=clear_learning_objectives)

    @abc.abstractmethod
    def get_item_form_record(self, item_record_type):
        """Gets the ``ItemnFormRecord`` corresponding to the given item record ``Type``.

        :param item_record_type: the item record type
        :type item_record_type: ``osid.type.Type``
        :return: the item record
        :rtype: ``osid.assessment.records.ItemFormRecord``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemFormRecord


class ItemList:
    """Like all ``OsidLists,``  ``ItemList`` provides a means for accessing ``Item`` elements sequentially either one at a time or many at a time.

    Examples: while (il.hasNext()) { Item item = il.getNextItem(); }

    or
      while (il.hasNext()) {
           Item[] items = il.getNextItems(il.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_item(self):
        """Gets the next ``Item`` in this list.

        :return: the next ``Item`` in this list. The ``has_next()`` method should be used to test that a next ``Item`` is available before calling this method.
        :rtype: ``osid.assessment.Item``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Item

    next_item = property(fget=get_next_item)

    @abc.abstractmethod
    def get_next_items(self, n):
        """Gets the next set of ``Item`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Item`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Item`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Item``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Item


class Assessment:
    """An ``Assessment`` represents a sequence of assessment items.

    Like all OSID objects, an ``Assessment`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    An ``Assessment`` may have an accompanying rubric used for assessing
    performance. The rubric assessment is established canonically in
    this ``Assessment``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_level_id(self):
        """Gets the ``Id`` of a ``Grade`` corresponding to the assessment difficulty.

        :return: a grade ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    level_id = property(fget=get_level_id)

    @abc.abstractmethod
    def get_level(self):
        """Gets the ``Grade`` corresponding to the assessment difficulty.

        :return: the level
        :rtype: ``osid.grading.Grade``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    level = property(fget=get_level)

    @abc.abstractmethod
    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        :return: ``true`` if a rubric is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        :return: an assessment ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_rubric()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    rubric_id = property(fget=get_rubric_id)

    @abc.abstractmethod
    def get_rubric(self):
        """Gets the rubric.

        :return: the assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- ``has_rubric()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment

    rubric = property(fget=get_rubric)

    @abc.abstractmethod
    def get_assessment_record(self, assessment_record_type):
        """Gets the assessment record corresponding to the given ``Assessment`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_record_type)`` is ``true`` .

        :param assessment_record_type: the type of the record to retrieve
        :type assessment_record_type: ``osid.type.Type``
        :return: the assessment record
        :rtype: ``osid.assessment.records.AssessmentRecord``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentRecord


class AssessmentForm:
    """This is the form for creating and updating ``Assessments``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_level_metadata(self):
        """Gets the metadata for a grade level.

        :return: metadata for the grade level
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    level_metadata = property(fget=get_level_metadata)

    @abc.abstractmethod
    def set_level(self, grade_id):
        """Sets the level of difficulty expressed as a ``Grade``.

        :param grade_id: the grade level
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level(self):
        """Clears the grade level.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level = property(fset=set_level, fdel=clear_level)

    @abc.abstractmethod
    def get_rubric_metadata(self):
        """Gets the metadata for a rubric assessment.

        :return: metadata for the assesment
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    rubric_metadata = property(fget=get_rubric_metadata)

    @abc.abstractmethod
    def set_rubric(self, assessment_id):
        """Sets the rubric expressed as another assessment.

        :param assessment_id: the assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``assessment_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rubric(self):
        """Clears the rubric.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric = property(fset=set_rubric, fdel=clear_rubric)

    @abc.abstractmethod
    def get_assessment_form_record(self, assessment_record_type):
        """Gets the ``AssessmentFormRecord`` corresponding to the given assessment record ``Type``.

        :param assessment_record_type: the assessment record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the assessment record
        :rtype: ``osid.assessment.records.AssessmentFormRecord``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentFormRecord


class AssessmentList:
    """Like all ``OsidLists,``  ``AssessmentList`` provides a means for accessing ``Assessment`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Assessment assessment =
    al.getNextAssessment(); }

    or
      while (al.hasNext()) {
           Assessment[] assessments = al.hetNextAssessments(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_assessment(self):
        """Gets the next ``Assessment`` in this list.

        :return: the next ``Assessment`` in this list. The ``has_next()`` method should be used to test that a next ``Assessment`` is available before calling this method.
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment

    next_assessment = property(fget=get_next_assessment)

    @abc.abstractmethod
    def get_next_assessments(self, n):
        """Gets the next set of ``Assessment`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Assessment`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Assessment`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment


class AssessmentOffered:
    """An ``AssessmentOffered`` represents a sequence of assessment items.

    Like all OSID objects, an ``AssessmentOffered`` is identified by its
    ``Id`` and any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_id(self):
        """Gets the assessment ``Id`` corresponding to this assessment offering.

        :return: the assessment id
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_id = property(fget=get_assessment_id)

    @abc.abstractmethod
    def get_assessment(self):
        """Gets the assessment corresponding to this assessment offereng.

        :return: the assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment

    assessment = property(fget=get_assessment)

    @abc.abstractmethod
    def get_level_id(self):
        """Gets the ``Id`` of a ``Grade`` corresponding to the assessment difficulty.

        :return: a grade id
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    level_id = property(fget=get_level_id)

    @abc.abstractmethod
    def get_level(self):
        """Gets the ``Grade`` corresponding to the assessment difficulty.

        :return: the level
        :rtype: ``osid.grading.Grade``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    level = property(fget=get_level)

    @abc.abstractmethod
    def are_items_sequential(self):
        """Tests if the items or parts in this assessment are taken sequentially.

        :return: ``true`` if the items are taken sequentially, ``false`` if the items can be skipped and revisited
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def are_items_shuffled(self):
        """Tests if the items or parts appear in a random order.

        :return: ``true`` if the items appear in a random order, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def has_start_time(self):
        """Tests if there is a fixed start time for this assessment.

        :return: ``true`` if there is a fixed start time, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_start_time(self):
        """Gets the start time for this assessment.

        :return: the designated start time
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``has_start_time()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    start_time = property(fget=get_start_time)

    @abc.abstractmethod
    def has_deadline(self):
        """Tests if there is a fixed end time for this assessment.

        :return: ``true`` if there is a fixed end time, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_deadline(self):
        """Gets the end time for this assessment.

        :return: the designated end time
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``has_deadline()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    deadline = property(fget=get_deadline)

    @abc.abstractmethod
    def has_duration(self):
        """Tests if there is a fixed duration for this assessment.

        :return: ``true`` if there is a fixed duration, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_duration(self):
        """Gets the duration for this assessment.

        :return: the duration
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``has_duration()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    duration = property(fget=get_duration)

    @abc.abstractmethod
    def is_scored(self):
        """Tests if this assessment will be scored.

        :return: ``true`` if this assessment will be scored ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_score_system_id(self):
        """Gets the grade system ``Id`` for the score.

        :return: the grade system ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_scored()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    score_system_id = property(fget=get_score_system_id)

    @abc.abstractmethod
    def get_score_system(self):
        """Gets the grade system for the score.

        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- ``is_scored()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem

    score_system = property(fget=get_score_system)

    @abc.abstractmethod
    def is_graded(self):
        """Tests if this assessment will be graded.

        :return: ``true`` if this assessment will be graded, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_id(self):
        """Gets the grade system ``Id`` for the grade.

        :return: the grade system ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)

    @abc.abstractmethod
    def get_grade_system(self):
        """Gets the grade system for the grade.

        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)

    @abc.abstractmethod
    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        :return: ``true`` if a rubric is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        :return: an assessment offered ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_rubric()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    rubric_id = property(fget=get_rubric_id)

    @abc.abstractmethod
    def get_rubric(self):
        """Gets the rubric.

        :return: the assessment offered
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``IllegalState`` -- ``has_rubric()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOffered

    rubric = property(fget=get_rubric)

    @abc.abstractmethod
    def get_assessment_offered_record(self, assessment_taken_record_type):
        """Gets the assessment offered record corresponding to the given ``AssessmentOffered`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_offered_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_offered_record_type)`` is ``true``
        .

        :param assessment_taken_record_type: an assessment offered record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the assessment offered record
        :rtype: ``osid.assessment.records.AssessmentOfferedRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedRecord


class AssessmentOfferedForm:
    """This is the form for creating and updating an ``AssessmentOffered``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentOfferedAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_level_metadata(self):
        """Gets the metadata for a grade level.

        :return: metadata for the grade level
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    level_metadata = property(fget=get_level_metadata)

    @abc.abstractmethod
    def set_level(self, grade_id):
        """Sets the level of difficulty expressed as a ``Grade``.

        :param grade_id: the grade level
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level(self):
        """Clears the level.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level = property(fset=set_level, fdel=clear_level)

    @abc.abstractmethod
    def get_items_sequential_metadata(self):
        """Gets the metadata for sequential operation.

        :return: metadata for the sequential flag
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    items_sequential_metadata = property(fget=get_items_sequential_metadata)

    @abc.abstractmethod
    def set_items_sequential(self, sequential):
        """Sets the items sequential flag.

        :param sequential: ``true`` if the items are taken sequentially, ``false`` if the items can be skipped and revisited
        :type sequential: ``boolean``
        :raise: ``InvalidArgument`` -- ``sequential`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_items_sequential(self):
        """Clears the items sequential flag.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    items_sequential = property(fset=set_items_sequential, fdel=clear_items_sequential)

    @abc.abstractmethod
    def get_items_shuffled_metadata(self):
        """Gets the metadata for shuffling items.

        :return: metadata for the shuffled flag
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    items_shuffled_metadata = property(fget=get_items_shuffled_metadata)

    @abc.abstractmethod
    def set_items_shuffled(self, shuffle):
        """Sets the shuffle flag.

        The shuffle flag may be overidden by other assessment sequencing
        rules.

        :param shuffle: ``true`` if the items are shuffled, ``false`` if the items appear in the designated order
        :type shuffle: ``boolean``
        :raise: ``InvalidArgument`` -- ``shuffle`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_items_shuffled(self):
        """Clears the shuffle flag.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    items_shuffled = property(fset=set_items_shuffled, fdel=clear_items_shuffled)

    @abc.abstractmethod
    def get_start_time_metadata(self):
        """Gets the metadata for the assessment start time.

        :return: metadata for the start time
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    start_time_metadata = property(fget=get_start_time_metadata)

    @abc.abstractmethod
    def set_start_time(self, start):
        """Sets the assessment start time.

        :param start: assessment start time
        :type start: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``start`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_start_time(self):
        """Clears the start time.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_time = property(fset=set_start_time, fdel=clear_start_time)

    @abc.abstractmethod
    def get_deadline_metadata(self):
        """Gets the metadata for the assessment deadline.

        :return: metadata for the end time
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    deadline_metadata = property(fget=get_deadline_metadata)

    @abc.abstractmethod
    def set_deadline(self, end):
        """Sets the assessment end time.

        :param end: assessment end time
        :type end: ``timestamp``
        :raise: ``InvalidArgument`` -- ``end`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_deadline(self):
        """Clears the deadline.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    deadline = property(fset=set_deadline, fdel=clear_deadline)

    @abc.abstractmethod
    def get_duration_metadata(self):
        """Gets the metadata for the assessment duration.

        :return: metadata for the duration
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    duration_metadata = property(fget=get_duration_metadata)

    @abc.abstractmethod
    def set_duration(self, duration):
        """Sets the assessment duration.

        :param duration: assessment duration
        :type duration: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``duration`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_duration(self):
        """Clears the duration.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    duration = property(fset=set_duration, fdel=clear_duration)

    @abc.abstractmethod
    def get_score_system_metadata(self):
        """Gets the metadata for a score system.

        :return: metadata for the grade system
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    score_system_metadata = property(fget=get_score_system_metadata)

    @abc.abstractmethod
    def set_score_system(self, grade_system_id):
        """Sets the scoring system.

        :param grade_system_id: the grade system
        :type grade_system_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_system_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_system(self):
        """Clears the score system.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_system = property(fset=set_score_system, fdel=clear_score_system)

    @abc.abstractmethod
    def get_grade_system_metadata(self):
        """Gets the metadata for a grading system.

        :return: metadata for the grade system
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    grade_system_metadata = property(fget=get_grade_system_metadata)

    @abc.abstractmethod
    def set_grade_system(self, grade_system_id):
        """Sets the grading system.

        :param grade_system_id: the grade system
        :type grade_system_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_system_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system(self):
        """Clears the grading system.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system = property(fset=set_grade_system, fdel=clear_grade_system)

    @abc.abstractmethod
    def get_assessment_offered_form_record(self, assessment_offered_record_type):
        """Gets the ``AssessmentOfferedFormRecord`` corresponding to the given assessment record ``Type``.

        :param assessment_offered_record_type: the assessment offered record type
        :type assessment_offered_record_type: ``osid.type.Type``
        :return: the assessment offered record
        :rtype: ``osid.assessment.records.AssessmentOfferedFormRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedFormRecord


class AssessmentOfferedList:
    """Like all ``OsidLists,``  ``AssessmentOfferedList`` provides a means for accessing ``AssessmentTaken`` elements sequentially either one at a time or many at a time.

    Examples: while (aol.hasNext()) { AssessmentOffered assessment =
    aol.getNextAssessmentOffered();

    or
      while (aol.hasNext()) {
           AssessmentOffered[] assessments = aol.hetNextAssessmentsOffered(aol.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_assessment_offered(self):
        """Gets the next ``AssessmentOffered`` in this list.

        :return: the next ``AssessmentOffered`` in this list. The ``has_next()`` method should be used to test that a next ``AssessmentOffered`` is available before calling this method.
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOffered

    next_assessment_offered = property(fget=get_next_assessment_offered)

    @abc.abstractmethod
    def get_next_assessments_offered(self, n):
        """Gets the next set of ``AssessmentOffered`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``AssessmentOffered`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``AssessmentOffered`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOffered


class AssessmentTaken:
    """Represents a taken assessment or an assessment in progress."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_offered_id(self):
        """Gets the ``Id`` of the ``AssessmentOffered``.

        :return: the assessment offered ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_offered_id = property(fget=get_assessment_offered_id)

    @abc.abstractmethod
    def get_assessment_offered(self):
        """Gets the ``AssessmentOffered``.

        :return: the assessment offered
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOffered

    assessment_offered = property(fget=get_assessment_offered)

    @abc.abstractmethod
    def get_taker_id(self):
        """Gets the ``Id`` of the resource who took or is taking this assessment.

        :return: the resource ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    taker_id = property(fget=get_taker_id)

    @abc.abstractmethod
    def get_taker(self):
        """Gets the ``Resource`` taking this assessment.

        :return: the resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    taker = property(fget=get_taker)

    @abc.abstractmethod
    def get_taking_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` who took or is taking the assessment.

        :return: the agent ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    taking_agent_id = property(fget=get_taking_agent_id)

    @abc.abstractmethod
    def get_taking_agent(self):
        """Gets the ``Agent``.

        :return: the agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    taking_agent = property(fget=get_taking_agent)

    @abc.abstractmethod
    def has_started(self):
        """Tests if this assessment has begun.

        :return: ``true`` if the assessment has begun, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_actual_start_time(self):
        """Gets the time this assessment was started.

        :return: the start time
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``has_started()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    actual_start_time = property(fget=get_actual_start_time)

    @abc.abstractmethod
    def has_ended(self):
        """Tests if this assessment has ended.

        :return: ``true`` if the assessment has ended, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_completion_time(self):
        """Gets the time of this assessment was completed.

        :return: the end time
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``has_ended()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    completion_time = property(fget=get_completion_time)

    @abc.abstractmethod
    def get_time_spent(self):
        """Gets the total time spent taking this assessment.

        :return: the total time spent
        :rtype: ``osid.calendaring.Duration``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    time_spent = property(fget=get_time_spent)

    @abc.abstractmethod
    def get_completion(self):
        """Gets a completion percentage of the assessment.

        :return: the percent complete (0-100)
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    completion = property(fget=get_completion)

    @abc.abstractmethod
    def is_scored(self):
        """Tests if a score is available for this assessment.

        :return: ``true`` if a score is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_score_system_id(self):
        """Gets a score system ``Id`` for the assessment.

        :return: the grade system
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_score()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    score_system_id = property(fget=get_score_system_id)

    @abc.abstractmethod
    def get_score_system(self):
        """Gets a grade system for the score.

        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- ``is_scored()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem

    score_system = property(fget=get_score_system)

    @abc.abstractmethod
    def get_score(self):
        """Gets a score for the assessment.

        :return: the score
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_scored()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    score = property(fget=get_score)

    @abc.abstractmethod
    def is_graded(self):
        """Tests if a grade is available for this assessment.

        :return: ``true`` if a grade is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_id(self):
        """Gets a grade ``Id`` for the assessment.

        :return: the grade
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grade_id = property(fget=get_grade_id)

    @abc.abstractmethod
    def get_grade(self):
        """Gets a grade for the assessment.

        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    grade = property(fget=get_grade)

    @abc.abstractmethod
    def get_feedback(self):
        """Gets any overall comments available for this assessment by the grader.

        :return: comments
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    feedback = property(fget=get_feedback)

    @abc.abstractmethod
    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        :return: ``true`` if a rubric is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        :return: an assessment taken ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_rubric()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    rubric_id = property(fget=get_rubric_id)

    @abc.abstractmethod
    def get_rubric(self):
        """Gets the rubric.

        :return: the assessment taken
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``IllegalState`` -- ``has_rubric()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTaken

    rubric = property(fget=get_rubric)

    @abc.abstractmethod
    def get_assessment_taken_record(self, assessment_taken_record_type):
        """Gets the assessment taken record corresponding to the given ``AssessmentTaken`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_taken_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_taken_record_type)`` is ``true`` .

        :param assessment_taken_record_type: an assessment taken record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the assessment taken record
        :rtype: ``osid.assessment.records.AssessmentTakenRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenRecord


class AssessmentTakenForm:
    """This is the form for creating and updating an ``AssessmentTaken``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentTakenAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_taker_metadata(self):
        """Gets the metadata for a resource to manually set which resource will be taking the assessment.

        :return: metadata for the resource
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    taker_metadata = property(fget=get_taker_metadata)

    @abc.abstractmethod
    def set_taker(self, resource_id):
        """Sets the resource who will be taking this assessment.

        :param resource_id: the resource Id
        :type resource_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``resource_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_taker(self):
        """Clears the resource.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    taker = property(fset=set_taker, fdel=clear_taker)

    @abc.abstractmethod
    def get_assessment_taken_form_record(self, assessment_taken_record_type):
        """Gets the ``AssessmentTakenFormRecord`` corresponding to the given assessment taken record ``Type``.

        :param assessment_taken_record_type: the assessment taken record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the assessment taken record
        :rtype: ``osid.assessment.records.AssessmentTakenFormRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenFormRecord


class AssessmentTakenList:
    """Like all ``OsidLists,``  ``AssessmentTakenList`` provides a means for accessing ``AssessmentTaken`` elements sequentially either one at a time or many at a time.

    Examples: while (atl.hasNext()) { AssessmentTaken assessment =
    atl.getNextAssessmentTaken();

    or
      while (atl.hasNext()) {
           AssessmentTaken[] assessments = atl.hetNextAssessmentsTaken(atl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_assessment_taken(self):
        """Gets the next ``AssessmentTaken`` in this list.

        :return: the next ``AssessmentTaken`` in this list. The ``has_next()`` method should be used to test that a next ``AssessmentTaken`` is available before calling this method.
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTaken

    next_assessment_taken = property(fget=get_next_assessment_taken)

    @abc.abstractmethod
    def get_next_assessments_taken(self, n):
        """Gets the next set of ``AssessmentTaken`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``AssessmentTaken`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``AssessmentTaken`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTaken


class AssessmentSection:
    """Represents an assessment section.

    An assessment section represents a cluster of questions used to
    organize the execution of an assessment. The section is the student
    aspect of an assessment part.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_taken_id(self):
        """Gets the ``Id`` of the ``AssessmentTaken``.

        :return: the assessment taken ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_taken_id = property(fget=get_assessment_taken_id)

    @abc.abstractmethod
    def get_assessment_taken(self):
        """Gets the ``AssessmentTakeb``.

        :return: the assessment taken
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTaken

    assessment_taken = property(fget=get_assessment_taken)

    @abc.abstractmethod
    def has_allocated_time(self):
        """Tests if this section must be completed within an allocated time.

        :return: ``true`` if this section has an allocated time, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_allocated_time(self):
        """Gets the allocated time for this section.

        :return: allocated time
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``has_allocated_time()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    allocated_time = property(fget=get_allocated_time)

    @abc.abstractmethod
    def are_items_sequential(self):
        """Tests if the items or parts in this section are taken sequentially.

        :return: ``true`` if the items are taken sequentially, ``false`` if the items can be skipped and revisited
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def are_items_shuffled(self):
        """Tests if the items or parts appear in a random order.

        :return: ``true`` if the items appear in a random order, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_section_record(self, assessment_section_record_type):
        """Gets the assessment section record corresponding to the given ``AssessmentSection`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_section_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_section_record_type)`` is ``true``
        .

        :param assessment_section_record_type: an assessment section record type
        :type assessment_section_record_type: ``osid.type.Type``
        :return: the assessment section record
        :rtype: ``osid.assessment.records.AssessmentSectionRecord``
        :raise: ``NullArgument`` -- ``assessment_section_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_section_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentSectionRecord


class AssessmentSectionList:
    """Like all ``OsidLists,``  ``AssessmentSectionList`` provides a means for accessing ``AssessmentSection`` elements sequentially either one at a time or many at a time.

    Examples: while (asl.hasNext()) { AssessmentSection section =
    asl.getNextAssessmentSection();

    or
      while (asl.hasNext()) {
           AssessmentSection[] sections = asl.hetNextAssessmentSections(asl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_assessment_section(self):
        """Gets the next ``AssessmentSection`` in this list.

        :return: the next ``AssessmentSection`` in this list. The ``has_next()`` method should be used to test that a next ``AssessmentSection`` is available before calling this method.
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSection

    next_assessment_section = property(fget=get_next_assessment_section)

    @abc.abstractmethod
    def get_next_assessment_sections(self, n):
        """Gets the next set of ``AssessmentSection`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``AssessmentSection`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``AssessmentSection`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSection


class Bank:
    """A bank defines a collection of assessments and items."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_record(self, bank_record_type):
        """Gets the bank record corresponding to the given ``Bank`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``bank_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bank_record_type)``
        is ``true`` .

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the bank record
        :rtype: ``osid.assessment.records.BankRecord``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankRecord


class BankForm:
    """This is the form for creating and updating banks.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BankAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_form_record(self, bank_record_type):
        """Gets the ``BankFormRecord`` corresponding to the given bank record ``Type``.

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the bank record
        :rtype: ``osid.assessment.records.BankFormRecord``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankFormRecord


class BankList:
    """Like all ``OsidLists,``  ``BankList`` provides a means for accessing ``Bank`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Bank bank = bl.getNextBank(); }

    or
      while (bl.hasNext()) {
           Bank[] banks = bl.getNextBanks(bl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_bank(self):
        """Gets the next ``Bank`` in this list.

        :return: the next ``Bank`` in this list. The ``has_next()`` method should be used to test that a next ``Bank`` is available before calling this method.
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    next_bank = property(fget=get_next_bank)

    @abc.abstractmethod
    def get_next_banks(self, n):
        """Gets the next set of ``Bank`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Bank`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Bank`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank


class BankNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BankHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` at this node.

        :return: the bank represented by this node
        :rtype: ``osid.assessment.Bank``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def get_parent_bank_nodes(self):
        """Gets the parents of this bank.

        :return: the parents of this node
        :rtype: ``osid.assessment.BankNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankNodeList

    parent_bank_nodes = property(fget=get_parent_bank_nodes)

    @abc.abstractmethod
    def get_child_bank_nodes(self):
        """Gets the children of this bank.

        :return: the children of this node
        :rtype: ``osid.assessment.BankNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankNodeList

    child_bank_nodes = property(fget=get_child_bank_nodes)


class BankNodeList:
    """Like all ``OsidLists,``  ``BankNodeList`` provides a means for accessing ``BankNode`` elements sequentially either one at a time or many at a time.

    Examples: while (bnl.hasNext()) { BankNode node =
    bnl.getNextBankNode(); }

    or
      while (bnl.hasNext()) {
           BankNode[] nodes = bnl.getNextBankNodes(bnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_bank_node(self):
        """Gets the next ``BankNode`` in this list.

        :return: the next ``BankNode`` in this list. The ``has_next()`` method should be used to test that a next ``BankNode`` is available before calling this method.
        :rtype: ``osid.assessment.BankNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankNode

    next_bank_node = property(fget=get_next_bank_node)

    @abc.abstractmethod
    def get_next_bank_nodes(self, n):
        """Gets the next set of ``BankNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``BankNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``BanklNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.BankNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankNode


class ResponseList:
    """Like all ``OsidLists,``  ``ResponseList`` provides a means for accessing ``Response`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Response response =
    rl.getNextResponse(); }

    or
      while (rl.hasNext()) {
           Response[] responses = rl.getNextResponses(rl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_response(self):
        """Gets the next ``Response`` in this list.

        :return: the next ``Response`` in this list. The ``has_next()`` method should be used to test that a next ``Response`` is available before calling this method.
        :rtype: ``osid.assessment.Response``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Response

    next_response = property(fget=get_next_response)

    @abc.abstractmethod
    def get_next_responses(self, n):
        """Gets the next set of ``Response`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Response`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Response`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Response``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Response
