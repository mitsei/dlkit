"""JSON implementations of assessment sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from bson.objectid import ObjectId
from importlib import import_module


from . import objects
from . import queries
from . import searches
from .. import MONGO_LISTENER
from .. import utilities
from ..assessment_authoring import objects as assessment_authoring_objects
from ..id.objects import IdList
from ..osid import sessions as osid_sessions
from ..osid.osid_errors import PermissionDenied
from ..osid.sessions import OsidSession
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import OsidListList
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from ..utilities import get_registry
from .assessment_utilities import check_effective
from .assessment_utilities import get_assessment_part_lookup_session
from .assessment_utilities import get_assessment_section
from .assessment_utilities import get_assessment_section as get_section_util
from .assessment_utilities import get_first_part_id_for_assessment
from .assessment_utilities import get_item_lookup_session
from .objects import ItemList
from .objects import ResponseList
from dlkit.abstract_osid.assessment import sessions as abc_assessment_sessions
from dlkit.abstract_osid.assessment.objects import AnswerForm as ABCAnswerForm
from dlkit.abstract_osid.assessment.objects import AssessmentForm as ABCAssessmentForm
from dlkit.abstract_osid.assessment.objects import AssessmentOfferedForm as ABCAssessmentOfferedForm
from dlkit.abstract_osid.assessment.objects import AssessmentTakenForm as ABCAssessmentTakenForm
from dlkit.abstract_osid.assessment.objects import BankForm as ABCBankForm
from dlkit.abstract_osid.assessment.objects import ItemForm as ABCItemForm
from dlkit.abstract_osid.assessment.objects import QuestionForm as ABCQuestionForm
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.primitives import Type as ABCType
from dlkit.primordium.calendaring.primitives import DateTime


SUBMITTED = True
DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')
COMPARATIVE = 0
PLENARY = 1


class AssessmentSession(abc_assessment_sessions.AssessmentSession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self, catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._assessments_taken = dict()

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_take_assessments(self):
        """Tests if this user can take this assessment section.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        return: (boolean) - ``false`` if assessment methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def has_assessment_begun(self, assessment_taken_id):
        """Tests if this assessment has started.

        An assessment begins from the designated start time if a start
        time is defined. If no start time is defined the assessment may
        begin at any time. Assessment sections cannot be accessed if the
        return for this method is ``false``.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (boolean) - ``true`` if this assessment has begun,
                ``false`` otherwise
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_assessment_taken(assessment_taken_id).has_started()

    @utilities.arguments_not_none
    def is_assessment_over(self, assessment_taken_id):
        """Tests if this assessment is over.

        An assessment is over if ``finished_assessment()`` is invoked or
        the designated finish time has expired.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (boolean) - ``true`` if this assessment is over,
                ``false`` otherwise
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_assessment_taken(assessment_taken_id).has_ended()

    @utilities.arguments_not_none
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

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (boolean) - ``true`` if this synchronous sections are
                required, ``false`` otherwise
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_assessment_taken(assessment_taken_id).get_assessment_offered().are_sections_sequential()

    @utilities.arguments_not_none
    @check_effective
    def get_first_assessment_section(self, assessment_taken_id):
        """Gets the first assessment section in this assesment.

        All assessments have at least one ``AssessmentSection``.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.AssessmentSection) - the first
                assessment section
        raise:  IllegalState - ``has_assessment_begun()`` is ``false``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_taken = self._get_assessment_taken(assessment_taken_id)
        return assessment_taken._get_first_assessment_section()

    @utilities.arguments_not_none
    @check_effective
    def has_next_assessment_section(self, assessment_section_id):
        """Tests if there is a next assessment section in the assessment following the given assessment section ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if there is a next section,
                ``false`` otherwise
        raise:  IllegalState - ``has_assessment_begun()`` is ``false``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            self.get_next_assessment_section(assessment_section_id)
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_next_assessment_section(self, assessment_section_id):
        """Gets the next assessemnt section following the given assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.AssessmentSection) - the next section
        raise:  IllegalState - ``has_next_assessment_section()`` is
                ``false``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_taken = self.get_assessment_section(assessment_section_id)._assessment_taken
        return assessment_taken._get_next_assessment_section(assessment_section_id)

    @utilities.arguments_not_none
    @check_effective
    def has_previous_assessment_section(self, assessment_section_id):
        """Tests if there is a previous assessment section in the assessment following the given assessment section ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if there is a previous assessment
                section, ``false`` otherwise
        raise:  IllegalState - ``has_assessment_begun()`` is ``false``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            self.get_previous_assessment_section(assessment_section_id)
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_previous_assessment_section(self, assessment_section_id):
        """Gets the next assessemnt section following the given assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.AssessmentSection) - the previous
                assessment section
        raise:  IllegalState - ``has_next_assessment_section()`` is
                ``false``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_taken = self.get_assessment_section(assessment_section_id)._assessment_taken
        return assessment_taken._get_previous_assessment_section(assessment_section_id)

    @utilities.arguments_not_none
    @check_effective
    def get_assessment_section(self, assessment_section_id):
        """Gets an assessemnts section by ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.AssessmentSection) - the assessment
                section
        raise:  IllegalState - ``has_assessment_begun()`` is ``false``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_section_util(assessment_section_id, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    @check_effective
    def get_assessment_sections(self, assessment_taken_id):
        """Gets the assessment sections of this assessment.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.AssessmentSectionList) - the list of
                assessment sections
        raise:  IllegalState - ``has_assessment_begun()`` is ``false``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_taken = self._get_assessment_taken(assessment_taken_id)
        return assessment_taken._get_assessment_sections()

    @utilities.arguments_not_none
    def is_assessment_section_complete(self, assessment_section_id):
        """Tests if the all responses have been submitted to this assessment section.

        If ``is_assessment_section_complete()`` is false, then
        ``get_unanswered_questions()`` may return a list of questions
        that can be submitted.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if this assessment section is
                complete, ``false`` otherwise
        raise:  IllegalState - ``is_assessment_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).is_complete()

    @utilities.arguments_not_none
    @check_effective
    def get_incomplete_assessment_sections(self, assessment_taken_id):
        """Gets the incomplete assessment sections of this assessment.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.AssessmentSectionList) - the list of
                incomplete assessment sections
        raise:  IllegalState - ``has_assessment_begun()`` is ``false``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        section_list = []
        for section in self.get_assessment_sections(assessment_taken_id):
            if not section.is_complete():
                section_list.append(section)
        return objects.AssessmentSectionList(section_list, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def has_assessment_section_begun(self, assessment_section_id):
        """Tests if this assessment section has started.

        A section begins from the designated start time if a start time
        is defined. If no start time is defined the section may begin at
        any time. Assessment items cannot be accessed or submitted if
        the return for this method is ``false``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if this assessment section has
                begun, ``false`` otherwise
        raise:  IllegalState - ``has_assessment_begun()`` is ``false or
                is_assessment_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_section_util(assessment_section_id,
                                runtime=self._runtime)._assessment_taken.has_started()

    @utilities.arguments_not_none
    def is_assessment_section_over(self, assessment_section_id):
        """Tests if this assessment section is over.

        An assessment section is over if new or updated responses can
        not be submitted such as the designated finish time has expired.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if this assessment is over,
                ``false`` otherwise
        raise:  IllegalState - ``has_assessmen_sectiont_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_section_util(assessment_section_id,
                                runtime=self._runtime).is_over()

    @utilities.arguments_not_none
    @check_effective
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

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if this synchronous responses are
                required, ``false`` otherwise
        raise:  IllegalState - ``has_assessment_begun()`` is ``false or
                is_assessment_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).are_items_sequential()

    @utilities.arguments_not_none
    @check_effective
    def get_first_question(self, assessment_section_id):
        """Gets the first question in this assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.Question) - the first question
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_first_question()

    @utilities.arguments_not_none
    @check_effective
    def has_next_question(self, assessment_section_id, item_id):
        """Tests if there is a next question following the given question ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (boolean) - ``true`` if there is a next question,
                ``false`` otherwise
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            self.get_next_question(assessment_section_id, item_id)
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_next_question(self, assessment_section_id, item_id):
        """Gets the next question in this assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.Question) - the next question
        raise:  IllegalState - ``has_next_question()`` is ``false``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_next_question(question_id=item_id)

    @utilities.arguments_not_none
    @check_effective
    def has_previous_question(self, assessment_section_id, item_id):
        """Tests if there is a previous question preceeding the given question ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (boolean) - ``true`` if there is a previous question,
                ``false`` otherwise
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            self.get_previous_question(assessment_section_id, item_id)
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_previous_question(self, assessment_section_id, item_id):
        """Gets the previous question in this assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.Question) - the previous question
        raise:  IllegalState - ``has_previous_question()`` is ``false``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_next_question(question_id=item_id, reverse=True)

    @utilities.arguments_not_none
    @check_effective
    def get_question(self, assessment_section_id, item_id):
        """Gets the ``Question`` specified by its ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.Question) - the returned ``Question``
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_question(question_id=item_id)

    @utilities.arguments_not_none
    @check_effective
    def get_questions(self, assessment_section_id):
        """Gets the questions of this assessment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.QuestionList) - the list of assessment
                questions
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Does this want to return a blocking list of available questions?
        return self.get_assessment_section(assessment_section_id).get_questions()

    @utilities.arguments_not_none
    @check_effective
    def get_response_form(self, assessment_section_id, item_id):
        """Gets the response form for submitting an answer.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.AnswerForm) - an answer form
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(item_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')

        # This is a little hack to get the answer record types from the Item's
        # first Answer record types. Should really get it from item genus types somehow:
        record_type_data_sets = get_registry('ANSWER_RECORD_TYPES', self._runtime)
        section = self.get_assessment_section(assessment_section_id)
        # because we're now giving session-unique question IDs
        question = section.get_question(item_id)
        ils = section._get_item_lookup_session()
        real_item_id = Id(question._my_map['itemId'])
        item = ils.get_item(real_item_id)
        item_map = item.object_map
        all_answers = item_map['answers']
        try:
            all_answers += [wa.object_map for wa in item.get_wrong_answers()]
        except AttributeError:
            pass

        answer_record_types = []
        if len(all_answers) > 0:
            for record_type_idstr in all_answers[0]['recordTypeIds']:
                identifier = Id(record_type_idstr).get_identifier()
                if identifier in record_type_data_sets:
                    answer_record_types.append(Type(**record_type_data_sets[identifier]))
        else:
            for record_type_idstr in item_map['question']['recordTypeIds']:
                identifier = Id(record_type_idstr).get_identifier()
                if identifier in record_type_data_sets:
                    answer_record_types.append(Type(**record_type_data_sets[identifier]))
        # Thus endith the hack.

        obj_form = objects.AnswerForm(
            bank_id=self._catalog_id,
            record_types=answer_record_types,
            item_id=item_id,
            catalog_id=self._catalog_id,
            assessment_section_id=assessment_section_id,
            runtime=self._runtime,
            proxy=self._proxy)
        obj_form._for_update = False  # This may be redundant
        self._forms[obj_form.get_id().get_identifier()] = not SUBMITTED
        return obj_form

    @utilities.arguments_not_none
    @check_effective
    def submit_response(self, assessment_section_id, item_id, answer_form):
        """Submits an answer to an item.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        arg:    answer_form (osid.assessment.AnswerForm): the response
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  InvalidArgument - one or more of the elements in the
                form is invalid
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id, item_id,`` or
                ``answer_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``answer_form`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(answer_form, ABCAnswerForm):
            raise errors.InvalidArgument('argument type is not an AnswerForm')

        # OK, so the following should actually NEVER be true. Remove it?
        if answer_form.is_for_update():
            raise errors.InvalidArgument('the AnswerForm is for update only, not submit')
        #

        try:
            if self._forms[answer_form.get_id().get_identifier()] == SUBMITTED:
                raise errors.IllegalState('answer_form already used in a submit transaction')
        except KeyError:
            raise errors.Unsupported('answer_form did not originate from this assessment session')
        if not answer_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        answer_form._my_map['_id'] = ObjectId()
        self.get_assessment_section(assessment_section_id).submit_response(item_id, answer_form)
        self._forms[answer_form.get_id().get_identifier()] = SUBMITTED

    @utilities.arguments_not_none
    @check_effective
    def skip_item(self, assessment_section_id, item_id):
        """Skips an item.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        raise:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # add conditional: if the assessment or part allows us to skip:
        self.get_assessment_section(assessment_section_id).submit_response(item_id, None)

    @utilities.arguments_not_none
    @check_effective
    def is_question_answered(self, assessment_section_id, item_id):
        """Tests if the given item has a response.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (boolean) - ``true`` if this item has a response,
                ``false`` otherwise
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).is_question_answered(item_id)

    @utilities.arguments_not_none
    @check_effective
    def get_unanswered_questions(self, assessment_section_id):
        """Gets the unanswered questions of this assessment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.QuestionList) - the list of questions
                with no rsponses
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_questions(answered=False)

    @utilities.arguments_not_none
    @check_effective
    def has_unanswered_questions(self, assessment_section_id):
        """Tests if there are unanswered questions in this assessment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (boolean) - ``true`` if there are unanswered questions,
                ``false`` otherwise
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # There's probably a more efficient way to implement this:
        return bool(self.get_unanswered_questions(assessment_section_id).available())

    @utilities.arguments_not_none
    @check_effective
    def get_first_unanswered_question(self, assessment_section_id):
        """Gets the first unanswered question in this assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.Question) - the first unanswered
                question
        raise:  IllegalState - ``has_unanswered_questions()`` is
                ``false``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        questions = self.get_unanswered_questions(assessment_section_id)
        if not questions.available():
            raise errors.IllegalState('There are no more unanswered questions available')
        return questions.next()

    @utilities.arguments_not_none
    @check_effective
    def has_next_unanswered_question(self, assessment_section_id, item_id):
        """Tests if there is a next unanswered question following the given question ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (boolean) - ``true`` if there is a next unanswered
                question, ``false`` otherwise
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # There's probably a more efficient way to implement this:
        try:
            self.get_next_unanswered_question(assessment_section_id, item_id)
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_next_unanswered_question(self, assessment_section_id, item_id):
        """Gets the next unanswered question in this assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.Question) - the next unanswered
                question
        raise:  IllegalState - ``has_next_unanswered_question()`` is
                ``false``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Or this could call through to get_next_question in the section
        questions = self.get_unanswered_questions(assessment_section_id)
        for question in questions:
            if question.get_id() == item_id:
                if questions.available():
                    return questions.next()
                else:
                    raise errors.IllegalState('No next unanswered question is available')
        raise errors.NotFound('item_id is not found in Section')

    @utilities.arguments_not_none
    @check_effective
    def has_previous_unanswered_question(self, assessment_section_id, item_id):
        """Tests if there is a previous unanswered question preceeding the given question ``Id``.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (boolean) - ``true`` if there is a previous unanswered
                question, ``false`` otherwise
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # There's probably a more efficient way to implement this:
        try:
            self.get_previous_unanswered_question(assessment_section_id, item_id)
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_previous_unanswered_question(self, assessment_section_id, item_id):
        """Gets the previous unanswered question in this assesment section.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.Question) - the previous unanswered
                question
        raise:  IllegalState - ``has_previous_unanswered_question()`` is
                ``false``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Or this could call through to get_next_question in the section with reverse=True
        questions = self.get_unanswered_questions(assessment_section_id)
        previous_question = questions.next()
        if previous_question.get_id() == item_id:
            raise errors.IllegalState('No previous unanswered question is available')
        for question in questions:
            if question.get_id() == item_id:
                return previous_question
            else:
                previous_question = question
        raise errors.NotFound('item_id is not found in Section')

    @utilities.arguments_not_none
    @check_effective
    def get_response(self, assessment_section_id, item_id):
        """Gets the submitted response to the associated item.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.Response) - the response
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_response(question_id=item_id)

    @utilities.arguments_not_none
    @check_effective
    def get_responses(self, assessment_section_id):
        """Gets all submitted responses.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        return: (osid.assessment.ResponseList) - the list of responses
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_assessment_section(assessment_section_id).get_responses()

    @utilities.arguments_not_none
    def clear_response(self, assessment_section_id, item_id):
        """Clears the response to an item The item appears as unanswered.

        If no response exists, the method simply returns.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        raise:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if (not self.has_assessment_section_begun(assessment_section_id) or
                self.is_assessment_section_over(assessment_section_id)):
            raise errors.IllegalState()
        # Should probably check to see if responses can be cleared, but how?
        self.get_assessment_section(assessment_section_id).submit_response(item_id, None)

    @utilities.arguments_not_none
    @check_effective
    def finish_assessment_section(self, assessment_section_id):
        """Indicates an assessment section is complete.

        Finished sections may or may not allow new or updated responses.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        raise:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        raise:  NotFound - ``assessment_section_id`` is not found
        raise:  NullArgument - ``assessment_section_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if (not self.has_assessment_section_begun(assessment_section_id) or
                self.is_assessment_section_over(assessment_section_id)):
            raise errors.IllegalState()
        self.get_assessment_section(assessment_section_id).finish()

    @utilities.arguments_not_none
    @check_effective
    def is_answer_available(self, assessment_section_id, item_id):
        """Tests if an answer is available for the given item.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (boolean) - ``true`` if an answer are available,
                ``false`` otherwise
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Note: we need more settings elsewhere to indicate answer available conditions
        # This makes the simple assumption that answers are available only when
        # a response has been submitted for an Item.
        try:
            response = self.get_response(assessment_section_id, item_id)
            # need to invoke something like .object_map before
            # a "null" response throws IllegalState
            response.object_map
        except errors.IllegalState:
            return False
        else:
            return True

    @utilities.arguments_not_none
    @check_effective
    def get_answers(self, assessment_section_id, item_id):
        """Gets the acceptable answers to the associated item.

        arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.AnswerList) - the answers
        raise:  IllegalState - ``is_answer_available()`` is ``false``
        raise:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        raise:  NullArgument - ``assessment_section_id or item_id is
                null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.is_answer_available(assessment_section_id, item_id):
            return self.get_assessment_section(assessment_section_id).get_answers(question_id=item_id)
        raise errors.IllegalState()

    @utilities.arguments_not_none
    @check_effective
    def finish_assessment(self, assessment_taken_id):
        """Indicates the entire assessment is complete.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        raise:  IllegalState - ``has_begun()`` is ``false or is_over()``
                is ``true``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_taken = self._get_assessment_taken(assessment_taken_id)
        assessment_taken_map = assessment_taken._my_map
        if assessment_taken.has_started() and not assessment_taken.has_ended():
            assessment_taken_map['completionTime'] = DateTime.utcnow()
            assessment_taken_map['ended'] = True
            collection = JSONClientValidated('assessment',
                                             collection='AssessmentTaken',
                                             runtime=self._runtime)
            collection.save(assessment_taken_map)
        else:
            raise errors.IllegalState()

    def _get_assessment_taken(self, assessment_taken_id):
        """Helper method for getting an AssessmentTaken objects given an Id."""
        if assessment_taken_id not in self._assessments_taken:
            mgr = self._get_provider_manager('ASSESSMENT')
            lookup_session = mgr.get_assessment_taken_lookup_session(proxy=self._proxy)  # Should this be _for_bank?
            lookup_session.use_federated_bank_view()
            self._assessments_taken[assessment_taken_id] = (
                lookup_session.get_assessment_taken(assessment_taken_id))
        return self._assessments_taken[assessment_taken_id]


class AssessmentResultsSession(abc_assessment_sessions.AssessmentResultsSession, osid_sessions.OsidSession):
    """This session is used to access the tested assessment items and their associated responses.

    Assessment results may also be available and is expressed as a
    rubric through another assessment.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self, catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_access_assessment_results(self):
        """Tests if this user can take this assessment.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        return: (boolean) - ``false`` if assessment methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_items(self, assessment_taken_id):
        """Gets the items questioned in a assessment.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.ItemList) - the list of assessment
                questions
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        taken_lookup_session = mgr.get_assessment_taken_lookup_session(proxy=self._proxy)
        taken_lookup_session.use_federated_bank_view()
        taken = taken_lookup_session.get_assessment_taken(assessment_taken_id)
        ils = get_item_lookup_session(runtime=self._runtime, proxy=self._proxy)
        ils.use_federated_bank_view()
        item_list = []
        if 'sections' in taken._my_map:
            for section_id in taken._my_map['sections']:
                section = get_assessment_section(Id(section_id),
                                                 runtime=self._runtime,
                                                 proxy=self._proxy)
                for question in section._my_map['questions']:
                    item_list.append(ils.get_item(Id(question['questionId'])))
        return ItemList(item_list)

    @utilities.arguments_not_none
    def get_responses(self, assessment_taken_id):
        """Gets the submitted responses.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.ResponseList) - the submitted answers
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        taken_lookup_session = mgr.get_assessment_taken_lookup_session(proxy=self._proxy)
        taken_lookup_session.use_federated_bank_view()
        taken = taken_lookup_session.get_assessment_taken(assessment_taken_id)
        response_list = OsidListList()
        if 'sections' in taken._my_map:
            for section_id in taken._my_map['sections']:
                section = get_assessment_section(Id(section_id),
                                                 runtime=self._runtime,
                                                 proxy=self._proxy)
                response_list.append(section.get_responses())
        return ResponseList(response_list)

    @utilities.arguments_not_none
    def are_results_available(self, assessment_taken_id):
        """Tests if the results are available for this assessment.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (boolean) - ``true`` if results are available, ``false``
                otherwise
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # not implemented yet
        return False

    @utilities.arguments_not_none
    def get_grade_entries(self, assessment_taken_id):
        """Gets a list of grade entries for this assessment.

        Each grade entry may indicate a grade or score input by multiple
        graders.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.grading.GradeEntryList) - a list of grade entries
        raise:  IllegalState - ``are_results_available()`` is ``false``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # not implemented yet and are_results_available is False
        raise errors.IllegalState()


class ItemLookupSession(abc_assessment_sessions.ItemLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Item`` objects."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_lookup_items(self):
        """Tests if this user can perform ``Item`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_item_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_item_view(self):
        """A complete view of the ``Item`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this assessment bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_item(self, item_id):
        """Gets the ``Item`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Item`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Item`` and retained for compatibility.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item`` to
                retrieve
        return: (osid.assessment.Item) - the returned ``Item``
        raise:  NotFound - no ``Item`` found with the given ``Id``
        raise:  NullArgument - ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(item_id, 'assessment').get_identifier())},
                 **self._view_filter()))
        return objects.Item(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_items_by_ids(self, item_ids):
        """Gets an ``ItemList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the items
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Items`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    item_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``item_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        object_id_list = []
        for i in item_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'assessment').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.ItemList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_items_by_genus_type(self, item_genus_type):
        """Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` which does not include assessment items of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        arg:    item_genus_type (osid.type.Type): an assessment item
                genus type
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``item_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(item_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.ItemList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_items_by_parent_genus_type(self, item_genus_type):
        """Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` and include any additional assessment items with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        arg:    item_genus_type (osid.type.Type): an assessment item
                genus type
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``item_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ItemList([])

    @utilities.arguments_not_none
    def get_items_by_record_type(self, item_record_type):
        """Gets an ``ItemList`` containing the given assessment item record ``Type``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        arg:    item_record_type (osid.type.Type): an item record type
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ItemList([])

    @utilities.arguments_not_none
    def get_items_by_question(self, question_id):
        """Gets an ``ItemList`` containing the given question.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        arg:    question_id (osid.id.Id): a question ``Id``
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``question_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_items_by_answer(self, answer_id):
        """Gets an ``ItemList`` containing the given answer.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        arg:    answer_id (osid.id.Id): an answer ``Id``
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``answer_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_items_by_learning_objective(self, objective_id):
        """Gets an ``ItemList`` containing the given learning objective.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        arg:    objective_id (osid.id.Id): a learning objective ``Id``
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_items_by_learning_objectives(self, objective_ids):
        """Gets an ``ItemList`` containing the given learning objectives.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        arg:    objective_ids (osid.id.IdList): a list of learning
                objective ``Ids``
        return: (osid.assessment.ItemList) - the returned ``Item`` list
        raise:  NullArgument - ``objective_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_items(self):
        """Gets all ``Items``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those items that are accessible through this session.

        return: (osid.assessment.ItemList) - a list of ``Items``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.ItemList(result, runtime=self._runtime, proxy=self._proxy)

    items = property(fget=get_items)


class ItemQuerySession(abc_assessment_sessions.ItemQuerySession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_search_items(self):
        """Tests if this user can perform ``Item`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this assessment bank
        only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_item_query(self):
        """Gets an assessment item query.

        return: (osid.assessment.ItemQuery) - the assessment item query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.ItemQuery(runtime=self._runtime)

    item_query = property(fget=get_item_query)

    @utilities.arguments_not_none
    def get_items_by_query(self, item_query):
        """Gets a list of ``Items`` matching the given item query.

        arg:    item_query (osid.assessment.ItemQuery): the item query
        return: (osid.assessment.ItemList) - the returned ``ItemList``
        raise:  NullArgument - ``item_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``item_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in item_query._query_terms:
            if '$in' in item_query._query_terms[term] and '$nin' in item_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': item_query._query_terms[term]['$in']}},
                             {term: {'$nin': item_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: item_query._query_terms[term]})
        for term in item_query._keyword_terms:
            or_list.append({term: item_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('assessment',
                                             collection='Item',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.ItemList(result, runtime=self._runtime, proxy=self._proxy)


class ItemSearchSession(abc_assessment_sessions.ItemSearchSession, ItemQuerySession):
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

    def get_item_search(self):
        """Gets an assessment item search.

        return: (osid.assessment.ItemSearch) - the assessment item
                search
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceSearchSession.get_resource_search_template
        return searches.ItemSearch(runtime=self._runtime)

    item_search = property(fget=get_item_search)

    def get_item_search_order(self):
        """Gets an assessment item search order.

        The ``ItemSearchOrder`` is supplied to an ``ItemSearch`` to
        specify the ordering of results.

        return: (osid.assessment.ItemSearchOrder) - the assessment item
                search order
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    item_search_order = property(fget=get_item_search_order)

    @utilities.arguments_not_none
    def get_items_by_search(self, item_query, item_search):
        """Gets the search results matching the given search query using the given search.

        arg:    item_query (osid.assessment.ItemQuery): the item query
        arg:    item_search (osid.assessment.ItemSearch): the item
                search
        return: (osid.assessment.ItemSearchResults) - the returned
                search results
        raise:  NullArgument - ``item_query`` or ``item_search`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``item_search`` or ``item_query`` is not
                of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        # Copied from osid.resource.ResourceQuerySession.get_resources_by_query_template
        and_list = list()
        or_list = list()
        for term in item_query._query_terms:
            and_list.append({term: item_query._query_terms[term]})
        for term in item_query._keyword_terms:
            or_list.append({term: item_query._keyword_terms[term]})
        if item_search._id_list is not None:
            identifiers = [ObjectId(i.identifier) for i in item_search._id_list]
            and_list.append({'_id': {'$in': identifiers}})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if item_search.start is not None and item_search.end is not None:
            result = collection.find(query_terms)[item_search.start:item_search.end]
        else:
            result = collection.find(query_terms)
        return searches.ItemSearchResults(results=result, query_terms=dict(item_query._query_terms), runtime=self._runtime)

    @utilities.arguments_not_none
    def get_item_query_from_inspector(self, item_query_inspector):
        """Gets an item query from an inspector.

        The inspector is available from an ``ItemSearchResults``.

        arg:    item_query_inspector
                (osid.assessment.ItemQueryInspector): a query inspector
        return: (osid.assessment.ItemQuery) - the item query
        raise:  NullArgument - ``item_query_inspector`` is ``null``
        raise:  Unsupported - ``item_query_inspector`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ItemAdminSession(abc_assessment_sessions.ItemAdminSession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_create_items(self):
        """Tests if this user can create ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Item`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_item_with_record_types(self, item_record_types):
        """Tests if this user can create a single ``Item`` using the desired record types.

        While ``AssessmentManager.getItemRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Item``.
        Providing an empty array tests if an ``Item`` can be created
        with no records.

        arg:    item_record_types (osid.type.Type[]): array of item
                record types
        return: (boolean) - ``true`` if ``Item`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``item_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_item_form_for_create(self, item_record_types):
        """Gets the assessment item form for creating new assessment items.

        A new form should be requested for each create transaction.

        arg:    item_record_types (osid.type.Type[]): array of item
                record types to be included in the create operation or
                an empty list if none
        return: (osid.assessment.ItemForm) - the assessment item form
        raise:  NullArgument - ``item_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in item_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if item_record_types == []:
            obj_form = objects.ItemForm(
                bank_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.ItemForm(
                bank_id=self._catalog_id,
                record_types=item_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_item(self, item_form):
        """Creates a new ``Item``.

        arg:    item_form (osid.assessment.ItemForm): the form for this
                ``Item``
        return: (osid.assessment.Item) - the new ``Item``
        raise:  IllegalState - ``item_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``item_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``item_form`` did not originate from
                ``get_item_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(item_form, ABCItemForm):
            raise errors.InvalidArgument('argument type is not an ItemForm')
        if item_form.is_for_update():
            raise errors.InvalidArgument('the ItemForm is for update only, not create')
        try:
            if self._forms[item_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('item_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('item_form did not originate from this session')
        if not item_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(item_form._my_map)

        self._forms[item_form.get_id().get_identifier()] = CREATED
        result = objects.Item(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_items(self):
        """Tests if this user can update ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        return: (boolean) - ``false`` if assessment item modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_item_form_for_update(self, item_id):
        """Gets the assessment item form for updating an existing item.

        A new item form should be requested for each update transaction.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        return: (osid.assessment.ItemForm) - the assessment item form
        raise:  NotFound - ``item_id`` is not found
        raise:  NullArgument - ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(item_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (item_id.get_identifier_namespace() != 'assessment.Item' or
                item_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(item_id.get_identifier())})

        obj_form = objects.ItemForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_item(self, item_form):
        """Updates an existing item.

        arg:    item_form (osid.assessment.ItemForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``item_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``item_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``item_form`` did not originate from
                ``get_item_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(item_form, ABCItemForm):
            raise errors.InvalidArgument('argument type is not an ItemForm')
        if not item_form.is_for_update():
            raise errors.InvalidArgument('the ItemForm is for update only, not create')
        try:
            if self._forms[item_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('item_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('item_form did not originate from this session')
        if not item_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(item_form._my_map)

        self._forms[item_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Item(
            osid_object_map=item_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_items(self):
        """Tests if this user can delete ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Item`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_item(self, item_id):
        """Deletes the ``Item`` identified by the given ``Id``.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item`` to
                delete
        raise:  NotFound - an ``Item`` was not found identified by the
                given ``Id``
        raise:  NullArgument - ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(item_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        # This needs to be updated to actually check for AssessmentsTaken (and does that find even work?)
        if collection.find({'itemIds': str(item_id)}).count() != 0:
            raise errors.IllegalState('this Item is being used in one or more Assessments')
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        item_map = collection.find_one({'_id': ObjectId(item_id.get_identifier())})
        objects.Item(osid_object_map=item_map,
                     runtime=self._runtime,
                     proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(item_id.get_identifier())})

    def can_manage_item_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Item`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_item(self, item_id, alias_id):
        """Adds an ``Id`` to an ``Item`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Item`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another item, it is reassigned to the
        given item ``Id``.

        arg:    item_id (osid.id.Id): the ``Id`` of an ``Item``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``item_id`` not found
        raise:  NullArgument - ``item_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=item_id, equivalent_id=alias_id)

    def can_create_questions(self):
        """Tests if this user can create ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Question`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_question_with_record_types(self, question_record_types):
        """Tests if this user can create a single ``Question`` using the desired record types.

        While ``AssessmentManager.getQuestionRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Question``.
        Providing an empty array tests if a ``Question`` can be created
        with no records.

        arg:    question_record_types (osid.type.Type[]): array of
                question record types
        return: (boolean) - ``true`` if ``Question`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``question_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_question_form_for_create(self, item_id, question_record_types):
        """Gets the question form for creating new questions.

        A new form should be requested for each create transaction.

        arg:    item_id (osid.id.Id): an assessment item ``Id``
        arg:    question_record_types (osid.type.Type[]): array of
                question record types to be included in the create
                operation or an empty list if none
        return: (osid.assessment.QuestionForm) - the question form
        raise:  NullArgument - ``question_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template

        if not isinstance(item_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in question_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if question_record_types == []:
            # WHY are we passing bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.QuestionForm(
                bank_id=self._catalog_id,
                item_id=item_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.QuestionForm(
                bank_id=self._catalog_id,
                record_types=question_record_types,
                item_id=item_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_question(self, question_form):
        """Creates a new ``Question``.

        arg:    question_form (osid.assessment.QuestionForm): the form
                for this ``Question``
        return: (osid.assessment.Question) - the new ``Question``
        raise:  AlreadyExists - a question already exists for this item
        raise:  IllegalState - ``question_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``question_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``question_form`` did not originate from
                ``get_question_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(question_form, ABCQuestionForm):
            raise errors.InvalidArgument('argument type is not an QuestionForm')
        if question_form.is_for_update():
            raise errors.InvalidArgument('the QuestionForm is for update only, not create')
        try:
            if self._forms[question_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('question_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('question_form did not originate from this session')
        if not question_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        item_id = Id(question_form._my_map['itemId']).get_identifier()
        question_form._my_map['_id'] = ObjectId(item_id)
        item = collection.find_one({'$and': [{'_id': ObjectId(item_id)},
                                             {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]})
        # set the name in the question, so it can be shown to students
        question_form._my_map['displayName']['text'] = item['displayName']['text']
        question_form._my_map['description']['text'] = item['description']['text']
        if item['question'] is None:
            item['question'] = question_form._my_map
        else:
            item['question'] = question_form._my_map  # Let's just assume we can overwrite it
        collection.save(item)
        self._forms[question_form.get_id().get_identifier()] = CREATED
        return objects.Question(osid_object_map=question_form._my_map,
                                runtime=self._runtime,
                                proxy=self._proxy)

    def can_update_questions(self):
        """Tests if this user can update ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if question modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_question_form_for_update(self, question_id):
        """Gets the question form for updating an existing question.

        A new question form should be requested for each update
        transaction.

        arg:    question_id (osid.id.Id): the ``Id`` of the ``Question``
        return: (osid.assessment.QuestionForm) - the question form
        raise:  NotFound - ``question_id`` is not found
        raise:  NullArgument - ``question_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(question_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        document = collection.find_one({'question._id': ObjectId(question_id.get_identifier())})
        obj_form = objects.QuestionForm(osid_object_map=document['question'],
                                        runtime=self._runtime,
                                        proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED
        return obj_form

    @utilities.arguments_not_none
    def update_question(self, question_form):
        """Updates an existing question.

        arg:    question_form (osid.assessment.QuestionForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``question_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``question_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``question_form`` did not originate from
                ``get_question_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(question_form, ABCQuestionForm):
            raise errors.InvalidArgument('argument type is not an QuestionForm')
        if not question_form.is_for_update():
            raise errors.InvalidArgument('the QuestionForm is for update only, not create')
        try:
            if self._forms[question_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('question_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('question_form did not originate from this session')
        if not question_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        item_id = Id(question_form._my_map['itemId']).get_identifier()
        item = collection.find_one({'$and': [{'_id': ObjectId(item_id)},
                                   {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]})
        item['question'] = question_form._my_map
        try:
            collection.save(item)
        except:  # what exceptions does mongodb save raise?
            raise errors.OperationFailed()
        self._forms[question_form.get_id().get_identifier()] = UPDATED
        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Question(osid_object_map=question_form._my_map,
                                runtime=self._runtime,
                                proxy=self._proxy)

    def can_delete_questions(self):
        """Tests if this user can delete ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Question`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_question(self, question_id):
        """Deletes the ``Question`` identified by the given ``Id``.

        arg:    question_id (osid.id.Id): the ``Id`` of the ``Question``
                to delete
        raise:  NotFound - a ``Question`` was not found identified by
                the given ``Id``
        raise:  NullArgument - ``question_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(question_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        item = collection.find_one({'question._id': ObjectId(question_id.get_identifier())})

        item['question'] = None
        collection.save(item)

    def can_create_answers(self):
        """Tests if this user can create ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Answer``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Answer`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_answers_with_record_types(self, answer_record_types):
        """Tests if this user can create a single ``Answer`` using the desired record types.

        While ``AssessmentManager.getAnswerRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Answer``.
        Providing an empty array tests if an ``Answer`` can be created
        with no records.

        arg:    answer_record_types (osid.type.Type[]): array of answer
                record types
        return: (boolean) - ``true`` if ``Answer`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``answern_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_answer_form_for_create(self, item_id, answer_record_types):
        """Gets the answer form for creating new answers.

        A new form should be requested for each create transaction.

        arg:    item_id (osid.id.Id): an assessment item ``Id``
        arg:    answer_record_types (osid.type.Type[]): array of answer
                record types to be included in the create operation or
                an empty list if none
        return: (osid.assessment.AnswerForm) - the answer form
        raise:  NullArgument - ``answer_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template

        if not isinstance(item_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in answer_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if answer_record_types == []:
            # WHY are we passing bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.AnswerForm(
                bank_id=self._catalog_id,
                item_id=item_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.AnswerForm(
                bank_id=self._catalog_id,
                record_types=answer_record_types,
                item_id=item_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_answer(self, answer_form):
        """Creates a new ``Answer``.

        arg:    answer_form (osid.assessment.AnswerForm): the form for
                this ``Answer``
        return: (osid.assessment.Answer) - the new ``Answer``
        raise:  IllegalState - ``answer_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``answer_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``answer_form`` did not originate from
                ``get_answer_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.create_asset_content_template
        from dlkit.abstract_osid.assessment.objects import AnswerForm as ABCAnswerForm
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(answer_form, ABCAnswerForm):
            raise errors.InvalidArgument('argument type is not an AnswerForm')
        if answer_form.is_for_update():
            raise errors.InvalidArgument('the AnswerForm is for update only, not create')
        try:
            if self._forms[answer_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('answer_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('answer_form did not originate from this session')
        if not answer_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        answer_form._my_map['_id'] = ObjectId()
        item_id = Id(answer_form._my_map['itemId']).get_identifier()
        item = collection.find_one(
            {'$and': [{'_id': ObjectId(item_id)},
                      {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]})
        item['answers'].append(answer_form._my_map)
        result = collection.save(item)

        self._forms[answer_form.get_id().get_identifier()] = CREATED
        from .objects import Answer
        return Answer(
            osid_object_map=answer_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_update_answers(self):
        """Tests if this user can update ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if answer modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_answer_form_for_update(self, answer_id):
        """Gets the answer form for updating an existing answer.

        A new answer form should be requested for each update
        transaction.

        arg:    answer_id (osid.id.Id): the ``Id`` of the ``Answer``
        return: (osid.assessment.AnswerForm) - the answer form
        raise:  NotFound - ``answer_id`` is not found
        raise:  NullArgument - ``answer_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        from .objects import AnswerForm
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(answer_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        document = collection.find_one({'answers._id': ObjectId(answer_id.get_identifier())})
        for sub_doc in document['answers']:  # There may be a MongoDB shortcut for this
            if sub_doc['_id'] == ObjectId(answer_id.get_identifier()):
                result = sub_doc
        obj_form = AnswerForm(
            osid_object_map=result,
            runtime=self._runtime,
            proxy=self._proxy)
        obj_form._for_update = True
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED
        return obj_form

    @utilities.arguments_not_none
    def update_answer(self, answer_form):
        """Updates an existing answer.

        arg:    answer_form (osid.assessment.AnswerForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``answer_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``answer_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``answer_form`` did not originate from
                ``get_answer_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.update_asset_content_template
        from dlkit.abstract_osid.assessment.objects import AnswerForm as ABCAnswerForm
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(answer_form, ABCAnswerForm):
            raise errors.InvalidArgument('argument type is not an AnswerForm')
        if not answer_form.is_for_update():
            raise errors.InvalidArgument('the AnswerForm is for update only, not create')
        try:
            if self._forms[answer_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('answer_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('answer_form did not originate from this session')
        if not answer_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        item_id = Id(answer_form._my_map['itemId']).get_identifier()
        item = collection.find_one(
            {'$and': [{'_id': ObjectId(item_id)},
                      {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]})
        index = 0
        found = False
        for i in item['answers']:
            if i['_id'] == ObjectId(answer_form._my_map['_id']):
                item['answers'].pop(index)
                item['answers'].insert(index, answer_form._my_map)
                found = True
                break
            index += 1
        if not found:
            raise errors.NotFound()
        try:
            collection.save(item)
        except:  # what exceptions does mongodb save raise?
            raise errors.OperationFailed()
        self._forms[answer_form.get_id().get_identifier()] = UPDATED
        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        from .objects import Answer

        return Answer(
            osid_object_map=answer_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_answers(self):
        """Tests if this user can delete ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Answer`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_answer(self, answer_id):
        """Deletes the ``Answer`` identified by the given ``Id``.

        arg:    answer_id (osid.id.Id): the ``Id`` of the ``Answer`` to
                delete
        raise:  NotFound - an ``Answer`` was not found identified by the
                given ``Id``
        raise:  NullArgument - ``answer_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.delete_asset_content_template
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        from .objects import Answer
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        if not isinstance(answer_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        item = collection.find_one({'answers._id': ObjectId(answer_id.get_identifier())})

        index = 0
        found = False
        for i in item['answers']:
            if i['_id'] == ObjectId(answer_id.get_identifier()):
                answer_map = item['answers'].pop(index)
            index += 1
            found = True
        if not found:
            raise errors.OperationFailed()
        Answer(
            osid_object_map=answer_map,
            runtime=self._runtime,
            proxy=self._proxy)._delete()
        collection.save(item)

    # This is out of spec, but used by the EdX / LORE record extensions...
    @utilities.arguments_not_none
    def duplicate_item(self, item_id):
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        mgr = self._get_provider_manager('ASSESSMENT')
        lookup_session = mgr.get_item_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        try:
            lookup_session.use_unsequestered_item_view()
        except AttributeError:
            pass
        item_map = dict(lookup_session.get_item(item_id)._my_map)
        del item_map['_id']
        if 'bankId' in item_map:
            item_map['bankId'] = str(self._catalog_id)
        if 'assignedBankIds' in item_map:
            item_map['assignedBankIds'] = [str(self._catalog_id)]
        insert_result = collection.insert_one(item_map)
        result = objects.Item(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)
        return result


class ItemNotificationSession(abc_assessment_sessions.ItemNotificationSession, osid_sessions.OsidSession):
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Item`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``ItemLookupSession``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)

        if not MONGO_LISTENER.is_alive():
            MONGO_LISTENER.initialize(runtime)
            MONGO_LISTENER.start()

        self._receiver = kwargs['receiver']
        db_prefix = ''
        try:
            db_prefix_param_id = Id('parameter:mongoDBNamePrefix@mongo')
            db_prefix = runtime.get_configuration().get_value_by_parameter(db_prefix_param_id).get_string_value()
        except (AttributeError, KeyError, errors.NotFound):
            pass
        self._ns = '{0}assessment.Item'.format(db_prefix)

        if self._ns not in MONGO_LISTENER.receivers:
            MONGO_LISTENER.receivers[self._ns] = dict()
        MONGO_LISTENER.receivers[self._ns][self._receiver] = {
            'authority': self._authority,
            'obj_name_plural': 'items',
            'i': False,
            'u': False,
            'd': False,
            'reliable': False,
        }

    def __del__(self):
        """Make sure the receiver is removed from the listener"""
        del MONGO_LISTENER.receivers[self._ns][self._receiver]
        super(ItemNotificationSession, self).__del__()

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_register_for_item_notifications(self):
        """Tests if this user can register for ``Item`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for assessment items
        in assessment banks which are children of this assessment bank
        in the assessment bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this assessment bank
        only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def reliable_item_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.reliable_resource_notifications
        MONGO_LISTENER.receivers[self._ns][self._receiver]['reliable'] = True

    def unreliable_item_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.unreliable_resource_notifications
        MONGO_LISTENER.receivers[self._ns][self._receiver]['reliable'] = False

    @utilities.arguments_not_none
    def acknowledge_item_notification(self, notification_id):
        """Acknowledge an item notification.

        arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def register_for_new_items(self):
        """Register for notifications of new assessment items.

        ``ItemReceiver.newItems()`` is invoked when a new ``Item`` is
        created.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        MONGO_LISTENER.receivers[self._ns][self._receiver]['i'] = True

    def register_for_changed_items(self):
        """Registers for notification of updated assessment items.

        ``ItemReceiver.changedItems()`` is invoked when an assessment
        item is changed.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        MONGO_LISTENER.receivers[self._ns][self._receiver]['u'] = True

    @utilities.arguments_not_none
    def register_for_changed_item(self, item_id):
        """Registers for notification of an updated assessment item.

        ``ItemReceiver.changedItems()`` is invoked when the specified
        assessment item is changed.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Assessment``
                to monitor
        raise:  NotFound - an ``item`` was not found identified by the
                given ``Id``
        raise:  NullArgument - ``item_id is null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not MONGO_LISTENER.receivers[self._ns][self._receiver]['u']:
            MONGO_LISTENER.receivers[self._ns][self._receiver]['u'] = []
        if isinstance(MONGO_LISTENER.receivers[self._ns][self._receiver]['u'], list):
            MONGO_LISTENER.receivers[self._ns][self._receiver]['u'].append(item_id.get_identifier())

    def register_for_deleted_items(self):
        """Registers for notification of deleted assessment items.

        ``ItemReceiver.deletedItems()`` is invoked when an assessment
        item is removed from the assessment bank.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        MONGO_LISTENER.receivers[self._ns][self._receiver]['d'] = True

    @utilities.arguments_not_none
    def register_for_deleted_item(self, item_id):
        """Registers for notification of a deleted assessment item.

        ``ItemReceiver.deletedItems()`` is invoked when the specified
        assessment item is removed from the assessment bank.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item`` to
                monitor
        raise:  NotFound - an ``Item`` was not found identified by the
                given ``Id``
        raise:  NullArgument - ``item_id is null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not MONGO_LISTENER.receivers[self._ns][self._receiver]['d']:
            MONGO_LISTENER.receivers[self._ns][self._receiver]['d'] = []
        if isinstance(MONGO_LISTENER.receivers[self._ns][self._receiver]['d'], list):
            MONGO_LISTENER.receivers[self._ns][self._receiver]['d'].append(item_id.get_identifier())

    def reliable_item_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.reliable_resource_notifications
        MONGO_LISTENER.receivers[self._ns][self._receiver]['reliable'] = True

    def unreliable_item_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.unreliable_resource_notifications
        MONGO_LISTENER.receivers[self._ns][self._receiver]['reliable'] = False

    @utilities.arguments_not_none
    def acknowledge_item_notification(self, notification_id):
        """Acknowledge an item notification.

        arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ItemBankSession(abc_assessment_sessions.ItemBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Item`` to ``Bank`` mappings.

    An ``Item`` may appear in multiple ``Banks``. Each ``Bank`` may have
    its own authorizations governing who is allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'assessment.ItemBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_item_bank_mappings(self):
        """Tests if this user can perform lookups of item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bank_view(self):
        """A complete view of the ``Item`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_item_ids_by_bank(self, bank_id):
        """Gets the list of ``Item``  ``Ids`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of related item ``Ids``
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for item in self.get_items_by_bank(bank_id):
            id_list.append(item.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_items_by_bank(self, bank_id):
        """Gets the list of ``Items`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.assessment.ItemList) - list of related items
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_item_lookup_session_for_bank(bank_id, proxy=self._proxy)
        lookup_session.use_isolated_bank_view()
        return lookup_session.get_items()

    @utilities.arguments_not_none
    def get_item_ids_by_banks(self, bank_ids):
        """Gets the list of ``Item Ids`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for item in self.get_items_by_banks(bank_ids):
            id_list.append(item.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_items_by_banks(self, bank_ids):
        """Gets the list of ``Items`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.assessment.ItemList) - list of items
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        item_list = []
        for bank_id in bank_ids:
            item_list += list(
                self.get_items_by_bank(bank_id))
        return objects.ItemList(item_list)

    @utilities.arguments_not_none
    def get_bank_ids_by_item(self, item_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``Item``.

        arg:    item_id (osid.id.Id): ``Id`` of an ``Item``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NotFound - ``item_id`` is not found
        raise:  NullArgument - ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_item_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        item = lookup_session.get_item(item_id)
        id_list = []
        for idstr in item._my_map['assignedBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_banks_by_item(self, item_id):
        """Gets the list of ``Banks`` mapped to an ``Item``.

        arg:    item_id (osid.id.Id): ``Id`` of an ``Item``
        return: (osid.assessment.BankList) - list of banks
        raise:  NotFound - ``item_id`` is not found
        raise:  NullArgument - ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_banks_by_ids(
            self.get_bank_ids_by_item(item_id))


class ItemBankAssignmentSession(abc_assessment_sessions.ItemBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Items`` to ``Banks``.

    An ``Item`` may map to multiple ``Banks`` and removing the last
    reference to an ``Item`` is the equivalent of deleting it. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    operate on it.

    Moving or adding a reference of an ``Item`` to another ``Bank`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'assessment.ItemBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Bank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_items(self):
        """Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_assign_items_to_bank(self, bank_id):
        """Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given bank node in which any item can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        banks = lookup_session.get_banks()
        id_list = []
        for bank in banks:
            id_list.append(bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_bank_ids_for_item(self, bank_id, item_id):
        """Gets a list of banks including and under the given bank node in which a specific item can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` or ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_bank_ids(bank_id)

    @utilities.arguments_not_none
    def assign_item_to_bank(self, item_id, bank_id):
        """Adds an existing ``Item`` to a ``Bank``.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  AlreadyExists - ``item_id`` is already assigned to
                ``bank_id``
        raise:  NotFound - ``item_id`` or ``bank_id`` not found
        raise:  NullArgument - ``item_id`` or ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._assign_object_to_catalog(item_id, bank_id)

    @utilities.arguments_not_none
    def unassign_item_from_bank(self, item_id, bank_id):
        """Removes an ``Item`` from a ``Bank``.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  NotFound - ``item_id`` or ``bank_id`` not found or
                ``item_id`` not assigned to ``bank_id``
        raise:  NullArgument - ``item_id`` or ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(item_id, bank_id)

    @utilities.arguments_not_none
    def reassign_item_to_billing(self, item_id, from_bank_id, to_bank_id):
        """Moves an ``Item`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        raise:  NotFound - ``item_id, from_bank_id,`` or ``to_bank_id``
                not found or ``item_id`` not mapped to ``from_bank_id``
        raise:  NullArgument - ``item_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class AssessmentLookupSession(abc_assessment_sessions.AssessmentLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving assessments."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_lookup_assessments(self):
        """Tests if this user can perform ``Assessment`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_assessment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_assessment_view(self):
        """A complete view of the ``Assessment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_assessment(self, assessment_id):
        """Gets the ``Assessment`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Assessment`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Assessment`` and retained
        for compatibility.

        arg:    assessment_id (osid.id.Id): ``Id`` of the ``Assessment``
        return: (osid.assessment.Assessment) - the assessment
        raise:  NotFound - ``assessment_id`` not found
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(assessment_id, 'assessment').get_identifier())},
                 **self._view_filter()))
        return objects.Assessment(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_by_ids(self, assessment_ids):
        """Gets an ``AssessmentList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assessments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        arg:    assessment_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``assessment_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        object_id_list = []
        for i in assessment_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'assessment').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.AssessmentList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_by_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        arg:    assessment_genus_type (osid.type.Type): an assessment
                genus type
        return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        raise:  NullArgument - ``assessment_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(assessment_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_by_parent_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        arg:    assessment_genus_type (osid.type.Type): an assessment
                genus type
        return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        raise:  NullArgument - ``assessment_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentList([])

    @utilities.arguments_not_none
    def get_assessments_by_record_type(self, assessment_record_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        arg:    assessment_record_type (osid.type.Type): an assessment
                record type
        return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        raise:  NullArgument - ``assessment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentList([])

    def get_assessments(self):
        """Gets all ``Assessments``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        return: (osid.assessment.AssessmentList) - a list of
                ``Assessments``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.AssessmentList(result, runtime=self._runtime, proxy=self._proxy)

    assessments = property(fget=get_assessments)


class AssessmentQuerySession(abc_assessment_sessions.AssessmentQuerySession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_search_assessments(self):
        """Tests if this user can perform ``Assessment`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_assessment_query(self):
        """Gets an assessment query.

        return: (osid.assessment.AssessmentQuery) - the assessment query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.AssessmentQuery(runtime=self._runtime)

    assessment_query = property(fget=get_assessment_query)

    @utilities.arguments_not_none
    def get_assessments_by_query(self, assessment_query):
        """Gets a list of ``Assessments`` matching the given assessment query.

        arg:    assessment_query (osid.assessment.AssessmentQuery): the
                assessment query
        return: (osid.assessment.AssessmentList) - the returned
                ``AssessmentList``
        raise:  NullArgument - ``assessment_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        """Gets a list of ``Assessments`` matching the given assessment query.

        arg:    assessment_query (osid.assessment.AssessmentQuery): the
                assessment query
        return: (osid.assessment.AssessmentList) - the returned
                ``AssessmentList``
        raise:  NullArgument - ``assessment_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        if 'assessmentOfferedId' in assessment_query._query_terms:
            collection = JSONClientValidated('assessment',
                                             collection='AssessmentOffered',
                                             runtime=self._runtime)
            match = '$in' in assessment_query._query_terms['assessmentOfferedId'].keys()
            if match:
                match_identifiers = [ObjectId(Id(i).identifier) for i in assessment_query._query_terms['assessmentOfferedId']['$in']]
                query = {'$in': match_identifiers}
            else:
                match_identifiers = [ObjectId(Id(i).identifier) for i in assessment_query._query_terms['assessmentOfferedId']['$in']]
                query = {'$nin': match_identifiers}

            result = collection.find({
                "_id": query
            })

            assessment_ids = [ObjectId(Id(r['assessmentId']).identifier) for r in result]

            collection = JSONClientValidated('assessment',
                                             collection='Assessment',
                                             runtime=self._runtime)
            result = collection.find({
                "_id": {"$in": assessment_ids}
            })
            return objects.AssessmentList(result, runtime=self._runtime, proxy=self._proxy)
        else:
            # and_list = list()
            # or_list = list()
            # for term in assessment_query._query_terms:
            #     and_list.append({term: assessment_query._query_terms[term]})
            # for term in assessment_query._keyword_terms:
            #     or_list.append({term: assessment_query._keyword_terms[term]})
            # if or_list:
            #     and_list.append({'$or': or_list})
            # view_filter = self._view_filter()
            # if view_filter:
            #     and_list.append(view_filter)
            # if and_list:
            #     query_terms = {'$and': and_list}
            #
            #     collection = JSONClientValidated('assessment',
            #                                      collection='Assessment',
            #                                      runtime=self._runtime)
            #     result = collection.find(query_terms).sort('_id', DESCENDING)
            # else:
            #     result = []
            # return objects.AssessmentList(result, runtime=self._runtime, proxy=self._proxy)
            and_list = list()
            or_list = list()
            for term in assessment_query._query_terms:
                if '$in' in assessment_query._query_terms[term] and '$nin' in assessment_query._query_terms[term]:
                    and_list.append(
                        {'$or': [{term: {'$in': assessment_query._query_terms[term]['$in']}},
                                 {term: {'$nin': assessment_query._query_terms[term]['$nin']}}]})
                else:
                    and_list.append({term: assessment_query._query_terms[term]})
            for term in assessment_query._keyword_terms:
                or_list.append({term: assessment_query._keyword_terms[term]})
            if or_list:
                and_list.append({'$or': or_list})
            view_filter = self._view_filter()
            if view_filter:
                and_list.append(view_filter)
            if and_list:
                query_terms = {'$and': and_list}
                collection = JSONClientValidated('assessment',
                                                 collection='Assessment',
                                                 runtime=self._runtime)
                result = collection.find(query_terms).sort('_id', DESCENDING)
            else:
                result = []
            return objects.AssessmentList(result, runtime=self._runtime, proxy=self._proxy)


class AssessmentAdminSession(abc_assessment_sessions.AssessmentAdminSession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_create_assessments(self):
        """Tests if this user can create ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Assessment`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_assessment_with_record_types(self, assessment_record_types):
        """Tests if this user can create a single ``Assessment`` using the desired record interface types.

        While ``AssessmentManager.getAssessmentRecordTypes()`` can be
        used to examine which record interfaces are supported, this
        method tests which record(s) are required for creating a
        specific ``Assessment``. Providing an empty array tests if an
        ``Assessment`` can be created with no records.

        arg:    assessment_record_types (osid.type.Type[]): array of
                assessment record types
        return: (boolean) - ``true`` if ``Assessment`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``assessment_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_form_for_create(self, assessment_record_types):
        """Gets the assessment form for creating new assessments.

        A new form should be requested for each create transaction.

        arg:    assessment_record_types (osid.type.Type[]): array of
                assessment record types to be included in the create
                operation or an empty list if none
        return: (osid.assessment.AssessmentForm) - the assessment form
        raise:  NullArgument - ``assessment_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in assessment_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if assessment_record_types == []:
            obj_form = objects.AssessmentForm(
                bank_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.AssessmentForm(
                bank_id=self._catalog_id,
                record_types=assessment_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_assessment(self, assessment_form):
        """Creates a new ``Assessment``.

        arg:    assessment_form (osid.assessment.AssessmentForm): the
                form for this ``Assessment``
        return: (osid.assessment.Assessment) - the new ``Assessment``
        raise:  IllegalState - ``assessment_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``assessment_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_form`` did not originate from
                ``get_assessment_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        if not isinstance(assessment_form, ABCAssessmentForm):
            raise errors.InvalidArgument('argument type is not an AssessmentForm')
        if assessment_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentForm is for update only, not create')
        try:
            if self._forms[assessment_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('assessment_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('assessment_form did not originate from this session')
        if not assessment_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(assessment_form._my_map)

        self._forms[assessment_form.get_id().get_identifier()] = CREATED
        result = objects.Assessment(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_assessments(self):
        """Tests if this user can update ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Assessment`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_form_for_update(self, assessment_id):
        """Gets the assessment form for updating an existing assessment.

        A new assessment form should be requested for each update
        transaction.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        return: (osid.assessment.AssessmentForm) - the assessment form
        raise:  NotFound - ``assessment_id`` is not found
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        if not isinstance(assessment_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (assessment_id.get_identifier_namespace() != 'assessment.Assessment' or
                assessment_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(assessment_id.get_identifier())})

        obj_form = objects.AssessmentForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_assessment(self, assessment_form):
        """Updates an existing assessment.

        arg:    assessment_form (osid.assessment.AssessmentForm): the
                form containing the elements to be updated
        raise:  IllegalState - ``assessment_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``assessment_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_form did not originate from
                get_assessment_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        if not isinstance(assessment_form, ABCAssessmentForm):
            raise errors.InvalidArgument('argument type is not an AssessmentForm')
        if not assessment_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentForm is for update only, not create')
        try:
            if self._forms[assessment_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('assessment_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('assessment_form did not originate from this session')
        if not assessment_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(assessment_form._my_map)

        self._forms[assessment_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Assessment(
            osid_object_map=assessment_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_assessments(self):
        """Tests if this user can delete ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Assessment`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_assessment(self, assessment_id):
        """Deletes an ``Assessment``.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment`` to remove
        raise:  NotFound - ``assessment_id`` not found
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        """Delete all the children AssessmentParts recursively, too"""
        def remove_children_parts(parent_id):
            part_collection = JSONClientValidated('assessment_authoring',
                                                  collection='AssessmentPart',
                                                  runtime=self._runtime)
            if 'assessment.Assessment' in parent_id:
                query = {"assessmentId": parent_id}
            else:
                query = {"assessmentPartId": parent_id}

            # need to account for magic parts ...
            for part in part_collection.find(query):
                part = assessment_authoring_objects.AssessmentPart(osid_object_map=part,
                                                                   runtime=self._runtime,
                                                                   proxy=self._proxy)
                apls = get_assessment_part_lookup_session(runtime=self._runtime,
                                                          proxy=self._proxy)
                apls.use_unsequestered_assessment_part_view()
                apls.use_federated_bank_view()
                part = apls.get_assessment_part(part.ident)
                try:
                    part.delete()
                except AttributeError:
                    part_collection.delete_one({'_id': ObjectId(part.ident.get_identifier())})
                remove_children_parts(str(part.ident))

        if not isinstance(assessment_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        if collection.find({'assessmentId': str(assessment_id)}).count() != 0:
            raise errors.IllegalState('there are still AssessmentsOffered associated with this Assessment')
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        collection.delete_one({'_id': ObjectId(assessment_id.get_identifier())})
        remove_children_parts(str(assessment_id))

    def can_manage_assessment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Assessment`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_assessment(self, assessment_id, alias_id):
        """Adds an ``Id`` to an ``Assessment`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Assessment`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another assessment, it is reassigned
        to the given assessment ``Id``.

        arg:    assessment_id (osid.id.Id): the ``Id`` of an
                ``Assessment``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``assessment_id`` not found
        raise:  NullArgument - ``assessment_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=assessment_id, equivalent_id=alias_id)

    # This is out of spec, but used by the EdX / LORE record extensions...
    @utilities.arguments_not_none
    def duplicate_assessment(self, assessment_id):
        collection = JSONClientValidated('assessment',
                                         collection='Assessment',
                                         runtime=self._runtime)
        mgr = self._get_provider_manager('ASSESSMENT')
        lookup_session = mgr.get_assessment_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        try:
            lookup_session.use_unsequestered_assessment_view()
        except AttributeError:
            pass
        assessment_map = dict(lookup_session.get_assessment(assessment_id)._my_map)
        del assessment_map['_id']
        if 'bankId' in assessment_map:
            assessment_map['bankId'] = str(self._catalog_id)
        if 'assignedBankIds' in assessment_map:
            assessment_map['assignedBankIds'] = [str(self._catalog_id)]
        insert_result = collection.insert_one(assessment_map)
        result = objects.Assessment(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)
        return result


class AssessmentBankSession(abc_assessment_sessions.AssessmentBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Assessment`` to ``Bank`` mappings.

    An ``Assessment`` may appear in multiple ``Banks``. Each ``Bank``
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'assessment.AssessmentBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_assessment_bank_mappings(self):
        """Tests if this user can perform lookups of assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bank_view(self):
        """A complete view of the ``Assessment`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_assessment_ids_by_bank(self, bank_id):
        """Gets the list of ``Assessment``  ``Ids`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of related assessment ``Ids``
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for assessment in self.get_assessments_by_bank(bank_id):
            id_list.append(assessment.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessments_by_bank(self, bank_id):
        """Gets the list of ``Assessments`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.assessment.AssessmentList) - list of related
                assessments
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_lookup_session_for_bank(bank_id, proxy=self._proxy)
        lookup_session.use_isolated_bank_view()
        return lookup_session.get_assessments()

    @utilities.arguments_not_none
    def get_assessment_ids_by_banks(self, bank_ids):
        """Gets the list of ``Assessment Ids`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for assessment in self.get_assessments_by_banks(bank_ids):
            id_list.append(assessment.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessments_by_banks(self, bank_ids):
        """Gets the list of ``Assessments`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.assessment.AssessmentList) - list of assessments
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        assessment_list = []
        for bank_id in bank_ids:
            assessment_list += list(
                self.get_assessments_by_bank(bank_id))
        return objects.AssessmentList(assessment_list)

    @utilities.arguments_not_none
    def get_bank_ids_by_assessment(self, assessment_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``Assessment``.

        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NotFound - ``assessment_id`` is not found
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        assessment = lookup_session.get_assessment(assessment_id)
        id_list = []
        for idstr in assessment._my_map['assignedBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_banks_by_assessment(self, assessment_id):
        """Gets the list of ``Banks`` mapped to an ``Assessment``.

        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        return: (osid.assessment.BankList) - list of banks
        raise:  NotFound - ``assessment_id`` is not found
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_banks_by_ids(
            self.get_bank_ids_by_assessment(assessment_id))


class AssessmentBankAssignmentSession(abc_assessment_sessions.AssessmentBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Assessments`` to ``Banks``.

    An ``Assessment`` may map to multiple ``Banks`` and removing the
    last reference to an ``Assessment`` is the equivalent of deleting
    it. Each ``Bank`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of an ``Assessment`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'assessment.AssessmentBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Bank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_assessments(self):
        """Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_assign_assessments_to_bank(self, bank_id):
        """Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given banks node in which any assessment can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        banks = lookup_session.get_banks()
        id_list = []
        for bank in banks:
            id_list.append(bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_bank_ids_for_assessment(self, bank_id, assessment_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` or ``assessment_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_bank_ids(bank_id)

    @utilities.arguments_not_none
    def assign_assessment_to_bank(self, assessment_id, bank_id):
        """Adds an existing ``Assessment`` to a ``Bank``.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  AlreadyExists - ``assessment_id`` is already assigned to
                ``bank_id``
        raise:  NotFound - ``assessment_id`` or ``bank_id`` not found
        raise:  NullArgument - ``assessment_id`` or ``bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._assign_object_to_catalog(assessment_id, bank_id)

    @utilities.arguments_not_none
    def unassign_assessment_from_bank(self, assessment_id, bank_id):
        """Removes an ``Assessment`` from a ``Bank``.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  NotFound - ``assessment_id`` or ``bank_id`` not found or
                ``assessment_id`` not assigned to ``bank_id``
        raise:  NullArgument - ``assessment_id`` or ``bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(assessment_id, bank_id)

    @utilities.arguments_not_none
    def reassign_assessment_to_billing(self, assessment_id, from_bank_id, to_bank_id):
        """Moves an ``Assessment`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        raise:  NotFound - ``assessment_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_id`` not mapped
                to ``from_bank_id``
        raise:  NullArgument - ``assessment_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class AssessmentBasicAuthoringSession(abc_assessment_sessions.AssessmentBasicAuthoringSession, osid_sessions.OsidSession):
    """This session defines methods to manage assessment items in an assessment.

    This session is used for simple assessments without sections or
    parts. Updating the items on an assessment authored with sections
    and parts may result in an error.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        self._part_item_session = mgr.get_assessment_part_item_session_for_bank(self._catalog_id, proxy=self._proxy)
        self._part_item_design_session = mgr.get_assessment_part_item_design_session_for_bank(self._catalog_id, proxy=self._proxy)
        self._part_item_session.use_federated_bank_view()
        self._first_part_index = {}

    def _get_first_part_id(self, assessment_id):
        """This session implemenation assumes all items are assigned to the first assessment part"""
        if assessment_id not in self._first_part_index:
            self._first_part_index[assessment_id] = get_first_part_id_for_assessment(
                assessment_id,
                runtime=self._runtime,
                proxy=self._proxy,
                create=True,
                bank_id=self._catalog_id)
        return self._first_part_index[assessment_id]

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_author_assessments(self):
        """Tests if this user can author assessments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        authoring operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_items(self, assessment_id):
        """Gets the items in sequence from an assessment.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        return: (osid.assessment.ItemList) - list of items
        raise:  NotFound - ``assessmentid`` not found
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if assessment_id.get_identifier_namespace() != 'assessment.Assessment':
            raise errors.InvalidArgument
        return self._part_item_session.get_assessment_part_items(self._get_first_part_id(assessment_id))

    @utilities.arguments_not_none
    def add_item(self, assessment_id, item_id):
        """Adds an existing ``Item`` to an assessment.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        raise:  NotFound - ``assessment_id`` or ``item_id`` not found
        raise:  NullArgument - ``assessment_id`` or ``item_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if assessment_id.get_identifier_namespace() != 'assessment.Assessment':
            raise errors.InvalidArgument
        self._part_item_design_session.add_item(item_id, self._get_first_part_id(assessment_id))

    @utilities.arguments_not_none
    def remove_item(self, assessment_id, item_id):
        """Removes an ``Item`` from this assessment.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        raise:  NotFound - ``assessment_id`` or ``item_id`` not found or
                ``item_id`` not on ``assessmentid``
        raise:  NullArgument - ``assessment_id`` or ``item_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if assessment_id.get_identifier_namespace() != 'assessment.Assessment':
            raise errors.InvalidArgument
        self._part_item_design_session.remove_item(item_id, self._get_first_part_id(assessment_id))

    @utilities.arguments_not_none
    def move_item(self, assessment_id, item_id, preceeding_item_id):
        """Moves an existing item to follow another item in an assessment.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        arg:    item_id (osid.id.Id): the ``Id`` of an ``Item``
        arg:    preceeding_item_id (osid.id.Id): the ``Id`` of a
                preceeding ``Item`` in the sequence
        raise:  NotFound - ``assessment_id`` is not found, or
                ``item_id`` or ``preceeding_item_id`` not on
                ``assessment_id``
        raise:  NullArgument - ``assessment_id, item_id`` or
                ``preceeding_item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if assessment_id.get_identifier_namespace() != 'assessment.Assessment':
            raise errors.InvalidArgument
        self._part_item_design_session.move_item_behind(item_id, self._get_first_part_id(assessment_id), preceeding_item_id)

    @utilities.arguments_not_none
    def order_items(self, item_ids, assessment_id):
        """Sequences existing items in an assessment.

        arg:    item_ids (osid.id.Id[]): the ``Id`` of the ``Items``
        arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        raise:  NotFound - ``assessment_id`` is not found or an
                ``item_id`` is not on ``assessment_id``
        raise:  NullArgument - ``assessment_id`` or ``item_ids`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        if assessment_id.get_identifier_namespace() != 'assessment.Assessment':
            raise errors.InvalidArgument
        self._part_item_design_session.order_items(item_ids, self._get_first_part_id(assessment_id))


class AssessmentOfferedLookupSession(abc_assessment_sessions.AssessmentOfferedLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving assessments offered."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_lookup_assessments_offered(self):
        """Tests if this user can perform ``AssessmentOffered`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_assessment_offered_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_assessment_offered_view(self):
        """A complete view of the ``AssessmentOffered`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_assessment_offered(self, assessment_offered_id):
        """Gets the ``AssessmentOffered`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentOffered`` may have
        a different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentOffered`` and
        retained for compatibility.

        arg:    assessment_offered_id (osid.id.Id): ``Id`` of the
                ``AssessmentOffered``
        return: (osid.assessment.AssessmentOffered) - the assessment
                offered
        raise:  NotFound - ``assessment_offered_id`` not found
        raise:  NullArgument - ``assessment_offered_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(assessment_offered_id, 'assessment').get_identifier())},
                 **self._view_filter()))
        return objects.AssessmentOffered(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_offered_by_ids(self, assessment_offered_ids):
        """Gets an ``AssessmentOfferedList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentOffered`` objects may be omitted from
        the list and may present the elements in any order including
        returning a unique set.

        arg:    assessment_offered_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``assessment_offered_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        object_id_list = []
        for i in assessment_offered_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'assessment').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.AssessmentOfferedList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_offered_by_genus_type(self, assessment_offered_genus_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus ``Type`` which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        arg:    assessment_offered_genus_type (osid.type.Type): an
                assessment offered genus type
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        raise:  NullArgument - ``assessment_offered_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(assessment_offered_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentOfferedList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_offered_by_parent_genus_type(self, assessment_offered_genus_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments offered that are accessible
        through this session.

        arg:    assessment_offered_genus_type (osid.type.Type): an
                assessment offered genus type
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        raise:  NullArgument - ``assessment_offered_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentOfferedList([])

    @utilities.arguments_not_none
    def get_assessments_offered_by_record_type(self, assessment_record_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        arg:    assessment_record_type (osid.type.Type): an assessment
                offered record type
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        raise:  NullArgument - ``assessment_offered_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentOfferedList([])

    @utilities.arguments_not_none
    def get_assessments_offered_by_date(self, start, end):
        """Gets an ``AssessmentOfferedList`` that have designated start times where the start times fall in the given range inclusive.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        arg:    start (osid.calendaring.DateTime): start of time range
        arg:    end (osid.calendaring.DateTime): end of time range
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        raise:  InvalidArgument - ``end`` is less than ``start``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_offered_for_assessment(self, assessment_id):
        """Gets an ``AssessmentOfferedList`` by the given assessment.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentId': str(assessment_id)},
                 **self._view_filter()))
        return objects.AssessmentOfferedList(result, runtime=self._runtime)

    def get_assessments_offered(self):
        """Gets all ``AssessmentOffered`` elements.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        return: (osid.assessment.AssessmentOfferedList) - a list of
                ``AssessmentOffered`` elements
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.AssessmentOfferedList(result, runtime=self._runtime, proxy=self._proxy)

    assessments_offered = property(fget=get_assessments_offered)


class AssessmentOfferedQuerySession(abc_assessment_sessions.AssessmentOfferedQuerySession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_search_assessments_offered(self):
        """Tests if this user can perform ``AssessmentOffered`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments offered in banks which
        are children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_assessment_offered_query(self):
        """Gets an assessment offered query.

        return: (osid.assessment.AssessmentOfferedQuery) - the
                assessment offered query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.AssessmentOfferedQuery(runtime=self._runtime)

    assessment_offered_query = property(fget=get_assessment_offered_query)

    @utilities.arguments_not_none
    def get_assessments_offered_by_query(self, assessment_offered_query):
        """Gets a list of ``AssessmentOffered`` elements matching the given assessment offered query.

        arg:    assessment_offered_query
                (osid.assessment.AssessmentOfferedQuery): the assessment
                offered query
        return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOfferedList``
        raise:  NullArgument - ``assessment_offered_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_offered_query`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in assessment_offered_query._query_terms:
            if '$in' in assessment_offered_query._query_terms[term] and '$nin' in assessment_offered_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': assessment_offered_query._query_terms[term]['$in']}},
                             {term: {'$nin': assessment_offered_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: assessment_offered_query._query_terms[term]})
        for term in assessment_offered_query._keyword_terms:
            or_list.append({term: assessment_offered_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('assessment',
                                             collection='AssessmentOffered',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.AssessmentOfferedList(result, runtime=self._runtime, proxy=self._proxy)


class AssessmentOfferedAdminSession(abc_assessment_sessions.AssessmentOfferedAdminSession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_create_assessments_offered(self):
        """Tests if this user can create ``AssessmentOffered`` objects.

        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentOffered`` creation
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_assessment_offered_with_record_types(self, assessment_offered_record_types):
        """Tests if this user can create a single ``AssessmentOffered`` using the desired record types.

        While ``AssessmentManager.getAssessmentOfferedRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentOffered``. Providing an empty array tests if an
        ``AssessmentOffered`` can be created with no records.

        arg:    assessment_offered_record_types (osid.type.Type[]):
                array of assessment offered record types
        return: (boolean) - ``true`` if ``AssessmentOffered`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``assessment_offered_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_offered_form_for_create(self, assessment_id, assessment_offered_record_types):
        """Gets the assessment offered form for creating new assessments offered.

        A new form should be requested for each create transaction.

        arg:    assessment_id (osid.id.Id): the ``Id`` of the related
                ``Assessment``
        arg:    assessment_offered_record_types (osid.type.Type[]):
                array of assessment offered record types to be included
                in the create operation or an empty list if none
        return: (osid.assessment.AssessmentOfferedForm) - the assessment
                offered form
        raise:  NotFound - ``assessment_id`` is not found
        raise:  NullArgument - ``assessment_id`` or
                ``assessment_offered_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template

        if not isinstance(assessment_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in assessment_offered_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if assessment_offered_record_types == []:
            # WHY are we passing bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.AssessmentOfferedForm(
                bank_id=self._catalog_id,
                assessment_id=assessment_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.AssessmentOfferedForm(
                bank_id=self._catalog_id,
                record_types=assessment_offered_record_types,
                assessment_id=assessment_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_assessment_offered(self, assessment_offered_form):
        """Creates a new ``AssessmentOffered``.

        arg:    assessment_offered_form
                (osid.assessment.AssessmentOfferedForm): the form for
                this ``AssessmentOffered``
        return: (osid.assessment.AssessmentOffered) - the new
                ``AssessmentOffered``
        raise:  IllegalState - ``assessment_offrered_form`` already used
                in a create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``assessment_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_form`` did not originate from
                ``get_assessment_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        if not isinstance(assessment_offered_form, ABCAssessmentOfferedForm):
            raise errors.InvalidArgument('argument type is not an AssessmentOfferedForm')
        if assessment_offered_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentOfferedForm is for update only, not create')
        try:
            if self._forms[assessment_offered_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('assessment_offered_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('assessment_offered_form did not originate from this session')
        if not assessment_offered_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(assessment_offered_form._my_map)

        self._forms[assessment_offered_form.get_id().get_identifier()] = CREATED
        result = objects.AssessmentOffered(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_assessments_offered(self):
        """Tests if this user can update ``AssessmentOffered`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Assessment`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_offered_form_for_update(self, assessment_offered_id):
        """Gets the assessment offered form for updating an existing assessment offered.

        A new assessment offered form should be requested for each
        update transaction.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        return: (osid.assessment.AssessmentOfferedForm) - the assessment
                offered form
        raise:  NotFound - ``assessment_offered_id`` is not found
        raise:  NullArgument - ``assessment_offered_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        if not isinstance(assessment_offered_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (assessment_offered_id.get_identifier_namespace() != 'assessment.AssessmentOffered' or
                assessment_offered_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(assessment_offered_id.get_identifier())})

        obj_form = objects.AssessmentOfferedForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_assessment_offered(self, assessment_offered_form):
        """Updates an existing assessment offered.

        arg:    assessment_offered_form
                (osid.assessment.AssessmentOfferedForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``assessment_offrered_form`` already used
                in an update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``assessment_offered_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_form`` did not originate from
                ``get_assessment_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        if not isinstance(assessment_offered_form, ABCAssessmentOfferedForm):
            raise errors.InvalidArgument('argument type is not an AssessmentOfferedForm')
        if not assessment_offered_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentOfferedForm is for update only, not create')
        try:
            if self._forms[assessment_offered_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('assessment_offered_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('assessment_offered_form did not originate from this session')
        if not assessment_offered_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(assessment_offered_form._my_map)

        self._forms[assessment_offered_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.AssessmentOffered(
            osid_object_map=assessment_offered_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_assessments_offered(self):
        """Tests if this user can delete ``AssessmentsOffered``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``AssessmentOffered`` deletion
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_assessment_offered(self, assessment_offered_id):
        """Deletes an ``AssessmentOffered``.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered`` to remove
        raise:  NotFound - ``assessment_offered_id`` not found
        raise:  NullArgument - ``assessment_offered_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ObjectiveAdminSession.delete_objective_template

        if not isinstance(assessment_offered_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        if collection.find({'assessmentOfferedId': str(assessment_offered_id)}).count() != 0:
            raise errors.IllegalState('there are still AssessmentTakens associated with this AssessmentOffered')

        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        collection.delete_one({'_id': ObjectId(assessment_offered_id.get_identifier())})

    def can_manage_assessment_offered_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentsOffered``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentOffered`` aliasing
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_assessment_offered(self, assessment_offered_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentOffered`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentOffered`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment offered, it is
        reassigned to the given assessment offered ``Id``.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of an
                ``AssessmentOffered``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``assessment_offered_id`` not found
        raise:  NullArgument - ``assessment_offered_id`` or ``alias_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=assessment_offered_id, equivalent_id=alias_id)


class AssessmentOfferedBankSession(abc_assessment_sessions.AssessmentOfferedBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``AssessmentOffered`` to ``Bank`` mappings.

    An ``AssessmentOffered`` may appear in multiple ``Banks``. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'assessment.AssessmentOfferedBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_assessment_offered_bank_mappings(self):
        """Tests if this user can perform lookups of assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bank_view(self):
        """A complete view of the ``AssessmentOffered`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_assessment_offered_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentOffered``  ``Ids`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of related assessment offered
                ``Ids``
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for assessment_offered in self.get_assessments_offered_by_bank(bank_id):
            id_list.append(assessment_offered.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessments_offered_by_bank(self, bank_id):
        """Gets the list of ``AssessmentOffereds`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.assessment.AssessmentOfferedList) - list of
                related assessments offered
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_offered_lookup_session_for_bank(bank_id, proxy=self._proxy)
        lookup_session.use_isolated_bank_view()
        return lookup_session.get_assessments_offered()

    @utilities.arguments_not_none
    def get_assessment_offered_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentOffered Ids`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for assessment_offered in self.get_assessments_offered_by_banks(bank_ids):
            id_list.append(assessment_offered.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessments_offered_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentOffered`` objects corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.assessment.AssessmentOfferedList) - list of
                assessments offered
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        assessment_offered_list = []
        for bank_id in bank_ids:
            assessment_offered_list += list(
                self.get_assessments_offered_by_bank(bank_id))
        return objects.AssessmentOfferedList(assessment_offered_list)

    @utilities.arguments_not_none
    def get_bank_ids_by_assessment_offered(self, assessment_offered_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentOffered``.

        arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NotFound - ``assessment_offered_id`` is not found
        raise:  NullArgument - ``assessment_offered_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_offered_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        assessment_offered = lookup_session.get_assessment_offered(assessment_offered_id)
        id_list = []
        for idstr in assessment_offered._my_map['assignedBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_banks_by_assessment_offered(self, assessment_offered_id):
        """Gets the list of ``Banks`` mapped to an ``AssessmentOffered``.

        arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        return: (osid.assessment.BankList) - list of banks
        raise:  NotFound - ``assessment_offered_id`` is not found
        raise:  NullArgument - ``assessment_offered_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_banks_by_ids(
            self.get_bank_ids_by_assessment_offered(assessment_offered_id))


class AssessmentOfferedBankAssignmentSession(abc_assessment_sessions.AssessmentOfferedBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``AssessmentOffered`` objects to ``Banks``.

    An ``AssessmentOffered`` may map to multiple ``Banks`` and removing
    the last reference to an ``AssessmentOffered`` is the equivalent of
    deleting it. Each ``Bank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``AssessmentOffered`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'assessment.AssessmentOfferedBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Bank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_assessments_offered(self):
        """Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_assign_assessments_offered_to_bank(self, bank_id):
        """Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given banks node in which any assessment offered can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        banks = lookup_session.get_banks()
        id_list = []
        for bank in banks:
            id_list.append(bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_bank_ids_for_assessment_offered(self, bank_id, assessment_offered_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment offered can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` or ``assessment_offered_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_bank_ids(bank_id)

    @utilities.arguments_not_none
    def assign_assessment_offered_to_bank(self, assessment_offered_id, bank_id):
        """Adds an existing ``AssessmentOffered`` to a ``Bank``.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  AlreadyExists - ``assessment_offered_id`` is already
                assigned to ``bank_id``
        raise:  NotFound - ``assessment_offered_id`` or ``bank_id`` not
                found
        raise:  NullArgument - ``assessment_offered_id`` or ``bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._assign_object_to_catalog(assessment_offered_id, bank_id)

    @utilities.arguments_not_none
    def unassign_assessment_offered_from_bank(self, assessment_offered_id, bank_id):
        """Removes an ``AssessmentOffered`` from a ``Bank``.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  NotFound - ``assessment_offered_id`` or ``bank_id`` not
                found or ``assessment_offered_id`` not assigned to
                ``bank_id``
        raise:  NullArgument - ``assessment_offered_id`` or ``bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(assessment_offered_id, bank_id)

    @utilities.arguments_not_none
    def reassign_assessment_offered_to_billing(self, assessment_offered_id, from_bank_id, to_bank_id):
        """Moves an ``AssessmentOffered`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        raise:  NotFound - ``assessment_offered_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_offered_id``
                not mapped to ``from_bank_id``
        raise:  NullArgument - ``assessment_offered_id, from_bank_id,``
                or ``to_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class AssessmentTakenLookupSession(abc_assessment_sessions.AssessmentTakenLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving assessments taken."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_lookup_assessments_taken(self):
        """Tests if this user can perform ``AssessmentTaken`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_assessment_taken_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_assessment_taken_view(self):
        """A complete view of the ``AssessmentTaken`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_assessment_taken(self, assessment_taken_id):
        """Gets the ``AssessmentTaken`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentTaken`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentTaken`` and
        retained for compatibility.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.AssessmentTaken) - the assessment taken
        raise:  NotFound - ``assessment_taken_id`` not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(assessment_taken_id, 'assessment').get_identifier())},
                 **self._view_filter()))
        return objects.AssessmentTaken(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_taken_by_ids(self, assessment_taken_ids):
        """Gets an ``AssessmentTakenList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentTaken`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        arg:    assessment_taken_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``assessment_taken_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        object_id_list = []
        for i in assessment_taken_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'assessment').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.AssessmentTakenList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_taken_by_genus_type(self, assessment_taken_genus_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type`` which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    assessment_taken_genus_type (osid.type.Type): an
                assessment taken genus type
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken list``
        raise:  NullArgument - ``assessment_taken_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(assessment_taken_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentTakenList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_taken_by_parent_genus_type(self, assessment_taken_genus_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments taken that are accessible
        through this session.

        arg:    assessment_taken_genus_type (osid.type.Type): an
                assessment taken genus type
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken list``
        raise:  NullArgument - ``assessment_taken_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentTakenList([])

    @utilities.arguments_not_none
    def get_assessments_taken_by_record_type(self, assessment_taken_record_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        arg:    assessment_taken_record_type (osid.type.Type): an
                assessment taken record type
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  NullArgument - ``assessment_taken_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentTakenList([])

    @utilities.arguments_not_none
    def get_assessments_taken_by_date(self, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        arg:    from (osid.calendaring.DateTime): start date
        arg:    to (osid.calendaring.DateTime): end date
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_for_taker(self, resource_id):
        """Gets an ``AssessmentTakenList`` for the given resource.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_by_date_for_taker(self, resource_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        arg:    from (osid.calendaring.DateTime): start date
        arg:    to (osid.calendaring.DateTime): end date
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, from`` or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_for_assessment(self, assessment_id):
        """Gets an ``AssessmentTakenList`` for the given assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentOffered',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentId': str(assessment_id)},
                 **self._view_filter())).sort('_id', DESCENDING)
        assessments_offered = objects.AssessmentOfferedList(
            result,
            runtime=self._runtime)

        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        ao_ids = []
        for assessment_offered in assessments_offered:
            ao_ids.append(str(assessment_offered.get_id()))

        result = collection.find(
            dict({'assessmentOfferedId': {'$in': ao_ids}},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentTakenList(result,
                                           runtime=self._runtime,
                                           proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_taken_by_date_for_assessment(self, assessment_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        arg:    from (osid.calendaring.DateTime): start date
        arg:    to (osid.calendaring.DateTime): end date
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``assessment_id, from`` or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_for_taker_and_assessment(self, resource_id, assessment_id):
        """Gets an ``AssessmentTakenList`` for the given resource and assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  NullArgument - ``resource_id`` or ``assessment_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_by_date_for_taker_and_assessment(self, resource_id, assessment_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource and assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        arg:    from (osid.calendaring.DateTime): start date
        arg:    to (osid.calendaring.DateTime): end date
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, assessment_id, from`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Gets an ``AssessmentTakenList`` by the given assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  NullArgument - ``assessment_offered_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentOfferedId': str(assessment_offered_id)},
                 **self._view_filter()))
        return objects.AssessmentTakenList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessments_taken_by_date_for_assessment_offered(self, assessment_offered_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        arg:    from (osid.calendaring.DateTime): start date
        arg:    to (osid.calendaring.DateTime): end date
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``assessment_offered_id, from,`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessments_taken_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id):
        """Gets an ``AssessmentTakenList`` for the given resource and assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  NullArgument - ``resource_id`` or
                ``assessmen_offeredt_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)

        am = self._get_provider_manager('ASSESSMENT')
        aols = am.get_assessment_offered_lookup_session(proxy=self._proxy)
        aols.use_federated_bank_view()
        offered = aols.get_assessment_offered(assessment_offered_id)
        try:
            deadline = offered.get_deadline()
            nowutc = DateTime.utcnow()
            if nowutc > deadline:
                raise errors.PermissionDenied('you are passed the deadline for the offered')
        except errors.IllegalState:
            # no deadline set
            pass

        result = collection.find(
            dict({'assessmentOfferedId': str(assessment_offered_id),
                  'takingAgentId': str(resource_id)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentTakenList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessments_taken_by_date_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource and assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        arg:    from (osid.calendaring.DateTime): start date
        arg:    to (osid.calendaring.DateTime): end date
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, assessment_offered_id,
                from,`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_assessments_taken(self):
        """Gets all ``AssessmentTaken`` elements.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        return: (osid.assessment.AssessmentTakenList) - a list of
                ``AssessmentTaken`` elements
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.AssessmentTakenList(result, runtime=self._runtime, proxy=self._proxy)

    assessments_taken = property(fget=get_assessments_taken)


class AssessmentTakenQuerySession(abc_assessment_sessions.AssessmentTakenQuerySession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_search_assessments_taken(self):
        """Tests if this user can perform ``AssessmentTaken`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessments taken in banks which
        are children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_assessment_taken_query(self):
        """Gets an assessment taken query.

        return: (osid.assessment.AssessmentTakenQuery) - the assessment
                taken query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.AssessmentTakenQuery(runtime=self._runtime)

    assessment_taken_query = property(fget=get_assessment_taken_query)

    @utilities.arguments_not_none
    def get_assessments_taken_by_query(self, assessment_taken_query):
        """Gets a list of ``AssessmentTaken`` elements matching the given assessment taken query.

        arg:    assessment_taken_query
                (osid.assessment.AssessmentTakenQuery): the assessment
                taken query
        return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTakenList``
        raise:  NullArgument - ``assessment_taken_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_taken_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in assessment_taken_query._query_terms:
            if '$in' in assessment_taken_query._query_terms[term] and '$nin' in assessment_taken_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': assessment_taken_query._query_terms[term]['$in']}},
                             {term: {'$nin': assessment_taken_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: assessment_taken_query._query_terms[term]})
        for term in assessment_taken_query._keyword_terms:
            or_list.append({term: assessment_taken_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('assessment',
                                             collection='AssessmentTaken',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.AssessmentTakenList(result, runtime=self._runtime, proxy=self._proxy)


class AssessmentTakenAdminSession(abc_assessment_sessions.AssessmentTakenAdminSession, osid_sessions.OsidSession):
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
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_create_assessments_taken(self):
        """Tests if this user can create ``AssessmentTaken`` objects.

        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentTaken`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_assessment_taken_with_record_types(self, assessment_taken_record_types):
        """Tests if this user can create a single ``AssessmentTaken`` using the desired record types.

        While ``AssessmentManager.getAssessmentTakenRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentTaken``. Providing an empty array tests if an
        ``AssessmentTaken`` can be created with no records.

        arg:    assessment_taken_record_types (osid.type.Type[]): array
                of assessment taken record types
        return: (boolean) - ``true`` if ``AssessmentTaken`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``assessment_taken_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_taken_form_for_create(self, assessment_offered_id, assessment_taken_record_types):
        """Gets the assessment taken form for creating new assessments taken.

        A new form should be requested for each create transaction.

        arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                related ``AssessmentOffered``
        arg:    assessment_taken_record_types (osid.type.Type[]): array
                of assessment taken record types to be included in the
                create operation or an empty list if none
        return: (osid.assessment.AssessmentTakenForm) - the assessment
                taken form
        raise:  NotFound - ``assessment_offered_id`` is not found
        raise:  NullArgument - ``assessment_offered_id`` or
                ``assessment_taken_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(assessment_offered_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in assessment_taken_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')

        am = self._get_provider_manager('ASSESSMENT')
        aols = am.get_assessment_offered_lookup_session(proxy=self._proxy)
        aols.use_federated_bank_view()
        offered = aols.get_assessment_offered(assessment_offered_id)
        try:
            deadline = offered.get_deadline()
            nowutc = DateTime.utcnow()
            if nowutc > deadline:
                raise errors.PermissionDenied('you are passed the deadline for the offered')
        except errors.IllegalState:
            # no deadline set
            pass

        if assessment_taken_record_types == []:
            # WHY are we passing bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.AssessmentTakenForm(
                bank_id=self._catalog_id,
                assessment_offered_id=assessment_offered_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.AssessmentTakenForm(
                bank_id=self._catalog_id,
                record_types=assessment_taken_record_types,
                assessment_offered_id=assessment_offered_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_assessment_taken(self, assessment_taken_form):
        """Creates a new ``AssessmentTaken``.

        arg:    assessment_taken_form
                (osid.assessment.AssessmentTakenForm): the form for this
                ``AssessmentTaken``
        return: (osid.assessment.AssessmentTaken) - the new
                ``AssessmentTaken``
        raise:  IllegalState - ``assessment_taken_form`` already used in
                a create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``assessment_taken_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_offered_form`` did not
                originate from
                ``get_assessment_taken_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # This impl differs from the usual create_osid_object method in that it
        # sets an agent id and default display name based on the underlying Assessment
        # and checks for exceeding max attempts...
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        if not isinstance(assessment_taken_form, ABCAssessmentTakenForm):
            raise errors.InvalidArgument('argument type is not an AssessmentTakenForm')
        if assessment_taken_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentForm is for update only, not create')
        try:
            if self._forms[assessment_taken_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('assessment_taken_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('assessment_taken_form did not originate from this session')
        if not assessment_taken_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')

        # ...here:
        assessment_offered_id = Id(assessment_taken_form._my_map['assessmentOfferedId'])
        aols = AssessmentOfferedLookupSession(
            catalog_id=None, runtime=self._runtime)
        aols.use_federated_bank_view()
        assessment_offered = aols.get_assessment_offered(assessment_offered_id)
        try:
            if assessment_offered.has_max_attempts():
                max_attempts = assessment_offered.get_max_attempts()
                num_takens = collection.find({'$and': [{'assessmentOfferedId': str(assessment_offered.get_id())},
                                                       {'takingAgentId': str(self.get_effective_agent_id())},
                                                       {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]}).count()
                if num_takens >= max_attempts:
                    raise errors.PermissionDenied('exceeded max attempts')
        except AttributeError:
            pass
        assessment_taken_form._my_map['takingAgentId'] = str(self.get_effective_agent_id())

        insert_result = collection.insert_one(assessment_taken_form._my_map)
        self._forms[assessment_taken_form.get_id().get_identifier()] = CREATED
        return objects.AssessmentTaken(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

    def can_update_assessments_taken(self):
        """Tests if this user can update ``AssessmentTaken`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentTaken``
                modification is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_taken_form_for_update(self, assessment_taken_id):
        """Gets the assessment taken form for updating an existing assessment taken.

        A new assessment taken form should be requested for each update
        transaction.

        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        return: (osid.assessment.AssessmentTakenForm) - the assessment
                taken form
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        if not isinstance(assessment_taken_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (assessment_taken_id.get_identifier_namespace() != 'assessment.AssessmentTaken' or
                assessment_taken_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(assessment_taken_id.get_identifier())})

        obj_form = objects.AssessmentTakenForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_assessment_taken(self, assessment_taken_form):
        """Updates an existing assessment taken.

        arg:    assessment_taken_form
                (osid.assessment.AssessmentTakenForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``assessment_taken_form`` already used in
                an update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``assessment_taken_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_offered_form`` did not
                originate from
                ``get_assessment_taken_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        if not isinstance(assessment_taken_form, ABCAssessmentTakenForm):
            raise errors.InvalidArgument('argument type is not an AssessmentTakenForm')
        if not assessment_taken_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentTakenForm is for update only, not create')
        try:
            if self._forms[assessment_taken_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('assessment_taken_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('assessment_taken_form did not originate from this session')
        if not assessment_taken_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(assessment_taken_form._my_map)

        self._forms[assessment_taken_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.AssessmentTaken(
            osid_object_map=assessment_taken_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_assessments_taken(self):
        """Tests if this user can delete ``AssessmentsTaken``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``AssessmentTaken`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_assessment_taken(self, assessment_taken_id):
        """Deletes an ``AssessmentTaken``.

        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken`` to remove
        raise:  NotFound - ``assessment_taken_id`` not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        if not isinstance(assessment_taken_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        assessment_taken_map = collection.find_one(
            dict({'_id': ObjectId(assessment_taken_id.get_identifier())},
                 **self._view_filter()))

        objects.AssessmentTaken(osid_object_map=assessment_taken_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(assessment_taken_id.get_identifier())})

    def can_manage_assessment_taken_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentsTaken``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentTaken`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_assessment_taken(self, assessment_taken_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentTaken`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentTaken`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment taken, it is
        reassigned to the given assessment taken ``Id``.

        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of an
                ``AssessmentTaken``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``assessment_taken_id`` not found
        raise:  NullArgument - ``assessment_taken_id`` or ``alias_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=assessment_taken_id, equivalent_id=alias_id)


class AssessmentTakenBankSession(abc_assessment_sessions.AssessmentTakenBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``AssessmentTaken`` to ``Bank`` mappings.

    An ``AssessmentTaken`` may appear in multiple ``Banks``. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'assessment.AssessmentTakenBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_assessment_taken_bank_mappings(self):
        """Tests if this user can perform lookups of assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bank_view(self):
        """A complete view of the ``AssessmentTaken`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_assessment_taken_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentTaken``  ``Ids`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of related assessment taken
                ``Ids``
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for assessment_taken in self.get_assessments_taken_by_bank(bank_id):
            id_list.append(assessment_taken.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessments_taken_by_bank(self, bank_id):
        """Gets the list of ``AssessmentTakens`` associated with a ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.assessment.AssessmentTakenList) - list of related
                assessments taken
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_taken_lookup_session_for_bank(bank_id, proxy=self._proxy)
        lookup_session.use_isolated_bank_view()
        return lookup_session.get_assessments_taken()

    @utilities.arguments_not_none
    def get_assessment_taken_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentTaken Ids`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for assessment_taken in self.get_assessments_taken_by_banks(bank_ids):
            id_list.append(assessment_taken.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessments_taken_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentTaken`` objects corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.assessment.AssessmentTakenList) - list of
                assessments taken
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        assessment_taken_list = []
        for bank_id in bank_ids:
            assessment_taken_list += list(
                self.get_assessments_taken_by_bank(bank_id))
        return objects.AssessmentTakenList(assessment_taken_list)

    @utilities.arguments_not_none
    def get_bank_ids_by_assessment_taken(self, assessment_taken_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentTaken``.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of an
                ``AssessmentTaken``
        return: (osid.id.IdList) - list of bank ``Ids``
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_taken_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        assessment_taken = lookup_session.get_assessment_taken(assessment_taken_id)
        id_list = []
        for idstr in assessment_taken._my_map['assignedBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_banks_by_assessment_taken(self, assessment_taken_id):
        """Gets the list of ``Banks`` mapped to an ``AssessmentTaken``.

        arg:    assessment_taken_id (osid.id.Id): ``Id`` of an
                ``AssessmentTaken``
        return: (osid.assessment.BankList) - list of banks
        raise:  NotFound - ``assessment_taken_id`` is not found
        raise:  NullArgument - ``assessment_taken_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_banks_by_ids(
            self.get_bank_ids_by_assessment_taken(assessment_taken_id))


class AssessmentTakenBankAssignmentSession(abc_assessment_sessions.AssessmentTakenBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``AssessmentTaken`` objects to ``Banks``.

    An ``AssessmentTaken`` may map to multiple ``Banks`` and removing
    the last reference to an ``AssessmentTaken`` is the equivalent of
    deleting it. Each ``Bank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``AssessmentTaken`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'assessment.AssessmentTakenBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Bank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_assessments_taken(self):
        """Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_assign_assessments_taken_to_bank(self, bank_id):
        """Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given banks node in which any assessment taken can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        banks = lookup_session.get_banks()
        id_list = []
        for bank in banks:
            id_list.append(bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_bank_ids_for_assessment_taken(self, bank_id, assessment_taken_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment taken can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` or ``assessment_taken_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_bank_ids(bank_id)

    @utilities.arguments_not_none
    def assign_assessment_taken_to_bank(self, assessment_taken_id, bank_id):
        """Adds an existing ``AssessmentTaken`` to a ``Bank``.

        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  AlreadyExists - ``assessment_taken_id`` is already
                assigned to ``bank_id``
        raise:  NotFound - ``assessment_taken_id`` or ``bank_id`` not
                found
        raise:  NullArgument - ``assessment_taken_id`` or ``bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._assign_object_to_catalog(assessment_taken_id, bank_id)

    @utilities.arguments_not_none
    def unassign_assessment_taken_from_bank(self, assessment_taken_id, bank_id):
        """Removes an ``AssessmentTaken`` from a ``Bank``.

        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  NotFound - ``assessment_taken_id`` or ``bank_id`` not
                found or ``assessment_taken_id`` not assigned to
                ``bank_id``
        raise:  NullArgument - ``assessment_taken_id`` or ``bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(assessment_taken_id, bank_id)

    @utilities.arguments_not_none
    def reassign_assessment_taken_to_billing(self, assessment_taken_id, from_bank_id, to_bank_id):
        """Moves an ``AssessmentTaken`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        raise:  NotFound - ``assessment_taken_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_taken_id`` not
                mapped to ``from_bank_id``
        raise:  NullArgument - ``assessment_taken_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BankLookupSession(abc_assessment_sessions.BankLookupSession, osid_sessions.OsidSession):
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
    _session_namespace = 'assessment.BankLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_banks(self):
        """Tests if this user can perform ``Bank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.can_lookup_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_lookup_catalogs()
        return True

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bank_view(self):
        """A complete view of the ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_bank(self, bank_id):
        """Gets the ``Bank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bank`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bank`` and retained for compatibility.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.assessment.Bank) - the bank
        raise:  NotFound - ``bank_id`` not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=bank_id)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if bank_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.Bank, cat_name='Bank')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(bank_id, 'assessment').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Bank.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(bank_id, 'assessment', 'Bank')

        return objects.Bank(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_banks_by_ids(self, bank_ids):
        """Gets a ``BankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the banks
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bank`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        arg:    bank_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.assessment.BankList) - the returned ``Bank`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Bank() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=bank_ids)
        catalog_id_list = []
        for i in bank_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.BankList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_banks_by_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` which does not include banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        arg:    bank_genus_type (osid.type.Type): a bank genus type
        return: (osid.assessment.BankList) - the returned ``Bank`` list
        raise:  NullArgument - ``bank_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=bank_genus_type)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(bank_genus_type)}).sort('_id', DESCENDING)

        return objects.BankList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_banks_by_parent_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` and include any additional banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        arg:    bank_genus_type (osid.type.Type): a bank genus type
        return: (osid.assessment.BankList) - the returned ``Bank`` list
        raise:  NullArgument - ``bank_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_banks_by_record_type(self, bank_record_type):
        """Gets a ``BankList`` containing the given bank record ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        arg:    bank_record_type (osid.type.Type): a bank record type
        return: (osid.assessment.BankList) - the returned ``Bank`` list
        raise:  NullArgument - ``bank_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_banks_by_provider(self, resource_id):
        """Gets a ``BankList`` from the given provider ````.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.assessment.BankList) - the returned ``Bank`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_banks(self):
        """Gets all ``Banks``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        return: (osid.assessment.BankList) - a ``BankList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.BankList(result, runtime=self._runtime, proxy=self._proxy)

    banks = property(fget=get_banks)


class BankQuerySession(abc_assessment_sessions.BankQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Bank`` objects.

    The search query is constructed using the ``BankQuery``.

    Banks may have aquery record indicated by their respective record
    types. The query record is accessed via the ``BankQuery``.

    """
    _session_namespace = 'assessment.BankQuerySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_query_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_search_banks(self):
        """Tests if this user can perform ``Bank`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.can_search_bins_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def get_bank_query(self):
        """Gets a bank query.

        return: (osid.assessment.BankQuery) - a bank query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.get_bin_query_template
        return queries.BankQuery(runtime=self._runtime)

    bank_query = property(fget=get_bank_query)

    @utilities.arguments_not_none
    def get_banks_by_query(self, bank_query):
        """Gets a list of ``Bank`` objects matching the given bank query.

        arg:    bank_query (osid.assessment.BankQuery): the bank query
        return: (osid.assessment.BankList) - the returned ``BankList``
        raise:  NullArgument - ``bank_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``bank_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_query(bank_query)
        query_terms = dict(bank_query._query_terms)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        result = collection.find(query_terms).sort('_id', DESCENDING)

        return objects.BankList(result, runtime=self._runtime)


class BankAdminSession(abc_assessment_sessions.BankAdminSession, osid_sessions.OsidSession):
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
    _session_namespace = 'assessment.BankAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_banks(self):
        """Tests if this user can create ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Bank`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs()
        return True

    @utilities.arguments_not_none
    def can_create_bank_with_record_types(self, bank_record_types):
        """Tests if this user can create a single ``Bank`` using the desired record types.

        While ``AssessmentManager.getBankRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bank``.
        Providing an empty array tests if a ``Bank`` can be created with
        no records.

        arg:    bank_record_types (osid.type.Type[]): array of bank
                record types
        return: (boolean) - ``true`` if ``Bank`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``bank_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=bank_record_types)
        return True

    @utilities.arguments_not_none
    def get_bank_form_for_create(self, bank_record_types):
        """Gets the bank form for creating new banks.

        A new form should be requested for each create transaction.

        arg:    bank_record_types (osid.type.Type[]): array of bank
                record types to be included in the create operation or
                an empty list if none
        return: (osid.assessment.BankForm) - the bank form
        raise:  NullArgument - ``bank_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=bank_record_types)
        for arg in bank_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if bank_record_types == []:
            result = objects.BankForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.BankForm(
                record_types=bank_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_bank(self, bank_form):
        """Creates a new ``Bank``.

        arg:    bank_form (osid.assessment.BankForm): the form for this
                ``Bank``
        return: (osid.assessment.Bank) - the new ``Bank``
        raise:  IllegalState - ``bank_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``bank_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``bank_form`` did not originate from
                ``get_bank_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=bank_form)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        if not isinstance(bank_form, ABCBankForm):
            raise errors.InvalidArgument('argument type is not an BankForm')
        if bank_form.is_for_update():
            raise errors.InvalidArgument('the BankForm is for update only, not create')
        try:
            if self._forms[bank_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('bank_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('bank_form did not originate from this session')
        if not bank_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(bank_form._my_map)

        self._forms[bank_form.get_id().get_identifier()] = CREATED
        result = objects.Bank(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_banks(self):
        """Tests if this user can update ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Bank`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_update_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_update_catalogs()
        return True

    @utilities.arguments_not_none
    def get_bank_form_for_update(self, bank_id):
        """Gets the bank form for updating an existing bank.

        A new bank form should be requested for each update transaction.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.BankForm) - the bank form
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=bank_id)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        if not isinstance(bank_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(bank_id.get_identifier())})

        cat_form = objects.BankForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_bank(self, bank_form):
        """Updates an existing bank.

        arg:    bank_form (osid.assessment.BankForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``bank_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``bank_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``bank_form`` did not originate from
                ``get_bank_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=bank_form)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        if not isinstance(bank_form, ABCBankForm):
            raise errors.InvalidArgument('argument type is not an BankForm')
        if not bank_form.is_for_update():
            raise errors.InvalidArgument('the BankForm is for update only, not create')
        try:
            if self._forms[bank_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('bank_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('bank_form did not originate from this session')
        if not bank_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(bank_form._my_map)  # save is deprecated - change to replace_one

        self._forms[bank_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Bank(osid_object_map=bank_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_banks(self):
        """Tests if this user can delete banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Bank`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_delete_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_delete_catalogs()
        return True

    @utilities.arguments_not_none
    def delete_bank(self, bank_id):
        """Deletes a ``Bank``.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank`` to
                remove
        raise:  NotFound - ``bank_id`` not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=bank_id)
        collection = JSONClientValidated('assessment',
                                         collection='Bank',
                                         runtime=self._runtime)
        if not isinstance(bank_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['Item', 'Assessment', 'AssessmentOffered', 'AssessmentTaken', 'Bank']:
            obj_collection = JSONClientValidated('assessment',
                                                 collection=object_catalog,
                                                 runtime=self._runtime)
            if obj_collection.find({'assignedBankIds': {'$in': [str(bank_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(bank_id.get_identifier())})

    def can_manage_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Bank`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_bank(self, bank_id, alias_id):
        """Adds an ``Id`` to a ``Bank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bank`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another bank, it is reassigned to the
        given bank ``Id``.

        arg:    bank_id (osid.id.Id): the ``Id`` of a ``Bank``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``bank_id`` not found
        raise:  NullArgument - ``bank_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=bank_id, alias_id=alias_id)
        self._alias_id(primary_id=bank_id, equivalent_id=alias_id)


class BankHierarchySession(abc_assessment_sessions.BankHierarchySession, osid_sessions.OsidSession):
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
    _session_namespace = 'assessment.BankHierarchySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchySession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_traversal_session_for_hierarchy(
                Id(authority='ASSESSMENT',
                   namespace='CATALOG',
                   identifier='BANK'),
                proxy=self._proxy)

    def get_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_access_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_access_catalog_hierarchy()
        return True

    def use_comparative_bank_view(self):
        """The returns from the bank methods may omit or translate elements based on this session, such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    def get_root_bank_ids(self):
        """Gets the root bank ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root bank ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalog_ids()
        return self._hierarchy_session.get_roots()

    root_bank_ids = property(fget=get_root_bank_ids)

    def get_root_banks(self):
        """Gets the root banks in this bank hierarchy.

        return: (osid.assessment.BankList) - the root banks
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalogs()
        return BankLookupSession(
            self._proxy,
            self._runtime).get_banks_by_ids(list(self.get_root_bank_ids()))

    root_banks = property(fget=get_root_banks)

    @utilities.arguments_not_none
    def has_parent_banks(self, bank_id):
        """Tests if the ``Bank`` has any parents.

        arg:    bank_id (osid.id.Id): a bank ``Id``
        return: (boolean) - ``true`` if the bank has parents, ``false``
                otherwise
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_parent_catalogs(catalog_id=bank_id)
        return self._hierarchy_session.has_parents(id_=bank_id)

    @utilities.arguments_not_none
    def is_parent_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a direct parent of a bank.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``bank_id,``  ``false`` otherwise
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``id`` or ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_parent_of_catalog(id_=id_, catalog_id=bank_id)
        return self._hierarchy_session.is_parent(id_=bank_id, parent_id=id_)

    @utilities.arguments_not_none
    def get_parent_bank_ids(self, bank_id):
        """Gets the parent ``Ids`` of the given bank.

        arg:    bank_id (osid.id.Id): a bank ``Id``
        return: (osid.id.IdList) - the parent ``Ids`` of the bank
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalog_ids(catalog_id=bank_id)
        return self._hierarchy_session.get_parents(id_=bank_id)

    @utilities.arguments_not_none
    def get_parent_banks(self, bank_id):
        """Gets the parents of the given bank.

        arg:    bank_id (osid.id.Id): a bank ``Id``
        return: (osid.assessment.BankList) - the parents of the bank
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalogs(catalog_id=bank_id)
        return BankLookupSession(
            self._proxy,
            self._runtime).get_banks_by_ids(
                list(self.get_parent_bank_ids(bank_id)))

    @utilities.arguments_not_none
    def is_ancestor_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is an ancestor of a bank.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``bank_id,``  ``false`` otherwise
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_ancestor_of_catalog(id_=id_, catalog_id=bank_id)
        return self._hierarchy_session.is_ancestor(id_=id_, ancestor_id=bank_id)

    @utilities.arguments_not_none
    def has_child_banks(self, bank_id):
        """Tests if a bank has any children.

        arg:    bank_id (osid.id.Id): a ``bank_id``
        return: (boolean) - ``true`` if the ``bank_id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_child_catalogs(catalog_id=bank_id)
        return self._hierarchy_session.has_children(id_=bank_id)

    @utilities.arguments_not_none
    def is_child_of_bank(self, id_, bank_id):
        """Tests if a bank is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``bank_id,``  ``false`` otherwise
        raise:  NotFound - ``bank_id`` not found
        raise:  NullArgument - ``bank_id`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_child_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_child_of_catalog(id_=id_, catalog_id=bank_id)
        return self._hierarchy_session.is_child(id_=bank_id, child_id=id_)

    @utilities.arguments_not_none
    def get_child_bank_ids(self, bank_id):
        """Gets the child ``Ids`` of the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the bank
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalog_ids(catalog_id=bank_id)
        return self._hierarchy_session.get_children(id_=bank_id)

    @utilities.arguments_not_none
    def get_child_banks(self, bank_id):
        """Gets the children of the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` to query
        return: (osid.assessment.BankList) - the children of the bank
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalogs(catalog_id=bank_id)
        return BankLookupSession(
            self._proxy,
            self._runtime).get_banks_by_ids(
                list(self.get_child_bank_ids(bank_id)))

    @utilities.arguments_not_none
    def is_descendant_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a descendant of a bank.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``bank_id,``  ``false`` otherwise
        raise:  NotFound - ``bank_id`` not found
        raise:  NullArgument - ``bank_id`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_descendant_of_catalog(id_=id_, catalog_id=bank_id)
        return self._hierarchy_session.is_descendant(id_=id_, descendant_id=bank_id)

    @utilities.arguments_not_none
    def get_bank_node_ids(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a bank node
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_node_ids(
                catalog_id=bank_id,
                ancestor_levels=ancestor_levels,
                descendant_levels=descendant_levels,
                include_siblings=include_siblings)
        return self._hierarchy_session.get_nodes(
            id_=bank_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)

    @utilities.arguments_not_none
    def get_bank_nodes(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.assessment.BankNode) - a bank node
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_nodes
        return objects.BankNode(self.get_bank_node_ids(
            bank_id=bank_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)._my_map, runtime=self._runtime, proxy=self._proxy)


class BankHierarchyDesignSession(abc_assessment_sessions.BankHierarchyDesignSession, osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Bank`` objects.

    Each node in the hierarchy is a unique ``Bank``.

    """
    _session_namespace = 'assessment.BankHierarchyDesignSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_design_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_design_session_for_hierarchy(
                Id(authority='ASSESSMENT',
                   namespace='CATALOG',
                   identifier='BANK'),
                proxy=self._proxy)

    def get_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_modify_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_modify_catalog_hierarchy()
        return True

    @utilities.arguments_not_none
    def add_root_bank(self, bank_id):
        """Adds a root bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        raise:  AlreadyExists - ``bank_id`` is already in hierarchy
        raise:  NotFound - ``bank_id`` not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_root_catalog(catalog_id=bank_id)
        return self._hierarchy_session.add_root(id_=bank_id)

    @utilities.arguments_not_none
    def remove_root_bank(self, bank_id):
        """Removes a root bank from this hierarchy.

        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        raise:  NotFound - ``bank_id`` not a parent of ``child_id``
        raise:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_root_catalog(catalog_id=bank_id)
        return self._hierarchy_session.remove_root(id_=bank_id)

    @utilities.arguments_not_none
    def add_child_bank(self, bank_id, child_id):
        """Adds a child to a bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``bank_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``bank_id`` or ``child_id`` not found
        raise:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_child_catalog(catalog_id=bank_id, child_id=child_id)
        return self._hierarchy_session.add_child(id_=bank_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_bank(self, bank_id, child_id):
        """Removes a child from a bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``bank_id`` not parent of ``child_id``
        raise:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalog(catalog_id=bank_id, child_id=child_id)
        return self._hierarchy_session.remove_child(id_=bank_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_banks(self, bank_id):
        """Removes all children from a bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        raise:  NotFound - ``bank_id`` is not in hierarchy
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalogs(catalog_id=bank_id)
        return self._hierarchy_session.remove_children(id_=bank_id)
