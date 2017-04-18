"""Implementations of assessment abstract base class sessions."""
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


class MyAssessmentTakenSession:
    """This session defines methods for retrieving assessments taken by the authenticated agent.

    An ``AssessmentTaken`` is created using the
    ``AssessmentTakenAdminSession``.

    Assessments taken may have an additional records indicated by their
    respective record types. The record is accessed via the
    ``AssessmentTaken``. The returns may not be cast directly from the
    returns in the lookup methods.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_get_my_taken_assessments(self):
        """Tests if this user can perform ``AssessmentOffered`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessments_started_during(self, start, end):
        """Gets all the assessments started by this agent during the given period of time inclusive.

        :param start: start time
        :type start: ``osid.calendaring.DateTime``
        :param end: end time
        :type end: ``osid.calendaring.DateTime``
        :return: the started assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_started(self):
        """Gets all the assessments started by this agent.

        :return: the started assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    assessments_started = property(fget=get_assessments_started)

    @abc.abstractmethod
    def get_assessments_in_progress_during(self, start, end):
        """Gets all the assessments in progress by this agent overlapping with the given period of time inclusive.

        :param start: start time
        :type start: ``osid.calendaring.DateTime``
        :param end: end time
        :type end: ``osid.calendaring.DateTime``
        :return: the in progress assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_in_progress(self):
        """Gets all the assessments started but not completed by this agent.

        :return: the assessments in progress
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    assessments_in_progress = property(fget=get_assessments_in_progress)

    @abc.abstractmethod
    def get_assessments_completed(self):
        """Gets all the assessments completed by this agent.

        :return: the completed assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    assessments_completed = property(fget=get_assessments_completed)


class AssessmentSession:
    """This session is used to take an assessment.

    The assessment associated with this session represents the
    "assessment taken" by an ``Agent``. This session may be created
    using an ``AssessmentOffered`` ``Id`` retrieved from an assessment
    bank, and instantiating this session represents the transaction of
    taking an assessment. Resuming an assessment, if permitted, is
    performed through instantiating this session with the
    ``AssessmentTaken`` ``Id``.

    ``Assessment Items`` are accessed via the ``Question`` interface. A
    ``Question``  ``Id`` is the same as the ``Item`` Id.

    This session manages the flow of control for the assessment taking
    process. It allows for two types of processes:

      * synchronous response: Each consecutive question is only
        available after the previous item was submitted or skipped.
      * asynchronous response: Questions may be accessed independently
        of response submission.


    It may be the case that it is allowed to suspend and resume an
    assessment. ``can_suspend()`` indicates the availability of this
    feature. ``finished()`` indicates the assessment is complete.

    This session is used in the context of an ``AssessmentSection``. An
    assessment with no sections defined is assumed to have a single
    default section that maps to the entire assessment.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_take_assessments(self):
        """Tests if this user can take this assessment section.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        :return: ``false`` if assessment methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def has_assessment_begun(self, assessment_taken_id):
        """Tests if this assessment has started.

        An assessment begins from the designated start time if a start
        time is defined. If no start time is defined the assessment may
        begin at any time. Assessment sections cannot be accessed if the
        return for this method is ``false``.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if this assessment has begun, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_assessment_over(self, assessment_taken_id):
        """Tests if this assessment is over.

        An assessment is over if ``finished_assessment()`` is invoked or
        the designated finish time has expired.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if this assessment is over, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def requires_synchronous_sections(self, assessment_taken_id):
        """Tests if synchronous sections are required.

        This method should be checked to determine if all sections are
        available when requested, or the next sections becomes available
        only after the previous section is complete.

        There are two methods for retrieving sections. One is using the
        built-in hasNextSection() and getNextSection() methods. In
        synchronous mode, hasNextSection() is false until the current
        section is completed. In asynchronous mode,
        ``has_next_section()`` returns true until the end of the
        assessment.

        ``AssessmentSections`` may also be accessed via an
        ``AssessmentSectionList``. If syncronous sections are required,
        ``AssessmentSectionList.available() == 0`` and
        ``AssessmentSectionList.getNextQuestion()`` blocks until the
        section is complete. ``AssessmentSectionList.hasNext()`` is
        always true until the end of the assessment is reached.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if this synchronous sections are required, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_first_assessment_section(self, assessment_taken_id):
        """Gets the first assessment section in this assesment.

        All assessments have at least one ``AssessmentSection``.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the first assessment section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSection

    @abc.abstractmethod
    def has_next_assessment_section(self, assessment_section_id):
        """Tests if there is a next assessment section in the assessment following the given assessment section ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if there is a next section, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_next_assessment_section(self, assessment_section_id):
        """Gets the next assessemnt section following the given assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the next section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_next_assessment_section()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSection

    @abc.abstractmethod
    def has_previous_assessment_section(self, assessment_section_id):
        """Tests if there is a previous assessment section in the assessment following the given assessment section ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if there is a previous assessment section, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_previous_assessment_section(self, assessment_section_id):
        """Gets the next assessemnt section following the given assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the previous assessment section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_next_assessment_section()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSection

    @abc.abstractmethod
    def get_assessment_section(self, assessment_section_id):
        """Gets an assessemnts section by ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the assessment section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSection

    @abc.abstractmethod
    def get_assessment_sections(self, assessment_taken_id):
        """Gets the assessment sections of this assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the list of assessment sections
        :rtype: ``osid.assessment.AssessmentSectionList``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSectionList

    @abc.abstractmethod
    def is_assessment_section_complete(self, assessment_section_id):
        """Tests if the all responses have been submitted to this assessment section.

        If ``is_assessment_section_complete()`` is false, then
        ``get_unanswered_questions()`` may return a list of questions
        that can be submitted.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this assessment section is complete, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_assessment_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_incomplete_assessment_sections(self, assessment_taken_id):
        """Gets the incomplete assessment sections of this assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the list of incomplete assessment sections
        :rtype: ``osid.assessment.AssessmentSectionList``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSectionList

    @abc.abstractmethod
    def has_assessment_section_begun(self, assessment_section_id):
        """Tests if this assessment section has started.

        A section begins from the designated start time if a start time
        is defined. If no start time is defined the section may begin at
        any time. Assessment items cannot be accessed or submitted if
        the return for this method is ``false``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this assessment section has begun, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false or is_assessment_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_assessment_section_over(self, assessment_section_id):
        """Tests if this assessment section is over.

        An assessment section is over if new or updated responses can
        not be submitted such as the designated finish time has expired.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this assessment is over, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessmen_sectiont_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def requires_synchronous_responses(self, assessment_section_id):
        """Tests if synchronous responses are required in this assessment section.

        This method should be checked to determine if all items are
        available when requested, or the next item becomes available
        only after the response to the current item is submitted.

        There are two methods for retrieving questions. One is using the
        built-in ``has_next_question()`` and ``get_next_question()``
        methods. In synchronous mode, ``has_next_question()`` is
        ``false`` until the response for the current question is
        submitted. In asynchronous mode, ``has_next_question()`` returns
        ``true`` until the end of the assessment.

        ``Questions`` may also be accessed via a ``QuestionList``. If
        syncronous responses are required, ``QuestionList.available() ==
        0`` and ``QuestionList.getNextQuestion()`` blocks until the
        response is submitted. ``QuestionList.hasNext()`` is always true
        until the end of the assessment is reached.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this synchronous responses are required, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false or is_assessment_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_first_question(self, assessment_section_id):
        """Gets the first question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the first question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def has_next_question(self, assessment_section_id, item_id):
        """Tests if there is a next question following the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a next question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_next_question(self, assessment_section_id, item_id):
        """Gets the next question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the next question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_next_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def has_previous_question(self, assessment_section_id, item_id):
        """Tests if there is a previous question preceeding the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a previous question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_previous_question(self, assessment_section_id, item_id):
        """Gets the previous question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the previous question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_previous_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def get_question(self, assessment_section_id, item_id):
        """Gets the ``Question`` specified by its ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the returned ``Question``
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def get_questions(self, assessment_section_id):
        """Gets the questions of this assessment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the list of assessment questions
        :rtype: ``osid.assessment.QuestionList``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.QuestionList

    @abc.abstractmethod
    def get_response_form(self, assessment_section_id, item_id):
        """Gets the response form for submitting an answer.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: an answer form
        :rtype: ``osid.assessment.AnswerForm``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AnswerForm

    @abc.abstractmethod
    def submit_response(self, assessment_section_id, item_id, answer_form):
        """Submits an answer to an item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param answer_form: the response
        :type answer_form: ``osid.assessment.AnswerForm``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``InvalidArgument`` -- one or more of the elements in the form is invalid
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id, item_id,`` or ``answer_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``answer_form`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def skip_item(self, assessment_section_id, item_id):
        """Skips an item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def is_question_answered(self, assessment_section_id, item_id):
        """Tests if the given item has a response.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if this item has a response, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_unanswered_questions(self, assessment_section_id):
        """Gets the unanswered questions of this assessment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the list of questions with no rsponses
        :rtype: ``osid.assessment.QuestionList``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.QuestionList

    @abc.abstractmethod
    def has_unanswered_questions(self, assessment_section_id):
        """Tests if there are unanswered questions in this assessment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if there are unanswered questions, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_first_unanswered_question(self, assessment_section_id):
        """Gets the first unanswered question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the first unanswered question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_unanswered_questions()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def has_next_unanswered_question(self, assessment_section_id, item_id):
        """Tests if there is a next unanswered question following the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a next unanswered question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_next_unanswered_question(self, assessment_section_id, item_id):
        """Gets the next unanswered question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the next unanswered question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_next_unanswered_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def has_previous_unanswered_question(self, assessment_section_id, item_id):
        """Tests if there is a previous unanswered question preceeding the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a previous unanswered question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_previous_unanswered_question(self, assessment_section_id, item_id):
        """Gets the previous unanswered question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the previous unanswered question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_previous_unanswered_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def get_response(self, assessment_section_id, item_id):
        """Gets the submitted response to the associated item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the response
        :rtype: ``osid.assessment.Response``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Response

    @abc.abstractmethod
    def get_responses(self, assessment_section_id):
        """Gets all submitted responses.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the list of responses
        :rtype: ``osid.assessment.ResponseList``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ResponseList

    @abc.abstractmethod
    def clear_response(self, assessment_section_id, item_id):
        """Clears the response to an item The item appears as unanswered.

        If no response exists, the method simply returns.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def finish_assessment_section(self, assessment_section_id):
        """Indicates an assessment section is complete.

        Finished sections may or may not allow new or updated responses.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def is_answer_available(self, assessment_section_id, item_id):
        """Tests if an answer is available for the given item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if an answer are available, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_answers(self, assessment_section_id, item_id):
        """Gets the acceptable answers to the associated item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the answers
        :rtype: ``osid.assessment.AnswerList``
        :raise: ``IllegalState`` -- ``is_answer_available()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AnswerList

    @abc.abstractmethod
    def finish_assessment(self, assessment_taken_id):
        """Indicates the entire assessment is complete.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_begun()`` is ``false or is_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentResultsSession:
    """This session is used to access the tested assessment items and their associated responses.

    Assessment results may also be available and is expressed as a
    rubric through another assessment.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_access_assessment_results(self):
        """Tests if this user can take this assessment.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        :return: ``false`` if assessment methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_items(self, assessment_taken_id):
        """Gets the items questioned in a assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the list of assessment questions
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_responses(self, assessment_taken_id):
        """Gets the submitted responses.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the submitted answers
        :rtype: ``osid.assessment.ResponseList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ResponseList

    @abc.abstractmethod
    def are_results_available(self, assessment_taken_id):
        """Tests if the results are available for this assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if results are available, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_entries(self, assessment_taken_id):
        """Gets a list of grade entries for this assessment.

        Each grade entry may indicate a grade or score input by multiple
        graders.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: a list of grade entries
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``IllegalState`` -- ``are_results_available()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryList


class ItemLookupSession:
    """This session provides methods for retrieving ``Item`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_items(self):
        """Tests if this user can perform ``Item`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_item_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_item_view(self):
        """A complete view of the ``Item`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this assessment bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_item(self, item_id):
        """Gets the ``Item`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Item`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Item`` and retained for compatibility.

        :param item_id: the ``Id`` of the ``Item`` to retrieve
        :type item_id: ``osid.id.Id``
        :return: the returned ``Item``
        :rtype: ``osid.assessment.Item``
        :raise: ``NotFound`` -- no ``Item`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Item

    @abc.abstractmethod
    def get_items_by_ids(self, item_ids):
        """Gets an ``ItemList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the items
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Items`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param item_ids: the list of ``Ids`` to retrieve
        :type item_ids: ``osid.id.IdList``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``item_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_genus_type(self, item_genus_type):
        """Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` which does not include assessment items of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        :param item_genus_type: an assessment item genus type
        :type item_genus_type: ``osid.type.Type``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_parent_genus_type(self, item_genus_type):
        """Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` and include any additional assessment items with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        :param item_genus_type: an assessment item genus type
        :type item_genus_type: ``osid.type.Type``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_record_type(self, item_record_type):
        """Gets an ``ItemList`` containing the given assessment item record ``Type``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param item_record_type: an item record type
        :type item_record_type: ``osid.type.Type``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_question(self, question_id):
        """Gets an ``ItemList`` containing the given question.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param question_id: a question ``Id``
        :type question_id: ``osid.id.Id``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``question_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_answer(self, answer_id):
        """Gets an ``ItemList`` containing the given answer.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param answer_id: an answer ``Id``
        :type answer_id: ``osid.id.Id``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_learning_objective(self, objective_id):
        """Gets an ``ItemList`` containing the given learning objective.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param objective_id: a learning objective ``Id``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items_by_learning_objectives(self, objective_ids):
        """Gets an ``ItemList`` containing the given learning objectives.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param objective_ids: a list of learning objective ``Ids``
        :type objective_ids: ``osid.id.IdList``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_items(self):
        """Gets all ``Items``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those items that are accessible through this session.

        :return: a list of ``Items``
        :rtype: ``osid.assessment.ItemList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    items = property(fget=get_items)


class ItemQuerySession:
    """This session provides methods for searching ``Item`` objects.

    The search query is constructed using the ``ItemQuery``. The
    assessment item record ``Type`` also specifies the query record for
    the assessment item query.

    This session defines views that offer differing behaviors for
    searching.

      * federated assessment bank view: searches include assessment
        items in assessment banks of which this assessment bank is a
        ancestor in the assessment bank hierarchy
      * isolated bank


    Assessment items may have a query record indicated by their
    respective record types. Thequery record is accessed via the
    ``ItemQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_items(self):
        """Tests if this user can perform ``Item`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this assessment bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_item_query(self):
        """Gets an assessment item query.

        :return: the assessment item query
        :rtype: ``osid.assessment.ItemQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQuery

    item_query = property(fget=get_item_query)

    @abc.abstractmethod
    def get_items_by_query(self, item_query):
        """Gets a list of ``Items`` matching the given item query.

        :param item_query: the item query
        :type item_query: ``osid.assessment.ItemQuery``
        :return: the returned ``ItemList``
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList


class ItemSearchSession:
    """This session provides methods for searching ``Item`` objects.

    The search query is constructed using the ``ItemQuery``. The
    assessment item record ``Type`` also specifies the query record for
    the assessment item query.

    ``get_items_by_query()`` is the basic search method and returns a
    list of ``Items``. A more advanced search may be performed with
    ``getItemsBySearch()``. It accepts an ``ItemSearch`` in addition to
    the query for the purpose of specifying additional options affecting
    the entire search, such as ordering. ``get_items_by_search()``
    returns an ``ItemSearchResults`` that can be used to access the
    resulting ``ItemList`` or be used to perform a search within the
    result set through ``ItemSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated assessment bank view: searches include assessment
        items in assessment banks of which this assessment bank is a
        ancestor in the assessment bank hierarchy
      * isolated bank view: searches are restricted to assessment items
        in this assessment bank


    Assessment items may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``ItemQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_item_search(self):
        """Gets an assessment item search.

        :return: the assessment item search
        :rtype: ``osid.assessment.ItemSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemSearch

    item_search = property(fget=get_item_search)

    @abc.abstractmethod
    def get_item_search_order(self):
        """Gets an assessment item search order.

        The ``ItemSearchOrder`` is supplied to an ``ItemSearch`` to
        specify the ordering of results.

        :return: the assessment item search order
        :rtype: ``osid.assessment.ItemSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemSearchOrder

    item_search_order = property(fget=get_item_search_order)

    @abc.abstractmethod
    def get_items_by_search(self, item_query, item_search):
        """Gets the search results matching the given search query using the given search.

        :param item_query: the item query
        :type item_query: ``osid.assessment.ItemQuery``
        :param item_search: the item search
        :type item_search: ``osid.assessment.ItemSearch``
        :return: the returned search results
        :rtype: ``osid.assessment.ItemSearchResults``
        :raise: ``NullArgument`` -- ``item_query`` or ``item_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_search`` or ``item_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemSearchResults

    @abc.abstractmethod
    def get_item_query_from_inspector(self, item_query_inspector):
        """Gets an item query from an inspector.

        The inspector is available from an ``ItemSearchResults``.

        :param item_query_inspector: a query inspector
        :type item_query_inspector: ``osid.assessment.ItemQueryInspector``
        :return: the item query
        :rtype: ``osid.assessment.ItemQuery``
        :raise: ``NullArgument`` -- ``item_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``item_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQuery


class ItemAdminSession:
    """This session creates, updates, and deletes ``Items``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Item,`` an ``ItemForm`` is requested using
    ``get_item_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ItemForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ItemForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ItemForm`` corresponds
    to an attempted transaction.

    For updates, ``ItemForms`` are requested to the ``ItemForm``  ``Id``
    that is to be updated using ``getItemFormForUpdate()``. Similarly,
    the ``ItemForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``ItemForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``ItemForm``. To unmap an ``ItemForm``
    from the current ``Bank,`` the ``ItemBankAssignmentSession`` should
    be used. These delete operations attempt to remove the ``Item``
    itself thus removing it from all known ``Bank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_items(self):
        """Tests if this user can create ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_item_with_record_types(self, item_record_types):
        """Tests if this user can create a single ``Item`` using the desired record types.

        While ``AssessmentManager.getItemRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Item``.
        Providing an empty array tests if an ``Item`` can be created
        with no records.

        :param item_record_types: array of item record types
        :type item_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Item`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``item_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_form_for_create(self, item_record_types):
        """Gets the assessment item form for creating new assessment items.

        A new form should be requested for each create transaction.

        :param item_record_types: array of item record types to be included in the create operation or an empty list if none
        :type item_record_types: ``osid.type.Type[]``
        :return: the assessment item form
        :rtype: ``osid.assessment.ItemForm``
        :raise: ``NullArgument`` -- ``item_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemForm

    @abc.abstractmethod
    def create_item(self, item_form):
        """Creates a new ``Item``.

        :param item_form: the form for this ``Item``
        :type item_form: ``osid.assessment.ItemForm``
        :return: the new ``Item``
        :rtype: ``osid.assessment.Item``
        :raise: ``IllegalState`` -- ``item_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``item_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_form`` did not originate from ``get_item_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Item

    @abc.abstractmethod
    def can_update_items(self):
        """Tests if this user can update ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if assessment item modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_form_for_update(self, item_id):
        """Gets the assessment item form for updating an existing item.

        A new item form should be requested for each update transaction.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the assessment item form
        :rtype: ``osid.assessment.ItemForm``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemForm

    @abc.abstractmethod
    def update_item(self, item_form):
        """Updates an existing item.

        :param item_form: the form containing the elements to be updated
        :type item_form: ``osid.assessment.ItemForm``
        :raise: ``IllegalState`` -- ``item_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``item_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_form`` did not originate from ``get_item_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_items(self):
        """Tests if this user can delete ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_item(self, item_id):
        """Deletes the ``Item`` identified by the given ``Id``.

        :param item_id: the ``Id`` of the ``Item`` to delete
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Item`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_item_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_item(self, item_id, alias_id):
        """Adds an ``Id`` to an ``Item`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Item`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another item, it is reassigned to the
        given item ``Id``.

        :param item_id: the ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``item_id`` not found
        :raise: ``NullArgument`` -- ``item_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_create_questions(self):
        """Tests if this user can create ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Question`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_question_with_record_types(self, question_record_types):
        """Tests if this user can create a single ``Question`` using the desired record types.

        While ``AssessmentManager.getQuestionRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Question``.
        Providing an empty array tests if a ``Question`` can be created
        with no records.

        :param question_record_types: array of question record types
        :type question_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Question`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``question_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_question_form_for_create(self, item_id, question_record_types):
        """Gets the question form for creating new questions.

        A new form should be requested for each create transaction.

        :param item_id: an assessment item ``Id``
        :type item_id: ``osid.id.Id``
        :param question_record_types: array of question record types to be included in the create operation or an empty list if none
        :type question_record_types: ``osid.type.Type[]``
        :return: the question form
        :rtype: ``osid.assessment.QuestionForm``
        :raise: ``NullArgument`` -- ``question_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.QuestionForm

    @abc.abstractmethod
    def create_question(self, question_form):
        """Creates a new ``Question``.

        :param question_form: the form for this ``Question``
        :type question_form: ``osid.assessment.QuestionForm``
        :return: the new ``Question``
        :rtype: ``osid.assessment.Question``
        :raise: ``AlreadyExists`` -- a question already exists for this item
        :raise: ``IllegalState`` -- ``question_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``question_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``question_form`` did not originate from ``get_question_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Question

    @abc.abstractmethod
    def can_update_questions(self):
        """Tests if this user can update ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if question modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_question_form_for_update(self, question_id):
        """Gets the question form for updating an existing question.

        A new question form should be requested for each update
        transaction.

        :param question_id: the ``Id`` of the ``Question``
        :type question_id: ``osid.id.Id``
        :return: the question form
        :rtype: ``osid.assessment.QuestionForm``
        :raise: ``NotFound`` -- ``question_id`` is not found
        :raise: ``NullArgument`` -- ``question_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.QuestionForm

    @abc.abstractmethod
    def update_question(self, question_form):
        """Updates an existing question.

        :param question_form: the form containing the elements to be updated
        :type question_form: ``osid.assessment.QuestionForm``
        :raise: ``IllegalState`` -- ``question_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``question_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``question_form`` did not originate from ``get_question_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_questions(self):
        """Tests if this user can delete ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Question`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_question(self, question_id):
        """Deletes the ``Question`` identified by the given ``Id``.

        :param question_id: the ``Id`` of the ``Question`` to delete
        :type question_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Question`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``question_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_create_answers(self):
        """Tests if this user can create ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Answer``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Answer`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_answers_with_record_types(self, answer_record_types):
        """Tests if this user can create a single ``Answer`` using the desired record types.

        While ``AssessmentManager.getAnswerRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Answer``.
        Providing an empty array tests if an ``Answer`` can be created
        with no records.

        :param answer_record_types: array of answer record types
        :type answer_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Answer`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``answern_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_answer_form_for_create(self, item_id, answer_record_types):
        """Gets the answer form for creating new answers.

        A new form should be requested for each create transaction.

        :param item_id: an assessment item ``Id``
        :type item_id: ``osid.id.Id``
        :param answer_record_types: array of answer record types to be included in the create operation or an empty list if none
        :type answer_record_types: ``osid.type.Type[]``
        :return: the answer form
        :rtype: ``osid.assessment.AnswerForm``
        :raise: ``NullArgument`` -- ``answer_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AnswerForm

    @abc.abstractmethod
    def create_answer(self, answer_form):
        """Creates a new ``Answer``.

        :param answer_form: the form for this ``Answer``
        :type answer_form: ``osid.assessment.AnswerForm``
        :return: the new ``Answer``
        :rtype: ``osid.assessment.Answer``
        :raise: ``IllegalState`` -- ``answer_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``answer_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``answer_form`` did not originate from ``get_answer_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Answer

    @abc.abstractmethod
    def can_update_answers(self):
        """Tests if this user can update ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if answer modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_answer_form_for_update(self, answer_id):
        """Gets the answer form for updating an existing answer.

        A new answer form should be requested for each update
        transaction.

        :param answer_id: the ``Id`` of the ``Answer``
        :type answer_id: ``osid.id.Id``
        :return: the answer form
        :rtype: ``osid.assessment.AnswerForm``
        :raise: ``NotFound`` -- ``answer_id`` is not found
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AnswerForm

    @abc.abstractmethod
    def update_answer(self, answer_form):
        """Updates an existing answer.

        :param answer_form: the form containing the elements to be updated
        :type answer_form: ``osid.assessment.AnswerForm``
        :raise: ``IllegalState`` -- ``answer_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``answer_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``answer_form`` did not originate from ``get_answer_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_answers(self):
        """Tests if this user can delete ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Answer`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_answer(self, answer_id):
        """Deletes the ``Answer`` identified by the given ``Id``.

        :param answer_id: the ``Id`` of the ``Answer`` to delete
        :type answer_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Answer`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ItemNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Item`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``ItemLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_item_notifications(self):
        """Tests if this user can register for ``Item`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for assessment items
        in assessment banks which are children of this assessment bank
        in the assessment bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this assessment bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_item_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_item_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_item_notification(self, notification_id):
        """Acknowledge an item notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_items(self):
        """Register for notifications of new assessment items.

        ``ItemReceiver.newItems()`` is invoked when a new ``Item`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_items(self):
        """Registers for notification of updated assessment items.

        ``ItemReceiver.changedItems()`` is invoked when an assessment
        item is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_item(self, item_id):
        """Registers for notification of an updated assessment item.

        ``ItemReceiver.changedItems()`` is invoked when the specified
        assessment item is changed.

        :param item_id: the ``Id`` of the ``Assessment`` to monitor
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``item`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_items(self):
        """Registers for notification of deleted assessment items.

        ``ItemReceiver.deletedItems()`` is invoked when an assessment
        item is removed from the assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_item(self, item_id):
        """Registers for notification of a deleted assessment item.

        ``ItemReceiver.deletedItems()`` is invoked when the specified
        assessment item is removed from the assessment bank.

        :param item_id: the ``Id`` of the ``Item`` to monitor
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Item`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_item_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_item_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_item_notification(self, notification_id):
        """Acknowledge an item notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ItemBankSession:
    """This session provides methods to retrieve ``Item`` to ``Bank`` mappings.

    An ``Item`` may appear in multiple ``Banks``. Each ``Bank`` may have
    its own authorizations governing who is allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_item_bank_mappings(self):
        """Tests if this user can perform lookups of item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_bank_view(self):
        """A complete view of the ``Item`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_item_ids_by_bank(self, bank_id):
        """Gets the list of ``Item``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related item ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_items_by_bank(self, bank_id):
        """Gets the list of ``Items`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_item_ids_by_banks(self, bank_ids):
        """Gets the list of ``Item Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_items_by_banks(self, bank_ids):
        """Gets the list of ``Items`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_bank_ids_by_item(self, item_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``Item``.

        :param item_id: ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_item(self, item_id):
        """Gets the list of ``Banks`` mapped to an ``Item``.

        :param item_id: ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class ItemBankAssignmentSession:
    """This session provides methods to re-assign ``Items`` to ``Banks``.

    An ``Item`` may map to multiple ``Banks`` and removing the last
    reference to an ``Item`` is the equivalent of deleting it. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    operate on it.

    Moving or adding a reference of an ``Item`` to another ``Bank`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_items(self):
        """Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_items_to_bank(self, bank_id):
        """Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given bank node in which any item can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_item(self, bank_id, item_id):
        """Gets a list of banks including and under the given bank node in which a specific item can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_item_to_bank(self, item_id, bank_id):
        """Adds an existing ``Item`` to a ``Bank``.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``item_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``item_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``item_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_item_from_bank(self, item_id, bank_id):
        """Removes an ``Item`` from a ``Bank``.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id`` or ``bank_id`` not found or ``item_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``item_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_item_to_billing(self, item_id, from_bank_id, to_bank_id):
        """Moves an ``Item`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id, from_bank_id,`` or ``to_bank_id`` not found or ``item_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``item_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ItemSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``ItemQuery`` can be retrieved from this session and mapped to
    this ``Bank`` to create a virtual collection of ``Items``. The Items
    may be sequenced using the ``ItemSearchOrder`` from this session.

    This ``Bank`` has a default query that matches any Item and a
    default search order that specifies no sequencing. The queries may
    be examined using an ``ItemQueryInspector``. The query may be
    modified by converting the inspector back to an ``ItemQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart banks.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_item_query(self):
        """Gets an assessment item query.

        :return: the assessment item query
        :rtype: ``osid.assessment.ItemQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQuery

    item_query = property(fget=get_item_query)

    @abc.abstractmethod
    def get_item_search_order(self):
        """Gets an assessment item search order.

        :return: the assessment item search order
        :rtype: ``osid.assessment.ItemSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemSearchOrder

    item_search_order = property(fget=get_item_search_order)

    @abc.abstractmethod
    def apply_item_query(self, item_query):
        """Applies an item query to this bank.

        :param item_query: the item query
        :type item_query: ``osid.assessment.ItemQuery``
        :raise: ``NullArgument`` -- ``item_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_item_query(self):
        """Gets an item query inspector for this bank.

        :return: the item query inspector
        :rtype: ``osid.assessment.ItemQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQueryInspector

    @abc.abstractmethod
    def apply_item_sequencing(self, item_search_order):
        """Applies an item search order to this bank.

        :param item_search_order: the item search order
        :type item_search_order: ``osid.assessment.ItemSearchOrder``
        :raise: ``NullArgument`` -- ``item_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_item_query_from_inspector(self, item_query_inspector):
        """Gets an item query from an inspector.

        :param item_query_inspector: an item query inspector
        :type item_query_inspector: ``osid.assessment.ItemQueryInspector``
        :return: the item query
        :rtype: ``osid.assessment.ItemQuery``
        :raise: ``NullArgument`` -- ``item_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``item_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQuery


class AssessmentLookupSession:
    """This session defines methods for retrieving assessments."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_assessments(self):
        """Tests if this user can perform ``Assessment`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_assessment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_assessment_view(self):
        """A complete view of the ``Assessment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment(self, assessment_id):
        """Gets the ``Assessment`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Assessment`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Assessment`` and retained
        for compatibility.

        :param assessment_id: ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``NotFound`` -- ``assessment_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.Assessment

    @abc.abstractmethod
    def get_assessments_by_ids(self, assessment_ids):
        """Gets an ``AssessmentList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assessments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param assessment_ids: the list of ``Ids`` to retrieve
        :type assessment_ids: ``osid.id.IdList``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    @abc.abstractmethod
    def get_assessments_by_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :param assessment_genus_type: an assessment genus type
        :type assessment_genus_type: ``osid.type.Type``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    @abc.abstractmethod
    def get_assessments_by_parent_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :param assessment_genus_type: an assessment genus type
        :type assessment_genus_type: ``osid.type.Type``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    @abc.abstractmethod
    def get_assessments_by_record_type(self, assessment_record_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :param assessment_record_type: an assessment record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    @abc.abstractmethod
    def get_assessments(self):
        """Gets all ``Assessments``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :return: a list of ``Assessments``
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    assessments = property(fget=get_assessments)


class AssessmentQuerySession:
    """This session provides methods for querying ``Assessment`` objects.

    The search query is constructed using the ``AssessmentQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessments in banks of
        which this bank is a ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments in
        this bank


    Assessments may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``AssessmentQuery``. The returns in this session may not be cast
    directly to these interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_assessments(self):
        """Tests if this user can perform ``Assessment`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets an assessment query.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def get_assessments_by_query(self, assessment_query):
        """Gets a list of ``Assessments`` matching the given assessment query.

        :param assessment_query: the assessment query
        :type assessment_query: ``osid.assessment.AssessmentQuery``
        :return: the returned ``AssessmentList``
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList


class AssessmentSearchSession:
    """This session provides methods for searching among ``Assessment`` objects.

    The search query is constructed using the ``AssessmentQuery``.

    ``get_assessments_by_query()`` is the basic search method and
    returns a list of ``Assessments``. A more advanced search may be
    performed with ``getAssessmentsBySearch()``. It accepts an
    ``AssessmentSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_assessments_by_search()`` returns an
    ``AssessmentSearchResults`` that can be used to access the resulting
    ``AssessmentList`` or be used to perform a search within the result
    set through ``AssessmentSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessments in banks of
        which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments in
        this bank


    Assessments may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``AssessmentQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_search(self):
        """Gets an assessment search.

        :return: the assessment search
        :rtype: ``osid.assessment.AssessmentSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSearch

    assessment_search = property(fget=get_assessment_search)

    @abc.abstractmethod
    def get_assessment_search_order(self):
        """Gets an assessment search order.

        The ``AssessmentSearchOrder`` is supplied to an
        ``AssessmentSearch`` to specify the ordering of results.

        :return: the assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSearchOrder

    assessment_search_order = property(fget=get_assessment_search_order)

    @abc.abstractmethod
    def get_assessments_by_search(self, assessment_query, assessment_search):
        """Gets the search results matching the given search query using the given search.

        :param assessment_query: the assessment query
        :type assessment_query: ``osid.assessment.AssessmentQuery``
        :param assessment_search: the assessment search
        :type assessment_search: ``osid.assessment.AssessmentSearch``
        :return: the search results
        :rtype: ``osid.assessment.AssessmentSearchResults``
        :raise: ``NullArgument`` -- ``assessment_query`` or ``assessment_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_query`` or ``assessment_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSearchResults

    @abc.abstractmethod
    def get_assessment_query_from_inspector(self, assessment_query_inspector):
        """Gets an assessment query from an inspector.

        The inspector is available from an ``AssessmentSearchResults``.

        :param assessment_query_inspector: an assessment query inspector
        :type assessment_query_inspector: ``osid.assessment.AssessmentQueryInspector``
        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``NullArgument`` -- ``assessment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQuery


class AssessmentAdminSession:
    """This session creates, updates, and deletes ``Assessments``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Assessment,`` an ``AssessmentForm`` is requested using
    ``get_assessment_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``AssessmentForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``AssessmentForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``AssessmentForm``
    corresponds to an attempted transaction.

    For updates, ``AssessmentForms`` are requested to the ``Assessment``
    ``Id`` that is to be updated using ``getAssessmentFormForUpdate()``.
    Similarly, the ``AssessmentForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``AssessmentForm`` can only be used once for a
    successful update and cannot be reused.

    The delete operations delete ``Assessments``. To unmap an
    ``Assessment`` from the current ``Bank,`` the
    ``AssessmentBankAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Assessment`` itself thus removing
    it from all known ``Bank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_assessments(self):
        """Tests if this user can create ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_assessment_with_record_types(self, assessment_record_types):
        """Tests if this user can create a single ``Assessment`` using the desired record interface types.

        While ``AssessmentManager.getAssessmentRecordTypes()`` can be
        used to examine which record interfaces are supported, this
        method tests which record(s) are required for creating a
        specific ``Assessment``. Providing an empty array tests if an
        ``Assessment`` can be created with no records.

        :param assessment_record_types: array of assessment record types
        :type assessment_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Assessment`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_form_for_create(self, assessment_record_types):
        """Gets the assessment form for creating new assessments.

        A new form should be requested for each create transaction.

        :param assessment_record_types: array of assessment record types to be included in the create operation or an empty list if none
        :type assessment_record_types: ``osid.type.Type[]``
        :return: the assessment form
        :rtype: ``osid.assessment.AssessmentForm``
        :raise: ``NullArgument`` -- ``assessment_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentForm

    @abc.abstractmethod
    def create_assessment(self, assessment_form):
        """Creates a new ``Assessment``.

        :param assessment_form: the form for this ``Assessment``
        :type assessment_form: ``osid.assessment.AssessmentForm``
        :return: the new ``Assessment``
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- ``assessment_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``assessment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form`` did not originate from ``get_assessment_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment

    @abc.abstractmethod
    def can_update_assessments(self):
        """Tests if this user can update ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_form_for_update(self, assessment_id):
        """Gets the assessment form for updating an existing assessment.

        A new assessment form should be requested for each update
        transaction.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the assessment form
        :rtype: ``osid.assessment.AssessmentForm``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentForm

    @abc.abstractmethod
    def update_assessment(self, assessment_form):
        """Updates an existing assessment.

        :param assessment_form: the form containing the elements to be updated
        :type assessment_form: ``osid.assessment.AssessmentForm``
        :raise: ``IllegalState`` -- ``assessment_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``assessment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form did not originate from get_assessment_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_assessments(self):
        """Tests if this user can delete ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_assessment(self, assessment_id):
        """Deletes an ``Assessment``.

        :param assessment_id: the ``Id`` of the ``Assessment`` to remove
        :type assessment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_assessment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_assessment(self, assessment_id, alias_id):
        """Adds an ``Id`` to an ``Assessment`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Assessment`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another assessment, it is reassigned
        to the given assessment ``Id``.

        :param assessment_id: the ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Assessment`` objects in this ``Bank``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``AssessmentLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_assessment_notifications(self):
        """Tests if this user can register for ``Assessment`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for assessments in
        banks which are children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for assessments to this
        bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_notification(self, notification_id):
        """Acknowledge an assessment notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments(self):
        """Register for notifications of new assessments.

        ``AssessmentReceiver.newAssessments()`` is invoked when a new
        ``Assessment`` appears in this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments(self):
        """Registers for notification of updated assessments.

        ``AssessmentReceiver.changedAssessments()`` is invoked when an
        assessment in this assessment bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessment(self, assessment_id):
        """Registers for notification of an updated assessment.

        ``AssessmentReceiver.changedAssessments()`` is invoked when the
        specified assessment in this assessment bank is changed.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments(self):
        """Registers for notification of deleted assessments.

        ``AssessmentReceiver.deletedAssessments()`` is invoked when an
        assessment is removed from this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessment(self, assessment_id):
        """Registers for notification of a deleted assessment.

        ``AssessmentReceiver.deletedAssessments()`` is invoked when the
        specified assessment is removed from this assessment bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_notification(self, notification_id):
        """Acknowledge an assessment notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentBankSession:
    """This session provides methods to retrieve ``Assessment`` to ``Bank`` mappings.

    An ``Assessment`` may appear in multiple ``Banks``. Each ``Bank``
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_assessment_bank_mappings(self):
        """Tests if this user can perform lookups of assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_bank_view(self):
        """A complete view of the ``Assessment`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_ids_by_bank(self, bank_id):
        """Gets the list of ``Assessment``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessments_by_bank(self, bank_id):
        """Gets the list of ``Assessments`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessments
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    @abc.abstractmethod
    def get_assessment_ids_by_banks(self, bank_ids):
        """Gets the list of ``Assessment Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessments_by_banks(self, bank_ids):
        """Gets the list of ``Assessments`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessments
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    @abc.abstractmethod
    def get_bank_ids_by_assessment(self, assessment_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``Assessment``.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_assessment(self, assessment_id):
        """Gets the list of ``Banks`` mapped to an ``Assessment``.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class AssessmentBankAssignmentSession:
    """This session provides methods to re-assign ``Assessments`` to ``Banks``.

    An ``Assessment`` may map to multiple ``Banks`` and removing the
    last reference to an ``Assessment`` is the equivalent of deleting
    it. Each ``Bank`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of an ``Assessment`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_assessments(self):
        """Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_assessments_to_bank(self, bank_id):
        """Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given banks node in which any assessment can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_assessment(self, bank_id, assessment_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_assessment_to_bank(self, assessment_id, bank_id):
        """Adds an existing ``Assessment`` to a ``Bank``.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_assessment_from_bank(self, assessment_id, bank_id):
        """Removes an ``Assessment`` from a ``Bank``.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``bank_id`` not found or ``assessment_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_assessment_to_billing(self, assessment_id, from_bank_id, to_bank_id):
        """Moves an ``Assessment`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``AssessmentQuery`` can be retrieved from this session and mapped
    to this ``Bank`` to create a virtual collection of ``Assessments``.
    The assessments may be sequenced using the ``AssessmentSearchOrder``
    from this session.

    This ``Bank`` has a default query that matches any assessment and a
    default search order that specifies no sequencing. The queries may
    be examined using an ``AssessmentQueryInspector``. The query may be
    modified by converting the inspector back to an ``AssessmentQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets an assessment query.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def get_assessment_search_order(self):
        """Gets an assessment search order.

        :return: the assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentSearchOrder

    assessment_search_order = property(fget=get_assessment_search_order)

    @abc.abstractmethod
    def apply_assessment_query(self, assessment_query):
        """Applies an assessment query to this bank.

        :param assessment_query: the assessment query
        :type assessment_query: ``osid.assessment.AssessmentQuery``
        :raise: ``NullArgument`` -- ``assessment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_assessment_query(self):
        """Gets an assessment query inspector for this bank.

        :return: the assessment query inspector
        :rtype: ``osid.assessment.AssessmentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    @abc.abstractmethod
    def apply_assessment_sequencing(self, assessment_search_order):
        """Applies an assessment search order to this bank.

        :param assessment_search_order: the assessment search order
        :type assessment_search_order: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_query_from_inspector(self, assessment_query_inspector):
        """Gets an assessment query from an inspector.

        :param assessment_query_inspector: an assessment query inspector
        :type assessment_query_inspector: ``osid.assessment.AssessmentQueryInspector``
        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``NullArgument`` -- ``assessment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQuery


class AssessmentBasicAuthoringSession:
    """This session defines methods to manage assessment items in an assessment.

    This session is used for simple assessments without sections or
    parts. Updating the items on an assessment authored with sections
    and parts may result in an error.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_author_assessments(self):
        """Tests if this user can author assessments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        authoring operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_items(self, assessment_id):
        """Gets the items in sequence from an assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``assessmentid`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def add_item(self, assessment_id, item_id):
        """Adds an existing ``Item`` to an assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``item_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_item(self, assessment_id, item_id):
        """Removes an ``Item`` from this assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``item_id`` not found or ``item_id`` not on ``assessmentid``
        :raise: ``NullArgument`` -- ``assessment_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def move_item(self, assessment_id, item_id, preceeding_item_id):
        """Moves an existing item to follow another item in an assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param item_id: the ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :param preceeding_item_id: the ``Id`` of a preceeding ``Item`` in the sequence
        :type preceeding_item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` is not found, or ``item_id`` or ``preceeding_item_id`` not on ``assessment_id``
        :raise: ``NullArgument`` -- ``assessment_id, item_id`` or ``preceeding_item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_items(self, item_ids, assessment_id):
        """Sequences existing items in an assessment.

        :param item_ids: the ``Id`` of the ``Items``
        :type item_ids: ``osid.id.Id[]``
        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` is not found or an ``item_id`` is not on ``assessment_id``
        :raise: ``NullArgument`` -- ``assessment_id`` or ``item_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentOfferedLookupSession:
    """This session defines methods for retrieving assessments offered."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_assessments_offered(self):
        """Tests if this user can perform ``AssessmentOffered`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_assessment_offered_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_assessment_offered_view(self):
        """A complete view of the ``AssessmentOffered`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_offered(self, assessment_offered_id):
        """Gets the ``AssessmentOffered`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentOffered`` may have
        a different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentOffered`` and
        retained for compatibility.

        :param assessment_offered_id: ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the assessment offered
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``NotFound`` -- ``assessment_offered_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.AssessmentOffered

    @abc.abstractmethod
    def get_assessments_offered_by_ids(self, assessment_offered_ids):
        """Gets an ``AssessmentOfferedList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentOffered`` objects may be omitted from
        the list and may present the elements in any order including
        returning a unique set.

        :param assessment_offered_ids: the list of ``Ids`` to retrieve
        :type assessment_offered_ids: ``osid.id.IdList``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessments_offered_by_genus_type(self, assessment_offered_genus_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus ``Type`` which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param assessment_offered_genus_type: an assessment offered genus type
        :type assessment_offered_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessments_offered_by_parent_genus_type(self, assessment_offered_genus_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments offered that are accessible
        through this session.

        :param assessment_offered_genus_type: an assessment offered genus type
        :type assessment_offered_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessments_offered_by_record_type(self, assessment_record_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param assessment_record_type: an assessment offered record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessments_offered_by_date(self, start, end):
        """Gets an ``AssessmentOfferedList`` that have designated start times where the start times fall in the given range inclusive.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param start: start of time range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of time range
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessments_offered_for_assessment(self, assessment_id):
        """Gets an ``AssessmentOfferedList`` by the given assessment.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessments_offered(self):
        """Gets all ``AssessmentOffered`` elements.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :return: a list of ``AssessmentOffered`` elements
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    assessments_offered = property(fget=get_assessments_offered)


class AssessmentOfferedQuerySession:
    """This session provides methods for querying ``AssessmentOffered`` objects.

    The search query is constructed using the
    ``AssessmentOfferedQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessments offered in
        banks of which this bank is a ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments
        offered in this bank


    Asessments offered may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``AssessmentOfferedQuery``. The returns in this session may not be
    cast directly to these interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_assessments_offered(self):
        """Tests if this user can perform ``AssessmentOffered`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments offered in banks which
        are children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_offered_query(self):
        """Gets an assessment offered query.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQuery

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @abc.abstractmethod
    def get_assessments_offered_by_query(self, assessment_offered_query):
        """Gets a list of ``AssessmentOffered`` elements matching the given assessment offered query.

        :param assessment_offered_query: the assessment offered query
        :type assessment_offered_query: ``osid.assessment.AssessmentOfferedQuery``
        :return: the returned ``AssessmentOfferedList``
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList


class AssessmentOfferedSearchSession:
    """This session provides methods for searching among ``AssessmentOffered`` objects.

    The search query is constructed using the
    ``AssessmentOfferedQuery``.

    ``get_assessments_offered_by_query()`` is the basic search method
    and returns a list of ``AssessmentOffered`` elements. A more
    advanced search may be performed with
    ``getAssessmentsOfferedBySearch()``. It accepts an
    ``AssessmentOfferedSearch`` in addition to the query for the purpose
    of specifying additional options affecting the entire search, such
    as ordering. ``get_assessments_offered_by_search()`` returns an
    ``AssessmentOfferedSearchResults`` that can be used to access the
    resulting ``AssessmentOfferedList`` or be used to perform a search
    within the result set through ``AssessmentOfferedSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessments offered in
        banks of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments
        offered in this bank


    Assessments offered may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``AssessmentOfferedQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_offered_search(self):
        """Gets an assessment offered search.

        :return: the assessment offered search
        :rtype: ``osid.assessment.AssessmentOfferedSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedSearch

    assessment_offered_search = property(fget=get_assessment_offered_search)

    @abc.abstractmethod
    def get_assessment_offered_search_order(self):
        """Gets an assessment offered search order.

        The ``AssessmentOfferedSearchOrder`` is supplied to an
        ``AssessmentOfferedSearch`` to specify the ordering of results.

        :return: the assessment offered search order
        :rtype: ``osid.assessment.AssessmentOfferedSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedSearchOrder

    assessment_offered_search_order = property(fget=get_assessment_offered_search_order)

    @abc.abstractmethod
    def get_assessments_offered_by_search(self, assessment_offered_query, assessment_offered_search):
        """Gets the search results matching the given search query using the given search.

        :param assessment_offered_query: the assessment offered query
        :type assessment_offered_query: ``osid.assessment.AssessmentOfferedQuery``
        :param assessment_offered_search: the assessment offered search
        :type assessment_offered_search: ``osid.assessment.AssessmentOfferedSearch``
        :return: the assessment offered search results
        :rtype: ``osid.assessment.AssessmentOfferedSearchResults``
        :raise: ``NullArgument`` -- ``assessment_offered_query`` or ``assessment_offered_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_query`` or ``assessment_offered_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedSearchResults

    @abc.abstractmethod
    def get_assessment_offered_query_from_inspector(self, assessment_offered_query_inspector):
        """Gets an assessment offered query from an inspector.

        The inspector is available from an
        ``AssessmentOfferedSearchResults``.

        :param assessment_offered_query_inspector: an assessment offered query inspector
        :type assessment_offered_query_inspector: ``osid.assessment.AssessmentOfferedQueryInspector``
        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``NullArgument`` -- ``assessment_offered_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_offered_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQuery


class AssessmentOfferedAdminSession:
    """This session creates, updates, and deletes ``AssessmentsOffered``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``AssessmentOffered,`` an ``AssessmentOfferedForm`` is requested
    using ``get_assessment_offered_form_for_create()`` specifying the
    assessment and desired record ``Types`` or none if no record
    ``Types`` are needed. The returned ``AssessmentOfferedForm`` will
    indicate that it is to be used with a create operation and can be
    used to examine metdata or validate data prior to creation. Once the
    ``AssessmentOfferedForm`` is submiited to a create operation, it
    cannot be reused with another create operation unless the first
    operation was unsuccessful. Each ``AssessmentOfferedForm``
    corresponds to an attempted transaction.

    For updates, ``AssessmentOfferedForms`` are requested to the
    ``AssessmentOffered``  ``Id`` that is to be updated using
    ``getAssessmentOfferedFormForUpdate()``. Similarly, the
    ``AssessmentOfferedForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AssessmentOfferedForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``AssessmentsOffered``. To unmap an
    ``AssessmentOffered`` from the current ``Bank,`` the
    ``AssessmentOfferedBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``AssessmentOffered`` itself
    thus removing it from all known ``Bank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_assessments_offered(self):
        """Tests if this user can create ``AssessmentOffered`` objects.

        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``AssessmentOffered`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_assessment_offered_with_record_types(self, assessment_offered_record_types):
        """Tests if this user can create a single ``AssessmentOffered`` using the desired record types.

        While ``AssessmentManager.getAssessmentOfferedRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentOffered``. Providing an empty array tests if an
        ``AssessmentOffered`` can be created with no records.

        :param assessment_offered_record_types: array of assessment offered record types
        :type assessment_offered_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssessmentOffered`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_form_for_create(self, assessment_id, assessment_offered_record_types):
        """Gets the assessment offered form for creating new assessments offered.

        A new form should be requested for each create transaction.

        :param assessment_id: the ``Id`` of the related ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param assessment_offered_record_types: array of assessment offered record types to be included in the create operation or an empty list if none
        :type assessment_offered_record_types: ``osid.type.Type[]``
        :return: the assessment offered form
        :rtype: ``osid.assessment.AssessmentOfferedForm``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``assessment_offered_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedForm

    @abc.abstractmethod
    def create_assessment_offered(self, assessment_offered_form):
        """Creates a new ``AssessmentOffered``.

        :param assessment_offered_form: the form for this ``AssessmentOffered``
        :type assessment_offered_form: ``osid.assessment.AssessmentOfferedForm``
        :return: the new ``AssessmentOffered``
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``IllegalState`` -- ``assessment_offrered_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``assessment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form`` did not originate from ``get_assessment_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOffered

    @abc.abstractmethod
    def can_update_assessments_offered(self):
        """Tests if this user can update ``AssessmentOffered`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_form_for_update(self, assessment_offered_id):
        """Gets the assessment offered form for updating an existing assessment offered.

        A new assessment offered form should be requested for each
        update transaction.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the assessment offered form
        :rtype: ``osid.assessment.AssessmentOfferedForm``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedForm

    @abc.abstractmethod
    def update_assessment_offered(self, assessment_offered_form):
        """Updates an existing assessment offered.

        :param assessment_offered_form: the form containing the elements to be updated
        :type assessment_offered_form: ``osid.assessment.AssessmentOfferedForm``
        :raise: ``IllegalState`` -- ``assessment_offrered_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``assessment_offered_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form`` did not originate from ``get_assessment_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_assessments_offered(self):
        """Tests if this user can delete ``AssessmentsOffered``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        :return: ``false`` if ``AssessmentOffered`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_assessment_offered(self, assessment_offered_id):
        """Deletes an ``AssessmentOffered``.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to remove
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_assessment_offered_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentsOffered``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``AssessmentOffered`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_assessment_offered(self, assessment_offered_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentOffered`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentOffered`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment offered, it is
        reassigned to the given assessment offered ``Id``.

        :param assessment_offered_id: the ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentOfferedNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``AssessmentOffered`` objects in this ``Bank``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``AssessmentOfferedLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_assessment_offered_notifications(self):
        """Tests if this user can register for ``AssessmentOffered`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for assessments
        offered in banks which are children of this bank in the bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for assessments offered
        to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_offered_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_offered_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_offered_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_offered_notification(self, notification_id):
        """Acknowledge an assessment offered notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments_offered(self):
        """Register for notifications of new assessments offered.

        ``AssessmentOfferedReceiver.newAssessmentsOffered()`` is invoked
        when a new ``AssessmentOffered`` appears in this assessmen
        tbank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments_offered_for_assessment(self, assessment_id):
        """Register for notifications of new assessments offered by assessment.

        ``AssessmentOfferedReceiver.newAssessmentsOffered()`` is invoked
        when a new ``AssessmentOffered`` appears in this assessment
        bank.

        :param assessment_id: ``Id`` of an assessment to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments_offered(self):
        """Registers for notification of updated assessments offered.

        ``AssessmentOfferedReceiver.changedAssessmentsOffered()`` is
        invoked when an assessment offered in this assessment bank is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments_offered_for_assessment(self, assessment_id):
        """Register for notifications of updated assessments offered by assessment.

        ``AssessmentOfferedReceiver.changedAssessmentsOffered()`` is
        invoked when an ``AssessmentOffered`` in this assessment bank is
        changed.

        :param assessment_id: ``Id`` of an assessment to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessment_offered(self, assessment_offered_id):
        """Registers for notification of an updated assessment offered.

        ``AssessmentOfferedReceiver.changedAssessmentsOffered()`` is
        invoked when the specified assessment offered in this assessment
        bank is changed.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments_offered(self):
        """Registers for notification of deleted assessments offered.

        ``AssessmentOfferedReceiver.deletedAssessmentsOffered()`` is
        invoked when an assessment offered is removed from the
        assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments_offered_for_assessment(self, assessment_id):
        """Register for notifications of deleted assessments offered by assessment.

        ``AssessmentOfferedReceiver.deletedAssessmenstOffered()`` is
        invoked when an ``AssessmentOffered`` is removed form the
        assessment bank.

        :param assessment_id: ``Id`` of an assessment to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessment_offered(self, assessment_offered_id):
        """Registers for notification of a deleted assessment offered.

        ``AssessmentOfferedReceiver.deletedAssessmentsOffered()`` is
        invoked when the specified assessment offered is removed from
        the assessment bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_offered_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_offered_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_offered_notification(self, notification_id):
        """Acknowledge an assessment_offered notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentOfferedBankSession:
    """This session provides methods to retrieve ``AssessmentOffered`` to ``Bank`` mappings.

    An ``AssessmentOffered`` may appear in multiple ``Banks``. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_assessment_offered_bank_mappings(self):
        """Tests if this user can perform lookups of assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_bank_view(self):
        """A complete view of the ``AssessmentOffered`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_offered_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentOffered``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment offered ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessments_offered_by_bank(self, bank_id):
        """Gets the list of ``AssessmentOffereds`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessments offered
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_assessment_offered_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentOffered Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessments_offered_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentOffered`` objects corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessments offered
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    @abc.abstractmethod
    def get_bank_ids_by_assessment_offered(self, assessment_offered_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentOffered``.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_assessment_offered(self, assessment_offered_id):
        """Gets the list of ``Banks`` mapped to an ``AssessmentOffered``.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class AssessmentOfferedBankAssignmentSession:
    """This session provides methods to re-assign ``AssessmentOffered`` objects to ``Banks``.

    An ``AssessmentOffered`` may map to multiple ``Banks`` and removing
    the last reference to an ``AssessmentOffered`` is the equivalent of
    deleting it. Each ``Bank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``AssessmentOffered`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_assessments_offered(self):
        """Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_assessments_offered_to_bank(self, bank_id):
        """Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given banks node in which any assessment offered can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_assessment_offered(self, bank_id, assessment_offered_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment offered can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_assessment_offered_to_bank(self, assessment_offered_id, bank_id):
        """Adds an existing ``AssessmentOffered`` to a ``Bank``.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_offered_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_assessment_offered_from_bank(self, assessment_offered_id, bank_id):
        """Removes an ``AssessmentOffered`` from a ``Bank``.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` or ``bank_id`` not found or ``assessment_offered_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_assessment_offered_to_billing(self, assessment_offered_id, from_bank_id, to_bank_id):
        """Moves an ``AssessmentOffered`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_offered_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_offered_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_offered_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentOfferedSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``AssessmentOfferedQuery`` can be retrieved from this session and
    mapped to this ``Bank`` to create a virtual collection of
    ``AssessmentsOffered``. The assessments may be sequenced using the
    ``AssessmentSearchOrder`` from this session.

    This ``Bank`` has a default query that matches any assessment and a
    default search order that specifies no sequencing. The queries may
    be examined using an ``AssessmentOfferedQueryInspector``. The query
    may be modified by converting the inspector back to an
    ``AssessmentOfferedQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_offered_query(self):
        """Gets an assessment offered query.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQuery

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @abc.abstractmethod
    def get_assessment_offered_search_order(self):
        """Gets an assessment offered search order.

        :return: the assessment offered search order
        :rtype: ``osid.assessment.AssessmentOfferedSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedSearchOrder

    assessment_offered_search_order = property(fget=get_assessment_offered_search_order)

    @abc.abstractmethod
    def apply_assessment_offered_query(self, assessment_offered_query):
        """Applies an assessment offered query to this bank.

        :param assessment_offered_query: the assessment offered query
        :type assessment_offered_query: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``NullArgument`` -- ``assessment_offered_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_assessment_offered_query(self):
        """Gets an assessment offered query inspector for this bank.

        :return: the assessment offered query inspector
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQueryInspector

    @abc.abstractmethod
    def apply_assessment_offered_sequencing(self, assessment_offered_search_order):
        """Applies an assessment offered search order to this bank.

        :param assessment_offered_search_order: the assessment offered search order
        :type assessment_offered_search_order: ``osid.assessment.AssessmentOfferedSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_offered_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_offered_query_from_inspector(self, assessment_offered_query_inspector):
        """Gets an assessment offered query from an inspector.

        :param assessment_offered_query_inspector: a assessment offered query inspector
        :type assessment_offered_query_inspector: ``osid.assessment.AssessmentOfferedQueryInspector``
        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``NullArgument`` -- ``assessment_offered_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_offered_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQuery


class AssessmentTakenLookupSession:
    """This session defines methods for retrieving assessments taken."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_assessments_taken(self):
        """Tests if this user can perform ``AssessmentTaken`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_assessment_taken_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_assessment_taken_view(self):
        """A complete view of the ``AssessmentTaken`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_taken(self, assessment_taken_id):
        """Gets the ``AssessmentTaken`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentTaken`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentTaken`` and
        retained for compatibility.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the assessment taken
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``NotFound`` -- ``assessment_taken_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.AssessmentTaken

    @abc.abstractmethod
    def get_assessments_taken_by_ids(self, assessment_taken_ids):
        """Gets an ``AssessmentTakenList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentTaken`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param assessment_taken_ids: the list of ``Ids`` to retrieve
        :type assessment_taken_ids: ``osid.id.IdList``
        :return: the returned ``AssessmentTaken list``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_genus_type(self, assessment_taken_genus_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type`` which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_taken_genus_type: an assessment taken genus type
        :type assessment_taken_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentTaken list``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_parent_genus_type(self, assessment_taken_genus_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments taken that are accessible
        through this session.

        :param assessment_taken_genus_type: an assessment taken genus type
        :type assessment_taken_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentTaken list``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_record_type(self, assessment_taken_record_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        :param assessment_taken_record_type: an assessment taken record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_date(self, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_for_taker(self, resource_id):
        """Gets an ``AssessmentTakenList`` for the given resource.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_date_for_taker(self, resource_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_for_assessment(self, assessment_id):
        """Gets an ``AssessmentTakenList`` for the given assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_date_for_assessment(self, assessment_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``assessment_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_for_taker_and_assessment(self, resource_id, assessment_id):
        """Gets an ``AssessmentTakenList`` for the given resource and assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_date_for_taker_and_assessment(self, resource_id, assessment_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource and assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, assessment_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Gets an ``AssessmentTakenList`` by the given assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_date_for_assessment_offered(self, assessment_offered_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``assessment_offered_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id):
        """Gets an ``AssessmentTakenList`` for the given resource and assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``assessmen_offeredt_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken_by_date_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource and assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, assessment_offered_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessments_taken(self):
        """Gets all ``AssessmentTaken`` elements.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :return: a list of ``AssessmentTaken`` elements
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    assessments_taken = property(fget=get_assessments_taken)


class AssessmentTakenQuerySession:
    """This session provides methods for searching among ``AssessmentTaken`` objects.

    The search query is constructed using the ``AssessmentTakenQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessments taken in banks
        of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments taken
        in this bank


    Assessments taken may have a query record indicated by their
    respective query record types. The query record is accessed via the
    ``AssessmentTakenQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_assessments_taken(self):
        """Tests if this user can perform ``AssessmentTaken`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments taken in banks which
        are children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_taken_query(self):
        """Gets an assessment taken query.

        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQuery

    assessment_taken_query = property(fget=get_assessment_taken_query)

    @abc.abstractmethod
    def get_assessments_taken_by_query(self, assessment_taken_query):
        """Gets a list of ``AssessmentTaken`` elements matching the given assessment taken query.

        :param assessment_taken_query: the assessment taken query
        :type assessment_taken_query: ``osid.assessment.AssessmentTakenQuery``
        :return: the returned ``AssessmentTakenList``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList


class AssessmentTakenSearchSession:
    """This session provides methods for searching among ``AssessmentTaken`` objects.

    The search query is constructed using the ``AssessmentTakenQuery``.

    ``get_assessments_taken_by_query()`` is the basic search method and
    returns a list of ``AssessmentTaken`` elements. A more advanced
    search may be performed with ``getAssessmentsTakenBySearch()``. It
    accepts an ``AssessmentTakenSearch`` in addition to the query for
    the purpose of specifying additional options affecting the entire
    search, such as ordering. ``get_assessments_taken_by_search()``
    returns an ``AssessmentTakenSearchResults`` that can be used to
    access the resulting ``AssessmenTakenList`` or be used to perform a
    search within the result set through ``AssessmentTakenSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessments taken in banks
        of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments taken
        in this bank


    Assessments taken may have query records indicated by their
    respective record types. The query record is accessed via the
    ``AssessmentTakenQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_taken_search(self):
        """Gets an assessment taken search.

        :return: the assessment taken search
        :rtype: ``osid.assessment.AssessmentTakenSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenSearch

    assessment_taken_search = property(fget=get_assessment_taken_search)

    @abc.abstractmethod
    def get_assessment_taken_search_order(self):
        """Gets an assessment taken search order.

        The ``AssessmentTakenSearchOrder`` is supplied to an
        ``AssessmentTakenSearch`` to specify the ordering of results.

        :return: the assessment taken search order
        :rtype: ``osid.assessment.AssessmentTakenSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenSearchOrder

    assessment_taken_search_order = property(fget=get_assessment_taken_search_order)

    @abc.abstractmethod
    def get_assessments_taken_by_search(self, assessment_taken_query, assessment_taken_search):
        """Gets the search results matching the given search query using the given assessment taken query.

        :param assessment_taken_query: the assessment taken query
        :type assessment_taken_query: ``osid.assessment.AssessmentTakenQuery``
        :param assessment_taken_search: the assessment taken search
        :type assessment_taken_search: ``osid.assessment.AssessmentTakenSearch``
        :return: the assessment taken search results
        :rtype: ``osid.assessment.AssessmentTakenSearchResults``
        :raise: ``NullArgument`` -- ``assessment_taken_query`` or ``assessment_taken_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_query`` or ``assessment_taken_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenSearchResults

    @abc.abstractmethod
    def get_assessment_taken_query_from_inspector(self, assessment_taken_query_inspector):
        """Gets an assessment taken query from an inspector.

        The inspector is available from an
        ``AssessmentTakenSearchResults``.

        :param assessment_taken_query_inspector: an assessment taken query inspector
        :type assessment_taken_query_inspector: ``osid.assessment.AssessmentTakenQueryInspector``
        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``NullArgument`` -- ``assessment_taken_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_taken_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQuery


class AssessmentTakenAdminSession:
    """This session creates, updates, and deletes ``AssessmentsTaken``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``AssessmentTaken,`` an ``AssessmentTakenForm`` is requested using
    ``get_assessment_taken_form_for_create()`` specifying the assessment
    offered and desired record ``Types`` or none if no record ``Types``
    are needed. The returned ``AssessmentTakenForm`` will indicate that
    it is to be used with a create operation and can be used to examine
    metdata or validate data prior to creation. Once the
    ``AssessmentTakenForm`` is submiited to a create operation, it
    cannot be reused with another create operation unless the first
    operation was unsuccessful. Each ``AssessmentTakenForm`` corresponds
    to an attempted transaction.

    For updates, ``AssessmentTakenForms`` are requested to the
    ``AssessmentTaken``  ``Id`` that is to be updated using
    ``getAssessmentTakenFormForUpdate()``. Similarly, the
    ``AssessmentTakenForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AssessmentTakenForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``AssessmentsTaken``. To unmap an
    ``AssessmentTakenForm`` from the current ``Bank,`` the
    ``AssessmentTakenFormBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``AssessmentTakenForm``
    itself thus removing it from all known ``Bank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_assessments_taken(self):
        """Tests if this user can create ``AssessmentTaken`` objects.

        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``AssessmentTaken`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_assessment_taken_with_record_types(self, assessment_taken_record_types):
        """Tests if this user can create a single ``AssessmentTaken`` using the desired record types.

        While ``AssessmentManager.getAssessmentTakenRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentTaken``. Providing an empty array tests if an
        ``AssessmentTaken`` can be created with no records.

        :param assessment_taken_record_types: array of assessment taken record types
        :type assessment_taken_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssessmentTaken`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_form_for_create(self, assessment_offered_id, assessment_taken_record_types):
        """Gets the assessment taken form for creating new assessments taken.

        A new form should be requested for each create transaction.

        :param assessment_offered_id: the ``Id`` of the related ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param assessment_taken_record_types: array of assessment taken record types to be included in the create operation or an empty list if none
        :type assessment_taken_record_types: ``osid.type.Type[]``
        :return: the assessment taken form
        :rtype: ``osid.assessment.AssessmentTakenForm``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``assessment_taken_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenForm

    @abc.abstractmethod
    def create_assessment_taken(self, assessment_taken_form):
        """Creates a new ``AssessmentTaken``.

        :param assessment_taken_form: the form for this ``AssessmentTaken``
        :type assessment_taken_form: ``osid.assessment.AssessmentTakenForm``
        :return: the new ``AssessmentTaken``
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``IllegalState`` -- ``assessment_taken_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``assessment_taken_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_form`` did not originate from ``get_assessment_taken_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTaken

    @abc.abstractmethod
    def can_update_assessments_taken(self):
        """Tests if this user can update ``AssessmentTaken`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``AssessmentTaken`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_form_for_update(self, assessment_taken_id):
        """Gets the assessment taken form for updating an existing assessment taken.

        A new assessment taken form should be requested for each update
        transaction.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the assessment taken form
        :rtype: ``osid.assessment.AssessmentTakenForm``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenForm

    @abc.abstractmethod
    def update_assessment_taken(self, assessment_taken_form):
        """Updates an existing assessment taken.

        :param assessment_taken_form: the form containing the elements to be updated
        :type assessment_taken_form: ``osid.assessment.AssessmentTakenForm``
        :raise: ``IllegalState`` -- ``assessment_taken_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``assessment_taken_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_form`` did not originate from ``get_assessment_taken_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_assessments_taken(self):
        """Tests if this user can delete ``AssessmentsTaken``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        :return: ``false`` if ``AssessmentTaken`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_assessment_taken(self, assessment_taken_id):
        """Deletes an ``AssessmentTaken``.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken`` to remove
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_assessment_taken_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentsTaken``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``AssessmentTaken`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_assessment_taken(self, assessment_taken_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentTaken`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentTaken`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment taken, it is
        reassigned to the given assessment taken ``Id``.

        :param assessment_taken_id: the ``Id`` of an ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentTakenNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``AssessmentTaken`` objects in this ``Bank``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``AssessmentTakenLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_assessment_taken_notifications(self):
        """Tests if this user can register for ``AssessmentTaken`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for assessments
        taken in banks which are children of this bank in the bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for assessments taken
        to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_taken_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_taken_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_taken_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_taken_notification(self, notification_id):
        """Acknowledge an assessment taken notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments_taken(self):
        """Register for notifications of new assessments taken in this assessment bank.

        ``AssessmentTakenReceiver.newAssessmentsTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments_taken_for_taker(self, resource_id):
        """Register for notifications of new assessments taken for a resource.

        ``AssessmentTakenReceiver.newAssessmenstTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Register for notifications of new assessments taken for an assessment offered.

        ``AssessmentTakenReceiver.newAssessmentsTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessments_taken_for_assessment(self, assessment_id):
        """Register for notifications of new assessments taken for an assessment.

        ``AssessmentTakenReceiver.newAssessmentsTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments_taken(self):
        """Registers for notification of updated assessments taken.

        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an assessment taken in this assessment bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments_taken_for_taker(self, resource_id):
        """Register for notifications of changed assessments taken for a resource.

        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is changed in this assessment bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Register for notifications of changed assessments taken for an assessment offered.

        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is changed in this assessment bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessments_taken_for_assessment(self, assessment_id):
        """Register for notifications of changed assessments taken for an assessment.

        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is changed in this assessment bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessment_taken(self, assessment_taken_id):
        """Registers for notification of an updated assessment taken.

        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when the specified assessment taken in this assessment bank is
        changed.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken`` to monitor
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments_taken(self):
        """Registers for notification of deleted assessments taken.

        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an assessment taken is removed from this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments_taken_for_taker(self, resource_id):
        """Register for notifications of deleted assessments taken for a resource.

        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is removed from this assessment
        bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Register for notifications of deleted assessments taken for an assessment offered.

        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is removed from this assessment
        bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessments_taken_for_assessment(self, assessment_id):
        """Register for notifications of deleted assessments taken for an assessment.

        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is removed from this assessment
        bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessment_taken(self, assessment_taken_id):
        """Registers for notification of a deleted assessment taken.

        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when the specified assessment taken is removed from this
        assessment bank.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken`` to monitor
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_taken_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_taken_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_taken_notification(self, notification_id):
        """Acknowledge an assessment_taken notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentTakenBankSession:
    """This session provides methods to retrieve ``AssessmentTaken`` to ``Bank`` mappings.

    An ``AssessmentTaken`` may appear in multiple ``Banks``. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_assessment_taken_bank_mappings(self):
        """Tests if this user can perform lookups of assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_bank_view(self):
        """A complete view of the ``AssessmentTaken`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_taken_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentTaken``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment taken ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessments_taken_by_bank(self, bank_id):
        """Gets the list of ``AssessmentTakens`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessments taken
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_assessment_taken_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentTaken Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessments_taken_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentTaken`` objects corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessments taken
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    @abc.abstractmethod
    def get_bank_ids_by_assessment_taken(self, assessment_taken_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentTaken``.

        :param assessment_taken_id: ``Id`` of an ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_assessment_taken(self, assessment_taken_id):
        """Gets the list of ``Banks`` mapped to an ``AssessmentTaken``.

        :param assessment_taken_id: ``Id`` of an ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class AssessmentTakenBankAssignmentSession:
    """This session provides methods to re-assign ``AssessmentTaken`` objects to ``Banks``.

    An ``AssessmentTaken`` may map to multiple ``Banks`` and removing
    the last reference to an ``AssessmentTaken`` is the equivalent of
    deleting it. Each ``Bank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``AssessmentTaken`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_assessments_taken(self):
        """Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_assessments_taken_to_bank(self, bank_id):
        """Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given banks node in which any assessment taken can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_assessment_taken(self, bank_id, assessment_taken_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment taken can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_assessment_taken_to_bank(self, assessment_taken_id, bank_id):
        """Adds an existing ``AssessmentTaken`` to a ``Bank``.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_taken_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_assessment_taken_from_bank(self, assessment_taken_id, bank_id):
        """Removes an ``AssessmentTaken`` from a ``Bank``.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` or ``bank_id`` not found or ``assessment_taken_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_assessment_taken_to_billing(self, assessment_taken_id, from_bank_id, to_bank_id):
        """Moves an ``AssessmentTaken`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_taken_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_taken_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_taken_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentTakenSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``AssessmentTakenQuery`` can be retrieved from this session and
    mapped to this ``Bank`` to create a virtual collection of
    ``AssessmentsTaken``. The assessments may be sequenced using the
    ``AssessmentSearchOrder`` from this session.

    This ``Bank`` has a default query that matches any assessment and a
    default search order that specifies no sequencing. The queries may
    be examined using an ``AssessmentTakenQueryInspector``. The query
    may be modified by converting the inspector back to an
    ``AssessmentTakenQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_taken_query(self):
        """Gets an assessment taken query.

        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQuery

    assessment_taken_query = property(fget=get_assessment_taken_query)

    @abc.abstractmethod
    def get_assessment_taken_search_order(self):
        """Gets an assessment taken search order.

        :return: the assessment taken search order
        :rtype: ``osid.assessment.AssessmentTakenSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenSearchOrder

    assessment_taken_search_order = property(fget=get_assessment_taken_search_order)

    @abc.abstractmethod
    def apply_assessment_taken_query(self, assessment_taken_query):
        """Applies an assessment taken query to this bank.

        :param assessment_taken_query: the assessment taken query
        :type assessment_taken_query: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``NullArgument`` -- ``assessment_taken_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_assessment_taken_query(self):
        """Gets an assessment taken query inspector for this bank.

        :return: the assessment taken query inspector
        :rtype: ``osid.assessment.AssessmentTakenQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQueryInspector

    @abc.abstractmethod
    def apply_assessment_taken_sequencing(self, assessment_taken_search_order):
        """Applies an assessment taken search order to this bank.

        :param assessment_taken_search_order: the assessment taken search order
        :type assessment_taken_search_order: ``osid.assessment.AssessmentTakenSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_taken_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_taken_query_from_inspector(self, assessmen_taken_query_inspector):
        """Gets an assessment taken query from an inspector.

        :param assessmen_taken_query_inspector: a assessment taen query inspector
        :type assessmen_taken_query_inspector: ``osid.assessment.AssessmentTakenQueryInspector``
        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``NullArgument`` -- ``assessmen_taken_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessmen_taken_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQuery


class BankLookupSession:
    """This session provides methods for retrieving ``Bank`` objects.

    The ``Bank`` represents a collection of ``Items`` and
    ``Assessments``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Banks`` it can access, without breaking execution.
    However, an administrative application may require all ``Bank``
    elements to be available.

    Banks may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Bank``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_banks(self):
        """Tests if this user can perform ``Bank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_bank_view(self):
        """A complete view of the ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_bank(self, bank_id):
        """Gets the ``Bank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bank`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bank`` and retained for compatibility.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.Bank

    @abc.abstractmethod
    def get_banks_by_ids(self, bank_ids):
        """Gets a ``BankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the banks
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bank`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param bank_ids: the list of ``Ids`` to retrieve
        :type bank_ids: ``osid.id.IdList``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def get_banks_by_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` which does not include banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param bank_genus_type: a bank genus type
        :type bank_genus_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def get_banks_by_parent_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` and include any additional banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param bank_genus_type: a bank genus type
        :type bank_genus_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def get_banks_by_record_type(self, bank_record_type):
        """Gets a ``BankList`` containing the given bank record ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def get_banks_by_provider(self, resource_id):
        """Gets a ``BankList`` from the given provider ````.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def get_banks(self):
        """Gets all ``Banks``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :return: a ``BankList``
        :rtype: ``osid.assessment.BankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    banks = property(fget=get_banks)


class BankQuerySession:
    """This session provides methods for searching among ``Bank`` objects.

    The search query is constructed using the ``BankQuery``.

    Banks may have aquery record indicated by their respective record
    types. The query record is accessed via the ``BankQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_banks(self):
        """Tests if this user can perform ``Bank`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_query(self):
        """Gets a bank query.

        :return: a bank query
        :rtype: ``osid.assessment.BankQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    @abc.abstractmethod
    def get_banks_by_query(self, bank_query):
        """Gets a list of ``Bank`` objects matching the given bank query.

        :param bank_query: the bank query
        :type bank_query: ``osid.assessment.BankQuery``
        :return: the returned ``BankList``
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class BankSearchSession:
    """This session provides methods for searching among ``Bank`` objects.

    The search query is constructed using the ``BankQuery``.

    ``get_banks_by_query()`` is the basic search method and returns a
    list of ``Bank`` objects.A more advanced search may be performed
    with ``getBanksBySearch()``. It accepts a ``BankSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_banks_by_search()`` returns a ``BankSearchResults`` that can
    be used to access the resulting ``BankList`` or be used to perform a
    search within the result set through ``BankSearch``.

    Banks may have a query record indicated by their respective record
    types. The query record is accessed via the ``BankQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_search(self):
        """Gets a bank search.

        :return: a bank search
        :rtype: ``osid.assessment.BankSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankSearch

    bank_search = property(fget=get_bank_search)

    @abc.abstractmethod
    def get_bank_search_order(self):
        """Gets a bank search order.

        The ``BankSearchOrder`` is supplied to a ``BankSearch`` to
        specify the ordering of results.

        :return: the bank search order
        :rtype: ``osid.assessment.BankSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankSearchOrder

    bank_search_order = property(fget=get_bank_search_order)

    @abc.abstractmethod
    def get_banks_by_search(self, bank_query, bank_search):
        """Gets the search results matching the given search query using the given search.

        :param bank_query: the bank query
        :type bank_query: ``osid.assessment.BankQuery``
        :param bank_search: the bank search
        :type bank_search: ``osid.assessment.BankSearch``
        :return: the bank search results
        :rtype: ``osid.assessment.BankSearchResults``
        :raise: ``NullArgument`` -- ``bank_query`` or ``bank_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_query`` or ``bank_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankSearchResults

    @abc.abstractmethod
    def get_bank_query_from_inspector(self, bank_query_inspector):
        """Gets a bank query from an inspector.

        The inspector is available from a ``BankSearchResults``.

        :param bank_query_inspector: a bank query inspector
        :type bank_query_inspector: ``osid.assessment.BankQueryInspector``
        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``NullArgument`` -- ``bank_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``bank_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQuery


class BankAdminSession:
    """This session creates, updates, and deletes ``Banks``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Bank,`` a ``BankForm`` is requested using
    ``get_bank_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BankForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BankForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BankForm`` corresponds
    to an attempted transaction.

    For updates, ``BankForms`` are requested to the ``Bank``  ``Id``
    that is to be updated using ``getBankFormForUpdate()``. Similarly,
    the ``BankForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``BankForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Banks``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_banks(self):
        """Tests if this user can create ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Bank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_bank_with_record_types(self, bank_record_types):
        """Tests if this user can create a single ``Bank`` using the desired record types.

        While ``AssessmentManager.getBankRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bank``.
        Providing an empty array tests if a ``Bank`` can be created with
        no records.

        :param bank_record_types: array of bank record types
        :type bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Bank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_form_for_create(self, bank_record_types):
        """Gets the bank form for creating new banks.

        A new form should be requested for each create transaction.

        :param bank_record_types: array of bank record types to be included in the create operation or an empty list if none
        :type bank_record_types: ``osid.type.Type[]``
        :return: the bank form
        :rtype: ``osid.assessment.BankForm``
        :raise: ``NullArgument`` -- ``bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankForm

    @abc.abstractmethod
    def create_bank(self, bank_form):
        """Creates a new ``Bank``.

        :param bank_form: the form for this ``Bank``
        :type bank_form: ``osid.assessment.BankForm``
        :return: the new ``Bank``
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- ``bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_form`` did not originate from ``get_bank_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    @abc.abstractmethod
    def can_update_banks(self):
        """Tests if this user can update ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Bank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_form_for_update(self, bank_id):
        """Gets the bank form for updating an existing bank.

        A new bank form should be requested for each update transaction.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: the bank form
        :rtype: ``osid.assessment.BankForm``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankForm

    @abc.abstractmethod
    def update_bank(self, bank_form):
        """Updates an existing bank.

        :param bank_form: the form containing the elements to be updated
        :type bank_form: ``osid.assessment.BankForm``
        :raise: ``IllegalState`` -- ``bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_form`` did not originate from ``get_bank_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_banks(self):
        """Tests if this user can delete banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Bank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_bank(self, bank_id):
        """Deletes a ``Bank``.

        :param bank_id: the ``Id`` of the ``Bank`` to remove
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Bank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_bank(self, bank_id, alias_id):
        """Adds an ``Id`` to a ``Bank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bank`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another bank, it is reassigned to the
        given bank ``Id``.

        :param bank_id: the ``Id`` of a ``Bank``
        :type bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BankNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Bank`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_bank_notifications(self):
        """Tests if this user can register for ``Bank`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def reliable_bank_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_bank_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_bank_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_bank_notification(self, notification_id):
        """Acknowledge a bank notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_banks(self):
        """Register for notifications of new banks.

        ``BankReceiver.newBanks()`` is invoked when a new Bank is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_banks(self):
        """Registers for notification of updated banks.

        ``BankReceiver.changedBanks()`` is invoked when a bank is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_bank(self, bank_id):
        """Registers for notification of an updated bank.

        ``BankReceiver.changedBanks()`` is invoked when the specified
        bank is changed.

        :param bank_id: the Id of the bank to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_banks(self):
        """Registers for notification of deleted banks.

        ``BankReceiver.deletedBanks()`` is invoked when a bank is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_bank(self, bank_id):
        """Registers for notification of a deleted bank.

        ``BankReceiver.deletedBanks()`` is invoked when the specified
        bank is deleted.

        :param bank_id: the Id of the bank to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_bank_hierarchy(self):
        """Registers for notification of an updated bank hierarchy structure.

        ``BankReceiver.changedChildOfBanks()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_bank_hierarchy_for_ancestors(self, bank_id):
        """Registers for notification of an updated bank hierarchy structure.

        ``BankReceiver.changedChildOfBanks()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param bank_id: the ``Id`` of the ``Bank`` node to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_bank_hierarchy_for_descendants(self, bank_id):
        """Registers for notification of an updated bank hierarchy structure.

        ``BankReceiver.changedChildOfBanks()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param bank_id: the ``Id`` of the ``Bank`` node to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_bank_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_bank_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_bank_notification(self, notification_id):
        """Acknowledge an bank notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BankHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Bank`` objects.

    Each node in the hierarchy is a unique ``Bank``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_banks()`` and ``getChildBanks()``. To relate these
    ``Ids`` to another OSID, ``get_bank_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Bank`` available in the Assessment OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_banks()`` or ``get_child_banks()`` in lieu
    of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: bank elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    @abc.abstractmethod
    def get_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    bank_hierarchy = property(fget=get_bank_hierarchy)

    @abc.abstractmethod
    def can_access_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_bank_view(self):
        """The returns from the bank methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_bank_ids(self):
        """Gets the root bank ``Ids`` in this hierarchy.

        :return: the root bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_bank_ids = property(fget=get_root_bank_ids)

    @abc.abstractmethod
    def get_root_banks(self):
        """Gets the root banks in this bank hierarchy.

        :return: the root banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.BankList

    root_banks = property(fget=get_root_banks)

    @abc.abstractmethod
    def has_parent_banks(self, bank_id):
        """Tests if the ``Bank`` has any parents.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a direct parent of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_bank_ids(self, bank_id):
        """Gets the parent ``Ids`` of the given bank.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_banks(self, bank_id):
        """Gets the parents of the given bank.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: the parents of the bank
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def is_ancestor_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is an ancestor of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_banks(self, bank_id):
        """Tests if a bank has any children.

        :param bank_id: a ``bank_id``
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_bank(self, id_, bank_id):
        """Tests if a bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_bank_ids(self, bank_id):
        """Gets the child ``Ids`` of the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :return: the children of the bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_banks(self, bank_id):
        """Gets the children of the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :return: the children of the bank
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    @abc.abstractmethod
    def is_descendant_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a descendant of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_bank_node_ids(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bank node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_bank_nodes(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bank node
        :rtype: ``osid.assessment.BankNode``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankNode


class BankHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Bank`` objects.

    Each node in the hierarchy is a unique ``Bank``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    @abc.abstractmethod
    def get_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    bank_hierarchy = property(fget=get_bank_hierarchy)

    @abc.abstractmethod
    def can_modify_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_bank(self, bank_id):
        """Adds a root bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_bank(self, bank_id):
        """Removes a root bank from this hierarchy.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_bank(self, bank_id, child_id):
        """Adds a child to a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_bank(self, bank_id, child_id):
        """Removes a child from a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_banks(self, bank_id):
        """Removes all children from a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
